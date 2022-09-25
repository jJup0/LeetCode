class MyCircularQueue:
    """
    Design your implementation of the circular queue. The circular queue is a linear data structure
    in which the operations are performed based on FIFO (First In First Out) principle and the last
    position is connected back to the first position to make a circle. It is also called
    "Ring Buffer".
    One of the benefits of the circular queue is that we can make use of the spaces in front of the
    queue. In a normal queue, once the queue becomes full, we cannot insert the next element even
    if there is a space in front of the queue. But using the circular queue, we can use the space
    to store new values.
    Implementation the MyCircularQueue class:
        MyCircularQueue(k) Initializes the object with the size of the queue to be k.
        int Front() Gets the front item from the queue. If the queue is empty, return -1.
        int Rear() Gets the last item from the queue. If the queue is empty, return -1.
        boolean enQueue(int value) Inserts an element into the circular queue. Return true if the
            operation is successful.
        boolean deQueue() Deletes an element from the circular queue. Return true if the operation
            is successful.
        boolean isEmpty() Checks whether the circular queue is empty or not.
        boolean isFull() Checks whether the circular queue is full or not.
    You must solve the problem without using the built-in queue data structure in your programming 
    language. 
    Constraints:
        1 <= k <= 1000
        0 <= value <= 1000
        At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
    """

    def __init__(self, k: int):
        self.q = [0] * k  # list to use as a queue
        self.front = 0  # index of current front value
        self.rear = -1  # index of current rear value
        self.count = 0  # current amount of items in queue
        self.size = k  # maximum size of queue

    def enQueue(self, value: int) -> bool:
        # if queue is full, cannot enqueue
        if self.isFull():
            return False
        # update rear index, add value to queue and update current size, return success
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        # if queue is empty, cannot dequeue
        if self.isEmpty():
            return False
        # update front index, update current size, return success
        self.count -= 1
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
