class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        n = len(arr)
        done = [False]*n
        while stack:
            i = stack.pop()
            jump = arr[i]
            if not jump:
                return True
            lower = i-jump
            if lower >= 0 and not done[lower]:
                stack.append(lower)
            higher = i+jump
            if higher < n and not done[higher]:
                stack.append(higher)
            done[i] = True
        return False