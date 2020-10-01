use std::fmt::{self, Display, Formatter};

/// FizzBuzz game object that holds the current number.
#[derive(Debug)]
struct FizzBuzz {
    next: usize,
}

impl FizzBuzz {
    pub fn new(start: usize) -> Self {
        Self { next: start }
    }
}

impl Default for FizzBuzz {
    fn default() -> Self {
        Self::new(0)
    }
}

impl Iterator for FizzBuzz {
    type Item = FizzBuzzOutput;

    fn next(&mut self) -> Option<Self::Item> {
        // we implemented From<usize> for FizzBuzzOutput, so we can simply use `into`
        // to convert our number into our result.
        let result = self.next.into();
        self.next += 1;

        Some(result)
    }
}

/// FizzBuzz game output. Holds all possible output variants.
#[derive(Debug)]
enum FizzBuzzOutput {
    Fizz,
    Buzz,
    FizzBuzz,
    Other(usize),
}

impl From<usize> for FizzBuzzOutput {
    fn from(num: usize) -> Self {
        match num {
            n if n % 5 == 0 && n % 3 == 0 => Self::FizzBuzz,
            n if n % 3 == 0 => Self::Fizz,
            n if n % 5 == 0 => Self::Buzz,
            n => Self::Other(n),
        }
    }
}

impl Display for FizzBuzzOutput {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match self {
            Self::Other(n) => write!(f, "{}", n),
            Self::FizzBuzz => write!(f, "FizzBuzz"),
            Self::Fizz => write!(f, "Fizz"),
            Self::Buzz => write!(f, "Buzz"),
        }
    }
}

fn main() {
    // create the fizzbuzz game
    let fizzbuzz = FizzBuzz::default();

    // FizzBuzz implements iterator, so we can use a loop to iterate over the results.
    // We could also omit the `take` but this would result in an endless loop.
    for result in fizzbuzz.take(50) {
        // FizzBuzzOutput implements `Display`, so we can directly print it.
        println!("{}", result)
    }
}
