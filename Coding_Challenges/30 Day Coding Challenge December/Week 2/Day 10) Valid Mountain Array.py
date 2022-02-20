class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3) or arr[1] < arr[0]:
            return False
        increasing = True
        prev = -1
        for x in arr:
            if x == prev:
                return False
            if ((x > prev) != increasing):
                if not increasing:
                    return False
                increasing = False
            prev = x
        return not increasing
