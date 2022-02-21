# Linked List

from __future__ import annotations
from hashlib import new
from typing import Any, Optional

class Node(object):
    def __init__(self, data: Any, next: Node = None) -> None:
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode
            return
        
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        
        currentNode.next = newNode
    
    def print(self) -> None:
        currentNode = self.head
        if currentNode is None: return

        while currentNode:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print()
        
    def insert(self, data: Any) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        self.head = newNode
        self.head.next = temp

    def remove(self, data: Any) -> None:
        currentNode = self.head
        if currentNode and currentNode.data == data:
            self.head = currentNode.next
            currentNode = None
            return

        previousNode = currentNode
        currentNode = currentNode.next
        while currentNode:
            if currentNode.data == data:
                previousNode.next = currentNode.next
                return
            previousNode = currentNode
            currentNode = currentNode.next
        
    def reverseIterative(self) -> None:
        previousNode = None
        currentNode = self.head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        
        self.head = previousNode

    def reverseRecursive(self) -> None:
        def _reverseRecursive_(currentNode: Node, prevNode: Node) -> Node:
            if currentNode is None: return prevNode

            nextNode = currentNode.next
            currentNode.next = prevNode

            return _reverseRecursive_(nextNode, currentNode)
        
        self.head = _reverseRecursive_(self.head, None)

    def reverseEven(self) -> None:
        def _reverseEven_(head: Node, prevNode: Node) -> Optional[Node]:
            if head is None: return None

            currentNode = head
            while currentNode and currentNode.data % 2 == 0:
                nextNode = currentNode.next
                currentNode.next = prevNode
                prevNode = currentNode
                currentNode = nextNode
            
            if currentNode != head:
                head.next = currentNode
                _reverseEven_(currentNode, None)
                return prevNode
            else:
                head.next = _reverseEven_(head.next, head)
                return head
        
        self.head = _reverseEven_(self.head, None)
                

    
if __name__ == "__main__":
    l = LinkedList()
    l.print()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.insert(7)
    l.remove(7)
    l.remove(6)
    l.remove(3)
    l.print()
    l.reverseIterative()
    l.reverseRecursive()
    l.print()
    l.reverseEven()
    l.print()
