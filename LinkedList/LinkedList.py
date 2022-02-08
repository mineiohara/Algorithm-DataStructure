from __future__ import annotations
from typing import Any, Optional
import gc

class Node(object):
    def __init__(self, data: Any, nextNode: Node = None):
        self.data = data
        self.next = nextNode

class LinkedList(object):
    def __init__(self, head = None) -> None:
        self.head = head
    
    def append(self, data: Any) -> None:
        if not self.head:
            self.head = Node(data)
            return
        
        lastNode = self.head
        while lastNode.next: lastNode = lastNode.next
        lastNode.next = Node(data)
    
    def insert(self, data: Any) -> None:
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    def print(self) -> None:
        currentNode = self.head

        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
    
    def remove(self, data: Any) -> None:
        currentNode = self.head

        if currentNode and currentNode.data == data:
            self.head = currentNode.next
            gc.collect()
            # currentNode = None
            return

        previousNode = None
        while currentNode.data != data and currentNode:
            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode is None: return

        previousNode.next = currentNode.next
    
    def reverseInterative(self) -> None:
        previousNode = None
        currentNode = self.head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        
        self.head = previousNode
    
    def reverseRecursive(self) -> None:
        def _reverseRecursive_(currentNode: Node, previousNode: Node) -> Node:
            if not currentNode: return previousNode

            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

            return _reverseRecursive_(currentNode, previousNode)
        
        self.head = _reverseRecursive_(self.head, None)

    def reverseEven(self) -> None:
        def _reverseEven_(head: Node, previousNode: Node) -> Optional[Node]:
            if head is None: return None

            currentNode = head
            while currentNode and currentNode.data % 2 == 0:
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode
            
            if currentNode != head:
                head.next = currentNode
                _reverseEven_(currentNode, None)
                return previousNode
            else:
                head.next = _reverseEven_(head.next, head)
                return head
                
        self.head = _reverseEven_(self.head, None)
        
    



if __name__ == "__main__":
    l = LinkedList()
    # l.append(1)s
    l.append(2)
    # l.append(3)
    l.append(3)
    # l.append(5)
    # l.insert(0)
    # l.append(6)
    # l.append(7)
    # l.append(2)
    # l.append(4)
    # l.append(6)
    l.print()
    print("#############")
    # l.remove(2)
    # l.print()
    # l.remove(1)
    # l.reverseEven()
    l.reverseEven()
    l.print()
