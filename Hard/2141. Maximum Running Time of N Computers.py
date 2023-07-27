class Solution:
    """
    You have n computers. You are given the integer n and a 0-indexed integer array
    batteries where the ith battery can run a computer for batteries[i] minutes. You are
    interested in running alln computers simultaneously using the given batteries.

    Initially, you can insert at most one battery into each computer. After that and at
    any integer time moment, you can remove a battery from a computer and insert another
    battery any number of times. The inserted battery can be a totally new battery or a
    battery from another computer. You may assume that the removing and inserting
    processes take no time.

    Note that the batteries cannot be recharged.

    Return the maximum number of minutes you can run all the n computers simultaneously.

    Constraints:
    - 1 <= n <= batteries.length <= 10^5
    - 1 <= batteries[i] <= 10^9
    """

    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        """
        Start with computers hooked up to largest batteries.
        Then greedily distribute remaining batteries as if they were all split up into units of 1.
        O(n + m) / O(n)     time / space complexity
        """
        if len(batteries) < n:
            return 0

        batteries.sort()
        # assign largest batteries to computers
        computer_batteries = batteries[-n:]

        # add pseudo-computer with unlimited battery so that
        # computer with larget battery can never be matched
        computer_batteries.append(float("inf"))  # type: ignore # float incompatible

        # charge in len(batteries)-n smallest batteries
        charge_remaining = sum(batteries[i] for i in range(len(batteries) - n))
        for computer_count, computer_charge in enumerate(computer_batteries, start=1):
            # charge needed to match the charge of all previous computers
            # with the computer that has the next largest battery
            charge_needed = (computer_count) * (
                computer_batteries[computer_count] - computer_charge
            )
            # if the charge can be matched, "use up" batteries and move to next computer
            if charge_remaining >= charge_needed:
                charge_remaining -= charge_needed
                continue
            # else if the charge of the next computer cannot be matched, "distribute"
            # the charge equally among the previous computers, and return
            return computer_charge + charge_remaining // (computer_count)

        assert False, "Computer with infinite battery can not be matched"
