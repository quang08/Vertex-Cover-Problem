class VertexCover:
    def __init__(self, graph):
        self.graph = graph
        self.edges = self.build_edges()  # Xây dựng danh sách các cạnh
        self.V = len(graph)  # Số lượng đỉnh

    def build_edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                edge = frozenset([u, v])
                if edge not in edges:
                    edges.append(edge)
        return edges

    def is_cover(self, cover, remaining_edges):
        for edge in remaining_edges:
            if not any(vertex in edge for vertex in cover):
                return False
        return True

    def backtrack(self, current_cover, best_cover):
        # Nếu tập đỉnh hiện tại đã bao phủ hết các cạnh
        if self.is_cover(current_cover, self.edges):
            if len(current_cover) < len(best_cover[0]) or not best_cover[0]:  # Kiểm tra kích thước
                best_cover[0] = set(current_cover)  # Cập nhật tập đỉnh tốt nhất
            return

        for vertex in range(self.V):
            if vertex not in current_cover:  # Nếu đỉnh chưa có trong tập phủ
                current_cover.add(vertex)  # Thêm đỉnh vào tập phủ

                # Gọi đệ quy để tìm tập đỉnh tốt nhất
                self.backtrack(current_cover, best_cover)

                current_cover.remove(vertex)  # Loại bỏ đỉnh khi quay lui

    def find_vertex_cover(self):
        current_cover = set()
        best_cover = [set()]  # Sử dụng danh sách để lưu tập đỉnh tốt nhất
        self.backtrack(current_cover, best_cover)
        return best_cover[0]  # Trả về tập đỉnh tốt nhất
