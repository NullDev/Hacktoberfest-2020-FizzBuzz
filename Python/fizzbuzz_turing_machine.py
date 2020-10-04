#!/usr/bin/env python3
# FizzBuzz implementation using a deterministic single-tape turing machine
# Author: @lennart-k

from typing import Any, Dict, List, Optional, Set, Tuple
from collections import namedtuple

BLANK = "_"
LEFT = -1
RIGHT = 1
STAY = 0

WORDS = {
    "f": "Fizz",
    "b": "Buzz",
    "F": "FizzBuzz"
}

Transition = namedtuple(
    "Transition", ("read_letter", "write_letter", "move_direction", "next_state"))


class Tape:
    """A tape that extends indefinitely to the right"""
    content: List[str]

    def __init__(self, tape_input: str) -> None:
        self.content = list(tape_input)

    def _expand_to_index(self, index: int) -> None:
        if index < 0:
            raise Exception("Tape does not extend below 0")

        if index >= len(self.content):
            self.content += (index+1-len(self.content))*[BLANK]

    def read(self, index: int) -> str:
        self._expand_to_index(index)
        return self.content[index]

    def write(self, index: int, letter: str) -> None:
        self._expand_to_index(index)
        self.content[index] = letter

    def __len__(self) -> int:
        return len(self.content)

    def __getitem__(self, index: int) -> str:
        return self.read(index)

    def __setitem__(self, index: int, letter: str) -> None:
        self.write(index, letter)

    def __repr__(self) -> str:
        return f"<Tape {''.join(self.content)}>"


class DeterministicTuringMachine:
    """
    A deterministic turing machine with a single tape
    """
    input_alphabet: Set[str]
    tape_alphabet: Set[str]
    states: Set[Any]
    transitions: Dict[Any, Set[Transition]]
    start_state: Any
    accept_state: Any
    reject_state: Any
    tape: Tape

    current_state: Any
    headpos: int = 0

    def __init__(
        self,
        input_alphabet: Set[str],
        tape_alphabet: Set[str],
        states: Set[Any],
        transitions: Dict[Any, Set[Transition]],
        start_state: Any,
        accept_state: Any,
        reject_state: Any,
        tape_input: str
    ) -> None:
        self.input_alphabet = input_alphabet
        self.tape_alphabet = input_alphabet | tape_alphabet | {BLANK}
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = Tape(tape_input)
        self.current_state = start_state

    @property
    def current_letter(self) -> str:
        if self.headpos < 0:
            raise Exception("Head cannot move below 0")
        if self.headpos >= len(self.tape):
            return BLANK
        return self.tape[self.headpos]

    def step(self) -> Optional[bool]:
        transitions = set(filter(
            lambda transition: self.current_letter in transition.read_letter,
            self.transitions.get(self.current_state, set())))

        if not transitions:
            return False  # reject

        if len(transitions) >= 2:
            raise Exception(
                f"Turing machine is non-detereministic at {self.current_state}")

        transition: Transition = next(iter(transitions))

        self.tape[self.headpos] = transition.write_letter

        self.headpos += transition.move_direction

        if transition.next_state not in self.states:
            raise Exception(f"Invalid next_state {transition.next_state}")

        self.current_state = transition.next_state

        if self.current_state == self.accept_state:
            return True
        if self.current_state == self.reject_state:
            return False

    def run(self) -> Tuple[bool, str]:
        """Run step until we reach accept or reject"""
        while True:
            result = self.step()
            if isinstance(result, bool):
                return result, "".join(self.tape.content).rstrip(BLANK)


tm = DeterministicTuringMachine(
    input_alphabet={"1"},
    tape_alphabet={
        "f",  # Fizz
        "b",  # Buzz
        "F",  # FizzBuzz
        "X"   # START
    },
    states={"start", 0, 1, 2, 3, 4, 5, 6, 7, 8, "accept", "reject"},
    transitions={
        "start": {
            Transition("1", "X", RIGHT, 0),           # Mark first letter
            Transition(BLANK, BLANK, STAY, "accept")  # Empty input, done
        },
        0: {
            Transition("1", "1", RIGHT, 1),           # Second 1
            Transition(BLANK, BLANK, LEFT, 3),        # No more Fizz
        },
        1: {
            Transition("1", "f", RIGHT, 2),           # Third 1: Fizz!
            Transition(BLANK, BLANK, LEFT, 3),        # No more Fizz
        },
        2: {
            Transition("1", "1", RIGHT, 0),           # First 1
            Transition(BLANK, BLANK, LEFT, 3),        # No more Fizz
        },
        3: {
            Transition("1", "1", LEFT, 3),            # Go to start
            Transition("f", "f", LEFT, 3),            # Go to start
            Transition("X", "X", STAY, 4),            # We are at start
        },
        4: {
            Transition("X", "1", RIGHT, 5),           # Unmark start, first 1
            Transition("1", "1", RIGHT, 5),           # First 1
            Transition("f", "f", RIGHT, 5),           # First 1
            Transition(BLANK, BLANK, STAY, "accept"),  # No more Buzz
        },
        5: {
            Transition("1", "1", RIGHT, 6),           # Second 1
            Transition("f", "f", RIGHT, 6),           # Second 1
            Transition(BLANK, BLANK, STAY, "accept"),  # No more Buzz
        },
        6: {
            Transition("1", "1", RIGHT, 7),           # Third 1
            Transition("f", "f", RIGHT, 7),           # Third 1
            Transition(BLANK, BLANK, STAY, "accept"),  # No more Buzz
        },
        7: {
            Transition("1", "1", RIGHT, 8),           # Fourth 1
            Transition("f", "f", RIGHT, 8),           # Fourth 1
            Transition(BLANK, BLANK, STAY, "accept"),  # No more Buzz
        },
        8: {
            Transition("1", "b", RIGHT, 4),           # Buzz!
            Transition("f", "F", RIGHT, 4),           # FizzBuzz!
            Transition(BLANK, BLANK, STAY, "accept"),  # No more Buzz
        }
    },
    start_state="start",
    accept_state="accept",
    reject_state="reject",
    tape_input=100*"1"
)

result, tape = tm.run()

for index, letter in enumerate(tape):
    print(WORDS.get(letter, index+1))
