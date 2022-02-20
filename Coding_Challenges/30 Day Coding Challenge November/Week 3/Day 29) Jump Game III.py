class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        n = len(arr)
        i_isNew = [True]*n
        while stack:
            i = stack.pop()
            jump = arr[i]

            if not jump:
                return True

            lower = i-jump
            if lower >= 0 and i_isNew[lower]:
                stack.append(lower)
            higher = i+jump
            if higher < n and i_isNew[higher]:
                stack.append(higher)
            done[i] = False
        return False
