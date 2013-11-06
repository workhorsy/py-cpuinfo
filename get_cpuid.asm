; clear && rm -f out && nasm -f elf -o get_cpuid.o get_cpuid.asm
; gcc -m32 get_cpuid.o -o get_cpuid

; clear && nasm -o out -f bin get_cpuid.asm && ndisasm out

section .data


section .text
global main

main:
	mov ax, 1
	cpuid
	mov ax, bx
	ret


