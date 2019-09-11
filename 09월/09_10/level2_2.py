import itertools

a = '011'
prime_number = [1] * (10**7)
prime_number[0] = 0
prime_number[1] = 0
for num in range(10**7):
    if prime_number[num]:
        for d in range(2, (10**7-1)//num):
            prime_number[num*d] = 0


def solution(numbers):
    answer = 0
    set_num = set()
    for k in range(1, len(numbers)+1):

        for case in itertools.permutations(list(numbers), k):
            temp = ''
            for char in case:
                temp += char
            temp = int(temp)

            if prime_number[temp]:
                if temp not in set_num:
                    answer += 1
            set_num.add(temp)

    return answer


print(solution(a))