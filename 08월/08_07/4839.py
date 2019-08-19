import sys

sys.stdin = open("input.txt", "r")

def bi_search(num,p):

    l = 1
    r = p
    c = 0
    ans = 0

    if num == p or num == 1:
        return ans

    for i in range(15):
        c =  (l + r)//2
        
        if num == c:
            return (i+1)
        if num > c:
            l = c
        else:
            r = c

for test_case in range(1, int(input()) + 1):
    p, num1, num2 = map(int,input().split())

    num_a = bi_search(num1, p)
    num_b = bi_search(num2, p)

    if num_a == num_b:
        ans = 0
    elif num_a > num_b:
        ans = 'B'
    else:
        ans = 'A'

    print('#{} {}'.format(test_case,ans))
