# Doubly Linked List

from __future__ import annotations
from typing import Any, Optional

class Node(object):
    def __init__(self, data: Any, prev: Node = None, next: Node = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.next: currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode
    
    
    def print(self) -> None:
        currentNode = self.head
        if currentNode is None: return

        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print()

    def insert(self, data: Any) -> None:
        temp = self.head
        if temp is None: 
            self.head = Node(data)
            return
        
        newNode = Node(data, None, temp)
        temp.prev = newNode
        self.head = newNode

    def remove(self, data: Any) -> None:
        currentNode = self.head

        if currentNode and currentNode.data == data:
            self.head = currentNode.next
            if currentNode.next is not None: currentNode.next.prev = self.head
            currentNode = None
            return

        while currentNode and currentNode.data != data:
            currentNode = currentNode.next
        
        if currentNode is None: return

        prevNode = currentNode.prev
        prevNode.next = currentNode.next

        if currentNode.next is not None: currentNode.next.prev = prevNode
        
        currentNode = None


    def reverseIterative(self) -> None:
        currentNode = self.head

        while currentNode:
            prevNode = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = prevNode
            currentNode = currentNode.prev
        
        if prevNode: self.head = prevNode.prev

    def reverseRecursive(self) -> None:
        def _reverseRecursive_(currentNode: Node) -> Optional[Node]:
            if currentNode is None: return None

            prevNode = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = prevNode

            if currentNode.prev is None: return currentNode

            return _reverseRecursive_(currentNode.prev)

        self.head = _reverseRecursive_(self.head)

    def sort(self) -> None:
        if self.head is None: return

        currentNode = self.head
        while currentNode.next:
            nextNode = currentNode.next
            while nextNode:
                if currentNode.data > nextNode.data: currentNode.data, nextNode.data = nextNode.data, currentNode.data
                nextNode = nextNode.next
            
            currentNode = currentNode.next


if __name__ == "__main__":
    l = DoublyLinkedList()
    l.insert(0)
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.append(7)
    l.insert(-1)
    l.print()
    l.remove(3)
    l.print()
    l.append(0)
    l.append(1)
    l.append(1)
    l.append(1)
    l.append(1)
    l.print()
    l.remove(0)
    l.remove(1)
    l.remove(3)
    l.print()
    l.reverseIterative()
    l.reverseRecursive()
    l.print()
    l.sort()
    l.print()