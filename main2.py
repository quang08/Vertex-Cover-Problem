from greedy.greedy import vertex_cover_greedy
from greedy.greedy_optimized import vertex_cover_greedy_optimized
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

test_case = {
    "graph": create_complete_bipartite_graph(100, 100),
    "description": "Complete Bipartite Graph K_{100,100}"
}

def run_single_test(test_case):
    graph = test_case['graph']
    
    results = []
    
    # Greedy Algorithm
    try:
        start_time = time.time()
        vertex_cover_greedy(graph)  # We only measure the time, not the result
        greedy_time = time.time() - start_time
    except Exception as e:
        greedy_time = "N/A"
    
    # Priority Queue Greedy Algorithm
    try:
        start_time = time.time()
        vertex_cover_greedy_optimized(graph)  # We only measure the time, not the result
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
        "Bipartite Graph K_{100,100}",  
        f"{greedy_time:.6f}s",  
        f"{pq_greedy_time:.6f}s", 
        percentage_difference_str
    ])
    
    return results

results = run_single_test(test_case)

table_headers = ["Test Case", "Greedy Time", "PQ Greedy Time", "Percentage Difference"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))