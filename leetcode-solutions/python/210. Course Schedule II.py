# https://leetcode.com/problems/course-schedule-ii/

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        dep = [0] * numCourses
        for i in range(len(prerequisites)):
            c, p = prerequisites[i]
            graph[p].append(c)
            dep[c] += 1
        q = deque()
        # start with coures which have zero dep
        for i, n in enumerate(dep):
            if n == 0:
                q.append(i)
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for n in graph[cur]:
                dep[n] -= 1
                if dep[n] == 0:
                    q.append(n)
        if len(ans) == numCourses:
            return ans
        else:
            return []
