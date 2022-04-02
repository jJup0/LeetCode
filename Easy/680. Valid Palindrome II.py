class Solution:
    def validPalindrome(self, s: str) -> bool:

        # go through letters from both sides at the same time, normal palindrone check
        for i in range(len(s)//2):
            # if two letters are not the same
            if s[i] != s[-(i+1)]:
                j = len(s) - 1 - i
                # delete one of them and see if remaining string is normal palindrome
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]

        # if normal palidrome return True
        return True
