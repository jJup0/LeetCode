import bisect
from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str):
        return self.removeDuplicateLetters_simple(s)

    def removeDuplicateLetters_over_engineered(self, s: str):
        """
        O(n^2 * log(n)) / O(n)    time / space complexity
        """
        # last occurance of letters not yet in char_list_res
        char_to_occurances: defaultdict[str, list[int]] = defaultdict(list)
        for i, c in enumerate(s):
            char_to_occurances[c].append(i)

        # char list representation of result
        char_list_res: list[str] = []

        # next lowest idx to accept when constructing result string
        next_lowest_idx = -1

        remaining_sorted_char_set = sorted(char_to_occurances.keys())

        # every iteration one character is removed char_to_occurances and added
        # to char_list_res
        while char_to_occurances:  # O(n)
            # iterate through remaining characters in lexicographical order
            for c in remaining_sorted_char_set:  # O(n)
                # retrieve ocurrances (not by .items()) to make sorting more efficient
                occurances_of_curr_char = char_to_occurances[c]

                # first occurance that is allowed to be kept when constructing res
                lowest_allowed_idx = occurances_of_curr_char[  # O(log(n))
                    min(
                        len(occurances_of_curr_char) - 1,
                        bisect.bisect(occurances_of_curr_char, next_lowest_idx),
                    )
                ]

                # if the substring s[new_idx:] contains all remaining letters,
                # add c to result list. If this is the case, then c is the
                # lexicographically lowest character that can be appended to
                # result, while still keeping 1 of each character
                if all(
                    lowest_allowed_idx <= o[-1] for o in char_to_occurances.values()
                ):
                    char_list_res.append(c)
                    # set new next lowest index
                    next_lowest_idx = lowest_allowed_idx
                    # delete char from occurances, no longer relevant, as already in result
                    char_to_occurances.pop(c)
                    # remove from sorted keys
                    remaining_sorted_char_set.remove(c)  # in total O(n ^ 2)
                    break

        # join char list to string
        return "".join(char_list_res)

    def removeDuplicateLetters_simple(self, s: str) -> str:
        """
        O(n^2 * log(n)) / O(n)    time / space complexity
        """
        set_s = set(s)  # O(n)
        for c in sorted(set_s):  # O(n * log(n))
            suffix = s[s.index(c) :]  # O(n)
            if set(suffix) == set_s:  # O(n)
                return c + self.removeDuplicateLetters_simple(suffix.replace(c, ""))
        return ""  # only when s == ''
