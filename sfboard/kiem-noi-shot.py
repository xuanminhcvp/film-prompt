#!/usr/bin/env python3
"""Kiểm nối shot — bắt chỗ nhân vật/đạo cụ "nhảy" giữa hai clip liền nhau.

    python3 sfboard/kiem-noi-shot.py PIPELINE-RUTHS-HOUSE.project [S1 S2 ...]

So trường `pose` của SF ở hai shot kề nhau.

Mặc định chỉ báo mối NẶNG — đổi khu vực hoặc đổi tư thế, những thứ luôn cần nhịp chuyển.
Thêm --day-du để xem cả khoảng cách và tay cầm (đồ vặt đổi qua lại là bình thường, chỉ
đáng quan tâm khi món đó được thoại nhắc tới). Xem luật ở .claude/skills/skills-film.
"""
import json
import os
import re
import sys

AXES = [("zone", "KHU VỰC"), ("who", "TƯ THẾ"), ("dist", "KHOẢNG CÁCH"), ("hands", "TAY CẦM")]
# đổi zone hoặc tư thế là phải có nhịp chuyển; dist/hands chỉ nhắc
NANG = {"zone", "who"}

# HAI KIỂU `pose` CÙNG TỒN TẠI trong các project, phải đọc được cả hai:
#   dict   — {"zone": …, "who": {…}}          (RUTHS-HOUSE)
#   chuỗi  — "khu vực · A đứng … · B ngồi …"  (PORCH-LIGHT)
# Bản cũ chỉ đọc dict nên gặp project kiểu chuỗi là ném AttributeError giữa chừng,
# tức là scene NÀO cũng không kiểm được chứ không phải kiểm ra sạch — hỏng ồn ào
# nhưng dễ tưởng là script lỗi vặt rồi bỏ qua, và thế là mất luôn phép kiểm nối.
_TU_THE = ("đứng", "ngồi", "quỳ", "nằm", "dựa", "cúi", "đi ")


def _tu_chuoi(s: str) -> dict:
    """'khu vực · A đứng trái · B ngồi phải · tập hồ sơ đóng' → dict bốn trục.

    Đoạn ĐẦU là khu vực. Đoạn nào mở đầu bằng TÊN RIÊNG + từ chỉ tư thế thì vào
    `who` theo tên người; phần còn lại (đạo cụ, tay cầm) gom vào `hands`.
    `hands` gom thành MỘT chuỗi đã chuẩn hoá thường + sắp xếp, vì so từng đoạn
    một thì mọi khác biệt chính tả/hoa-thường đều báo động giả."""
    phan = [x.strip() for x in s.split("·") if x.strip()]
    if not phan:
        return {}
    ra = {"zone": phan[0], "who": {}, "hands": {}}
    con = []
    for seg in phan[1:]:
        # GHI CHÚ KHUNG HÌNH KHÔNG PHẢI TƯ THẾ. '(ngoài khung)', '(out nét)' nói
        # máy có thấy người đó không — người đứng yên bị OTS cắt ra vẫn đứng yên.
        # Không bóc ra thì mỗi lần đổi góc lại báo một mối 'nhảy' không có thật,
        # và báo động giả nhiều thì người ta thôi đọc cả bản kiểm.
        seg = re.sub(r"\s*\((?:ngoài khung|out nét|mờ|khuất)[^)]*\)", "", seg).strip()
        m = re.match(r"^([A-ZĐÂÊÔƯÁÀẢÃẠ][^\s]*)\s+(.+)$", seg)
        if m and any(t in seg.lower() for t in _TU_THE):
            ra["who"][m.group(1)] = m.group(2).strip()
        else:
            con.append(seg.lower())
    if con:
        ra["hands"]["_"] = " · ".join(sorted(con))
    return ra


def _chuan(pose):
    """Chuẩn hoá pose về dict, dù nguồn là dict hay chuỗi."""
    if isinstance(pose, str):
        return _tu_chuoi(pose)
    return pose or {}


def flat(pose, key):
    """Trả về dict phẳng cho một trục — who/hands là dict theo nhân vật."""
    v = _chuan(pose).get(key)
    if v is None:
        return None
    return v if isinstance(v, dict) else {"_": v}


def _tu(s):
    """Bộ từ của một mô tả, đã bỏ hoa-thường và mọi dấu câu."""
    return set(re.sub(r"[^\w\s]", " ", str(s).lower()).split())


def _dau_tu_the(s):
    """Từ chỉ tư thế đứng đầu mô tả — 'ngồi mép giường cúi xuống' → 'ngồi'."""
    for t in _TU_THE:
        if str(s).lower().lstrip().startswith(t.strip()):
            return t.strip()
    return None


def _gan(x, y, key):
    """Hai mô tả có ĐÁNG COI LÀ CÙNG MỘT TRẠNG THÁI không?

    So chuỗi thô thì mọi khác biệt CÁCH GỌI đều thành một mối "nhảy": cùng một
    khúc vỉa hè lúc ghi 'giữa vỉa hè' lúc ghi 'mặt vỉa hè', cùng một chỗ ngồi
    lúc ghi 'ngồi mép giường' lúc ghi 'ngồi mép giường cúi xuống', thậm chí chỉ
    lệch một dấu cách trước dấu phẩy. Bản kiểm ALTAR ra 654 cảnh báo kiểu đó thì
    không ai đọc nữa — và một phép kiểm không ai đọc thì bằng không có.

    Nên coi là CÙNG trạng thái khi bộ từ của bên này nằm trọn trong bên kia
    (mô tả sau chỉ nói kỹ hơn chứ không dời chỗ). Riêng trục tư thế còn đòi
    thêm: từ chỉ tư thế đứng đầu phải y nhau, để ngồi → đứng, nằm → ngồi vẫn
    báo đúng như trước.
    """
    a, b = _tu(x), _tu(y)
    if a == b:
        return True
    if not (a <= b or b <= a):
        return False
    if key == "who":
        return _dau_tu_the(x) is not None and _dau_tu_the(x) == _dau_tu_the(y)
    return True


def diff(a, b, key="zone"):
    """[(ai, trước, sau)] cho các giá trị khác nhau giữa hai trục."""
    if a is None or b is None:
        return []
    out = []
    for k in sorted(set(a) | set(b)):
        # người chỉ có ở MỘT bên = ra/vào khung hình (hoặc bị OTS cắt),
        # KHÔNG phải nhảy chỗ — không so được, bỏ qua
        if k not in a or k not in b:
            continue
        if a[k] != b[k] and not _gan(a[k], b[k], key):
            out.append((k, a[k], b[k]))
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != "--day-du"]
    day_du = "--day-du" in sys.argv
    proj = args[0]
    path = os.path.join(proj, "sf-board.json")
    if not os.path.exists(path):
        sys.exit(f"không thấy {path}")
    data = json.load(open(path, encoding="utf-8"))
    want = set(args[1:])

    SF = {f["id"]: f for sc in data["scenes"] for f in sc.get("sfs", [])}
    tong_canh, tong_thieu = 0, 0

    for sc in data["scenes"]:
        if want and sc["id"] not in want:
            continue
        shots = sc.get("shots", [])
        if len(shots) < 2:
            continue

        thieu = [s["id"] for s in shots if not (SF.get(s.get("sf"), {}) or {}).get("pose")]
        canh = []

        for truoc, sau in zip(shots, shots[1:]):
            pa = (SF.get(truoc.get("sf"), {}) or {}).get("pose")
            pb = (SF.get(sau.get("sf"), {}) or {}).get("pose")
            if not pa or not pb:
                continue
            # hai loại gián đoạn CỐ Ý, tự khai bằng cờ ở shot:
            #   chuyen   — shot mang chuyển động, nhân vật đi từ chỗ này sang chỗ khác
            #   hoituong — hồi tưởng / cắt sang dòng thời gian khác, không so vị trí được
            co_y = ("chuyen", "hoituong")
            if any(truoc.get(k) or sau.get(k) for k in co_y) \
                    or _chuan(pa).get("chuyen") or _chuan(pb).get("chuyen"):
                continue
            # BẢN SAO O.S — clip quay lại chính người nói câu vọng/điện thoại/loa
            # để lấy chuẩn giọng (skill bước 1, 'Xử lý Thoại O.S'). Nó cố ý đứng ở
            # không gian khác hai clip kẹp quanh, nên so vị trí là vô nghĩa.
            if any('BẢN SAO O.S' in (s.get('notes') or '') for s in (truoc, sau)):
                continue
            for key, ten in (AXES if day_du else [a for a in AXES if a[0] in NANG]):
                for ai, x, y in diff(flat(pa, key), flat(pb, key), key):
                    nhan = "⚠ " if key in NANG else "· "
                    who = "" if ai == "_" else f"{ai}: "
                    canh.append(f"  {nhan}{truoc['id']:9}→ {sau['id']:9} {ten:11} {who}{x} → {y}")
                    if key in NANG:
                        tong_canh += 1

        print(f"\n═══ {sc['id']}  ({len(shots)} shot) ═══")
        if thieu:
            tong_thieu += len(thieu)
            print(f"  chưa khai `pose` ({len(thieu)}): {', '.join(thieu)}")
        if canh:
            print("\n".join(canh))
        elif not thieu:
            print("  ✓ không có mối nào nhảy")

    print(f"\n{'─' * 60}")
    print(f"⚠ mối cần nhịp chuyển : {tong_canh}")
    print(f"  shot chưa khai pose : {tong_thieu}")
    print("\nCách xử, theo thứ tự ưu tiên: đặt vào NHỊP KHÔNG THOẠI · cho vừa đi vừa nói (chỉ")
    print("khi câu đó nói lúc đang đi vẫn ổn) · viết đường đi vào khối KẾT CLIP của shot TRƯỚC.")
    print("KHÔNG tự chế thêm lời thoại để tạo cớ di chuyển.")
    print('Gián đoạn cố ý thì khai ở shot: "chuyen": true (shot mang chuyển động) hoặc\n"hoituong": true (hồi tưởng / khác dòng thời gian).')
    if not day_du:
        print("Thêm --day-du để xem cả khoảng cách và tay cầm.")
    return 1 if tong_canh else 0


if __name__ == "__main__":
    sys.exit(main())
