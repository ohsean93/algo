T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    list_a = input().split()
    list_b = input().split()
    words = dict()
    cnt = 0
    for word in list_a:
        words[word] = 1
    for word in list_b:
        if words.get(word):
            cnt += 1
    print('#{} {}'.format(test_case, cnt))
