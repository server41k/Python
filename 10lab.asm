.model Small
.286
.stack 100h
.data
.code
vivod macro
mov dl,20h; код символа «пробел»
mov ah,02h
int 21h
endm
start: mov ax, @data
mov ds, ax
mov si, 0; код символа
mov cx,1
k1: mov dl, 10 ; переход на новую строку
mov ah,02h
int 21h
loop k1
top: mov dl, 10
mov ah,02h
int 21h
mov dl, 

m2: mov di,0; количество выведенных
символов в строке
mov cx, 24 ; для вывода 24-х пробелов
mov dl, 10
mov ah, 02h
int 21h
k2: vivod
loop k2
k3: cmp si, 256
je konec
cmp di, 15
je m2
cmp si,13
ja l1
cmp si, 7
je m1
cmp si, 8
je m1
cmp si, 9
je m1
cmp si, 10
je m1
cmp si, 13
je m1
; вывод символа
l1: mov dx, si
mov ah, 02h
int 21h
vivod
l2: inc si
inc di
jmp k3
m1: vivod
vivod
jmp l2
konec: mov ah, 4ch
int 21h
end start 