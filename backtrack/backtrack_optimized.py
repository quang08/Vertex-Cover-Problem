# The Dynamic Ordering of Vertices approach enhances the backtracking algorithm by dynamically selecting vertices in a more efficient order during recursion. The idea is to pick vertices that have the highest potential for covering edges early in the process, which can help prune the search space faster.

# •	Dynamic Ordering: At each recursive call, the algorithm dynamically chooses the vertex with the highest degree (i.e., the vertex that is connected to the most other vertices). This vertex is more likely to help cover many edges quickly, potentially reducing the search space.
# •	Two Branches: The algorithm still explores two branches for each vertex:
# •	One branch includes the chosen vertex in the cover.
# •	The other branch excludes the vertex.
# •	Recursion with Reduced Search Space: Each recursive call reduces the set of remaining vertices by removing the chosen vertex. This continues until a valid vertex cover is found or the recursion terminates.

def vertex_cover_dynamic_ordering(graph, k):
    def is_valid_vertex_cover(graph, vertex_cover):
        for u in graph:
            for v in graph[u]:
                if u not in vertex_cover and v not in vertex_cover:
                    return False
        return True

    def dynamic_backtrack(vertex_cover, remaining_vertices):
        # Base cases
        if is_valid_vertex_cover(graph, vertex_cover):
            return vertex_cover
        if len(vertex_cover) > k:
            return None

        if not remaining_vertices:
            return None
        
        # Choose the vertex with the highest degree from the remaining vertices
        max_degree_vertex = max(remaining_vertices, key=lambda u: len(graph[u]))
        
        # Copy remaining vertices and remove the chosen one
        remaining_vertices_without_max = remaining_vertices.copy()
        remaining_vertices_without_max.remove(max_degree_vertex)

        # Explore the branch where we include the max_degree_vertex
        vertex_cover_with = vertex_cover.copy()
        vertex_cover_with.add(max_degree_vertex)
        result = dynamic_backtrack(vertex_cover_with, remaining_vertices_without_max)

        if result:
            return result
        
        # Explore the branch where we do not include the max_degree_vertex
        return dynamic_backtrack(vertex_cover, remaining_vertices_without_max)

    return dynamic_backtrack(set(), set(graph.keys()))