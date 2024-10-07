def is_valid_vertex_cover(graph, vertex_cover):
    # check if all edges are covered
    # It ensures that for every edge, at least one of its endpoints is in the vertex cover.
    for u in graph:
        for v in graph[u]:
            if u not in vertex_cover and v not in vertex_cover:
                return False # If an edge is not covered, return False
    return True

# tries to find a valid vertex cover of size k or less using backtracking. 
def vertex_cover_backtracking(graph, k):
    def backtrack(vertex_cover, index):
        # At each step, it either includes or excludes the current vertex (controlled by the index).
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

# # Test Case
# graph = {
#     0: [1, 2],
#     1: [0, 3, 4],
#     2: [0, 4],
#     3: [1],
#     4: [1, 2]
# }


# # K = số lượng đỉnh tối đa để thử nghiệm
# k = 3
# print("Vertex Cover (Backtracking):", vertex_cover_backtracking(graph, k))

# #     3
# #     |
# #     1 --- 4
# #    /      |
# #   0       |
# #    \      |
# #     2 ----'

# # => Res = {1, 2}

test_cases = [
    # Test Case 1: Simple Single Edge Graph
    {
        "graph": {
            0: [1],
            1: [0]
        },
        "description": "Simple Single Edge Graph"
    },
    # Test Case 2: Small Triangle Graph
    {
        "graph": {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
        "description": "Small Triangle Graph"
    },
    # Test Case 3: Disconnected Graph
    {
        "graph": {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        },
        "description": "Disconnected Graph"
    },
    # Test Case 4: Line Graph (Path Graph)
    {
        "graph": {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3]
        },
        "description": "Line Graph (Path Graph)"
    },
    # Test Case 5: Star Graph
    {
        "graph": {
            0: [1, 2, 3, 4],
            1: [0],
            2: [0],
            3: [0],
            4: [0]
        },
        "description": "Star Graph"
    },
    # Test Case 6: Complete Graph (K4)
    {
        "graph": {
            0: [1, 2, 3],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [0, 1, 2]
        },
        "description": "Complete Graph (K4)"
    },
    # Test Case 7: Cyclic Graph
    {
        "graph": {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 0]
        },
        "description": "Cyclic Graph"
    },
    # Test Case 8: Tree Graph
    {
        "graph": {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        },
        "description": "Tree Graph"
    },
    # Test Case 9: Bipartite Graph (Complete Bipartite)
    {
        "graph": {
            0: [3, 4],
            1: [3, 4],
            2: [3, 4],
            3: [0, 1, 2],
            4: [0, 1, 2]
        },
        "description": "Bipartite Graph"
    },
    # Test Case 10: Graph with Isolated Vertex
    {
        "graph": {
            0: [1],
            1: [0],
            2: []
        },
        "description": "Graph with Isolated Vertex"
    }
]

# Assuming the greedy and backtrack functions are defined and imported

def run_tests(test_cases):
    for i, test_case in enumerate(test_cases):
        graph = test_case['graph']
        description = test_case['description']
        
        # Print the test case description
        print(f"Test Case {i+1}: {description}")
        
         # Run Backtracking Algorithm (with a reasonable k, based on the number of vertices)
        k = len(graph)  # Maximum size k can be the number of vertices in the worst case
        backtrack_result = vertex_cover_backtracking(graph, k)
        print(f"Backtracking Vertex Cover: {backtrack_result}")
        print("-" * 40)

# Run the tests
run_tests(test_cases)