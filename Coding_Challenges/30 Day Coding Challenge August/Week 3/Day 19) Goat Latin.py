class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i, curWord in enumerate(words):
            if not curWord[0].lower() in 'aeiou':
                newGoatLatinWord = curWord[1:] + curWord[0] + 'ma' + 'a'*(i+1)
            else:
                newGoatLatinWord = curWord + 'ma' + 'a'*(i+1)
            words[i] = newGoatLatinWord
        return ' '.join(words)
