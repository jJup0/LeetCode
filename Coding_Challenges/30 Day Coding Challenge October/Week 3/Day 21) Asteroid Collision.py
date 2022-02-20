# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         i = 1
#         while i < len(asteroids):
#             # print(i, end=" ")
#             cur, prev = asteroids[i], asteroids[i-1]
#             if cur < 0 and prev > 0:
#                 if abs(cur) > prev:
#                     asteroids.pop(i-1)
#                     i -= 1
#                 elif abs(cur) < prev:
#                     asteroids.pop(i)
#                 else:
#                     asteroids.pop(i-1)
#                     asteroids.pop(i-1)
#                     i -= 1
#             else:
#                 i += 1
#             i = max(i, 1)
#             # print("new i:", i, asteroids)
#         return asteroids


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [float('-inf')]
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:  # negative velocity asteroid crashing
                while stack[-1] > 0 and stack[-1] <= -asteroid:
                    if stack.pop() == -asteroid:
                        break
                else:
                    if stack[-1] < 0:
                        stack.append(asteroid)
        return stack[1:]
