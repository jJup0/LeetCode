class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strnums = [str(n) for n in nums]
        strnums = [f"{n}{n[0]}{n[-1]}" for n in strnums]  # adds first and last digits to ensure eg 12 comes before 121 when sorting
        strnums.sort(reverse=True)
        strnums = [n[:-2] for n in strnums]  # take those added digits away again
        retVal = ''.join(strnums).lstrip("0")
        return retVal or "0"

# class Comparator(str):
#     def __lt__(self, other):
#         return self+other < other+self

# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         if not nums: return ""
#         nums = list(map(str, nums))
#         nums.sort(reverse=True, key=Comparator)
#         return "".join(nums) if nums[0] != "0" else "0"
