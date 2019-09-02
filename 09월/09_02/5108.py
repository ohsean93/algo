import sys

sys.stdin = open("input.txt", "r")


def insertion_list(index, start_node, insert_node):
    node = start_node
    while index > 1:
        node = node.next
        index -= 1
    node.next, insert_node.next = insert_node, node.next


def find_list(index, start_node):
    node = start_node
    while index > 0:
        node = node.next
        index -= 1
    return node.element


class Node:
    def __init__(self, element, next_address=None):
        self.element = element
        self.next = next_address


T = int(input())
for test_case in range(1, T + 1):
    n, m, L = map(int, input().split())
    input_list = list(map(int, input().split()))
    head = Node(input_list.pop())
    while len(input_list):
        head = Node(input_list.pop(), head)

    for _ in range(m):
        insert_index, value = map(int, input().split())
        add_node = Node(value)
        insertion_list(insert_index, head, add_node)
    ans = find_list(L, head)
    print('#{} {}'.format(test_case, ans))