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

function runChicken(chickenString) {
    const vm = new ChickenVM(compile(chickenString), '(unused)');
    return vm.execute().trim();
}
