class Node:
    def __init__(self, data, p_node=None, l_node=None, r_node=None):
        self.data = data
        self.p_node = p_node
        self.l_node = l_node
        self.next_node = r_node

    def __repr__(self):
        return str(self.data)


class Heap:
    def __init__(self):
        self.head = None
        self.index = 0

    def append(self, node):
        self.index += 1

        if self.head:
            target_node = self.head
            if target_node.data > node.data:
                target_node.data, node.data = node.data, target_node.data
            ind = bin(self.index)[3:][::-1]

            while len(ind) == 1:
                d = ind.pop()
                if d == '0':
                    target_node = target_node.l_node
                else:
                    target_node = target_node.r_node
                if target_node.data > node.data:
                    target_node.data, node.data = node.data, target_node.data

            if ind[0] == '0':
                target_node.l_node, node.p_node = node, target_node
            else:
                target_node.r_node, node.p_node = node, target_node

        else:
            self.head = node

    def pop(self):
        ind = bin(self.index)[3:][::-1]
        return_data = self.head.data
        target_node = self.head

        while ind:
            d = ind.pop()
            if d == '0':
                target_node = target_node.l_node
            else:
                target_node = target_node.r_node

        self.head.data = target_node.data
        target_node = None
        self.index -= 1

        up_node = self.head
        while up_node:
            if up_node.l_node:
                l = up_node.l_node.data
                if up_node.r_node:
                    r = up_node.r_node.data
                    if l > r:
                        if l > up_node.data:
                            up_node.data, up_node.l_node.data = l, up_node.data
                            up_node = up_node.l_node
                        else:
                            break
                    else:
                        if r > up_node.data:
                            up_node.data, up_node.r_node.data = r, up_node.data
                            up_node = up_node.r_node
                        else:
                            break
        return return_data
