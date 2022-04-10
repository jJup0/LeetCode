from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # keep record like a stack
        record = []
        # iterate through all operations
        for op in ops:
            # if "+" add previous two scores to record
            if op == "+":
                record.append(record[-1] + record[-2])
            # if "C" delete last record
            elif op == "C":
                record.pop()
            # if "C" add duplicate of last record
            elif op == "D":
                record.append(record[-1] * 2)
            # else value is an integer, so add integer value to stack
            else:
                record.append(int(op))

        # return sum of stack
        return sum(record)
