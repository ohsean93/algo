import sys

sys.stdin = open('input.txt', 'r')


def cal(now_num, can_use_operator, num_list):
    if num_list:
        next_num_list = num_list.copy()
        temp = next_num_list.pop()
        if can_use_operator[0]:
            next_can_use_operator = can_use_operator.copy()
            next_can_use_operator[0] -= 1
            next_num = now_num + temp
            cal(next_num, next_can_use_operator, next_num_list)
        if can_use_operator[1]:
            next_can_use_operator = can_use_operator.copy()
            next_can_use_operator[1] -= 1
            next_num = now_num - temp
            cal(next_num, next_can_use_operator, next_num_list)
        if can_use_operator[2]:
            next_can_use_operator = can_use_operator.copy()
            next_can_use_operator[2] -= 1
            next_num = now_num * temp
            cal(next_num, next_can_use_operator, next_num_list)
        if can_use_operator[3]:
            next_can_use_operator = can_use_operator.copy()
            next_can_use_operator[3] -= 1
            next_num = int(now_num / temp)
            cal(next_num, next_can_use_operator, next_num_list)
    else:
        global final_nums
        if final_nums[0] < now_num:
            final_nums[0] = now_num
        if final_nums[1] > now_num:
            final_nums[1] = now_num


T = int(input())
for test_case in range(1, T+1):
    final_nums = [-1e9, 1e9]
    n = int(input())
    operator = list(map(int, input().split()))
    nums = list(reversed(list(map(int, input().split()))))

    first_num = nums.pop()
    cal(first_num, operator, nums)

    ans = final_nums[0] - final_nums[1]
    print('#{} {}'.format(test_case, ans))