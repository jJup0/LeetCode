import heapq
from typing import List, Tuple


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        INT_INF = 1_000_000

        n = len(jobDifficulty)
        if n < d:
            return -1

        # dp[i] is difficulty to complete up to ith job with k days, dp2 is with k+1 days
        dp = [INT_INF] * n
        dp2 = [0] * n
        for day in range(d):
            stack = []
            for i in range(day, n):
                
                # complete ith job as the "only" job on a day
                dp2[i] = dp[i - 1] + jobDifficulty[i] if i else jobDifficulty[i]
                
                # while the top top on the stack is less/equal to the current job, replace 
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    dp2[i] = min(dp2[i], dp2[j] - jobDifficulty[j] + jobDifficulty[i])
                
                if stack:
                    dp2[i] = min(dp2[i], dp2[stack[-1]])

                stack.append(i)

            dp, dp2 = dp2, dp

        return dp[-1]


    def minDifficulty_partition_flawed_logic(self, jobDifficulty: List[int], d: int) -> int:
        MAX_IMPOSSIBLE = 1_000_000

        def partition(l: int, r: int) -> Tuple[int, int, int, int, int, int]:
            if r-l == 1:
                return MAX_IMPOSSIBLE, -1, -1, -1, l, r

            max_left = [0] * (r-l)
            max_right = [0] * (r-l)

            m = 0
            for i in range(l, r):
                m = max(m, jobDifficulty[i])
                max_left[i-l-1] = m
            max_left[0] = MAX_IMPOSSIBLE
            

            m = 0
            for i in range(r-1, l, -1):
                m = max(m, jobDifficulty[i])
                max_right[i-l] = m

            m = MAX_IMPOSSIBLE
            m_i = -1
            for i, (ml, mr) in enumerate(zip(max_left, max_right)):
                m_curr = ml + mr
                if m_curr < m:
                    m = m_curr
                    m_i = i
            return m, max_left[m_i], max_right[m_i], m_i, l, r

        ls = {(0, len(jobDifficulty)): max(jobDifficulty)}
        for _ in range(d-1):
            partition_results = []
            for l, r in ls:
                partition_results.append(partition(l, r))

            _, diff_l, diff_r, split_idx, l, r = min(partition_results)
            ls.pop((l, r))
            ls[(l, split_idx)] = diff_l
            ls[(split_idx, r)] = diff_r

        print(sorted(ls.items()))

        return sum(ls.values())

    def minDifficulty_heap(self, jobDifficulty: List[int], d: int) -> int:

        MAX_IMPOSSIBLE = 1_000_000
        n = len(jobDifficulty)

        dp = [[MAX_IMPOSSIBLE] * (n + 1) for _ in range(d + 1)]

        heap = [(0, 0, 0)]
        while heap and dp[-1][-1] == MAX_IMPOSSIBLE:
            prev_difficulty, day, job_i = heapq.heappop(heap)
            day = -day
            job_i = -job_i

            if prev_difficulty > dp[day][job_i]:
                continue
            dp[day][job_i] = prev_difficulty

            if day == d:
                continue

            difficulty_today = 0
            for j in range(job_i, n - (d - day) + 1):
                job = jobDifficulty[j]
                if job > difficulty_today:
                    difficulty_today = job

                heapq.heappush(heap, (prev_difficulty + difficulty_today, -(day + 1), -(j + 1)))

        res = dp[-1][-1]
        return -1 if res == MAX_IMPOSSIBLE else res


S = Solution()
# print(S.minDifficulty(
#     [6, 5, 4, 3, 2, 1],
#     2
# )
# )
print(S.minDifficulty(
    [42, 35, 957, 671, 87, 222, 524, 5, 280, 878, 242, 398, 610, 984, 649, 513, 563, 997, 786, 223, 413, 961, 208, 189, 519, 606, 504, 406, 994, 475, 940, 476, 762, 283, 218, 404, 715, 755, 689, 457, 20, 403, 749, 68, 17, 763, 78, 695, 445, 338, 643, 400, 615, 29, 866, 861, 103, 665, 743, 361, 798, 236, 255, 15, 326, 124, 14, 588, 711, 992, 501, 731, 538, 619, 765, 8, 477, 854, 243, 95, 627, 480, 505, 800, 818, 722, 194, 717, 305, 810, 497, 686, 704, 322, 532, 22, 234, 290, 885, 416, 155, 428, 161, 315, 152, 441, 730, 926, 175, 536, 646, 922, 951, 101, 107, 233, 61, 735, 669, 512, 28, 569, 447, 982, 916, 321, 1000, 754, 483, 482, 811, 654, 47, 344, 772, 978, 467, 308, 472, 269, 0, 252, 131, 834, 303, 945, 469, 785, 537, 188, 449,
        675, 528, 733, 271, 541, 822, 328, 904, 876, 889, 55, 16, 853, 154, 767, 573, 925, 279, 697, 525, 431, 375, 958, 836, 911, 166, 965, 523, 709, 923, 587, 603, 226, 354, 641, 620, 316, 110, 292, 529, 943, 1, 151, 737, 959, 27, 56, 353, 681, 26, 677, 337, 723, 12, 914, 955, 134, 370, 260, 490, 684, 364, 618, 232, 870, 985, 196, 225, 359, 129, 58, 341, 67, 494, 757, 229, 323, 256, 21, 783, 692, 642, 37, 909, 248, 81, 345, 425, 478, 651, 309, 435, 10, 534, 450, 576, 144, 201, 496, 267, 609, 11, 454, 531, 966, 156, 176, 190, 542, 856, 365, 983, 947, 758, 950, 388, 820, 867, 833, 605, 741, 34, 663, 884, 65, 628, 969, 864, 664, 718, 805, 891, 657, 863, 960, 518, 71, 300, 756, 613, 667, 228, 274, 971, 970, 552, 556, 648, 251], 10
)
)
