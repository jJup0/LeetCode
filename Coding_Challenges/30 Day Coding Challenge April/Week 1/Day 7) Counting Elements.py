# class Solution:
def countElements(self, arr: [int]) -> int:
    arr.sort()
    retVal = 0
    multiplier = 1
    i = 0
    while i < len(arr)-1:
        if (arr[i] + 1 == arr[i+1]):
            retVal += multiplier
        if (arr[i] == arr[i+1]):
            multiplier += 1
        else:
            multiplier = 1
        i += 1
    return retVal


x = countElements(0, [0, 0, 1, 1, 2, 3, 5, 7])
print(x)
