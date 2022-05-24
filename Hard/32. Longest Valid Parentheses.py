import random


class Solution:
    """
    Given a string containing just the characters '(' and ')', find the length of the longest valid
    (well-formed) parentheses substring.
    Constraints:
        0 <= s.length <= 3 * 10^4
        s[i] is '(', or ')'
    """

    def longestValidParentheses(self, s: str) -> int:
        # stack storing longest valid parentheses at current depth so far, and starting index
        # stacks have equal size at each iteration
        streak_stack = [0]
        i_stack = [0]

        # result variable
        res = 0

        for i, c in enumerate(s):
            if c == '(':
                i_stack.append(i)
                streak_stack.append(0)
            else:
                # if closing bracket, and there are unclosed brackets
                if len(i_stack) > 1:
                    # delete last streak at depth as opening bracket depth is now lower
                    streak_stack.pop()

                    # get last index of previous depth
                    prev_i = i_stack.pop()

                    # calculate new valid bracket length, current length plus previous streak
                    valid_brack_length = i - prev_i + 1 + streak_stack[-1]

                    # update res if longer
                    if valid_brack_length > res:
                        res = valid_brack_length

                    # update streak of current depth
                    streak_stack[-1] = valid_brack_length
                else:
                    # if there are no unclosed brackets, reset both stacks
                    i_stack[0] = i + 1
                    streak_stack[0] = 0

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
