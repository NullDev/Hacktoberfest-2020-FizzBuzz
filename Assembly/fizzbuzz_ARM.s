@ I see there're assembly codes for x86 and MIPS so I implement it on ARM assembly
@ Author : @Tantatorn-dev


.data

.balign 4
num_str: .asciz "%d\n"

.balign 4
fizz: .asciz "Fizz"

.balign 4
buzz: .asciz "Buzz"

.balign 4
fizzbuzz: .asciz "FizzBuzz"

.balign 4
num: .word 0

.balign 4
lr_bu: .word 0

.balign 4
lr_bu_2: .word 0

.text

@ fizzbuzz function
fizz_buzz:
    @ Save Link Register

    LDR R2, addr_lr_bu_2
    STR lr,[R2]

    @ R5 is our num start at 0
    MOV R5,R0

start:
    
    MOV R6, #3
    MOV R7, #5

    @ check if R5 % 3 == 0
    MOV R6, R5 MOD #3
    CMP R6, #0
    BEQ print_fizz

    @ check if R5 % 5 == 0
    MOV R6, R5 MOD #5
    CMP R6, #0
    BEQ print_buzz

    @ check if R5 % 3 == 0 && R5 % 5 == 0
    MOV R6, R5 MOD #15
    CMP R6, #0
    BEQ print_fizzbuzz

print_num:
    @ print number
    LDR R0, num_str
    MOV R1, R5
    BL printf
    B increment

print_fizz:
    @ print fizz
    LDR R0,addr_fizz
    BL printf
    B increment

print_buzz:
    @ print buzz
    LDR R0,addr_buzz
    BL printf
    B increment

print_fizzbuzz:
    @ print fizzbuzz
    LDR R0,addr_fizzbuzz
    BL printf
    B increment

increment:
    @increment R5 value
    ADD R5,R5,#1

    @ if R5 equals to 101 end loop
    CMP R5,#101
    BEQ end

    B start

end:

    @ Restore Link Register
    LDR lr, addr_lr_bu_2
    LDR lr, [lr]
    BX lr

    @ variable to back up Link Register
    addr_lr_bu_2: .word lr_bu_2




@ Used by the compiler to tell libc where main is located
.global main
.func main
main:
    @ Keep the value inside Link Register
    LDR R1, addr_lr_bu
    STR lr, [R1]
    @ Mem[R1] <- LR


    @ Pass by values entered to fizz_buzz
    LDR R0, addr_num
    LDR R0, [R0]

    BL fizz_buzz

    @ Restore the saved value to link register
    LDR lr, addr_lr_bu

    LDR lr, [lr] @ LR <- Mem[addr_lr_bu]
    BX lr @ Return to main function

@ Define addresses
addr_num_str: .word num_str
addr_fizzbuzz: .word fizzbuzz
addr_fizz: .word fizz
addr_buzz: .word buzz

addr_lr_bu: .word lr_bu

@ Declare printf and scanf functions to be linked with
.global printf