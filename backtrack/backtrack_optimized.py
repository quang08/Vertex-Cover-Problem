class VertexCoverOptimized:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)  # Số lượng đỉnh
        self.m = sum(len(adj) for adj in graph.values()) // 2  # Số lượng cạnh (chia đôi vì mỗi cạnh đếm 2 lần)
        self.edges = [[0] * self.n for _ in range(self.n)]  # Ma trận kề
        
        # Khởi tạo ma trận kề
        for u in graph:
            for v in graph[u]:
                self.edges[u][v] = 1  # Cạnh từ u đến v
                self.edges[v][u] = 1  # Cạnh từ v đến u

    def coverWithKVertex(self, k):
        V = self.n
        set_val = (1 << k) - 1  # Tạo tập con đầu tiên với k đỉnh
        limit = (1 << V)  # Giới hạn cho tất cả các đỉnh
        best_cover_vertices = set()  # Tập đỉnh phủ tốt nhất
        while set_val < limit:
            vis = [[False] * (self.n + 1) for _ in range(self.n + 1)]  # Đặt lại mảng vis
            cnt = 0  # Đếm số cạnh đã được bao phủ
            current_cover_vertices = set()  # Lưu các đỉnh được phủ cho tập con hiện tại

            for j in range(V):  # Duyệt qua tất cả các đỉnh
                if set_val & (1 << j):  # Nếu đỉnh j nằm trong tập hiện tại
                    current_cover_vertices.add(j)  # Thêm đỉnh vào tập hiện tại
                    for k in range(V):
                        if self.edges[j][k] and not vis[j][k]:  # Nếu có cạnh và chưa được kiểm tra
                            vis[j][k] = True  # Đánh dấu cạnh là đã được kiểm tra
                            vis[k][j] = True  # Đánh dấu ngược lại
                            cnt += 1  # Tăng số cạnh đã bao phủ

            if cnt >= self.m:  # Nếu số cạnh đã bao phủ lớn hơn hoặc bằng m
                best_cover_vertices = current_cover_vertices  # Cập nhật tập đỉnh phủ tốt nhất
                break  # Dừng tìm kiếm

            # Gosper's hack để sinh tập con tiếp theo
            c = set_val & -set_val  # Tìm phần tử đầu tiên trong set
            r = set_val + c  # Tăng set
            set_val = (((r ^ set_val) >> 2) // c) | r  # Cập nhật set
        
        return best_cover_vertices if best_cover_vertices else None  # Trả về các đỉnh phủ hoặc None

    def helper(self):
        low, high = 1, self.n
        best_cover = None  # Biến lưu trữ tập đỉnh phủ tốt nhất
        while low <= high:
            mid = (low + high) // 2  
            cover_result = self.coverWithKVertex(mid)  # Kiểm tra tập đỉnh
            if cover_result is not None:  # Nếu tìm thấy tập phủ
                best_cover = cover_result  # Cập nhật tập đỉnh phủ tốt nhất
                high = mid - 1 
            else:
                low = mid + 1 
        return best_cover  # Trả về tập đỉnh phủ tốt nhất

    def find_vertex_cover(self):
        return self.helper()

