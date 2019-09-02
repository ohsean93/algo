import sys

sys.stdin = open("input.txt", "r")


def find_prime(end_num):
    global checker
    global numbers

    if end_num < checker:
        return

    while checker < end_num:
        checker += 1
        if numbers[checker]:
            prime_numbers.append(checker)
            for num in range(2 * checker, 10**6 + 1, checker):
                if numbers[num]:
                    numbers[num] = 0


def divisor(divided_number):
    global numbers
    dp_point = divided_number
    sum_num = 1
    r = 0
    for num in prime_numbers:
        if numbers[divided_number]:
            sum_num *= numbers[divided_number]
            break
        if divided_number == 1:
            break
        while (divided_number % num) == 0:
            r += 1
            divided_number //= num
        if r:
            sum_num *= numbers[num**r]
            r = 0

    numbers[dp_point] = sum_num
    return sum_num


T = int(input())
numbers = [1] * (10**6 + 1)
checker = 1
prime_numbers = []
find_prime(10**6)
numbers = [0] * (10**6 + 1)
sum_number = [0] * (10**6 + 1)
for number in prime_numbers:
    temp_num = number
    r = 1
    if number == 2:
        while temp_num <= 10 ** 6:
            numbers[temp_num] = 1
            temp_num *= number
            r += 1
    else:
        while temp_num <= 10**6:
            numbers[temp_num] = ((number**(r + 1) - 1)//(number - 1))
            temp_num *= number
            r += 1

numbers[1] = 1
sum_number[1] = 1
sum_number[2] = 2
for number in range(3, 10**6+1):
    divisor(number)
    sum_number[number] = sum_number[number-1] + numbers[number]

ans_list = []
for test_case in range(1, T + 1):
    L, R = map(int, input().split())
    ans = sum_number[R]-sum_number[L-1]
    ans_list.append('#{} {}'.format(test_case, ans))

print('\n'.join(ans_list))