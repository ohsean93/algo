import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    ans = 0
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    i = n
    queue = []
    for j, pizza_che in enumerate(pizza[:n]):
        queue.append([pizza_che, j])

    pizza = pizza[n:]

    while True:
        if len(queue) == 1:
            ans = queue[0][1] + 1
            break
        one_pizza = queue[0][0]
        one_pizza //= 2
        if one_pizza == 0:
            if len(pizza):
                queue[0] = [pizza.pop(0), i]
                i += 1
            else:
                queue.pop(0)
                continue
        else:
            queue[0][0] = one_pizza
        queue.append(queue.pop(0))

    print('#{} {}'.format(test_case+1, ans))