class Solution:
    """
    Given a string containing just the characters '(' and ')', find the length of the longest valid
    (well-formed) parentheses substring.
    Constraints:
        0 <= s.length <= 3 * 10^4
        s[i] is '(', or ')'
    """

    def longestValidParentheses(self, s: str) -> int:
        # stack storing starting indexes of unclosed brackets,
        # with stack[0] storing last position where no brackets are open
        stack = [-1]

        # result variable
        res = 0

        for i, c in enumerate(s):
            if c == "(":
                # append index to opening brackets stack
                stack.append(i)
            else:
                # remove last index from stack as bracket is now closed
                stack.pop()

                # if closing bracket, and there are unclosed brackets
                if stack:
                    # current valid bracket streak is current position - last position of unclosed bracket
                    curr_streak = i - stack[-1]
                    # update res if larger
                    if curr_streak > res:
                        res = curr_streak
                else:
                    # if there are no unclosed brackets, reset stack
                    stack.append(i)
        return res


# class Solution2:
#     def longestValidParentheses(self, s: str) -> int:
#         curr_open = 0
#         opened_arr = defaultdict(list)
#         closed_arr = defaultdict(list)

#         res = 0

#         def find_new_max(biggest_so_far, opened_arr, closed_arr):
#             opens = sorted(opened_arr.items())
#             if not opens:
#                 return biggest_so_far

#             closes = sorted(closed_arr.items())
#             breakers = []
#             for level, idxs in closes:
#                 if level >= opens[0][0] - 1:
#                     break
#                 breakers.extend(idxs)
#             breakers.sort()

#             for open_level, open_idxs in opens:

#                 for open_idx in open_idxs:
#                     for close_idx in closed_arr[open_level - 1]:
#                         if bisect(a=breakers, x=open_idx) == bisect(a=breakers, x=close_idx):
#                             biggest_so_far = max(biggest_so_far, close_idx-open_idx + 1)
#                         else:
#                             break

#                 breakers.extend(closed_arr[open_level - 1])
#                 breakers.sort()

#             return biggest_so_far

#         for i, c in enumerate(s):
#             if c == '(':
#                 curr_open += 1
#                 closed_arr[curr_open].append(i)
#             else:
#                 curr_open -= 1
#                 opened_arr[curr_open].append(i)

#         return find_new_max(res, opened_arr, closed_arr)

# def longestValidParentheses(self, s: str) -> int:
#         start = 0
#         curr_open = 0

#         res = 0

#         for i, c in enumerate(s):
#             if c == '(':
#                 curr_open += 1
#             else:
#                 curr_open -= 1
#                 if curr_open == 0:
#                     res = max(res, i - start + 1)
#                 elif curr_open < 0:
#                     res = max(res, i - start)
#                     curr_open = 0
#                     start = i + 1

#         if curr_open > 0:
#             curr_open = 0
#             for i, c in enumerate(reversed(s)):
#                 if c == ')':
#                     curr_open += 1
#                 else:
#                     curr_open -= 1
#                 if curr_open < 0:
#                     res = max(res, i)
#                     break

#         return res
