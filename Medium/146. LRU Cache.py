class ListNode:
    def __init__(
        self,
        key: int,
        value: int,
        prev: "ListNode | None" = None,
        next: "ListNode | None" = None,
    ) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __hash__(self) -> int:
        return hash((self.key, self.value))


class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU)
    cache.

    Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache. If the number of keys exceeds the
      capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.

    Constraints:
    - 1 <= capacity <= 3000
    - 0 <= key <= 10^4
    - 0 <= value <= 10^5
    - At most 2 * 10^5 calls will be made to get and put.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.capacity_remaining = capacity

        # use a dictionary for quick access to a node in the linked list
        # and a linked list to model the recently used attribute
        # head of linked linked is least recently used
        self.value_lookup: dict[int, ListNode] = {}
        self.lr_dummy_head = ListNode(-1, -1)
        self.lr_tail = self.lr_dummy_head

    def get(self, key: int) -> int:
        if key in self.value_lookup:
            # make key most recently used
            self._update_used(key)
            return self.value_lookup[key].value
        # key not in cache
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.value_lookup:
            # update the value and most recently used
            self.value_lookup[key].value = value
            self._update_used(key)
            return

        if self.capacity_remaining == 0:
            # if no space is remaining, need to remove least recently used
            to_remove = self.lr_dummy_head.next
            assert to_remove is not None
            self.lr_dummy_head.next = to_remove.next

            if self.capacity == 1:
                # if capacity is 1 then current node which is being removed is
                # the tail, after removal, head is tail
                self.lr_tail = self.lr_dummy_head
            else:
                # else make next least recently used node the dummy-head's next node
                assert to_remove.next is not None
                to_remove.next.prev = self.lr_dummy_head

            # remove from lookup
            self.value_lookup.pop(to_remove.key)
            self.capacity_remaining += 1

        # create a new node and add to lookup
        new_node = ListNode(key, value)
        self.value_lookup[key] = new_node

        # add the node to the list
        self.lr_tail.next = new_node
        new_node.prev = self.lr_tail
        # and make it the tail
        self.lr_tail = new_node

        # decrease the capacity remaining
        self.capacity_remaining -= 1

    def _update_used(self, key: int):
        # get the node to put at the end of the list
        curr_node = self.value_lookup[key]
        if curr_node is self.lr_tail:
            # if it already is at the end, nothing to do
            return

        prev_node = curr_node.prev
        next_node = curr_node.next
        assert prev_node is not None and next_node is not None

        # remove the node from its place in the list
        prev_node.next = next_node
        next_node.prev = prev_node

        # append to the end of the list
        self.lr_tail.next = curr_node
        curr_node.prev = self.lr_tail
        # remove next node
        curr_node.next = None
        # make current node new tail of the list
        self.lr_tail = curr_node
