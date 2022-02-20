class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        A.sort()
        possibleHours = []
        for i in range(4):  # find possible hours
            tens = A[i]
            if tens > 2:
                break
            possibleHours += [(tens, units) for units in A[:i]+A[i+1:] if tens*10 + units < 24]
        for tens, units in reversed(possibleHours):  # find minutes for possible hours
            A.remove(tens)
            A.remove(units)
            for i1, i2 in ((1, 0), (0, 1)):
                if A[i1] * 10 + A[i2] < 60:
                    return f'{tens}{units}:{A[i1]}{A[i2]}'
            A += [tens, units]
        return ''
