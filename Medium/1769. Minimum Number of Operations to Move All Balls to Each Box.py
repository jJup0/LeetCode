"""
You have n boxes. You are given a binary string boxes of length n, where
boxes[i] is'0' if the ith box is empty, and'1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is
adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be
more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of
operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

Constraints:
- n == boxes.length
- 1 <= n <= 2000
- boxes[i] is either'0' or'1'.
"""


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # res[i] = total_dist_left + total_dist_right for current index i during iteration
        total_dist_left = 0
        total_dist_right = sum(
            dist for dist, val in enumerate(boxes, start=1) if val == "1"
        )
        # total amount of balls to the left and right of current index
        ball_count_left = 0
        ball_count_right = boxes.count("1")

        prev_val = "0"
        answer: list[int] = []
        for val in boxes:
            if prev_val == "1":
                ball_count_left += 1
            total_dist_left += ball_count_left

            total_dist_right -= ball_count_right
            if val == "1":
                ball_count_right -= 1

            answer.append(total_dist_left + total_dist_right)
            prev_val = val
        return answer
