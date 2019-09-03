import sys

sys.stdin = open("input.txt", "r")


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node

    def __str__(self):
        node = self
        return_list = []
        while node.next_node:
            return_list.append(str(node.element))
            node = node.next_node
        return_list.append(str(node.element))
        return ' '.join(return_list)


def insertion(add_index, element, list_head):

    if add_index == 0:
        new_node = Node(element, list_head)
        return new_node
    else:
        node = list_head
        while add_index > 1:
            node = node.next_node
            add_index -= 1
        new_node = Node(element)
        if node.next_node:
            node.next_node, new_node.next_node = new_node, node.next_node
        else:
            node.next_node = new_node
        return list_head


def delete(target_index, list_head):
    if target_index == 0:
        return list_head.next_node
    else:
        node = list_head
        while target_index > 1:
            target_index -= 1
            node = node.next_node
        if node.next_node:
            node2 = node.next_node
            node.next_node = node2.next_node
        else:
            node = None
        return list_head


def change(target_index, list_head, element):
    node = list_head
    while target_index > 0:
        node = node.next_node
        target_index -= 1
    node.element = element


def my_list(origin_list):
    list_head = Node(origin_list.pop())
    while origin_list:
        list_head = Node(origin_list.pop(), list_head)
    return list_head


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    origin = list(map(int, input().split()))
    head = my_list(origin)
    for _ in range(M):
        print(head)
        input_list = input().split()
        if input_list[0] == 'I':
            index = int(input_list[1])
            num = int(input_list[2])
            head = insertion(index, num, head)
            N += 1
        elif input_list[0] == 'C':
            index = int(input_list[1])
            num = int(input_list[2])
            change(index, head, num)
        elif input_list[0] == 'D':
            index = int(input_list[1])
            head = delete(index, head)
            N -= 1
    print(head)
    ans = 0
    if L > N:
        ans = -1
    else:
        node = head
        while L > 0:
            node = node.next_node
            L -= 1
        ans = node.element

    print('#{} {}'.format(test_case, ans))