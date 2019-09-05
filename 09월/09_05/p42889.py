N = 7
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    answer = []
    temp_answer = []
    clear = [0] * (N + 2)
    clear_user = []

    sum_num = 0
    for i in stages:
        clear[i] += 1

    clear = clear[::-1]
    clear.pop()
    sum_num = 0
    for num in clear:
        sum_num += num
        clear_user.append(sum_num)
    clear_user = clear_user[::-1]

    for i in range(1, N + 1):
        if clear_user[i-1]:
            temp_answer.append((clear_user[i]/clear_user[i-1], i))
        else:
            temp_answer.append((1, i))

    temp_answer.sort()
    for fail_rate, stage in temp_answer:
        answer.append(stage)
    return answer


print(solution(N, stages))