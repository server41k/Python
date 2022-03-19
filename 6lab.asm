   .model Small
        .286
 .stack
 .data
    Message db 'Hello World',10,13,'$'
    Gruppa  db 'Rand',10,13,'$'
    Imya    db 'random',10,13,'$'
    kekw    db 'kekw',10,13,'$'
 .code
    Start:mov ax, @data
          mov ds, ax
          mov dx, offset Message
          mov ah, 9h
          int 21h

          mov ax, @data
          mov ds, ax
          mov dx, offset Gruppa
          mov ah, 9h
          int 21h
          
          mov ax, @data
          mov ds, ax
          mov dx, offset kekw
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
