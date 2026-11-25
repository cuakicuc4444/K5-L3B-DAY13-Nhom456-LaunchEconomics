"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        # Yêu cầu vượt giới hạn chuyển sang nhân viên và không tính phút của trợ lý.
        reqs = reqs[reqs['so_lan_chay'] <= max_lan_chay]

    token = (runs['tokens_in'].sum() * gia_vao + runs['tokens_out'].sum() * gia_ra) / 1000
    tool = runs['tool_calls'].sum() * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else math.inf

    return {
        'token': token,
        'tool': tool,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
    }


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ p1, p2."""
    from statistics import NormalDist
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def nhiem_vu_d(reqs, icc=0.02):
    """Tính toán cỡ mẫu D1 và tỉ lệ mở lại 7 ngày hiện tại cho kế hoạch pilot."""
    from statistics import NormalDist
    n_req = co_mau(0.70, 0.75)
    m_staff = 75
    de_75 = 1 + (m_staff - 1) * icc
    n_staff_75 = math.ceil(n_req * de_75)
    c_needed_75 = math.ceil(n_staff_75 / m_staff)
    max_20_staff = int(20 / icc)
    max_6_depot = int(6 / icc)

    n_6pt = co_mau(0.70, 0.76)
    m_min_6pt = math.ceil(n_6pt * (1 - icc) / (20 - n_6pt * icc))
    de_6pt = 1 + (m_min_6pt - 1) * icc

    z_crit = NormalDist().inv_cdf(1 - 0.05 / 2)
    se_null = math.sqrt(2 * 0.725 * 0.275 / n_6pt)
    se_alt = math.sqrt((0.70 * 0.30 + 0.75 * 0.25) / n_6pt)
    power_at_5pt = 1 - NormalDist().cdf((z_crit * se_null - 0.05) / se_alt)

    reopen_all = reqs['mo_lai_trong_7_ngay'].mean()
    sub = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    reopen_sub = sub['mo_lai_trong_7_ngay'].mean()

    print('\n--- Nhiệm vụ D1 · Cỡ mẫu & Tỉ lệ mở lại ---')
    print(f'a) Chia theo yêu cầu (MDE 5 điểm): {n_req} yêu cầu/nhóm')
    print(f'b) Theo nhân viên, m=75: DE={de_75:.2f}, n={n_staff_75}/nhóm -> {c_needed_75} người/nhóm (tổng {2*c_needed_75} > 40)')
    print(f'c) 20 nhân viên/nhóm: tối đa {max_20_staff} < {n_req} (không đạt)')
    print(f'd) 6 depot/nhóm: tối đa {max_6_depot} < {n_req} (không đạt)')
    print(f'e) MDE 6 điểm ({n_6pt}/nhóm), 20 nhân viên/nhóm: m >= {m_min_6pt}, DE={de_6pt:.2f}, power tại 5 điểm = {power_at_5pt:.2f}')
    print(f'Tỉ lệ mo_lai_trong_7_ngay: toàn bộ {reopen_all:.2%} ({int(reqs["mo_lai_trong_7_ngay"].sum())}/{len(reqs)}), noi_dia+hang_nang {reopen_sub:.2%} ({int(sub["mo_lai_trong_7_ngay"].sum())}/{len(sub)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    chi_phi_chay_lai = mo_hinh(runs[runs['attempt'] > 1], reqs)
    hoa_don_chay_lai = chi_phi_chay_lai['token'] + chi_phi_chay_lai['tool']
    print(f'Token và tool từ lượt 2 trở đi: {hoa_don_chay_lai:,.0f} đ')
    # Nhiệm vụ A3: tính lại theo từng loại yêu cầu.
    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f'{"Loại":<14} {"Yêu cầu":>9} {"Thành công":>12} '
          f'{"Tỷ lệ TC":>10} {"Lượt/YC":>9} {"CPS (đ)":>12} {"So với tự làm":>15}')
    for loai, reqs_loai in reqs.groupby('loai', sort=False):
        runs_loai = runs[runs['request_id'].isin(reqs_loai['request_id'])]
        chi_phi = mo_hinh(runs_loai, reqs_loai)
        so_yeu_cau = len(reqs_loai)
        thanh_cong = chi_phi['thanh_cong']
        cps = chi_phi['cps']
        print(f'{loai:<14} {so_yeu_cau:>9,} {thanh_cong:>12,} '
              f'{thanh_cong / so_yeu_cau:>10.1%} {len(runs_loai) / so_yeu_cau:>9.2f} {cps:>12,.0f} '
              f'{cps / BASELINE:>14.2f}×')
    print('CPS và tỷ lệ so với tự làm: simulated.')

    # Nhiệm vụ A4: phân bổ chi phí cố định trên số việc thành công dự kiến.
    reqs_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pilot = runs[runs['request_id'].isin(reqs_pilot['request_id'])]
    chi_phi_pilot = mo_hinh(runs_pilot, reqs_pilot)
    ti_le_pilot = chi_phi_pilot['thanh_cong'] / len(reqs_pilot)
    # Khối lượng tháng tính trên mọi loại yêu cầu, chỉ tính việc thành công thuộc pilot.
    ti_le_thanh_cong_tren_tong = chi_phi_pilot['thanh_cong'] / len(reqs)
    chi_phi_co_dinh_thang = 40_000_000

    print('\nA4 · Chi phí cố định cho nội địa và hàng nặng')
    print(f'Tỷ lệ thành công trong phạm vi: {ti_le_pilot:.2%}')
    print(f'Việc thành công trong phạm vi / tổng yêu cầu: {ti_le_thanh_cong_tren_tong:.2%}')
    print(f'CPS trước chi phí cố định: {chi_phi_pilot["cps"]:,.0f} đ (simulated)')
    print(f'{"YC/tháng":>10} {"TC/tháng":>10} {"Cố định/TC":>12} '
          f'{"CPS tổng (đ)":>14} {"So với tự làm":>15}')
    for so_yeu_cau_thang in (45_000, 22_500):
        thanh_cong_thang = so_yeu_cau_thang * ti_le_thanh_cong_tren_tong
        co_dinh_moi_viec = chi_phi_co_dinh_thang / thanh_cong_thang
        cps_tong = chi_phi_pilot['cps'] + co_dinh_moi_viec
        print(f'{so_yeu_cau_thang:>10,} {thanh_cong_thang:>10,.0f} '
              f'{co_dinh_moi_viec:>12,.0f} {cps_tong:>14,.0f} '
              f'{cps_tong / BASELINE:>14.2f}×')
    print('CPS tổng và tỷ lệ so với tự làm: simulated.')

    # Nhiệm vụ B1: đổi từng yếu tố so với CPS của A2.
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    cps_goc = ket_qua['cps']
    print('\nB1 · Bảng độ nhạy (simulated)')
    print(f'{"Kịch bản":<28} {"CPS (đ)":>10} {"Thay đổi":>10}')
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:<28} {cps:>10,.0f} {cps / cps_goc - 1:>+10.1%}')

    print('\nB2 · Token và xem lại cùng gấp đôi (simulated)')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'{cps_cap:,.0f} đ ({cps_cap / cps_goc - 1:+.1%})')

    print('\nB3 · Chi phí cả hệ thống theo giới hạn chạy (simulated)')
    print(f'{"Lượt tối đa":>11} {"Tổng trợ lý":>14} {"Không TC":>10} '
          f'{"Cả hệ thống":>14} {"CPS (đ)":>10}')
    for gioi_han in (1, 2, 3):
        ket_qua_gioi_han = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua_gioi_han['thanh_cong']
        tong_tro_ly = ket_qua_gioi_han['tong']
        tong_he_thong = tong_tro_ly + BASELINE * khong_thanh_cong
        print(f'{gioi_han:>11} {tong_tro_ly:>14,.0f} {khong_thanh_cong:>10,} '
              f'{tong_he_thong:>14,.0f} {ket_qua_gioi_han["cps"]:>10,.0f}')

    print('\nB4 · Xem lại 100% lượt có kết quả trong phạm vi pilot (simulated)')
    so_xem_lai = runs_pilot.loc[runs_pilot['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((reqs_pilot['ket_qua'] == 'lam_lai').sum())
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    phut_lam_lai_tb = round(phut_lam_lai_tb, 1)
    hoa_don_pilot = chi_phi_pilot['token'] + chi_phi_pilot['tool']
    thanh_cong_pilot = chi_phi_pilot['thanh_cong']
    print(f'Yêu cầu xem lại: {so_xem_lai}; ca làm lại: {so_lam_lai}; '
          f'token và tool: {hoa_don_pilot:,.0f} đ')
    for phut_lam_lai in (9, phut_lam_lai_tb):
        chi_phi_lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
        cps = (hoa_don_pilot + so_xem_lai * 5 * LUONG_PHUT + chi_phi_lam_lai) / thanh_cong_pilot
        ngan_sach_xem_lai = BASELINE * thanh_cong_pilot - hoa_don_pilot - chi_phi_lam_lai
        phut_hoa_von = ngan_sach_xem_lai / (so_xem_lai * LUONG_PHUT)
        print(f'Làm lại {phut_lam_lai:g} phút/ca: {cps:,.0f} đ ({cps / BASELINE:.2f}×), '
              f'xem lại hòa vốn ở {phut_hoa_von:.1f} phút/yêu cầu')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    nhiem_vu_d(reqs)
