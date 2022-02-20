# import timeit


# def doset():
#     s = set()
#     for i in range(10000):
#         s.add(i)
#     l = list(s)


# def dolist():
#     s = list()
#     for i in range(10000):
#         s.append(i)
#     l = set(l)


# x = timeit.timeit(doset, number=100)
# print(x)
# x = timeit.timeit(doset, number=100)
# print(x)
