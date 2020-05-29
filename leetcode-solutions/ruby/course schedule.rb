# Cycle detection in directed graph

def can_finish(num_courses, prerequisites)
  graph = Array.new(num_courses) { Array.new }
  prerequisites.each do |m, n|
      graph[m] << n
  end
  visited = []
  visiting = {}
  num_courses.times do |n|
      next if visited[n]
      visiting[n] = true
      return false unless dfs(visited, visiting, graph, n)
  end
  
  true
end

def dfs(visited, visiting, graph, node)
  graph[node].each do |c|
      return false if visiting[c]
      visiting[c] = true
      return false unless dfs(visited, visiting, graph, c)
  end
  
  visiting.delete(node)
  visited[node] = true
  true
end

input = [[1,0],[0,1]]
puts can_finish(2, input)
