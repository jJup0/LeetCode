def prevthreeSumClosest(self, nums: [int], target: int):
    nums.sort()
    pos_set = set()
    neg_set = set()
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            neg_set.add(nums[i])
        else:
            for j in range(i, len(nums)):
                pos_set.add(nums[j])
            break
        i += 1
    print(pos_set, neg_set)
    smallest_Diff_i = (2 >> 31, None)
    prevDiff = 2 >> 31

    for i, val in enumerate(nums):
        curDiff = abs(target - val)
        if curDiff < smallest_Diff_i[0]:
            smallest_Diff_i = (curDiff, i)
        elif prevDiff < curDiff:
            break
        prevDiff = curDiff


def pileOfShitThreeSumClosest(self, nums: [int], target: int):
    nums.sort()
    nums = tuple(nums)
    lenNums = len(nums)
    seen = set()
    best_diff = 2 << 31
    for i in range(lenNums - 2):
        print('new i')
        for j in range(i, lenNums - 1):
            diff = target - nums[i] - nums[j]
            if diff in seen:
                continue
            seen.add(diff)
            l_b_diff = 2 << 31  # best
            l_pre_diff = 2 << 31  # previous
            for x in range(3):
                if x == 0:
                    i1, j1 = 0, i
                elif x == 1:
                    i1, j1 = i + 1, j
                elif x == 2:
                    i1, j1 = j + 1, lenNums
                for k in range(i1, j1):
                    l_cur_diff = diff + nums[k]
                    if abs(l_cur_diff) > abs(l_pre_diff):
                        break
                    if abs(l_cur_diff) < l_b_diff:
                        l_b_diff = l_cur_diff
                    l_pre_diff = l_cur_diff
            if abs(l_b_diff) < abs(best_diff):
                best_diff = l_b_diff

    return best_diff


class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        numsLen = len(nums)
        closest = []
        for i in range(0, len(nums) - 2):
            l, r = i+1, numsLen-1
            if nums[i] + nums[r] + nums[r-1] < target:  # if current value plus two biggest values is smaller than target, append
                closest.append(nums[i]+nums[r]+nums[r-1])
            elif nums[i]+nums[l]+nums[l+1] > target:  # if current value plus next two is bigger than target append
                closest.append(nums[i]+nums[l]+nums[l+1])
            else:
                while l < r:  # zero in from both sides to get closer to target
                    mysum = nums[i]+nums[l]+nums[r]
                    closest.append(mysum)
                    if mysum < target:
                        l += 1
                    elif mysum > target:
                        r -= 1
                    else:
                        return target
        closest.sort(key=lambda x: abs(x-target))  # sort closest[] according to the distance from target
        return closest[0]
