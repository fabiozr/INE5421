class Node:
    def __init__(self,  value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, value):
        if self.value is None:
            self.value = value
        elif self.right is None:
            self.right = Node(value)
        elif self.left is None:
            self.left = Node(value)
        else:
            self.left.add(value)


def printTree(node: Node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + node.value)
        printTree(node.right, level + 1)

