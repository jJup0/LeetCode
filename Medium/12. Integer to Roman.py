class Solution:
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.

    Constraints:
        1 <= num <= 3999
    """

    def intToRoman(self, num: int) -> str:
        """
        Predetermine combinations like IV, IX etc. and go through roman values in descending order.
        r := number of different roman numerals, assuming 1, 5, 10, 50 ... distribution
        O(r) / (r)      time / space complexity 
        """
        res_string_builder = []

        # conversion from value to roman digits
        dec2rom = ((1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'),
                   (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M'))

        # iterate from highest to lowest
        for (curr_val, roman_string) in reversed(dec2rom):
            # keep appending result with roman numerals with num is greater than the current value
            while num >= curr_val:
                num -= curr_val
                res_string_builder.append(roman_string)

            # early termination, not necessary for correctness
            if not num:
                break

        # build string from string list
        return ''.join(res_string_builder)

    def intToRoman_alternative(self, num: int) -> str:
        i_mxrVal = 7
        res_string_builder = []
        dec2rom = ((0, ''), (1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'))
        subs___ = (0, 0, 1, 1, 3, 3, 5, 5)
        while num:
            curMaxVal = dec2rom[i_mxrVal][0]

            if num >= curMaxVal:
                num -= curMaxVal
                res_string_builder.append(dec2rom[i_mxrVal][1])
            elif num >= curMaxVal - dec2rom[subs___[i_mxrVal]][0]:
                num -= curMaxVal - dec2rom[subs___[i_mxrVal]][0]
                res_string_builder.append(dec2rom[subs___[i_mxrVal]][1] + dec2rom[i_mxrVal][1])
            else:
                i_mxrVal -= 1

        return ''.join(res_string_builder)
