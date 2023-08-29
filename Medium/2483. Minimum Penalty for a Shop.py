class Solution:
    """
    You are given the customer visit log of a shop represented by a 0-indexed
    string customers consisting only of characters 'N' and 'Y':
    - if the ith character is 'Y', it means that customers come at the ith hour
    - whereas 'N' indicates that no customers come at the ith hour.

    If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
    - For every hour when the shop is open and no customers come, the penalty increases by 1.
    - For every hour when the shop is closed and customers come, the penalty increases by 1.
    - Return the earliest hour at which the shop must be closed to incur a minimum penalty.

    Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

    Constraints:
    - 1 <= customers.length <= 10^5
    - customers consists only of characters 'Y' and 'N'.
    """

    def bestClosingTime(self, customers: str) -> int:
        # penalty = amount of customer vists after closing + no customer visits
        # before closing. At hour 0 this is equal to the total amount of visits
        penalty = customers.count("Y")

        # track minimum penalty and corresponding closing time
        result_penalty = penalty
        result_index = 0
        for closing_hour, customer in enumerate(customers, start=1):
            if customer == "Y":
                # if current hour has visitors, then staying open for the visitors
                # to stay at current hour decreases penalty by 1
                penalty -= 1
                if penalty < result_penalty:
                    result_penalty = penalty
                    result_index = closing_hour
            else:
                # else staying open for the current hour incurs a penalty as there are no visitors
                penalty += 1

        return result_index
