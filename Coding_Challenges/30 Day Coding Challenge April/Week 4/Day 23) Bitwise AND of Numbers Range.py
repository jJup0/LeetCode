class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n >= (m << 1):
            return 0
        ret = m
        for x in range(m+1, n+1):
            ret &= x
        return ret


# # pattern test
# for m in range(1, 100):
#     pp = ''
#     for n in range(m, m+40):
#         z = rangeBitwiseAnd(0, m, n)
#         pp += str(z).rjust(2)+'_'
#     print(pp + "{0:b}".format(m).rjust(10) + '   ' + str(pp.count(str(m))))
