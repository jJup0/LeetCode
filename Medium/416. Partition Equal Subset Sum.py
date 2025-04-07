class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """Check all combinations of sums of numbers and if it equals half the total sum.

        Complexity:
            Time: O(2^n)
            Space: O(2^n)
        """
        total_sum = sum(nums)
        if total_sum & 1:
            # odd sum, cannot split
            return False

        target = total_sum // 2
        reachable_sums = set([0])
        for num in nums:
            reachable_sums.update([prev + num for prev in reachable_sums])
            if target in reachable_sums:
                return True
        return False

    def canPartition2(self, nums: list[int]) -> bool:
        """Use bigint bitmap instead of set.

        Complexity:
            Time: O(n * sum(nums))
            Space: O(sum(nums))
        """
        total = sum(nums)
        if total & 1:
            return False

        target = total // 2
        bitmap_reachable_sums = 1 << 0
        for num in nums:
            bitmap_reachable_sums |= bitmap_reachable_sums << num

        return (bitmap_reachable_sums & (1 << target)) != 0


def test():
    import random
    import time
    from typing import Any, Callable

    def time_func(func: Callable[[], Any], description: str = "") -> Any:
        t1 = time.perf_counter_ns()
        res = func()
        t2 = time.perf_counter_ns()
        print(f"{(t2 - t1)/1_000_000:.2f}ms for {description}")
        return res

    s = Solution()
    res = s.canPartition([3, 3, 3, 4, 5])
    assert res

    for magnitude, n in [(6, 40), (9, 10)]:
        max_num = 10**magnitude
        arr = [random.randint(1, max_num) for _ in range(n)]
        if sum(arr) & 1:
            arr[-1] += 1
        print(f"\n{n=} {max_num=}, unique numbers={len(set(arr))}")
        res = time_func(lambda: s.canPartition(arr), f"Set")
        res = time_func(lambda: s.canPartition2(arr), f"Bitmap")
