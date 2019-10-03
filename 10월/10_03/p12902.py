import sys

sys.stdin = open('input.txt', 'r')


def solution(n):
    if n % 2:
        return 0
    a, b = 3, 1
    for _ in range(n // 2):
        a, b = 3 * a + 2 * b, a

    return b % 1000000007