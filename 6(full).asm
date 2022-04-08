        .model small
        .stack 100h
 .data
    a    dd 09FFFFh                    ;
    b    db '       ', 10, 13, '$'
    c    dw 10
 .code
    start:
          mov ax, @data
          mov ds, ax
        
          mov si, 6
          mov dx, word ptr [a+2]    ;указываем на взятие слова из позиции а + 2
          mov ax, word ptr a        ;указываем на взятие слова из позиции а(первые FFFFh)
    kl:   div c                     ;(dx ax) / c ==> dl = остаток, ax = floor(ax / 10)
          add dl, 30h               ; тут добавляем 30h чтобы из числа сделать ASCII символ
          mov [b + si], dl          ; позиции [b + si] строки b присваиваем значение dl (остаток)
          dec si                    ;уменьшаем si
          mov dx, 0                 ;dx = 0 чтобы делить только ax на 10
          cmp ax, 0                 ;пока ax != 0
          jne kl                    ;прыгать к kl
          mov dx, offset b          ;dx = адрес позиции первого знака b
          mov ah, 9h                ; команда вывода строки до $
          int 21h                   ;прерывание
          mov ah, 4ch               ; командда конеца программы
          int 21h                   ; прерывание       ; прерывание
        end start