f = open('file.txt')
dot_count = 0
comma_count = 0
lines = 0
dot_count2 = 0
comma_count2 = 0
lines2 = 0
for l in f:
    for i in l:
        if i == '.':
            dot_count += 1
            dot_count2 += 1
        if i == ',':
            comma_count2 += 1
            comma_count += 1
        if i == '\n':
            lines += 1
    print(f'String: {l}', f'comma: {comma_count2}',
          '\n', f'dot: {dot_count2}', '\n', sep='')
    dot_count2 = 0
    comma_count2 = 0
print('Total:')
print('Lines:', lines, "\nComma:",
      comma_count, "\nDot:", dot_count)
