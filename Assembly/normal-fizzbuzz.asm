; FizzBuzz implemented in x86asm
; Author: @meneza

global _main
extern _printf

section .text
_main:
    push ebp
    mov ebp, esp
    xor esi, esi

check:
    cmp esi, 100
    je end

    push newline
    call _printf
    add esp, 4

    inc esi
    xor ebx, ebx
    xor edx, edx
    mov eax, esi
    mov ecx, 3
    idiv ecx
    test edx, edx
    jne check2

    push fizz
    call _printf
    add esp, 4
    inc ebx

check2:
    xor edx, edx
    mov eax, esi
    mov ecx, 5
    idiv ecx
    test edx, edx
    jne regular

    push buzz
    call _printf
    add esp, 4
    inc ebx

regular:
    test ebx, ebx
    jne check

    push esi
    push format
    call _printf
    add esp, 8
    jmp check

end:
    mov esp, ebp
    pop ebp
    ret
    

section .data
fizz:
    db "Fizz", 0
buzz:
    db "Buzz", 0
format:
    db "%i", 0
newline:
    db 0xA
