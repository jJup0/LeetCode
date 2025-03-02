"""
You are given two 2D integer arrays nums1 and nums2.
- nums1[i] = [id_i, val_i] indicate that the number with the id id_i has a
  value equal to val_i.
- nums2[i] = [id_i, val_i] indicate that the number with the id id_i has a
  value equal to val_i.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id,
respecting the following conditions:
- Only ids that appear in at least one of the two arrays should be included in
  the resulting array.
- Each id should be included only once and its value should be the sum of the
  values of this id in the two arrays. If the id does not exist in one of the two
  arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending
order by id.

Constraints:
- 1 <= nums1.length, nums2.length <= 200
- nums1[i].length == nums2[j].length == 2
- 1 <= id_i, val_i <= 1000
- Both arrays contain unique ids.
- Both arrays are in strictly ascending order by id.
"""


class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        res: list[list[int]] = []
        i1 = i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            id1, val1 = nums1[i1]
            id2, val2 = nums2[i2]
            if id1 == id2:
                res.append([id1, val1 + val2])
                i1 += 1
                i2 += 1
            elif id1 < id2:
                res.append([id1, val1])
                i1 += 1
            else:
                res.append([id2, val2])
                i2 += 1

        while i1 < len(nums1):
            res.append(nums1[i1])
            i1 += 1
        while i2 < len(nums2):
            res.append(nums1[i2])
            i2 += 1
        return res
