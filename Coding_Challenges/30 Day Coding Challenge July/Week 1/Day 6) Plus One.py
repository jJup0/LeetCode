class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                break
        return digits
