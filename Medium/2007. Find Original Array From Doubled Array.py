from collections import Counter, deque
from typing import Deque, Dict, List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        res = []
        # iterate through occurances of values
        for k in counter.keys():
            count = counter[k]

            # handle zero as special case
            if k == 0:
                if count % 2:
                    return []
                res.extend(0 for _ in range(count//2))

            # if a value is not part of a double-chain previously visited
            elif count > 0:
                # find lowest multiple in chain of doubles
                while (k % 2 == 0) and ((k//2) in counter):
                    k //= 2

                # process all values in the doubles chain, virtually assinging them pairs of doubles/halfs
                while k in counter:
                    count = counter[k]

                    if count:
                        # add value to res, count times
                        res.extend(k for _ in range(count))

                        # if there are not enough double values in changed, return []
                        if counter[k * 2] < count:
                            return []

                        # subtract count from double to mark the values as used in a pair
                        counter[k * 2] -= count

                        # set counter to 0, as all occurances of a value have a double-pair
                        counter[k] = 0

                    # go to next double
                    k *= 2

        return res

    def findOriginalArray_broken(self, changed: List[int]) -> List[int]:
        # breaks for duplicates
        if len(changed) & 1:
            return []

        chains: Dict[int, Deque[int]] = {}
        for val in changed:
            if val == 0:
                l = chains.pop(0, deque())
                l.append(0)
                chains[0] = l
                continue

            half = val >> 1
            double = val << 1
            if (val % 2 == 0) and (half in chains):
                l = chains[half]
                if len(l) > 1:
                    del chains[half]
                l.append(val)
                chains[val] = l

                if double in chains:
                    l2 = chains[double]
                    chains.pop(l2[0], None)
                    chains.pop(l2[-1], None)
                    chains.pop(l[-1], None)
                    l.extend(l2)
                    chains[l2[-1]] = l

            elif double in chains:
                l = chains[double]
                if len(l) > 1:
                    del chains[double]
                l.appendleft(val)
                chains[val] = l
            else:
                chains[val] = deque((val,))

        print(chains)

        if any(len(l) & 1 for l in chains.values()):
            return []
        res = []
        for val in chains.keys():
            l = chains[val]
            res.extend(l[i] for i in range(0, len(l), 2))
            l.clear()
        return res

    def findOriginalArray_sort_4000ms(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            return []
        changed.sort()
        res = []
        res_i = 0
        for val in changed:
            if res_i == len(res):
                res.append(val)
            else:
                if val > res[res_i] * 2:
                    return []
                elif val < res[res_i] * 2:
                    res.append(val)
                else:
                    res_i += 1
        return res if res_i == len(res) else []
