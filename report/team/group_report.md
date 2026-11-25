# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom456
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

- **Phần A–B (Nguyễn Ngọc Vinh):** Dùng dữ liệu của 1.200 yêu cầu và 1.624 lượt chạy để tính chi phí mỗi việc thành công, so với mức 12.000 đ khi nhân viên tự làm và kiểm tra độ nhạy của chi phí.
- **Phần C (Phân tích lỗi):** Gắn nhãn 20 ca lỗi độc lập theo 5 loại lỗi của Google PAIR. Người 4 đã hoàn thành bộ nhãn 2 và gửi cho Người 3 để đối soát chéo, tính tỉ lệ đồng thuận và hoàn thiện bảng khắc phục.
- **Phần D (Kế hoạch pilot):** Thiết kế thử nghiệm ngẫu nhiên phân cụm theo nhân viên, tính cỡ mẫu hiệu dụng và xây dựng 3 luật dừng kiểm soát an toàn, chi phí và mức độ sử dụng.
- **Phần E (Chỉ số & Hồ sơ v0 - Nguyễn Tùng Dương):** Đặc tả chỉ số đo lường, thiết kế danh sách event có `trace_id`, đánh giá rủi ro kinh tế từ bảng độ nhạy và đóng gói hồ sơ launch v0 một trang trình hội đồng Gate 2a.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A.** Cộng chi phí token và tool của mọi lượt chạy, chi phí xem lại và làm lại. Chia cho số yêu cầu thành công, tính riêng theo loại yêu cầu và phân bổ 40 triệu đ chi phí cố định mỗi tháng cho phạm vi nội địa và hàng nặng. Chi tiết trong [bảng chi phí A–B](bang_chi_phi.md).
- **B.** Dùng lại mô hình để thay đổi các yếu tố chi phí, so sánh giới hạn 1–3 lượt và tính kịch bản xem lại 100% yêu cầu có kết quả. Chi tiết trong [bảng chi phí A–B](bang_chi_phi.md).
- **C.** Hai người gắn nhãn độc lập 20 ca lỗi, đối soát chéo đạt tỉ lệ đồng thuận 20/20 (100%), chọn 5 ca tiêu biểu cho 5 loại lỗi và xây dựng bảng khắc phục có ngưỡng đo lường và vai trò phụ trách. Chi tiết trong [bảng lỗi C](bang_loi.md).
- **D.** Tính toán cỡ mẫu D1, chọn đơn vị phân bổ là nhân viên (20 đối chứng song song), thiết lập 3 luật dừng định lượng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ. Chi tiết trong [kế hoạch pilot D](pilot_plan.yaml).
- **E.** Tính thử 3 chỉ số trên 1.200 yêu cầu, thiết lập 10 telemetry event có `trace_id` để kết nối đo lường, lượng hóa rủi ro kinh tế và đóng gói hồ sơ 1 trang. Chi tiết trong [đặc tả chỉ số E](chi_so.md) và [hồ sơ launch v0](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **A.** Ba phép thử A1 đều đạt. Chi phí bình quân là 4.472 đ/việc thành công (`simulated`). Nội địa và hàng nặng có CPS 4.599 đ sau khi cộng chi phí cố định ở mức 45.000 yêu cầu/tháng (`simulated`).
- **B.** Chi phí nhạy nhất với số ca làm lại (+51,8%, `simulated`). Giới hạn 2 lượt có chi phí cả hệ thống thấp nhất, 6.901.220 đ (`simulated`). Nếu xem lại 100% và làm lại mất 15,3 phút/ca, CPS là 12.415 đ (`simulated`).
- **C.** Đạt tỉ lệ đồng thuận đối soát chéo 20/20 (100%), thiết lập quy tắc rõ ràng cho các ca dễ lẫn; 5 ca khắc phục đều có cơ chế phát hiện tự động bằng event/ngưỡng và phân công vai trò rõ ràng.
- **D.** Cỡ mẫu yêu cầu: $n=859$ yêu cầu/nhóm (20 nhân viên/nhóm), MDE 0,06 (power 0,80), lộ trình rollout 10% → 25% → 50%, có cơ chế rollback trong 30 phút.
- **E.** Chỉ số chính đạt 82,83%, tỉ lệ bỏ qua gợi ý 27,12%, tỉ lệ mở lại trong 7 ngày là 4,25%. Đề xuất Gate 2a: **Go có điều kiện** (kèm 4 điều kiện rõ ràng về kỹ thuật và vận hành).

## 5. Khó khăn và cách xử lý

- **A4.** Bản đầu dùng tỷ lệ thành công trong phạm vi pilot để nhân với tổng khối lượng mọi loại yêu cầu. Đã đổi hệ số thành 900/1.200 và chạy lại để xác nhận bảng A4.
- **C.** Dễ nhầm lẫn giữa lỗi người dùng và lỗi hệ thống (ca 6, 9) hoặc lỗi hệ thống và lỗi ngầm (ca 8, 15). Nhóm đã bám sát nguyên tắc phân loại theo nguyên nhân gốc chứ không theo vị trí khắc phục.
- **D.** Cỡ mẫu nhân viên bị giới hạn (toàn công ty chỉ có 40 nhân viên CSKH). Nhóm đã tính toán đánh đổi chấp nhận tăng MDE từ 0,05 lên 0,06 để đảm bảo đủ power thống kê 0,80 với 20 nhân viên mỗi nhánh.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

- **Nguyễn Ngọc Vinh (2A202603877):** Phụ trách code và kiểm tra kết quả A1–A4, B1–B4. [Báo cáo cá nhân](2A202603877_NguyenNgocVinh.md).
- **Nguyễn Lâm Tùng (2A202603854):** Phụ trách kiểm số A–B, code cỡ mẫu D1 và lập kế hoạch [pilot_plan.yaml](pilot_plan.yaml). [Báo cáo cá nhân](2A202603854_NguyenLamTung.md).
- **Thành viên 3:** Phụ trách gắn nhãn độc lập bộ 1 và hoàn thiện bảng lỗi [bang_loi.md](bang_loi.md).
- **Nguyễn Tùng Dương:** Phụ trách gắn nhãn độc lập bộ 2, đặc tả chỉ số & event [chi_so.md](chi_so.md), xây dựng và hoàn thiện [hồ sơ launch v0](ho_so_launch_v0.md), tổng hợp báo cáo nhóm.

## 7. Hạn chế và hướng cải thiện

- **Thời gian xử lý là số giả lập.** Với kịch bản xem lại 100% yêu cầu có kết quả, chi phí mỗi việc thành công tăng từ 11.743 đ lên 12.415 đ (`simulated`) khi thời gian làm lại tăng từ 9 lên 15,3 phút/ca. Trong pilot, cần ghi thời gian xem lại và làm lại thực tế để tính lại chi phí.
- **Chi phí cố định mỗi việc phụ thuộc vào khối lượng.** A4 dự báo theo tỷ lệ 900/1.200 của mẫu. Khi có số liệu pilot, cần dùng số yêu cầu đủ điều kiện và số việc thành công thực tế để cập nhật dự báo theo tháng.

## 8. Tài liệu tham khảo

- Định nghĩa các cột, đơn giá giả định và công thức tính chi phí. [Dữ liệu và công thức Lab 13](../../docs/du_lieu_va_cong_thuc.md)
- Yêu cầu cho mô hình chi phí và các kịch bản độ nhạy A–B. [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- Dữ liệu giả lập dùng để tính và đối chiếu kết quả. [Nhật ký lượt chạy](../../src/logix_runs.csv) · [Danh sách yêu cầu hoàn phí](../../src/logix_requests.csv)
