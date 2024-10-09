import heapq

# •	Problem: Each time, you are finding the vertex with the maximum number of uncovered edges by scanning all vertices. This takes O(n) time for each iteration.
# max_degree_vertex = max(graph, key=lambda u: len([v for v in graph[u] if (u, v) not in covered_edges and (v, u) not in covered_edges]))
# •	Optimization: Use a max-heap (priority queue) to efficiently retrieve the vertex with the maximum number of uncovered edges. This way, you can reduce the time complexity of finding the max-degree vertex to O(log n).

def vertex_cover_greedy_optimized(graph):
    covered_edges = set()
    vertex_cover = set()

    # Create a max-heap that stores all the vertices based on their degree with negative degrees (because heapq is a min-heap by default) to still use max heap
    heap = [(-len(graph[u]), u) for u in graph]
    heapq.heapify(heap)
    
    while len(covered_edges) < len([(u, v) for u in graph for v in graph[u]]):
        # Get the vertex with the most uncovered edges
        while heap:
            max_degree, max_degree_vertex = heapq.heappop(heap)
            max_degree = -max_degree  # Convert back to positive degree
            
            # Recalculate the degree to ensure it is still valid after some edges are covered:
            # When you select a vertex from the heap (which stores vertices based on the number of uncovered edges they have), some of its edges may have already been covered by previous vertex selections. Therefore, the number of uncovered edges (its “degree”) might be lower now. So, before using that vertex, the code checks its current number of uncovered edges and compares it with the number that was originally stored in the heap. If the numbers don’t match, it recalculates and updates the heap with the new degree.
            uncovered_edges = len([v for v in graph[max_degree_vertex] if (max_degree_vertex, v) not in covered_edges and (v, max_degree_vertex) not in covered_edges])
            
            # If the recalculated number of uncovered edges is equal to the original, the vertex is still valid, and you can proceed to add it to the vertex cover.
            if uncovered_edges == max_degree:
                break  # This is the correct vertex to choose
            else: # vertex is pushed back into the heap with its new degree:
                # Push the recalculated degree back into the heap
                heapq.heappush(heap, (-uncovered_edges, max_degree_vertex))

        # Add the vertex to the vertex cover
        vertex_cover.add(max_degree_vertex)

        # Mark all edges incident to the vertex as covered
        for v in graph[max_degree_vertex]:
            covered_edges.add((max_degree_vertex, v))
            covered_edges.add((v, max_degree_vertex))

    return vertex_cover