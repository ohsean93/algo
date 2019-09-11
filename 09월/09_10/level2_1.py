def solution(n):
    answer = 0
    n = int(n)
    cnt = (bin(n).replace('0b', '')).count('1')
    for num in range(n+1, 2 * n + 1):
        cnt_num = (bin(num).replace('0b', '')).count('1')
        if cnt == cnt_num:
            answer = num
            break

    return answer


print(solution(78))