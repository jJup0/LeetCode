import heapq


class Solution:
    def minDifficulty(self, job_difficulty: list[int], d: int) -> int:
        return self.minDifficulty_fast(job_difficulty, d)

    def minDifficulty_fast(self, job_difficulty: list[int], d: int) -> int:
        """
        n := len(job_difficulty)
        O(d * n) / O(n)     time / space complexity
        """
        INT_INF = 1_000_000

        n = len(job_difficulty)
        if n < d:
            return -1

        self._job_difficulty = job_difficulty

        # prev_dp[i] is difficulty to complete up to ith job with `current_day` days,
        # next_dp[i] is with `current_day + 1` days
        prev_dp = [INT_INF] * n
        next_dp = [0] * n
        for current_day in range(d):
            # stack of jobs where for job_idx_stack[i], job_idx_stack[j]:
            # `job_difficulty[i] > job_difficulty[j]` if `i < j`
            job_idx_stack: list[int] = []
            # first job that can be taken is at `current_day`th job,
            # since at least one job a day must be completed
            for job_idx in range(current_day, n):
                next_dp[job_idx] = self._calc_min_diff(
                    prev_dp, next_dp, job_idx_stack, job_idx
                )

            # switch list pointers, data now in next_dp is invalid
            prev_dp, next_dp = next_dp, prev_dp

        return prev_dp[-1]

    def _calc_min_diff(
        self,
        prev_dp: list[int],
        next_dp: list[int],
        job_idx_stack: list[int],
        starting_job_idx: int,
    ) -> int:
        current_job_diff = self._job_difficulty[starting_job_idx]
        # base difficulty is difficulty to only complete current job
        min_diff_upto_job = (
            prev_dp[starting_job_idx - 1] + current_job_diff
            if starting_job_idx
            else current_job_diff
        )

        # while the top of the stack is less/equal to the current job,
        # include the easier job in the current day
        while (
            job_idx_stack
            and self._job_difficulty[job_idx_stack[-1]] <= current_job_diff
        ):
            job_2_idx = job_idx_stack.pop()
            job_d_diff = self._job_difficulty[job_2_idx]
            assert job_2_idx < starting_job_idx
            assert job_d_diff < current_job_diff
            # update minimum difficulty if it is easier 
            min_diff_upto_job = min(
                min_diff_upto_job,
                next_dp[job_2_idx] - self._job_difficulty[job_2_idx] + current_job_diff,
            )

        if job_idx_stack:
            # if total difficulty for a more difficult job is less than the
            # current minimum difficulty, update minimum difficulty
            min_diff_upto_job = min(min_diff_upto_job, next_dp[job_idx_stack[-1]])

        job_idx_stack.append(starting_job_idx)
        return min_diff_upto_job

    def minDifficulty_heap(self, job_difficulty: list[int], d: int) -> int:
        """
        n := len(job_difficulty)
        O(n^2 * d) / O(n^2 * d)     time / space complexity
        """
        n = len(job_difficulty)
        if n < d:
            return -1

        INT_INF = 1_000_000

        # dp[i][j] = minimum difficulty for completing `j` jobs in `i` days
        dp = [[INT_INF] * (n + 1) for _ in range(d + 1)]

        # heap[i] = total_difficulty, -day, -job_index. Values are negated
        # to prefer later days and more jobs completed
        heap: list[tuple[int, int, int]] = [(0, 0, 0)]
        while heap and dp[-1][-1] == INT_INF:
            difficulty, neg_day, neg_job_i = heapq.heappop(heap)
            day = -neg_day
            job_i = -neg_job_i

            # check if lower difficulty has been achieved for this day and job count,
            # continue if greater equal, else update
            if difficulty >= dp[day][job_i]:
                continue
            dp[day][job_i] = difficulty

            # if all days used up, continue
            if day == d:
                continue

            difficulty_today = 0
            for j in range(job_i, n - (d - day) + 1):
                job = job_difficulty[j]
                if job > difficulty_today:
                    difficulty_today = job

                heapq.heappush(
                    heap, (difficulty + difficulty_today, -(day + 1), -(j + 1))
                )

        return dp[-1][-1]


s = Solution()
print(s.minDifficulty_fast([6, 5, 4, 3, 2, 1], 2))
