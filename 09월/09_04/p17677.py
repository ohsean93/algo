input_list = [
    ('FRANCE', 'french'),
    ('handshake', 'shake hands'),
    ('aa1+aa2', 'AAAA12'),
    ('E=M*C^2', 'e=m*c^2'),
]


def solution(str1, str2):
    matrix_str1 = doc_list(str1)
    matrix_str2 = doc_list(str2)

    cup_num, co_num = 0, 0
    for i in range(0, 27):
        for j in range(0, 27):
            cup_num += min(matrix_str1[i][j], matrix_str2[i][j])
            co_num += max(matrix_str1[i][j], matrix_str2[i][j])

    if co_num == 0:
        answer = 65536
    else:
        answer = 65536*cup_num//co_num
    return answer


def doc_list(origin_str):
    temp = 0
    return_list = [[0] * 27 for _ in range(27)]
    for char in origin_str:  # type: str
        ord_char = ord(char.lower()) - 96
        if temp:
            if 1 <= ord_char <= 26:
                return_list[temp][ord_char] += 1
                temp = ord_char
            else:
                temp = 0
        else:
            if 1 <= ord_char <= 26:
                temp = ord_char

    return return_list


print(ord('a') - 96, ord('z') - 96)
for str_1, str_2 in input_list:
    print(solution(str_1, str_2))