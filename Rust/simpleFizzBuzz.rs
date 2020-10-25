fn checker(num:isize, n:isize) -> bool {
    if num % n == 0 {
        true
    } else {
        false
    } 
}
fn main() {
let mut line = String::new()
    let mut startAt = 1;
    let max = 99;
    while start <= max {
        match (checker(startAt, 3), checker(startAt, 5)) {
            (true,true) => println!("FizzBuzz"),
            (true,false) => println!("Fizz"),
            (false,true) => println!("Buzz"),
            (false,false) => println!("{}", startAt)
        }

        startAt+=1;
    }
}
