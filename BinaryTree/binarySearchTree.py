# Binary search tree

from tkinter.tix import Tree
from typing import Any

class Node(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert_(node: Node, value: Any) -> Node:
            if node is None: return Node(value)

            if value < node.value: node.left = _insert_(node.left, value)
            else: node.right = _insert_(node.right, value)

            return node
        
        _insert_(self.root, value)


    def inorder(self) -> None:
        def _inorder_(node: Node) -> None:
            if node is not None:
                _inorder_(node.left)
                print(node.value, end=" ")
                _inorder_(node.right)
        
        _inorder_(self.root)
        print()


    def search(self, value: Any) -> bool:
        def _search_(node: Node, value: Any) -> bool:
            if node is None: return False

            if node.value == value: return True
            elif node.value > value: return _search_(node.left, value)
            else: return _search_(node.right, value)
        
        return _search_(self.root, value)

    def minValue(node: Node) -> Node:
        currentNode = node
        while currentNode.left:
            currentNode = currentNode.left
        
        return currentNode

    def remove(self, value: Any) -> None:
        def _remove_(node: Node, value: Any) -> Node:
            if node is None: return Node

            if node.value > value: node.left = _remove_(node.left, value)
            elif node.value < value: node.right = _remove_(node.right, value)
            else:
                if node.left is None: return node.right
                elif node.right is None: return node.left

                temp = self.minValue(node.right)
                node.value = temp.value
                node.right = _remove_(node.right, value)
            
            return node

        _remove_(self.root, value)



if __name__ == "__main__":
    b = BinarySearchTree()
    b.insert(3)
    b.insert(1)
    b.insert(4)
    b.insert(5)
    b.insert(7)
    b.insert(10)
    b.inorder()
    print(b.search(10))
    print(b.search(20))
    b.remove(10)
    b.inorder()