# t1 = "abcdefgxyopyknd"
# t2 = "gefoxyloon"
# i = 0
# while i < len(t1):
#     if t1[i] not in t2:
#         t1[i] = ''
# print(t1)

"laobcdemmmmmmmfgxyopyknd"
"gefoxyloon"

text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"

dp1 = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
dp2 = [[0]*(len(text2)+1)]*(len(text1)+1)

print(dp1)
print(dp2)
print(dp1 == dp2)
print(len(dp1))
print(len(dp2))
print(len(dp1[0]))
print(len(dp2[0]))


[[0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5], [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5]]
