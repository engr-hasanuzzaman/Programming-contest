# Tarjan Algorithm for finding SCC (Strongly Connected Component)
- Run `DFS` with random node/vertex unless `unvisited`
- in `DFS`
    - make passing node as
        ```python
            ids[at] = weak_component[at] = node
            stack.append(at)
            on_stack[at] = true
            visited[at] = true
        ```
    - iterate all the neighbors as `to`
    - if neighbor is not visited run `DFS`
    - update weak_link[at] = min(weak_link[at], weak_link[to])
    - if `id[at] == weak_link[at]
    - remove element from stack till `at` element
- after processing each node, `weak_link` will contain parent `id` of that `SCC` group