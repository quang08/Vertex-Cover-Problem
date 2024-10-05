# Algorithm: Vertex Cover Greedy
## Input: Graph G
## Output: Vertex cover set

### Goal
- We want to select the vertex with the most uncovered edges at each step of the greedy algorithm for the Vertex Cover Problem.
- The degree of a vertex in this context refers to the number of uncovered edges that are incident (connected) to it.
**=> By selecting the vertex with the most uncovered edges (i.e., the maximum degree vertex among uncovered edges), we aim to cover as many edges as possible in each step.**
- Then add both directions of an edge between two vertices to the covered_edges set. This is important because the graph is undirected, meaning that an edge between vertex *u* and vertex *v* can be represented as *(u, v)* or *(v, u)*. Both representations need to be marked as “covered.”

### Pseudocode
1. Initialize an empty set `covered_edges` to store the covered edges.
2. Initialize an empty set `vertex_cover` to store the vertices in the vertex cover.

3. While there are still uncovered edges:
    a. Find the vertex `v` with the maximum number of uncovered edges:
       - For each vertex `u` in the graph:
           - Count the number of edges incident to `u` that are not in the set `covered_edges`.
           - Select the vertex with the highest count.
    
    b. Add the selected vertex `v` to the set `vertex_cover`.

    c. Mark all edges incident to `v` as covered by adding them to `covered_edges`:
       - For each neighbor `u` of `v`:
           - Add the edge (v, u) and (u, v) to `covered_edges`.

4. Return the set `vertex_cover` as the final vertex cover.

## Solution

```python
def vertex_cover_greedy(graph):
    covered_edges = set() # set of edges that are covered by the vertices in the vertex cover
    vertex_cover = set() # set of vertices that are in the vertex cover

    # while there are still uncovered edges
    while len(covered_edges) < len([(u, v) for u in graph for v in graph[u]]):

        # find the vertex with the most uncovered edges
        max_degree_vertex = max(graph, key=lambda u: len([v for v in graph[u] if (u, v) not in covered_edges and (v, u) not in covered_edges]))

        # add the vertex to the vertex cover
        vertex_cover.add(max_degree_vertex)

        # mark all edges incident to the vertex as covered
        for v in graph[max_degree_vertex]:
            covered_edges.add((max_degree_vertex, v))
            covered_edges.add((v, max_degree_vertex))

    return vertex_cover

```
