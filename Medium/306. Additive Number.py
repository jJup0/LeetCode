class Solution:
    """
    An additive number is a string whose digits can form an additive sequence.
    A valid additive sequence should contain at least three numbers. Except for the first two
    numbers, each subsequent number in the sequence must be the sum of the preceding two.
    Given a string containing only digits, return true if it is an additive number or false otherwise.
    Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or
    1, 02, 3 is invalid.
    Constraints:
        1 <= num.length <= 35
        num consists only of digits.
    """

    def isAdditiveNumber(self, num_str: str) -> bool:
        """
        Check if num_str can partitioned in a way that a fibonacci sequence (with different starting numbers) arises
        """
        n = len(num_str)

        # num[:i] is first number in sequence
        for i in range(1, (n//2) + 1):

            # check for leading 0
            if num_str[0] == "0" and i > 1:
                break

            # first number in sequence
            fib1 = int(num_str[:i])

            # num[i:j] is the second number in the sequence
            for j in range(i + 1, n-i + 1):
                # check for leading 0
                if num_str[i] == "0" and j-i > 1:
                    break

                # seq contains last two values in sequence
                seq = [fib1, int(num_str[i:j])]

                # replace index for fibonacci (flip flops between 0 and 1)
                replace_idx = 0

                # start index in num_str for next fibonacci number
                start = j

                while start < n:
                    next_fib = sum(seq)
                    next_fib_str = str(next_fib)
                    l = len(next_fib_str)
                    # check if next fib is next sequence of digits in num_str
                    if num_str[start:start+l] != next_fib_str:
                        break
                    # if yes continue checking, replace fib value in seq, update start index and replace index
                    seq[replace_idx] = next_fib
                    start += l
                    # next time s
                    replace_idx ^= 1
                else:
                    # if end of string sequence reached, return true
                    return True

        # if no sequence is found return false
        return False
