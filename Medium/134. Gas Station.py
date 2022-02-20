class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = 0                     # current gas in car when starting from 0
        min_index = 0                   # index where gas is at a minimum
        min_spare_gas = float('inf')    # amount of gas at minimum
        
        for i,(g, c) in enumerate(zip(gas,cost)):
            cur_gas += g - c
            if cur_gas < min_spare_gas:
                min_spare_gas = cur_gas
                min_index = i
                
        if cur_gas < 0:
            return -1
        
        # start one station after minimum gas 
        return (min_index + 1) % len(gas)