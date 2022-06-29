from typing import List


class Solution:
    """
    You are given an array of people, people, which are the attributes of some people in a queue
    (not necessarily in order). Each people[i] = [h_i, k_i] represents the ith person of height h_i
    with exactly k_i other people in front who have a height greater than or equal to h_i.
    Reconstruct and return the queue that is represented by the input array people. The returned
    queue should be formatted as an array queue, where queue[j] = [h_j, k_j] is the attributes of
    the jth person in the queue (queue[0] is the person at the front of the queue).
    Constraints:
        1 <= people.length <= 2000
        0 <= hi <= 10^6
        0 <= ki < people.length
        It is guaranteed that the queue can be reconstructed.
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        O(n^2) time (due to list.insert, apparantly faster not possible)
        O(1) extra space (people sorted in place, res not included)
        """
        # result variable
        res = []

        # sort people in descending order by height
        # if equal then (in ascending order) by nr of people in front
        people.sort(key=lambda x: (-x[0], x[1]))

        # iterate over sorted people, inserting into res at nr
        # having people sorted by height means taller people will be inserted first, therefore when inserting
        # p, every person in the queue is guaranteed to be taller/equal p's height. Also: no more shorter people
        # can be added in front of p,  meaning in the current queue, p fits perfectly at position p[1]
        for p in people:
            res.insert(p[1], p)

        return res
