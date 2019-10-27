def solution(n):
    answer = []
    for i in range(n):
        new_answer = [0]
        checker = 0
        for num in answer:
            checker = (checker + 1) % 2

            new_answer += [num, checker]
        answer = new_answer
    return answer