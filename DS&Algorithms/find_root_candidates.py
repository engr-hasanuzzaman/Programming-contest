import graphlib
from math import degrees


def root_candidates(g, n):
    degrees = [0] * n
    leaves = []
    leaves_count = 0
    for node in range(n):
        degrees[node] += len(g[node])
        if degrees[node] <= 1:
            leaves.append(node)
            leaves_count += 1
    print("---leave noded are after first iteration ", leaves)

    while leaves_count < n:
        for leave in leaves:
            new_leaves = []
            for child in g[leave]:
                degrees[child] -= 1
                if degrees[child] == 1:
                    print("--- new leave ", leave, child, degrees[child])
                    new_leaves.append(child)
            leaves_count += len(new_leaves)
            degrees[leave] = 0
            leaves = new_leaves
    print("-----the degree is ", degrees)
    return leaves

graph = [[2,1,5], [0], [3, 0], [2], [5], [4, 6, 0], [5]]
print("---expecte root candidates for graph ins ", root_candidates(graph, len(graph)))
