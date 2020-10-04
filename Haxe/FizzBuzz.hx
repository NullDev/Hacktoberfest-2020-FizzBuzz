// This is FizzBuzz in Haxe
// Haxe is a bit of a legend in game development. Doesn't see much use, syntax is just OK, but it's really amazing because the compiler transpiles to a wide variety of targets
class FizzBuzz {
    static function main() {
        for (i in (1...100)) {
            if (i % 15 == 0) {
                trace("FizzBuzz");
            } else if (i % 3 == 0) {
                trace("Fizz");
            } else if (i % 5 == 0) {
                trace("Buzz");
            } else {
                trace(i);
            }
        }
    }
}