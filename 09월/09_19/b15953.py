import sys
sys.stdin = open('input.txt', 'r')

#  1 2 3 4 5 6  => 1 3 6 10 15 21
#  500 300 200 50 30 10
#  1 2 4 8 16  => 1 3 7 15 31
#   512 256 128 64 32


def con_1(rank_num):
    if rank_num == 0:
        prize = 0
    elif rank_num == 1:
        prize = 500
    elif rank_num < 4:
        prize = 300
    elif rank_num < 7:
        prize = 200
    elif rank_num < 11:
        prize = 50
    elif rank_num < 16:
        prize = 30
    elif rank_num < 22:
        prize = 10
    else:
        prize = 0
    return prize


def con_2(rank_num):

    if rank_num:
        n = len(bin(rank_num))-2
        if n < 6:
            prize = 2**(10-n)
        else:
            prize = 0
    else:
        prize = 0
    return prize


T = int(input())
ans_list = [0] * T
for test_case in range(T):
    a, b = map(int, input().split())
    ans = 10000 * (con_1(a) + con_2(b))
    ans_list[test_case] = str(ans)

print('\n'.join(ans_list))