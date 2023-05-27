from random import randint as rint
from typing import Any, List, Tuple

import pyperclip


class TestData:
    def __init__(self, test_cases: list[str], count: int = 10):
        self.test_cases = test_cases
        self.case_count = count

    def clear_test_cases(self):
        self.test_cases.clear()

    def set_test_case_count(self, count: int):
        self.case_count = count

    def int_couple_list(self, min_val: int, max_val: int, size: int):
        l: list[list[int]] = []
        for _ in range(size):
            l.append([rint(min_val, max_val), rint(min_val, max_val)])

        self.test_cases.append(str(l))

    def int_list(self, min_val: int, max_val: int, size: int):
        l: list[int] = []
        for _ in range(size):
            l.append(rint(min_val, max_val))

        self.test_cases.append(str(l))

    def almost_non_decreasing_int_list(self, size: int):
        l = list(range(size))

        for _ in range(rint(0, 3)):
            l[rint(0, size - 1)] = rint(0, size)

        self.test_cases.append(str(l))

    def two_rects(self):
        for _ in range(2):
            self.test_cases.append(str(rint(-10, 0)))
            self.test_cases.append(str(rint(-10, 0)))
            self.test_cases.append(str(rint(0, 10)))
            self.test_cases.append(str(rint(0, 10)))

    def digits_str(self, size: int):
        self.test_cases.append(
            '"' + "".join(str(rint(0, 9)) for _ in range(size)) + '"'
        )

    def similar_words_list(self, line_count: int, word_count: int, max_word_len: int):
        for _ in range(line_count):
            l: list[str] = []
            for _ in range(word_count):
                l.append(
                    "".join(
                        chr(rint(ord("a"), ord("e")))
                        for _ in range(rint(0, max_word_len))
                    )
                )
            self.test_cases.append(str(l))

    def skyline_list(
        self,
        min_l: int,
        max_l: int,
        min_w: int,
        max_w: int,
        min_h: int,
        max_h: int,
        size: int,
    ):
        l: list[list[int]] = []
        for _ in range(size):
            left = rint(min_l, max_l)
            right = left + rint(min_w, max_w)
            height = rint(min_h, max_h)
            l.append([left, right, height])
        l.sort()
        self.test_cases.append(str(l))


class ComplexStructureTestData:
    def median_from_data_stream(self, calls: int) -> Tuple[List[str], List[List[Any]]]:
        methods = ["MedianFinder"] + ["addNum", "findMedian"] * calls
        paramss: list[list[int]] = [[]]
        for _ in range(calls):
            paramss.append([rint(-100_000, 100_000)])
            paramss.append([])

        return methods, paramss

    def generate_and_copy_to_clip(self, calls: int):
        methods, paramss = self.median_from_data_stream(1)

        mstr = str(methods).replace(" ", "").replace("'", '"')
        pstr = str(paramss).replace(" ", "").replace("'", '"')
        s = mstr + "\n" + pstr
        pyperclip.copy(s)
        print(s)
        print("^ copied to clipboard")

        return methods, paramss

    def evaluate(self, methods: list[str], paramss: list[list[Any]]):
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
    t = TestData(test_cases, 3)

    for _ in range(t.case_count):
        t.int_list(min_val=-1000, max_val=1000, size=1000)

    s = "\n".join(test_cases).replace(" ", "").replace("'", '"')
    pyperclip.copy(s)
    print(s)
    print("^ copied to clipboard")
