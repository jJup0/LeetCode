from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        dependents = defaultdict(set)
        prereqs = defaultdict(set)
        for i, j in prerequisites:
            dependents[i].add(j)
            prereqs[j].add(i)
        stack = [node for node in range(numCourses) if not prereqs[node]]  # add all not prereqs to stack
        while stack:
            curCourse = stack.pop()
            for prereq in dependents[curCourse]:
                prereqs[prereq].remove(curCourse)
                if not prereqs[prereq]:
                    stack.append(prereq)    # (add all not prereqs to stack) so if now nothing still depends on it, add to stack
            prereqs.pop(curCourse)    # nothing depends on curCourse anymore since we popped them all in prerequisites{}
        return not prereqs
