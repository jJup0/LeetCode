import heapq


class KthLargest:
    """
    Design a class to find the kth largest element in a stream. Note that it is
    the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

        KthLargest(int k, int[] nums) Initializes the object with the integer k
          and the stream of integers nums.
        int add(int val) Appends the integer val to the stream and returns the
          element representing the kth largest element in the stream.

    Constraints:
        1 <= k <= 10^4
        0 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        -10^4 <= val <= 10^4
        At most 10^4 calls will be made to add.
        It is guaranteed that there will be at least k elements in the array when you search for the kth element.
    """

    def __init__(self, k: int, nums: list[int]):
        # create a heap out of the k largest values, then heap[0] will be the kth largest
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)
        # it is possible for len(heap) == k - 1. If so, add "infinitely small"
        # number to heap, which will be removed at first add() call
        if len(self.heap) < k:
            heapq.heappush(self.heap, -1_000_000)

    def add(self, val: int) -> int:
        # if value is larger than kth largest then pushpop to heap
        if val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        # return kth largest (== smallest value on heap)
        return self.heap[0]
