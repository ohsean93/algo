num_list = [1] * (10**6 + 1)
num_list[0] = num_list[1] = 0
i = 2
prime_num = []
while i <= 10**3:
    if num_list[i]:
        prime_num.append(str(i))
        j = 2 * i
        while j <= 10**6:
            num_list[j] = 0
            j += i
    i += 1
while i <= 10**6:
    if num_list[i]:
        prime_num.append(str(i))
    i += 1
print(' '.join(prime_num))

