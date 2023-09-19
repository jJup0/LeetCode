class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        Due to the fact that there is a duplicate number, there will be a cycle,
        if entries in nums are treated as pointers to another entry in nums.
        Use Floyd's Cycle Detection Algorithm.
        O(n) / O(1)     time / space complexity
        """

        # find some point in the cycle using slow/fast method
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 1. 2 * slow_steps = fast_steps
        # let c be the cycle length, x the number of steps required to get to the
        #   first index in the cycle from the start, and y the number of steps from
        #   the meeting point of fast and slow to the first cycle index
        #
        # fast needs to reach the first cycle index, a full cycle and another (c-y) steps to intercept slow
        # 2. fast_steps = x + c + (c - y)
        #
        # # slow needs to reach the first cycle index, and takes another (c-y) to be intercepted by y
        # 3. slow_steps = x + (c - y)
        #
        # substitute 2. and 3. into 1.:
        # 2 * (x + (c - y)) = x + c + c - y
        # rearrange:
        # x = y

        # this means that from distance from intersection point to first cycle
        # index is the same as from the start to the first cycle index, so
        # start another slow step pointer and intersect again
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

    def findDuplicate_binary_search(self, nums: list[int]) -> int:
        """
        O(n * log(n)) / O(1)     time / space complexity
        """
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) >> 1
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low
