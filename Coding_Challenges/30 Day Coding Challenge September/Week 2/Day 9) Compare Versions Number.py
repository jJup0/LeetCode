# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         version1 = [int(n) for n in version1.split('.')]
#         version2 = [int(n) for n in version2.split('.')]
#         for i in range(min(len(version1), len(version2))):
#             if int(version1[i]) != int(version2[i]):
#                 break
#         else:
#             i += 1
#             if len(version1) < len(version2):
#                 return 1 if 0 > sum(version2[i:]) else -1 if 0 < sum(version2[i:]) else 0
#             elif len(version1) > len(version2):
#                 return 1 if sum(version1[i:]) > 0 else -1 if sum(version1[i:]) < 0 else 0
#             else:
#                 return 0
#         return 1 if version1[i] > version2[i] else -1 if version1[i] < version2[i] else 0
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(n) for n in version1.split('.')]
        version2 = [int(n) for n in version2.split('.')]
        m, n = len(version1), len(version2)
        for i in range(max(m, n)):
            v1_n = version1[i] if i < m else 0
            v2_n = version2[i] if i < n else 0
            if v1_n != v2_n:
                return 1 if v1_n > v2_n else -1
        return 0
