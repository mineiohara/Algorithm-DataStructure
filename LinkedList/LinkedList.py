from __future__ import annotations
from typing import Any

class Node(object):
    def __init__(self, data: Any, nextNode: Node = None):
        self.data = data
        self.next = nextNode

class LinkedList(object):
    def __init__(self, head = None) -> None:
        self.head = head
    
    def append(self, data: Any) -> None:
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def insert(self, data: Any) -> None:
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def print(self) -> None:
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
    
    def remove(self, data: Any) -> None:
        currentNode = self.head
        if currentNode and currentNode.data == data:
            self.head = currentNode.next
            currentNode = None
            return
        
        previousNode = None
        while currentNode and currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            return
        
        previousNode.next = currentNode.next
        currentNode = None




if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    # l.print()
    l.remove(2)
    # l.print()
    l.remove(1)
    l.print()
