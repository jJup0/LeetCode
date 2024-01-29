"""
Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue (push,
peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only push to
  top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may
  simulate a stack using a list or deque (double-ended queue) as long as you
  use only a stack's standard operations.

Constraints:
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.
"""


class MyQueue:
    def __init__(self):
        self.stack: list[int] = []

    def push(self, x: int) -> None:
        """
        O(n) / O(n)   time / space complexity
        """
        # empty the stack by extracting items into a new stack
        temp_stack: list[int] = []
        while self.stack:
            temp_stack.append(self.stack.pop())

        # push the new element to the bottom of the stack (back of the queue)
        self.stack.append(x)

        # place back the elements from temporary stack
        while temp_stack:
            self.stack.append(temp_stack.pop())

    def pop(self) -> int:
        """
        O(1) / O(1)   time / space complexity
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        O(1) / O(1)   time / space complexity
        """
        ret = self.stack.pop()
        self.stack.append(ret)
        return ret

    def empty(self) -> bool:
        """
        O(1) / O(1)   time / space complexity
        """
        return len(self.stack) == 0
