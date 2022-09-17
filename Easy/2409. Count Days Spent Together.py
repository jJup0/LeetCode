class Solution:
    """
    Alice and Bob are traveling to Rome for separate business meetings.
    You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the
    city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city fro
    the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format
    "MM-DD", corresponding to the month and day of the date.
    Return the total number of days that Alice and Bob are in Rome together.
    You can assume that all dates occur in the same calendar year, which is not a leap year. Note
    that the number of days per month can be represented as:
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
    Constraints:
        All dates are provided in the format "MM-DD".
        Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
        The given dates are valid dates of a non-leap year.
    """

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Calculate abosulte days past since January 1st, then calculate intersection interval.
        O(1) / O(1)     time / space complexity
        """
        # predefined amount of days in months
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # calculate days away from January 1st for both arrivals and departures
        day_arr_a = sum(months[:int(arriveAlice[:2]) - 1]) + int(arriveAlice[3:])
        day_leave_a = sum(months[:int(leaveAlice[:2]) - 1]) + int(leaveAlice[3:])

        day_arr_b = sum(months[:int(arriveBob[:2]) - 1]) + int(arriveBob[3:])
        day_leave_b = sum(months[:int(leaveBob[:2]) - 1]) + int(leaveBob[3:])

        # calculate intersection interval
        start = max(day_arr_a, day_arr_b)
        stop = min(day_leave_a, day_leave_b)

        # interval may have negative length, return 0 if so
        return max(0, stop-start+1)
