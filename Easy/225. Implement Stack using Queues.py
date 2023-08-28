from collections import deque


class MyStack:

    """
    Implement a last-in-first-out (LIFO) stack using only two queues.
    The implemented stack should support all the functions of a normal stack
    (push, top, pop, and empty).

    Constraints:
    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, top, and empty.
    - All the calls to pop and top are valid.
    Follow-up:
        Can you implement the stack using only one queue?
    """

    def __init__(self):
        # applying follow-up: only one queue
        # using only append and popleft functions of deque to simulate queue
        # queue will always be in a state that resembles a stack in terms O(1) pop operations,
        # this way peek is also in O(1), as queue[-1] would not be allowed in this challenge
        self.queue: deque[int] = deque()

    # O(n)
    # append the item to the queue and then cycle all previous items to the back of the queue,
    # maintaining the stack property
    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            temp = self.queue.popleft()
            self.queue.append(temp)

    # O(1)
    # queue is in stack order, so simply pop left
    def pop(self) -> int:
        return self.queue.popleft()

    # O(1)
    # first item in the queue is the top item in the stack
    def top(self) -> int:
        return self.queue[0]

    # O(1)
    # stack is empty iff queue is empty
    def empty(self) -> bool:
        return len(self.queue) == 0
