        model small
        .286
        .stack 100h
        .data
b db 'String does not exist$'
        .code
start:  mov ax,[ds:2ch]
        mov ds,ax
        mov si,-1 ; index po simvolam
k3:     inc si
        mov di,si ; nachalo obozrevaemoy stroki
k2:     mov dl,[ds:si] ; simvol iz sredy okrujeniya
        cmp dl,'A'
        je k4 ; simvol est'
        inc si
        cmp dl,0
        jne k2
        ; proverka na vtoroy 0
        mov dl,[ds:si]
        cmp dl,0
        jne k3
        ; stroki net
        cmp bp, 1
        je k6
        mov ax, @data
        mov ds, ax
        mov dx, offset b
        mov ah,9h
        int 21h
        jmp k6
        ;vyvod stroki
k4:     mov si, di
        mov dl, ''
k1:     mov ah, 2h
        int 21h
        mov dl, [ds:si]
        cmp dl, 0
        je k5
        inc si
        jmp k1
        ;exit
k5:     mov ah, 2h
        int 21h
        mov dl, 10
        mov ah, 2h
        int 21h
        mov dl, 13
        mov bp, 1
        jmp k3 
k6:     mov ah,4ch
        int 21h
end start