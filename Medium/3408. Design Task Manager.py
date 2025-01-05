"""
There is a task management system that allows users to manage their tasks, each
associated with a priority. The system should efficiently handle adding,
modifying, executing, and removing tasks.

Implement the TaskManager class:
- TaskManager(vector<vector<int>>& tasks) initializes the task manager with a
  list of user-task-priority triples. Each element in the input list is of the form
  [userId, taskId, priority], which adds a task to the specified user with the
  given priority.
- void add(int userId, int taskId, int priority) adds a task with the specified
  taskId and priority to the user with userId. It is guaranteed that taskId does
  not exist in the system.
- void edit(int taskId, int newPriority) updates the priority of the existing
  taskId to newPriority. It is guaranteed that taskId exists in the system.
- void rmv(int taskId) removes the task identified by taskId from the system.
  It is guaranteed that taskId exists in the system.
- int execTop() executes the task with the highest priority across all users.
  If there are multiple tasks with the same highest priority, execute the one with
  the highest taskId. After executing, the taskId is removed from the system.
  Return the userId associated with the executed task. If no tasks are available,
  return -1.

Note that a user may be assigned multiple tasks.

Constraints:
- 1 <= tasks.length <= 10^5
- 0 <= userId <= 10^5
- 0 <= taskId <= 10^5
- 0 <= priority <= 10^9
- 0 <= newPriority <= 10^9
- At most 2 * 10^5 calls will be made in total to add, edit, rmv, and execTop
  methods.
"""

import abc
import heapq
from collections import defaultdict

from sortedcontainers import SortedList


class BaseTaskManager(abc.ABC):
    @abc.abstractmethod
    def __init__(self, tasks: list[list[int]]): ...

    @abc.abstractmethod
    def add(self, userId: int, taskId: int, priority: int) -> None: ...

    @abc.abstractmethod
    def edit(self, taskId: int, newPriority: int) -> None: ...

    @abc.abstractmethod
    def rmv(self, taskId: int) -> None: ...

    @abc.abstractmethod
    def execTop(self) -> int: ...


class TaskManagerSortedList(BaseTaskManager):
    """
    Maintain a SortedList of current tasks, up to date with the current priority.
    Maintain a dict for O(1) lookup for task IDs.
    """

    def __init__(self, tasks: list[list[int]]):
        """O(n * log(n)) time complexity"""
        self.tlist = SortedList((prio, tid, uid) for uid, tid, prio in tasks)
        self.tid_to_prio = {tid: (prio, uid) for uid, tid, prio in tasks}

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """O(log(n)) time complexity"""
        self.tlist.add((priority, taskId, userId))
        self.tid_to_prio[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        """O(log(n)) time complexity"""
        old_prio, uid = self.tid_to_prio[taskId]
        self.tlist.remove((old_prio, taskId, uid))
        self.tid_to_prio[taskId] = (newPriority, uid)
        self.tlist.add((newPriority, taskId, uid))

    def rmv(self, taskId: int) -> None:
        """O(log(n)) time complexity"""
        old_prio, uid = self.tid_to_prio[taskId]
        self.tlist.remove((old_prio, taskId, uid))
        self.tid_to_prio.pop(taskId)

    def execTop(self) -> int:
        """O(1) time complexity"""
        if not self.tlist:
            return -1
        _prio, tid, uid = self.tlist.pop(-1)
        self.tid_to_prio.pop(tid)
        return uid


class TaskManagerHeap(BaseTaskManager):
    """
    Better time complexity for init and rmv() than SortedList Implementation.
    """

    def __init__(self, tasks: list[list[int]]):
        """O(n) time complexity"""
        self.max_heap = [(-prio, -tid, 0) for _uid, tid, prio in tasks]
        heapq.heapify(self.max_heap)
        # Original implementaiton tracked latest priority for each tasks,
        # which works correctly except in the case for when a task ID is
        # reused with the same priority
        #
        # example:
        # add(1, 1, 1); rmv(1); add(1, 1, 1)
        # execTop()
        # execTop() # prints 1 instead of -1
        self.taskid_to_edit_id = defaultdict(
            int, {tid: 0 for _uid, tid, _prio in tasks}
        )
        self.task_to_uid = {tid: uid for uid, tid, _prio in tasks}

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """O(log(n)) time complexity"""
        self.taskid_to_edit_id[taskId] += 1
        heapq.heappush(
            self.max_heap,
            (-priority, -taskId, self.taskid_to_edit_id[taskId]),
        )
        self.task_to_uid[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        """O(log(n)) time complexity"""
        self.taskid_to_edit_id[taskId] += 1
        heapq.heappush(
            self.max_heap,
            (-newPriority, -taskId, self.taskid_to_edit_id[taskId]),
        )

    def rmv(self, taskId: int) -> None:
        """O(1) time complexity"""
        # increment edit id to invalidate all edits of task id in heap
        self.taskid_to_edit_id[taskId] += 1

    def execTop(self) -> int:
        """
        O(1) amoritzed time complexity.
        Amortizes edit() and rmv() calls().
        """
        while self.max_heap:
            _neg_prio, neg_task_id, edit_id = heapq.heappop(self.max_heap)
            task_id = -neg_task_id

            if edit_id != self.taskid_to_edit_id[task_id]:
                continue

            return self.task_to_uid[task_id]

        return -1


class TaskManager(TaskManagerHeap):
    pass


from typing import Any


def test():
    inputs: list[list[Any]] = [
        [[[1, 101, 10], [2, 102, 20], [3, 103, 15]]],
        [4, 104, 5],
        [102, 8],
        [],
        [101],
        [5, 105, 15],
        [],
    ]

    s = TaskManager(*inputs[0])
    s.add(*inputs[1])
    s.edit(*inputs[2])
    print(s.execTop(*inputs[3]))
    s.rmv(*inputs[4])
    s.add(*inputs[5])


def test2():
    inputs: list[list[Any]] = [
        [[[10, 26, 25]]],
        [26],
        [],
    ]
    s = TaskManager([[10, 26, 25]])
    s.rmv(*inputs[1])
    print(s.execTop())


def test3():
    inputs: list[list[Any]] = [
        [
            [
                [8, 12, 32],
                [0, 28, 49],
                [2, 21, 22],
                [1, 6, 23],
                [1, 10, 30],
                [3, 15, 5],
                [6, 9, 21],
                [7, 24, 2],
                [2, 5, 35],
                [10, 8, 31],
            ]
        ],
        [1, 22, 10],
        [22],
        [],
    ]
    s = TaskManager(*inputs[0])
    s.add(*inputs[1])
    s.rmv(*inputs[2])
    s.execTop(*inputs[3])


def test4():
    inputs: list[list[Any]] = [
        [[[10, 25, 31]]],
        [25, 9],
        [],
    ]
    s = TaskManager(*inputs[0])
    s.edit(*inputs[1])
    res1 = s.execTop(*inputs[2])
    assert res1 == 10, res1


def test_reuse_task_id_bug():
    th = TaskManagerHeap([])
    tsl = TaskManagerSortedList([])
    for t in th, tsl:
        t.add(1, 1, 1)
    for t in th, tsl:
        t.rmv(1)
    for t in th, tsl:
        t.add(1, 1, 1)
    for t in th, tsl:
        print(t.execTop())
    for t in th, tsl:
        print(t.execTop())


def fuzz():
    import random

    def _r():
        return random.randint(1, 1000)

    print("----- FUZZ ----")

    tids = set(_r() for _ in range(50))

    l = [[_r(), tid, _r()] for tid in tids]
    print(f"Init with {l=}")
    tsl = TaskManagerSortedList(l)
    th = TaskManagerHeap(l)

    for i in range(1000):
        if i % 10:
            tids = set(tsl.tid_to_prio.keys())
        r = random.random()
        if r < 0.1:
            if not tsl.tid_to_prio:
                continue
            tid = random.choice(list(tsl.tid_to_prio.keys()))
            print(f"removing {tid}")
            tsl.rmv(tid)
            th.rmv(tid)
        elif r < 0.4:
            tid = next(iter(tids))
            while tid in tids:
                tid = random.randint(0, 100000)
            tids.add(tid)
            add_params = (_r(), tid, _r())
            print(f"adding {add_params}")
            tsl.add(*add_params)
            th.add(*add_params)
        elif r < 0.5:
            real = tsl.execTop()
            heap_res = th.execTop()
            if real != heap_res:
                raise Exception(f"Bad execTop: {heap_res} --- != {real} (real)")
            print(f"execTop(), got {real}")
        else:
            if not tsl.tid_to_prio:
                continue
            tid = random.choice(list(tsl.tid_to_prio.keys()))
            new_prio = _r()
            tsl.edit(tid, new_prio)
            th.edit(tid, new_prio)
            print(f"edit({tid, new_prio})")
