import heapq


class Solution:
    """
    You are given an integer array cookies, where cookies[i] denotes the number
    of cookies in the ith bag. You are also given an integer k that denotes the
    number of children to distribute all the bags of cookies to. All the cookies
    in the same bag must go to the same child and cannot be split up.

    The unfairness of a distribution is defined as the maximumtotal cookies
    obtained by a single child in the distribution.

    Return the minimum unfairness of all distributions.

    Constraints:
    - 2 <= cookies.length <= 8
    - 1 <= cookies[i] <= 10^5
    - 2 <= k <= cookies.length
    """

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        """Calculate a greedy heuristic first, and then exhaustive dfs search.
        O(n^k) / O(n * k)   time / space complexity.
        """
        # calculate greedy heuristic by sorting cookies by size descending,
        # and greedily giving the next cookie to the child with the fewest cookies
        cookies.sort(reverse=True)
        heap: list[tuple[int, int]] = [(0, i) for i in range(k)]
        for c in cookies:
            cookie_count, index = heapq.heappop(heap)
            cookie_count += c
            heapq.heappush(heap, (cookie_count, index))
        result = max(cookie_count for cookie_count, _ in heap)

        def dfs(cookies_idx: int, distribution: list[int]) -> None:
            """Updates nonlocal `result` with the best possible distribution.

            Args:
                cookies_idx (int): Index of which cookie to distribute next.
                distribution (list[int]):
                  Assignment of current cookie count to children.
                  distribution[child_index] = current_cookie_count.
            """
            nonlocal cookies, result
            if cookies_idx == len(cookies):
                # if all cookies have been destributed, update the fairness,
                # no need to check if max(distribution) is smaller than result,
                # as otherwise dfs() would not have been called
                result = max(distribution)
                return

            curr_cookie = cookies[cookies_idx]
            # iterate over which child to give the cookie
            for child_idx, cookie_count in enumerate(distribution):
                new_cookie_sum = cookie_count + curr_cookie
                # if giving the current child a cookie cannot
                # improve the result, do not give the cookie
                if new_cookie_sum >= result:
                    continue

                # give the child the cookies
                distribution[child_idx] = new_cookie_sum
                # dfs and distribute the next cookie, no need to copy the state
                dfs(cookies_idx + 1, distribution)
                # restore state, take the cookie away from the child again
                distribution[child_idx] = cookie_count

        dfs(0, [0] * k)
        return result
