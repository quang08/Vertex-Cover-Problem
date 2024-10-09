def vertex_cover_tree(graph):
    """
    Solves the vertex cover problem for a tree using dynamic programming.
    graph: adjacency list of the tree
    """
    # Memoization table to store the solution for each node: (node, include) -> result
    memo = {}

    def dp(u, parent, include):
        # If the result is already computed, return it
        if (u, include) in memo:
            return memo[(u, include)]

        # Case 1: u is included in the vertex cover
        if include:
            # The size of the vertex cover when u is included is 1 (for u itself)
            # plus the minimum cover sizes of its children, either included or excluded
            result = 1
            for v in graph[u]:
                if v != parent:  # Avoid going back to the parent
                    result += min(dp(v, u, True), dp(v, u, False))

        # Case 2: u is not included in the vertex cover
        else:
            # If u is not included, all of its children must be included in the cover
            result = 0
            for v in graph[u]:
                if v != parent:  # Avoid going back to the parent
                    result += dp(v, u, True)

        # Store the result in the memoization table
        memo[(u, include)] = result
        return result

    # The root of the tree can either be included or not in the vertex cover
    root = list(graph.keys())[0]  # Assuming the root is the first node in the adjacency list
    return min(dp(root, None, True), dp(root, None, False))