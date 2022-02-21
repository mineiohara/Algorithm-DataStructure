# Linked list

from __future__ import annotations
from hashlib import new
from typing import Any

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
        if self.head is None: return

        currentNode = self.head

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
            return

        previousNode = currentNode
        currentNode = currentNode.next
        while currentNode:
            if currentNode.data == data:
                previousNode.next = currentNode.next
                return
            previousNode = currentNode
            currentNode = currentNode.next
        
                

    
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
    l.print()
