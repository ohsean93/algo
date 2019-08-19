import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    n = int(input())
    screws = []
    for i in range(n):
        screws += [[0,0]].copy()
    input_list = list(map(int,input().split()))
    for i, size in enumerate(input_list):
        screws[i//2][i%2]=size

    ans = screws.copy()

    for i, screw in enumerate(screws):
        len_screw = 1
        is_use = 1<<i
        end = screw[1]
        line = screws.copy()
        line[0] = screw

        while True:
            for j, next_screw in enumerate(screws):
                if next_screw[0] == end:
                    if is_use & 1<<j:
                        pass
                    else:
                        line[len_screw] = next_screw
                        end = next_screw[1]
                        is_use += 1<<j
                        len_screw += 1
                        break

            else:
                break
                        
            if len_screw == len(screws):
                ans = line
        
                
    print('#{} '.format(test_case), end='' )
    for i, screw in enumerate(ans):
        if i == n - 1:
            print('{} {}'.format(screw[0],screw[1]),end='')
        else:
            print('{} {}'.format(screw[0],screw[1]),end=' ')
    print()
                

    