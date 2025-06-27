import bisect
import heapq
import inspect
import itertools
import json
import math
import pathlib
import random
import re
import string
import sys
import time
from collections import Counter, defaultdict, deque
from functools import cache
from typing import Any, Dict, List, Optional, TypeAlias

from sortedcontainers import SortedList

sys.setrecursionlimit(100_000)
TII: TypeAlias = tuple[int, int]
LLI: TypeAlias = list[list[int]]
StrADict: TypeAlias = dict[str, Any]


MOD = 10**9 + 7
INT_INF = 1 << 62


class Solution:
    pass


class ProvidedTestcasesRunner:
    @classmethod
    def _get_single_public_method(cls):
        methods = [
            name
            for name, _func in inspect.getmembers(
                Solution(), predicate=inspect.ismethod
            )
            if not name.startswith("_")
        ]
        assert len(methods) == 1, f"Solution has more than one public method: {methods}"
        return methods[0]

    @classmethod
    def _get_testcase_filepath(cls):
        here = pathlib.Path(__file__).parent
        match = re.search(r"\d", pathlib.Path(__file__).name)
        assert match, "No number in file name"
        question_nr_str = match.group()
        test_case_filename = f"test_case_q{question_nr_str}.txt"
        test_case_filepath = here / test_case_filename
        return test_case_filepath

    @classmethod
    def _get_arguments_for_all_test_cases(cls):
        testcase_filepath = cls._get_testcase_filepath()
        with open(testcase_filepath) as f:
            all_args = [json.loads(line) for line in f]
        return all_args

    @classmethod
    def run_tests(cls):
        s = Solution()
        method_name = cls._get_single_public_method()
        param_count = len(inspect.signature(getattr(s, method_name)).parameters)
        param_count_plus_result = param_count + 1
        all_args = cls._get_arguments_for_all_test_cases()
        for test_case_nr in range(1, len(all_args) // (param_count_plus_result) + 2):
            args = all_args[
                (test_case_nr - 1)
                * param_count_plus_result : (test_case_nr)
                * param_count_plus_result
            ]
            if len(args) < param_count_plus_result:
                # incomplete testcase
                break
            expected_result = args.pop()

            res = getattr(s, method_name)(*args)
            assert res == expected_result, f"{expected_result=} {res=}"
            print(f"Passed testcase {test_case_nr} | result = {res}")


def test():
    s = Solution()
    res = s.___________(
        1,
    )
    real = True
    assert res == real, res


ProvidedTestcasesRunner.run_tests()
test()
