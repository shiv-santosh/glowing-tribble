import tree


def dfs(node: tree.BinaryTree):
    if node is None:
        return None
    print(node.val)
    dfs(node.left)
    dfs(node.right)


if __name__ == '__main__':
    tree = tree.random_binary_tree()
    dfs(tree)
