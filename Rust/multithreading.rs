// Ineffective but shows the idea
// Author: @dlemel8

use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let data: Vec<_> = (0..=100).map(|x| format!("{}", x)).collect();
    let shared_data = Arc::new(Mutex::new(data));

    let fizz_numbers = shared_data.clone();
    let fizz_thread = thread::spawn(move || {
        let mut fizz_numbers = fizz_numbers.lock().unwrap();
        let mut offset = 0;
        while offset < fizz_numbers.len() {
            fizz_numbers[offset] = match offset % 5 {
                0 => "FizzBuzz",
                _ => "Fizz"
            }.to_string();
            offset += 3;
        }
    });

    let buzz_numbers = shared_data.clone();
    let buzz_thread = thread::spawn(move || {
        let mut buzz_numbers = buzz_numbers.lock().unwrap();
        let mut offset = 0;
        while offset < buzz_numbers.len() {
            if offset % 3 != 0 {
                buzz_numbers[offset] = "Buzz".to_string();
            }
            offset += 5;
        }
    });

    fizz_thread.join().unwrap();
    buzz_thread.join().unwrap();

    let final_data = shared_data.lock().unwrap();
    final_data.iter().skip(1).for_each(|i| println!("{}", i))
}
