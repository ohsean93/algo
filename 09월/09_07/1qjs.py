ss = "a"


def my_zip(str_origin, num):
    temp = ''
    cnt = 1
    return_str = ''
    while len(str_origin) >= num:
        checker = str_origin[:num]
        str_origin = str_origin[num:]
        if temp == checker:
            cnt += 1
            if len(str_origin) < num:
                return_str += (str(cnt))

        else:
            if cnt != 1:
                return_str += (str(cnt) + temp)
                cnt = 1

            else:
                return_str += temp
        temp = checker

    return_str += temp
    return return_str + str_origin


def solution(s):
    if len(s) == 1:
        return 1
    n = len(s)
    answer = 1000
    for i in range(1, n // 2 + 1):
        num = len(my_zip(s, i))
        str_zip = my_zip(s, i)
        print(i, str_zip)
        if num < answer:
            answer = num

    return answer


print(solution(ss))