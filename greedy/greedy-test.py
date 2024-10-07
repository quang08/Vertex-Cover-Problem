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
        
        # Run Greedy Algorithm
        greedy_result = vertex_cover_greedy(graph)
        print(f"Greedy Vertex Cover: {greedy_result}")
        
        print("-" * 40)

# Run the tests
run_tests(test_cases)