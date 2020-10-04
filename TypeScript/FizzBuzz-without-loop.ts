// FizzBuzz without loop, only timeout very 100ms
// Author: @EhrenfeldN

class FizzBuzz {

public index: number = 1;
public intervale: any = 0;

    constructor() {
        this.intervale = setInterval( () => {
            if (this.index % 3 === 0 && this.index % 5 === 0) this.printResult("FizzBuzz");
            else if (this.index % 3 === 0) this.printResult("Fizz");
            else if (this.index % 5 === 0) this.printResult("Buzz");
            else this.printResult(this.index);
        }, 100);
    }

    public printResult(text_to_display: string | number): void {
        console.log(text_to_display);
        this.index++;
        if (this.index > 100) clearInterval(this.intervale);
    }

}
new FizzBuzz();
