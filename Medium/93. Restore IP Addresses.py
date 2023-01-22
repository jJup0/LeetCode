class Solution:
    """
    A valid IP address consists of exactly four integers separated by single dots. Each integer
    is between 0 and 255 (inclusive) and cannot have leading zeros.
    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312"
    and "192.168@1.1" are invalid IP addresses.
    Given a string s containing only digits, return all possible valid IP addresses that can be formed by
    inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid
    IP addresses in any order.

    Constraints:
        1 <= s.length <= 20
        s consists of digits only.
    """

    def restoreIpAddresses(self, s: str) -> list[str]:
        # make a copy of length of s, will not change
        n = len(s)

        # result list to be filled by helper()
        res = []

        # constuct IP address as list with length 4 with numbers as strings
        # i: index of next char in s to consider
        # prev_nums: unique list that will be mutated and passed along during generation
        def helper(i, prev_nums):
            # if the list already contains 4 numbers
            if len(prev_nums) == 4:
                # prev_nums contains all digits from s append it in IP format to result
                if i == n:
                    res.append('.'.join(prev_nums))
            # if index for s out of bounds, or too many digits left to place in IP address return
            elif (i >= n) or (n-i > 3 * (4 - len(prev_nums))):
                return
            # if the next digit to add to IP address starts with 0, keep building with only one 0,
            # as leading zeroes are not allowed
            elif s[i] == "0":
                prev_nums.append("0")
                helper(i + 1, prev_nums)
                prev_nums.pop()
            else:
                # take next 1, 2 or 3 digits into consideration as candidate for next part in IP address
                # min(3, n-i) needed to avoid index out of bounds for s
                for j in range(min(3, n - i)):
                    # take a slice of the digits in question
                    s_slice = s[i:i + j + 1]
                    # check to see if number can fit in a byte (only for j == 2 could this if statement evaluate to false)
                    if int(s_slice) < 256:
                        # append digit slice to prev_nums, call helper with new start index, then pop digit slice again
                        prev_nums.append(s_slice)
                        helper(i + j + 1, prev_nums)
                        prev_nums.pop()

        # call helper with index 0, and prev_nums empty
        helper(0, [])
        return res
