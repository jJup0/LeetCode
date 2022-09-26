from collections import defaultdict
from typing import List


class Solution:
    """
    You are given an array of strings equations that represent relationships between variables
    where each string equations[i] is of length 4 and takes one of two different forms:
    "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that
    represent one-letter variable names.
    Return true if it is possible to assign integers to variable names so as to satisfy all the
    given equations, or false otherwise.

    Constraints:
        1 <= equations.length <= 500
        equations[i].length == 4
        equations[i][0] is a lowercase letter.
        equations[i][1] is either '=' or '!'.
        equations[i][2] is '='.
        equations[i][3] is a lowercase letter.
    """

    def equationsPossible(self, equations: List[str]) -> bool:
        """
        Solution does not iterate over all equalities before checking inequality like many other
        solutions, allowing for earlier termination.
        O(n) / O(n)     time / space complexity
        """
        # maps a character c to a set of all characters that c should be equal to, including upper
        # case versions of the letters if unequal
        equality_map = defaultdict(set)

        for a, eq, _, b in equations:
            # fetch equality sets for both characters
            set_a, set_b = equality_map[a], equality_map[b]

            # ensure a and b are in their own sets
            set_a.add(a)
            set_b.add(b)

            if eq == '=':
                # if a and b should be equal, but have previously been determined as unequal
                if (b.upper() in set_a) or (a.upper() in set_b):
                    return False

                # update the equality set of both letters to the union of their sets
                set_a.update(set_b)
                equality_map[b] = set_a
            else:
                # if a and b should be unequal, but have previously been determined as equal
                if (b in set_a) or (a in set_b):
                    return False

                # each equality set now needs to include inequality of all characters in the
                # equality set of the other
                set_a.update(c.upper() for c in set_b if c.islower())
                set_b.update(c.upper() for c in set_a if c.islower())

        return True


    def equationsPossible_uf_modified_stolen(self, equations: List[str]) -> bool:
        # union find data structure
        uf = {c: c for c in map(chr, range(ord('a'), ord('z') + 1))}

        # union find methods
        def union(a, b):
            uf[find(b)] = find(a)

        def find(c):
            if uf[c] != c:
                uf[c] = find(uf[c])
            return uf[c]
    
        # create union between a and b if they should be equal
        for a, eq, _, b in equations:
            if eq == '=':
                union(a, b)
    
        # check for all inequalities if a and b are in union
        for a, eq, _, b in equations:
            if eq == '!' and find(a) == find(b):
                return False
        return True
