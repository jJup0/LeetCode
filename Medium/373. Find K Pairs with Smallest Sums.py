import heapq


class Solution:
    """
    You are given two integer arrays nums1 and nums2 sorted in ascending order
    and an integer k.

    Define a pair (u, v) which consists of one element from the first array and
    one element from the second array.

    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
    Constraints:
    - 1 <= nums1.length, nums2.length <= 10^5
    - -10^9 <= nums1[i], nums2[i] <= 10^9
    - nums1 and nums2 both are sorted in ascending order.
    - 1 <= k <= 10^4
    """

    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        # heap of pairs, each entry contains pair sum,
        # index from nums1 and index from nums2
        heap: list[tuple[int, int, int]] = [(nums1[0] + nums2[0], 0, 0)]
        # pairs of indexes already added to the heap
        visited: set[tuple[int, int]] = set([(0, 0)])

        res: list[list[int]] = []
        while k and heap:
            # get smallest pair from heap, and append it to result
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            # keep same number for nums1, and take next biggest number in nums2,
            # and add to the queue if not yet visited
            new_j = j + 1
            if new_j < len(nums2) and (i, new_j) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[new_j], i, new_j))
                visited.add((i, new_j))

            # analogously for keeping number from nums2
            new_i = i + 1
            if new_i < len(nums1) and (new_i, j) not in visited:
                heapq.heappush(heap, (nums1[new_i] + nums2[j], new_i, j))
                visited.add((new_i, j))

            k -= 1

        return res
