# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Token, tool, xem lại và làm lại | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần** hoá đơn token và tool bình quân (`simulated`).
- Làm lại chiếm tỉ trọng lớn nhất, **51,77%** tổng chi phí (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (`simulated`) | 0,22× (`simulated`) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (`simulated`) | 0,69× (`simulated`) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (`simulated`) | 1,88× (`simulated`) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (`simulated`) | 0,85× (`simulated`) |

- Quốc tế chưa đáng đưa vào pilot. Với giới hạn 3 lượt, nhóm này dùng trung bình 2,32 lượt/yêu cầu mà chỉ thành công 27,3%, với chi phí 22.515 đ/việc thành công (`simulated`), gấp 1,88 lần mức tự làm.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | ≈ 4.599 đ (`simulated`) | 0,38× (`simulated`) |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | ≈ 5.784 đ (`simulated`) | 0,48× (`simulated`) |

- Tính tay từ A3 và A4: 900/1.200 yêu cầu thành công thuộc phạm vi pilot; lấy 75% tổng lượng tháng để chia 40 triệu đồng. Cộng vào CPS 3.414 đ (`simulated`), cả hai mức vẫn dưới 12.000 đ.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (`simulated`) | +5,6% (`simulated`) |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (`simulated`) | −2,8% (`simulated`) |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (`simulated`) | +40,7% (`simulated`) |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (`simulated`) | −20,3% (`simulated`) |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (`simulated`) | +51,8% (`simulated`) |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (`simulated`) | −25,9% (`simulated`) |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (`simulated`) | +23,1% (`simulated`) |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (`simulated`) | −5,2% (`simulated`) |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (`simulated`) | −8,1% (`simulated`) |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi: **6.543 đ/việc thành công, tăng 46,3%** (`simulated`). Hai tác động cộng lại vì các khoản chi phí cộng tuyến tính.
- Ba yếu tố ảnh hưởng mạnh nhất: 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương nhân viên (+23,1%). Các mức thay đổi đều là `simulated`.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (`simulated`) | 319 | 7.449.781 đ (`simulated`) | 4.111 đ (`simulated`) |
| 2 lần | 4.093.220 đ (`simulated`) | 234 | 6.901.220 đ (`simulated`) | 4.237 đ (`simulated`) |
| 3 lần | 4.373.585 đ (`simulated`) | 222 | 7.037.585 đ (`simulated`) | 4.472 đ (`simulated`) |

- Tối đa 2 lượt rẻ nhất cho công ty (6.901.220 đ, `simulated`). Giới hạn 1 lượt cho CPS thấp nhất (4.111 đ, `simulated`) và có thêm 85 yêu cầu để nhân viên xử lý so với giới hạn 2 lượt.

## B4 · Nếu phải xem lại tất cả

- Xem lại cả 948 yêu cầu có kết quả: **11.743 đ/việc thành công** (0,98×) nếu làm lại 9 phút/ca, hoặc **12.415 đ** (1,03×) nếu làm lại 15,3 phút/ca. Cả hai kịch bản là `simulated`.
- Pilot cần đo thời gian xem lại, thời gian làm lại và tỉ lệ xem lại có thể giảm an toàn. Với xem lại 100%, ngưỡng hòa vốn là **5,1 phút/yêu cầu** hoặc **4,8 phút/yêu cầu** tương ứng (`simulated`).
