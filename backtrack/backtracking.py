class VertexCover:
    def __init__(self, graph):
        self.graph = graph
        self.edges = self.build_edges()  # Xây dựng danh sách các cạnh
        self.V = len(graph)  # Số lượng đỉnh

    def build_edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if {u, v} not in edges:  # Đảm bảo không có cạnh trùng lặp
                    edges.append({u, v})
        return edges

    def is_cover(self, cover, remaining_edges):
        # Kiểm tra xem các tập phủ đỉnh hiện có có thể phủ hết các cạnh không
        covered_edges = set()
        for vertex in cover:
            for edge in self.edges:
                if vertex in edge:
                    covered_edges.add(frozenset(edge))  # Sử dụng frozenset để so sánh tập
        return covered_edges == set(frozenset(edge) for edge in remaining_edges)

    def backtrack(self, current_cover, remaining_edges, best_cover):
        # Nếu đã kiểm tra tất cả các cạnh
        if self.is_cover(current_cover, remaining_edges):
            return min(len(current_cover), best_cover)

        for vertex in range(self.V):
            if vertex not in current_cover:  # Nếu vertex chưa có trong current_cover
                current_cover.add(vertex)  # Thêm vertex vào tập phủ
                new_remaining_edges = [edge for edge in remaining_edges if vertex not in edge]

                best_cover = self.backtrack(current_cover, new_remaining_edges, best_cover)  # Gọi đệ quy
                current_cover.remove(vertex)  # Quay lại

        return best_cover

    def find_vertex_cover(self):
        current_cover = set()
        best_cover = float('inf')
        remaining_edges = self.edges.copy()
        best_cover = self.backtrack(current_cover, remaining_edges, best_cover)
        return best_cover