## Topological sorting
```py
visited = [False] * N
# we will keep processed node in reverse order
ordering = [0] * N
i = N - 1 # for ordering
for vertex in range(V):
    if visited[vertex] == False:
        dfs(vertex, graph, visited, i, ordering)
return ordering

def dfs(at, graph, visited, i, ordering):
    visited[at] = True

    for neighbor in graph[at]:
        if not visited[neighbor]:
            i = self.dfs(neighbor, graph, visited, i, ordering)
    
    ordering[i] = at
    return i - 1
```