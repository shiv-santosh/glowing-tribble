import random


class BinaryTree:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def random_binary_tree():
    node = BinaryTree(int((random.random() * 20) // 1))

    node.left = BinaryTree(int((random.random() * 20) // 1))
    node.right = BinaryTree(int((random.random() * 20) // 1))

    node.left.left = BinaryTree(int((random.random() * 20) // 1))
    node.left.right = BinaryTree(int((random.random() * 20) // 1))
    node.right.left = BinaryTree(int((random.random() * 20) // 1))
    node.right.right = BinaryTree(int((random.random() * 20) // 1))

    node.left.left = BinaryTree(int((random.random() * 20) // 1))
    node.left.right = BinaryTree(int((random.random() * 20) // 1))
    node.right.left = BinaryTree(int((random.random() * 20) // 1))
    node.right.right = BinaryTree(int((random.random() * 20) // 1))

    node.left.left.left = BinaryTree(int((random.random() * 20) // 1))
    node.left.left.right = BinaryTree(int((random.random() * 20) // 1))
    node.left.right.left = BinaryTree(int((random.random() * 20) // 1))
    node.left.right.right = BinaryTree(int((random.random() * 20) // 1))
    node.right.left.left = BinaryTree(int((random.random() * 20) // 1))
    node.right.left.right = BinaryTree(int((random.random() * 20) // 1))
    node.right.right.left = BinaryTree(int((random.random() * 20) // 1))
    node.right.right.right = BinaryTree(int((random.random() * 20) // 1))
    print("-=-=-=-=-=-=-=-=-=-=-RANDOM_TREE-=-=-=-=-=-=-=-=-=-=-")
    print_tree(node)
    print("-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
    return node


def print_tree(node: BinaryTree, right=None, level=0):
    if node is None:
        return
    s = ""
    if level != 0:
        if right:
            s = ((level - 1) * "    ") + "r---"
        else:
            s = ((level - 1) * "    ") + "l---"
    # s = level * "\t"
    s += str(node.val)
    print(s)
    print_tree(node.right, True, level + 1)
    print_tree(node.left, False, level + 1)
