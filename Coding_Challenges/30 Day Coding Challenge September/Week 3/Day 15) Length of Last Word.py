class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s.rstrip()
        return len(s) - s.rfind(" ") - 1
