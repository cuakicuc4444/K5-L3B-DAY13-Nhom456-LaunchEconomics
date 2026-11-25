# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số yêu cầu nhân viên mở trợ lý ÷ tổng yêu cầu thuộc nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn phát hiện hoàn sai tiền ÷ số đơn được kiểm tra mẫu | Không cần tính |

*Ghi chú: Chỉ số trong đợt chạy thử là 82,83% (chính), 27,12% (dùng) và 4,25% (an toàn); không viết "trợ lý đã nâng chỉ số" do đợt chạy thử chưa có nhóm đối chứng.*

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện NV | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý của trợ lý hiện trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | quyet_dinh (giu/sua/bo), phut_xem_lai_that, trace_id | Khi nhân viên bấm duyệt, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | phut_lam_lai_that, ly_do, trace_id | Khi nhân viên hoàn thành xử lý lại ca bị lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi hệ thống thực hiện lệnh chuyển tiền hoàn phí |
| `handoff_to_staff` | Agent | reason, tom_tat_ngu_canh, trace_id | Khi agent chuyển ca sang cho nhân viên giải quyết |
| `ticket_closed` | Hệ thống ticket | closed_at, dong_trong_24h, trace_id | Khi ticket được hoàn tất và đóng lại |
| `ticket_reopened` | Khách | reopened_at, ly_do, trace_id | Khi khách hàng mở lại ticket trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán / QA | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần khi kiểm tra mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng 24h và không mở lại 7 ngày):** Tính từ `ticket_closed` (kiểm tra `closed_at` so với thời điểm tạo trong `refund_request_created` $\le 24$h) và kiểm tra không có event `ticket_reopened` mang cùng `trace_id` trong vòng 7 ngày sau khi đóng.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm các event `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia cho tổng số event `staff_review_decision` được ghi nhận.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Đếm số event `ticket_reopened` có thời gian mở lại trong vòng 7 ngày, chia cho tổng số event `ticket_closed`.
- **Chỉ số dùng tự đề xuất (% mở bằng trợ lý):** Đếm số event `agent_suggestion_shown` chia cho số event `refund_request_created` có `arm == 'intervention'`.
- **Chỉ số an toàn tự đề xuất (% đơn hoàn sai tiền kiểm tra mẫu):** Đếm số event `audit_sample_checked` có `so_tien_da_hoan != so_tien_dung`, chia cho tổng số event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, lên **6.787 đ** (`simulated`) | Tỉ lệ làm lại theo tuần > 7% (mức chạy thử là 4,9% trong phạm vi pilot) | Thu hẹp phạm vi về chỉ `noi_dia`, rà soát 20 trace làm lại gần nhất để sửa prompt và tool | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí mỗi việc thành công tăng lên **11.743 đ** (0,98×) hoặc **12.415 đ** (1,03× nếu làm lại mất 15,3 phút) (`simulated`), mất lợi thế so với nhân viên tự làm | Tỉ lệ yêu cầu cần xem lại vẫn còn > 50% ở cuối bước rollout 0.25 | Thực hiện giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ của nhân viên < 15% | Trưởng nhóm CSKH |
| Khối lượng thực tế thấp hơn dự kiến | Phân bổ chi phí cố định 40 triệu đ/tháng làm tăng **+1.185 đ/việc** ở 45.000 yc/tháng và tăng **+2.370 đ/việc** nếu còn 22.500 yc/tháng (`simulated`) | Số việc thành công theo tuần thấp hơn 50% kế hoạch dự kiến | Tạm hoãn mở rộng pilot, đàm phán lại mức phí cố định cơ sở hạ tầng | PM trợ lý hoàn phí |
