class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # determine sign of result
        start_sign = "-" if (numerator * denominator) < 0 else ""

        # use positive numbers for calculating
        numerator, denominator = abs(numerator), abs(denominator)

        # calculate pre-comma part of result
        integer_part = numerator // denominator

        remainder = (numerator - integer_part * denominator) * 10
        divisor = denominator

        # list containing strings of digits for the result
        post_comma_digits = []
        # dictionary for storing previous remainders and at what iteration they occured
        remainders = {}

        # while remainder exists, and has never been seen
        while remainder and (not (remainder in remainders)):
            # store occurance of remainder
            remainders[remainder] = len(post_comma_digits)

            # calculate next digit
            next_digit = remainder // divisor

            # add it to the digits list
            post_comma_digits.append(str(next_digit))

            # calculate the remainder for the next iteration
            remainder = (remainder - next_digit * divisor) * 10

        # if the result is a recurring decimal, add brackets to the string digit list
        if remainder:
            post_comma_digits[remainders[remainder]] = "(" + post_comma_digits[remainders[remainder]]
            post_comma_digits[-1] += ")"

        # if the result is a decimal, construct the result using a decimal point
        if post_comma_digits:
            return start_sign + str(integer_part) + "." + ''.join(post_comma_digits)

        # else return the result without a decimal point
        return start_sign + str(integer_part)
