from collections import Counter


class Solution:
    def threeSum(self, nums: [int]):
        ele_dict = Counter(nums)
        neg_set = set()
        pos_set = set()

        for e in ele_dict:
            if e >= 0:
                pos_set.add(e)
            else:
                neg_set.add(e)

        result = set()
        for e1 in sorted(neg_set):  # O(n^2 log(n)^2) but can break early
            for e2 in sorted(pos_set):
                e3 = - (e1 + e2)
                if e3 < e1:
                    break
                if e3 > e2:
                    continue
                e3_present = (e3 == e1) | (e3 == e2)
                if (ele_dict.get(e3, 0) > e3_present):
                    result.add((e1, e3, e2))

        if ele_dict.get(0, 0) >= 3:
            result.add((0, 0, 0))
        return result

    def threeSum1(self, nums: [int]):
        ele_dict = Counter(nums)
        neg_set = set()
        pos_set = set()

        for e in ele_dict:
            if e >= 0:
                pos_set.add(e)
            else:
                neg_set.add(e)

        result = set()
        for e1 in neg_set:  # O(n^2)
            for e2 in pos_set:
                e3 = - (e1 + e2)
                e3_present = (e3 == e1) | (e3 == e2)
                if (ele_dict.get(e3, 0) > e3_present):
                    answer = tuple(sorted((e1, e3, e2)))
                    result.add(answer)

        if ele_dict.get(0, 0) >= 3:
            result.add((0, 0, 0))
        return result
