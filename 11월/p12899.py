n = 3
ans = ''

while n:
    temp = n % 3
    n = n // 3
    if temp == 0:
        ans = '1' + ans
    elif temp == 1:
        ans = '2' + ans
    else:
        ans = '4' + ans
print(ans)