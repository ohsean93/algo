matrix = [
    ['100', "ryan", "music", "2"], ["200", "apeach", "math", "2"],
    ['300', "tube", "computer", "3"], ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]
]
sub_set_list = dict()


def all_sub_set(use_list, size):
    global sub_set_list
    if use_list:
        start_node = use_list[-1] + 1
    else:
        start_node = 0

    for next_node in range(start_node, size):
        next_list = use_list + [next_node]
        sub_set_list[len(next_list)].append(next_list)
        all_sub_set(next_list, size)


def solution(relation):
    global sub_set_list
    n = len(relation)
    cols = list(zip(*relation))
    m = len(cols)
    sub_set_list = dict()
    for i in range(1, m+1):
        sub_set_list[i] = []
    all_sub_set([], m)
    candidate_list = []
    use_col = []

    for i in range(1, m+1):
        for case in sub_set_list[i]:
            if i == 1:
                if len(set(cols[case[0]])) == n:
                    candidate_list.append(case)
                    use_col.append(1 << case[0])
            else:
                test_case = []
                checker = 0
                for index in case:
                    checker += 1 << index
                    test_case.append(cols[index])
                for use in use_col:
                    if checker & use == use:
                        break
                else:
                    if len(set(zip(*test_case))) == n:
                        candidate_list.append(case)
                        use_col.append(checker)

    answer = len(candidate_list)
    return answer


print(solution(matrix))