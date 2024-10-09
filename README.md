# Hướng dẫn cài đặt môi trường

## Clone repo về máy
`git clone https://github.com/quang08/Vertex-Cover-Problem.git`

## Cài các thư viện liên quan
`pip install -r requirements.txt`

- có thể chạy virtual enviroment nếu muốn: `python -m venv venv && source venv/bin/activate`

## Đọc tìm hiểu code

- `main.py`: Đây là file tổng, là nơi đang được sử dụng để gọi hàm greedy (và backtrack) để so sánh hiệu năng, hoặc đơn giản chỉ là show kết quả của 2 thuật toán
- `backtrack/backtracking.py`: Đây là file cho hàm backtracking chưa cải tiến
- `backtrack/backtrack_optimized.py`: Đây là file cho hàm backtracking đã cải tiến

## Nhiệm vụ
- Vì cần demo trước lớp, nên việc code thuật toán, có test case ví dụ (từ test case to đến nhỏ) đều quan trọng
- Vậy nên, cần ứng dụng thuật toán backtrack và backtrack đã cải tiến, đưa ra những test case để so sánh cải tiến và không cải tiến với nhau
- Tạo một file tổng riêng cho backtrack (`main3.py` chẳng hạn), để gọi 2 hàm backtrack cải tiến và chưa cải tiến