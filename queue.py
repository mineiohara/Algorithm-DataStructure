# Queue


from typing import Any, Optional

class Queue(object):
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)
    
    def dequeue(self) -> Optional[Any]: #Equal to deque library popleft()
        if self.queue: return self.queue.pop(0)
        else: return
    
    def reverse(self) -> None:
        currentQueue = self.queue
        newQueue = []

        while currentQueue:
            newQueue.append(currentQueue.pop())
        
        self.queue = newQueue


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
    q.reverse()
    print(q.queue)