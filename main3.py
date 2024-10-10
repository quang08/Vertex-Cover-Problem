from backtrack.backtrack_optimized import VertexCoverOptimized
from backtrack.backtracking import VertexCover
import time
from tabulate import tabulate
# Vertex Cover Problem
# Given a graph, find the minimum number of vertices that can be included in a vertex cover to cover all the edges.

# Test case example:
test_cases = [
    # Test Case 1: Simple Single Edge Graph
    {
        "graph": {
            0: [1],
            1: [0]
        },
        "description": "Simple Single Edge Graph", 
        "Explanation": "There is only one edge, so including either vertex 0 or 1 will cover the edge.",
    },
    # Test Case 2: Small Triangle Graph
    {
        "graph": {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
        "description": "Small Triangle Graph",
        "Explanation": "This graph is a triangle. Any two vertices will cover all the edges.",
    },
    # Test Case 3: Disconnected Graph
    {
        "graph": {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        },
        "description": "Disconnected Graph",
        "Explanation": "The graph consists of two disconnected edges. Each edge requires one vertex to be covered.",
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
        "description": "Line Graph (Path Graph)",
        "Explanation": "This is a line graph (path). Choosing vertices 1 and 3 covers all the edges.",
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
        "description": "Star Graph",
        "Explanation": "The star graph has a central vertex (0) connected to all other vertices. Including vertex 0 in the vertex cover will cover all edges.",
    },
    # Test Case 6: Complete Graph (K4)
    {
        "graph": {
            0: [1, 2, 3],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [0, 1, 2]
        },
        "description": "Complete Graph (K4)",
        "Explanation": "A complete graph is a graph where every vertex is connected to every other vertex. To cover all edges, we need to include any three of the four vertices.",
    },
    # Test Case 7: Cyclic Graph
    {
        "graph": {
            0: [1, 4],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 0]
        },
        "description": "Cyclic Graph",
        "Explanation": "This graph is a cycle with 5 vertices. At least three vertices are needed to cover all the edges.",
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
        "description": "Tree Graph",
        "Explanation": "This is a tree. Including the root vertex (1) and one other vertex will cover all the edges.",
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
        "description": "Bipartite Graph",
        "Explanation": "This is a bipartite graph with partitions {0, 1, 2} and {3, 4}. To cover all the edges, you need to select both vertices from one partition (either {3, 4} or {0, 1, 2}).",
    },
    # Test Case 10: Graph with Isolated Vertex
    {
        "graph": {
            0: [1],
            1: [0],
            2: []
        },
        "description": "Graph with Isolated Vertex",
        "Explanation": "The graph has one edge between vertices 0 and 1, and vertex 2 is isolated. The vertex cover should focus on covering the edges, so the isolated vertex is irrelevant..",
    }
]

def run_single_test(test_case):
    graph = test_case['graph']
    description = test_case['description']
    results = []
    
    try:
        vc_optimized = VertexCoverOptimized(graph).find_vertex_cover()
    except Exception as e:
        vc_optimized = f"Error: {e}"
    
    try:
        vc_original = VertexCover(graph).find_vertex_cover()
    except Exception as e:
        vc_original = f"Error: {e}"

    results.append([description, vc_optimized, vc_original])
    
    return results

def run_all_tests(test_cases):
    all_results = []
    for test_case in test_cases:
        all_results.extend(run_single_test(test_case))
    return all_results

results = run_all_tests(test_cases)

# Print results in tabular format
table_headers = ["Test Case", "Optimized Vertex Cover", "Original Vertex Cover"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))