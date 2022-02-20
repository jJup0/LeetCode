def BrutemaxArea(self, height: [int]) -> int:
    retVal = 0
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            if (j - i) * min(height[i], height[j]) > retVal:
                retVal = (j - i) * min(height[i], height[j])
            # print(i, j)
            # print(min(height[i], height[j]))

    return retVal


def decentEstimationButDontWorkmaxArea(self, height: [int]) -> int:
    retVal = 0
    middle = (len(height) - 1) / 2
    pillarValues = {}
    BiggestTwo_i_score = [[0, 0], [0, 0]]
    for i in range(len(height)):
        curScore = height[i] * (i - middle)
        pillarValues[i] = curScore
        if curScore > BiggestTwo_i_score[0][1]:
            BiggestTwo_i_score[0] = [i, curScore]
        elif curScore < BiggestTwo_i_score[1][1]:
            BiggestTwo_i_score[1] = [i, curScore]
    retVal = (BiggestTwo_i_score[0][0] - BiggestTwo_i_score[1][0]) * min(
        height[BiggestTwo_i_score[0][0]], height[BiggestTwo_i_score[1][0]])
    print(BiggestTwo_i_score)
    return retVal


class Solution:
    def maxArea(self, height: [int]) -> int:
        upperb = len(height) - 1
        lowerb = 0
        curMax = 0
        while upperb != lowerb:
            curScore = (upperb - lowerb) * min(height[upperb], height[lowerb])
            if (curScore > curMax):
                curMax = curScore
            if height[upperb] < height[lowerb]:
                upperb -= 1
            else:
                lowerb += 1
        return curMax
