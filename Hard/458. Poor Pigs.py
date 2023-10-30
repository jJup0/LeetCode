"""
There are buckets buckets of liquid, where exactly one of the buckets is poisonous.
To figure out which one is poisonous, you feed some number of (poor) pigs the liquid
to see whether they will die or not. Unfortunately, you only have minutesToTest
minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:
1. Choose some live pigs to feed.
2. For each pig, choose which buckets to feed it. The pig will consume all the chosen
   buckets simultaneously and will take no time. Each pig can feed from any number of
   buckets, and each bucket can be fed from by any number of pigs.
3. Wait for minutesToDie minutes. You may not feed any other pigs during this time.
4. After minutesToDie minutes have passed, any pigs that have been fed the poisonous
   bucket will die, and all others will survive.
5. Repeat this process until you run out of time.

Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs
needed to figure out which bucket is poisonous within the allotted time.

Constraints:
- 1 <= buckets <= 1000
- 1 <= minutesToDie <= minutesToTest <= 100
"""
import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """Let `test_rounds` := minutesToTest//minutesToDie. We can test
        `test_rounds` times. Each pig can either die after a test or not.
        That means each pig can encode `test_rounds + 1` information:

        For a line of bucketes of length `test_rounds + 1`:
        1 pig can discover what bucket is poisionous by testing each one until it dies.

        For a square of buckets, we need 2 pigs: let one pig test each row, and the
        other test each column. This way we can find out on whatever row and column
        both pigs die on (or if they survive, then the last row and/or column), is
        the poisonous bucket.

        Same procedure for a cube, we need three pigs.

        For cubes of higher dimensions this analogy breaks down, but the strategy still works.
        We encode the buckets as a number in base `test_rounds + 1`.
        The first pig drinks all buckets with a 0 in the units position in the
        first round, then all buckets with a 1 in the units position, then all
        buckets with a 2 (if test_rounds+1 > 2) etc.
        The second pig drinks all buckets with a 0 in the "tens" position, then
        all with a 1 etc.


        Now we just have to find an integer `pigs` where: (test_rounds + 1)^pigs >= buckets,
        i.e. pigs >= log_`test_rounds + 1`(buckets)
        """

        testing_rounds = minutesToTest // minutesToDie
        # due to the inaccuracy of floats, we cannot simply math.ceil the logarithm result
        # e.g. math.log(125, 5) == 3.0000000000000004 instead of 3, and so
        # when ceiled the result is 4 instead of 3
        inaccurate_float_result = math.log(buckets, testing_rounds + 1)
        inaccurate_int_result = math.ceil(inaccurate_float_result)

        check_pow = math.pow(testing_rounds + 1, inaccurate_int_result - 1)

        if check_pow >= buckets:
            return inaccurate_int_result - 1
        return inaccurate_int_result
