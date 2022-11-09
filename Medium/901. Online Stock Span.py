from typing import List, Tuple


class StockSpanner:
    """
    Design an algorithm that collects daily price quotes for some stock and returns the span of
    that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days
    (starting from today and going backward) for which the stock price was less than or equal to
    today's price.
        For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85],
            then the stock spans would be [1,1,1,2,1,4,6].

    Implement the StockSpanner class:
        StockSpanner() Initializes the object of the class.
        int next(int price) Returns the span of the stock's price given that today's price is
            price.

    Constraints:
        1 <= price <= 10^5
        At most 10^4 calls will be made to next.
    """

    def __init__(self):
        """
        Keep track of previous prices in a stack, and compressing last items on the satck when a
        higher price occurs.
        O(calls_to_next) / O(n)     time / space complexity
        """

        # strictly decreasing stack
        # stack[i] = (highest price for a range of consecutive days, amount of days)
        # init with impossibly high value to avoid checking if stack is empty
        self.stack: List[Tuple[int, int]] = [(1_000_000, 0)]

    def next(self, price: int) -> int:
        # O(1) amortized time complexity

        res = 1
        # while the price is higher than on previous days, add days to result
        while self.stack[-1][0] <= price:
            res += self.stack.pop()[1]

        # append price and result to stack
        self.stack.append((price, res))
        return res
