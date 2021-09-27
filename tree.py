import random


class BinaryTree:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def random_binary_tree(random=True):
    i = 0
    node = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right = BinaryTree(int((random.random() * 20) // 1) if random else i)

    i += 1
    node.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)

    i += 1
    node.left.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)

    i += 1
    node.left.left.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.left.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.left.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.left.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.left.right.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.left.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right.left.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right.left.right = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right.right.left = BinaryTree(int((random.random() * 20) // 1) if random else i)
    i += 1
    node.right.right.right.right = BinaryTree(int((random.random() * 20) // 1) if random else i)

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


def invert_binary_tree(node: BinaryTree):
    if node is None:
        return None
    node.right, node.left = invert_binary_tree(node.left), invert_binary_tree(node.right)
    return node


def get_height(node: BinaryTree):
    if node is None:
        return -1
    return 1 + max(get_height(node.left), get_height(node.left))


def preorder(node: BinaryTree):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


def inorder(node: BinaryTree):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def postorder(node: BinaryTree):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


def leaf_count(node: BinaryTree):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return leaf_count(node.left) + leaf_count(node.right)


if __name__ == '__main__':
    node = random_binary_tree(False)
    print(leaf_count(node))
