# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom456 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ (`simulated`), gấp 16,28 lần hóa đơn token và tool chia cho số yêu cầu (274,65 đ) | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | noi_dia: 2.696 đ (0,22×), hang_nang: 8.221 đ (0,69×); cộng chi phí cố định 40tr/tháng đạt 0,38× - 0,48× so với 12.000 đ; quoc_te: 1,88× bị loại khỏi pilot | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đóng trong 24h & không mở lại 7 ngày: 82,83% (chính) · Tỉ lệ bỏ qua gợi ý: 27,12% (dùng) · Mở lại trong 7 ngày: 4,25% (an toàn) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 20/20 (100%), đủ 5 loại lỗi Google PAIR đều có cách phát hiện đo được bằng event/ngưỡng và phân công vai trò chịu trách nhiệm | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | 20 nhân viên đối chứng và 20 nhân viên can thiệp song song; MDE 0,06 (power 0,80, n=859/nhóm); rollout 10% → 25% → 50%; 3 luật dừng rõ ngưỡng và người dừng | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Số ca làm lại gấp đôi tăng CPS +51,8% lên 6.787 đ (`simulated`); Xem lại 100% chạm trần hòa vốn 11.743 đ - 12.415 đ (0,98× - 1,03× so với 12.000 đ) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1:** Sửa khóa chống trùng idempotency và cơ chế đối soát sổ cái (xử lý triệt để ca lỗi 7, ca 20) trước ngày bắt đầu pilot. Người phụ trách: Kỹ sư trưởng agent. Ngày kiểm tra: 2026-12-01.
- **Điều kiện 2:** Giám đốc vận hành ký phê duyệt văn bản đánh đổi chấp nhận MDE 6 điểm (power giảm còn ~0,64 nếu hiệu ứng thực tế là 5 điểm) với 20 nhân viên mỗi nhóm. Người phụ trách: Giám đốc vận hành. Ngày kiểm tra: 2026-12-01.
- **Điều kiện 3:** Kích hoạt đầy đủ 10 event có `trace_id` trong hệ thống telemetry; thay thế số phút giả lập bằng phút đo thực tế ngay sau tuần 1 rollout. Người phụ trách: Kỹ sư trưởng agent. Ngày kiểm tra: 2026-12-08.
- **Điều kiện 4:** Thiết lập quy trình giảm tỷ lệ xem lại theo bậc (khi tỷ lệ sửa + bỏ của nhân viên duy trì dưới 15%), tránh rủi ro xem lại 100% làm mất hoàn toàn lợi thế kinh tế. Người phụ trách: Trưởng nhóm CSKH. Ngày kiểm tra: 2026-12-15.
