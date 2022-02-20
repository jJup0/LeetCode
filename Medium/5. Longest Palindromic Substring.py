class pileOfShitDontWorkSolution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        #
        doubleMiddles = []
        tripleMiddles = []
        retVal = ''
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                doubleMiddles.append(i)
                i += 2
                continue
            if i < len(s) - 2 and s[i] == s[i+2]:
                tripleMiddles.append(i+1)
                i += 3
                continue
            i += 1
        #
        print(doubleMiddles)
        print(tripleMiddles)
        #
        maxLength = 0
        i_extension = 0
        while len(doubleMiddles):
            i = doubleMiddles[-1]
            lowerb = i - i_extension
            # actaully +1 but in str[a:b] b is excluded
            higherb = i + 2 + i_extension
            if lowerb >= 0 and higherb <= len(s):
                if lowerb > 1:
                    if s[lowerb:higherb] == s[higherb-1:lowerb-1:-1]:  # palindrome getting longer
                        if 2 + i_extension*2 > maxLength:
                            maxLength = 2 + 2 * i_extension
                            retVal = s[lowerb:higherb]
                        i_extension += 1
                    else:
                        print('stopped:' + str(lowerb) + '-' +
                              str(higherb) + s[lowerb:higherb] + s[higherb-1:lowerb-1:-1])
                        doubleMiddles.pop()  # palindrome stop
                        i_extension = 0
                else:
                    if s[lowerb:higherb] == s[higherb-1::-1]:  # palindrome getting longer
                        if 2 + i_extension*2 > maxLength:
                            maxLength = 2 + 2 * i_extension
                            retVal = s[lowerb:higherb]
                        i_extension += 1
                    else:
                        print('stopped:' + str(lowerb) + '-' +
                              str(higherb) + s[lowerb:higherb] + s[higherb-1:lowerb-1:-1])
                        doubleMiddles.pop()  # palindrome stop
                        i_extension = 0
        i_extension = 1
        while len(tripleMiddles):
            i = tripleMiddles[-1]
            lowerb = i - i_extension
            higherb = i + 1 + i_extension
            if lowerb >= 0 and higherb < len(s):
                if s[lowerb:higherb] == s[higherb:lowerb-1:-1]:  # palindrome getting longer
                    if 1 + i_extension*2 > maxLength:
                        maxLength = 1 + 2 * i_extension
                        retVal = s[lowerb:higherb]
                    i_extension += 1
                else:
                    tripleMiddles.pop()  # palindrome stop
                    i_extension = 1
        return retVal

# class Solution:


def longestPalindrome(self, s: str) -> str:
    if len(s) == 0:
        return ""
    maxLen = 1
    start = 0
    for i in range(len(s)):
        if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
            # print('i:' + str(i) + ', maxLen: ' + str(maxLen) +
            #    ', stringseg: ' + s[i-maxLen-1:i+1])
            start = i-maxLen-1
            maxLen += 2
            # print('newstart:' + str(start) +
            #       ', new maxLen: ' + str(maxLen) + '\n')
            continue

        # initialises an even length palindrome
        if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
            start = i-maxLen
            maxLen += 1
            # print('## ' + s[i-maxLen + 1:i+1] + ' ## start: ' +
            #       str(start) + ', maxLen: ' + str(maxLen) + '\n')
    return s[start:start+maxLen]


'123456789'
print(longestPalindrome(0, '123456789poop987654321'))
