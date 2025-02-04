class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.n = 0

    def __len__(self):
        return self.n

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
                        curr.right.parent = curr
                        break
                    else:
                        curr = curr.right

    def search(self, value):
        if self.root is None:
            return 'Empty tree'
        else:
            curr = self.root
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
        node = self.search(value)
        if node is None:
            raise ValueError('Value does not exist')
        else:
            self._delete(node=node)

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
            node.parent = node.left = node.right = None
        else:
            successor = self.successor(node)
            node.value = successor.value
            self._delete(successor)

    def successor(self, node):
        if node is None:
            return 'No Successor'

        if node.right is None:
            return None
        else:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

    def traverse(self, order):
        if order == 'inorder':
            yield from self.in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self.pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self.post_order_traversal(self.root)
        else:
            return 'Unknown order'

    def in_order_traversal(self, node):
        if node:
            yield from self.in_order_traversal(node.left)
            yield node.value
            yield from self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            yield node.value
            yield from self.pre_order_traversal(node.left)
            yield from self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            yield from self.post_order_traversal(node.left)
            yield from self.post_order_traversal(node.right)
            yield node.value


if __name__ == '__main__':
    bst = BinarySearchTree()
    a = [10, 6, 8, 13, 14, 15, 17, 12]
    for i in a:
        bst.insert(i)

    elements = []
    for i in bst.traverse('postorder'):
        elements.append(i)
    print(elements)

    bst.delete(14)
    elements = []
    for i in bst.traverse('preorder'):
        elements.append(i)
    print(elements)
