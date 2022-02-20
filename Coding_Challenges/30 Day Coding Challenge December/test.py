# import timeit
# import random
# from typing import *


# def t1():
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         res = 0
#         for i, c in enumerate(mods[1:30], start=1):
#             if c:
#                 res += c * mods[60-i]

#     global mods
#     numPairsDivisibleBy60(0, mods)


# def t2():
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         res = 0
#         for i, c in enumerate(mods[1:30], start=1):
#             res += c * mods[60-i]

#     global mods
#     numPairsDivisibleBy60(0, mods)


# mods = [0 if random.random() < 0.98 else random.randint(0, 100) for _ in range(60)]

# RUNS = 100
# x = timeit.timeit(t1, number=RUNS)
# print(x)
# x = timeit.timeit(t2, number=RUNS)
# print(x)

# print(sorted(random.randint(0, 100) for _ in range(10)))
n = 10
c = 11
check = []
for P in range(0, c):
    i = int(n*P/c)
    while i < int(n*(P+1)/c):
        check.append(i)
        i += 1

print(check)
j = 0

for num in check:
    if num != j:
        print("{num} != {j}")
    j += 1
