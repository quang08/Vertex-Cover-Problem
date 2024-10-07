def is_valid_vertex_cover(graph, vertex_cover):
    for u in graph:
        for v in graph[u]:
            if u not in vertex_cover and v not in vertex_cover:
                return False
    
    return True

def vertex_cover_backtracking(graph, k):
    def backtrack(vertex_cover, index):
        if is_valid_vertex_cover(graph, vertex_cover):
            return vertex_cover
        if len(vertex_cover) > k or index >= len(graph):
            return None
        
        vertex_cover_with = vertex_cover.copy()
        vertex_cover_with.add(list(graph.keys())[index])
        result = backtrack(vertex_cover_with, index + 1)

        if result:
            return result
        
        return backtrack(vertex_cover, index + 1)
    
    return backtrack(set(), 0)

# Test Case
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}


# K = số lượng đỉnh tối đa để thử nghiệm
k = 3
print("Vertex Cover (Backtracking):", vertex_cover_backtracking(graph, k))