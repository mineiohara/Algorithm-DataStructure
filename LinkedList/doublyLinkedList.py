# Doubly Linked List

from __future__ import annotations
from dataclasses import dataclass
from hashlib import new
from typing import Any

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
        while currentNode:
            print(currentNode.data, end=" ")
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
        pass

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
