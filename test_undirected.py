from tree import TreeNode
from undirected_tree import find_max_path_undirected


def test_find_max_path_undirected():
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.children = [node2, node3]
    node2.children = [node4]
    node3.children = [node5]

    assert find_max_path_undirected(root) == 4
