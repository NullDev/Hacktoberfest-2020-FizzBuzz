"""
Fizz Buzz Generator using Dictionary
Author: @fenilgandhi
# Using Dictionary, _ Shorthands & pure garbage packing code
"""

_ = {
    "01": "Fizz",
    "10": "Buzz",
    "00": "FizzBuzz"
}

def main():
    print(*(_.get(f"{bool(___%3)*1}{bool(___%5)*1}", ___) for ___ in range(1, 1000)), sep="\n")

if __name__ == "__main__":
    main()