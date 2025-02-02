"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [a_i, b_i] indicates that you must take course a_i first if
you want to take course b_i.
- For example, the pair [0, 1] indicates that you have to take course 0 before
  you can take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b,
and course b is a prerequisite of course c, then course a is a prerequisite of
course c.

You are also given an array queries where queries[j] = [u_j, v_j]. For the jth
query, you should answer whether course u_j is a prerequisite of course v_j or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Constraints:
- 2 <= numCourses <= 100
- 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
- prerequisites[i].length == 2
- 0 <= a_i, b_i <= numCourses - 1
- a_i!= b_i
- All the pairs [a_i, b_i] are unique.
- The prerequisites graph has no cycles.
- 1 <= queries.length <= 10^4
- 0 <= u_i, v_i <= numCourses - 1
- u_i!= v_i
"""

from functools import cache


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """

        @cache
        def is_prerequisite(couese_a: int, course_b: int) -> bool:
            nonlocal is_direct_prerequisite_of
            if course_b in is_direct_prerequisite_of[couese_a]:
                return True
            return any(
                is_prerequisite(course_c, course_b)
                for course_c in is_direct_prerequisite_of[couese_a]
            )

        is_direct_prerequisite_of: list[set[int]] = [set() for _ in range(numCourses)]
        for pre, post in prerequisites:
            is_direct_prerequisite_of[pre].add(post)

        return [is_prerequisite(a, b) for a, b in queries]
