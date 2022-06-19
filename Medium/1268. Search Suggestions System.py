import bisect
from typing import List


class Solution:
    """
    You are given an array of strings products and a string searchWord.
    Design a system that suggests at most three product names from products after each character
    of searchWord is typed. Suggested products should have common prefix with searchWord. If
    there are more than three products with a common prefix return the three lexicographically
    minimums products.
    Return a list of lists of the suggested products after each character of searchWord is typed.
    Constraints:
        1 <= products.length <= 1000
        1 <= products[i].length <= 3000
        1 <= sum(products[i].length) <= 2 * 10^4
        All the strings of products are unique.
        products[i] consists of lowercase English letters.
        1 <= searchWord.length <= 1000
        searchWord consists of lowercase English letters.
    """

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Binary search approach. n := len(products), k := len(searchWord)
        Time: O(n * log(n) + min(n, k) * log(n) * k)
        Extra space (ignoring result): O(k) 
        """
        # sort products so that they are in lexicographical order
        products.sort()

        n = len(products)

        # current partial search term
        partial_search_term = ""

        # minimum index from which to search in products for
        lo = 0

        # result variable
        res = [[] for _ in range(len(searchWord))]

        for i, c in enumerate(searchWord):
            # add current letter to partial search term
            partial_search_term += c

            # find index where partial would be inserted
            insert_idx = bisect.bisect_left(products, partial_search_term, lo=lo)

            no_matching_prefix = True
            # check three words starting from that index for matching prefix
            for offset in range(min(3, n - insert_idx)):
                product = products[insert_idx + offset]
                if product.startswith(partial_search_term):
                    no_matching_prefix = False
                    res[i].append(product)
                else:
                    # if a word does not have a matching prefix, neither will any following word
                    break

            # if no words were found in current iteration, no further words will be found (performance only)
            if no_matching_prefix:
                break

            # insert index is new lo index from where to search from
            lo = insert_idx

        return res
