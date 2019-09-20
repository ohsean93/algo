"""
1 노드와 링크드 리스트를 합쳐서 정의
장점 : 점들만 정의하고 연결하므로 메모리에 유리 (점 이외의 코스트가 없다.)
단점 : 출력 형식이 점(원소) 하나와 길이가 1인 리스트가 같다. 즉 리스트인지 노드인지 구분이 불가하다.
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        if self.next_node:
            return_list = [self.data]
            end_node = self
            while end_node.next_node:
                end_node = end_node.next_node
                return_list.append(end_node.data)
            return str(return_list)
        else:
            return str(self.data)

    def append(self, add_node):
        end_node = self
        while end_node.next_node:
            end_node = end_node.next_node
        end_node.next_node = add_node

    def pop(self):
        temp = None
        end_node = self
        while end_node.next_node:
            temp = end_node
            end_node = end_node.next_node

        if temp:
            temp.next_node = None
            return end_node
        else:
            a = self.data
            self.data = None
            return a


a = Node(10)
a.append(Node(5))
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)