"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10
slots:'0','1','2','3','4','5','6','7','8','9'. The wheels can rotate freely and
wrap around: for example we can turn'9' to be'0', or'0' to be'9'. Each move
consists of turning one wheel one slot.

The lock initially starts at'0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of
these codes, the wheels of the lock will stop turning and you will be unable to
open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it
is impossible.

Constraints:
- 1 <= deadends.length <= 500
- deadends[i].length == 4
- target.length == 4
- target will not be in the list deadends.
- target and deadends[i] consist of digits only.
"""


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        d := digits of lock, here 4
        O(10^d) / O(10^d)     time / space complexity
        """
        target_int = int(target)
        if target_int == 0:
            return 0

        deadends_set = set(int(d) for d in deadends)
        if 0 in deadends_set:
            return -1

        visited = [False] * 10000
        visited[0] = True
        queue = [0]
        steps = 0
        while queue:
            steps += 1
            new_queue: list[int] = []
            for code in queue:
                magnitude = 1
                while magnitude <= 1000:
                    digit = (code // magnitude) % 10
                    if digit == 9:
                        code1 = code - 9 * magnitude
                    else:
                        code1 = code + magnitude
                    if digit == 0:
                        code2 = code + 9 * magnitude
                    else:
                        code2 = code - magnitude

                    for new_code in (code1, code2):
                        if new_code == target_int:
                            return steps
                        if new_code in deadends_set:
                            continue
                        if not visited[new_code]:
                            new_queue.append(new_code)
                            visited[new_code] = True
                    magnitude *= 10
            queue = new_queue
        return -1
