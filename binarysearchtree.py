class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)


class Binarysearchtree:
    def __init__(self):
        self.root = None
        self.n = 0

    def __str__(self):
        pass

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while curr:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = new_node
                        curr.left.parent = curr
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new_node
                        curr.right.parent = new_node
                        break
                    else:
                        curr = curr.right

    def search(self, value):
        curr = self.root
        if self.root is None:
            return 'Empty Tree'
        else:
            while curr:
                if curr is None or curr.value is value:
                    return curr
                elif value < curr.value:
                    if curr.left is None:
                        return None
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        return None
                    else:
                        curr = curr.right

    def delete(self, value):
        pass

    # helper function for delete method
    def _delete(self, node):
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right is node:
                    node.parent.right = None
                else:
                    node.parent.left = None
        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = node
                self.root = child_node
            else:
                if node.parent.right is node:
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                child_node.parent = node.parent
        else:
            successor = self.successor(node)
            node.value = successor.value
            self._delete(successor)

    def successor(self, node):
        if node is None:
            return None
        if node.right is None:
            return None
        else:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr


    def traverse(self, order):
        if order == 'inorder':
            yield from self.in_order(self.root)
        elif order == 'preorder':
            yield from self.pre_order(self.root)
        elif order == 'postorder':
            yield from self.post_order(self.root)
        else:
            return 'Unknown order'


    def successor(self, node):
        if node is None:
            return None

        if node.right is None:
            return None
        else:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr


    def in_order(self, node):
        if node:
            yield from self.in_order(node.left)
            yield (node.value)
            yield from self.in_order(node.right)


    def pre_order(self, node):
        if node:
            yield (node.value)
            yield from self.pre_order(node.left)
            yield from self.pre_order(node.right)


    def post_order(self, node):
        if node:
            yield from self.post_order(node.left)
            yield from self.post_order(node.right)
            yield (node.value)


if __name__ == '__main__':
    bs = Binarysearchtree()
    a = [13, 7, 3, 8, 15, 14, 19, 21]
    for i in a:
        bs.insert(i)
    
    bs.delete(21)
    element = []
    for i in bs.traverse('preorder'):
        element.append(i)

    print(element)