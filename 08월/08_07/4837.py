import sys

sys.stdin = open("input.txt", "r")

set_num = [1,2,3,4,5,6,7,8,9,10,11,12]

for test_case in range(int(input())):
    n, k = map(int, input().split())

    num = 0
    count_set = 0

    while num < 2**12:
        sum_sub_set = 0
        count = 0
        check = num
        for i in range(12):
            if check % 2 == 1:
                count += 1
                sum_sub_set += set_num[i]
            
            if count > n:
                break

            check = check//2
        
        else:
            if count == n:
                if sum_sub_set == k:
                    count_set += 1

        num+=1

    print('#{} {}'.format(test_case, count_set))
