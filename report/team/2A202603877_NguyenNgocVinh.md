# Báo cáo cá nhân — Nguyễn Ngọc Vinh (2A202603877)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ngọc Vinh
- MSSV: 2A202603877
- Email: 26ai.vinhnn2@vinuni.edu.vn
- Vai trong nhóm: Người viết code phần A và B

## 2. Phần việc phụ trách

Phụ trách mô hình chi phí mỗi việc thành công (A1–A4) và phân tích độ nhạy (B1–B4).

## 3. Đóng góp cụ thể

- Hoàn thiện phần kiểm tra A1 và hàm tính chi phí trong `src/lab13.py` với hỗ trợ của ChatGPT. Mô hình cộng chi phí của mọi lượt chạy và chia cho số yêu cầu thành công.
- Tính chi phí theo bốn loại yêu cầu và phân bổ chi phí cố định cho phạm vi nội địa và hàng nặng ở hai mức khối lượng tháng.
- Chạy chín kịch bản độ nhạy, so sánh chi phí cả hệ thống theo giới hạn lượt chạy và tính mức hòa vốn khi xem lại 100% yêu cầu có kết quả.

## 4. Bằng chứng

- [Code A–B](../../src/lab13.py) và [bảng chi phí A–B](bang_chi_phi.md).
- Em chạy `python -X utf8 lab13.py` trong `src`. A1 báo `ĐẠT` cho cả ba phép thử (1,20 · 1,25 · 1,25).
- A2 ghi nhận 978 yêu cầu thành công, với CPS 4.472 đ (`simulated`). B3 cho thấy giới hạn 2 lượt có chi phí cả hệ thống thấp nhất, 6.901.220 đ (`simulated`).

## 5. Công cụ AI đã dùng

ChatGPT (Codex) để giải thích công thức, hỗ trợ viết và sửa code A–B, rồi điền bảng từ kết quả em tự chạy trong PowerShell. Em kiểm tra ba phép thử A1, chạy lại A4 sau khi sửa hệ số quy đổi khối lượng, và dùng kết quả chương trình để đối chiếu các số ghi trong bảng.

## 6. Tự đánh giá

Em phân biệt được chi phí mỗi việc thành công và chi phí cả hệ thống. Giới hạn 1 lượt có CPS thấp nhất, còn 2 lượt cho chi phí cả hệ thống thấp nhất khi tính thêm phần nhân viên xử lý thay. Qua A4, em rút kinh nghiệm kiểm tra phạm vi của tử số và mẫu số trước khi nhân với khối lượng tháng.
