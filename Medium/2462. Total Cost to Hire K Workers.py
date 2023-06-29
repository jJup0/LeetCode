import heapq


class Solution:
    """
    You are given a 0-indexed integer array costs where costs[i] is the cost of
    hiring the ith worker.

    You are also given two integers k and candidates. We want to hire exactly k
    workers according to the following rules:
    - You will run k sessions and hire exactly one worker in each session.
    - In each hiring session, choose the worker with the lowest cost from either
      the first candidates workers or the last candidates workers. Break the tie
      by the smallest index.
    - For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first
      hiring session, we will choose the 4th worker because they have the lowest
      cost [3,2,7,7,1,2].
    - In the second hiring session, we will choose 1st worker because they have
      the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2].
      Please note that the indexing may be changed in the process.
    - If there are fewer than candidates workers remaining, choose the worker
      with the lowest cost among them. Break the tie by the smallest index.
    - A worker can only be chosen once.

    Return the total cost to hire exactly k workers.

    Constraints:
    - 1 <= costs.length <= 10^5
    - 1 <= costs[i] <= 10^5
    - 1 <= k, candidates <= costs.length
    """

    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        # if any candidate can be hired, take the cheapest ones
        if 2 * candidates >= len(costs):
            return sum(heapq.nsmallest(k, costs))

        # currently availible candidates to choose from
        # curr = [(costs[i], i) for i in range(-k, k)]
        curr = [(c, i) for i, c in enumerate(costs[:candidates])]
        curr.extend(
            (c, i)
            for i, c in enumerate(costs[-candidates:], start=len(costs) - candidates)
        )
        heapq.heapify(curr)

        res = 0
        # next candidate to take either from start or end
        i = candidates
        j = len(costs) - candidates - 1
        for worker_i in range(k):
            # take cheapest worker from availible workers
            cost, index = heapq.heappop(curr)
            res += cost

            if index < j:
                # if current lowest cost candidate was taken from the left side,
                # take the next candidate from the left
                heapq.heappush(curr, (costs[i], i))
                i += 1
            else:
                # else take the next candidate from the right
                heapq.heappush(curr, (costs[j], j))
                j -= 1

            if i > j:
                # if i > j, then any candidates can be taken from the remaining ones
                res += sum(c for c, _ in heapq.nsmallest(k - worker_i - 1, curr))
                break
        return res
