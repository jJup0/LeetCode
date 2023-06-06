class Solution:
    """
    A sequence of numbers is called an arithmetic progression if the difference
    between any two consecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged to
    form an arithmetic progression. Otherwise, return false.

    Constraints:
        2 <= arr.length <= 1000
        -10^6 <= arr[i] <= 10^6
    """

    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        prev = arr[1]
        for i in range(2, len(arr)):
            num = arr[i]
            if num - prev != diff:
                return False
            prev = num
        return True
