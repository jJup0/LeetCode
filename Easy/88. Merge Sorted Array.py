from typing import List


class Solution:
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
    be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    Constraints:
        nums1.length == m + n
        nums2.length == n
        0 <= m, n <= 200
        1 <= m + n <= 200
        -10^9 <= nums1[i], nums2[j] <= 10^9
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        O(n + m) time, O(1) space
        """
        # insert poisition
        insert = m + n - 1
        # index for nums1
        i = m - 1
        # index for nums2
        j = n - 1

        # while indexes of both are in bounds, merge from higher end
        while j >= 0 and i >= 0:
            # if current nums2 item is bigger, insert it, otherwise insert from nums1
            if nums2[j] >= nums1[i]:
                nums1[insert] = nums2[j]
                j -= 1
            else:
                nums1[insert] = nums1[i]
                i -= 1
            insert -= 1

        # if not all of nums2 has been inserted, do so
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1

        # if not all of nums1 has been inserted does not need to be handled,
        # as the values are already in position
