"""
You are given an integer n, which indicates that there are n courses labeled from
1 to n. You are also given a 2D integer array relations where
relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to
be completed before course nextCoursej (prerequisite relationship). Furthermore,
you are given a 0-indexed integer array time where time[i] denotes how many months
it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses
following these rules:
- You may start taking a course at any time if the prerequisites are met.
- Any number of courses can be taken at the same time.
- Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every
course (i.e., the graph is a directed acyclic graph).

Constraints:
- 1 <= n <= 5 * 10^4
- 0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)
- relations[j].length == 2
- 1 <= prevCoursej, nextCoursej <= n
- prevCoursej != nextCoursej
- All the pairs [prevCoursej, nextCoursej] are unique.
- time.length == n
- 1 <= time[i] <= 10^4
- The given graph is a directed acyclic graph.
"""
import heapq


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """Build prerequisite graph-like structure, iterate through courses using minheap.

        Possible to have O(|relations| + n) time complexity by using a normal
        queue/stack and tracking the "latest allowed start time" for each course,
        so that curr_time = max_start_time[course] + time[course] and updating the
        result to be max(result, curr_time).

        O(|relations| + n * log(n)) / O(|relations| + n)    time / space complexity
        """
        # use `relations` build prequisite counter and post courses list
        remaining_prequisites = [0] * n
        post_courses: list[list[int]] = [[] for _ in range(n)]
        for pre, post in relations:
            # relations are 1 indexed, so decrement
            pre -= 1
            post -= 1
            post_courses[pre].append(post)
            remaining_prequisites[post] += 1

        # build a minheap of finish times for courses with no prerequisites
        queue = [
            (time[course], course)
            for course, incoming_count in enumerate(remaining_prequisites)
            if incoming_count == 0
        ]
        heapq.heapify(queue)

        # track current time as months that have passed
        curr_time = 0
        while queue:
            # get earliest finish time from queue
            curr_time, course = heapq.heappop(queue)
            for post in post_courses[course]:
                # decrement prerequisite counter for all post courses
                remaining_prequisites[post] -= 1
                if remaining_prequisites[post] == 0:
                    # if a course has no more prequisites, push it to the queue with its finish time
                    heapq.heappush(queue, (curr_time + time[post], post))

        # return months that have passed
        return curr_time
