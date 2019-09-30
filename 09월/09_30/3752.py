T = int(input())
for test_case in range(1, T+1):
    temp = set()
    temp.add(0)
    n = int(input())
    scores = list(map(int, input().split()))

    for score in scores:
        new_temp = set()
        for num in temp:
            sub_score = score + num
            new_temp.add(sub_score)
        temp = temp.union(new_temp)

    print('#{} {}'.format(test_case, len(temp)))


