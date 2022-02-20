
# stolen
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n):
        self.parents = list(range(n))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        # Creat unions between indexes
        ownership = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        # Append emails to correct index
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(email_account) for i, email_account in ans.items()]
