class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n-1 > len(flowerbed)//2:
            return False
        if not n:
            return True
        zeroes = 2*(flowerbed[0] == 0)
        for plot in flowerbed[1:]:
            if plot:
                zeroes = 0
            else:
                if zeroes == 2:
                    zeroes = 1
                    n -= 1
                    if not n:
                        return True
                else:
                    zeroes += 1

        return n == 1 and zeroes == 2
