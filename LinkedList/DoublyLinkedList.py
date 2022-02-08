from __future__ import annotations
from os import pread
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, previousNode: Node = None, nextNode: Node = None) -> None:
        self.data = data
        self.next = nextNode
        self.prev = previousNode

class DoublyLinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        currentNode = self.head
        while currentNode.next: currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode

    def insert(self, data: Any) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
    
    def print(self) -> None:
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

    def remove(self, data: Any) -> None:
        priviousNode = None
        currentNode = self.head

        if currentNode and currentNode.data == data:
            self.head = currentNode.next
            if self.head is not None: self.head.prev = None
            currentNode = None
            return

        while currentNode and currentNode.data != data:
            priviousNode = currentNode
            currentNode = currentNode.next
        
        if currentNode is None: return

        priviousNode.next = currentNode.next
        if currentNode.next: currentNode.next.prev = priviousNode
        currentNode = None

    def reverseIterative(self) -> None:
        previousNode = None
        currentNode = self.head

        while currentNode:
            previousNode = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = previousNode

            currentNode = currentNode.prev
        
        if previousNode:
            self.head = previousNode.prev

    def reverseRecursive(self) -> None:
        def _reverseRecursive_(currentNode: Node) -> Optional[Node]:
            if currentNode is None: return None

            previousNode = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = previousNode

            if currentNode.prev is None:
                return currentNode
            
            return _reverseRecursive_(currentNode.prev)
        
        self.head = _reverseRecursive_(self.head)
    
    def bubbleSort(self) -> None:
        if self.head is None: return

        currentNode = self.head

        while currentNode.next:
            nextNode = currentNode.next
            while nextNode:
                if currentNode.data > nextNode.data:
                    currentNode.data, nextNode.data = nextNode.data, currentNode.data

                nextNode = nextNode.next

            currentNode = currentNode.next


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(5)
    d.append(2)
    d.insert(3)
    d.reverseRecursive()
    d.reverseRecursive()
    d.bubbleSort()
    d.print()
