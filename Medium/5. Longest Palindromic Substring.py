class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        char_list = ['>'] + list(s) + ['$']

        palindrome_ranges = [(i, i) for i in range(1, len(char_list)-1)]
        prev = '#'
        for i, c in enumerate(char_list):
            if c == prev:
                palindrome_ranges.append((i-1, i))
            prev = c

        res_range = palindrome_ranges[-1]
        while palindrome_ranges:
            res_range = palindrome_ranges[-1]
            new_seeds = []
            for i, j in palindrome_ranges:
                if char_list[i-1] == char_list[j+1]:
                    new_seeds.append((i-1, j+1))
            palindrome_ranges = new_seeds

        return s[res_range[0]-1:res_range[1]]


S = Solution()
s = "babad"
print(S.longestPalindrome(s))
s = "xabbay"
print(S.longestPalindrome(s))
