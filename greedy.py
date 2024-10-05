def vertex_cover_greedy(graph):
    covered_edges = set() # set of edges that are covered by the vertices in the vertex cover
    vertex_cover = set() # set of vertices that are in the vertex cover

    # while there are still uncovered edges
    while len(covered_edges) < len([(u, v) for u in graph for v in graph[u]]):

        # find the vertex with the most uncovered edges
        # checks each neighbor  v  of vertex  u  to see if the edge  (u, v)  or  (v, u)  is not in the covered_edges set (meaning the edge hasn’t been covered yet).
        max_degree_vertex = max(graph, key=lambda u: len([v for v in graph[u] if (u, v) not in covered_edges and (v, u) not in covered_edges]))

        # add the vertex to the vertex cover
        vertex_cover.add(max_degree_vertex)

        # mark all edges incident to the vertex as covered
        for v in graph[max_degree_vertex]:
            covered_edges.add((max_degree_vertex, v))
            covered_edges.add((v, max_degree_vertex))

    return vertex_cover


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

#     3
#     |
#     1 --- 4
#    /      |
#   0       |
#    \      |
#     2 ----'

# => Res = {1, 2}

print("Vertex Cover (Greedy):", vertex_cover_greedy(graph))