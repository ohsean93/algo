def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        if answer == 0:
            for j in range(i+1):
                temp = s[j:j+n-i]
                if temp == temp[::-1]:
                    answer = n-i
                    break

    return answer