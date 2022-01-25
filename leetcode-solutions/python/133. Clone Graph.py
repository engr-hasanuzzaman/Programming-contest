# https://leetcode.com/problems/clone-graph/

# by calling DFS two times
# first create all the nodes
# then push the neighbors
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        node_container = {}
        stack = [node]
        visited = {}
        visited[node.val] = True
        # create all the nodes and contain on the node_container
        while stack:
            cur_node = stack.pop()
            node_container[cur_node.val] = Node(cur_node.val)
            for neighbor in cur_node.neighbors:
                if neighbor.val in visited:
                    continue
                visited[neighbor.val] = True
                stack.append(neighbor)
        
        # assign all the neighbors
        stack = [node]
        visited = {}
        visited[node.val] = True
        while stack:
            cur_node = stack.pop()
            visited[cur_node.val] = True
            
            for neighbor in cur_node.neighbors:
                node_container[cur_node.val].neighbors.append(node_container[neighbor.val])
                if neighbor.val in visited:
                    continue
                stack.append(neighbor)
                visited[neighbor.val] = True
        return node_container[node.val]