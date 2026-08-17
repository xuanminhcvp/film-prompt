# -*- coding: utf-8 -*-
"""Thư viện dựng prompt dùng chung cho PIPELINE-ALTAR.

Mọi scene BẮT BUỘC gọi qua đây — một chỗ sửa, cả phim đổi theo.
"""
import math, os, re

import kb1, kb2, kb3, kb4

KB = {}
for _m in (kb1, kb2, kb3, kb4):
    for _k in dir(_m):
        if re.fullmatch(r'S\d+', _k):
            KB[_k] = getattr(_m, _k)


# ─────────────────────────── KỊCH BẢN ────────────────────────────
def line(sid, i):
    who, s = KB[sid][1][i]
    return f'{who}: "{s}"'


def text(sid, *idx):
    """Thoại nguyên văn của các dòng chỉ định (0-based)."""
    return "\n".join(line(sid, i) for i in idx)


def dem_tu(t):
    return len(re.findall(r"[A-Za-z']+", re.sub(r'^\s*[A-ZÀ-ỸĐ\.\' ]+(\(.*?\))?:', '', t, flags=re.M)))


def giay(t, ketclip=False):
    """Giây tối thiểu: 3 từ/giây (+2s nếu có KẾT CLIP), làm tròn lên bậc 6/8/10/12/14."""
    can = dem_tu(t) / 3 + (2 if ketclip else 0)
    for b in (6, 8, 10, 12, 14, 16, 18, 20):
        if can <= b + 0.5:
            return b
    return int(math.ceil(can))


def script(sid):
    return "\n".join(line(sid, i) for i in range(len(KB[sid][1])))


# ─────────────────────────── THẺ REF ─────────────────────────────
P_HEAD = (
    "Ảnh chân dung tham chiếu nhân vật, photorealistic, chất điện ảnh, **KHUNG DỌC 2:3 (cao hơn rộng)**,\n"
    "da có kết cấu thật với lỗ chân lông nhìn rõ, nét căng. Chụp NGANG NGỰC TRỞ LÊN, chính diện hơi chếch,\n"
    "mặt chiếm khoảng 40% chiều cao khung, NHÌN THẲNG VÀO ỐNG KÍNH. Nền xám trung tính trơn, không đồ đạc.\n"
    "Ánh sáng studio dịu từ chếch trái, đều trên mặt, KHÔNG mảng tối gắt. Mặc kín, cài cúc, KHÔNG hở ngực.\n"
    "Miệng khép tự nhiên, KHÔNG cười. KHÔNG chữ, KHÔNG watermark, KHÔNG logo.\n\n")

F_HEAD = (
    "Ảnh tham chiếu TRANG PHỤC, photorealistic, chất điện ảnh, **KHUNG DỌC 9:16 (cao hơn rộng)**.\n"
    "Chụp TOÀN THÂN, thấy trọn từ đỉnh đầu tới mũi giày, người đứng thẳng tự nhiên, hai tay buông xuôi, chính diện.\n"
    "NGƯỜI CHIẾM GẦN TRỌN CHIỀU CAO KHUNG — chừa lề nhỏ trên đầu và dưới chân, hai bên để trống.\n"
    "Nền xám trung tính trơn, sàn cùng tông, không đồ đạc. Ánh sáng studio đều, dịu, thấy rõ chất vải và nếp gấp.\n"
    "Gương mặt giống ẢNH CHÂN DUNG tham chiếu — KHÔNG đổi tuổi, KHÔNG đổi tông da, KHÔNG làm sáng da.\n"
    "Mặt nhìn rõ nhưng KHÔNG phải trọng tâm — trọng tâm là BỘ QUẦN ÁO. Biểu cảm trung tính, không cười.\n"
    "KHÔNG chữ, KHÔNG watermark, KHÔNG logo thương hiệu.\n\n")

F_HEAD_NGOI = (
    "Ảnh tham chiếu TRANG PHỤC, photorealistic, chất điện ảnh, **KHUNG DỌC 9:16 (cao hơn rộng)**.\n"
    "Chụp TOÀN THÂN NGƯỜI NGỒI XE LĂN, thấy trọn từ đỉnh đầu tới bánh xe và mũi giày, chính diện, lưng thẳng.\n"
    "NGƯỜI VÀ XE CHIẾM GẦN TRỌN CHIỀU CAO KHUNG — chừa lề nhỏ trên và dưới, hai bên để trống.\n"
    "Nền xám trung tính trơn, sàn cùng tông, không đồ đạc. Ánh sáng studio đều, dịu, thấy rõ chất vải và khung xe.\n"
    "Gương mặt giống ẢNH CHÂN DUNG tham chiếu — KHÔNG đổi tuổi, KHÔNG đổi tông da, KHÔNG làm sáng da.\n"
    "Mặt nhìn rõ nhưng KHÔNG phải trọng tâm — trọng tâm là BỘ QUẦN ÁO và CHIẾC XE LĂN.\n"
    "Biểu cảm trung tính, không cười. KHÔNG chữ, KHÔNG watermark, KHÔNG logo thương hiệu.\n\n")

PROP_HEAD = (
    "Ảnh tĩnh photorealistic, tỉ lệ 1:1, ống kính 85mm, ánh sáng STUDIO SÁNG và ĐỀU từ hai phía để KHÔNG có mảng tối.\n"
    "Đạo cụ đặt trên một mặt bàn gỗ trơn màu nâu trung tính để thấy rõ bóng đổ và tỷ lệ kích thước. Hậu cảnh xoá phông nhẹ.\n"
    "Vật đặt CHÍNH GIỮA khung, góc BA PHẦN TƯ để thấy cả mặt trước lẫn một mặt bên, chiếm khoảng 70% chiều rộng khung.\n"
    "Thấy rõ chất liệu và độ cũ mới. KHÔNG có người, KHÔNG có bàn tay, KHÔNG vật thể thứ hai trong khung.\n"
    "KHÔNG watermark, KHÔNG logo thương hiệu.\n\n")

LC_DAU = (
    "1. KHUNG & CHẤT ẢNH\n"
    "· Mọi ảnh trong chat này: **16:9 ngang**, photorealistic, chất điện ảnh, da có kết cấu thật, nét căng.\n"
    "· Nhân dạng lấy ĐÚNG theo ảnh đính kèm: gương mặt, vóc dáng, tông da, kiểu tóc, đúng bộ đồ trong ảnh.\n"
    "  Giữ nguyên độ tuổi và tông da của từng người, KHÔNG làm sáng da, KHÔNG trẻ hoá.\n"
    "· KHÔNG ai nhìn vào ống kính.\n\n"
    "2. ẢNH ĐÍNH KÈM\n"
    "· Ảnh gửi kèm là ảnh THAM CHIẾU, KHÔNG phải khung hình cần vẽ lại.\n"
    "· Mỗi nhân vật có hai ảnh: một CHÂN DUNG (nền xám trơn, ngang ngực — để lấy đúng gương mặt) và một TOÀN THÂN\n"
    "  (nền xám trơn — để lấy đúng bộ quần áo của cảnh này). Nhận ra ai là ai bằng mô tả trong từng lệnh khung hình.\n"
    "· Ảnh đạo cụ nếu có là ảnh vật thể trên nền trung tính: lấy đúng hình dáng, kích thước và độ cũ của vật đó.\n"
    "· **ẢNH BỐI CẢNH đính kèm là để KHOÁ LOOK.** Giữ nguyên 100% kiến trúc, vật liệu, bảng màu, ánh sáng và tông màu\n"
    "  của frame tham chiếu đó. Máy quay được tự do đổi góc và cỡ cảnh, nhưng KHÔNG được đổi giờ giấc, thời tiết,\n"
    "  màu tường, màu sàn hay đồ đạc cố định.\n\n")

LC_CUOI = (
    "\nLUẬT CHỮ\n"
    "· KHÔNG chữ đọc được ở bất kỳ đâu trong khung: không biển hiệu, không nhãn, không watermark, không logo.\n"
    "· Ngoại lệ duy nhất là chữ được liệt kê tường minh trong lệnh của từng khung hình.\n\n"
    "LUẬT NGƯỜI\n"
    "· Chỉ vẽ đúng những người được liệt kê trong lệnh của từng khung hình. KHÔNG tự thêm, KHÔNG nhân bản, KHÔNG bớt người.\n"
    "· Quần chúng nền chỉ xuất hiện khi lệnh khung hình nêu rõ, và TUYỆT ĐỐI không nhìn vào ống kính.\n"
    "· Người ngồi xe lăn LUÔN ngồi đúng chiếc xe trong ảnh toàn thân của người đó, trừ khi lệnh khung hình nói khác.\n\n"
    "LUẬT TAY\n"
    "· CẤM giơ ngón tay lên để đếm hoặc minh hoạ cho lời đang nói, CẤM xoa cằm, CẤM chống cằm ra vẻ suy nghĩ.\n"
    "· Người đang nói mà không có việc gì cho tay thì để tay buông dọc thân, đặt trên đùi, trên tay vịn hoặc\n"
    "  nắm hờ — KHÔNG bịa thêm cử chỉ minh hoạ.\n"
    "· Chỉ vẽ đúng động tác tay được nêu trong lệnh khung hình.")


def luatchung(vatlieu, floorplan, truc):
    return LC_DAU + vatlieu.strip() + "\n\n" + floorplan.strip() + "\n\n" + truc.strip() + LC_CUOI


# ─────────────────────── SF (khung hình) ────────────────────────
# `pose.who` phải tả TƯ THẾ CỦA NGƯỜI, không tả chỗ họ nằm trong khung hình.
# Ghi chú khung ("nửa trái khung", "tiền cảnh phải", "out nét") đổi mỗi lần đổi
# góc máy dù người đứng yên; để nguyên thì `kiem-noi-shot.py` báo "nhảy tư thế"
# ở gần như mọi mối nối và bảng kiểm thành vô dụng. Bóc chúng ra ở một chỗ duy nhất.
_RE_KHUNG = re.compile(
    r"(?:,\s*)?(?:ở\s+)?(?:nửa|rìa)\s+(?:trái|phải|trên|dưới)\s+khung"
    r"|(?:,\s*)?(?:ở\s+)?(?:chính diện\s+)?giữa\s+khung"
    r"|(?:,\s*)?(?:ở\s+)?tiền\s*cảnh\s+(?:trái|phải)"
    r"|(?:,\s*)?(?:ở\s+)?rìa\s+(?:trái|phải|trên|dưới)"
    r"|(?:,\s*)?out\s*nét|(?:,\s*)?ngoài\s+vùng\s+nét|(?:,\s*)?ngoài\s+khung", re.I)


def _khu_vuc(z):
    """Chỉ giữ TÊN KHU VỰC, bỏ phần bổ nghĩa sau dấu phẩy.

    `zone` là khu vực của cả cụm; viết thêm "…, cạnh cửa phục vụ" hay
    "…, tiền rơi dưới chân" là tả đạo cụ chứ không phải đổi chỗ đứng, mà
    `kiem-noi-shot.py` so nguyên chuỗi nên mỗi câu bổ nghĩa thành một mối giả."""
    return z.split(",")[0].strip()


def _bo_ghi_chu_khung(v):
    v = _RE_KHUNG.sub("", v)
    v = re.sub(r"\s{2,}", " ", v).strip(" ,·")
    return v or "giữ nguyên tư thế"


def sf(sid, cam, doing, hands, look, emo, freeze, chars, bg, zone, who, dist, hands_pose,
       label=None, desc="", luat=None, cut=""):
    """Sinh một thẻ SF đúng 6 khối bắt buộc.

    `cut` — Lệnh Cắt Tham Chiếu: một chat dùng chung cho cả địa điểm nên ảnh ref
    của các khung trước vẫn nằm trong ngữ cảnh. Không chỉ đích danh người bị gạt
    thì model kéo họ vào khung sau, thành chật khung và sai cast."""
    d = {
        "id": sid,
        "label": label or sid.replace("SF-", ""),
        "desc": desc,
        "prompt": (f"MÁY QUAY: {cam}\n\n"
                   f"AI VÀ ĐANG LÀM GÌ: {doing}\n\n"
                   f"TAY: {hands}\n\n"
                   f"HƯỚNG NHÌN: {look}\n\n"
                   f"BIỂU CẢM: {emo}\n\n"
                   f"ĐÓNG BĂNG: {freeze}"
                   + (f"\n\nTHAM CHIẾU: {cut}" if cut else "")),
        "status": "proposed",
        "notes": "",
        "usedBy": [],
        "refs": {"chars": list(chars), "bg": bg},
        "pose": {"zone": _khu_vuc(zone), "who": {k: _bo_ghi_chu_khung(v) for k, v in who.items()},
                 "dist": dist, "hands": {k: _bo_ghi_chu_khung(v) for k, v in hands_pose.items()}},
    }
    if luat:
        d["luatchung"] = luat
    return d


def ref(rid, label, desc, prompt, chars=(), bg=None, luat=None, status="proposed"):
    d = {"id": rid, "label": label, "desc": desc, "prompt": prompt,
         "status": status, "notes": "", "usedBy": [],
         "refs": {"chars": list(chars), "bg": bg}}
    if luat:
        d["luatchung"] = luat
    return d


# ─────────────────────── SHOT (prompt video) ────────────────────
CAM_MAC_DINH = "TĨNH"
DUOI_THOAI = ("Âm thanh: CHỈ thoại nhân vật, tiếng Anh giọng Mỹ, rõ lời. Không âm nền. Không nhạc, không narrator, "
              "không phụ đề. MỘT SHOT LIỀN DUY NHẤT suốt cả video — tuyệt đối KHÔNG chuyển cảnh, KHÔNG cắt. "
              "Không thêm, xóa, thay thế hoặc nhân bản nhân vật.")


def _nhandien(nd):
    return "Nhận diện:\n" + "\n".join(f"- {n} = {m}" for n, m in nd)


def shot(vid, sfid, sid, idx, goc, nd, trongkhung, dien, thoai, im=(), cam=CAM_MAC_DINH,
         ketclip=None, dur=None, note=""):
    """Shot có thoại. `thoai` = [(TÊN, nhãn cảm xúc, số dòng kịch bản)]."""
    t = text(sid, *idx)
    kh = []
    for ten, nhan, i in thoai:
        kh.append(f'{ten} — {nhan}:\n"{KB[sid][1][i][1]}"')
    for ten, nhan in im:
        kh.append(f"{ten} — silent, {nhan}")
    d = dur or giay(t, bool(ketclip))
    pv = (f"{_nhandien(nd)}\n"
          f"Trong khung: {trongkhung} Ngoài những người đã nêu, KHÔNG thêm ai khác vào khung.\n\n"
          f"Một shot liền {d} giây, không chuyển cảnh. Camera {cam}. "
          f"TUYỆT ĐỐI KHÔNG để Camera lùi, kéo lùi hay PULL-OUT.\n\n"
          f"{dien}:\n\n" + "\n\n".join(kh) + f"\n\n{DUOI_THOAI}")
    if ketclip:
        pv += f"\n\nKẾT CLIP: {ketclip}"
    return {"id": vid, "sf": sfid, "dur": d, "vstatus": "", "ai_request": "", "notes": note,
            "text": t, "prompt": pv, "music": {}, "goc": goc}


def shotx(vid, sfid, goc, nd, trongkhung, dien, lines, im=(), cam=CAM_MAC_DINH,
          ketclip=None, dur=None, note=""):
    """Như `shot` nhưng thoại truyền thẳng bằng chuỗi — dùng khi một câu quá dài
    phải trải qua hai shot (chữ vẫn giữ nguyên 100%, chỉ chia chỗ cắt hình)."""
    t = "\n".join(f'{n}: "{s}"' for n, _, s in lines)
    kh = [f'{n} — {nh}:\n"{s}"' for n, nh, s in lines]
    for ten, nhan in im:
        kh.append(f"{ten} — silent, {nhan}")
    d = dur or giay(t, bool(ketclip))
    pv = (f"{_nhandien(nd)}\n"
          f"Trong khung: {trongkhung} Ngoài những người đã nêu, KHÔNG thêm ai khác vào khung.\n\n"
          f"Một shot liền {d} giây, không chuyển cảnh. Camera {cam}. "
          f"TUYỆT ĐỐI KHÔNG để Camera lùi, kéo lùi hay PULL-OUT.\n\n"
          f"{dien}:\n\n" + "\n\n".join(kh) + f"\n\n{DUOI_THOAI}")
    if ketclip:
        pv += f"\n\nKẾT CLIP: {ketclip}"
    return {"id": vid, "sf": sfid, "dur": d, "vstatus": "", "ai_request": "", "notes": note,
            "text": t, "prompt": pv, "music": {}, "goc": goc}


def nhip(vid, sfid, mota, goc, nd, trongkhung, trangthai, goiy, sfx, music, dur=6,
         cam=CAM_MAC_DINH):
    """Nhịp không thoại — BẮT BUỘC có nhạc và SFX/Ambient."""
    pv = (f"{_nhandien(nd)}\n"
          f"Trong khung: {trongkhung} Ngoài những người đã nêu, KHÔNG thêm ai khác vào khung.\n\n"
          f"Một shot liền {dur} giây, không chuyển cảnh. Camera {cam}. "
          f"TUYỆT ĐỐI KHÔNG để Camera lùi, kéo lùi hay PULL-OUT.\n\n"
          f"KHÔNG CÓ LỜI THOẠI TRONG CLIP NÀY. Tuyệt đối không ai mở miệng nói.\n\n"
          f"TRẠNG THÁI: {trangthai}\n"
          f"GỢI Ý DIỄN BIẾN: {goiy} Model tự chọn cử chỉ cho hợp lý, không ai nói.\n\n"
          f"Âm thanh: {sfx} KHÔNG lời thoại, KHÔNG nhạc, KHÔNG narrator, KHÔNG phụ đề. "
          f"MỘT SHOT LIỀN DUY NHẤT — tuyệt đối KHÔNG chuyển cảnh, KHÔNG cắt. "
          f"Không thêm, xóa hoặc nhân bản nhân vật.")
    return {"id": vid, "sf": sfid, "dur": dur, "vstatus": "", "ai_request": "", "notes": "",
            "text": f"[NHỊP] {mota}", "prompt": pv, "music": music, "goc": goc}


def nhac(role, emo, a, b):
    return {"role": role, "emo": emo, "a_kind": "có lời", "a": a, "b_kind": "không lời", "b": b}


# ─────────────────── BỘ HÀM TẮT CHO MỖI SCENE ───────────────────
# ────────────────────── QUẦN CHÚNG NỀN ──────────────────────
# THẺ ĐỊA ĐIỂM LUÔN TRỐNG NGƯỜI — không bao giờ viết quần chúng vào `luatchung`.
# Người nền chỉ tồn tại dưới dạng CHỮ TRONG KHỐI `AI VÀ ĐANG LÀM GÌ` CỦA TỪNG SF,
# nên mỗi SF tự mang câu quần chúng của riêng nó, cắt đúng theo nón quan sát của
# góc máy đó. Id địa điểm ở đây chỉ là KHOÁ TRA CỨU để biết chỗ đó có người hay
# không (nơi công cộng đang giờ hoạt động thì bắt buộc có; nhà riêng, văn phòng
# cá nhân, nơi đã đóng cửa thì không) — không có gì được ghi ngược vào thẻ.
# Mỗi chỗ giữ vài biến thể xoay vòng để đám đông không đứng yên một tư thế suốt
# scene, và từng SF ghi đè bằng `qc=` khi nón quan sát của nó khác.

def mk(sid, bg_mac_dinh, qc=None, qcv=None):
    """Trả về (SFS, SHOTS, S, V, VX, B) — mọi scene dùng chung một lối viết.

    `qc`/`qcv` là dict {số hiệu SF: câu quần chúng} — QUYẾT ĐỊNH RIÊNG CHO TỪNG
    KHUNG theo nón quan sát của chính khung đó, không phải một bộ câu khoá theo
    thẻ địa điểm rồi xoay vòng: xoay vòng thì câu quần chúng rơi vào khung nào là
    do số thứ tự, nên rất hay chửi nhau với câu hậu cảnh ngay trước nó (khách
    ngồi sau lưng bàn thờ, hàng ghế lơ lửng trước cánh cửa). Chuỗi rỗng = nón
    quan sát này không thấy ai. Thiếu khoá là lỗi, không phải mặc định rỗng.
    """
    from nv import refs, nd
    SFS, SHOTS = [], []

    def _lay(bang, n, ghide):
        if os.environ.get('BOQC'):   # dựng bản trắng quần chúng để rà lại nón quan sát
            return ""
        if ghide is not None:
            return ghide
        if not bang:
            return ""
        if n not in bang:
            raise KeyError(f"{sid}: thiếu quyết định quần chúng cho SF {n!r}")
        return bang[n]

    def _lay_v(n, ghide):
        """Quần chúng cho prompt video. Mặc định lấy thẳng câu của SF cùng số hiệu
        — SF vẽ ai thì clip phải giữ đúng người đó, không được để họ bốc hơi khi
        Grok dựng hình. Chỉ khai `qcv` riêng khi clip cần câu khác."""
        if ghide is not None:
            return ghide
        if qcv and n in qcv:          # ghi đè lẻ: khung nào khối SF tự khai người
            return qcv[n]             # nền thì clip phải khai lại bằng câu riêng
        t = _lay(qc, n, None)
        return (t + " Không ai trong số họ nhìn vào camera.") if t else ""

    def S(n, cam, doing, hands, look, emo, freeze, keys, zone, who, dist, hpose, bg=None,
          qc=None, _qc=qc):
        them = _lay(_qc, n, qc)
        SFS.append(sf(f"SF-{sid}-{n}", cam, doing.rstrip() + (" " + them if them else ""),
                      hands, look, emo, freeze, refs(*keys), bg or bg_mac_dinh,
                      zone, who, dist, hpose))

    def V(n, idx, goc, ndl, tk, dien, thoai, im=(), cam=CAM_MAC_DINH, ketclip=None, dur=None,
          qcv=None):
        them = _lay_v(n, qcv)
        SHOTS.append(shot(f"V-{sid}-{n}", f"SF-{sid}-{n}", sid, idx, goc, nd(*ndl),
                          tk.rstrip() + (" " + them if them else ""), dien,
                          thoai, im, cam, ketclip, dur))

    def VX(n, goc, ndl, tk, dien, lines, im=(), cam=CAM_MAC_DINH, ketclip=None, dur=None,
           qcv=None):
        them = _lay_v(n, qcv)
        SHOTS.append(shotx(f"V-{sid}-{n}", f"SF-{sid}-{n}", goc, nd(*ndl),
                           tk.rstrip() + (" " + them if them else ""), dien,
                           lines, im, cam, ketclip, dur))

    def B(n, mota, goc, ndl, tk, tt, gy, sfx, music, dur=6, cam=CAM_MAC_DINH,
          qcv=None):
        them = _lay_v(n, qcv)
        SHOTS.append(nhip(f"V-{sid}-{n}", f"SF-{sid}-{n}", mota, goc, nd(*ndl),
                          tk.rstrip() + (" " + them if them else ""), tt, gy,
                          sfx, music, dur, cam))

    return SFS, SHOTS, S, V, VX, B
