/**
 * This class contains several items to compile and run code for the chicken programming language:
 * - First there is the reference implementation for chicken.
 *   This function is highly unreadable and is very recursive.
 *   Due to the large amount of instructions executed for the fizzbuzz program, this function results in a maximum call stack size exceeded error.
 *
 * - Next it contains the class ChickenVM.
 *   This is a more efficient (and way more readable) implementation for the chicken programming language.
 *   This class requires an list of opcodes and an input string as constructor parameter.
 *   You can then call the function `execute` on the created instance of the vm to obtain the result of the code.
 *
 * - The next two things are the compile and decompile functions.
 *   As the names quite obviously state, these function are used to compile and decompile chicken.
 *   The compile function accepts a string and returns a list of opcodes (if the string was valid chicken).
 *   The decompile function accepts a list of opcodes and returns the corresponding chicken code.
 *
 * - The last function in this file 'runChicken' is a small helper function.
 *   The function accepts a chicken string together with an input string.
 *   It then compiles the chicken, creates a VM instance with the compiled chicken and the provided input.
 *   Finally it returns the result of the executed chicken.
 */


/**
 * The original chicken implementation
 * You can use this the same as the `runChicken` function
 */
function chicken(CHICKEN, Chicken) {
    Chicken &&( chicken. chicken =[,
        CHICKEN, CHICKEN = Chicken = chicken.
            $Chicken =-( CHICKEN ==( chicken.
            Chicken = Chicken ))], chicken.
        chicken [Chicken++] = chicken. chicken, chicken.
        CHICKEN = ++Chicken, chicken (--Chicken), chicken.
        $Chicken = ++Chicken, chicken. CHICKEN++ );
    Chicken = chicken. Chicken [chicken.
        $Chicken++ ]; chicken. Chicken = CHICKEN? Chicken?
        '\012'== Chicken? chicken (++ CHICKEN, chicken.
            chicken [++ chicken. CHICKEN ]=
            CHICKEN - CHICKEN ): Chicken
        ==' '|'\015'== Chicken ||
        (Chicken   )== "c" &  chicken. Chicken [chicken.
            $Chicken++ ]== "h" &  chicken. Chicken [chicken.
            $Chicken++ ]== "i" &  chicken. Chicken [chicken.
            $Chicken++ ]== "c" &  chicken. Chicken [chicken.
            $Chicken++ ]== "k" &  chicken. Chicken [chicken.
            $Chicken++ ]== "e" &  chicken. Chicken [chicken.
            $Chicken++ ]== "n"&&++chicken. chicken [chicken.
            CHICKEN]? chicken (CHICKEN)
            :[ "Error on line "+CHICKEN+": expected 'chicken'",
                chicken. CHICKEN = CHICKEN ++- CHICKEN ]:
        chicken. chicken :( CHICKEN = chicken.
        Chicken[chicken.CHICKEN], Chicken? (Chicken =

        --Chicken? --Chicken? --Chicken? --Chicken? --Chicken?
            --Chicken? --Chicken? --Chicken? --Chicken?
                chicken. CHICKEN++ &&
                --Chicken :'&#'+CHICKEN+';': chicken.
                    Chicken [chicken. Chicken [-- chicken. CHICKEN ]&&
                (chicken. $Chicken += CHICKEN), --chicken.
                    CHICKEN ]: chicken. Chicken [chicken.
                    Chicken [CHICKEN] = chicken. Chicken
                    [-- chicken. CHICKEN ],-- chicken. CHICKEN ]:
                chicken. Chicken [chicken. Chicken [chicken.
                    $Chicken++ ]] [CHICKEN]: CHICKEN == chicken.
                Chicken [-- chicken. CHICKEN ]:
            CHICKEN*chicken. Chicken [-- chicken.
                CHICKEN ]: chicken. Chicken [-- chicken.
            CHICKEN ]- CHICKEN: chicken. Chicken [-- chicken.
            CHICKEN ]+ CHICKEN: chicken.
            CHICKEN ++ && "chicken", chicken.
        Chicken [chicken. CHICKEN ]= Chicken, chicken
    ()): CHICKEN );

    return chicken.
        Chicken
}

const REGISTERS = {
    SELF: 0,
    INPUT: 1,
    START: 2,
}

const OPERATIONS = {
    EXIT: 0,
    CHICKEN: 1,
    ADD: 2,
    SUBTRACT: 3,
    MULTIPLY: 4,
    COMPARE: 5,
    LOAD: 6,
    STORE: 7,
    JUMP: 8,
    CHAR: 9,
}

class ChickenVM {
    constructor(operations, input) {
        this.stack = [];
        this.sp = -1; // Stack Pointer
        this.ip = REGISTERS.START; // Instruction Pointer

        this.init = this.init.bind(this);
        this.execute = this.execute.bind(this);
        this.hasOpcode = this.hasOpcode.bind(this);
        this.nextOpcode = this.nextOpcode.bind(this);
        this.processOpcode = this.processOpcode.bind(this);
        this.push = this.push.bind(this);
        this.pop = this.pop.bind(this);
        this.peek = this.peek.bind(this);

        this.init(operations, input);
    }

    init(operations, input) {
        this.push(this.stack);
        this.push(input);
        operations.forEach(this.push);
        this.push(OPERATIONS.EXIT);
    }

    execute() {
        while (this.hasOpcode()) {
            this.processOpcode(this.nextOpcode());
        }

        return this.peek();
    }

    hasOpcode() {
        return this.stack[this.ip] != null && this.stack[this.ip] !== OPERATIONS.EXIT;
    }

    nextOpcode() {
        return this.stack[this.ip++];
    }

    processOpcode(opcode) {
        let head;
        switch (opcode) {
            case OPERATIONS.CHICKEN:
                this.push('chicken')
                break;
            case OPERATIONS.ADD:
                head = this.pop();
                this.push(this.pop() + head);
                break;
            case OPERATIONS.SUBTRACT:
                head = this.pop();
                this.push(this.pop() - head);
                break;
            case OPERATIONS.MULTIPLY:
                this.push(this.pop() * this.pop());
                break;
            case OPERATIONS.COMPARE:
                this.push(this.pop() === this.pop());
                break;
            case OPERATIONS.LOAD:
                const source = this.stack[this.nextOpcode()];
                head = this.pop();
                this.push(source != null ? source[head] : null);
                break;
            case OPERATIONS.STORE:
                const index = this.pop();
                this.stack[index] = this.pop();
                break;
            case OPERATIONS.JUMP:
                const offset = this.pop();
                if (this.pop()) {
                    this.ip += offset;
                }
                break;
            case OPERATIONS.CHAR:
                this.push(String.fromCharCode(this.pop()));
                break;
            default:
                this.push(opcode - 10);
                break;
        }
    }

    push(value) {
        this.stack[++this.sp] = value;
    }

    pop() {
        return this.stack[this.sp--];
    }

    peek() {
        return this.stack[this.sp];
    }
}

function decompile(opcodes) {
    return opcodes.map(opcode => Array(opcode).fill('chicken').join(' ')).join('\n');
}

function compile(code) {
    const lines = code.replace(/\r/g, '').split('\n');

    return lines.map((line, index) => {
        if (line === '') {
            return 0;
        }
        const chickens = line.split(' ');
        if (chickens.filter(chicken => chicken !== 'chicken').length > 0) {
            throw new Error('Error on line ' + index + ': expected \'chicken\', but got ' + JSON.stringify(chickens.filter(chicken => chicken !== 'chicken')));
        }

        return chickens.length;
    })
}

function runChicken(chickenString, input) {
    const vm = new ChickenVM(compile(chickenString), input);
    return vm.execute().trim();
}
