.model small
    .286
.stack 100h
.data
    a dw 1234
    b db ' ',10,13,'$'
    c db 10
.code
    start:
        mov ax,@data
        mov ds,ax
        mov si,2
        mov ax, a
        k1:div c
        add ah,30h
        mov [b+si],ah
        dec si
        mov ah,0
        cmp al,0
        jne k1
        mov dx, offset b
        mov ah,9h
        int 21h
        mov ah,4ch
        int 21h
        end start
