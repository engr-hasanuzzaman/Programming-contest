# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        acts = []
        for account in accounts:
            acts.append(Account(account))

        union_find = UnionFind(acts)

        # create_connection
        for i in range(len(acts)):
            for j in range(i+1, len(acts)):
                account1 = acts[i]
                account2 = acts[j]
                for email in account1.emails.keys():
                    if account2.has_email(email):
                        union_find.union(account1, account2)
        ans = []
        for accounts in union_find.get_connectec_component():
            ans.append(Account.merge(accounts))
        return ans


class Account:
    def __init__(self, data):
        self.name = data[0]
        self.emails = {}
        for email in data[1:]:
            self.emails[email] = True

    def has_email(self, email):
        return email in self.emails

    @classmethod
    def merge(cls, accounts):
        emails = []
        for acc in accounts:
            emails += acc.emails.keys()
        emails = list(set(emails))
        emails.sort()
        return [accounts[0].name] + emails


class UnionFind:
    def __init__(self, accounts):
        self.accounts = accounts
        self.idx_map = {}
        self.parent = [-1] * len(accounts)

        for idx, account in enumerate(accounts):
            self.idx_map[account] = idx
            self.accounts[idx] = account

    def union(self, account1, account2):
        p1 = self.find(account1)
        p2 = self.find(account2)
        if p1 == p2:
            return

        parent1_weight, parent2_weight = abs(
            self.get_weight(p1)), abs(self.get_weight(p2))

        # p1 > p2
        if parent2_weight > parent1_weight:
            p1, p2 = p2, p1

        self.set_weight(p1, -(parent1_weight + parent2_weight))
        self.parent[self._idx(p2)] = self._idx(p1)

    def is_connected(self, account1, account2):
        return self.find(account1) == self.find(account2)

    def _idx(self, account):
        return self.idx_map[account]

    def find(self, account):
        idx = self._idx(account)

        if self.parent[idx] < 0:
            return account
        return self.find(self.accounts[self.parent[idx]])

    def get_weight(self, parent):
        idx = self._idx(parent)
        return self.parent[idx]

    def set_weight(self, parent, weight):
        idx = self._idx(parent)
        self.parent[idx] = weight

    def get_connectec_component(self):
        group = defaultdict(list)
        for account in self.accounts:
            parent = self.find(account)
            p_id = self._idx(parent)
            group[p_id].append(account)
        return group.values()
