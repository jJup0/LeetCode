"""
Design a number container system that can do the following:
- Insert or Replace a number at the given index in the system.
- Return the smallest index for the given number in the system.

Implement the NumberContainers class:
- NumberContainers() Initializes the number container system.
- void change(int index, int number) Fills the container at index with the
  number. If there is already a number at that index, replace it.
- int find(int number) Returns the smallest index for the given number, or -1
  if there is no index that is filled by number in the system.

Constraints:
- 1 <= index, number <= 10^9
- At most 10^5 calls will be made in total to change and find.
"""

import heapq


class NumberContainers:
    def __init__(self):
        self.nums_to_idx_heap: dict[int, list[int]] = {}
        self.idx_to_num: dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        """
        Complexity:
            Time: O(log(n))
            Space: O(1)
        """
        self.nums_to_idx_heap.setdefault(number, [])
        heapq.heappush(self.nums_to_idx_heap[number], index)
        self.idx_to_num[index] = number

    def find(self, number: int) -> int:
        """
        Amortizes calls to change()
        Complexity:
            Amortized Time: O(log(n))
            Space: O(1)
        """
        idxs = self.nums_to_idx_heap.get(number, [])
        while idxs:
            lowest_idx = idxs[0]
            if self.idx_to_num[lowest_idx] == number:
                return lowest_idx
            heapq.heappop(idxs)
        return -1
