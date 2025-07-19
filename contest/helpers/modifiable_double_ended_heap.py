import heapq
from collections import Counter
from typing import (
    Any,
    Iterator,
    MutableSet,
    Protocol,
    Sequence,
    TypeVar,
    cast,
    runtime_checkable,
)


@runtime_checkable
class SupportsNegAndOrd(Protocol):
    def __neg__(self) -> "SupportsNegAndOrd": ...
    def __lt__(self, other: Any, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...


SupportsNegAndOrdT = TypeVar("SupportsNegAndOrdT", bound=SupportsNegAndOrd)


class ModifiableDoubleEndedHeap(MutableSet[SupportsNegAndOrdT]):
    """Combines min and max heap, being able to remove and add arbitrary items."""

    def __init__(self, values: Sequence[SupportsNegAndOrdT]) -> None:
        self.min_heap: list[SupportsNegAndOrdT] = list(values)
        self.max_heap: list[SupportsNegAndOrdT] = [
            self._negate_value(v) for v in values
        ]
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        self.counter: Counter[SupportsNegAndOrdT] = Counter(values)
        self.len = len(values)

    def add(self, value: SupportsNegAndOrdT):
        self.counter[value] += 1
        self.len += 1
        heapq.heappush(self.min_heap, value)
        heapq.heappush(self.max_heap, self._negate_value(value))
        self._cleanup_heaps()

    def remove(self, value: SupportsNegAndOrdT) -> None:
        if value not in self.counter:
            raise KeyError(f"{value} not in {self.__class__.__name__}")
        if self.counter[value] == 1:
            self.counter.pop(value)
        else:
            self.counter[value] -= 1

        if value == self.min_heap[0]:
            heapq.heappop(self.min_heap)
        if self._negate_value(value) == self.max_heap[0]:
            heapq.heappop(self.max_heap)
        self._cleanup_heaps()
        self.len -= 1

    def discard(self, value: SupportsNegAndOrdT) -> None:
        try:
            self.remove(value)
        except KeyError:
            pass

    def pop(self):
        value = self._negate_value(self.max_heap[0])
        self.remove(value)
        return value

    def popleft(self):
        value = self.min_heap[0]
        self.remove(value)
        return value

    def get_smallest(self):
        return self.min_heap[0]

    def get_largest(self):
        return self._negate_value(self.max_heap[0])

    def __contains__(self, value: object) -> bool:
        return value in self.counter

    def __len__(self) -> int:
        return self.len

    def __iter__(self) -> Iterator[SupportsNegAndOrdT]:
        return self.counter.elements()

    def _cleanup_heaps(self):
        while self.min_heap and self.min_heap[0] not in self.counter:
            heapq.heappop(self.min_heap)
        while (
            self.max_heap and self._negate_value(self.max_heap[0]) not in self.counter
        ):
            heapq.heappop(self.max_heap)

        # futher garbage collection if heaps get way larger than they should actually be
        if len(self.min_heap) > 4 * len(self):
            self.min_heap = list(self.counter.elements())
            heapq.heapify(self.min_heap)
        if len(self.max_heap) > 4 * len(self):
            self.max_heap = [self._negate_value(v) for v in self.counter.elements()]
            heapq.heapify(self.max_heap)

    def _negate_value(self, v: SupportsNegAndOrdT) -> SupportsNegAndOrdT:
        """For some reason negation breaks out of type var..."""
        return cast(SupportsNegAndOrdT, -v)

    def __repr__(self) -> str:
        x = self.counter.elements()
        return str(sorted(x))
