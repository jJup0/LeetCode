from typing import List, Optional


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


# O(depth_of_deepest_nestedInteger) space
class NestedIterator:

    """
    You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

    Implement the NestedIterator class:

    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

    Your code will be tested with the following pseudocode:
        initialize iterator with nestedList
        res = []
        while iterator.hasNext()
            append iterator.next() to the end of res
        return res
    If res matches the expected flattened list, then your code will be judged as correct.

    Constraints:
        1 <= nestedList.length <= 500
        The values of the integers in the nested list is in the range [-10^6, 10^6]."""

    def __init__(self, nestedList: List["NestedInteger"]):
        # reference to original nestedList
        self.nested_list = nestedList
        # current index at nested list, start at -1 as it is incremented in inc_idx_and_update_child_iterator()
        self.idx = -1
        # iterator of nested integer if self.nested_list[self.idx] is not just an integer, have it be empty to avoid null checks
        self.child_iterator = None
        # increments the current index, and sets an sets child iterator if needed
        self.inc_idx_and_update_child_iterator()

    def inc_idx_and_update_child_iterator(self):
        self.idx += 1
        # if the new index is in bounds, and the NestedInteger at that index has is not just an integer
        if self.idx < len(self.nested_list) and (not self.nested_list[self.idx].isInteger()):
            # update the child iterator with the list of the nested integer at the current index
            self.child_iterator = NestedIterator(self.nested_list[self.idx].getList())
            # if that iterator is empty, get the next one immediately
            if not self.child_iterator.hasNext():
                self.inc_idx_and_update_child_iterator()

    def next(self) -> int:
        # get next element to be returned in iteration
        curr = self.nested_list[self.idx]
        # if it is just an integer return the value and increment index
        if curr.isInteger():
            res = curr.getInteger()
            self.inc_idx_and_update_child_iterator()
        else:
            # if the current child iterator has a next value, return it
            assert self.child_iterator != None
            res = self.child_iterator.next()
            # if that was the iterators last value, then increment index
            if not self.child_iterator.hasNext():
                self.inc_idx_and_update_child_iterator()

        return res

    def hasNext(self) -> bool:
        return self.idx < len(self.nested_list) and (self.nested_list[self.idx].isInteger() or
                                                     self.child_iterator.hasNext())  # type: ignore
