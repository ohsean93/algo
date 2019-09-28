# str_origin_list = ["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]

#
# def solution(emails):
#     for email in emails:
#         email = email.split('.')
#         print(email)
#     answer = -1
#     return answer
#
#
# solution(str_origin_list)
#
# print('a.a'.replace('.', '').isalpha())


from queue import PriorityQueue

# print(list('12345').sort())
print(sorted([(7,6),(7,4),(4,5)]))
#
#
# datas = [[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]


def solution(datas):
    for i, data in enumerate(datas):
        datas[i] = [data[1], data[2], data[0]]
    sorted(datas, reverse=True)

    pq = PriorityQueue()
    answer = []
    t = datas[-1][0]
    while datas:
        while datas and datas[-1][0]:
            data = datas.pop()
