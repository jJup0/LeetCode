import bisect
from collections import defaultdict
from typing import Dict, List, Tuple


class TimeMap:
    """
    Design a time-based key-value data structure that can store multiple values for the same key
    at different time stamps and retrieve the key's value at a certain timestamp.
    Implement the TimeMap class:
        TimeMap() Initializes the object of the data structure.
        void set(String key, String value, int timestamp) Stores the key key with the value value
            at the given time timestamp.
        String get(String key, int timestamp) Returns a value such that set was called previously
             with timestamp_prev <= timestamp. If there are multiple such values, it returns the
             value associated with the largest timestamp_prev. If there are no values, it returns
             "".

    Constraints:
        1 <= key.length, value.length <= 100
        key and value consist of lowercase English letters and digits.
        1 <= timestamp <= 107
        All the timestamps timestamp of set are strictly increasing.
        At most 2 * 105 calls will be made to set and get.
    """

    def __init__(self):
        """
        a := nr of calls to set, b:= nr of calls to get
        O(a + b * log(a)) / O(a)    time / space complexity 
        """
        # maps key to a list of timestamps and values, default values for minimum timestamp
        # acts as default return for when no value is set at a given timestamp
        self.t_map: Dict[str, List[int]] = defaultdict(lambda: [-1])
        self.v_map: Dict[str, List[str]] = defaultdict(lambda: [""])

    def set(self, key: str, value: str, timestamp: int) -> None:

        # since calls to set for a given key uses strictly increasing timestamp, simply append
        # value and timestamp to both arrays for key
        self.t_map[key].append(timestamp)
        self.v_map[key].append(value)

    def get(self, key: str, timestamp: int) -> str:

        # find the next lowest timestamp in the list of values for key by searching for timestamp
        # since this always returns the next index, decrease by one
        idx = bisect.bisect_right(self.t_map[key], timestamp) - 1

        # return value at that index
        return self.v_map[key][idx]
