from collections import deque
class Solution:
    def largestValues(self, root):
        #code here
        return self.bfs(root)
    def bfs(self, root):
        q = deque([root])
        max_values = []
        while q:
            size = len(q)
            max_val = float('-inf')
            for i in range(size):
                cur = q.popleft()
                max_val = max(max_val, cur.data)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
            max_values.append(max_val)
        return max_values
