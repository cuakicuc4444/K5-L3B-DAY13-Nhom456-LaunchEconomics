# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom456
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

**Phần A–B (Nguyễn Ngọc Vinh).** Dùng dữ liệu của 1.200 yêu cầu và 1.624 lượt chạy để tính chi phí mỗi việc thành công, so với mức 12.000 đ khi nhân viên tự làm và kiểm tra độ nhạy của chi phí.

...

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A.** Cộng chi phí token và tool của mọi lượt chạy, chi phí xem lại và làm lại. Chia cho số yêu cầu thành công, tính riêng theo loại yêu cầu và phân bổ 40 triệu đ chi phí cố định mỗi tháng cho phạm vi nội địa và hàng nặng.
- **B.** Dùng lại mô hình để thay đổi các yếu tố chi phí, so sánh giới hạn 1–3 lượt và tính kịch bản xem lại 100% yêu cầu có kết quả. Chi tiết trong [bảng chi phí A–B](bang_chi_phi.md).

...

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **A.** Ba phép thử A1 đều đạt. Chi phí bình quân là 4.472 đ/việc thành công (`simulated`). Nội địa và hàng nặng có CPS 4.599 đ sau khi cộng chi phí cố định ở mức 45.000 yêu cầu/tháng (`simulated`).
- **B.** Chi phí nhạy nhất với số ca làm lại (+51,8%, `simulated`). Giới hạn 2 lượt có chi phí cả hệ thống thấp nhất, 6.901.220 đ (`simulated`). Nếu xem lại 100% và làm lại mất 15,3 phút/ca, CPS là 12.415 đ (`simulated`).

...

## 5. Khó khăn và cách xử lý

**A4.** Bản đầu dùng tỷ lệ thành công trong phạm vi pilot để nhân với tổng khối lượng mọi loại yêu cầu. Đã đổi hệ số thành 900/1.200 và chạy lại để xác nhận bảng A4.

...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

- **Nguyễn Ngọc Vinh (2A202603877).** Phụ trách code và kiểm tra kết quả A1–A4, B1–B4. [Báo cáo cá nhân](2A202603877_NguyenNgocVinh.md).

## 7. Hạn chế và hướng cải thiện

- **Thời gian xử lý là số giả lập.** Với kịch bản xem lại 100% yêu cầu có kết quả, chi phí mỗi việc thành công tăng từ 11.743 đ lên 12.415 đ (`simulated`) khi thời gian làm lại tăng từ 9 lên 15,3 phút/ca. Trong pilot, cần ghi thời gian xem lại và làm lại thực tế để tính lại chi phí.
- **Chi phí cố định mỗi việc phụ thuộc vào khối lượng.** A4 dự báo theo tỷ lệ 900/1.200 của mẫu. Khi có số liệu pilot, cần dùng số yêu cầu đủ điều kiện và số việc thành công thực tế để cập nhật dự báo theo tháng.

## 8. Tài liệu tham khảo

- Định nghĩa các cột, đơn giá giả định và công thức tính chi phí. [Dữ liệu và công thức Lab 13](../../docs/du_lieu_va_cong_thuc.md)
- Yêu cầu cho mô hình chi phí và các kịch bản độ nhạy A–B. [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- Dữ liệu giả lập dùng để tính và đối chiếu kết quả. [Nhật ký lượt chạy](../../src/logix_runs.csv) · [Danh sách yêu cầu hoàn phí](../../src/logix_requests.csv)
