from greedy.greedy import vertex_cover_greedy
from greedy.greedy_optimized import vertex_cover_greedy_optimized
from backtrack.backtrack_optimized import vertex_cover_tree
from backtrack.backtracking import vertex_cover_backtracking
from tabulate import tabulate
import time

# Centralized test cases
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
            0: [1],
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
        "Explanation": "The graph has one edge between vertices 0 and 1, and vertex 2 is isolated. The vertex cover should focus on covering the edges, so the isolated vertex is irrelevant.",
    }
]

# Helper function to convert graph (adjacency list) to edge list
# def convert_to_edge_list(graph):
#     """Convert an adjacency list to an edge list."""
#     edge_list = []
#     for u in graph:
#         for v in graph[u]:
#             if (u, v) not in edge_list and (v, u) not in edge_list:  # Avoid duplicates
#                 edge_list.append((u, v))
#     return edge_list

def convert_to_edge_list(graph):
    """Convert an adjacency list to an edge list."""
    edge_list = []
    for u in graph:
        for v in graph[u]:
            if (u, v) not in edge_list and (v, u) not in edge_list:  # Avoid duplicates
                edge_list.append((u, v))
    return edge_list

def run_all_tests(test_cases):
    results = []
    
    for i, test_case in enumerate(test_cases):
        graph = test_case['graph']
        description = test_case['description']
        edge_list = convert_to_edge_list(graph)  # Convert to edge list for dynamic solution
        n = len(graph)
        
        # Collect results and execution time for each algorithm
        try:
            start_time = time.time()
            greedy_result = vertex_cover_greedy(graph)
            greedy_time = time.time() - start_time
        except Exception as e:
            greedy_result = f"Error: {e}"
            greedy_time = "N/A"
        
        try:
            start_time = time.time()
            pq_greedy_res = vertex_cover_greedy_optimized(graph)
            pq_greedy_time = time.time() - start_time
        except Exception as e:
            pq_greedy_res = f"Error: {e}"
            pq_greedy_time = "N/A"

        # # Backtracking Algorithm
        # try:
        #     start_time = time.time()
        #     backtrack_result = vertex_cover_backtracking(graph, n)  # Try for size n or less
        #     backtrack_time = time.time() - start_time
        # except Exception as e:
        #     backtrack_result = f"Error: {e}"
        #     backtrack_time = "N/A"
         
        # Append results and times to the list for the table
        results.append([
            description, 
            greedy_result, f"{greedy_time:.6f}s" if isinstance(greedy_time, float) else greedy_time,
            pq_greedy_res, f"{pq_greedy_time:.6f}s" if isinstance(pq_greedy_time, float) else pq_greedy_time,
            # backtrack_result, f"{backtrack_time:.6f}s" if isinstance(backtrack_time, float) else backtrack_time,
        ])
    
    return results

# Run all test cases and collect the results
results = run_all_tests(test_cases)

# Print the results as a table using tabulate
table_headers = ["Test Case", "Greedy", "Greedy Time", "PQ Greedy", "PQ Greedy Time"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))