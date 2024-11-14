from backtrack.backtrack_optimized import VertexCoverOptimized
from backtrack.backtracking import VertexCover
from tabulate import tabulate
import time
import random

# Function to create a large complete bipartite graph
def create_random_graph(num_vertices, edge_probability):
    graph = {i: [] for i in range(num_vertices)}  # Khởi tạo các đỉnh
    
    # Tạo cạnh ngẫu nhiên giữa các đỉnh với xác suất edge_probability
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < edge_probability:
                graph[i].append(j)
                graph[j].append(i)
    
    return graph

# Danh sách các test case với đồ thị ngẫu nhiên
test_cases = [
    {
        "graph": create_random_graph(200, 0.85),
        "description": "Random Graph with 200 vertices, 85% edge probability",
    },
    {
        "graph": create_random_graph(300, 0.9),
        "description": "Random Graph with 300 vertices, 90% edge probability",
    },
    {
        "graph": create_random_graph(400, 0.8),
        "description": "Random Graph with 400 vertices, 80% edge probability",
    },
    {
        "graph": create_random_graph(1000, 0.8),
        "description": "Random Graph with 1000 vertices, 80% edge probability",
    }
]

# Function to run a single test
def run_single_test(test_case):
    graph = test_case['graph']
    description = test_case['description']
    
    results = []
    
    # backtrack Algorithm (Chỉ chạy nếu số đỉnh < 1000)
    if len(graph) < 1000:
        try:
            start_time = time.time()
            VertexCover(graph)  # We only measure the time, not the result
            backtrack_time = time.time() - start_time
        except Exception as e:
            backtrack_time = "N/A"
    else:
        backtrack_time = "Skipped"
    
    # Priority Queue backtrack Algorithm
    try:
        start_time = time.time()
        VertexCoverOptimized(graph)  # We only measure the time, not the result
        pq_backtrack_time = time.time() - start_time
    except Exception as e:
        pq_backtrack_time = "N/A"
    
    if backtrack_time != "Skipped" and backtrack_time != "N/A" and pq_backtrack_time != "N/A":
        percentage_difference = ((backtrack_time - pq_backtrack_time) / backtrack_time) * 100
        percentage_difference_str = f"{percentage_difference:.2f}%"
    else:
        percentage_difference_str = "N/A"

    # Add execution times to the results list
    results.append([
        description,  # Test case description
        f"{backtrack_time:.6f}s" if backtrack_time not in ["N/A", "Skipped"] else backtrack_time,  # backtrack time
        f"{pq_backtrack_time:.6f}s" if pq_backtrack_time != "N/A" else "N/A",  # PQ backtrack time
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
table_headers = ["Test Case", "backtrack Time", "PQ backtrack Time", "Percentage Difference"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))
