class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ret = []
        prev = start = nums[0]
        for i in range(1, len(nums)):
            # gap in nums
            if nums[i] - 1 != prev:
                ret.append(str(start) if start == prev else f"{start}->{prev}")
                start = nums[i]
                
            prev = nums[i]
                       
        ret.append(str(start) if start == prev else f"{start}->{prev}")
        return ret