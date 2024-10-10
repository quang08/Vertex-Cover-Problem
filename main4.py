from backtrack.backtrack_optimized import VertexCoverOptimized
from backtrack.backtracking import VertexCover
from tabulate import tabulate
import time

# Function to create a large complete bipartite graph
def create_complete_bipartite_graph(m, n):
    graph = {}
    
    for u in range(m):  # Set A
        graph[u] = [v for v in range(m, m + n)]  # Connect every vertex in A to every vertex in B
    
    for v in range(m, m + n):  # Set B
        graph[v] = [u for u in range(m)]  # Connect every vertex in B to every vertex in A
    
    return graph

# List of test cases with different bipartite graphs
test_cases = [
    {
        "graph": create_complete_bipartite_graph(100, 100),
        "description": "Bipartite Graph K_{100,100}",
    },
    {
        "graph": create_complete_bipartite_graph(200, 200),
        "description": "Bipartite Graph K_{200,200}",
    },
    {
        "graph": create_complete_bipartite_graph(300, 300),
        "description": "Bipartite Graph K_{300,300}",
    }
]

# Function to run a single test
def run_single_test(test_case):
    graph = test_case['graph']
    description = test_case['description']
    
    results = []
    
    # Greedy Algorithm
    try:
        start_time = time.time()
        VertexCover(graph)  # We only measure the time, not the result
        greedy_time = time.time() - start_time
    except Exception as e:
        greedy_time = "N/A"
    
    # Priority Queue Greedy Algorithm
    try:
        start_time = time.time()
        VertexCoverOptimized(graph)  # We only measure the time, not the result
        pq_greedy_time = time.time() - start_time
    except Exception as e:
        pq_greedy_time = "N/A"
    
    if greedy_time != "N/A" and pq_greedy_time != "N/A":
        percentage_difference = ((greedy_time - pq_greedy_time) / greedy_time) * 100
        percentage_difference_str = f"{percentage_difference:.2f}%"
    else:
        percentage_difference_str = "N/A"

    # Add execution times to the results list
    results.append([
        description,  # Test case description
        f"{greedy_time:.6f}s" if greedy_time != "N/A" else "N/A",  # Greedy time
        f"{pq_greedy_time:.6f}s" if pq_greedy_time != "N/A" else "N/A",  # PQ Greedy time
        percentage_difference_str  # Percentage difference
    ])
    
    return results

# Function to run all test cases and collect results
def run_all_tests(test_cases):
    all_results = []
    for test_case in test_cases:
        all_results.extend(run_single_test(test_case))
    return all_results

# Run all tests and collect results
results = run_all_tests(test_cases)

# Print the results as a table
table_headers = ["Test Case", "Backtrack", "Optimized Backtrack", "Percentage Difference"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))