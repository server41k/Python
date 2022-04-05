def func():
    s = input()
    flag = 0
    for i in s:
        if i == '(':
            flag += 1
        if i == ')':
            flag -= 1
        if flag < 0:
            return False
    if flag == 0:
        return True
    else:
        return False


print(func())
