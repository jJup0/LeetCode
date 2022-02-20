class Solution:
    def wordPattern(self, pattern: str, sentence: str) -> bool:
        # patternDict = dict()
        # wordDict = dict()
        # sentence = sentence.split()
        # if len(pattern) != len(sentence):
        #     return False
        # for c, word in zip(pattern, sentence):
        #     if (word in wordDict and wordDict[word] != c):
        #         return False
        #     if c in patternDict:
        #         if patternDict[c] != word:
        #             return False
        #     else:
        #         patternDict[c] = word
        #         wordDict[word] = c
        # print(patternDict)
        # print(wordDict)
        # return True

        sentence = sentence.split()
        if len(pattern) != len(sentence):
            return False
        # return len of set of pairs equal to set of strs and pattern chars
        return len(set(zip(pattern, sentence))) == len(set(pattern)) == len(set(sentence))
