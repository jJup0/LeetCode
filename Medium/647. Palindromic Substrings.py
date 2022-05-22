class Solution:
    def countSubstrings(self, s: str) -> int:
        # left and right pointer in string from where to build palindrome
        l = r = 1

        # buffer s to avoid out of bounds checks, results in O(n) extra space
        s = "\n" + s + "$"
        end_idx = len(s) - 1 

        # result variable
        num_palindromes = 0

        while r < end_idx:
            starting_char = s[l]
            
            # find identical characters in a row
            while s[r] == starting_char:
                r += 1
            # palindromes within this sequence is ((r-l) choose 2)
            num_palindromes += ((r-l)*(r-l+1))//2

            # start building palidrome with center of identical r-l characters (builds even or odd length
            # palidromes depending on r-l) j is lower index, k is higher index
            j = l-1
            k = r

            # while adding characters on either side still makes substring a palindrome add to
            # result variable and increase range of j and k
            while s[j] == s[k]:
                j -= 1
                k += 1

            # number of extra palidromes is number of iterations where s[j] == s[k]
            num_palindromes += k - r
            
            # new starting position (l) is first index that was not same character as previous ones
            l = r

        return num_palindromes

    def ownSolutionO_n_bufferedStringVariant(self, s: str) -> int:
        n = len(s)
        buffered_s = '\n' + s + '$'
        res = 1
        prev = buffered_s[1]
        for seed in range(2, n + 1):
            c = buffered_s[seed]

            # odd length palidromes
            diff = 1
            while buffered_s[seed-diff] == buffered_s[seed+diff]:
                diff += 1
            res += diff

            # even length palidromes
            if c == prev:
                diff = 1
                while buffered_s[seed-diff-1] == buffered_s[seed+diff]:
                    diff += 1
                res += diff

            prev = c

        return res
