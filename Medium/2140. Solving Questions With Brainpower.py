class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        # choose[i] = max points possible for questions[i:] and choosing question i
        choose = [0] * (len(questions) + 1)
        # no_choose[i] = max points possible for questions[i:] and not choosing question i
        no_choose = [0] * (len(questions) + 1)

        # iterate through questions in reverse order
        for i in range(len(questions) - 1, -1, -1):
            points, skip = questions[i]

            # find the next possible question which can be answered if this question is chosen
            next_possible_question = min(i + skip + 1, len(questions))
            choose[i] = points + max(
                choose[next_possible_question],
                no_choose[next_possible_question],
            )
            # not choosing question i, results in the most points possible for questions[i+1:]
            no_choose[i] = max(choose[i + 1], no_choose[i + 1])

        # return maximum between choosing first question and not choosing it
        return max(choose[0], no_choose[0])
