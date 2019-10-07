# def solution(strs, t):
#     answer = 1
#     new_strs = []
#     checker = 1
#     for case in strs:
#         if case in t:
#             new_strs.append((1, case))
#             if case == t:
#                 checker = 0
#     strs = new_strs
#     answer = 100
#     while new_strs and checker:
#         new_strs = []
#         for cnt_a, a in strs:
#             for cnt_b, b in new_strs:
#                 new_cnt = cnt_a + cnt_b
#                 new_str = a + b
#                 if new_str in t and (new_cnt, new_str) not in strs:
#                     new_strs.append((new_cnt, new_str))
#                     if new_str == t:
#                         checker = 0
#                         if answer > new_cnt:
#                             answer = new_cnt
#         strs += new_strs
#
#     if checker:
#         return -1
#     return answer

def solution(strs, t):
    answer = 101
    temps = [(0, t)]
    new_strs = []
    for case in strs:
        if case in t:
            new_strs.append(case)

    strs = new_strs
    while temps:
        cnt, temp = temps.pop(0)
        cnt += 1
        for i in range(1, 6):
            a = temp[:i]
            if a in strs:
                next_temp = temp[i:]
                if next_temp:
                    temps. append((cnt, next_temp))
                else:
                    if answer > cnt:
                        answer = cnt
    if answer == 101:
        answer = -1
    return answer


print(solution(['ba', 'an', 'nan', 'ban', 'n'], 'banana'))