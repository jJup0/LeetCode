# Below is the interface for Iterator, which is already defined for you.
# class Iterator:
#     Initializes an iterator object to the beginning of a list.
#     def __init__(self, nums: List[int]):
#
#     Returns true if the iteration has more elements.
#     def hasNext(self) -> bool:
#
#     Returns the next element in the iteration.
#     def next(self) -> int:

class PeekingIterator:
    def __init__(self, iterator):
        # use iterator given and always store the next item and hasNext in separate variables
        self.iterator = iterator
        self.has_next = self.iterator.hasNext()
        self.next_item = self.iterator.next()

    def peek(self) -> int:
        # return the next item to be returned at next()
        return self.next_item

    def next(self) -> int:
        # store next item in temporary variable
        ret = self.next_item

        # update the "next" variables
        self.has_next = self.iterator.hasNext()
        self.next_item = self.iterator.next()
        return ret

    def hasNext(self) -> bool:
        # return precalculated has next
        return self.has_next
