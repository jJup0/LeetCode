class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Constraints:
    - nums1.length == m
    - nums2.length == n
    - 0 <= m <= 1000
    - 0 <= n <= 1000
    - 1 <= m + n <= 2000
    - -10^6 <= nums1[i], nums2[i] <= 10^6
    """

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        low_1 = 0
        high_1 = m
        while low_1 <= high_1:
            # get middle index for nums1 and nums2
            mid_1 = (low_1 + high_1) // 2
            mid_2 = (m + n + 1) // 2 - mid_1

            # from these indexes get lower and upper median candidates for each array
            # if an index is out of bounds, use inf or -inf
            upper_1 = float("inf") if mid_1 == m else nums1[mid_1]
            lower_1 = float("-inf") if mid_1 == 0 else nums1[mid_1 - 1]
            upper_2 = float("inf") if mid_2 == n else nums2[mid_2]
            lower_2 = float("-inf") if mid_2 == 0 else nums2[mid_2 - 1]

            if lower_1 <= upper_2 and lower_2 <= upper_1:
                # current "lower" median candidates are both smaller equal to
                # the "upper" median candidate of the other array
                if (m + n) % 2 == 0:
                    # even total length, take average of two middle values
                    # middle values are largest lower candidate and smallest upper candidate
                    return (max(lower_1, lower_2) + min(upper_1, upper_2)) / 2
                else:
                    # odd length, take larger of the two values
                    return max(lower_1, lower_2)
            elif lower_1 > upper_2:
                # lower median candidate of first array is larger than
                # upper median candidate of second array, index mid_1
                # (and so also high_1) is too large to be a median candidate
                high_1 = mid_1 - 1
            else:  # lower_2 > upper_1
                # analogous to case above
                low_1 = mid_1 + 1

        assert False
