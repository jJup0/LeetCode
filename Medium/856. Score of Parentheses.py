class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        # acts as a stack keeping track of score sum at a certain bracket opening level
        score_at_depth = [0]

        for c in s:
            # constraint: s consists of only '(' and ')', only two cases
            # add to stack if opening bracket
            if c == '(':
                score_at_depth.append(0)
            else:
                # if closing bracket pop score off the stack
                score = score_at_depth.pop()

                # constraint: s is a balanced parentheses string -> len(score_at_depth) >= 1
                if score == 0:
                    # if sum at current depth was 0 (case of "()") then add one to new top of stack
                    score_at_depth[-1] += 1
                else:
                    # if sum at current depth != 0, double it and add to new top
                    score_at_depth[-1] += score << 1

        # assert len(score_at_depth) == 1
        return score_at_depth[0]
