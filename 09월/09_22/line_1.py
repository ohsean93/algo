import sys

sys.stdin = open('input.txt', 'r')


def my_print(h, str_type, str_h, origin_str):
    origin_str = list(reversed(list(origin_str)))
    middle = (str_h - 2)
    all_star = ['#'] * str_h

    return_str = []

    while origin_str:
        matrix = [['.'] * str_h for _ in range(h)]
        ind = -1
        temp = []
        for i, case in enumerate(str_num[origin_str.pop()]):
            if i % 2 == 0:
                ind += 1
                if case == 1:
                    matrix[ind] = all_star
                elif case == 2:
                    matrix[ind][0] = '#'
                    matrix[ind][-1] = '#'
                elif case == 3:
                    matrix[ind][0] = '#'
                elif case == 4:
                    matrix[ind][-1] = '#'
            else:
                for _ in range(middle):
                    ind += 1
                    if case == 1:
                        matrix[ind] = all_star
                    elif case == 2:
                        matrix[ind][0] = '#'
                        matrix[ind][-1] = '#'
                    elif case == 3:
                        matrix[ind][0] = '#'
                    elif case == 4:
                        matrix[ind][-1] = '#'
        for i in range(h):
            temp.append(''.join(matrix[i]))
        k = (h - 2 * str_h + 1)//2
        if str_type == 'TOP':
            pass
        elif str_type == 'BOTTOM':
            temp = temp[-(2 * k):] + temp[:-(2 * k)]
        elif str_type == 'MIDDLE':
            temp = temp[-k:] + temp[:-k]
        return_str.append(temp)
    # TOP, BOTTOM, MIDDLE

    return return_str


# 전부 찍히는 것 1, 양끝 2, 좌 3, 우 4
str_num = {
    '0': [1, 2, 2, 2, 1],
    '1': [4, 4, 4, 4, 4],
    '2': [1, 4, 1, 3, 1],
    '3': [1, 4, 1, 4, 1],
    '4': [2, 2, 1, 4, 4],
    '5': [1, 3, 1, 4, 1],
    '6': [3, 3, 1, 2, 1],
    '7': [1, 4, 4, 4, 4],
    '8': [1, 2, 1, 2, 1],
    '9': [1, 2, 1, 4, 4],
}

print_list = []
n, sort_type = input().split()
n = int(n)
max_len = 0

for _ in range(n):
    a, b = input().strip().split(' ')
    a = int(a)
    if a > max_len:
        max_len = a
    print_list.append((a, b))

height = 2 * max_len - 1
print_list.reverse()
ans = []
while print_list:
    ans.extend(list(my_print(height, sort_type, *print_list.pop())))

for line in list(zip(*ans)):
    print(' '.join(line))