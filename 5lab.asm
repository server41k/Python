.model Small;.model small сообщает ассемблеру, что вы собираетесь использовать малую модель памяти
 .data                                              ;сегмент данных
    Imya   db 'Chaush Server Lenurovich',10,'$'
    Gruppa db 'I-1-20',10,'$'
 .code                              ; начало кода
    Start:mov ax, @data            ; в ax вводим сегмент данных
          mov ds, ax               ; далее перемещаем его в ds
          mov dx, offset Gruppa    ;в dx даём смещение группы
          mov ah, 9h               ; команда 9h - вывод
          int 21h                  ;прерывание

          mov dx, offset Imya
          mov ah, 9h
          int 21h
          mov ah, 4ch              ;завершение
          int 21h
        end Start
