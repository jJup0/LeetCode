"""
There are n friends that are playing a game. The friends are sitting in a
circle and are numbered from 1 to n in clockwise order. More formally, moving
clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n,
and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:
1. Start at the 1st friend.
2. Count the next k friends in the clockwise direction including the friend you
   started at. The counting wraps around the circle and may count some friends more
   than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, go back to step 2
   starting from the friend immediately clockwise of the friend who just lost and
   repeat.
5. Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

Constraints:
- 1 <= k <= n <= 500
"""


class RingListNode:
    def __init__(self, x: int, next: "RingListNode | None" = None):
        self.val = x
        self.next = next

    def __str__(self) -> str:
        vals: list[int | str] = [self.val]
        node = self.next
        while node and node is not self:
            vals.append(node.val)
            node = node.next
        if node is self:
            vals.append("loop")
        return str(vals)


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.findTheWinner_recursive(n, k)

    def findTheWinner_recursive(self, n: int, k: int) -> int:
        """
        O(n) / O(n)     time / space complexity
        """

        def recursive_0_indexed(n: int, k: int) -> int:
            if n == 1:
                return 0
            # calculate winner of of game with one less person
            winner_smaller_game = recursive_0_indexed(n - 1, k)

            # `winner_smaller_game` contains the winner assuming we start at the person with index 0
            # however, since we start at person with index k and not 0, simply add k to the result
            winner_smaller_game += k

            # modulo n since the game is played in a circle
            return winner_smaller_game % n

        return recursive_0_indexed(n, k) + 1  # 1-indexed

    def findTheWinner_linear_iterative(self, n: int, k: int) -> int:
        """
        Based on recurisve solution, but not intuitive at all if recursive solution is not known.
        O(n) / O(1)     time / space complexity
        """
        winner = 0
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1  # 1-indexed

    def findTheWinner_array_pseudo_pointer(self, n: int, k: int) -> int:
        """
        O(n * k) / O(n)       time / space complexity
        """
        # 0-indexed
        nexts = list(range(1, n))
        nexts.append(0)

        curr = -1
        for _ in range(n - 1):
            for _ in range(k - 1):
                curr = nexts[curr]
            nexts[curr] = nexts[nexts[curr]]
        return nexts[curr] + 1  # 1-indexed

    def findTheWinner_linked_list(self, n: int, k: int) -> int:
        """
        O(n * k) / O(n)       time / space complexity
        """
        head = tail = RingListNode(1)
        for i in range(2, n + 1):
            tail.next = RingListNode(i)
            tail = tail.next
        tail.next = head

        curr = tail
        for _ in range(n - 1):
            for _ in range(k - 1):
                curr = curr.next
                assert curr
            assert curr.next
            curr.next = curr.next.next
        return curr.val

    def findTheWinner_naive(self, n: int, k: int) -> int:
        """
        O(n^2 * k) / O(n)       time / space complexity
        """
        # 0-indexed
        playing = [True] * n
        i = -1
        for _ in range(n - 1):
            step = 0
            while step < k:
                i = (i + 1) % n
                step += playing[i]
            playing[i] = False
        return playing.index(True) + 1  # 1-indexed
