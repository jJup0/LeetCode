from typing import List
import math
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # without using strings
        
        res = []
        digits = 123456789
        ones = 111111111

        # amount of digits low has
        len_num = math.ceil(math.log10(low + 1))
        # amount of possible numbers with len_num digits
        rounds = 10 - len_num
        # amount of digits to chuck off of digits and ones to generate sequential digit numbers
        divf = int(math.pow(10, rounds-1)) 

        while divf: # can reach 0, then finished
            curr_ones = ones//divf  # number to add to get next strictly increasing number
            curr = digits//divf     # lowest number with 10-rounds strictly increasing digits 
            for _ in range(rounds):
                if curr > high:
                    return res
                if curr >= low:     # in first round, possible the generated number is less than low
                    res.append(curr)
                    
                curr += curr_ones
                
            divf //= 10             # generate next order numbers
            rounds -= 1             # this takes one round less
            
        return res
