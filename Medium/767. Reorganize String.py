import heapq
import math
from collections import Counter


class Solution:
    """
    Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.

    Constraints:
    - 1 <= s.length <= 500
    - s consists of lowercase English letters.
    """

    def reorganizeString(self, s: str) -> str:
        """
        Create a max-heap of characters in the string and their occurence count.
        O(n * log(n)) / O(n)    time / space complexity
        """
        # create a max heap of the characters and counts
        max_heap = [(-count, c) for c, count in Counter(s).items()]
        heapq.heapify(max_heap)
        # string cannot be reorganized iff the occurence count of the most common
        # character is more than half of the lenght of the string rounded up
        if -max_heap[0][0] > math.ceil(len(s) / 2):
            return ""

        # string builder for result
        res_char_list: list[str] = [""]
        while max_heap:
            # get most common character from heap
            neg_count, char = heapq.heappop(max_heap)

            # if it is the previously used character, need to place a character in between
            if char == res_char_list[-1]:
                # get second most common character and append to result
                second_neg_count, second_char = heapq.heappop(max_heap)
                res_char_list.append(second_char)
                if second_neg_count != -1:
                    # if there is more than one character remaining, decrement
                    # and push back on to max heap
                    second_neg_count += 1
                    heapq.heappush(max_heap, (second_neg_count, second_char))

            # append most common character to result
            res_char_list.append(char)
            if neg_count != -1:
                # if there is more than one character remaining, decrement
                # and push back on to max heap
                neg_count += 1
                heapq.heappush(max_heap, (neg_count, char))

        # create a string from the string builder
        return "".join(res_char_list)
