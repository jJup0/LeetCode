class slowSolution:
    def calculate(self, s: str) -> int:
        def doBinaryOperation(binop, op1, op2):
            if binop == "/":
                return op1 // op2
            if binop == "*":
                return op1 * op2
            if binop == "+":
                return op1 + op2
            if binop == "-":
                return op1 - op2

        curStr = ""
        sections = []
        for i, c in enumerate(s):
            if c in "+-*/":
                sections.append(int(curStr))
                sections.append(c)
                curStr = ""
            elif c != " ":
                curStr += c
        sections.append(int(curStr))

        for currOps in ("*/", "+-"):
            i = 0
            while i < len(sections):
                if isinstance(sections[i], str) and sections[i] in currOps:
                    op1 = sections.pop(i-1)
                    binop = sections.pop(i-1)
                    op2 = sections[i-1]
                    sections[i-1] = doBinaryOperation(binop, op1, op2)
                else:
                    i += 1
        return sections[0]


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '') + ' '
        stack = []
        prev_op = '+'
        num = "0"

        for c in s:
            if c.isdigit():
                num += c
            else:
                num = int(num)
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack[-1] *= num
                else:
                    stack[-1] //= num
                num = "0"
                prev_op = c
        return sum(stack)
