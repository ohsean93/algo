def print_con(n_num, r_num):
    stack = [0]
    while stack:
        num = stack.pop(0)
        if bin(num).count('1') == r_num:
            i = 1
            temp = []
            for checker in bin(num)[2:][::-1]:
                if checker == '1':
                    temp.append(str(i))
                i += 1
            print(' '.join(temp))
        else:
            k = min((len(bin(num))-2), num)
            for i in range(k, n_num):
                if 1 << i & num:
                    continue
                else:
                    stack.append((1 << i) + num)


n, r = map(int, input().split())
print_con(n, r)