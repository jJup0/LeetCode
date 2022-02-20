class Solution:
    def rand10(self):
        c = (rand7() - 1)*7 + rand7() - 1  # even generation between 0 and 48
        return self.rand10() if c >= 40 else (c % 10) + 1  # try again if c more than 40, because then it is rand9 (40...48)
