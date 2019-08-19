import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    doc = ''
    char_num = int(input())
    for i in range(char_num):
        char, num = input().split()
        for j in range(int(num)):
            doc += char
    
    print('#{}'.format(test_case+1))

    while True:
        print(doc[:10])
        if len(doc)<=10:
            break
        doc = doc[10:]


    