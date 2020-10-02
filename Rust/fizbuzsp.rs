// This is a folded Iterative Version for Fizz Buzz in Rustlang. It is buffered with a single string Allocation (write!)
// @author: Srinjana 
// compile by rustc filename.rs
// run by .\filename.exe in Windows

use std::fmt::Write;
 
fn fizzbuzz() -> String {
    (1..101).fold(String::new(), |mut output, x| {
        let fizz = if x % 3 == 0 { "Fizz" } else { "" };
        let buzz = if x % 5 == 0 { "Buzz" } else { "" };
        if fizz.len() + buzz.len() != 0 {
            output + fizz + buzz + "\n"
        } else {
            write!(&mut output, "{}", x).unwrap();
            output + "\n"
        }
    })
}
 
pub fn main() {
    println!("{}", fizzbuzz());
}