def plus(res=0):
    temp = input()
    if temp == 'exit':
        return 0

    try:
        res += int(temp)
        print('Result: ', end='')
        print(res)
        plus(res)
    except:
        print('Error')
        exit


print('Type "exit" to leave')
plus()
