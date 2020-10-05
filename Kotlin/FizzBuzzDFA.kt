// Small implementation of FizzBuzz as a deterministic finite automaton with generic states and alphabet
// You can run the code at the Kotlin Playground: https://pl.kotl.in/zTjBA9KYf
// Author: @tobi6112


enum class State {
    NUMBER, CHECK_NUMBER, FIZZ, BUZZ, FIZZBUZZ, START, END
}

class FizzBuzzDFA<T, R>(val alphabet: Iterable<R>, val transition: (T, R) -> T, val endStates: Set<T>, val startState: T) {
    private var currentState = startState
    private var currentValue = alphabet.first()

    fun startAutomaton() {
        alphabet.forEach {
            currentValue = it
            currentState = transition(currentState, currentValue)
            while(!endStates.contains(currentState)) {
                currentState = transition(currentState, currentValue)
            }
        }
    }
}

val transition : (State, Int) -> State = { state: State, value: Int ->
    when(state) {
        State.NUMBER -> {
            println(value)
            State.END
        }
        State.FIZZ -> {
            println("Fizz")
            State.END
        }
        State.BUZZ -> {
            println("Buzz")
            State.END
        }
        State.FIZZBUZZ -> {
            println("FizzBuzz")
            State.END
        }
        State.CHECK_NUMBER -> {
            when {
                value % 15 == 0 -> State.FIZZBUZZ
                value % 5 == 0 -> State.BUZZ
                value % 3 == 0 -> State.FIZZ
                else -> State.NUMBER
            }
        }
        State.START -> State.CHECK_NUMBER
        State.END -> State.CHECK_NUMBER
    }
}

fun main() {
    val dfa = FizzBuzzDFA((1..100), transition, setOf(State.END), State.START)
    dfa.startAutomaton()
}