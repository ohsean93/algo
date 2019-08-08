import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):

    doc = ''
    secert_list = input()
    bit = []
    for char in secert_list:
        if char == '+':
            num = 62
        elif char == '/':
            num = 63
        elif char.isdigit():
            num = int(char) + 52
        else:
            num = ord(char)
            if num<=90:
                num -= 65
            else:
                num -= 71
        
        bi_num = [0,0,0,0,0,0]
        for i in range(6):
            if num & 1 << i:
                bi_num[5-i] = 1

        bit += bi_num

    while True:
        if len(bit) == 0:
            break
        change_char = 0
        change_num = bit[:8]
        for i in range(8):
            change_char += change_num[7-i] * (2**i)
        
        bit = bit[8:]
        
        # print(change_char,end='')
        print(chr(change_char),end='')

    print()