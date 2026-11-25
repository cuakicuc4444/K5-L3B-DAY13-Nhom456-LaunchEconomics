# Báo cáo cá nhân — Nguyễn Lâm Tùng (2A202603854)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Lâm Tùng
- MSSV: 2A202603854
- Email: 26ai.tungnl2@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số và lập kế hoạch pilot (D)

## 2. Phần việc phụ trách

Phụ trách kiểm số đối chiếu phần mô hình chi phí và độ nhạy (A–B), viết code tính cỡ mẫu (D1) trong `src/lab13.py`, và hoàn thiện kế hoạch pilot `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Đối chiếu số liệu và tính tay kiểm chứng phần A4 (tỷ lệ thành công thuộc phạm vi pilot `900/1.200 = 75%`, chi phí cố định mỗi việc `1.185 đ` ở 45.000 yêu cầu/tháng và `2.370 đ` ở 22.500 yêu cầu/tháng), hợp nhất và hoàn thiện `report/team/bang_chi_phi.md` với đầy đủ nhãn `simulated`.
- Viết hàm `co_mau` và `nhiem_vu_d` trong `src/lab13.py` để tính toán 5 câu D1 (theo yêu cầu, theo nhân viên `m = 75`, giới hạn 20 nhân viên/nhóm, giới hạn 6 depot/nhóm, và MDE 6 điểm) cùng tỉ lệ `mo_lai_trong_7_ngay` hiện tại từ `src/logix_requests.csv`.
- Thiết kế và hoàn thiện `report/team/pilot_plan.yaml`: chốt phạm vi `noi_dia` + `hang_nang`, chọn cách chia theo nhân viên (20 đối chứng + 20 can thiệp), ghi rõ đánh đổi MDE 6 điểm (`n = 859`/nhóm, `m >= 299`, `DE = 6,96`, power ở 5 điểm giảm còn `0,64`), trả lời 5 câu kiểm tra D2, xây dựng 3 luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ và liệt kê `simulated_inputs`.

## 4. Bằng chứng

- [Code D1](../../src/lab13.py), [bảng chi phí A–B](bang_chi_phi.md) và [kế hoạch pilot](pilot_plan.yaml).
- Kết quả chạy `python lab13.py` trong `src/`:
  - D1a) Chia theo yêu cầu (MDE 5 điểm): `1.251` yêu cầu/nhóm; D1b) theo nhân viên `m = 75`: `DE = 2,48`, cần `3.103`/nhóm (`42` người/nhóm, tổng `84 > 40`); D1c) 20 nhân viên/nhóm: tối đa `1.000 < 1.251`; D1d) 6 depot/nhóm: tối đa `300 < 1.251`; D1e) MDE 6 điểm (`859`/nhóm): `m >= 299`, `DE = 6,96`, power tại 5 điểm = `0,64`.
  - Tỉ lệ `mo_lai_trong_7_ngay`: toàn bộ `4,25%` (`51/1.200`), phạm vi `noi_dia + hang_nang` là `3,97%` (`39/982`).
- Kiểm tra `yaml.safe_load` đọc `report/team/pilot_plan.yaml` hợp lệ, `0` dấu `?` ngoài dòng chú thích.

## 5. Công cụ AI đã dùng

Dùng trợ lý AI (Antigravity / Gemini) để hỗ trợ viết hàm `co_mau` và `nhiem_vu_d` trong `src/lab13.py`, chuẩn hóa cấu trúc YAML và rà soát công thức cỡ mẫu. Tự kiểm tra bằng cách tính tay đối chiếu A4 và D1e, chạy trực tiếp `python lab13.py` trên dữ liệu CSV và chạy `yaml.safe_load` kiểm tra cú pháp `pilot_plan.yaml`.

## 6. Tự đánh giá

Hiểu rõ sự khác biệt giữa cỡ mẫu lý thuyết và cỡ mẫu hiệu dụng khi chia theo cụm (`DE = 1 + (m - 1) × ICC`, giới hạn `c / ICC`), cũng như lý do phải dựa vào tỉ lệ mở lại thực tế (`4,25%`) và kết quả độ nhạy (`hang_nang` `8.221 đ`, giới hạn 2 lần chạy `6.901.220 đ`) trước khi đặt ngưỡng luật dừng để pilot không bị dừng oan ngay tuần đầu.
