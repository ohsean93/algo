import sys

sys.stdin = open("input.txt", "r")


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


def my_list(origin_list):
    my_list_head = Node(origin_list.pop())
    while origin_list:
        my_list_head = Node(origin_list.pop(), my_list_head)

    return my_list_head


def insertion(add_index, list_head):
    if add_index == 0:
        node = list_head
        while node.next_node:
            node = node.next_node
        node.next_node = Node(node.element+list_head.element)
        return list_head

    else:
        node = list_head
        while add_index > 1:
            node = node.next_node
            add_index -= 1
        if node.next_node:
            node2 = node.next_node
            new_node = Node(node.element + node2.element, node2)
            node.next_node = new_node
            return list_head
        else:
            node.next_node = Node(node.element)
            return list_head


def change_list(list_head):
    return_list = []
    node = list_head
    while node.next_node:
        return_list.append(str(node.element))
        node = node.next_node
    return_list.append(str(node.element))
    return return_list


T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    origin = list(map(int, input().split()))

    head = my_list(origin)
    temp = change_list(head)
    index = 0
    for _ in range(K):
        index = (index + M) % N

        head = insertion(index, head)
        if index == 0:
            index = N

        N += 1

    temp = change_list(head)
    temp.reverse()
    print('#{} {}'.format(test_case, ' '.join(temp[:10])))

