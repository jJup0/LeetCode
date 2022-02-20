# copy pasta almost understood
class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        def findNsum(l, r, target, N, result, results):
            # less values than needed for sum, no actual sum, target is smaller than smallest value summed up with itself N-times |
            # target is larger than largest value summed up N-times
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N != 2:  # recursively reduce N
                for i in range(l, r+1):  # first time: i in range(0, len(nums))
                    if i == l or (nums[i-1] != nums[i]):  # dont get how this solves the problem
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
            else:  # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:  # skip same values
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
