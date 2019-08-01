import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    T = int(input())
    list1 = list(map(int, list(input())))
    index_num = [0] * 10

    for i in list1:
        index_num[i] += 1

    max_count = 0
    for j in range(10):
        if max_count <= index_num[j]:
            max_count = index_num[j]
            num = j

    print("#{0} {1} {2}".format(test_case, num, max_count))