from __future__ import annotations
from typing import Any

class Node(object):
    def __init__(self, data: Any, nextNode: Node=None):
        self.data = data
        self.next = nextNode

class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        newNode = Node(data)
        if self.head is None:
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
    
    def remove(self, data: Any) -> None:

if __name__ == '__main__':
    l =LinkedList()
    l.append(1)
    l.insert(2)
    print(l.head.data)
    print(l.head.next.data)
