class Solution:
    def decodeString(self, s: str) -> str:
        operand_stack = [[]]
        multiplier_stack = []
        for i, c in enumerate(s):
            if c.isdigit():
                if s[i-1].isdigit():
                    multiplier_stack[-1] = multiplier_stack[-1] * 10 + (int(c))
                else:
                    multiplier_stack.append(int(c))
            elif c.isalpha():
                operand_stack[-1].append(c)
            elif c == '[':
                operand_stack.append([])
            else:  # if c == ']'
                amount = multiplier_stack.pop()
                word = operand_stack.pop()
                operand_stack[-1].extend(word*amount)
        return ''.join([''.join(o) for o in operand_stack])