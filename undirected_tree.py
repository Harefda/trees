class UndirectedTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def find_max_path_undirected(root):
    max_path = []
    max_sum = float("-inf")

    def dfs(node, parent):
        nonlocal max_path, max_sum
        path = [node.value]
        curr_sum = node.value

        for child in node.children:
            if child != parent:
                child_path, child_sum = dfs(child, node)
                curr_sum += child_sum

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_path = path + child_path

                if child_sum > max_sum:
                    max_sum = child_sum
                    max_path = child_path

        return path, curr_sum

    dfs(root, None)
    return sum(max_path)
