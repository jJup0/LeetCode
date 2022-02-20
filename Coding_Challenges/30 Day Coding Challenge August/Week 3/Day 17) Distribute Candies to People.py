class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        distributions = -0.5 + (2*candies+0.25)**0.5
        completedLoops = distributions//num_people
        lastPersonCandy = (completedLoops*(completedLoops+1)/2)*num_people
        lastPersonToGet_idx = int(distributions % num_people)
        retList = [0] * (num_people - 1) + [lastPersonCandy]
        for i in range(-2, -num_people+lastPersonToGet_idx-1, -1):
            retList[i] = retList[i+1] - completedLoops
        for i in range(lastPersonToGet_idx):
            retList[i] = retList[i-1] + completedLoops+1
        retList[lastPersonToGet_idx] += round(distributions*(distributions % 1))
        return [int(n) for n in retList]
