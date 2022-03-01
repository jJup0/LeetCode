class Solution:
    # O(n) runtime, O(1) additional space
    def countBits(self, num: int) -> [int]:
        # base case, 0 has 0 1's
        res = [0]
        final_len = num + 1
        # build result until length reached, more explicitly len(res) < num + 1,
        # because 0 is included in the result
        while len(res) < final_len:
            # amount of 1's for numbers with hsb (highest set bit) at position i+1
            # follows same structure as hsb=i, except incremented by 1, respecting the hsb at i+1
            # calculate remaining to avoid: unnecessary calulation and returning res[:num + 1]
            remaining = min(len(res), final_len - len(res))
            res.extend(1 + prev for prev in res[:remaining])
        
        return res
