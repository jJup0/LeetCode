class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from
    0 to numCourses - 1. You are given an array prerequisites where
    prerequisites[i] = [a_i, b_i] indicates that you must take course b_i
    first if you want to take course a_i.
    - For example, the pair [0, 1], indicates that to take course 0 you have
    to first take course 1.

    Return true if you can finish all courses. Otherwise, return false.

    Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= 5000
    - prerequisites[i].length == 2
    - 0 <= ai, bi < numCourses
    - All the pairs prerequisites[i] are unique.
    """

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        O(numCourses + prerequisites) / O(numCourses + prerequisites)   time / space complexity
        """
        # for each course list prerequisites, and the courses it is a prerequisite for
        course_to_pres: list[set[int]] = [set() for _ in range(numCourses)]
        course_to_posts: list[list[int]] = [[] for _ in range(numCourses)]
        for pre, post in prerequisites:
            course_to_pres[post].add(pre)
            course_to_posts[pre].append(post)

        # courses with no prerequisites
        availible_courses = [
            course for course, pres in enumerate(course_to_pres) if not pres
        ]
        finished_courses = 0

        # take courses while there are courses to take
        while availible_courses:
            base_course = availible_courses.pop()
            finished_courses += 1

            for post in course_to_posts[base_course]:
                # remove current course as prerequisite from all other courses
                course_to_pres[post].discard(base_course)

                # if this makes a course have no more prerequisites,
                # add it to list of availible courses
                if not course_to_pres[post]:
                    availible_courses.append(post)

        return finished_courses == numCourses
