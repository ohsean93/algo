import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    D, A, B, F = map(int,input().split())
    t_1 = D/(A+F)
    t_2 = (D-(B+A)*t_1)/(B+F)

    T_odd = t_1 / (1-((F-A)*(F-B))/((F+A)*(F+B)))
    T_even = t_2 / (1-((F-B)*(F-A))/((F+B)*(F+A)))

    S = F * (T_even + T_odd)

    print('#{} {}'.format(test_case+1,S))