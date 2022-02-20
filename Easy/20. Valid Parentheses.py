# class Solution(object):
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if (len(s) % 2) == 1:  # didnt improve speed
        return False
    parenthPairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        ' ': '\n'   # ' ' is our starting string
    }
    bracketStack = ' '
    for l in s:
        if l in parenthPairs:  # currently opening
            bracketStack += l
        # current is the one that should close
        elif l == parenthPairs[bracketStack[-1]]:
            bracketStack = bracketStack[:-1]
        else:
            return False
        return bracketStack == ' '
