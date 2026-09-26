"""
Problem 12: Queue Implementation (FIFO)
-------------------------------------------
Implement a Queue from scratch (enqueue, dequeue, peek, is_empty, size)
using collections.deque for O(1) operations on both ends (a plain
list would make dequeue O(n) because it has to shift every element).
"""

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"


if __name__ == "__main__":
    q = Queue()
    for val in ["a", "b", "c"]:
        q.enqueue(val)
    print("Queue after enqueues:", q)
    print("Peek:", q.peek())
    print("Dequeue:", q.dequeue())
    print("Queue after dequeue:", q)
    print("Size:", q.size())
    print("Is empty:", q.is_empty())
