import bisect
from collections import defaultdict


class Solution:

    # over engineered, more efficient translation of:
    # for c in sorted(set(s)):
    #     suffix = s[s.index(c):]
    #     if set(suffix) == set(s):
    #         return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    # return ''     # only when s == ''
    def smallestSubsequence(self, s: str) -> str:
        # last occurance of letters not yet in char_list_res
        last_occurance = defaultdict(list)
        for i, c in enumerate(s):
            last_occurance[c].append(i)

        # char list representation of result
        char_list_res = []

        # next lowest idx to accept when constructing result string
        next_lowest_idx = -1

        # every iteration one entry is removed and added to char_list_res
        while last_occurance:
            # go through remaining letters in lexicographical order
            for c in sorted(last_occurance.keys()):
                # retrieve ocurrances (not by .items()) to make sorting more efficient
                occurances = last_occurance[c]

                # equivalent to new_idx = s.index(c, next_lowest_idx)
                new_idx = occurances[min(len(occurances) - 1, bisect.bisect(occurances, next_lowest_idx))]

                # if the substring s[new_idx:] contains all remaining letters, add c to result list
                # read as: if the index is lower than the last occurance of all remainig letters
                if all(new_idx <= o[-1] for o in last_occurance.values()):
                    char_list_res.append(c)
                    # set new next lowest index
                    next_lowest_idx = new_idx
                    # delete char from occurances, no longer relevant, as already in result
                    del last_occurance[c]
                    break

        # join char list to string
        return ''.join(char_list_res)
