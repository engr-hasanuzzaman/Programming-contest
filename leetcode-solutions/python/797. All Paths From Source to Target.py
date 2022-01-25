# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        self.bt(graph, 0, len(graph) - 1, ans, [])
        return ans

    def bt(self, graph, index, target, ans, cur_list):
        cur_list.append(index)
        if index == target:
            ans.append(cur_list[:])
    
        for i in graph[index]:
            self.bt(graph, i, target, ans, cur_list)
        cur_list.pop()

# iterative solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        # dfs with itarative way
        # [node, path_array]
        stack = [[0, [0]]]
        while stack:
            [node, path] = stack.pop()
            if node == len(graph) - 1:
                ans.append(path[:])
            for neighbor in graph[node]:
                stack.append([neighbor, path[:] + [neighbor]])
        return ans
