; FizzBuzz in pure Assembly without using external libs without using any space on stack
; Author: @ViperX7

section .text
    global _start

section .data

fizz db  'Fizz' ;
buzz db  'Buzz' ;
nl db  0xa ;
vv db  0x0 ;

section .text

_start:

LOOP:
    inc r12
    mov rax,r12

FIZZ:
    mov ebx, 3
    xor edx, edx
    div ebx
    cmp edx, 0
    jnz BUZZ

    mov rdx,4
    mov rdi,1
    mov rsi,fizz
    mov rax,1
    syscall


    mov r15,1



BUZZ:
    mov  rax, r12
    mov ebx, 5
    xor edx, edx
    div ebx
    cmp edx, 0
    jnz CT

    mov rdx,4
    mov rdi,1
    mov rsi,buzz
    mov rax,1
    syscall

    mov r15,1


CT:
    cmp r15,1
    je NXT




mov rax,r12
PT_UNIT:
    cmp al, 9
    jg PT_TENS

    add al,0x30
    mov byte [vv], al

    mov rdx,1
    mov rdi,1
    mov rsi,vv
    mov rax,1
    syscall

    jmp NXT



PT_TENS:
    cmp al, 99
    jg NXT

    mov rbx,10
    xor edx, edx
    div rbx
    mov rbx, rax
    add rax,0x30
    mov byte [vv], al

    mov rdx,1
    mov rdi,1
    mov rsi,vv
    mov rax,1
    syscall


    mov rax,r12
    imul rbx,10
    sub rax,rbx
    jmp PT_UNIT


NXT:
    mov rdx,1
    mov rdi,1
    mov rsi,nl
    mov rax,1
    syscall

    cmp r12,100
    mov r15,0
    jne LOOP

    mov rsi,0
    mov rax,60
    syscall


EXIT:

    mov rdx,4
    mov rdi,1
    mov rsi,buzz
    mov rax,1
    syscall
