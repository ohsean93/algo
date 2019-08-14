a = 'asadfweadszvcx'

k = len(a)
a = list(a)

for index in range(k // 2):
    a[index], a[-index - 1] = a[-index - 1], a[index]

print(''.join(a))


num = 172917
num_str = ''
while True:
    char_num = num % 10
    num = num // 10
    num_str = chr(char_num + 48) + num_str
    if num == 0:
        break

print(num_str)