'''
Single source sortest path algorithm which work with negetive weight also (Dijkstra algorithm work only with positive weight)
It follows Dynamic Programming where we try out all the possible solutions and pick the best one.

If number of Vertix is N, do relaxsation N-1 time
Relaxasion: update the cost of U -> V if d[V] > d[U] + cost(U,V)
'''


class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        dist = [100000000 for _ in range(V)]
        dist[S] = 0
        for _ in range(V-1):
            for u, v, w in adj:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return dist

"""
function BellmanFord(list vertices, list edges, vertex source) is

    // This implementation takes in a graph, represented as
    // lists of vertices (represented as integers [0..n-1]) and edges,
    // and fills two arrays (distance and predecessor) holding
    // the shortest path from the source to each vertex

    distance := list of size n
    predecessor := list of size n

    // Step 1: initialize graph
    for each vertex v in vertices do

        distance[v] := inf             // Initialize the distance to all vertices to infinity
        predecessor[v] := null         // And having a null predecessor
    
    distance[source] := 0              // The distance from the source to itself is, of course, zero

    // Step 2: relax edges repeatedly
    
    repeat |V|−1 times:
         for each edge (u, v) with weight w in edges do
             if distance[u] + w < distance[v] then
                 distance[v] := distance[u] + w
                 predecessor[v] := u

    // Step 3: check for negative-weight cycles
    for each edge (u, v) with weight w in edges do
        if distance[u] + w < distance[v] then
            // Step 4: find a negative-weight cycle
            negativeloop := [v, u]
            repeat |V|−1 times:
                u := negativeloop[0]
                for each edge (u, v) with weight w in edges do
                    if distance[u] + w < distance[v] then
                        negativeloop := concatenate([v], negativeloop)
            find a cycle in negativeloop, let it be ncycle
            // use any cycle detection algorithm here
            error "Graph contains a negative-weight cycle", ncycle

    return distance, predecessor
"""
