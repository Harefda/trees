import pytest

from tree import Tree, TreeNode
from directed_tree import find_max_path_directed


def test_find_max_path_directed():
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6]

    tree = Tree(root)

    assert find_max_path_directed(tree) == 10


def test_find_max_path_directed_empty_tree():
    empty_tree = Tree(None)
    with pytest.raises(ValueError):
        find_max_path_directed(empty_tree)


def test_find_max_path_directed_invalid_tree():
    invalid_tree = Tree(TreeNode(1))
    invalid_tree.root.children = "invalid"  # Неверная структура
    with pytest.raises(ValueError):
        find_max_path_directed(invalid_tree)
