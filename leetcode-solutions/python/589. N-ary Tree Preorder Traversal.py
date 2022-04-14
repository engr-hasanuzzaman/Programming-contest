# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return ans
