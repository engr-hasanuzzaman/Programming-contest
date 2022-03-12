# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
# class Node
#     attr_accessor :val, :neighbors
#     def initialize(val = 0, neighbors = nil)
#		  @val = val
#		  neighbors = [] if neighbors.nil?
#         @neighbors = neighbors
#     end
# end

# @param {Node} node
# @return {Node}
def cloneGraph(node)
    return node if node.nil?
    
    visited = {}
    stack = [node]
    container = {}
    visited[node.val] = true

    until stack.empty?
        cur = stack.pop
        unless container.key?(cur.val)
            container[cur.val] = Node.new(cur.val)
        end
        
        new_node = container[cur.val]
        
        cur.neighbors.each do |node|
            unless container.key?(node.val)
                container[node.val] = Node.new(node.val)
            end
            new_neighbor = container[node.val]
            new_neighbor.neighbors << new_node
            
            next if visited.key?(node.val)
            visited[node.val] = true
            stack << node
        end
    end

    container[node.val]
end
