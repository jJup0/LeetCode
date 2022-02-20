class Solution:
    def wordPattern(self, pattern: str, sentence: str) -> bool:
        word_list = sentence.split()
        if len(pattern) != len(word_list): 
            return False
        # old solution:
        # return len(set(zip(pattern, word_list))) == len(set(pattern)) == len(set(word_list))
        
        c_2_word = {}
        word_2_c = {}
        for c, word in zip(pattern, word_list):
            prev_word = c_2_word.get(c, None)
            prev_c = word_2_c.get(word, None)
            if prev_word:
                if (not prev_c) or (word != prev_word):
                    return False
            elif prev_c:
                return False
            c_2_word[c] = word
            word_2_c[word] = c
        return True

        
