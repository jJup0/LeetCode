class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(n) for n in version1.split('.')]
        version2 = [int(n) for n in version2.split('.')]
        m = len(version1)
        n = len(version2)
        for i in range(max(m, n)):
            v1_n = version1[i] if i < m else 0
            v2_n = version2[i] if i < n else 0
            if v1_n != v2_n:
                return 1 if v1_n > v2_n else -1
        return 0