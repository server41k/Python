text = input()
print(text[::-1])


another_text = input()
temp = ''
for i in range(len(another_text)):
    temp = another_text[i] + temp
print(temp)
