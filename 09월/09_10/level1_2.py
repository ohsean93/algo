f = [1,2,3,4,5]


def solution(answers):
    supo_1 = [1, 2, 3, 4, 5]  # 5
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    supo_3 = [3, 3, 1, 1, 3, 3, 4, 4, 5, 5]  # 10
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for i, num in enumerate(answers):
        if num == supo_1[i % 5]:
            cnt_1 += 1
        if num == supo_2[i % 8]:
            cnt_2 += 1
        if num == supo_3[i % 10]:
            cnt_3 += 1

    answer = []

    ans_num = max(cnt_1, cnt_2, cnt_3)
    if ans_num == cnt_1:
        answer.append(1)
    if ans_num == cnt_2:
        answer.append(2)
    if ans_num == cnt_3:
        answer.append(3)

    return answer


print(solution(f))