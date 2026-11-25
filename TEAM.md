# Team

## Thông tin nhóm

- Tên nhóm: Nhom456
- Lớp: L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Ngọc Vinh | 2A202603877 | 26ai.vinhnn2@vinuni.edu.vn | cuakicuc4444 | Người viết code phần A và B |
|   2 | Nguyễn Lâm Tùng | | nlamtung.work@gmail.com | nlamtung | Người kiểm số và lập kế hoạch pilot (D) |
|   3 | Đỗ Duy Tùng | 2A202603844 | 26ai.tungdd@vinuni.edu.vn | Presceltooo | Người gắn nhãn 1 (Phân tích lỗi - C) |
|   4 | Nguyễn Tùng Dương |2A202603850 | nguyenduong342003@gmail.com | | Người gắn nhãn 2, kiêm giữ hồ sơ (E) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Nguyễn Ngọc Vinh (2A202603877)

### Phần việc phụ trách

- Phụ trách mô hình chi phí A1–A4 và phân tích độ nhạy B1–B4.

### Đóng góp cụ thể

- Hoàn thiện phần A–B trong `src/lab13.py` với hỗ trợ của ChatGPT, tự chạy chương trình và cập nhật bảng chi phí từ kết quả chạy.

### Bằng chứng

- [Code A–B](src/lab13.py), [bảng chi phí](report/team/bang_chi_phi.md) và [báo cáo cá nhân](report/team/2A202603877_NguyenNgocVinh.md). Ba phép thử A1 đều đạt (1,20 · 1,25 · 1,25).

## Đỗ Duy Tùng (2A202603844)

### Phần việc phụ trách

- Phụ trách gắn nhãn độc lập bộ 1, đối soát chéo bảng lỗi (nhiệm vụ C) và phụ trách phiếu chấm duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, đối chiếu với Người 4 đạt đồng thuận 20/20 (100%).
- Hoàn thiện bảng khắc phục 5 ca mẫu có event và ngưỡng phát hiện đo được cùng vai trò phụ trách.

### Bằng chứng

- [Bảng lỗi](report/team/bang_loi.md) và [báo cáo cá nhân](report/team/2A202603844_DoDuyTung.md).

## Nguyễn Tùng Dương

### Phần việc phụ trách

- Phụ trách gắn nhãn độc lập bộ 2 (nhiệm vụ C), đặc tả chỉ số & event (E1), phân tích rủi ro kinh tế (E2), hoàn thiện hồ sơ launch v0 Gate 2a (E3) và tổng hợp báo cáo nhóm.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi đạt tỉ lệ đồng thuận 100%, xây dựng danh sách 10 event telemetry có `trace_id` để kết nối đo lường.
- Tính toán và đặc tả các chỉ số chính, chỉ số sử dụng và chỉ số an toàn trên 1.200 yêu cầu.
- Lập bảng rủi ro kinh tế từ các kịch bản độ nhạy, đóng gói hồ sơ launch v0 một trang đầy đủ 7 mục và đề xuất Go có điều kiện trình Gate 2a.

### Bằng chứng

- [Bảng lỗi](report/team/bang_loi.md), [đặc tả chỉ số](report/team/chi_so.md), [hồ sơ launch v0](report/team/ho_so_launch_v0.md) và [báo cáo nhóm](report/team/group_report.md).
