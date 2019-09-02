import sys

sys.stdin = open("input.txt", "r")


class Node:
    def __init__(self, element, next_address=None, before_address=None):
        self.element = element
        self.next_address = next_address
        self.before_address = before_address


def insertion_node(index, origin_list_head, add_list_head):
    node = origin_list_head
    end_of_add_list_node = add_list_head
    while end_of_add_list_node.next_address:
        end_of_add_list_node = end_of_add_list_node.next_address

    if index == 0:
        end_of_add_list_node.next_address, node.before_address = node, add_list_head
        return add_list_head
    else:
        while index > 1:
            node = node.next_address
            index -= 1
        if node.next_address:
            node_1 = node
            node_2 = node.next_address
            node_1.next_address, add_list_head.before_address = add_list_head, node_1
            end_of_add_list_node.next_address, node_2.before_address = node_2, end_of_add_list_node

        else:
            node.next_address, add_list_head.before_address = add_list_head, node


        return origin_list_head


def change_my_list(origin_list):
    head = Node(origin_list.pop())
    while len(origin_list):
        new_node = Node(origin_list.pop(), head)
        head.before_address = new_node
        head = new_node

    return head


def find_index(list_head, add_list_head):
    node = list_head
    index_insertion = 0
    add_element = add_list_head.element
    while add_element >= node.element:
        node = node.next_address
        index_insertion += 1
        if node.next_address:
            continue
        else:
            if add_element >= node.element:
                index_insertion += 1
            break
    return index_insertion


def print_my_list(list_head):
    node = list_head
    num = 10
    while node.next_address:
        node = node.next_address
    while num:
        print(node.element, end=' ')
        node = node.before_address
        num -= 1
    print()


def len_my_list(list_head):
    length = 1
    end_of_list_node = list_head
    while end_of_list_node.next_address:
        end_of_list_node = end_of_list_node.next_address
        length += 1
    return length


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    origin = change_my_list(list(map(int, input().split())))

    for _ in range(M-1):
        new_list = change_my_list(list(map(int, input().split())))
        insertion_index = find_index(origin, new_list)
        origin = insertion_node(insertion_index, origin, new_list)

    print('#{}'.format(test_case), end=' ')
    print_my_list(origin)