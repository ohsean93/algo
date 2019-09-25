def solution(sticker):
    can_use = 0
    cannot_use = 0
    for num in sticker[1:]:
        cannot_use, can_use = can_use + num, max(can_use, cannot_use)
    answer = max(can_use, cannot_use)

    can_use = sticker[0]
    cannot_use = sticker[0]
    for num in sticker[2:-1]:
        cannot_use, can_use = can_use + num, max(can_use, cannot_use)
    answer = max(can_use, cannot_use, answer)

    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))