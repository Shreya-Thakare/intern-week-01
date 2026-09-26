"""
Problem 11: Stack Implementation (LIFO)
-------------------------------------------
Implement a Stack from scratch (push, pop, peek, is_empty, size)
using a plain Python list as the underlying storage.

All operations below are O(1), except is_empty/size which are O(1)
as well since Python lists track their length.
"""


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


if __name__ == "__main__":
    s = Stack()
    for val in [1, 2, 3]:
        s.push(val)
    print("Stack after pushes:", s)
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("Stack after pop:", s)
    print("Size:", s.size())
    print("Is empty:", s.is_empty())
