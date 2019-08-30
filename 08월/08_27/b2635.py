import sys

sys.stdin = open("input.txt", "r")


def sequence(start_num, second_nam):
    cnt = 1
    ans_list = [start_num]
    while second_nam >= 0:
        cnt += 1
        ans_list.append(second_nam)
        start_num, second_nam = second_nam, start_num - second_nam
    return cnt, ans_list


n = int(input())
num = 0
for i in range((n+1)//2, n+1):
    num2, ans2 = sequence(n, i)
    if num < num2:
        num = num2
        ans = ans2


ans = list(map(str, ans))
print(num)
print(' '.join(ans))