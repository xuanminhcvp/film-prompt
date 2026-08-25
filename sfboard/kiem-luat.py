# -*- coding: utf-8 -*-
"""Kiểm mọi LUẬT CỨNG của skills-film trên sf-board.json.

    python3 sfboard/kiem-luat.py <PROJECT> [--bo S4,S6,S7,S8] [--scene S13]

VÌ SAO PHẢI LÀ FILE, KHÔNG GÕ LẠI MỖI LẦN: gõ lại phép kiểm ở mỗi lượt thì mỗi
lượt là một phiên bản khác nhau, và kết quả "SẠCH" của lượt này không có nghĩa gì
cho lượt sau. Đã có lần bỏ sót 6 lỗi thật vì lý do đó. Sửa luật thì sửa Ở ĐÂY.
"""
import json, os, re, sys, argparse, collections

ap = argparse.ArgumentParser()
ap.add_argument('project')
# MẶC ĐỊNH KHÔNG BỎ SCENE NÀO. Bản cũ để sẵn 'S4,S6,S7,S8' (scene khoá lúc đó);
# vài tuần sau các scene ấy dựng xong nhưng danh sách vẫn nguyên, nên chạy không
# cờ là lặng lẽ bỏ 4 scene rồi in "✓ SẠCH" — đã lừa đúng một lần 2026-08-07 (S6
# có 21 lỗi mà báo sạch). Danh sách khoá phải do người gõ ở đúng lượt cần khoá.
ap.add_argument('--bo', default='', help='scene bỏ qua, vd --bo S14,S15')
ap.add_argument('--scene', default='', help='chỉ kiểm scene này')
a = ap.parse_args()

PROJ = os.path.abspath(a.project)
BO = {x.strip() for x in a.bo.split(',') if x.strip()} | {'REF'}

# Không có board thì nói thẳng, đừng ném traceback. Hai project trong kho này
# (8DOLLARS, RUTHS-HOUSE) đang ở đúng tình trạng đó, và Errno 2 trần khiến người
# đọc tưởng script hỏng thay vì hiểu là phim ấy chưa/không còn phần chữ.
BOARD = os.path.join(PROJ, 'sf-board.json')
if not os.path.isfile(BOARD):
    print(f"✗ {os.path.basename(PROJ)} không có sf-board.json — không có gì để kiểm.")
    # Sắp theo NGÀY SỬA, không theo bảng chữ cái: tên bản lưu đặt theo việc đang
    # làm ('bak-treem-125824') nên thứ tự chữ cái chẳng liên quan gì tới thứ tự
    # thời gian, mà chép nhầm bản cũ là mất phần chữ viết sau đó.
    BAK = sorted((f for f in os.listdir(PROJ) if 'sf-board.json' in f and f != 'sf-board.json'),
                 key=lambda f: os.path.getmtime(os.path.join(PROJ, f))) if os.path.isdir(PROJ) else []
    if BAK:
        moi = BAK[-1]
        ngay = __import__('datetime').datetime.fromtimestamp(os.path.getmtime(os.path.join(PROJ, moi)))
        print(f"  Có {len(BAK)} bản .bak ở gốc project, mới nhất: {moi} ({ngay:%Y-%m-%d %H:%M})")
        print("  Muốn kiểm thì chép một bản thành sf-board.json trước.")
    sys.exit(2)

d = json.load(open(BOARD, encoding='utf-8'))
ALL = {f['id']: f for s in d['scenes'] for f in s.get('sfs', [])}


# `goc` ĐÃ CHUYỂN TỪ SF SANG SHOT (2026-08-11, thấy trên tab video của board).
# Phép kiểm cũ đọc `sf['goc']` nên sau khi chuyển thì thấy None ở mọi SF: báo
# `thiếu-goc` cho cả phim, và — nguy hơn — hai phép kiểm `người-nói-vắng-khung`
# với `khung-1-người-sai-luật` TẮT CÂM vì cả hai lấy `goc` làm điều kiện vào.
# Đọc từ shot trước, SF sau, để dự án cũ (goc còn nằm ở SF) vẫn chạy được.
_GOC_SHOT = {x['sf']: x['goc'] for s in d['scenes'] for x in s.get('shots', [])
             if x.get('sf') and (x.get('goc') or '').strip()}


def goc_cua(sf_id):
    return _GOC_SHOT.get(sf_id) or (ALL.get(sf_id, {}).get('goc') or '')


# SF nào đang làm `refs.bg` cho SF khác thì KHÔNG phải mồ côi, dù không shot
# nào dùng nó — thẻ địa điểm của scene chưa dựng shot rơi vào diện này.
LA_NEO = {f['refs'].get('bg') for f in ALL.values() if f['refs'].get('bg')}


def co_anh(i):
    return any(os.path.exists(os.path.join(PROJ, 'assets', i + e)) for e in ('.png', '.jpg', '.jpeg', '.webp'))


def cc(p):
    """Cỡ cảnh — thứ tự kiểm quan trọng: đặc-tả → trung-rộng → RỘNG → cận → trung.

    CHỈ đọc dòng `MÁY QUAY:` chứ không quét cả prompt: chữ 'cận' còn nằm trong
    'tiền cảnh', 'cận kề', và chữ 'toàn cảnh' hay được nhắc lại khi tả hậu cảnh.
    Quét cả prompt thì cỡ cảnh bị chấm theo chữ vô tình lọt vào chứ không theo
    lệnh máy quay thật.
    """
    # MỤC ĐÍCH: Phân loại các cỡ cảnh trong prompt SF (bao gồm góc đặc tả Insert/ECU với mốc rất hạn chế ~2%).
    m = re.search(r'MÁY QUAY:([^\n]*)', p)
    dong = m.group(1).lower() if m else p.lower()
    if re.search(r'đặc tả|insert|extreme close-up|\becu\b', dong): return 'đặc-tả'
    if re.search(r'medium[- ]wide|trung[- ]rộng', dong): return 'trung-rộng'
    if re.search(r'cinematic wide|toàn cảnh|viễn cảnh', dong): return 'RỘNG'
    if re.search(r'close-up|cận', dong): return 'cận'
    return 'trung'



def dem_tu(t):
    """Số từ tiếng Anh, đã bỏ tên nhân vật đứng đầu dòng."""
    return len(re.findall(r"[A-Za-z']+", re.sub(r'^\s*[A-ZÀ-ỸĐ\.\' ]+(\(.*?\))?:', '', t, flags=re.M)))


def nguoi_noi(t):
    """Tên đứng đầu dòng thoại. Bỏ nhãn kỹ thuật, chỉ giữ người phát ngôn."""
    bo = {'NARRATOR', 'SFX', 'MUSIC', 'AMBIENT'}
    return {m.group(1).strip() for m in re.finditer(
        r'^\s*([A-Z][A-Z0-9 .\'’-]{0,40}?)(?:\s*\([^\n)]*\))?\s*:', t, re.M)
        if m.group(1).strip() not in bo}


# MỘT DÒNG THOẠI = tên viết hoa đứng đầu dòng rồi dấu hai chấm. Dùng để TÁCH
# lời nhân vật khỏi phần mô tả khung ([NHỊP], `goc`, prompt video) — hai thứ đó
# nói hai chuyện khác nhau và không được trộn khi hỏi "khung này có gì".
RE_DONG_THOAI = re.compile(r"^[ \t]*[A-Z][A-Z0-9 .'\u2019-]{0,40}(?:\s*\([^\n)]*\))?\s*:.*$", re.M)


def mo_theo_goc(ten, goc):
    """Nhân vật này bị `goc` xếp ra tiền cảnh/out nét/mờ không? Dùng khi
    `pose.who` để trống — `goc` là nơi duy nhất còn khai vai trò khung hình."""
    # 'sau lưng' KHÔNG phải dấu hiệu out nét — 'Damon đứng sau lưng Nia, rõ mặt'
    # là người NÉT đứng ở lớp sau. Chỉ ba dấu hiệu dưới mới là vai trò tiền cảnh
    # out nét, và vế nào đã nói 'rõ mặt' thì tự nó phủ định (SF-S3-B1 · SF-S32-B3
    # từng bị báo oan đúng vì hai lỗi này, 2026-08-25).
    for ve in re.split(r'[·;+]', goc or ''):
        if not re.search(r'\b' + re.escape(ten) + r'\b', ve, re.I):
            continue
        if re.search(r'rõ\s*mặt', ve, re.I):
            continue
        if re.search(r'out\s*nét|mờ|vai\s*và\s*gáy', ve, re.I):
            return True
    return False


def co_trong_goc(ten, goc):
    """Tên phải nằm trong một vế `goc` không bị đánh dấu ngoài khung."""
    for ve in re.split(r'[·;]', goc or ''):
        if re.search(r'\b' + re.escape(ten) + r'\b', ve, re.I) and not re.search(
                r'ngoài\s+khung|off[- ]?screen', ve, re.I):
            return True
    return False


# ---- `goc`: AI ĐANG Ở TRONG KHUNG VÀ Ở TRẠNG THÁI NÀO ----------------------
# `goc` là câu trả lời duy nhất, đọc được bằng mắt, cho câu hỏi "SF này có ai".
# Bước 5 viết khối "Trong khung" của prompt video bằng đúng dòng này, và mọi
# phép kiểm người-nói-vắng-khung cũng đọc nó. Thiếu `goc` thì không phải "thiếu
# một trường cho đẹp" — là cả hai thứ đó mất căn cứ, im lặng.
#
# Tên nhân vật lấy từ thẻ REF chân dung (mỗi nhân vật có đúng một thẻ) HỢP với
# tên đứng đầu dòng thoại. Hai nguồn bù nhau: nhân vật phụ có thoại mà chưa có
# thẻ REF vẫn được nhận, và nhân vật câm có thẻ REF cũng vậy.
TEN_NV = {t for i in ALL if i.startswith('REF_') and i.endswith('_PORTRAIT')
          for t in i[4:-9].split('_') if t}
for _s in d['scenes']:
    for _x in _s.get('shots', []):
        TEN_NV |= {w for ten in nguoi_noi(_x.get('text') or '') for w in ten.split()}
TEN_NV = {t for t in TEN_NV if len(t) > 2}
TEN_PROP = {i[9:].lower().replace('_', ' ') for i in ALL if i.startswith('REF_PROP_')}
RE_CO_CANH = re.compile(
    r'cận|CU\b|MCU\b|trung|rộng|toàn\s*cảnh|two-shot|wide|close|medium|establishing', re.I)
RE_OTS = re.compile(r'\bOTS\b|over[- ]the[- ]shoulder', re.I)
RE_VAI = re.compile(r'vai|gáy', re.I)
# TỪ VỰNG KHUNG HÌNH — chữ nói về ống kính và vị trí, KHÔNG nói về người là ai.
# Dùng để hỏi một câu duy nhất: bỏ hết chữ khung hình đi thì vế này còn nhắc tới
# NGƯỜI NÀO không? Nhờ vậy "vai+gáy quản lý tiền cảnh" (nhân vật không tên, vẫn
# chỉ được đích danh) khác được với "vai tiền cảnh phải" (không biết vai của ai).
RE_TU_KHUNG = re.compile(
    r'\b(?:vai|gáy|tiền\s*cảnh|hậu\s*cảnh|lớp\s*(?:trước|sau)|out|nét|mờ|rìa|trái|phải|giữa'
    r'|trên|dưới|sau|trước|góc|khung|khuất|che|một\s*phần|mảng|nhẹ|hơi|và|của|ở|bên'
    r'|\d+\s*mm|\d+)\b', re.I)


def co_ten_nv(s):
    return any(re.search(r'\b' + re.escape(t) + r'\b', s, re.I) for t in TEN_NV)


def neu_duoc_ai(ve):
    """Vế này có chỉ ra một CON NGƯỜI cụ thể không — tên riêng, hoặc chỉ danh
    kiểu 'quản lý', 'thiếu niên', 'người qua đường'?"""
    return co_ten_nv(ve) or bool(re.sub(RE_TU_KHUNG, ' ', ve).replace('+', ' ').strip(' ,.·;()-'))


def loi_goc(i, goc):
    """Lỗi của một dòng `goc`. Chỉ bắt thứ ĐẾM ĐƯỢC — 'tả người, đừng tả cảnh'
    là việc của mắt, luật đó nằm trong skill bước 4."""
    goc = (goc or '').strip()
    if not goc:
        return [('thiếu-goc', f"{i}: không biết khung này có ai")]
    out = []
    if not co_ten_nv(goc):
        out.append(('goc-không-nêu-ai', f"{i}: {goc[:70]}"))
    # OTS mà không nói VAI CỦA AI thì model tự chọn một người bất kỳ làm tiền
    # cảnh — hỏng đúng thứ OTS sinh ra để giữ: cặp ai-đang-nói-với-ai.
    if RE_OTS.search(goc) and not any(RE_VAI.search(ve) and neu_duoc_ai(ve)
                                      for ve in re.split(r'[·;,]', goc)):
        out.append(('goc-OTS-không-rõ-vai-ai', f"{i}: {goc[:70]}"))
    return out


def offscreen_hop_le(ten, text, prompt):
    """Ngoại lệ chỉ cho nguồn thoại vốn nằm ở thiết bị/nơi khác trong kịch bản."""
    s = text + '\n' + prompt
    # `\b` sau 'screen', KHÔNG phải `\)`: nhãn thật luôn viết kèm nguồn phát —
    # `VIVIAN (off-screen, qua điện thoại)` — nên đòi ngoặc đóng ngay sau chữ
    # 'screen' là bắt oan đúng những shot đã khai chuẩn nhất. 6 shot của S13 bị
    # báo oan vì đúng một dấu phẩy (2026-08-08).
    da_khai = re.search(r'\b' + re.escape(ten) + r'\s*\(off[- ]?screen\b', s, re.I)
    co_nguon = re.search(r'điện thoại|loa\b|bộ đàm|vọng từ|phone|speaker|intercom|radio', s, re.I)
    return bool(da_khai and co_nguon)


def la_ban_sao_os(x):
    """Clip BẢN SAO của một câu O.S — skill bước 1 mục 'Xử lý Thoại O.S' bắt phải
    dựng thêm: câu vốn phát ra ngoài khung (điện thoại · loa · gọi vọng) được quay
    lại bằng chính nhân vật đang nói, để lấy chuẩn giọng. Clip ấy CỐ TÌNH chỉ có
    một người và CỐ TÌNH nằm ở không gian khác clip liền kề, nên hai phép kiểm
    'khung-1-người' và 'đổi-không-gian' phải miễn cho nó — nếu không, làm đúng
    skill lại bị báo lỗi."""
    return 'BẢN SAO O.S' in ((x.get('notes') or '') + (x.get('label') or ''))


def la_master(f):
    """SF này có phải Master của một CỤM KHÔNG GIAN không (skill bước 1)?"""
    i = f['id']
    return 'MASTER' in i or (i.startswith('SF-M-') and f['refs'].get('bg'))


def master(sf):
    f = ALL.get(sf)
    while f and not (f['id'].startswith('REF_BG_') or f['id'].startswith('SF-M-') or 'MASTER' in f['id']):
        b = f['refs'].get('bg')
        if not b: return None
        f = ALL.get(b)
    return f['id'] if f else None


# ---- LUẬT KHÔNG CÓ SCRIPT NÀO KIỂM ĐƯỢC TRƯỚC 2026-08-07 -------------------
# Đo trên dữ liệu thật hôm đó: 20 shot / 4 phim mang nhãn cảm xúc bị cấm (một
# trong số đó là ĐÚNG chuỗi `startled, sharp` mà skill nêu đích danh làm ví dụ
# sai), 82/166 SF vượt trần 1.000 ký tự, 28 SF thiếu khối HƯỚNG NHÌN. Luật đã
# nằm ở đầu SKILL.md, nạp 100% mỗi lượt, viết in đậm — vẫn lọt. Kết luận: prose
# không cưỡng chế được, chỉ script mới cưỡng chế được.
NHAN_CAM = ('angry', 'shouting', 'harsh', 'furious', 'sharp', 'cutting',
            'cold', 'icy', 'stern', 'snapping', 'menacing')
# (Đã bỏ quy tắc 6 khối bắt buộc vì chuyển sang viết văn phong cinematic mạch lạc)
# Dấu hiệu CÓ TRẺ EM TRONG KHUNG — quyết định mức nặng của lỗi nhãn cảm xúc.
#
# HAI BẪY đã mắc khi viết phép kiểm này (2026-08-07), đừng lặp lại:
# · Chữ `bé` ĐỨNG MỘT MÌNH nghĩa là NHỎ, không phải trẻ con — 'nhỏ bé', 'người
#   bé', 'gấu bé'. Chỉ nhận cụm ghép rõ nghĩa.
# · Prompt SF hay mang chính câu cấm 'TUYỆT ĐỐI KHÔNG CÓ TRẺ EM' (79 lần trong
#   4 phim). Đếm mù là hiểu NGƯỢC hoàn toàn: khung cấm trẻ bị tính thành khung
#   có trẻ. Phải soi phủ định ngay trước cụm.
# Mã ref là tín hiệu chắc hơn chữ — nhưng đừng thêm `SON`/`DAUGHT`, nó nuốt
# HENDER-SON và PATTER-SON.
RE_TRE_REF = re.compile(r'BABY|KID|CHILD|TODDLER|GIRL|BOY')
RE_TRE_CHU = re.compile(
    r'(?:trẻ em|đứa trẻ|đứa bé|cậu bé|cô bé|em bé|thằng bé|con bé|bé gái|bé trai)', re.I)
RE_PHU_DINH = re.compile(r'(?:KHÔNG(?:\s+CÓ)?|CẤM|VẮNG|TUYỆT ĐỐI KHÔNG)\s*$', re.I)


def co_tre_em(sf_id, prompt_video=''):
    """Khung này có trẻ em không? Quyết định nhãn cảm xúc cấm là LỖI hay CẢNH BÁO."""
    f = ALL.get(sf_id) or {}
    if any(RE_TRE_REF.search(c) for c in (f.get('refs') or {}).get('chars', [])):
        return True
    txt = (f.get('prompt') or '') + '\n' + prompt_video
    for m in RE_TRE_CHU.finditer(txt):
        if not RE_PHU_DINH.search(txt[max(0, m.start() - 18):m.start()]):
            return True          # có nhắc trẻ em mà KHÔNG phải câu cấm
    return False


def nhan_cam_xuc(p):
    """Nhãn cảm xúc bị cấm, CHỈ quét ô nhãn — đoạn giữa '—' và ':' ngay trước
    dòng thoại. Quét cả prompt là bắt oan chữ 'cold' nằm trong lời thoại."""
    ra = []
    for nhan in re.findall(r'—\s*([^:\n]{1,60}):\s*(?:\n|")', p):
        for w in NHAN_CAM:
            if re.search(r'\b' + w, nhan, re.I):
                ra.append((nhan.strip(), w))
    return ra


# ---- LUẬT CẤP PHIM: phải nhìn ≥2 SCENE mới thấy sai ------------------------
# Mọi phép kiểm ở trên chạy trong phạm vi MỘT SF / MỘT shot / MỘT scene. Luật
# nào cần so hai scene với nhau thì rơi ra ngoài tầm nhìn đó và không ai gác —
# đúng hai lần trong ngày 2026-08-08: chuỗi S10·S11·S12·S13 tối liền nhau (luật
# '≤2 scene tối liền' có sẵn trong skill, còn chỉ đích danh cách chữa), và kế
# hoạch trang phục trong `desc` của thẻ REF trôi khỏi `refs.chars` thật ở 3
# scene. Cả hai lượt `kiem-luat.py` đều in '✓ SẠCH'; user bắt bằng mắt.
#
# Hai phép kiểm dưới chạy MỘT LẦN cho cả phim, không chạy trong vòng lặp scene,
# và TỰ TẮT khi có `--scene` — chạy chúng trên một scene lẻ thì kết luận vô
# nghĩa, mà im lặng bỏ qua còn tệ hơn (xem bẫy `--bo` ở trên).
RE_TOI = re.compile(r'CHẬP\s*TỐI|RẠNG\s*SÁNG|BAN\s*ĐÊM|\bĐÊM\b|\bKHUYA\b', re.I)
RE_SANG = re.compile(r'BAN\s*NGÀY|CHIỀU|\bTRƯA\b|\bSÁNG\b', re.I)
# Hậu tố id là tín hiệu chắc nhất (thẻ đặt tên `REF_<NƠI>_<GIỜ>`), rồi tới nhãn,
# cuối cùng mới tới khối ÁNH SÁNG. Đừng quét toàn bộ prompt: chữ 'đêm' nằm rải
# trong phần tả đạo cụ và thoại, quét mù là thẻ ban ngày cũng ra 'tối'.
GIO_HAU_TO = {'DEM': 'tối', 'CHAPTOI': 'tối', 'KHUYA': 'tối', 'RANGSANG': 'tối',
              'NGAY': 'sáng', 'SANG': 'sáng', 'TRUA': 'sáng', 'CHIEU': 'sáng'}


def the_dia_diem(sf_id):
    """Leo `refs.bg` tới thẻ gốc (Location Card). Dừng ở nút cuối nếu không có."""
    f, seen = ALL.get(sf_id), set()
    while f and f['id'] not in seen:
        seen.add(f['id'])
        if f['id'].startswith('REF_BG_'):
            return f
        b = f['refs'].get('bg')
        if not b or b not in ALL:
            return f
        f = ALL[b]
    return None


def gio_cua_the(f):
    """'tối' · 'sáng' · None nếu thẻ không khai giờ ở đâu cả."""
    if not f:
        return None
    hau = f['id'].rsplit('_', 1)[-1].upper()
    if hau in GIO_HAU_TO:
        return GIO_HAU_TO[hau]
    for s in (f.get('label') or '', re.search(r'ÁNH SÁNG:[^\n]*', f.get('prompt') or '')):
        s = s.group(0) if hasattr(s, 'group') else s
        if not s:
            continue
        if RE_TOI.search(s): return 'tối'
        if RE_SANG.search(s): return 'sáng'
    return None


LOI = collections.Counter()
C = collections.Counter()
CANH_BAO = []          # lỗi mức nhắc, không tính vào mã thoát
CANH_BAO_HANH_DONG = [] # nhắc khi thoại có chứa mệnh lệnh thay đổi trạng thái
NHAC_PROP = []         # thoại nhắc tên đạo cụ — người đọc tự quyết có trong khung không
CHUA_ANH = []          # SF chưa có ảnh — TIẾN ĐỘ, không phải lỗi
DAI = []               # prompt vượt mục tiêu ~1.000 nhưng chưa tới mức hỏng
BANG = []              # scene đang ở giai đoạn BẢNG SHOT (chưa sinh SF)
POSE_CHUOI = []        # SF có `pose` kiểu CHUỖI → phép kiểm người-trong-phòng bỏ qua
nsf = nshot = giay = 0
scs = [s for s in d['scenes'] if s.get('shots') and s['id'] not in BO]
if a.scene:
    scs = [s for s in scs if s['id'] == a.scene]

# NÓI RÕ ĐÃ BỎ QUA SCENE NÀO — nếu không, `--bo` mặc định làm scene đang dở bị
# lặng lẽ loại rồi script in "✓ SẠCH", và người đọc tưởng cả phim đã sạch. Đã
# mắc đúng bẫy này 2026-08-07 với S6: báo sạch trong khi S6 có 21 lỗi.
_bo_that = sorted(s['id'] for s in d['scenes'] if s.get('shots') and s['id'] in BO)
if _bo_that:
    print(f"⚠ BỎ QUA {len(_bo_that)} scene có shot: {', '.join(_bo_that)}"
          f"  → thêm --bo \"\" để kiểm cả những scene này\n")

for sc in scs:
    # ---- MẬT ĐỘ MAIN CAST TRONG KHUNG ----------------------------------------
    # Scene có 3 người mà đa số khung chỉ có 2 thì khán giả mất dấu người thứ ba
    # giữa một cuộc đối chất. Đo trên S1 ngày 2026-08-21: 3 người 14% · 2 người 73%
    # — đúng ngược định mức, và sinh ra từ việc đọc luật 'chia để trị' thành 'xoá
    # người khỏi khung'.
    #
    # BẢN SAO O.S KHÔNG TÍNH VÀO CAST: clip quay lại người nói câu vọng/điện thoại
    # cố tình đứng MỘT MÌNH ở không gian khác (skill bước 1, 'Xử lý Thoại O.S').
    # Tính họ vào cast là biến cảnh điện thoại 2 người thành cảnh 3 người, rồi đòi
    # 60% khung phải có đủ ba — một yêu cầu KHÔNG THỂ đạt, và cách duy nhất để
    # 'đạt' nó là nhồi người vào khung cho vừa con số. Đã báo oan đúng kiểu đó với
    # S4 ngày 2026-08-22 (Maya · Owen ở vỉa hè + dược sĩ ở quầy thuốc).
    #
    # ĐO THEO CỤM KHÔNG GIAN, KHÔNG ĐO CẢ SCENE (sửa 2026-08-22). Bản cũ gộp cả
    # scene rồi đòi 60% khung phải có ĐỦ mặt mọi người từng xuất hiện trong đó.
    # Cảnh có người BƯỚC VÀO GIỮA CHỪNG là báo oan không cách nào chữa: S7 có
    # Ellis vào ở shot thứ chín, nên tám khung đầu KHÔNG THỂ có anh ta — và cách
    # duy nhất để 'đạt' con số là nhét anh ta vào phòng trước khi kịch bản cho
    # anh ta vào, đúng cái bẫy đã ghi ở đoạn bản sao O.S ngay trên.
    # Skill bước 1 chia scene thành CỤM KHÔNG GIAN, mỗi cụm một Master SF và một
    # thế trận riêng — cast đếm được là cast CỦA MỘT CỤM, không phải của scene.
    # Ranh giới cụm: mỗi Master SF mở một cụm mới (sfs vốn đã bắt buộc xếp theo
    # thứ tự thời gian, có phép kiểm riêng ở dưới).
    _sf_ban_sao = {x['sf'] for x in sc['shots'] if la_ban_sao_os(x)}
    _cum, _dang = [], []
    for f in sc['sfs']:
        if la_master(f) and _dang:
            _cum.append(_dang)
            _dang = []
        _dang.append(f)
    if _dang:
        _cum.append(_dang)
    for _nhom in _cum:
        khung = [f for f in _nhom if f['id'] not in _sf_ban_sao
                 and isinstance((f.get('pose') or {}).get('who'), dict)]
        cast = set()
        for f in khung:
            cast |= set(f['pose']['who'])
        if len(cast) < 3:
            continue
        ten_cum = next((f['id'] for f in _nhom if la_master(f)), _nhom[0]['id'])
        du   = sum(1 for f in khung if len(f['pose']['who']) >= len(cast))
        hai  = sum(1 for f in khung if len(f['pose']['who']) == 2)
        t = len(khung) or 1
        if du / t < 0.60:
            print(f"  ✗ {sc['id']} · cụm {ten_cum}: chỉ {du}/{t} SF ({du/t:.0%}) có đủ {len(cast)} main cast — đích ≥60%")
            LOI['thiếu-khung-đủ-cast'] += 1
        if hai / t > 0.20:
            print(f"  ✗ {sc['id']} · cụm {ten_cum}: {hai}/{t} SF ({hai/t:.0%}) chỉ có 2 người — trần 20%")
            LOI['quá-nhiều-khung-2-người'] += 1

    bad = []
    sh = sc['shots']
    load = collections.Counter(x['sf'] for x in sh)

    for f in sc['sfs']:
        i = f['id']
        # THẺ ĐỊA ĐIỂM được miễn các phép kiểm dưới: nó không có `refs.bg` (nó
        # LÀ gốc). Dấu hiệu là tiền tố `REF_BG_` hoặc `SF-M-` (quy ước cũ).
        if i.startswith('REF_BG_') or (i.startswith('SF-M-') and not f['refs'].get('bg')):
            # Cập nhật trần ký tự theo quy định mới: Thẻ địa điểm (1.400)
            _pr = f.get('prompt') or ''
            if len(_pr) > 1400:
                bad.append(('thẻ-địa-điểm-quá-dài', f"{i}: {len(_pr)} ký tự (trần 1.400)"))
            continue
        if f['refs'].get('bg') not in ALL:
            bad.append(('bg-hỏng', f"{i}: bg={f['refs'].get('bg')!r}"))

        # MỤC ĐÍCH: Kiểm tra SF con phải cùng cụm không gian với Master SF mà nó trỏ tới (zone của SF con phải khớp với zone của Master SF).
        _m = master(i)
        if _m and _m != i and _m in ALL and isinstance(f.get('pose'), dict):
            _zc = re.split(r'→', f['pose'].get('zone') or '')[0].strip().lower()
            _pm = ALL[_m].get('pose')
            _zm = re.split(r'→', (_pm or {}).get('zone') or '')[0].strip().lower() \
                if isinstance(_pm, dict) else ''
            if _zc and _zm and not (set(_zc.split()) <= set(_zm.split())
                                    or set(_zm.split()) <= set(_zc.split())):
                bad.append(('SF-trỏ-sai-cụm',
                            f"{i}: zone {_zc!r} nhưng master {_m} ở cụm {_zm!r}"))
        for c in f['refs']['chars']:
            if c not in ALL:
                bad.append(('ref-chết', f"{i}: {c}"))
        # MỤC ĐÍCH: Đếm số thẻ ref nhân vật (bỏ qua thẻ Master SF neo bối cảnh phụ trong khung gối đầu).
        ref_nhan_vat = [c for c in f['refs']['chars'] if not ('MASTER' in c or c.startswith('SF-'))]
        if len(ref_nhan_vat) > 8:
            bad.append(('quá-4-nhân-vật', f"{i}: {len(ref_nhan_vat)} ảnh ref nhân vật"))
        if not f.get('pose'):
            bad.append(('thiếu-pose', i))
        bad += loi_goc(i, goc_cua(i))
        # CHƯA CÓ ẢNH KHÔNG PHẢI LỖI — đó là TIẾN ĐỘ. Đếm riêng, in một dòng ở
        # cuối. Trộn nó vào danh sách lỗi thì nó chiếm 43% bảng và đẩy các lỗi
        # thật ra khỏi tầm mắt; bảng kiểm nhiễu thì người ta thôi đọc.
        if not co_anh(i):
            CHUA_ANH.append(i)
        if i not in load and i not in LA_NEO:
            bad.append(('SF-mồ-côi', i))
        pr = f.get('prompt') or ''
        # Trần ký tự: SF con < 1.000 ký tự, Master SF < 1.400 ký tự.
        is_master = 'MASTER' in i or (i.startswith('SF-M-') and f['refs'].get('bg'))
        limit = 1400 if is_master else 1000
        if len(pr) > limit:
            DAI.append(f"{i}: {len(pr)} (trần {limit})")
        # (Đã bỏ khối kiểm tra thiếu tiêu đề để viết tự nhiên hơn)
        # Trần "dưới 10 chữ KHÔNG": câu cấm nhiều quá thì model đọc thành nhiễu
        # và bắt đầu bỏ qua cả những câu cấm thật sự quan trọng.
        nk = len(re.findall(r'KHÔNG', pr))
        if nk >= 10:
            bad.append(('quá-10-chữ-KHÔNG', f"{i}: {nk} chữ KHÔNG"))
        # (Đã bỏ kiểm tra thông số máy quay cứng ngắc vì văn phong cinematic dùng mô tả tương đối như "ngang tầm mắt")

        # NGƯỜI CÒN TRONG PHÒNG MÀ VẮNG `goc` → model dựng căn phòng KHÔNG CÓ họ.
        # `người-nói-vắng-khung` không bắt được ca này: nó chỉ soi người CÓ THOẠI,
        # còn người nằm/ngồi im suốt cảnh thì không có câu nào để soi.
        # Đã trả giá 2026-08-07: S8 mất bà Nadine ở 9/17 khung của chính cảnh bên
        # giường bà, vì `goc` chỉ khai người NÉT và người làm vai/gáy tiền cảnh.
        # Ai ra khỏi khung thật thì xoá khỏi `pose.who` — sửa dữ liệu, đừng nới luật.
        #
        # `pose` CÓ HAI KIỂU trong cùng một file: chuỗi `zone · who · dist · hands`
        # (191 SF, bản cũ) và dict `{zone, who, dist, hands}` (17 SF của S8). Chỉ
        # kiểu dict khai tên người ở dạng máy đọc được, nên phép kiểm chỉ chạy trên
        # nó — và ĐẾM số SF bị bỏ qua để in ra, đừng bỏ qua im lặng: một phép kiểm
        # chỉ phủ 8% dữ liệu mà báo "SẠCH" thì tệ hơn không có phép kiểm nào.
        _pose = f.get('pose')
        _who = _pose.get('who') if isinstance(_pose, dict) else None
        if isinstance(_who, dict) and goc_cua(i).strip():
            vang_phong = [t for t in sorted(_who)
                          if not co_trong_goc(t, goc_cua(i))]
            if vang_phong:
                bad.append(('người-trong-phòng-vắng-goc', f"{i}: {', '.join(vang_phong)}"))
        elif _pose:
            POSE_CHUOI.append(i)
            
        # MỤC ĐÍCH: Kiểm tra Master SF bắt buộc phải dùng cỡ cảnh RỘNG (Wide Shot / Cinematic Wide) để bao quát 100% bối cảnh.
        if (la_master(f) or 'MASTER' in i or i.startswith('SF-M-')) and pr:
            c_co = cc(pr)
            if c_co != 'RỘNG' and not re.search(r'wide|toàn\s*cảnh|cinematic\s*wide', pr, re.I):
                bad.append(('master-thiếu-góc-rộng', f"{i}: Master SF nhưng cỡ cảnh là '{c_co}' (BẮT BUỘC phải dùng góc RỘNG / Wide Shot để bao quát 70%-100% bối cảnh gốc)"))

        # DƯ NGƯỜI TRONG PROMPT: Tên nhân vật nhắc trong prompt phải có trong `goc` hoặc `pose.who`
        if pr and isinstance(_who, dict):
            nguoi_trong_pr = [t for t in TEN_NV if re.search(r'\b' + re.escape(t) + r'\b', pr, re.I)]
            du_nguoi = [t for t in nguoi_trong_pr if t not in _who and not co_trong_goc(t, goc_cua(i))]
            if du_nguoi:
                bad.append(('dư-người-trong-prompt', f"{i}: {', '.join(du_nguoi)} có trong prompt nhưng không có trong pose/goc"))


    # GIAI ĐOẠN BẢNG SHOT: shots đã chốt nhưng chưa sinh SF nào ngoài thẻ địa
    # điểm. Đây là lúc kiểm ĐÁNG GIÁ NHẤT — sửa một ô trên bảng rẻ hơn sửa 17
    # prompt đã viết. Nhưng bản cũ báo 'SF-chết' cho MỌI shot rồi `continue`,
    # tức vừa phun nhiễu vừa bỏ luôn ba phép kiểm duy nhất chạy được lúc này:
    # giây · kiểu dur · luật 1:1. Nhận ra giai đoạn này thì bỏ SF-chết và chạy
    # tiếp phần không cần SF.
    _sf_that = {f['id'] for f in sc['sfs']
                if not (f['id'].startswith('REF_BG_') or f['id'].startswith('SF-M-') or 'MASTER' in f['id'])}
    giai_doan_bang = not _sf_that and len(sh) > 1
    if giai_doan_bang:
        BANG.append(f"{sc['id']} ({len(sh)} shot)")
        
    so_nguoi_phat_ngon = len({n for x in sh for n in nguoi_noi(x.get('text') or '')})
    noi_truc_tiep = so_nguoi_phat_ngon >= 2
    co_ots = False
    # CẢNH ĐIỆN THOẠI: đọc từ `goc` + prompt SF, KHÔNG chỉ prompt video.
    # Hai phép kiểm dựa vào cờ này (thiếu-OTS · khung-1-người) chạy ngay từ bước 3,
    # còn prompt video mãi bước 4 mới có — nên bản cũ LUÔN ra False đúng lúc cần
    # nó nhất. S8 và S12 là hai cảnh điện thoại hai đầu dây, mỗi đầu một mình,
    # không dựng OTS được; chính ghi chú trong shot của S8 đã ghi là phép kiểm
    # phải tự tắt, mà nó không tắt. `goc` có từ bước 1, sớm nhất trong ba nguồn.
    # ĐẾM TỶ LỆ chứ không dùng any(): một shot lẻ có người nhấc máy (S9 gọi kiểm
    # tra người tham chiếu) KHÔNG được phép tắt phép kiểm OTS của cả cảnh
    # mặt-đối-mặt.
    def _co_dien_thoai(x):
        nguon = ((x.get('goc') or '') + '\n' + (x.get('prompt') or '') + '\n'
                 + ((ALL.get(x['sf']) or {}).get('prompt') or ''))
        return bool(re.search(r'ống\s*nghe|điện\s*thoại|đầu\s*dây|phone', nguon, re.I))
    is_scene_phone = bool(sh) and sum(map(_co_dien_thoai, sh)) / len(sh) >= 0.5

    for k, x in enumerate(sh):
        co_sf = x['sf'] in ALL
        if not co_sf and not giai_doan_bang:
            bad.append(('SF-chết', f"{x['id']} → {x['sf']}")); continue
        if co_sf:
            C[cc(ALL[x['sf']]['prompt'])] += 1
        pv = x.get('prompt') or ''
        if k and sh[k - 1]['sf'] == x['sf']:
            bad.append(('SF-lặp-kề', f"{x['id']} dùng lại {x['sf']} của shot trước"))
        w = 0 if '[NHỊP' in x['text'] else dem_tu(x['text'])
        can = w / 3 + (2 if 'KẾT CLIP' in pv else 0)
        # Skill cho phép tràn xấp xỉ 0,5s; dùng đúng biên đó để không báo oan
        # các câu chỉ vượt 1 từ ở tốc độ 3 từ/giây.
        if x['dur'] < can - 0.5:
            bad.append(('thiếu-giây', f"{x['id']}: {w} từ cần {can:.1f}s, đang {x['dur']}"))

        # MỤC ĐÍCH: Kiểm tra nhịp mang lời dẫn (NARRATOR:) phải đủ thời lượng (giây) đọc và lời dẫn không lọt vào prompt video.
        # `w = 0` ở trên tắt phép kiểm giây cho mọi shot [NHỊP] — đúng với nhịp câm,
        # nhưng nhịp CHÍNH LÀ nơi voiceover sống trong phim hook. Không kiểm thì lời
        # dẫn 24 từ bị nhét vào clip 4 giây và người dựng phát hiện lúc đã render.
        _nar = re.search(r'^\s*NARRATOR:\s*(.+)$', x['text'] or '', re.M | re.S)
        if _nar:
            _wn = len(re.findall(r"[A-Za-z']+", _nar.group(1)))
            if x['dur'] < _wn / 3 - 0.5:
                bad.append(('nhịp-thiếu-giây-cho-lời-dẫn',
                            f"{x['id']}: lời dẫn {_wn} từ cần {_wn/3:.1f}s, đang {x['dur']}s"))
            if 'NARRATOR' in (x.get('prompt') or ''):
                bad.append(('lời-dẫn-lọt-prompt-video', x['id']))
        if not isinstance(x['dur'], int):
            bad.append(('dur-sai-kiểu', f"{x['id']}: {x['dur']!r}"))
        # OTS ĐƯỢC KHAI Ở `goc` CỦA SHOT, KHÔNG PHỤ THUỘC SF — nên phải đếm ở
        # ngoài nhánh `co_sf` dưới đây. Bản cũ đếm bên trong nhánh đó, mà ở giai
        # đoạn BẢNG SHOT chưa SF nào tồn tại nên `co_ots` không bao giờ bật:
        # mọi scene đều ăn `thiếu-OTS` kể cả khi từng dòng `goc` đã ghi rõ OTS.
        # Đúng lúc bảng shot là lúc phép kiểm này đáng giá nhất thì nó báo oan.
        if '[NHỊP' not in x['text'] and RE_OTS.search(x.get('goc') or goc_cua(x['sf'])):
            co_ots = True

        # NGƯỜI NÓI CÓ TRONG KHUNG KHÔNG — chỉ hỏi được khi `goc` tồn tại.
        # SF không có `goc` thì mọi người nói đều "vắng khung", và bảng kiểm
        # phun ra hàng trăm dòng vô nghĩa che mất lỗi thật (đã đo: 325 dòng trên
        # một phim cũ). Thiếu `goc` đã có lỗi riêng ở trên; đừng đếm hai lần.
        if co_sf and '[NHỊP' not in x['text'] and (x.get('goc') or goc_cua(x['sf'])).strip():
            f = ALL[x['sf']]
            vang = [ten for ten in sorted(nguoi_noi(x['text']))
                    if not co_trong_goc(ten, x.get('goc') or goc_cua(x['sf']))
                    and not offscreen_hop_le(ten, x['text'], pv)]
            if vang:
                bad.append(('người-nói-vắng-khung',
                            f"{x['id']} → {x['sf']}: {', '.join(vang)}"))
            
            # Khung 1 người sai luật
            _who = (ALL[x['sf']].get('pose') or {}).get('who') if isinstance(ALL[x['sf']].get('pose'), dict) else None
            _sf_speakers = nguoi_noi(x['text'] or '')
            is_offscreen = any(offscreen_hop_le(ten, x.get('text', ''), pv) for ten in _sf_speakers)
            if noi_truc_tiep and len(_sf_speakers) > 0 and not is_offscreen and _who and len(_who) == 1 and not is_scene_phone and not la_ban_sao_os(x):
                bad.append(('khung-1-người-sai-luật', f"{x['id']}: thoại trực tiếp nhưng pose.who chỉ có 1 người"))
                
        # THIẾU REF_PROP — hỏi "đạo cụ có TRONG KHUNG không", chứ không phải "có
        # ai NHẮC TỚI nó không". Bản cũ quét cả dòng thoại nên báo oan kiểu không
        # thể chữa: Maya kể cái thùng máy giặt còn nằm lại trong cửa hàng
        # (V-S8-09) trong lúc cô đứng ở cầu thang bộ, và kể cho con nghe về "a
        # polite one. With a pen." (V-S6-06) ở bàn bếp. Đính REF_PROP cho hai
        # khung ấy là bắt model dựng cái thùng vào cầu thang — cách duy nhất để
        # "hết lỗi" lại chính là cách làm hỏng đúng cái ảnh.
        # Chỉ phần MÔ TẢ KHUNG mới tính là lỗi; nhắc trong thoại hạ xuống mức
        # nhắc và in riêng ở cuối, để tín hiệu không mất chứ không thành lỗi.
        # PROMPT VIDEO CŨNG CHỨA THOẠI — chép nguyên văn vào trong dấu nháy kép
        # (`MAYA — warm: "A polite one. With a pen."`). Bóc dòng thoại khỏi `text`
        # rồi quên bóc khỏi `pv` thì cái bẫy cũ quay lại y nguyên qua lối thứ hai:
        # V-S6-06 lại ăn 'thiếu-REF-PROP' ngay khi bước 4 viết xong. Trong prompt
        # video, thoại LUÔN nằm trong dấu nháy kép, nên bóc theo dấu nháy là đủ và
        # chính xác — phần mô tả khung không bao giờ nằm trong nháy.
        _mo_ta = (RE_DONG_THOAI.sub('', x.get('text') or '') + '\n'
                  + (x.get('goc') or '') + '\n' + re.sub(r'"[^"]*"', ' ', pv))
        _thoai = RE_DONG_THOAI.findall(x.get('text') or '')
        for prop_name in TEN_PROP:
            _re_prop = re.compile(r'\b' + re.escape(prop_name) + r'\b', re.I)
            if co_sf and any(c.startswith('REF_PROP_')
                             and prop_name in c[9:].lower().replace('_', ' ')
                             for c in ALL[x['sf']]['refs']['chars']):
                continue
            if _re_prop.search(_mo_ta):
                if co_sf:
                    bad.append(('thiếu-REF-PROP',
                                f"{x['id']}: khung có '{prop_name}' nhưng không đính ảnh REF_PROP"))
            elif any(_re_prop.search(t) for t in _thoai):
                NHAC_PROP.append(f"{sc['id']:5} {x['id']:11} thoại nhắc '{prop_name}'"
                                 f" — chỉ đính REF_PROP nếu khung thật sự thấy món đó")
        if not pv:
            continue          # chưa viết prompt video — các phép dưới chưa áp được
        # Bước 5 CẤM viết tên file vào prompt video (Grok không hiểu chuỗi đó) —
        # nên phép kiểm là NGƯỢC: prompt phải SẠCH mã nội bộ, và đủ ngắn.
        if 'REFS ·' in pv or 'REF_' in pv or 'Start frame:' in pv:
            bad.append(('còn-mã-nội-bộ', x['id']))
        # TRẦN 1.400 (nới từ 1.000 ngày 2026-08-11). Form prompt video ở
        # `4-prompt-video.md` đã đổi: khối `Nhận diện` chuyển sang gạch đầu dòng có
        # nhân dạng đầy đủ, thêm dòng "Chỉ X nói. Y im lặng." và câu cấm camera lùi.
        # Đo trên form mới: 2 người ~1.030 · 3 người ~1.150 · 4 người ~1.275 ký tự —
        # tức trần cũ bắt lỗi mọi prompt đúng form. Giữ trần để chặn prompt phình
        # thật sự, nhưng đặt ở mức form mới vừa đủ thở.
        if '[NHỊP' not in x['text'] and len(pv) > 1400:
            bad.append(('prompt-quá-dài', f"{x['id']}: {len(pv)} ký tự (trần 1.400)"))
        if '[NHỊP' in x['text'] and not (x.get('music') or {}).get('a'):
            bad.append(('nhịp-thiếu-nhạc', x['id']))
        # MỤC ĐÍCH: Cho phép góc rộng mở rộng đến 20-25% và dùng thoại khi hợp lý (thiết lập bối cảnh nhóm/di chuyển).
        # Không bắt lỗi thoại-trên-khung-rộng cứng để tăng tính linh hoạt cho góc rộng.
        # CẢNH BÁO: Hành động thay đổi trạng thái trong thoại
        # Nếu thoại chứa các cụm lệnh kinh điển, phải nhắc người duyệt kiểm tra SF
        RE_HANH_DONG = re.compile(r'\b(?:open up|open the door|sit|sit down|stand up|let me in|give it to me)\b', re.I)
        hd_match = RE_HANH_DONG.search(x.get('text') or '')
        if hd_match:
            CANH_BAO_HANH_DONG.append(f"{sc['id']:5} {x['id']:11} Thoại lệnh '{hd_match.group(0)}' → Đảm bảo SF vẽ trạng thái CHƯA LÀM (vd: cửa đóng, đang đứng...).")

        # MỤC ĐÍCH: Kiểm tra các luật tinh chỉnh Prompt Video (Nhận diện tối giản, từ cấm phụ kiện/vùng dưới, cấm câu phủ định camera, khớp dur).
        # MỤC ĐÍCH: Kiểm tra các luật tinh chỉnh Prompt Video (Nhận diện tối giản, từ cấm phụ kiện/vùng dưới, cấm câu phủ định camera, khớp dur, đối chiếu pose.who).
        if pv:
            # Bullet nhận diện: sửa regex để nhận cả tên viết hoa lẫn thường (E)
            bullets = re.findall(r'^\s*-\s*([A-Za-zÀ-ỹ][A-Za-zÀ-ỹ0-9_ ]*?)\s*=\s*(.+)$', pv, re.M)
            if bullets:
                for nv_name, nv_desc in bullets:
                    line_full = f"- {nv_name} = {nv_desc}"
                    if len(line_full) > 80:
                        bad.append(('bullet-nhận-diện-quá-dài', f"{x['id']}: bullet '{nv_name}' {len(line_full)} ký tự (trần 80)"))
                    
                    # Từ cấm phụ kiện/vùng dưới và loại áo cụ thể (chỉ cho phép ghi màu áo: 'áo màu X')
                    RE_TU_CAM_ND = re.compile(r'\b(?:tất|vớ|giày|dép|quần|thắt\s*lưng|đồng\s*hồ|nhẫn|khuyên|ba\s*lô|túi|cà\s*vạt|sơ\s*mi|thun|polo|blazer|cardigan|sweater|hoodie|nỉ|len)\b', re.I)
                    m_cam = RE_TU_CAM_ND.search(nv_desc)
                    if m_cam:
                        bad.append(('nhận-diện-chứa-từ-cấm', f"{x['id']}: bullet '{nv_name}' chứa loại áo/từ cấm '{m_cam.group(0)}' (chỉ ghi màu áo: 'áo màu X')"))
                    
                    if 'rõ mặt' in nv_desc.lower():
                        bad.append(('nhận-diện-thừa-rõ-mặt', f"{x['id']}: bullet '{nv_name}' chứa từ thừa 'rõ mặt' (nhân vật chính không cần ghi rõ mặt)"))

                    # MỤC ĐÍCH: Khuyến nghị thêm cụm ', im như tượng' cho nhân vật mờ ở tiền cảnh để khóa chuyển động xoay mặt
                    if 'mờ' in nv_desc.lower() and 'im như tượng' not in nv_desc.lower():
                        CANH_BAO.append(f"{sc['id']:5} {x['id']:11} bullet '{nv_name}' mờ tiền cảnh — nên thêm ', im như tượng' để khóa chuyển động xoay mặt")


                # MỤC ĐÍCH (G): Đối chiếu khối Nhận diện của shot với pose.who của SF nó đang dùng (tập tên người & cờ mờ ở khung hình).
                if co_sf and isinstance((ALL[x['sf']].get('pose') or {}).get('who'), dict):
                    who_dict = ALL[x['sf']]['pose']['who']
                    bullet_map = {b[0].strip().upper(): b[1].strip() for b in bullets}
                    who_map_upper = {k.upper(): (k, v) for k, v in who_dict.items()}
                    
                    if set(bullet_map.keys()) != set(who_map_upper.keys()):
                        bad.append(('nhận-diện-lệch-SF', f"{x['id']} → {x['sf']}: người trong Nhận diện ({list(bullet_map.keys())}) không khớp pose.who ({list(who_map_upper.keys())})"))
                    else:
                        for k_upper, (orig_name, pose_desc) in who_map_upper.items():
                            b_desc = bullet_map.get(k_upper, '')
                            # `pose.who` TOÀN BỘ board có thể để trống chuỗi (chỉ dùng
                            # làm danh sách tên) — khi đó vai trò khung hình nằm ở `goc`,
                            # và đọc mỗi pose.who thì phép so LUÔN ra 'nét', báo oan mọi
                            # bullet khai đúng cờ mờ. Trống thì tra `goc` của chính SF ấy.
                            if str(pose_desc).strip():
                                is_pose_mo = bool(re.search(r'out\s*nét|mờ|rìa|ngoài\s*khung|sau\s*lưng', str(pose_desc), re.I))
                            else:
                                is_pose_mo = mo_theo_goc(orig_name, ALL[x['sf']].get('goc') or '')
                            is_bullet_mo = bool(re.search(r'mờ', b_desc, re.I))
                            if is_pose_mo and not is_bullet_mo:
                                bad.append(('nhận-diện-lệch-SF', f"{x['id']}: '{orig_name}' out nét/mờ ở pose.who nhưng bullet Nhận diện thiếu cờ 'mờ ở khung hình'"))
                            elif not is_pose_mo and is_bullet_mo:
                                bad.append(('nhận-diện-lệch-SF', f"{x['id']}: '{orig_name}' nét ở pose.who nhưng bullet Nhận diện bị gán cờ 'mờ ở khung hình'"))

            # MỤC ĐÍCH (F): Kiểm tra nhãn thoại không được chứa từ vị trí/khung hình (off-screen, O.S., ngoài khung...) khi nhân vật có mặt trong khung.
            for m_tb in re.finditer(r'^\s*([A-Za-zÀ-ỹ0-9_ ]+?)\s*—\s*([^:\n]{1,60}):\s*"', pv, re.M):
                spk_name, emo_label = m_tb.group(1).strip(), m_tb.group(2).strip()
                RE_POS_LABEL = re.compile(r'\b(?:off[- ]?screen|o\.s\.|ngoài\s*khung|khuất\s*mặt|sau\s*lưng|chỉ\s*thấy\s*vai)\b', re.I)
                if RE_POS_LABEL.search(emo_label) and not re.search(r'điện\s*thoại|loa', emo_label, re.I):
                    bad.append(('nhãn-off-screen-sai-khung', f"{x['id']}: nhãn thoại của '{spk_name}' chứa từ vị trí/khung hình '{emo_label}' (chỉ khai mờ ở khung hình ở khối Nhận diện)"))

            # Cấm các cụm từ phủ định camera
            RE_PHU_DINH_CAM = re.compile(r'back to camera|không ai nhìn về camera|never turning to face|quay lưng về phía camera', re.I)
            m_pd = RE_PHU_DINH_CAM.search(pv)
            if m_pd:
                bad.append(('cấm-phủ-định-camera', f"{x['id']}: chứa cụm phủ định camera '{m_pd.group(0)}'"))

            # Kiểm tra con số giây dur khớp với câu khóa prompt video
            m_dur = re.search(r'Một shot liền\s+(?:duy nhất\s+)?(\d+)\s*giây', pv, re.I)
            if m_dur:
                pv_giay = int(m_dur.group(1))
                if pv_giay != x['dur']:
                    bad.append(('dur-lệch-câu-khóa', f"{x['id']}: dur={x['dur']}s nhưng prompt ghi '{pv_giay} giây'"))


        # NHÃN CẢM XÚC CẤM — hai mức, vì hai file skill từng khai phạm vi khác
        # nhau (SKILL.md cấm không điều kiện · 4-prompt-video.md chỉ cấm khi có
        # trẻ trong khung). Thống nhất 2026-08-07: có trẻ = LỖI, toàn người lớn
        # = CẢNH BÁO cho user tự quyết, vì cảnh người lớn đôi khi cần đúng sắc đó.
        for nhan, w in nhan_cam_xuc(pv):
            if co_tre_em(x['sf'], x['prompt']):
                bad.append(('nhãn-cấm-CÓ-TRẺ', f"{x['id']}: \"{nhan}\" ← {w}"))
            else:
                CANH_BAO.append(f"{sc['id']:5} {x['id']:11} \"{nhan}\" ← {w}")

    # THIẾU OTS
    if noi_truc_tiep and len(sh) >= 3 and not co_ots and not is_scene_phone:
        bad.append(('thiếu-OTS', f"{sc['id']}: cụm thoại trực tiếp >=3 shot nhưng không có khung OTS nào"))

    # MỤC ĐÍCH: Cho phép tái sử dụng SF khoảng 20-25% toàn dự án (scene thoại đảo góc có thể đạt 30-50%).
    # Cảnh báo nếu một SF bị lạm dụng gánh quá 5 shot hoặc tỷ lệ tái sử dụng vượt ngưỡng 50% trong scene.
    so_shot_dung_lai = sum(v - 1 for v in load.values() if v > 1)
    ty_le_reuse = (so_shot_dung_lai / max(len(sh), 1)) * 100
    if ty_le_reuse > 50.0:
        bad.append(('tái-sử-dụng-SF-quá-nhiều', f"{sc['id']}: dùng lại SF {ty_le_reuse:.1f}% shot (trần 50% cho scene)"))
    for k, v in load.items():
        if v > 5:
            bad.append(('SF-gánh-nhiều-shot', f"{k}: gánh {v} shot (nên <= 5 shot)"))

    # MỤC ĐÍCH: Đảm bảo thành phần tái sử dụng cân bằng (OTS+cận không dồn quá 60%, cần dùng lại two-shot và master).
    seen_sf_in_scene = set()
    re_ots = 0
    re_wide = 0
    for x in sh:
        sf_id = x['sf']
        if sf_id in seen_sf_in_scene:
            f = ALL.get(sf_id, {})
            c_co = cc(f.get('prompt') or '')
            is_ots = bool(RE_OTS.search(x.get('goc') or goc_cua(sf_id)))
            if c_co in ('RỘNG', 'trung-rộng') or la_master(f) or 'two-shot' in (x.get('goc') or '').lower():
                re_wide += 1
            else:
                re_ots += 1
        else:
            seen_sf_in_scene.add(sf_id)
    if (re_ots + re_wide) >= 4 and (re_ots / max(re_ots + re_wide, 1)) > 0.60:
        bad.append(('tái-sử-dụng-dồn-vào-OTS', f"{sc['id']}: {re_ots}/{re_ots+re_wide} shot dùng lại ({re_ots/(re_ots+re_wide):.0%}) dồn vào OTS+cận (trần 60%, cần dùng lại two-shot và master)"))

    # KIỂM TRA THỨ TỰ THỜI GIAN CỦA SF (Chronological order)
    # Mục đích: Đảm bảo các SF trong mảng sfs được sắp xếp đúng theo thứ tự thời gian xuất hiện của chúng trong video.
    # Phát hiện lỗi gom các Master SF lên đầu mảng nếu thực tế chúng xuất hiện ở giữa hoặc cuối cảnh.
    first_shot_idx = {}
    for idx, x in enumerate(sh):
        if x['sf'] not in first_shot_idx:
            first_shot_idx[x['sf']] = idx
            
    sfs_in_order = [f['id'] for f in sc['sfs'] if f['id'] in first_shot_idx]
    
    for k in range(len(sfs_in_order) - 1):
        if first_shot_idx[sfs_in_order[k]] > first_shot_idx[sfs_in_order[k+1]]:
            sf1 = sfs_in_order[k]
            sf2 = sfs_in_order[k+1]
            if 'MASTER' in sf1 or (sf1.startswith('SF-M-') and ALL.get(sf1, {}).get('refs', {}).get('bg')):
                bad.append(('SF-Master-sai-thứ-tự', f"{sf1} đứng trước {sf2} nhưng xuất hiện sau trong mạch shot"))
            else:
                bad.append(('SF-sai-thứ-tự-thời-gian', f"{sf1} đứng trước {sf2} nhưng xuất hiện sau trong mạch shot"))

    nsf += len(load); nshot += len(sh); giay += sum(x['dur'] for x in sh)
    for t, _ in bad:
        LOI[t] += 1
    # MỤC ĐÍCH: Hiển thị thống kê số lượng SF, shot và tỷ lệ tái sử dụng SF trong cảnh.
    rate_str = f" [Dùng lại SF: {so_shot_dung_lai}/{len(sh)} ({ty_le_reuse:.0f}%)]" if so_shot_dung_lai > 0 else ""
    print(f"{'✓' if not bad else '✗'} {sc['id']:5}{len(load):3} SF {len(sh):3} shot{rate_str}")
    for t, m in bad:
        print(f"      ✗ {t:22} {m}")

# ---- NHÃN HIỆU: bề mặt mang chữ phải được khoá là hư cấu ------------------
RE_HANGHOA = re.compile(
    r'thùng carton|thùng hàng|thùng rác|xe đẩy hàng|tủ điện|bình chữa cháy|máy giặt|máy sấy|tủ lạnh|tivi|màn hình|lò vi sóng'
    r'|lò nướng|máy hút bụi|máy pha cà phê|hộp thuốc|máy tính|laptop|điện thoại'
    r'|xe hơi|sedan|bao bì|vỏ hộp', re.I)
RE_KHOA_NHAN = re.compile(r'hư cấu|làm mờ|không.{0,25}thương hiệu có thật', re.I)
RE_BRAND = re.compile(
    r'\b(samsung|lg|sony|panasonic|toshiba|whirlpool|maytag|kenmore|frigidaire'
    r'|bosch|lenovo|dell|apple|iphone|macbook|nike|adidas|coca[- ]?cola|pepsi'
    r'|toyota|honda|ford|chevrolet|bmw|mercedes)\b', re.I)

# MỤC ĐÍCH: Đảm bảo các khung hình ngoại cảnh có lòng đường/ngã tư bắt buộc phải khai báo xe cộ di chuyển hoặc đỗ lề đường, tránh biến mặt đường thành phố đi bộ hoang vắng.
RE_CO_DUONG = re.compile(r'lòng đường|mặt đường|ngã tư|làn xe|bãi đỗ', re.I)
RE_CO_XE = re.compile(
    r'(ô tô|xe hơi|sedan|xe tải|xe bán tải|taxi|xe buýt|xe máy|xe đạp)[^.\n]{0,40}?'
    r'(chạy|di chuyển|lăn bánh|đỗ|dừng|nối đuôi)'
    r'|(đỗ|dừng)[^.\n]{0,20}?(sát lề|ven đường|dọc lề)', re.I)

print('\n── TỪ KHOÁ NHÃN HIỆU & THƯƠNG HIỆU CÓ THẬT ──')
loi_nhan = 0
for i, f in ALL.items():
    pr = f.get('prompt') or ''
    if not pr: continue
    m = RE_BRAND.search(pr)
    if m:
        print(f"  ✗ {i:28} Cảnh báo có thương hiệu thật '{m.group(0)}' lọt vào prompt")
        loi_nhan += 1
        LOI['thương-hiệu-có-thật'] += 1
    elif RE_HANGHOA.search(pr) and not RE_KHOA_NHAN.search(pr):
        print(f"  ✗ {i:28} Có hàng hoá/thiết bị nhưng chưa khoá nhãn hư cấu")
        loi_nhan += 1
        LOI['nhãn-chưa-khoá'] += 1
    if RE_CO_DUONG.search(pr) and not RE_CO_XE.search(pr):
        print(f"  ✗ {i:28} Có lòng đường/mặt đường nhưng chưa khai báo xe cộ đỗ/chạy")
        loi_nhan += 1
        LOI['ngoại-cảnh-phố-vắng-xe'] += 1
if not loi_nhan:
    print('  ✓ không có')

# mối nối + đổi không gian
print('\n── ĐỔI KHÔNG GIAN KHÔNG CÓ NHỊP LẶNG ──')
allsh = [(s['id'], x) for s in d['scenes'] if s.get('shots') for x in s['shots']]
hong = loi_nhan
for (sa, x), (sb, y) in zip(allsh, allsh[1:]):
    ma, mb = master(x['sf']), master(y['sf'])
    if ma == mb or ma is None or mb is None:
        continue
    # ĐỔI MASTER KHÔNG PHẢI LÀ ĐỔI KHÔNG GIAN. Skill bước 1 bắt mở Master SF mới
    # mỗi khi THẾ TRẬN đổi — người thứ ba bước vào, cả nhóm xoay 180 độ — kể cả
    # khi không ai rời khỏi chỗ cũ. Bản cũ so mã Master nên coi mọi lần đổi thế
    # trận là đổi cảnh và đòi chèn nhịp lặng vào giữa: S13 (ông cụ đứng vào hàng
    # ngay sau lưng Maya) và S14 (bà Holt bước ra sau vai con gái) đều bị đòi,
    # mà chèn nhịp ở đó là cắt ngang đúng nhịp căng nhất của cảnh.
    # Phép kiểm này tên là ĐỔI KHÔNG GIAN thì phải hỏi đúng câu đó: hai Master
    # có leo về cùng một THẺ ĐỊA ĐIỂM không. Cú nhảy vị trí trong cùng một phòng
    # đã có `kiem-noi-shot.py` gác bằng bốn trục zone/who/dist/hands, chính xác
    # hơn nhiều — không cần gác hai lần bằng một phép kiểm thô hơn.
    _na, _nb = the_dia_diem(x['sf']), the_dia_diem(y['sf'])
    if _na is not None and _na is _nb:
        continue
    if '[NHỊP' in x['text'] or '[NHỊP' in y['text']:
        continue
    # Bản sao O.S: cắt sang chỗ người nói câu vọng rồi cắt về — không phải đổi cảnh.
    if la_ban_sao_os(x) or la_ban_sao_os(y):
        continue
    # Miễn nếu là điện thoại (cắt qua lại hai không gian)
    if sa == sb:
        is_phone_x = re.search(r'ống\s*nghe|điện\s*thoại|đầu\s*dây|phone', x.get('prompt') or '', re.I)
        is_phone_y = re.search(r'ống\s*nghe|điện\s*thoại|đầu\s*dây|phone', y.get('prompt') or '', re.I)
        if is_phone_x or is_phone_y:
            continue
    k = ' 🔒' if (sa in BO or sb in BO) else ''
    print(f"  ✗ {x['id']:11} {str(ma)[5:]:14}→ {y['id']:11} {str(mb)[5:]:14}"
          f"{'(trong lòng %s)' % sa if sa == sb else '(mối %s→%s)' % (sa, sb)}{k}")
    hong += 1
    LOI['thiếu-nhịp-chuyển-cảnh'] += 1
if not hong:
    print('  ✓ không có')

# ---- CẤP PHIM (a): CHUỖI SCENE TỐI -----------------------------------------
# 'Không quá 2 scene tối liền nhau' — scene tên 'đêm tệ nhất' chỉ tệ khi quanh
# nó có ngày. Giờ của một scene lấy từ thẻ địa điểm mà SF của nó trỏ vào; scene
# dùng nhiều thẻ mà có MỘT thẻ ban ngày thì tính là sáng, vì chỉ cần một nhịp
# sáng là mạch đã bị cắt.
KHONG_RO_GIO = []
if not a.scene:
    print('\n── CHUỖI SCENE TỐI LIỀN NHAU (trần: 2) ──')
    chuoi = []
    for sc in [s for s in d['scenes'] if s.get('shots') and s['id'] not in BO]:
        the = {(the_dia_diem(f['id']) or {}).get('id') for f in sc['sfs']} - {None}
        gio = {gio_cua_the(ALL.get(t)) for t in the} - {None}
        if not gio:
            KHONG_RO_GIO.append(f"{sc['id']} (thẻ {', '.join(sorted(the)) or '—'})")
        chuoi.append((sc['id'], 'sáng' if 'sáng' in gio else ('tối' if gio else None)))
    run = []
    qua_dai = 0
    for sid, g in chuoi + [(None, None)]:
        if g == 'tối':
            run.append(sid); continue
        if len(run) > 2:
            print(f"  ✗ {len(run)} scene tối liền: {' → '.join(run)}"
                  f"   → cắt mạch bằng một cảnh giờ hành chính")
            qua_dai += 1
        run = []
    if not qua_dai:
        print('  ✓ không có')
    hong += qua_dai

# ---- CẤP PHIM (b): TRANG PHỤC — `desc` NÓI MỘT ĐẰNG, `refs.chars` MỘT NẺO ----
# Thẻ `REF_*_FULL` khai scene nào mặc bộ này bằng MỘT DÒNG máy đọc được:
#     Dùng: S4 · S5 · S8 · S9
# Bắt buộc phải là dòng riêng đúng dạng đó, KHÔNG quét `S\d+` trong văn xuôi:
# desc hay nhắc scene trong vế PHỦ ĐỊNH ('S10 dùng bộ RAIN', 'bộ HOME để riêng
# cho S16-S17') nên quét mù thì mỗi thẻ tự nhận luôn cả scene của thẻ khác.
# Thẻ không có dòng đó thì KHÔNG kiểm — và phải đếm ra, đừng bỏ qua im lặng.
RE_DUNG = re.compile(r'^\s*Dùng:\s*(.+)$', re.M)
THIEU_DUNG = []
if not a.scene:
    print('\n── TRANG PHỤC: `desc` thẻ REF vs `refs.chars` thật ──')
    dung_that = collections.defaultdict(set)
    for s in d['scenes']:
        if s['id'] in BO:
            continue
        for f in s.get('sfs', []):
            for c in f['refs']['chars']:
                if c.endswith('_FULL'):
                    dung_that[c].add(s['id'])
    lech = 0
    for f in ALL.values():
        if not f['id'].endswith('_FULL'):
            continue
        m = RE_DUNG.search(f.get('desc') or '')
        if not m:
            THIEU_DUNG.append(f['id']); continue
        khai = set(re.findall(r'\bS\d+\b', m.group(1)))
        that = dung_that.get(f['id'], set())
        if khai - that:
            print(f"  ✗ {f['id']:28} desc nhận {' · '.join(sorted(khai - that, key=lambda z: int(z[1:])))} "
                  f"nhưng KHÔNG SF nào của scene đó đính")
            lech += 1
        if that - khai:
            print(f"  ✗ {f['id']:28} SF của {' · '.join(sorted(that - khai, key=lambda z: int(z[1:])))} "
                  f"đang đính nhưng desc KHÔNG nhận")
            lech += 1
    if not lech:
        print('  ✓ không có')
    hong += lech

# MỤC ĐÍCH: Phép kiểm trang phục theo CHỨC VỤ — phát hiện thẻ REF FULL của nhân vật mang chức danh thiết chế (thẩm phán, bác sĩ, cảnh sát...) nhưng prompt thiếu y phục nghi thức/chuyên môn tương ứng.
MAU_CHUC_VU = {
    r'thẩm\s*phán|chủ\s*tọa|hội\s*thẩm|chủ\s*tịch\s*hội\s*đồng|judge|chairman': (r'áo\s*choàng|robe|lễ\s*phục', 'áo choàng/lễ phục'),
    r'bác\s*sĩ|dược\s*sĩ|y\s*tá|doctor|nurse': (r'blouse|áo\s*blouse|đồ\s*mổ|scrubs', 'áo blouse/đồ mổ'),
    r'cảnh\s*sát|police|officer': (r'đồng\s*phục\s*cảnh\s*sát|police\s*uniform', 'đồng phục cảnh sát'),
    r'lính\s*cứu\s*hỏa|firefighter': (r'đồ\s*bảo\s*hộ|đồng\s*phục', 'đồ bảo hộ/đồng phục'),
    r'linh\s*mục|giáo\s*sĩ|priest': (r'áo\s*dòng|lễ\s*phục', 'áo dòng/lễ phục'),
}
THIEU_Y_PHUC = []
for f in ALL.values():
    if f['id'].endswith('_FULL'):
        lbl = (f.get('label') or '') + ' ' + (f.get('desc') or '')
        _port_id = f['id'].replace('_FULL', '_PORTRAIT')
        if _port_id in ALL:
            lbl += ' ' + (ALL[_port_id].get('label') or '') + ' ' + (ALL[_port_id].get('desc') or '')
        pr = f.get('prompt') or ''
        for pat_cv, (pat_yp, ten_yp) in MAU_CHUC_VU.items():
            if re.search(r'\b(?:' + pat_cv + r')\b', lbl, re.I):
                if not re.search(r'\b(?:' + pat_yp + r')\b', pr, re.I):
                    THIEU_Y_PHUC.append((f['id'], ten_yp))

if THIEU_Y_PHUC:
    print('\n── TRANG PHỤC SAI CHỨC VỤ (Y PHỤC THIẾT CHẾ) ──')
    for fid, typ in THIEU_Y_PHUC:
        print(f"  ✗ {fid}: vai mang chức danh thiết chế nhưng prompt thiếu {typ}")
        LOI['trang-phục-sai-chức-vụ'] += 1

# Tỷ lệ cỡ cảnh chỉ có nghĩa khi ĐA SỐ shot đã có SF. Ở giai đoạn bảng shot mới
# có 1-2 SF nên tỷ lệ ra 100% cho một loại — con số đúng về số học nhưng đọc ra
# thì sai hẳn, và một dòng thống kê đánh lừa cũng tệ như một lỗi báo oan.
t = sum(C.values()) or 1
# MỤC ĐÍCH: Thống kê tổng quan số SF, shot, thời lượng và tỷ lệ tái sử dụng SF toàn bộ kịch bản.
n_reuse_all = nshot - nsf
reuse_pct_all = (n_reuse_all / max(nshot, 1)) * 100
print(f"\n{nsf} SF · {nshot} shot · {giay // 60}:{giay % 60:02d} · Tái sử dụng SF: {n_reuse_all}/{nshot} shot ({reuse_pct_all:.1f}%, đích ~20-25%)")

# MỤC ĐÍCH: Phát hiện và cảnh báo khi dự án có nhiều shot nhưng chưa áp dụng tái sử dụng SF cho các shot đảo góc đối thoại.
CANH_BAO_REUSE = []
if nshot >= 10 and reuse_pct_all < 5.0:
    CANH_BAO_REUSE.append(f"Tỷ lệ tái sử dụng SF mới đạt {reuse_pct_all:.1f}% ({n_reuse_all}/{nshot} shot) — chưa dùng lại SF cũ cho các shot đối thoại lặp góc (đích ~20-25%).")

# MỤC ĐÍCH: Thống kê tỷ lệ cỡ cảnh (rộng ~20-25%, đặc tả rất hạn chế ~2%).
if sum(C.values()) >= nshot * 0.8:
    print(f"cận {C['cận']/t:.0%} · trung {C['trung']/t:.0%} · trung-rộng {C['trung-rộng']/t:.0%} · rộng {C['RỘNG']/t:.0%} · đặc-tả {C['đặc-tả']/t:.0%}"
          f" → rộng {C['RỘNG']/t:.0%} (đích ~20-25%) · đặc-tả {C['đặc-tả']/t:.0%} (đích ~2%)")
else:
    print(f"(chưa tính tỷ lệ cỡ cảnh — mới {sum(C.values())}/{nshot} shot có SF)")
nhip = sum(1 for _, x in allsh if '[NHỊP' in x['text'])
print(f"nhịp không thoại {nhip}/{len(allsh)-nhip} shot thoại = {nhip/max(len(allsh)-nhip,1):.0%} (đích ~15%)")

if BANG:
    print(f"\n── ĐANG Ở GIAI ĐOẠN BẢNG SHOT ({len(BANG)}) ──")
    print("   Chưa sinh SF nên chỉ kiểm được: giây · kiểu dur · cấu trúc bảng shot.")
    print("   Sửa bảng cho sạch RỒI mới sinh prompt — sửa ô rẻ hơn sửa 17 đoạn văn.")
    for m in BANG:
        print(f"  · {m}")

if CHUA_ANH or DAI:
    print(f"\n── TIẾN ĐỘ, KHÔNG PHẢI LỖI ──")
    if CHUA_ANH:
        print(f"  · {len(CHUA_ANH)} SF chưa có ảnh")
    if DAI:
        print(f"  · {len(DAI)} prompt 1.000-1.300 ký tự — vượt mục tiêu, chưa tới mức hỏng")

if POSE_CHUOI:
    print(f"\n── PHÉP KIỂM KHÔNG PHỦ TỚI ({len(POSE_CHUOI)} SF) ──")
    print("   `người-trong-phòng-vắng-goc` cần `pose` kiểu dict để đọc tên người.")
    print(f"   {len(POSE_CHUOI)} SF còn giữ `pose` kiểu chuỗi nên KHÔNG được kiểm — 'SẠCH' ở")
    print("   những scene đó không có nghĩa là đã rà. Đổi `pose` sang dict thì phủ được.")

# Hai phép kiểm cấp phim chỉ phủ được phần dữ liệu đã khai đúng dạng. In ra
# phần CHƯA phủ, vì '✓ không có' trên một nửa dữ liệu đọc ra y hệt '✓ không có'
# trên toàn bộ — và đó là cách một bảng kiểm nói dối mà không sai câu nào.
if KHONG_RO_GIO or THIEU_DUNG:
    print("\n── PHÉP KIỂM CẤP PHIM KHÔNG PHỦ TỚI ──")
    if KHONG_RO_GIO:
        print(f"   · {len(KHONG_RO_GIO)} scene không đọc được GIỜ: {', '.join(KHONG_RO_GIO)}")
        print("     Thẻ địa điểm cần hậu tố giờ trong id (`REF_<NƠI>_DEM`) hoặc nhãn ghi giờ.")
    if THIEU_DUNG:
        print(f"   · {len(THIEU_DUNG)} thẻ `_FULL` thiếu dòng `Dùng: S4 · S5 · …` trong `desc`")
        print(f"     {', '.join(THIEU_DUNG)}")

# MỤC ĐÍCH: Thống kê số shot mang lời dẫn NARRATOR: trong phim hook và nhắc rà soát nếu 0 shot (hỗ trợ cả kịch bản thuần thoại, thuần dẫn hoặc kết hợp).
if not a.scene and 'HOOK' in (d.get('film') or '').upper():
    _n = sum(1 for _, x in allsh if 'NARRATOR:' in (x.get('text') or ''))
    print(f"\n── LỜI DẪN NARRATOR ──\n  {_n} shot mang lời dẫn NARRATOR:")
    if _n == 0:
        print("  · Nhắc rà soát: Phim hook hiện có 0 shot lời dẫn. Nếu kịch bản gốc có luồng lời dẫn, hãy rà lại bước bóc hai luồng.")

if CANH_BAO_REUSE:
    print(f"\n── CẢNH BÁO: CHƯA TÁI SỬ DỤNG SF ({len(CANH_BAO_REUSE)}) ──")
    print("   Quy định: Với các shot đối thoại lặp góc (chuỗi A-B-A-B), trỏ ô `sf` về SF cũ thay vì sinh prompt SF mới trùng lặp.")
    for m in CANH_BAO_REUSE:
        print(f"  · {m}")

if CANH_BAO:
    print(f"\n── NHÃN CẢM XÚC GAY GẮT, khung KHÔNG có trẻ em ({len(CANH_BAO)}) ──")
    print("   Không tự sửa: cảnh người lớn đôi khi cần đúng sắc đó. User quyết.")
    for m in CANH_BAO:
        print(f"  · {m}")

if CANH_BAO_HANH_DONG:
    print(f"\n── CẢNH BÁO: THOẠI CÓ LỆNH THAY ĐỔI TRẠNG THÁI ({len(CANH_BAO_HANH_DONG)}) ──")
    print("   Quy tắc Trạng thái chờ: Khi thoại yêu cầu hành động, SF phải ở trạng thái CHƯA LÀM.")
    for m in CANH_BAO_HANH_DONG:
        print(f"  · {m}")

if NHAC_PROP:
    print(f"\n── NHẮC: THOẠI GỌI TÊN ĐẠO CỤ ({len(NHAC_PROP)}) ──")
    print("   Không phải lỗi. Nhắc trong thoại KHÔNG có nghĩa món đó ở trong khung;")
    print("   chỉ đính REF_PROP khi ảnh SF thật sự phải thấy nó.")
    for m in NHAC_PROP:
        print(f"  · {m}")

print(f"\n{'✓ SẠCH' if not LOI else '✗ TỔNG ' + str(sum(LOI.values())) + ' lỗi: ' + dict(LOI).__repr__()}")
if _bo_that:
    print(f"  (chưa kiểm {len(_bo_that)} scene: {', '.join(_bo_that)})")
sys.exit(1 if LOI or hong else 0)
