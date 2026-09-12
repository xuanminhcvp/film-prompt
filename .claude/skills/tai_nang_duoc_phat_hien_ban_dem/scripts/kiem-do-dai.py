#!/usr/bin/env python3
"""Soát độ dài và định dạng kịch bản của skill tai_nang_duoc_phat_hien_ban_dem.

    python3 kiem-do-dai.py KICH-BAN.md
    python3 kiem-do-dai.py -                    # đọc stdin (dán hook vào)
    python3 kiem-do-dai.py --tong 5000-6000 f   # user yêu cầu độ dài khác mặc định

Nhận cả hook riêng lẻ lẫn toàn bài. Tự tách:
  - MỞ MÀN   = các đoạn từ sau dòng `title:` tới trước đoạn lời rủ đầu tiên
  - LỜI RỦ   = đoạn đầu tiên có "comment" + ("like" hoặc "subscribe")
  - TOÀN BÀI = mọi đoạn trừ dòng `title:` (chỉ soát khi file có thân bài)
  - LỜI RỦ CUỐI = đoạn cuối cùng có "comment" hoặc "subscribe"

Định mức nằm ở references/4-hook-va-cta.md, 5-vi-thanh.md mục 6 và SKILL.md mục 1
— sửa ở đó trước, rồi mới sửa hằng số dưới đây.

Đếm từ: chỉ tính token có chữ hoặc số (dấu — đứng riêng không tính là từ).
Golden (GOLDEN-1.txt) đo bằng script này: mở màn 140 từ, lời rủ 37 từ,
toàn bài 7.781 từ, lời rủ cuối 51 từ. Golden báo LỖI định dạng vì viết liền —
đúng như mong đợi (luật dòng trống thắng Golden).
"""
import re
import sys

MO_MAN = (120, 160)          # 4-hook-va-cta.md mục 2.1
LOI_RU_TRAN = 40             # Golden 37
LOI_RU_CUOI_TRAN = 70        # 5-vi-thanh.md mục 6 — Golden ~50
TONG_MAC_DINH = (7500, 8000)  # SKILL.md mục 1
NGUONG_CO_THAN_BAI = 20      # số đoạn sau lời rủ để coi là toàn bài

KY_TU_CHO_PHEP = set("—’‘“”…")  # dấu câu tiếng Anh hợp lệ ngoài ASCII


def dem_tu(s: str) -> int:
    return sum(1 for t in s.split() if re.search(r"[A-Za-z0-9]", t))


def la_loi_ru(p: str) -> bool:
    p = p.lower()
    return bool(re.search(r"\bcomment", p)) and bool(re.search(r"\blike\b|subscrib", p))


def tach_doan(text: str):
    """Trả về (title, list đoạn, list lỗi định dạng, viết_liền)."""
    dong = text.replace("\r\n", "\n").split("\n")
    while dong and not dong[-1].strip():
        dong.pop()
    loi_dd = []
    title = ""
    if dong and dong[0].lower().startswith("title:"):
        title = dong[0]
        dong = dong[1:]
    else:
        loi_dd.append("dòng đầu không phải `title: ...`")

    doan = [d.strip() for d in dong if d.strip()]

    # Soát từng chỗ nối giữa hai dòng (dòng trống sau `title:` không tính).
    than = dong[1:] if dong and not dong[0].strip() else dong
    thieu = [i + 3 for i in range(len(than) - 1) if than[i].strip() and than[i + 1].strip()]
    kep = [i + 3 for i in range(len(than) - 1) if not than[i].strip() and not than[i + 1].strip()]
    viet_lien = len(doan) > 1 and len(thieu) == len(doan) - 1
    if thieu and not viet_lien:
        loi_dd.append(f"thiếu dòng trống giữa hai đoạn ở {len(thieu)} chỗ — dòng đầu tiên: {thieu[0]}")
    if kep:
        loi_dd.append(f"hai dòng trống liền nhau ở {len(kep)} chỗ — dòng đầu tiên: {kep[0]}")
    return title, doan, loi_dd, viet_lien


def muc(nhan, n, loi=None, canh_bao=None):
    trang_thai = "LỖI" if loi else ("CẢNH BÁO" if canh_bao else "OK")
    print(f"[{trang_thai}] {nhan}: {n} từ")
    for l in (loi or []):
        print(f"        ✗ {l}")
    for c in (canh_bao or []):
        print(f"        ! {c}")
    return bool(loi)


def main(argv):
    tong_khoang = TONG_MAC_DINH
    if "--tong" in argv:
        i = argv.index("--tong")
        a, b = argv[i + 1].split("-")
        tong_khoang = (int(a), int(b))
        del argv[i:i + 2]
    if not argv:
        print(__doc__)
        return 2
    text = sys.stdin.read() if argv[0] == "-" else open(argv[0], encoding="utf-8").read()

    title, doan, loi_dd, viet_lien = tach_doan(text)
    co_loi = False

    # --- Định dạng ---
    if viet_lien:
        loi_dd.append("viết liền không dòng trống — luật: giữa hai đoạn đúng một dòng trống (Golden không phải chuẩn ở chỗ này)")
    la = sorted({c for c in text if ord(c) > 127 and c not in KY_TU_CHO_PHEP})
    if la:
        print(f"[CẢNH BÁO] ký tự ngoài tiếng Anh: {' '.join(la)} — soát xem có chữ nước ngoài lọt vào không")
    if loi_dd:
        co_loi = True
        print("[LỖI] định dạng")
        for l in dict.fromkeys(loi_dd):
            print(f"        ✗ {l}")
    else:
        print("[OK] định dạng")

    # --- Mở màn + lời rủ ---
    vi_tri_ru = next((i for i, p in enumerate(doan) if la_loi_ru(p)), None)
    if vi_tri_ru is None:
        co_loi = True
        print("[LỖI] không tìm thấy đoạn lời rủ (cần 'comment' + 'like'/'subscribe')")
        return 1

    n_mo = sum(dem_tu(p) for p in doan[:vi_tri_ru])
    lo, hi = MO_MAN
    loi = []
    if n_mo > hi:
        loi.append(f"quá {hi} từ ({n_mo - hi} từ thừa) — cắt chi tiết thuộc về cảnh bắt gặp ở thân bài")
    elif n_mo < lo:
        loi.append(f"dưới {lo} từ — thiếu một chức năng? soát lại 6 chức năng ở 4-hook-va-cta.md 2.2")
    co_loi |= muc(f"mở màn ({vi_tri_ru} đoạn, chuẩn {lo}–{hi})", n_mo, loi)

    n_ru = dem_tu(doan[vi_tri_ru])
    loi = [f"quá {LOI_RU_TRAN} từ"] if n_ru > LOI_RU_TRAN else []
    co_loi |= muc(f"lời rủ đầu bài (trần {LOI_RU_TRAN})", n_ru, loi)

    # --- Toàn bài ---
    con_lai = len(doan) - vi_tri_ru - 1
    if con_lai < NGUONG_CO_THAN_BAI:
        print(f"(chỉ có hook — bỏ qua soát toàn bài)")
        return 1 if co_loi else 0

    n_tong = sum(dem_tu(p) for p in doan)
    lo, hi = tong_khoang
    loi = []
    if n_tong > hi:
        loi.append(f"quá {hi} từ ({n_tong - hi} từ thừa)")
    elif n_tong < lo:
        loi.append(f"thiếu {lo - n_tong} từ so với sàn {lo}")
    co_loi |= muc(f"toàn bài ({len(doan)} đoạn, chuẩn {lo}–{hi})", n_tong, loi)

    cuoi = next((i for i in range(len(doan) - 1, vi_tri_ru, -1)
                 if re.search(r"\bcomment|subscrib", doan[i].lower())), None)
    if cuoi is None:
        co_loi = True
        print("[LỖI] không tìm thấy lời rủ ở khối đóng bài")
    else:
        n_cuoi = dem_tu(doan[cuoi])
        cb = [f"quá {LOI_RU_CUOI_TRAN} từ — khối đóng bài phải ngắn"] if n_cuoi > LOI_RU_CUOI_TRAN else []
        muc(f"lời rủ cuối bài (trần {LOI_RU_CUOI_TRAN})", n_cuoi, canh_bao=cb)

    return 1 if co_loi else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
