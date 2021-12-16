# https://leetcode.com/problems/course-schedule/

from collections import deque
# use topoligical sort which find the order of processing based on the dependency/prerequisite
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        dep = [0] * numCourses
        # create a graph with parent -> [childs] with keep number dep for child
        for i in range(len(prerequisites)):
            c, p = prerequisites[i]
            graph[p].append(c)
            dep[c] += 1
        q = deque()
    
        # take all course which do not have any dep or does not depend on other
        for i in range(numCourses):
            if dep[i] == 0:
                q.append(i)
        visited = {}
        courseSequence = []
        while q:
            cur = q.popleft()
            courseSequence.append(cur)
            visited[cur] = True
            for _, n in enumerate(graph[cur]):
                dep[n] -= 1
                # no more dep, so we can pick this for processing
                if dep[n] == 0:
                    q.append(n)
        return len(courseSequence) == numCourses
