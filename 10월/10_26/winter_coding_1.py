from math import ceil, floor

def solution(w,h):
    a, b = w, h
    while a * b:
        a,b = b, a % b
    gcd = a + b
    small_sq_cut = 0
    b = 1
    for i in range(1, h//gcd +1):
        a = ceil(i*w/h)
        small_sq_cut += a - b + 1
        b = a
    answer = w * h - gcd * small_sq_cut
    return answer