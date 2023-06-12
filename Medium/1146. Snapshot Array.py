import bisect


class SnapshotArray:
    """
    Implement a SnapshotArray that supports the following interface:

    SnapshotArray(int length) initializes an array-like data structure with the
    given length. Initially, each element equals 0.
    - void set(index, val) sets the element at the given index to be equal to val.
    - int snap() takes a snapshot of the array and returns the snap_id: the total
      number of times we called snap() minus 1.
    - int get(index, snap_id) returns the value at the given index, at the time we
      took the snapshot with the given snap_id

    Constraints:

    - 1 <= length <= 5 * 104
    - 0 <= index < length
    - 0 <= val <= 109
    - 0 <= snap_id < (the total number of times we call snap())
    - At most 5 * 104 calls will be made to set, snap, and get.
    """

    def __init__(self, length: int):
        # list of values for a given index over time
        self.vals: list[list[tuple[int, int]]] = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # for "setting" a value for an index, the current snap_id and value are stored
        struct_to_add = (self.snap_id, val)

        last_idx, _ = self.vals[index][-1]
        if last_idx == self.snap_id:
            # if value for an index has been set without snap() called inbetween, overwrite
            self.vals[index][-1] = struct_to_add
        else:
            # else append
            self.vals[index].append(struct_to_add)

    def snap(self) -> int:
        res = self.snap_id
        self.snap_id += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        # O(log(n)) time

        # find value of index for snap_id
        idx = bisect.bisect(self.vals[index], (snap_id, -1))

        # if idx == len(self.vals[index]), which can happen if snap() has been
        # called without setting a new value for index, limit idx to last entry
        idx = min(idx, len(self.vals[index]) - 1)
        # same case as above, but for when not the last element of the list
        if self.vals[index][idx][0] > snap_id:
            idx -= 1

        return self.vals[index][idx][1]
