class Solution:
    """
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
    and with the smallest space complexity possible.

    Constraints:
        1 <= nums.length <= 5 * 10^4
        -5 * 10^4 <= nums[i] <= 5 * 10^4
    """

    def sortArray(self, nums: list[int]) -> list[int]:
        self.heapSort(nums)
        return nums

    def heapSort(self, nums: list[int]):
        """Heapifies nums, and extracts largest value at each iteration
        O(n * log(n)) / O(1)    time / space complexity
        """
        n = len(nums)

        # build a maxheap in O(n) time
        for i in range(n // 2 - 1, -1, -1):
            self._max_heapify(nums, n, i)

        # build sorted list, from largest to smallest, in O(n * log(n)) time
        for i in range(n - 1, 0, -1):
            # at each iteration swap the largest value remaining in the max heap (at index 0),
            # with the current "end" (largest index in nums which may not be at the correct
            # position) of the array
            nums[i], nums[0] = nums[0], nums[i]

            # then heapify again to get the largest unsorted value to the top of the max heap
            self._max_heapify(nums, i, 0)

        return nums

    def _max_heapify(self, arr: list[int], n: int, root_idx: int):
        """
        Heapifies array starting from root_idx. Implemented iteratively to comply with O(1)
        space complexity rule.
        O(log(n)) / O(1)    time / space complexity
        """
        while True:
            idx_of_largest_val = root_idx  # initialize largest as root
            # in a heap the left child index is 2*i + 1
            left_child_idx = 2 * root_idx + 1
            # right child = 2*i + 2
            right_child_idx = 2 * root_idx + 2

            # left child of root exists if idx < n, update largest_idx if the left child's
            # value is larger than that of root
            if left_child_idx < n and arr[left_child_idx] > arr[idx_of_largest_val]:
                idx_of_largest_val = left_child_idx

            # same for right child
            if right_child_idx < n and arr[right_child_idx] > arr[idx_of_largest_val]:
                idx_of_largest_val = right_child_idx

            # if one of either of the children is larger than the root, swap root and child
            # and heapify previous root value at new position
            if idx_of_largest_val != root_idx:
                # swap values
                arr[root_idx], arr[idx_of_largest_val] = (
                    arr[idx_of_largest_val],
                    arr[root_idx],
                )
                root_idx = idx_of_largest_val
            else:
                # root is larger than its children, local heap property achieved
                return
