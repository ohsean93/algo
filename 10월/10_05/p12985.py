def solution(n, a, b):
    answer = 0
    n -= 1
    a = bin((a - 1) | n)[2:]
    b = bin((b - 1) | n)[2:]
    n = len(bin(n)) - 2
    print(a, b)

    for j in range(min(len(a), len(b))):
        if a[-j] != b[-j]:
            answer = j
    return n - j