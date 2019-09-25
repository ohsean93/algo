# k 번쨰 블록의 값은 자기 자신을 제외한 가장 큰 약수
# 10^9 까지의 수
# 10^4.5 까지의 소수가 필요 => 31622.xxx 177.8xxx
p_num = [1] * 31625
checker = []
p_num[0] = p_num[1] = 0
for num in range(31625):
    if p_num[num]:
        for i in range(num*2, 31625, num):
            p_num[i] = 0
        checker.append(num)


def solution(begin, end):
    answer = []
    for tail in range(begin, end + 1):
        for prime in checker:
            if tail % prime == 0:
                answer.append(tail//prime)
                break
        else:
            answer.append(1)

    return answer