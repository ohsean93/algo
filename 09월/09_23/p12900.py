def solution(n):
    a = 1
    b = 1
    for _ in range(n):
        a, b = b, (a + b) % 1000000007
    answer = a % 1000000007

    return answer