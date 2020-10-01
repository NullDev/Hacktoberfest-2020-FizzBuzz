; NASM (x86)
section .text
global start
start:
  push dword startMessageLength
  push dword startMessage
  push dword 1
  mov eax, 4
  sub esp, 4
  int 0x80
  mov [counter], byte 1
next_number:
  mov al, [counter]
  xor ah, ah
  mov bl, 3
  div bl
  cmp ah, 0
  jne not_fizz
  mov al, [counter]
  xor ah, ah
  mov bl, 5
  div bl
  cmp ah, 0
  jne not_fizzbuzz
  push dword 9
  push dword fizzBuzzMessage
  push dword 1
  mov eax, 4
  sub esp, 4
  int 0x80
  jmp finished_this_number
not_fizzbuzz:
  push dword 5
  push dword fizzMessage
  push dword 1
  mov eax, 4
  sub esp, 4
  int 0x80
  jmp finished_this_number
not_fizz:
  mov al, [counter]
  xor ah, ah
  mov bl, 5
  div bl
  cmp ah, 0
  jne not_fizz_or_buzz
  push dword 5
  push dword buzzMessage
  push dword 1
  mov eax, 4
  sub esp, 4
  int 0x80
  jmp finished_this_number
not_fizz_or_buzz:
  mov al, [counter]
  xor ah, ah
  mov bl, 10
  div bl
  cmp al, 0
  je skip_padding
  add al, 48
  mov [counterMessage], al
skip_padding:
  add ah, 48
  mov [counterMessage+1], ah
  push dword 3
  push dword counterMessage
  push dword 1
  mov eax, 4
  sub esp, 4
  int 0x80
finished_this_number:
  add [counter], byte 1
  cmp [counter], byte 100
  jle next_number
  push dword endMessageLength
  push dword endMessage
  push dword 1
  mov eax, 4
  sub esp, 4
  int 0x80
quit:
  mov eax, 1
  sub esp, 4
  int 0x80
section .data
counter db 0
counterMessage db ' ', 0xa
startMessage db 'FizzBuzz test', 0xa
startMessageLength equ $ - startMessage
fizzMessage db 'Fizz', 0xa
buzzMessage db 'Buzz', 0xa
fizzBuzzMessage db 'FizzBuzz', 0xa
endMessage db 'Done!', 0xa
endMessageLength equ $ - endMessage
