# Báo cáo cá nhân — Nguyễn Tùng Dương (2A202603850)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tùng Dương
- MSSV: 2A202603850
- Email: nguyenduong342003@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (nhiệm vụ C và E)

## 2. Phần việc phụ trách

Phụ trách gắn nhãn độc lập bộ 2 ở nhiệm vụ C để đối soát chéo với Người 3, đặc tả chỉ số và danh sách event telemetry (E1), phân tích rủi ro kinh tế (E2), xây dựng và hoàn thiện hồ sơ launch v0 một trang trình Gate 2a (E3), cùng tổng hợp báo cáo nhóm.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (Phân tích lỗi):** Tự gắn nhãn độc lập 20 ca lỗi theo 5 nhóm của Google PAIR (`Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`) trong 8 phút; đối soát chéo với Người 3 đạt tỉ lệ đồng thuận tuyệt đối 20/20 (100%), chốt quy tắc cho các ca dễ lẫn và 5 ca khắc phục mẫu có vai trò phụ trách.
- **Nhiệm vụ E1 (Chỉ số và Event):**
  - Tính thử 3 chỉ số từ 1.200 yêu cầu: Chỉ số chính đạt **82,83%** (994/1.200 yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày); Tỉ lệ bỏ qua gợi ý đạt **27,12%** (48/177 yêu cầu được xem lại); Tỉ lệ lỗi lọt đến khách là **4,25%** (51/1.200 yêu cầu mở lại trong 7 ngày).
  - Đề xuất 2 chỉ số mới: `% yêu cầu nhóm can thiệp được mở bằng trợ lý` (chỉ số dùng) và `% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần` (chỉ số an toàn).
  - Thiết kế danh sách 10 telemetry event có `trace_id` để kết nối trace agent với luồng nghiệp vụ, lập bảng kiểm tra chéo đảm bảo 100% chỉ số đều có event để đo.
- **Nhiệm vụ E2 (Rủi ro kinh tế):** Lượng hóa 3 rủi ro từ bảng độ nhạy B: ca làm lại gấp đôi đẩy CPS tăng +51,8% lên 6.787 đ (`simulated`); xem lại 100% chạm trần hòa vốn 11.743 đ – 12.415 đ (`simulated`) so với mức 12.000 đ nhân viên tự làm; sụt giảm khối lượng làm tăng chi phí cố định phân bổ.
- **Nhiệm vụ E3 (Hồ sơ launch v0):** Đóng gói toàn bộ kết quả vào `report/team/ho_so_launch_v0.md` đúng 1 trang, 7 mục, gắn nhãn `simulated` đầy đủ cho các số giả định, không dùng từ cấm, đưa ra đề xuất **Go có điều kiện** kèm 4 điều kiện kiểm soát rủi ro rõ vai trò phụ trách và ngày kiểm tra.
- **Báo cáo nhóm:** Tổng hợp và hoàn thiện `report/team/group_report.md` tóm tắt toàn bộ giải pháp từ A đến E.

## 4. Bằng chứng

- Hồ sơ launch v0: [ho_so_launch_v0.md](ho_so_launch_v0.md) (1 trang, 7 mục đủ trạng thái và người phụ trách).
- Đặc tả chỉ số và rủi ro: [chi_so.md](chi_so.md).
- Bảng lỗi đối soát chéo: [bang_loi.md](bang_loi.md) (đồng thuận 20/20 = 100%).
- Báo cáo nhóm: [group_report.md](group_report.md).
- Phân công thành viên: [TEAM.md](../../TEAM.md).
- Các con số đã đối soát: CPS 4.472 đ (`simulated`), 978 việc thành công, chỉ số chính 82,83%, 3 luật dừng định lượng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ.

## 5. Công cụ AI đã dùng

Sử dụng trợ lý AI (Antigravity / Gemini) để hỗ trợ rà soát công thức tính chỉ số E1, định dạng bảng markdown đúng rubric Gate 2a, kiểm tra chặt chẽ việc gắn nhãn `simulated` và soát từ khóa cấm theo quy tắc 5 của lab. Tự kiểm tra bằng cách đối chiếu chéo số liệu giữa `bang_chi_phi.md`, `pilot_plan.yaml`, `bang_loi.md` và kiểm tra logic 4 điều kiện ràng buộc trong đề xuất Go có điều kiện.

## 6. Tự đánh giá

Hiểu sâu sắc vai trò của người giữ hồ sơ: kết nối các kết quả kỹ thuật và kinh tế thành một bức tranh quản trị nhất quán. Nhận thức rõ ràng Gate 2a chỉ duyệt kế hoạch pilot nhằm thu thập dữ liệu thực nghiệm có đối chứng, chứ chưa cho phép triển khai diện rộng; đồng thời nhận diện được "bẫy chi phí token" khi 92,46% chi phí thực tế nằm ở thời gian con người xem lại (40,69%) và làm lại (51,77%).
