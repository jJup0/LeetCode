class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while len(stones) > 1:
            stones.sort()
            s3 = 0
            biggestS3 = 0
            for _ in range(round(len(stones) + 0.9/2)):
                if len(stones) < 2 or biggestS3 > stones[-2]:
                    break
                if s3 >= stones[-2]:
                    s1 = s3
                    s2 = stones.pop(-1)
                else:
                    s1, s2 = stones.pop(-1), stones.pop(-1)
                    if s3:
                        stones.insert(0, s3)
                s3 = abs(s1 - s2)
                if s3 > biggestS3:
                    biggestS3 = s3
            if s3:
                stones.append(s3)
        if stones:
            return stones[0]
        return 0
