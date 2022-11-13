import heapq


class MedianFinder:
    """
    The median is the middle value in an ordered integer list. If the size of the list is even,
    there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the
    actual answer will be accepted.

    Constraints:
        -10^5 <= num <= 10^5
        There will be at least one element in the data structure before calling findMedian.
        At most 5 * 10^4 calls will be made to addNum and findMedian.
    """

    def __init__(self):
        """
        O(n) space complexity
        """
        # build heaps starting from the middle values, i.e. small[0] and large[0] are middle values
        self.small = []  # the smaller half of the list, max heap
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num) -> None:
        """
        O(log(n)) time complexity
        """
        if len(self.small) == len(self.large):
            # if an even number of items were added, push num to small, get largest value from smaller
            # half and push to large
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            # else push num to large, get smallest value and push to small
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        """
        O(1) time complexity
        """
        # if an even amount of values are contained, return mean of middle values
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            # else large contains more values, so return its smallest value
            return float(self.large[0])
