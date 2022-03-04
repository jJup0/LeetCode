class Solution:
    # some unneccessary computing done, as champagne tower is symmetrical
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # base case
        if query_row == 0:
            return min(1.0, poured)
        
        glasses = [poured]     # stores champagne supply of glasses
        for row_nr in range(1, query_row + 1):
            # use only one working array; at each new row one glass added to the end
            glasses.append(0)
            # glasses from previous row at index i pour into current row at indexes i and i+1
            # go through previous glasses row from last to first and pour overflowing champagne
            for i in range(row_nr-1, -1, -1):
                # if glass is not overflowing, nothing to pour, continue
                if glasses[i] < 1:
                    glasses[i] = 0
                    continue
                # one unit of champagne "kept" in glass above, half is poured to each glass underneath
                glasses[i] = (glasses[i] - 1) / 2
                # pour other half to i+1
                glasses[i+1] += glasses[i]

        # max capacity of glass is 1
        return min(1.0, glasses[query_glass])
            


class MoreUnderstandableSolution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return min(1.0, poured)
        prev_row = [poured]
        for row_nr in range(1, query_row + 1):
            glasses_row = [0]*(row_nr + 1)
            for glass_idx, amount in enumerate(prev_row):
                if amount < 1:
                    continue
                half = (amount-1) / 2
                glasses_row[glass_idx] += half 
                glasses_row[glass_idx+1] += half 
            prev_row = glasses_row
        
        return min(1.0, glasses_row[query_glass])