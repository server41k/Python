        .model small
        .286
 .data
      a    db 'Sroki ne sushestvyet$'
 .code
      start:
            mov ax,[ds:2ch];среда окружения
            mov ds,ax
            mov di,0
            mov si,0
            mov bp,1;номер искомой строки
            mov dl, 20h; чтобы при выводе 1 строки не вывелся 0

      k4:   inc di
            cmp di,bp;сравнение
            je  k3
      ;
      k1:   mov dl,[ds:si]
            inc si
            cmp dl,0
            jne k1
            mov dl,[ds:si]
            inc si
            cmp dl,0
            jne k4
            jmp k2
      
      k3:   mov ah,2h ;вывод нужнойстроки
            int 21h
            mov dl,[ds:si]
            cmp dl,0
            je  k5
            inc si
            jmp k3
			
      k2:   
            mov ax, @data;если нет строки
            mov ds, ax
            mov dx, offset a
            mov ah, 9h
            int 21h
            jmp k5
      k5:   mov ah,4ch;выход
            int 21h
        end start