# https://leetcode.com/problems/is-graph-bipartite/
# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)
  size = graph.size
  @colors = [nil] * size
  size.times do |v|
    # is not visited yet, default mark color true
    if @colors[v].nil?
      @colors[v] = true
      return false unless dfs(v, graph)
    end
  end

  true
end

def dfs(v, graph)
  graph[v].each do |neighbour|
    # is not visited, so mark opposite of parent/v
    if @colors[neighbour].nil?
      @colors[neighbour] = !@colors[v]

      # check it maintain bipartite property
      # return false if found wrong state, otherwise process remaining
      return false unless dfs(neighbour, graph)
    elsif @colors[neighbour] == @colors[v]
      return false
    end
    # return false if found wrong state, otherwise process remaining
  end

  true
end
