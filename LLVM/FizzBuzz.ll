; Handwritten LLVM implementation of FizzBuzz
; Author: @PAndaContron

; String constants
@.fizzstr = private constant [5 x i8] c"Fizz\00"
@.buzzstr = private constant [5 x i8] c"Buzz\00"
@.intform = private constant [3 x i8] c"%d\00"
@.newline = private constant [2 x i8] c"\0A\00"

; External printf function declaration
declare i32 @printf(i8*, ...)

define i32 @main() {
    ; Local pointers to string constants
    %fizzstr = getelementptr inbounds [5 x i8], [5 x i8]* @.fizzstr, i32 0, i32 0
    %buzzstr = getelementptr inbounds [5 x i8], [5 x i8]* @.buzzstr, i32 0, i32 0
    %intform = getelementptr inbounds [3 x i8], [3 x i8]* @.intform, i32 0, i32 0
    %newline = getelementptr inbounds [2 x i8], [2 x i8]* @.newline, i32 0, i32 0

    ; Initialize index to 1
    %ind = alloca i32
    store i32 1, i32* %ind
    br label %loop

loop:
    ; Load value of index
    %indval = load i32, i32* %ind

    ; Calculate remainders mod 3 and 5
    %mod3 = srem i32 %indval, 3
    %mod5 = srem i32 %indval, 5

    ; Boolean values for divisibility by 3 and 5
    %div3 = icmp eq i32 %mod3, 0
    %div5 = icmp eq i32 %mod5, 0

    ; Print "Fizz" if divisible by 3
    br i1 %div3, label %print_fizz, label %check5

print_fizz:
    %call1 = call i32 (i8*, ...) @printf(i8* %fizzstr)
    br label %check5

check5:
    ; Print "Buzz" if divisible by 5
    br i1 %div5, label %print_buzz, label %check_num

print_buzz:
    %call2 = call i32 (i8*, ...) @printf(i8* %buzzstr)
    br label %check_num

check_num:
    ; Print the value of the index if divisible by neither
    %div_either = or i1 %div3, %div5
    br i1 %div_either, label %loop_inc, label %print_num

print_num:
    %call3 = call i32 (i8*, ...) @printf(i8* %intform, i32 %indval)
    br label %loop_inc

loop_inc:
    ; Print newline
    %call4 = call i32 (i8*, ...) @printf(i8* %newline)

    ; Increment the index
    %newind = add nsw i32 %indval, 1
    store i32 %newind, i32* %ind

    ; Check index to end loop or jump back to the top
    %done = icmp sgt i32 %newind, 100
    br i1 %done, label %loop_end, label %loop

loop_end:
    ret i32 0
}
