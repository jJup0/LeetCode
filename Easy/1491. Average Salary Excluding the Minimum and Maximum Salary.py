class Solution:
    """
    You are given an array of unique integers salary where salary[i] is the
    salary of the ith employee.

    Return the average salary of employees excluding the minimum and maximum salary.
    Answers within 10-5 of the actual answer will be accepted.

    Constraints:
        3 <= salary.length <= 100
        1000 <= salary[i] <= 10^6
        All the integers of salary are unique.
    """

    def average(self, salary: list[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
