a =[1,2,4,5]


def solution(cookie):
    n = len(cookie)
    sum_cookie = [0] * (n + 1)
    for i, num in enumerate(cookie):
        sum_cookie[i + 1] = sum_cookie[i] + num

    answer = 0

    for i in range(n + 1):
        for j in range(i, n + 1):
            one_boy = sum_cookie[j] - sum_cookie[i]
            if one_boy < answer:
                continue
            checker = 2 * one_boy + sum_cookie[i]
            if checker in sum_cookie[j:]:
                answer = one_boy

    return answer



print(solution(a))