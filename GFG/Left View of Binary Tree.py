# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/0/#

def LeftView(root):
    if not root:
        return []
    ans = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for idx in range(level_size):
            cur_node = queue.popleft()
            # take leftmost node
            if idx == 0:
                ans.append(cur_node.data)

            if cur_node.left:
                queue.append(cur_node.left)

            if cur_node.right:
                queue.append(cur_node.right)
    return ans
