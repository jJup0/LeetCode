class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # x = bin(x)[2:]
        # y = bin(y)[2:]
        # if len(x) < len(y):
        #     x = x.zfill(len(y))
        # else:
        #     y = y.zfill(len(x))
        # return sum(xbit != ybit  for xbit, ybit in zip(x, y))

        # ret = 0
        # while x | y:
        #     ret += ((x ^ y) & 1)
        #     x >>= 1
        #     y >>= 1
        # return ret
    
        # return sum ((((x>>i) ^ (y>>i)) & 1) for i in range(max(x.bit_length(), y.bit_length())))
        
        # z = x ^ y
        # return sum ((z>>i & 1) for i in range(z.bit_length()))
        
        z = x ^ y
        res = 0
        while z:
            z &= z-1
            res += 1
        return res