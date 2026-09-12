#!/usr/bin/env python3
"""Soát title theo định mức của skills-title.

    python3 kiem-title.py titles.txt
    python3 kiem-title.py -            # đọc stdin
    python3 kiem-title.py -q file.txt  # chỉ in dòng có LỖI

Mỗi dòng trong file là một title. Dòng trống và dòng mở đầu bằng '#' bị bỏ qua.
Quy tắc nằm ở references/2-do-luong.md — sửa ở đó trước, rồi mới sửa file này.
"""
import re
import sys
import unicodedata

TRAN_TREN = 100
SAN_DUOI = 90
TOI_UU = (93, 99)   # dải an toàn: không sát sàn, không sát trần

EM_DASH = "—"
EN_DASH = "–"

TINH_TU_DANH_GIA = [
    "incredible", "shocking", "unbelievable", "amazing", "heartbreaking",
    "epic", "insane", "crazy", "jaw-dropping", "mind-blowing", "stunning",
]

HUA_SUONG = ["what happened next", "you won't believe", "you wont believe"]

# (mô tả cặp mòn, regex vế trước, regex vế sau)
CAP_MON = [
    ("T8xV1 — gọi cảnh sát rồi hoá ra anh ta là cảnh sát trưởng",
     r"call(ed)?\s+(the\s+)?cops|report(ed)?\s+", r"police chief|district attorney|sheriff"),
    ("T2xV4 — cho đi ít ỏi rồi cả băng mô-tô kéo đến",
     r"gave|fed|shared|helped|hid", r"harley|biker|hell'?s angels|rolled up"),
]


def do_dai(s: str) -> int:
    """Đếm ký tự như nền tảng đếm: chuẩn hoá NFC, không tính khoảng trắng thừa hai đầu."""
    return len(unicodedata.normalize("NFC", s.strip()))


def soat(title: str):
    """Trả về (loi, canh_bao) — hai list chuỗi mô tả."""
    loi, canh_bao = [], []
    t = title.strip()
    n = do_dai(t)

    if n > TRAN_TREN:
        loi.append(f"dài {n} ký tự, quá trần {TRAN_TREN} — nền tảng sẽ cắt mất vế lật")
    elif n < SAN_DUOI:
        loi.append(f"chỉ {n} ký tự, dưới sàn {SAN_DUOI} — thiếu chỗ cho hai đầu sắc")
    elif n < TOI_UU[0]:
        canh_bao.append(f"{n} ký tự, sát sàn — còn chỗ để thêm chi tiết (3-quy-trinh.md §5)")
    elif n > TOI_UU[1]:
        canh_bao.append(f"{n} ký tự, sát trần — một chữ nữa là bị cắt")

    so_em = t.count(EM_DASH)
    if so_em == 0:
        if EN_DASH in t or re.search(r"\s-\s", t):
            loi.append("dùng '-' hoặc '–' thay cho em dash '—'")
        else:
            loi.append("không có dấu '—' ngăn hai vế")
    elif so_em > 1:
        loi.append(f"có {so_em} dấu '—' — quá hai mệnh đề")
    else:
        truoc, sau = t.split(EM_DASH)
        if not (truoc.endswith(" ") and sau.startswith(" ")):
            canh_bao.append("dấu '—' thiếu khoảng trắng một bên")
        if "black" not in t.lower():
            loi.append("không có từ 'Black' — mặc định sản xuất của kênh")
        elif "black" not in truoc.lower():
            canh_bao.append("'Black' nằm ở vế sau, không ở vế trước")
        if len(sau.strip()) < 20:
            canh_bao.append("vế sau quá ngắn, khó có quy mô")
        for mo_ta, re_truoc, re_sau in CAP_MON:
            if re.search(re_truoc, truoc, re.I) and re.search(re_sau, sau, re.I):
                canh_bao.append(f"cặp mòn: {mo_ta}")

    caps = [w for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in {"CEO", "MIT", "FBI", "UFC", "SEAL", "US", "ER", "SOS"}]
    if len(caps) > 1:
        canh_bao.append(f"{len(caps)} từ CAPS ({', '.join(caps)}) — tối đa một")

    low = t.lower()
    for tu in TINH_TU_DANH_GIA:
        if re.search(rf"\b{re.escape(tu)}\b", low):
            loi.append(f"tính từ đánh giá: '{tu}'")
    for cum in HUA_SUONG:
        if cum in low:
            canh_bao.append(f"khuôn hứa suông: '{cum}'")

    if t.endswith("."):
        loi.append("có dấu chấm cuối câu")
    if t.count("!") > 1:
        canh_bao.append("nhiều hơn một dấu chấm than")
    # "One Call", "One Word", "No One" là khuôn chuẩn, không tính. Chỉ soát số lớn.
    so_chu = re.findall(r"\b(twenty|thirty|forty|fifty|sixty|hundred|thousand|million|billion)\b", low)
    so_chu = [x for x in so_chu if not re.search(rf"(a|per)\s+{x}", low)]
    if so_chu:
        canh_bao.append(f"số lớn viết bằng chữ ({', '.join(sorted(set(so_chu)))}) — title nên dùng chữ số")

    return loi, canh_bao


def main():
    args = [a for a in sys.argv[1:]]
    im_lang = "-q" in args
    args = [a for a in args if a != "-q"]
    if not args:
        print(__doc__)
        sys.exit(1)

    nguon = sys.stdin if args[0] == "-" else open(args[0], encoding="utf-8")
    titles = [l.rstrip("\n") for l in nguon if l.strip() and not l.lstrip().startswith("#")]
    if nguon is not sys.stdin:
        nguon.close()

    n_loi = n_cb = 0
    for i, t in enumerate(titles, 1):
        loi, cb = soat(t)
        if loi:
            n_loi += 1
        if cb:
            n_cb += 1
        if im_lang and not loi:
            continue
        trang_thai = "LỖI" if loi else ("CẢNH BÁO" if cb else "OK")
        print(f"[{trang_thai}] {do_dai(t):>3} | {i}. {t.strip()}")
        for m in loi:
            print(f"        ✗ {m}")
        for m in cb:
            print(f"        ! {m}")

    print(f"\n— Tổng {len(titles)} title: {len(titles) - n_loi - n_cb} OK · {n_cb} cảnh báo · {n_loi} lỗi")
    sys.exit(1 if n_loi else 0)


if __name__ == "__main__":
    main()
