a = [2, 14, 11, 21, 17, 24, 23]
d = 25
k = 2


def solution(distance, rocks, n):
    m = len(rocks)
    if m == n:
        return distance
    rocks.sort()
    gap = [0] * (m + 1)
    rocks = [0] + rocks + [distance]
    for i in range(m + 1):
        gap[i] = rocks[i+1]-rocks[i]
    gap = [distance] + gap
    for _ in range(n):
        min_num = min(gap)
        merge_num = distance
        temp = 0
        pop_num = 0
        index = 0
        p = gap.count(min_num)
        for __ in range(p):
            index = gap.index(min_num, index + 1)
            if index == 1:
                if merge_num > gap[index + 1]:
                    merge_num = gap[index + 1]
                    temp = index + 1
                    pop_num = index
            elif index == m + 1:
                if merge_num > gap[index - 1]:
                    merge_num = gap[index - 1]
                    temp = index - 1
                    pop_num = index
            else:
                if merge_num > gap[index + 1]:
                    merge_num = gap[index + 1]
                    temp = index + 1
                    pop_num = index
                if merge_num > gap[index - 1]:
                    merge_num = gap[index - 1]
                    temp = index - 1
                    pop_num = index
        m -= 1
        gap[temp] += min_num
        gap.pop(pop_num)

    answer = min(gap)
    return answer


print(solution(d, a, 2))