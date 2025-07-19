import pytest

from contest.helpers.modifiable_double_ended_heap import ModifiableDoubleEndedHeap


@pytest.fixture
def heap():
    return ModifiableDoubleEndedHeap([3, 1, 2, 2])


def test_init(heap: ModifiableDoubleEndedHeap[int]):
    assert len(heap) == 4
    assert heap.get_smallest() == 1
    assert heap.get_largest() == 3


def test_add(heap: ModifiableDoubleEndedHeap[int]):
    assert 4 not in heap
    heap.add(4)
    assert 4 in heap
    assert heap.get_largest() == 4
    assert len(heap) == 5


def test_remove_existing(heap: ModifiableDoubleEndedHeap[int]):
    heap.remove(2)  # appears twice initially
    assert 2 in heap
    assert len(heap) == 3

    heap.remove(2)  # now completely removed
    assert 2 not in heap
    assert len(heap) == 2


def test_remove_nonexistent_raises(heap: ModifiableDoubleEndedHeap[int]):
    with pytest.raises(KeyError, match="5 not in ModifiableDoubleEndedHeap"):
        heap.remove(5)


def test_discard(heap: ModifiableDoubleEndedHeap[int]):
    heap.discard(2)  # removes one
    heap.discard(2)  # removes the second
    heap.discard(2)  # does nothing
    assert 2 not in heap


def test_pop(heap: ModifiableDoubleEndedHeap[int]):
    largest = heap.get_largest()
    assert heap.pop() == largest
    assert largest not in heap


def test_popleft(heap: ModifiableDoubleEndedHeap[int]):
    smallest = heap.get_smallest()
    assert heap.popleft() == smallest
    assert smallest not in heap


def test_iter_and_contains(heap: ModifiableDoubleEndedHeap[int]):
    items = list(heap)
    for item in items:
        assert item in heap
    assert 999 not in heap


def test_repr(heap: ModifiableDoubleEndedHeap[int]):
    r = repr(heap)
    assert r.startswith("[")
    assert r.endswith("]")


def test_cleanup_trigger(heap: ModifiableDoubleEndedHeap[int]):
    heap = ModifiableDoubleEndedHeap([1, 3])
    for _ in range(100):
        heap.add(2)
    assert len(heap.min_heap) > 100
    for _ in range(10):
        heap.remove(2)
    # no cleanup yet
    assert len(heap.min_heap) > 100
    for _ in range(90):
        heap.remove(2)
    assert len(heap.min_heap) < 10
    assert len(heap) == 2

    # for cleanup coverage
    heap.pop()
    heap.pop()


@pytest.mark.skip
def test_basic_modifiable_double_ended_heap():
    import pytest

    mheap = ModifiableDoubleEndedHeap([0.1, 0.2])
    mheap.add(-0.3)
    mheap.add(-0.3)
    assert mheap.get_smallest() == -0.3
    assert mheap.get_largest() == 0.2
    assert 0.2 in mheap
    assert mheap.pop() == 0.2
    assert 0.2 not in mheap
    mheap.remove(0.1)
    with pytest.raises(KeyError):
        mheap.remove(0.1)

    mheap.popleft()
    mheap.popleft()
    assert len(mheap) == 0
    assert len(mheap.min_heap) == 0
    assert len(mheap.max_heap) == 0

    mheap.discard(1)
