class Solution:
    """
    A binary string is monotone increasing if it consists of some number of 0's (possibly none),
    followed by some number of 1's (also possibly none).

    You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

    Return the minimum number of flips to make s monotone increasing.

    Constraints:
        1 <= s.length <= 10^5
        s[i] is either '0' or '1'.
    """

    def minFlipsMonoIncr(self, s: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """

        # 'flips' tracks stores how many flips are needed if the ascending "happens"
        # at the current char, i.e. all chars before the current are 0, all after are 1s
        # therefore starting amount of flips (at pseudo index -1) is total amount of zeros
        flips = ret = s.count('0')
        for c in s:
            if (c == '0'):
                # if a 0 is encountered while traversing string in
                # acending order it does not need to be flipped
                flips -= 1
                # check if 'acension' starting here is minimal so far
                ret = min(ret, flips)
            else:
                # 1s however do have to be flipped
                flips += 1

        return ret
