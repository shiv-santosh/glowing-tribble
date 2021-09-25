from tree import random_binary_tree, BinaryTree


def bfs(node: BinaryTree, stk=None):
    if stk is None:
        stk = []
    print(node.val)
    if node.left is not None:
        stk.insert(0, node.left)
    if node.right is not None:
        stk.insert(0, node.right)
    if not bool(stk):
        return
    next = stk.pop()
    bfs(next, stk)


if __name__ == '__main__':
    node = random_binary_tree()
    bfs(node)
