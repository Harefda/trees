def find_max_path_directed(tree):
    if tree.root is None:
        raise ValueError("Tree is empty")

    max_path = []

    def dfs(node):
        nonlocal max_path
        if not node.children:
            return [node.value]

        max_subpath = []
        for child in node.children:
            subpath = dfs(child)
            if sum(subpath) > sum(max_subpath):
                max_subpath = subpath

        path = [node.value] + max_subpath
        if sum(path) > sum(max_path):
            max_path = path

        return path

    try:
        dfs(tree.root)
    except AttributeError as e:
        raise ValueError("Wrong structure") from e

    return sum(max_path)
