class Solution:
    """
    Given an integer array nums and an integer k, return the number of non-empty subarrays that
    have a sum divisible by k.

    A subarray is a contiguous part of an array.

    Constraints:
        1 <= nums.length <= 3 * 10^4
        -10^4 <= nums[i] <= 10^4
        2 <= k <= 10^4
    """

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        A subarray A[i:j] is divisible by k if A[:i] % k == A[:j] % k, because when their sums are
        subtracted from another the result modulo k is 0.

        Count occurances of modulos, then apply n choose 2 formula. Subarrays A[:i] which are
        already divisible by k are added separately

        O(n) / O(1)     time / space complexity
        """

        # modulo buckets
        buckets = [0] * k
        # current running sum
        curr_sum = 0
        for num in nums:
            # update sum and bucket count
            curr_sum += num
            buckets[curr_sum % k] += 1

        # subarrays nums[:i] are already divisible
        res = buckets[0]
        for bucket_count in buckets:
            # for all other subarrays of the same modulo class, each pair i, j
            # A[i:j] is divisible by k
            res += bucket_count * (bucket_count-1) // 2
        return res
