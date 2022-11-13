from random import randint as rint
from typing import Any, List, Tuple

import pyperclip


class TestData:

    def __init__(self, test_cases, count=10):
        self.test_cases = test_cases
        self.case_count = count

    def clear_test_cases(self):
        self.test_cases.clear()

    def set_test_case_count(self, count):
        self.case_count = count

    def int_couple_list(self, min_val, max_val, size):
        l = []
        for _ in range(size):
            l.append([rint(min_val, max_val), rint(min_val, max_val)])

        self.test_cases.append(str(l))

    def int_list(self, min_val, max_val, size):
        l = []
        for _ in range(size):
            l.append(rint(min_val, max_val))

        self.test_cases.append(str(l))

    def almost_non_decreasing_int_list(self, size):
        l = list(range(size))

        for _ in range(rint(0, 3)):
            l[rint(0, size-1)] = rint(0, size)

        self.test_cases.append(str(l))

    def two_rects(self):
        for _ in range(2):
            self.test_cases.append(str(rint(-10, 0)))
            self.test_cases.append(str(rint(-10, 0)))
            self.test_cases.append(str(rint(0, 10)))
            self.test_cases.append(str(rint(0, 10)))

    def digits_str(self, size):
        self.test_cases.append('"' + ''.join(str(rint(0, 9)) for _ in range(size)) + '"')

    def similar_words_list(self, line_count, word_count, max_word_len):
        for _ in range(line_count):
            l = []
            for _ in range(word_count):
                l.append(''.join(chr(rint(ord('a'), ord('e'))) for _ in range(rint(0, max_word_len))))
            self.test_cases.append(str(l))

    def skyline_list(self, min_l, max_l, min_w, max_w, min_h, max_h, size):
        l = []
        for _ in range(size):
            left = rint(min_l, max_l)
            right = left + rint(min_w, max_w)
            height = rint(min_h, max_h)
            l.append([left, right, height])
        l.sort()
        self.test_cases.append(str(l))


class ComplexStructureTestData:
    def median_from_data_stream(self, calls: int) -> Tuple[List[str], List[List[int]]]:
        methods = ["MedianFinder"] + ["addNum", "findMedian"] * calls
        paramss = [[]]
        for _ in range(calls):
            paramss.append([rint(-100_000, 100_000)])
            paramss.append([])

        return methods, paramss

    def generate_and_copy_to_clip(self, calls):
        methods, paramss = self.median_from_data_stream(1)

        mstr = str(methods).replace(" ", "").replace("'", '"')
        pstr = str(paramss).replace(" ", "").replace("'", '"')
        s = mstr + "\n" + pstr
        pyperclip.copy(s)
        print(s)
        print("^ copied to clipboard")

        return methods, paramss


    def evaluate(self, methods, paramss):
        print(methods, paramss)
        for method, params in zip(methods, paramss):
            if method == "MedianFinder":
                # S = MedianFinder(*params)
                pass
            else:
                # res = eval(f"S.{method}({','.join(str(param) for param in params)})")
                # if res:
                # print(res)
                pass


if __name__ == "__main__":
    test_cases = []
    t = TestData(test_cases, 10)
    SIZE = 10
    for _ in range(t.case_count):
        t.skyline_list(1, 200, 1, 200, 1, 20, SIZE)

    s = '\n'.join(test_cases).replace(" ", "").replace("'", '"')
    pyperclip.copy(s)
    print(s)
    print("^ copied to clipboard")
