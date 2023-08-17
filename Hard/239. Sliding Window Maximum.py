import collections
import heapq


class Solution:
    """
    You are given an array of integers nums, there is a sliding window of size k
    which is moving from the very left of the array to the very right. You can only
    see the k numbers in the window. Each time the sliding window moves right by
    one position.

    Return the max sliding window.

    Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length
    """

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Use max-heap to store current largest in sliding window.
        Do not remove elements as soon as they are outside of sliding window, but
        instead when they are outside of sliding window AND largest value.
        [O(n * log(k)) / O(k)    time / space complexity is possible with fibonacci heap]
        O(n * log(n)) / O(n)    time / space complexity
        """
        # create a max heap of the first k elements
        window = [-nums[i] for i in range(k)]
        heapq.heapify(window)
        max_sliding_window = [-window[0]]

        # variable to store all values that need to be removed at some point
        neg_to_remove_counter: dict[int, int] = collections.defaultdict(lambda: 0)
        for i in range(k, len(nums)):
            neg_num = -nums[i]
            # negation of value that is now outside of sliding window
            neg_to_remove = -nums[i - k]
            neg_to_remove_counter[neg_to_remove] += 1

            # the largest value from the max-heap while it is in the to_remove_counter
            while window and neg_to_remove_counter[window[0]] > 0:
                largest_popped = heapq.heappop(window)
                neg_to_remove_counter[largest_popped] -= 1

            # push the current value into the sliding window
            heapq.heappush(window, neg_num)
            # append the current largest to the result
            max_sliding_window.append(-window[0])

        return max_sliding_window

    def max_sliding_window_alt(self, nums: list[int], k: int) -> list[int]:
        dq: collections.deque[int] = collections.deque()
        res: list[int] = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])

        return res
