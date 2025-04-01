"""
You are given a 0-indexed 2D integer array questions where
questions[i] = [points_i, brainpower_i].

The array describes the questions of an exam, where you have to process the
questions in order (i.e., starting from question 0 ) and make a decision
whether to solve or skip each question. Solving question i will earn you
points_i points but you will be unable to solve each of the next brainpower_i
questions. If you skip question i, you get to make the decision on the next
question.
- For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
  - If question 0 is solved, you will earn 3 points but you will be unable to
    solve questions 1 and 2.
  - If instead, question 0 is skipped and question 1 is solved, you will earn 4
    points but you will be unable to solve questions 2 and 3.

Return the maximum points you can earn for the exam.

Constraints:
- 1 <= questions.length <= 10^5
- questions[i].length == 2
- 1 <= points_i, brainpower_i <= 10^5
"""


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        n = len(questions)
        # best[i] = the most amount of points reachable when answering question i, (0 <= i < n)
        # best[n] = the most amount of points reachable after finishing the exam
        best = [0] * (n + 1)
        for i, (points, brain) in enumerate(questions):
            # update best points for skipping current question
            best[i + 1] = max(best[i + 1], best[i])
            # update best points for answering current question
            next_available = min(i + brain + 1, n)
            best[next_available] = max(best[next_available], best[i] + points)
        return best[-1]


def test():
    s = Solution()
    res = s.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]])
    assert res == 5, res
