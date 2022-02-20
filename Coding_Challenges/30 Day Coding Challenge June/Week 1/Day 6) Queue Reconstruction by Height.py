class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        retVal = []
        for p in people:
            retVal.insert(p[1], p)
        return retVal