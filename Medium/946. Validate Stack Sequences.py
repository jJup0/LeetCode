class Solution:
    """
    Given two integer arrays pushed and popped each with distinct values, return
    true if this could have been the result of a sequence of push and pop operations
    on an initially empty stack, or false otherwise.

    Constraints:
        1 <= pushed.length <= 1000
        0 <= pushed[i] <= 1000
        All the elements of pushed are unique.
        popped.length == pushed.length
        popped is a permutation of pushed.
    """

    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Check validity by simulating stack.
        O(n) / O(n)     time / space complexity
        """
        # current state of the stack
        stack = []

        # iterator over push items
        push_iter = iter(pushed)
        for pop_item in popped:
            # while the stack is empty, or the last item
            # does not match, push the next item
            while not stack or stack[-1] != pop_item:
                push_val = next(push_iter, None)
                # if the iterator is exhausted, then the sequence is invalid
                if push_val is None:
                    return False

                stack.append(push_val)
            # last item on the stack matches up with pop_item, so pop from the stack
            stack.pop()

        # if every pop item has been matched, return true
        return True
