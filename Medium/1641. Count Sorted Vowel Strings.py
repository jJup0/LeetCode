class Solution:
    def countVowelStrings(self, n: int) -> int:
        # # mathematical O(1) solution I found:
        # # actual formula is (l - 1 + n)!/(n! * (l-1)!), with n = n and l = 5
        # return (n+4)*(n+3)*(n+2)*(n+1) // 24      # 24 = 4 factorial

        # list to track how many lexicographically sorted strings start with a letter
        # [u, o, i, e, a], so starting_with[2] represents how many strings start with 'i' so far
        starting_with = [1, 1, 1, 1, 1]

        # starting_with initialized for n=1, so start at 1
        for _ in range(1, n):

            # keep track of the running sum for the current iteration
            running_sum = 0

            # go through previous values of starting_with
            for i, count in enumerate(starting_with):
                # add the count to running_sum
                running_sum += count
                # update the current index with the running sum
                starting_with[i] = running_sum

                # example to show how it works:
                # start with n=1, arr = [1, 2, 3, 4, 5]
                # then for n=2, one can only prepend 'u' to all strings that start with 'u', therfore new_u = 1
                # for 'o', one can only prepend it to all strings that start with 'u' or 'o' etc...

        return sum(starting_with)
