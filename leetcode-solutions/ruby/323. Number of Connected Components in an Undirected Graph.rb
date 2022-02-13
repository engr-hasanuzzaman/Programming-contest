# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_components(n, edges)
    graph = Hash.new{|h,k| h[k] = []}
    edges.each do |a, b|
        graph[a].push(b)
        graph[b].push(a)
    end
    
    visited = {}
    count = 0
    n.times do |node|
        next if visited[node]
        count += 1
        stack = [node]
        visited[node] = true
        until stack.empty?
            cur_node = stack.pop
            for neighbor in graph[cur_node]
                unless visited[neighbor]
                    stack.push(neighbor) 
                    visited[neighbor] = true
                end
            end
        end
    end
    count
end
