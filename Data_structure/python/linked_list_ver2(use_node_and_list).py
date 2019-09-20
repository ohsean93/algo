class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        if node:
            self.length = 1
        else:
            self.length = 0
        return

    def __repr__(self):
        if self.length:
            return_list = [self.head.data]
            end_node = self.head
            while end_node.next_node:
                end_node = end_node.next_node
                return_list.append(end_node.data)
            return str(return_list)
        else:
            return 'empty'

    def append(self, node):
        self.length += 1
        if self.length:
            end_node = self.head
            while end_node.next_node:
                end_node = end_node.next_node
            end_node.next_node = node
        else:
            self.head = node

    def pop(self):
        if self.length:
            self.length -= 1
        else:
            return 'error'
        temp = None
        end_node = self.head
        while end_node.next_node:
            temp = end_node
            end_node = end_node.next_node

        return_value = end_node.data
        if temp:
            temp.next_node = None
        else:
            self.head = None
        return return_value


a = LinkedList(Node(10))
a.append(Node(5))
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)