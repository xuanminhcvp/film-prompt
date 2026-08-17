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
d = json.load(open(os.path.join(PROJ, 'sf-board.json'), encoding='utf-8'))
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
    """Cỡ cảnh — thứ tự kiểm quan trọng: wide → medium-wide → close-up.

    CHỈ đọc dòng `MÁY QUAY:` chứ không quét cả prompt: chữ 'cận' còn nằm trong
    'tiền cảnh', 'cận kề', và chữ 'toàn cảnh' hay được nhắc lại khi tả hậu cảnh.
    Quét cả prompt thì cỡ cảnh bị chấm theo chữ vô tình lọt vào chứ không theo
    lệnh máy quay thật.

    Board viết bằng TIẾNG VIỆT nên phải nhận cả 'cận cảnh', không chỉ 'close-up'.
    Bản cũ chỉ bắt tiếng Anh ở nhánh cận nhưng lại bắt tiếng Việt ở nhánh rộng,
    nên mọi khung cận của board tiếng Việt rơi hết vào nhánh mặc định 'trung':
    ALTAR in ra 'cận 0% · trung 89%' trong khi thực tế là cận 50% · trung 40%.
    Một dòng thống kê sai kiểu đó nguy hơn không có dòng nào, vì nó khiến người
    ta đi sửa một tỷ lệ vốn đã đạt.
    """
    m = re.search(r'MÁY QUAY:([^\n]*)', p)
    dong = m.group(1).lower() if m else p.lower()
    if re.search(r'cinematic wide|toàn cảnh|viễn cảnh', dong): return 'RỘNG'
    if re.search(r'medium-wide|trung[- ]rộng', dong): return 'trung-rộng'
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


def master(sf):
    f = ALL.get(sf)
    while f and not ((f.get('luatchung') or '').strip() or f['id'].startswith('SF-M-')):
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
# 6 khối bắt buộc của một prompt SF
KHOI_SF = ('MÁY QUAY', 'AI VÀ ĐANG LÀM GÌ', 'TAY', 'HƯỚNG NHÌN', 'BIỂU CẢM', 'ĐÓNG BĂNG')
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
    for nhan in re.findall(r'—\s*([^:\n]{1,60}):\s*\n', p):
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
# cuối cùng mới tới khối ÁNH SÁNG. Đừng quét cả `luatchung`: chữ 'đêm' nằm rải
# trong phần tả đạo cụ và thoại, quét mù là thẻ ban ngày cũng ra 'tối'.
GIO_HAU_TO = {'DEM': 'tối', 'CHAPTOI': 'tối', 'KHUYA': 'tối', 'RANGSANG': 'tối',
              'NGAY': 'sáng', 'SANG': 'sáng', 'TRUA': 'sáng', 'CHIEU': 'sáng'}


def the_dia_diem(sf_id):
    """Leo `refs.bg` tới thẻ mang `luatchung`. Dừng ở nút cuối nếu không có."""
    f, seen = ALL.get(sf_id), set()
    while f and f['id'] not in seen:
        seen.add(f['id'])
        if (f.get('luatchung') or '').strip():
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
    for s in (f.get('label') or '', re.search(r'ÁNH SÁNG:[^\n]*', f.get('luatchung') or '')):
        s = s.group(0) if hasattr(s, 'group') else s
        if not s:
            continue
        if RE_TOI.search(s): return 'tối'
        if RE_SANG.search(s): return 'sáng'
    return None


# KHÔNG kiểm 'hướng thứ N' (user chốt 2026-08-07). Quy ước đánh số vị trí máy
# chỉ là ghi chú cho người viết, không phải luật — hai shot trùng số vẫn có thể
# khác cỡ cảnh và khác chủ thể nét, tức vẫn đủ lệch. Máy đọc con số đó rồi phán
# "trùng góc" là suy diễn quá xa khỏi thứ nó thật sự đo được.


LOI = collections.Counter()
C = collections.Counter()
CANH_BAO = []          # lỗi mức nhắc, không tính vào mã thoát
CANH_BAO_HANH_DONG = [] # nhắc khi thoại có chứa mệnh lệnh thay đổi trạng thái
CHUA_ANH = []          # SF chưa render — TIẾN ĐỘ, không phải lỗi
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
    bad = []
    sh = sc['shots']
    load = collections.Counter(x['sf'] for x in sh)

    for f in sc['sfs']:
        i = f['id']
        # THẺ ĐỊA ĐIỂM được miễn các phép kiểm dưới: nó không có `refs.bg` (nó
        # LÀ gốc), và trần ký tự của nó là 1.400-1.800 chứ không phải 1.000.
        # Dấu hiệu là CÓ `luatchung`; tiền tố `SF-M-` là quy ước cũ, vẫn nhận.
        if (f.get('luatchung') or '').strip() or i.startswith('SF-M-'):
            continue
        if f['refs'].get('bg') not in ALL:
            bad.append(('bg-hỏng', f"{i}: bg={f['refs'].get('bg')!r}"))
        for c in f['refs']['chars']:
            if c not in ALL:
                bad.append(('ref-chết', f"{i}: {c}"))
        if len(f['refs']['chars']) > 8:
            bad.append(('quá-4-nhân-vật', f"{i}: {len(f['refs']['chars'])} ảnh ref"))
        if not f.get('pose'):
            bad.append(('thiếu-pose', i))
        bad += loi_goc(i, goc_cua(i))
        # CHƯA RENDER KHÔNG PHẢI LỖI — đó là TIẾN ĐỘ. Đếm riêng, in một dòng ở
        # cuối. Trộn nó vào danh sách lỗi thì nó chiếm 43% bảng và đẩy các lỗi
        # thật ra khỏi tầm mắt; bảng kiểm nhiễu thì người ta thôi đọc.
        if not co_anh(i):
            CHUA_ANH.append(i)
        if i not in load and i not in LA_NEO:
            bad.append(('SF-mồ-côi', i))
        pr = f.get('prompt') or ''
        # Trần ký tự: SF con <1.000. Master được 1.400-1.800 vì gánh bản đồ vị
        # trí cho cả cụm — nhưng master đã `continue` ở trên nên không tới đây.
        # ~1.000 là MỤC TIÊU chứ không phải trần (skill viết 'dưới ~1.000').
        # Đo trên dữ liệu thật: trung vị 981 — đặt lỗi ở 1.000 thì 45% thẻ bị
        # gắn nhãn lỗi, tức dán nhãn lên công việc bình thường. Lỗi chỉ khi
        # vượt XA; phần giữa gom thành một dòng nhắc.
        if len(pr) > 1300:
            bad.append(('SF-quá-dài', f"{i}: {len(pr)} ký tự (mục tiêu ~1.000)"))
        elif len(pr) > 1000:
            DAI.append(i)
        thieu = [k for k in KHOI_SF if k + ':' not in pr]
        if thieu:
            bad.append(('SF-thiếu-khối', f"{i}: {', '.join(thieu)}"))
        # Trần "dưới 10 chữ KHÔNG": câu cấm nhiều quá thì model đọc thành nhiễu
        # và bắt đầu bỏ qua cả những câu cấm thật sự quan trọng.
        nk = len(re.findall(r'KHÔNG', pr))
        if nk >= 10:
            bad.append(('quá-10-chữ-KHÔNG', f"{i}: {nk} chữ KHÔNG"))
        # MÁY QUAY VIẾT BẰNG SỐ: tiêu cự + độ cao + khoảng cách. Thiếu số thì
        # model tự chọn, và mỗi SF trong cùng cụm ra một cỡ cảnh khác nhau.
        mq = re.search(r'MÁY QUAY:(.*?)(?:\n\n|AI VÀ)', pr, re.S)
        mq = mq.group(1) if mq else ''
        thieu_so = [t for t, rx in (('mm', r'\d+\s*mm'), ('độ cao', r'cao\s*\d'),
                                    ('khoảng cách', r'cách\s'))
                    if not re.search(rx, mq)]
        if mq and thieu_so:
            bad.append(('máy-quay-thiếu-số', f"{i}: thiếu {', '.join(thieu_so)}"))

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
            
        # DƯ NGƯỜI TRONG PROMPT: Tên nhân vật nhắc trong thân prompt phải có trong `goc` hoặc `pose.who`
        # Trừ khối THAM CHIẾU — Lệnh Cắt Tham Chiếu gọi tên người bị gạt CHÍNH VÌ
        # họ không có trong khung, nên quét cả khối đó thì mọi SF đều báo dư người.
        if pr and isinstance(_who, dict):
            than_pr = re.split(r'\n\s*THAM CHIẾU:', pr)[0]
            nguoi_trong_pr = [t for t in TEN_NV if re.search(r'\b' + re.escape(t) + r'\b', than_pr, re.I)]
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
                if not ((f.get('luatchung') or '').strip() or f['id'].startswith('SF-M-'))}
    giai_doan_bang = not _sf_that and len(sh) > 1
    if giai_doan_bang:
        BANG.append(f"{sc['id']} ({len(sh)} shot)")
        
    so_nguoi_phat_ngon = len({n for x in sh for n in nguoi_noi(x.get('text') or '')})
    noi_truc_tiep = so_nguoi_phat_ngon >= 2
    co_ots = False
    is_scene_phone = any(re.search(r'ống\s*nghe|điện\s*thoại|đầu\s*dây|phone', x.get('prompt') or '', re.I) for x in sh)

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
        if not isinstance(x['dur'], int):
            bad.append(('dur-sai-kiểu', f"{x['id']}: {x['dur']!r}"))
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
                
            if RE_OTS.search(x.get('goc') or goc_cua(x['sf'])):
                co_ots = True
                
        # Thiếu REF_PROP
        for prop_name in TEN_PROP:
            if re.search(r'\b' + re.escape(prop_name) + r'\b', (x.get('text') or '') + '\n' + pv, re.I):
                if co_sf and not any(c.startswith('REF_PROP_') and prop_name in c[9:].lower().replace('_', ' ') for c in ALL[x['sf']]['refs']['chars']):
                    bad.append(('thiếu-REF-PROP', f"{x['id']}: nhắc tới '{prop_name}' nhưng không đính ảnh REF_PROP"))

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
        if '[NHỊP' not in x['text'] and co_sf and cc(ALL[x['sf']]['prompt']) == 'RỘNG':
            bad.append(('thoại-trên-khung-rộng', x['id']))
        # CẢNH BÁO: Hành động thay đổi trạng thái trong thoại
        # Nếu thoại chứa các cụm lệnh kinh điển, phải nhắc người duyệt kiểm tra SF
        RE_HANH_DONG = re.compile(r'\b(?:open up|open the door|sit|sit down|stand up|let me in|give it to me)\b', re.I)
        hd_match = RE_HANH_DONG.search(x.get('text') or '')
        if hd_match:
            CANH_BAO_HANH_DONG.append(f"{sc['id']:5} {x['id']:11} Thoại lệnh '{hd_match.group(0)}' → Đảm bảo SF vẽ trạng thái CHƯA LÀM (vd: cửa đóng, đang đứng...).")

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

    # LUẬT 1:1 (user chốt 2026-08-06): mỗi SF gánh ĐÚNG MỘT shot.
    for k, v in load.items():
        if v > 1:
            bad.append(('SF-gánh-2-shot', f"{k}: {v} shot — 1 shot = 1 SF"))

    nsf += len(load); nshot += len(sh); giay += sum(x['dur'] for x in sh)
    for t, _ in bad:
        LOI[t] += 1
    print(f"{'✓' if not bad else '✗'} {sc['id']:5}{len(load):3} SF {len(sh):3} shot"
          f"{'' if len(load) == len(sh) else f'  ⚠ 1:1 lệch ({len(load)} SF / {len(sh)} shot)'}")
    for t, m in bad:
        print(f"      ✗ {t:22} {m}")

# mối nối + đổi không gian
print('\n── ĐỔI KHÔNG GIAN KHÔNG CÓ NHỊP LẶNG ──')
allsh = [(s['id'], x) for s in d['scenes'] if s.get('shots') for x in s['shots']]
hong = 0
for (sa, x), (sb, y) in zip(allsh, allsh[1:]):
    ma, mb = master(x['sf']), master(y['sf'])
    if ma == mb or ma is None or mb is None:
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

# Tỷ lệ cỡ cảnh chỉ có nghĩa khi ĐA SỐ shot đã có SF. Ở giai đoạn bảng shot mới
# có 1-2 SF nên tỷ lệ ra 100% cho một loại — con số đúng về số học nhưng đọc ra
# thì sai hẳn, và một dòng thống kê đánh lừa cũng tệ như một lỗi báo oan.
t = sum(C.values()) or 1
print(f"\n{nsf} SF · {nshot} shot · {giay // 60}:{giay % 60:02d} · shot/SF {nshot / max(nsf,1):.2f} (luật 1:1 → phải là 1.00)")
if sum(C.values()) >= nshot * 0.8:
    print(f"cận {C['cận']/t:.0%} · trung {C['trung']/t:.0%} · trung-rộng {C['trung-rộng']/t:.0%} · rộng {C['RỘNG']/t:.0%}"
          f" → cận+trung {(C['cận']+C['trung'])/t:.0%} (đích 75-80%)")
else:
    print(f"(chưa tính tỷ lệ cỡ cảnh — mới {sum(C.values())}/{nshot} shot có SF)")
nhip = sum(1 for _, x in allsh if '[NHỊP' in x['text'])
print(f"nhịp không thoại {nhip}/{len(allsh)-nhip} shot thoại = {nhip/max(len(allsh)-nhip,1):.0%} (đích ~15%)")

if BANG:
    print(f"\n── ĐANG Ở GIAI ĐOẠN BẢNG SHOT ({len(BANG)}) ──")
    print("   Chưa sinh SF nên chỉ kiểm được: giây · kiểu dur · 1 shot = 1 SF.")
    print("   Sửa bảng cho sạch RỒI mới sinh prompt — sửa ô rẻ hơn sửa 17 đoạn văn.")
    for m in BANG:
        print(f"  · {m}")

if CHUA_ANH or DAI:
    print(f"\n── TIẾN ĐỘ, KHÔNG PHẢI LỖI ──")
    if CHUA_ANH:
        print(f"  · {len(CHUA_ANH)} SF chưa render ảnh")
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

print(f"\n{'✓ SẠCH' if not LOI else '✗ TỔNG ' + str(sum(LOI.values())) + ' lỗi: ' + dict(LOI).__repr__()}")
if _bo_that:
    print(f"  (chưa kiểm {len(_bo_that)} scene: {', '.join(_bo_that)})")
sys.exit(1 if LOI or hong else 0)
