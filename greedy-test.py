def vertex_cover_greedy(graph):
    covered_edges = set()
    vertex_cover = set()

    while len(covered_edges) < len([(u,v) for u in graph for v in graph[u]]):

        # find the vertex with the most uncovered edges
        # check each neighbor v of vertex u to see if the edge (u, v) or (v, u) is not in covered_edges (meaning it's not covered)
        max_degree_vertex = max(graph, key=lambda u: len([v for v in graph[u] if (u, v) not in covered_edges and (v, u) not in covered_edges]))

        vertex_cover.add(max_degree_vertex)

        # add both directions of the edges incident to the max vertex
        # mark them as covered
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

print("Vertex Cover (greedy): ", vertex_cover_greedy(graph))