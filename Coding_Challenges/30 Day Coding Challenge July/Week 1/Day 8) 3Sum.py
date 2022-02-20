class Solution:
    def threeSum(self, nums: [int]):
        ele_dict = dict()
        neg_set = set()
        pos_set = set()
        result = set()

        for e in nums:
            ele_dict[e] = ele_dict.get(e, 0) + 1  # get(key, 0) means return 0 if key doesnot exist
            if e >= 0:
                pos_set.add(e)
            else:
                neg_set.add(e)

        print(pos_set, neg_set)
        for e1 in pos_set:
            for e2 in neg_set:
                e3 = - (e1 + e2)
                first_two = (e1, e2)
                if (e3 not in first_two and e3 in ele_dict) or (e3 in first_two and ele_dict.get(e3, 0) > 1):
                    answer = tuple(sorted([e1, e2, e3]))
                    result.add(answer)

        if ele_dict.get(0, 0) >= 3:
            result.add((0, 0, 0))
        return result
