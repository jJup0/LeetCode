class Solution:
    def findMaximumXOR(self, nums: [int]) -> int:
        result, trie = 0, dict()
        length = max(nums).bit_length()
        for num in nums:
            curr = opposite = trie
            for digit in map(int, f'{num:b}'.zfill(length)):
                curr = curr.setdefault(digit, {})       # fills and traverses trie
                opposite = opposite.get(1 - digit) or opposite.get(digit)  # tracks largest, most opposite number

            curr['$'] = num             # terminates trie with value of the num
            result = max(result, opposite['$'] ^ num)
        return result
