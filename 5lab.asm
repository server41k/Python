.model Small;.model small сообщает ассемблеру, что вы собираетесь использовать малую модель памяти - один сегмент кода, один сегмент данных и один сегмент стека - и значения регистров сегментов никогда не меняются.
 .data
    Imya   db 'Chaush Server Lenurovich',10,13,'$'
    Gruppa db 'I-1-20',10,13,'$'
 .code
    Start:mov ax, @data
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
