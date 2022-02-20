
def mysingleNumber(nums: [int]) -> int:
    numbersDictionary = {}
    for number in nums:
        if number in numbersDictionary:
            numbersDictionary[number] = 2
        else:
            numbersDictionary[number] = 1

    for number in numbersDictionary:
        if numbersDictionary[number] == 1:
            return number


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r ^= n
        return r
