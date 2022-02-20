import bisect
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_str_len = len(n_str)
        len_digits = len(digits)
        # all values that have one less digit are automatically smaller
        res = sum(len_digits ** i for i in range(1, n_str_len))
        
        i = 0
        while i < len(n_str):
            digits_smaller_neq = bisect.bisect_left(digits, n_str[i])
            res += digits_smaller_neq * (len_digits ** (n_str_len - i - 1))
            
            if n_str[i] not in digits:
                break
            i += 1
        return res + (i == n_str_len) # i == n_str_len means n can be made from digits exactly