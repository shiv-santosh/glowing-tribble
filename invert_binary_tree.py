from tree import random_binary_tree, BinaryTree, print_tree


def invert_binary_tree(node: BinaryTree):
    if node is None:
        return None
    node.right, node.left = invert_binary_tree(node.left), invert_binary_tree(node.right)
    return node


if __name__ == '__main__':
    node = random_binary_tree()
    invert_binary_tree(node)
    print_tree(node)
