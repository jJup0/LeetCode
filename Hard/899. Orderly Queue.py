class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # if k is greater than 1, s can be arbitrarily rearranged
        if k > 1:
            return ''.join(sorted(s))

        # if k == 1 find minimum rotation
        return self.__min_rotate_n_squared(s)

    def __min_rotate_n_squared(self, s: str) -> str:
        """
        O(n^2) / O(n)   time / space complexity
        """
        n = len(s)
        possible_seeds = list(range(n))

        # this loop runs in O(n^2) time for cases like "aaaaaa" or "ababababababab"
        # delta is the current length of substrings being considered
        for delta in range(n):
            # if there is only one substring left, then break
            if len(possible_seeds) == 1:
                break

            # get the next character of remaining possible minimal substrings
            next_chars = [s[(poss + delta) % n] for poss in possible_seeds]
            # minimal next character
            min_next_char = min(next_chars)

            # leave only possible seeds that have minimal next character
            possible_seeds = [possible_seed for possible_seed, next_char in zip(possible_seeds, next_chars) if next_char == min_next_char]

        # all indexes remaining in possibles will have equal lexicographical order if rotated
        # around it
        return s[possible_seeds[0]:] + s[:possible_seeds[0]]

    def __duval(self, s: str) -> str:
        # duval algorithm, runs in O(n) time, dont really understand it, but here it is
        n = len(s)
        s += s
        i = 0
        res_idx = -1
        while (i < n):
            res_idx = i
            j = i + 1
            k = i
            while (j < n*2 and s[k] <= s[j]):
                if (s[k] < s[j]):
                    k = i
                else:
                    k += 1
                j += 1

            # skips over cases like "ab" repitition in "ababababxyz" apparently
            while (i <= k):
                i += j - k

        return s[res_idx:res_idx + n]
