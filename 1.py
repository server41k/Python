f = open('file.txt')
for line in f:
    for i in line:
        print(i, end ='')
