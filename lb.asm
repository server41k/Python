   .model Small
        .286
        .stack
 .DATA
    HelloMessage DB 'Hello World',10,13
    num          =  $ - HelloMessage
I.CODE
    START:push  @data
          pop   ds
          mov   cx,num
    a1:   lodsb
          int   29h
          loop  a1
          mov   ah,4ch
          int   21h
        mov ds, ax
        mov dx, offset Gruppa
        mov ah, 9h
        int 21h

        mov ax, @data
        mov ds, ax
        mov dx, offset Imya
        mov ah, 9h
        int 21h
        mov ah, 4ch
        int 21h
        end Start
