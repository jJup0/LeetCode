class Solution:
    # result string will always be of form a*[a-z]z*
    def getSmallestString(self, n: int, k: int) -> str:
        
        # result as char array to make it mutable
        res = ['a']*n
        
        # remaining k that still needs to be accounted for in return string
        k_remaining = k
        
        # current index in return string to be filled
        i = n - 1
        
        # fill with z's as long as rest of string can still be filled with a's
        while k_remaining - i > 26:
            res[i] = 'z'
            k_remaining -= 26
            i -= 1

        # insert one character so that score k can be achieved by filling everything to the 
        # left with a's
        res[i] = chr(k_remaining - i - 1 + ord('a'))
        return ''.join(res)
    
    
    # mathematical alternative found:
    # diff = k - n
    # quotient = diff // 25
    # reminder = diff % 25
    # # if needed if remainder 0 so as to not add extra 'z' in string, resulting in string length n + 1
    # return 'a'*(n-quotient-1) + chr(97+reminder) + 'z'*quotient if reminder else 'a'*(n-quotient)+ 'z'*quotient
