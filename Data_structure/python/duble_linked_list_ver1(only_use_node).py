class Node:
    def __init__(self, data, next_node=None, front_node=None):
        self.data = data
        self.next_node = next_node
        self.front_node = front_node

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
        end_node.next_node, add_node.front_node = add_node, end_node

    # def pop(self):
    #     temp = None
    #     end_node = self
    #     while end_node.next_node:
    #         temp = end_node
    #         end_node = end_node.next_node
    #
    #     if temp:
    #         temp.next_node = None
    #         return end_node
    #     else:
    #         a = self.data
    #         self.data = None
    #         return a