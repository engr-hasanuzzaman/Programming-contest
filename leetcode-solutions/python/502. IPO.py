# https://leetcode.com/problems/ipo/

from heapq import heappush, heappop, heapify


class Project:
    def __init__(self, profit, req_capital):
        self.profit = profit
        self.req_capital = req_capital


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if k == 0:
            return w
        N = len(profits)
        projects = [Project(profits[i], capital[i]) for i in range(N)]

        # order by min_capital
        projects.sort(key=lambda p: p.req_capital)

        # take projects with req_capital <= w
        idx = 0
        heap = []
        while idx < N and projects[idx].req_capital <= w:
            heappush(heap, -projects[idx].profit)
            idx += 1

        heapify(heap)
        for _ in range(k):
            # print(heap)
            if not heap:
                return w
            # use min heap as max heap
            w += (-heappop(heap))

            # add new e
            while idx < N and projects[idx].req_capital <= w:
                heappush(heap, -projects[idx].profit)
                idx += 1

        return w
