// Checks if `i % n` is equal to 0
// Returns `true` if it is equal to 0
// Returns `false` if it is not equal to 0
fn check_sound(i: isize, n: isize) -> bool {
    match i % n {
        0 => true,
        _ => false,
    }
}

fn main() {
    // A Vec<(String, isize)> of the sound/int pairs
    // Can add new pairs of sound/int to check against
    let sounds: Vec<(String, isize)> = vec![("Fizz".to_string(), 3), ("Buzz".to_string(), 5)];

    // Set max of range
    let max: isize = 100;

    // iterate from 1 to max
    // adding 1 becase x..y is exlcusive of y
    for i in 1..(max + 1) {
        // Set the output to blank line on each iteration
        let mut output = String::new();

        // Iterate through all sounds in `sounds`
        for sound in &sounds {
            // Match against `check_sound()`
            // If `true`, concat. the "sound" to output
            // If `false`, concat. an empty string
            output = match check_sound(i, sound.1) {
                true => [output, sound.0.to_string()].join(""),
                false => [output, "".to_string()].join(""),
            }
        }

        // Match against output
        // If output is an empty string, print `i`
        // Else, print output
        match output.as_ref() {
            "" => println!("{}", i),
            _ => println!("{}", output),
        }
    }
}
