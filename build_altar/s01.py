# -*- coding: utf-8 -*-
"""SCENE 1 — ST. MICHAEL'S CHURCH, ALTAR (sáng)."""
from lib import sf, shot, shotx, nhip, nhac
from nv import refs, nd

SFS, SHOTS = [], []
BG = "REF_NHATHO_SANG"
SID = "S1"

# ── LỆNH CẮT THAM CHIẾU ──
# Cả địa điểm dùng CHUNG một đoạn chat, nên ảnh ref của các khung trước vẫn nằm
# trong ngữ cảnh. Mỗi khung phải gọi tên người bị gạt, nếu không model kéo họ
# vào khung sau. Sinh tự động từ dàn diễn viên của scene trừ đi cast của khung.
DAN = {"MAYA_CUOI": "MAYA", "PRIEST": "PRIEST", "RYAN_CUOI": "RYAN",
       "VANESSA_DO": "VANESSA", "GUEST1_COMLE": "GUEST ONE", "GUEST2_LUA": "GUEST TWO",
       "ADRIAN_NHATHO": "ADRIAN", "SEBASTIAN": "SEBASTIAN"}


def _cut(keys):
    co = [DAN[k] for k in keys if k in DAN]
    bo = [v for k, v in DAN.items() if k not in keys]
    return (f"CHỈ tham chiếu {' và '.join(co)}. "
            f"KHÔNG tham chiếu và KHÔNG vẽ {', '.join(bo)}.") if bo else ""


# ── QUẦN CHÚNG NỀN ──
# Quyết định RIÊNG cho từng khung theo nón quan sát, không khoá theo thẻ địa điểm.
# Trục nhà thờ: bàn thờ ở đầu BẮC, cửa gỗ lớn ở đầu NAM, khách ngồi hai bên lối
# đi ở khoảng giữa. Máy nhìn về bàn thờ thì sau lưng người là bệ đá và hoa ly —
# KHÔNG có khách trong khung; máy nhìn xuôi lối đi về phía cửa thì mới có.
# Khách NGỒI từ đầu tới cuối scene, chỉ hướng chú ý đổi theo chỗ đang diễn ra
# chuyện. Không ai đứng dậy, không ai thì thầm, không tả nét mặt người nền.
QC = {
 "B1": "Tất cả khách nền ngồi yên tại chỗ, mặt hướng lên bậc bàn thờ.",
 "01": "",
 "02": "Ở rìa hai bên khung là đầu hai dãy ghế còn kín khách ngồi, mặt cùng hướng lên bậc bàn thờ.",
 "03": "Dọc hàng ghế phía sau là các khách khác ngồi nguyên tại chỗ, mặt hướng lên bậc bàn thờ.",
 "B2": "",
 "04": "Ở rìa PHẢI khung là bộ tứ đàn dây bốn người ngồi trên ghế, tay vẫn đang kéo đàn. Hai bên rìa khung còn lại là các hàng ghế kín khách ngồi nguyên tại chỗ, mặt hướng theo RYAN.",
 "05": "Khách trong các hàng ghế đó ngồi nguyên tại chỗ, mặt hướng lên phía bậc bàn thờ.",
 "06": "",
 "07": "",
 "08": "",
 "09": "",
 "10": "Các khách trong hàng ghế phía sau ngồi nguyên tại chỗ, mặt hướng lên phía bậc bàn thờ.",
 "11": "Khách trong các hàng ghế đó vẫn ngồi, một người ở hàng ngoài ngồi tựa hẳn vào lưng ghế.",
 "11b": "",
 "12": "Ngoài vùng nét phía sau là đầu các hàng ghế còn kín khách ngồi nguyên tại chỗ.",
 "13": "Khách trong các hàng ghế đó vẫn ngồi, một người đang ngồi gấp lại tờ chương trình lễ.",
 "14": "Ở nửa PHẢI khung, dọc lối đi là các hàng ghế kín khách ngồi nguyên tại chỗ.",
 "15": "Khách trong các hàng ghế đó ngồi nguyên tại chỗ, mặt hướng về phía ba người.",
 "16": "Các khách trong hàng ghế phía sau vẫn ngồi, một người đang ngồi sửa lại tà áo trên đùi.",
 "17": "Ngoài vùng nét ở rìa khung là đầu các hàng ghế còn kín khách ngồi nguyên tại chỗ.",
 "18": "",
 "19": "",
 "20": "Ngoài vùng nét phía sau là các hàng ghế kín khách ngồi nguyên tại chỗ.",
 "21": "Khách trong các hàng ghế đó ngồi nguyên tại chỗ.",
 "22": "Ở hai bên rìa khung là hai hàng ghế cuối còn khách ngồi nguyên tại chỗ.",
 "23": "Ngoài vùng nét ở rìa khung là hàng ghế cuối còn khách ngồi nguyên tại chỗ.",
 "24": "",
 "25": "Khách ở các hàng ghế cuối đó đang lần lượt rời ghế đứng lên, quay về phía cửa lớn.",
 "26": "Khách ở các hàng ghế cuối đó đã đứng lên gần hết, vài người đang lấy áo khoác trên lưng ghế.",
 "27": "Hai bên lối đi đó là các hàng ghế đã lác đác chỗ trống, số khách còn lại đang rời ghế đứng lên.",
 "B3": "",
}


def S(n, cam, doing, hands, look, emo, freeze, keys, zone, who, dist, hpose):
    q = QC[n]
    SFS.append(sf(f"SF-{SID}-{n}", cam, doing.rstrip() + (" " + q if q else ""),
                  hands, look, emo, freeze, refs(*keys), BG, zone, who, dist, hpose,
                  cut=_cut(keys)))


# Quần chúng cho prompt video: mặc định lấy thẳng câu của SF cùng số hiệu — SF vẽ
# ai thì clip phải giữ đúng người đó. Bảy khung dưới đây có người nền nằm sẵn
# trong câu hậu cảnh của SF chứ không nằm ở QC, nên phải khai riêng cho clip.
QCV = {"05": "Khách trong các hàng ghế phía sau ngồi nguyên tại chỗ.",
       "07": "Khách trong các hàng ghế phía sau ngồi nguyên tại chỗ.",
       "11b": "Khách ở các hàng ghế phía sau vẫn ngồi nguyên tại chỗ.",
       "13": "Khách trong các hàng ghế phía sau ngồi nguyên tại chỗ.",
       "23": "Khách ở hàng ghế cuối phía sau ngồi nguyên tại chỗ.",
       "25": "Khách ở các hàng ghế cuối đang lần lượt rời ghế đứng lên.",
       "27": "Khách còn lại ở hai bên lối đi đang rời ghế đứng lên."}


def _tkv(n, tk):
    q = QCV.get(n) or QC.get(n)
    return tk.rstrip() + (f" {q} Không ai trong số họ nhìn vào camera." if q else "")


def V(n, idx, goc, ndl, tk, dien, thoai, im=(), cam="TĨNH", ketclip=None):
    SHOTS.append(shot(f"V-{SID}-{n}", f"SF-{SID}-{n}", SID, idx, goc, nd(*ndl), _tkv(n, tk),
                      dien, thoai, im, cam, ketclip))


def B(n, mota, goc, ndl, tk, tt, gy, sfx, music, dur=6, cam="TĨNH"):
    SHOTS.append(nhip(f"V-{SID}-{n}", f"SF-{SID}-{n}", mota, goc, nd(*ndl), _tkv(n, tk), tt, gy, sfx, music, dur, cam))


KHACH = ""

# ─────────────────────────── NHỊP MỞ PHIM ───────────────────────────
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 20m, đặt ở cuối lối đi chính phía cửa lớn nhìn về bàn thờ",
  "Lòng nhà thờ chật kín khách dự cưới ngồi hai bên hàng ghế. MAYA đứng một mình trên bậc bàn thờ ở cuối lối đi, "
  "PRIEST đứng chếch sau lưng cô nửa bước. Lối đi giữa trải thảm đỏ hoàn toàn trống.",
  "MAYA hai tay nắm nhau trước bụng. PRIEST hai tay khoanh trước ngực giữ cuốn sách lễ.",
  "MAYA nhìn thẳng về phía cửa lớn cuối nhà thờ. PRIEST nhìn xuống cuốn sách lễ. Khách nền không nhìn vào ống kính.",
  "MAYA — người đã đợi hai mươi lăm phút trước mặt hai trăm người: cằm giữ ngang, môi mím, mắt mở to nhìn về phía cửa. "
  "PRIEST — mệt và ái ngại, khoé môi trễ.",
  "đúng khoảnh khắc ngay TRƯỚC khi một tiếng động ở cuối nhà thờ làm cả phòng quay đầu lại",
  ["MAYA_CUOI", "PRIEST"], "bậc bàn thờ cuối lối đi chính",
  {"MAYA": "đứng giữa bậc bàn thờ", "PRIEST": "đứng chếch sau lưng nửa bước"},
  "cách nhau nửa mét", {"MAYA": "hai tay nắm nhau trước bụng", "PRIEST": "hai tay giữ sách lễ"})
B("B1", "Mở phim. Toàn cảnh nhà thờ kín khách. MAYA đứng một mình trên bậc bàn thờ, lối đi giữa trống trơn.",
  "toàn cảnh 24mm · MAYA NÉT trên bậc bàn thờ + PRIEST NÉT chếch sau lưng · khách hai bên hàng ghế mờ",
  [("MAYA", "MAYA_CUOI"), ("PRIEST", "PRIEST")],
  "MAYA rõ mặt trên bậc bàn thờ, PRIEST rõ mặt chếch sau lưng cô. Khách hai bên hàng ghế mờ nhẹ, không ai nhìn vào camera.",
  "một đám cưới đã trễ hai mươi lăm phút và cả phòng đã bắt đầu hiểu ra điều mà cô dâu chưa chịu hiểu.",
  "MAYA đứng yên nhìn về phía cửa lớn, ngực thở một nhịp dài; PRIEST liếc đồng hồ đeo tay rồi nhìn xuống sách lễ; "
  "vài vị khách ở hàng ghế đầu quay đầu ra sau.",
  "Ambient tiếng vọng của một gian nhà thờ đá, tiếng ghế gỗ cọt kẹt và tiếng xì xào rất nhỏ.",
  nhac("ĐẨY", "Mở phim — nhạc chiếm sân khấu để dựng cả thế giới và đặt một người phụ nữ vào giữa nó, một mình.",
       "Cinematic soul at 74 BPM opening with a lone female alto humming very close to the mic over a slow felt-piano "
       "figure; low strings and a soft heartbeat kick enter at the eight-second mark and lift together; the pull comes "
       "at the very end when everything drops away except the voice; lyrics from a woman standing at the front of a "
       "room full of people and waiting, dignified and unhurried, never self-pitying; warm analog mix, tape saturation, "
       "female vocal, soul, cinematic, strings, intimate",
       "Cinematic instrumental at 74 BPM; felt piano alone for four seconds, then a low cello walking underneath, a slow "
       "string swell rising to one held chord and dropping straight back to piano; no percussion until a soft heartbeat "
       "kick in the last third; grand but restrained, warm analog mix, piano, cello, strings, cinematic, restrained"),
  dur=8)

# ─────────────────────────── LỄ CƯỚI ───────────────────────────
S("01", "two-shot trung 50mm, cao 1m55, cách MAYA 2m2, đặt chếch bên bậc bàn thờ để lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung trên bậc bàn thờ, PRIEST đứng ở nửa TRÁI khung quay mặt về phía lối đi và cầm sách lễ mở. "
  "Sau lưng hai người là bệ bàn thờ đá trắng và hai bình hoa ly.",
  "PRIEST hai tay đỡ cuốn sách lễ đang mở ngang ngực. MAYA hai tay nắm nhau trước bụng.",
  "PRIEST nhìn xuống trang sách rồi ngước về phía lối đi. MAYA nhìn nghiêng về phía PRIEST.",
  "PRIEST — người đang cố giữ nghi lễ chạy tiếp dù thiếu một người: giọng đều, mày hơi nhíu. "
  "MAYA — nghe tên mình được xướng lên bên cạnh một cái tên chưa có mặt: môi mím, mắt chớp chậm.",
  "đúng khoảnh khắc ngay TRƯỚC khi PRIEST đọc hết câu và ngẩng lên",
  ["MAYA_CUOI", "PRIEST"], "bậc bàn thờ",
  {"MAYA": "đứng nửa phải khung", "PRIEST": "đứng nửa trái khung"},
  "cách nhau nửa mét", {"MAYA": "hai tay nắm nhau trước bụng", "PRIEST": "hai tay đỡ sách lễ mở"})
V("01", [0], "two-shot trung 50mm · PRIEST NÉT trái + MAYA NÉT phải · khách nền mờ",
  [("MAYA", "MAYA_CUOI"), ("PRIEST", "PRIEST")],
  "PRIEST và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "PRIEST ngước lên khỏi cuốn sách lễ và nói ra cả gian phòng",
  [("PRIEST", "warm, formal", 0)], [("MAYA", "listening, still")])

S("02", "trung 50mm, cao 1m55, cách MAYA 2m5, đặt phía lối đi nhìn chếch lên bậc bàn thờ",
  "MAYA đứng ở nửa PHẢI khung trên bậc bàn thờ. Ở nửa TRÁI khung, ngay đầu hàng ghế trước, GUEST ONE đã đứng dậy "
  "khỏi ghế và nghiêng người về phía lối đi.",
  "GUEST ONE một tay vịn lưng ghế gỗ trước mặt. MAYA hai tay nắm nhau trước bụng.",
  "GUEST ONE nhìn thẳng vào mặt MAYA. MAYA nhìn về phía cửa lớn cuối nhà thờ, không quay sang.",
  "GUEST ONE — người vừa hết kiên nhẫn và nói to hơn mình định: mày nhướn, miệng hé. "
  "MAYA — nghe câu hỏi mà mình không muốn trả lời: quai hàm giữ, mắt vẫn hướng ra cửa.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay đầu lại trả lời",
  ["MAYA_CUOI", "GUEST1_COMLE"], "bậc bàn thờ và đầu hàng ghế trước",
  {"MAYA": "đứng trên bậc bàn thờ nửa phải khung", "GUEST ONE": "đứng ở đầu hàng ghế nửa trái khung"},
  "cách nhau ba mét", {"MAYA": "hai tay nắm nhau trước bụng", "GUEST ONE": "một tay vịn lưng ghế"})
V("02", [1, 2], "trung 50mm · GUEST ONE NÉT trái đứng ở hàng ghế + MAYA NÉT phải trên bậc bàn thờ",
  [("MAYA", "MAYA_CUOI"), ("GUEST ONE", "GUEST1_COMLE")],
  "GUEST ONE và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "GUEST ONE nghiêng người ra lối đi hỏi, MAYA quay đầu lại trả lời",
  [("GUEST ONE", "impatient, low", 1), ("MAYA", "steady, quiet", 2)])

S("03", "cận-trung 85mm, cao 1m55, cách MAYA 1m8, máy đặt bên hàng ghế đầu nhìn chếch lên",
  "MAYA đứng ở nửa PHẢI khung, hơi cúi xuống về phía hàng ghế đầu. GUEST TWO ngồi ở hàng ghế đầu nửa TRÁI khung, "
  "vươn người tới và đã đặt một bàn tay lên cổ tay MAYA.",
  "GUEST TWO một tay đặt lên cổ tay MAYA, tay kia giữ chiếc túi vải nhỏ trên đùi. MAYA để yên bàn tay bị nắm, "
  "tay còn lại nắm hờ vạt váy.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "GUEST TWO — người lớn tuổi thấy một cô gái sắp gãy và muốn đỡ: mày chau, giọng dỗ. "
  "MAYA — bị chạm vào đúng chỗ mình đang gồng: mắt hơi đỏ, môi mím chặt lại, cằm vẫn ngẩng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA rút nhẹ tay ra và đứng thẳng lên",
  ["MAYA_CUOI", "GUEST2_LUA"], "bậc bàn thờ, sát hàng ghế đầu",
  {"MAYA": "đứng nửa phải khung, hơi cúi xuống", "GUEST TWO": "ngồi hàng ghế đầu nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay để yên cho GUEST TWO nắm", "GUEST TWO": "một tay nắm cổ tay MAYA"})
V("03", [3, 4], "cận-trung 85mm · GUEST TWO NÉT trái ngồi hàng ghế + MAYA NÉT phải đứng cúi xuống",
  [("MAYA", "MAYA_CUOI"), ("GUEST TWO", "GUEST2_LUA")],
  "GUEST TWO và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "GUEST TWO siết nhẹ cổ tay MAYA, MAYA đứng thẳng lên và nói ra cả gian phòng",
  [("GUEST TWO", "gentle, coaxing", 3), ("MAYA", "firm, polite", 4)],
  ketclip="Cuối clip, hai cánh cửa gỗ lớn cuối nhà thờ bật mở, cả gian phòng quay đầu về phía đó. "
          "Clip dừng đúng lúc mọi cái đầu vừa quay xong.")

# ─────────────────────────── NHỊP: RYAN BƯỚC VÀO ───────────────────────────
S("B2", "trung-rộng 35mm, cao 1m60, cách RYAN 6m, đặt trong lối đi giữa nhìn về phía cửa lớn",
  "RYAN vừa bước qua hai cánh cửa gỗ lớn và đang đứng ở đầu lối đi giữa, VANESSA đứng sát bên phải anh, "
  "bàn tay hai người đang nắm vào nhau. Hai bên lối đi là các hàng ghế kín khách vẫn ngồi nguyên tại chỗ, đầu đã quay về phía hai người.",
  "RYAN tay phải nắm tay trái VANESSA, tay trái buông. VANESSA tay phải cầm chiếc clutch da đen.",
  "RYAN nhìn dọc lối đi về phía bàn thờ. VANESSA nhìn quét qua các hàng ghế hai bên. Khách nền không nhìn vào ống kính.",
  "RYAN — người đã quyết định từ trước và vào đây để nói ra: quai hàm siết, mắt thẳng, không né. "
  "VANESSA — người tới xem một màn kịch mà mình mua vé: cằm hếch, khoé môi giữ nét cười rất nhạt.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước bước đầu tiên xuống lối đi",
  ["RYAN_CUOI", "VANESSA_DO"], "đầu lối đi giữa, ngay trong cửa lớn",
  {"RYAN": "đứng giữa lối đi", "VANESSA": "đứng sát bên phải RYAN"},
  "sát nhau", {"RYAN": "tay phải nắm tay VANESSA", "VANESSA": "tay phải cầm clutch da đen"})
B("B2", "Hai cánh cửa lớn vừa mở. RYAN đứng đầu lối đi, tay nắm tay VANESSA. Cả nhà thờ quay đầu lại nhìn.",
  "trung-rộng 35mm · RYAN NÉT giữa lối đi + VANESSA NÉT sát bên phải · khách hai bên mờ",
  [("RYAN", "RYAN_CUOI"), ("VANESSA", "VANESSA_DO")],
  "RYAN và VANESSA rõ mặt ở đầu lối đi. Khách hai bên hàng ghế mờ, không ai nhìn vào camera.",
  "hai người vừa bước vào một căn phòng mà tất cả những người trong đó đang chờ một trong hai người, "
  "và họ nắm tay nhau bước vào.",
  "RYAN đứng lại một nhịp rồi bắt đầu bước xuống lối đi, VANESSA đi theo nửa bước sau; vài vị khách ở hàng ghế gần "
  "quay hẳn người lại; một người đưa tay lên miệng.",
  "SFX tiếng cánh cửa gỗ nặng đập vào tường đá và tiếng giày gõ trên nền đá, Ambient tiếng xì xào dâng lên rồi tắt.",
  nhac("NGHỈ", "Ngay sau tiếng nhạc lớn mở phim phải là một khoảng gần như câm để cú bước vào này nặng đúng mức của nó.",
       "Sparse folk at 58 BPM; a single nylon-string guitar picking one repeating figure, a female voice entering late "
       "and low, almost spoken, only a few words; no drums, no bass; the pull is when the guitar stops for a full beat "
       "and only room tone remains; lyrics about watching a door open and already knowing, plain and unadorned; "
       "dry intimate mix, female vocal, folk, sparse, quiet",
       "Ambient instrumental at 56 BPM; one sustained church-organ note held very low under a single struck piano key "
       "repeating every four seconds, a faint room reverb tail, no percussion, no arc, ending unresolved; "
       "organ, piano, minimal, cold, unresolved"),
  dur=8)

# ─────────────────────────── RYAN NÓI ───────────────────────────
S("04", "trung 50mm, cao 1m55, cách RYAN 2m5, đặt bên lối đi giữa lấy RYAN trước và MAYA phía sau",
  "RYAN đứng giữa lối đi ở nửa TRÁI khung, đã đi được nửa đường. Xa hơn ở nửa PHẢI khung, trên bậc bàn thờ, "
  "MAYA đứng quay mặt về phía anh. VANESSA đứng lùi sau RYAN nửa bước, chỉ thấy một phần thân người ngoài rìa trái.",
  "RYAN một tay giơ ngang ngực ra hiệu dừng lại, tay kia buông. MAYA hai tay buông xuống hai bên.",
  "RYAN nhìn về phía dàn nhạc bên phải khung rồi quét mắt qua các hàng ghế. MAYA nhìn thẳng vào RYAN.",
  "RYAN — người vừa cắt ngang một nghi lễ và cần cả phòng im: mắt thẳng, giọng lớn, không hằn học. "
  "MAYA — thấy chồng sắp cưới đứng nắm tay một người khác: mắt mở, môi hé, chưa hiểu.",
  "đúng khoảnh khắc ngay TRƯỚC khi tiếng đàn tắt hẳn và cả phòng im",
  ["RYAN_CUOI", "MAYA_CUOI", "VANESSA_DO"], "lối đi giữa và bậc bàn thờ",
  {"RYAN": "đứng giữa lối đi nửa trái khung", "MAYA": "đứng trên bậc bàn thờ phía sau nửa phải khung",
   "VANESSA": "đứng lùi sau RYAN, chỉ thấy một phần thân ngoài rìa trái"},
  "RYAN cách MAYA tám mét", {"RYAN": "một tay giơ ngang ngực ra hiệu dừng", "MAYA": "hai tay buông",
                             "VANESSA": "tay cầm clutch, ngoài rìa khung"})
V("04", [5, 6], "trung 50mm · RYAN NÉT giữa lối đi + MAYA NÉT trên bậc bàn thờ phía sau · VANESSA rìa trái, chỉ thấy một phần thân",
  [("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI"), ("VANESSA", "VANESSA_DO")],
  "RYAN rõ mặt ở tiền cảnh, MAYA rõ mặt phía sau trên bậc bàn thờ. VANESSA chỉ thấy một phần thân người ở rìa trái, "
  "KHÔNG rõ mặt, KHÔNG quay về camera. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN giơ tay ra hiệu cho dàn nhạc dừng lại, MAYA nhìn xuống hai bàn tay đang nắm nhau của anh và cô kia",
  [("RYAN", "loud, controlled", 5), ("MAYA", "quiet, unsteady", 6)])

S("05", "cận-trung 85mm, cao 1m55, cách RYAN 1m8, máy sau vai TRÁI của PRIEST; vai và gáy PRIEST chiếm rìa trái, out nét",
  "RYAN đứng chính diện chiếm phần lớn khung, đã lên tới chân bậc bàn thờ và đang chìa tay đòi chiếc micro. "
  "PRIEST chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng RYAN là lối đi trải thảm đỏ "
  "và các hàng ghế có khách.",
  "RYAN chìa bàn tay phải ra ngang tầm ngực, lòng bàn tay ngửa. PRIEST một tay giữ chiếc micro cần nhỏ trên bục giảng.",
  "RYAN nhìn thẳng vào mặt PRIEST qua vai ông.",
  "RYAN — người muốn cả hai trăm người nghe rõ và biết mình cần cái micro để làm việc đó: mắt mở, cằm hất nhẹ. ",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay RYAN chạm vào chiếc micro",
  ["RYAN_CUOI", "PRIEST"], "chân bậc bàn thờ, cạnh bục giảng",
  {"RYAN": "đứng chính diện giữa khung", "PRIEST": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"RYAN": "chìa bàn tay phải ra đòi micro", "PRIEST": "một tay giữ micro trên bục giảng"})
V("05", [7, 8], "OTS cận-trung 85mm · RYAN NÉT chính diện · vai và gáy PRIEST tiền cảnh trái out nét",
  [("RYAN", "RYAN_CUOI"), ("PRIEST", "PRIEST")],
  "RYAN rõ mặt chính diện. PRIEST chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "RYAN chìa tay đòi chiếc micro trên bục giảng, PRIEST giữ tay lại",
  [("RYAN", "loud, insistent", 7), ("PRIEST", "firm, reproachful", 8)])

S("06", "trung 50mm, cao 1m55, cách RYAN 2m4, đặt chếch bên bậc bàn thờ để lấy cả hai người",
  "RYAN đứng ở nửa TRÁI khung trên bậc thứ nhất, tay cầm micro hạ xuống ngang ngực. MAYA đứng ở nửa PHẢI khung "
  "trên bậc trên cùng, cách anh hai bước. Hậu cảnh là bệ bàn thờ đá trắng và hai bình hoa ly.",
  "RYAN một tay cầm micro hạ ngang ngực, tay kia buông. MAYA một tay đưa lên ngang bụng, lòng bàn tay hướng lên "
  "như đang hỏi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — người vừa nói xong câu không rút lại được và thấy nhẹ đi: vai hạ, mắt thẳng. "
  "MAYA — nghe một câu tiếng Anh rất rõ mà vẫn không ghép được nghĩa: mày chau, đầu hơi nghiêng, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước xuống một bậc về phía RYAN",
  ["RYAN_CUOI", "MAYA_CUOI"], "bậc bàn thờ",
  {"RYAN": "đứng bậc thứ nhất nửa trái khung", "MAYA": "đứng bậc trên cùng nửa phải khung"},
  "cách nhau hai bước", {"RYAN": "một tay cầm micro hạ ngang ngực", "MAYA": "một tay đưa ngang bụng ngửa lên"})
V("06", [9, 10], "trung 50mm · RYAN NÉT trái cầm micro + MAYA NÉT phải trên bậc bàn thờ",
  [("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI")],
  "RYAN và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN nói vào micro rồi hạ nó xuống, MAYA bước xuống một bậc về phía anh",
  [("RYAN", "flat, deliberate", 9), ("MAYA", "unsteady, searching", 10)])

S("07", "OTS cận 85mm, cao 1m55, cách RYAN 1m5, máy sau vai PHẢI của MAYA; vai và gáy MAYA chiếm rìa phải, out nét",
  "RYAN đứng chính diện chiếm phần lớn khung, micro hạ trong tay. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, "
  "ngoài vùng nét. Hậu cảnh sau lưng RYAN là lối đi thảm đỏ và các hàng ghế có khách đang ngồi im.",
  "RYAN một tay cầm micro, tay kia hất nhẹ về phía chiếc váy trước mặt rồi thả xuống.",
  "RYAN nhìn thẳng vào mặt MAYA qua vai cô, mắt quét một lượt từ vai xuống gấu váy rồi ngược lên.",
  "RYAN — người đang liệt kê ra thành tiếng những thứ mình chê: mép hơi nhếch, mắt lạnh, giọng đều và rõ.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN đưa micro lên miệng nói tiếp",
  ["RYAN_CUOI", "MAYA_CUOI"], "bậc bàn thờ",
  {"RYAN": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"RYAN": "một tay cầm micro, tay kia hất về phía váy", "MAYA": "hai tay buông, ngoài vùng nét"})
V("07", [11], "OTS cận 85mm · RYAN NÉT chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI")],
  "RYAN rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "RYAN đưa micro lên và chỉ tay vào chiếc váy trước mặt",
  [("RYAN", "dismissive, even", 11)], [("MAYA", "silent, not moving")])

S("08", "cận 85mm, cao 1m55, cách MAYA 1m4, máy sau vai TRÁI của RYAN; vai RYAN chiếm rìa trái tiền cảnh, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. RYAN chỉ còn là một mảng vai ở rìa TRÁI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng MAYA là bệ bàn thờ đá trắng và một bình hoa ly.",
  "MAYA hai tay buông thẳng xuống hai bên, các ngón khép lại.",
  "MAYA nhìn thẳng vào mặt RYAN qua vai anh.",
  "MAYA — người vừa nghe chính lời hứa cũ của mình bị đem ra làm trò: mắt ướt nhưng chưa rơi, quai hàm siết, "
  "giọng nhỏ và rất rõ.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN cắt lời cô",
  ["MAYA_CUOI", "RYAN_CUOI"], "bậc bàn thờ",
  {"MAYA": "đứng chính diện giữa khung", "RYAN": "một mảng vai tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "hai tay buông thẳng", "RYAN": "một tay cầm micro, ngoài vùng nét"})
V("08", [12], "OTS cận 85mm · MAYA NÉT chính diện · vai RYAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_CUOI"), ("RYAN", "RYAN_CUOI")],
  "MAYA rõ mặt chính diện. RYAN chỉ thấy MỘT MẢNG VAI ở tiền cảnh trái, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đứng yên, chỉ có ngực thở, rồi nói",
  [("MAYA", "quiet, wounded", 12)], [("RYAN", "silent, unmoved")])

S("09", "trung 50mm, cao 1m55, cách RYAN 2m2, đặt chếch bên bậc bàn thờ lấy RYAN nét và MAYA phía sau",
  "RYAN đứng ở nửa TRÁI khung, quay nửa người về phía các hàng ghế để nói cho cả phòng nghe. MAYA đứng ở nửa PHẢI "
  "khung cách anh hai bước, thấy rõ mặt. Hậu cảnh là bệ bàn thờ và các hàng ghế có khách ngồi im.",
  "RYAN một tay cầm micro sát miệng, tay kia buông thõng dọc thân.",
  "RYAN nhìn về phía các hàng ghế chứ không nhìn MAYA. MAYA nhìn thẳng vào RYAN.",
  "RYAN — người đang trình bày một bản tính toán mình cho là hợp lý: giọng đều, mắt sáng, không giận. "
  "MAYA — nghe mẹ mình bị đem ra làm ví dụ trước hai trăm người: mặt trắng ra, môi hé, thân đứng thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng người thốt lên từ hàng ghế",
  ["RYAN_CUOI", "MAYA_CUOI"], "bậc bàn thờ",
  {"RYAN": "đứng nửa trái khung, quay nửa người về hàng ghế", "MAYA": "đứng nửa phải khung"},
  "cách nhau hai bước", {"RYAN": "một tay cầm micro, tay kia đếm bằng ngón trỏ", "MAYA": "hai tay buông thẳng"})
V("09", [13], "trung 50mm · RYAN NÉT trái nói vào micro + MAYA NÉT phải đứng nghe",
  [("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI")],
  "RYAN và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN quay nửa người về phía các hàng ghế và đếm từng thứ trên đầu ngón tay",
  [("RYAN", "even, matter-of-fact", 13)], [("MAYA", "silent, going pale")])

S("10", "cận-trung 85mm, cao 1m40, cách GUEST ONE 1m6, máy đặt trong lòng hàng ghế ngang tầm người ngồi",
  "GUEST ONE ngồi ở nửa TRÁI khung trong hàng ghế, vừa nhổm nửa người lên khỏi mặt ghế. GUEST TWO ngồi ngay cạnh "
  "ở nửa PHẢI khung, đã đưa một bàn tay lên che miệng. Hậu cảnh là lưng ghế gỗ.",
  "GUEST ONE hai tay chống lên lưng ghế trước mặt. GUEST TWO một tay che miệng, tay kia nắm chặt chiếc túi vải nhỏ.",
  "Cả hai nhìn về phía bậc bàn thờ ngoài khung. TUYỆT ĐỐI không ai nhìn vào ống kính.",
  "GUEST ONE — người vừa nghe một câu vượt quá sức chịu và buột miệng: mày chau sâu, miệng mở. "
  "GUEST TWO — bàng hoàng, mắt mở to sau bàn tay.",
  "đúng khoảnh khắc ngay TRƯỚC khi GUEST ONE ngồi phịch trở lại xuống ghế",
  ["GUEST1_COMLE", "GUEST2_LUA"], "hàng ghế thứ hai bên trái lối đi",
  {"GUEST ONE": "ngồi nửa trái khung, nhổm nửa người lên", "GUEST TWO": "ngồi nửa phải khung"},
  "ngồi sát cạnh nhau", {"GUEST ONE": "hai tay chống lưng ghế trước", "GUEST TWO": "một tay che miệng"})
V("10", [14], "cận-trung 85mm · GUEST ONE NÉT trái + GUEST TWO NÉT phải, cùng hàng ghế",
  [("GUEST ONE", "GUEST1_COMLE"), ("GUEST TWO", "GUEST2_LUA")],
  "GUEST ONE và GUEST TWO, cả hai rõ mặt trong hàng ghế. Khách khác mờ, không ai nhìn vào camera.",
  "GUEST ONE nhổm lên khỏi ghế rồi buột miệng nói",
  [("GUEST ONE", "appalled, hushed", 14)], [("GUEST TWO", "silent, hand over mouth")])

S("11", "trung 50mm, cao 1m55, cách RYAN 2m4, đặt chếch bên bậc bàn thờ lấy cả hai người",
  "RYAN đứng ở nửa TRÁI khung, micro sát miệng, quay hẳn về phía các hàng ghế. MAYA đứng ở nửa PHẢI khung "
  "cách anh hai bước, mặt hướng về phía anh. Hậu cảnh là các hàng ghế có khách và lối đi thảm đỏ.",
  "RYAN một tay cầm micro sát miệng, tay kia giơ lên vẫy các hàng ghế mời nói theo.",
  "RYAN nhìn ra các hàng ghế. MAYA nhìn thẳng vào RYAN.",
  "RYAN — người đã đi quá xa và đang kéo cả phòng đi cùng: mắt sáng, khoé môi kéo lên. "
  "MAYA — nghề của mình bị gọi thành một câu chửi trước mặt hai trăm người: mắt không chớp, cằm ngẩng, thân bất động.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước một bước tới trước",
  ["RYAN_CUOI", "MAYA_CUOI"], "bậc bàn thờ",
  {"RYAN": "đứng nửa trái khung quay về hàng ghế", "MAYA": "đứng nửa phải khung"},
  "cách nhau hai bước", {"RYAN": "một tay cầm micro, tay kia vẫy mời hàng ghế", "MAYA": "hai tay buông thẳng"})
SHOTS.append(shotx("V-S1-11", "SF-S1-11", "trung 50mm · RYAN NÉT trái nói vào micro + MAYA NÉT phải đứng nghe",
  nd(("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI")),
  "RYAN và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN quay hẳn về phía các hàng ghế và nói vào micro",
  [("RYAN", "loud, performative",
    "I cannot marry a woman who wipes strangers for a living and has a dying mother attached to her like a debt.")],
  [("MAYA", "silent, perfectly still")]))

S("11b", "cận 85mm, cao 1m55, cách RYAN 1m4, máy sau vai PHẢI của MAYA; vai và gáy MAYA chiếm rìa phải, out nét",
  "RYAN đứng chính diện chiếm phần lớn khung, micro sát miệng, một tay giơ lên vẫy về phía các hàng ghế. "
  "MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh là các hàng ghế có khách ngồi im.",
  "RYAN một tay cầm micro sát miệng, tay kia giơ lên vẫy mời các hàng ghế nói theo.",
  "RYAN nhìn ra các hàng ghế phía sau MAYA.",
  "RYAN — người đang kéo cả hai trăm người vào trò của mình: mắt sáng, khoé môi kéo lên, giọng vang.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người trong hàng ghế đứng bật dậy",
  ["RYAN_CUOI", "MAYA_CUOI"], "bậc bàn thờ",
  {"RYAN": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau hai bước", {"RYAN": "một tay cầm micro, tay kia giơ lên vẫy hàng ghế",
                         "MAYA": "hai tay buông thẳng, ngoài vùng nét"})
SHOTS.append(shotx("V-S1-11b", "SF-S1-11b",
  "OTS cận 85mm · RYAN NÉT chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  nd(("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI")),
  _tkv("11b", "RYAN rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
              "TUYỆT ĐỐI KHÔNG quay mặt về camera."),
  "RYAN giơ tay vẫy các hàng ghế mời mọi người nói theo mình",
  [("RYAN", "loud, performative", "Say it with me. I am not marrying a bedpan maid.")],
  [("MAYA", "silent, perfectly still")],
  ketclip="Cuối clip, VANESSA từ lối đi bước lên đứng cạnh RYAN, sát vai anh. Clip dừng đúng lúc cô dừng chân."))

S("12", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt chếch bên bậc bàn thờ lấy MAYA trái và cặp kia phải",
  "MAYA đứng ở nửa TRÁI khung, đã bước xuống một bậc. VANESSA đứng ở nửa PHẢI khung, mới lên tới cạnh RYAN "
  "và hơi ngả người về phía anh; RYAN đứng sát bên phải VANESSA, chỉ thấy nửa người và một phần mặt ngoài rìa phải.",
  "MAYA hai tay buông thẳng. VANESSA một tay khoác vào khuỷu tay RYAN, tay kia cầm chiếc clutch da đen.",
  "MAYA nhìn thẳng vào mặt VANESSA. VANESSA nhìn lại MAYA.",
  "MAYA — người vừa gọi tên mẹ mình ra làm điểm tựa cuối cùng: giọng thấp, mắt thẳng, không van xin. "
  "VANESSA — người nói câu ác nhất bằng giọng dịu nhất: đầu nghiêng, khoé môi cong lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi lại cô ta là ai",
  ["MAYA_CUOI", "VANESSA_DO", "RYAN_CUOI"], "bậc bàn thờ",
  {"MAYA": "đứng nửa trái khung", "VANESSA": "đứng nửa phải khung cạnh RYAN",
   "RYAN": "đứng sát bên phải VANESSA, thấy nửa người ngoài rìa phải"},
  "cách nhau hai bước", {"MAYA": "hai tay buông thẳng", "VANESSA": "một tay khoác khuỷu tay RYAN",
                         "RYAN": "một tay cầm micro hạ xuống"})
V("12", [16, 17], "trung 50mm · MAYA NÉT trái + VANESSA NÉT phải · RYAN thấy nửa người rìa phải",
  [("MAYA", "MAYA_CUOI"), ("VANESSA", "VANESSA_DO"), ("RYAN", "RYAN_CUOI")],
  "MAYA và VANESSA rõ mặt. RYAN chỉ thấy nửa người ở rìa phải, KHÔNG phải trọng tâm. "
  "Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA bước xuống một bậc, VANESSA khoác tay RYAN và trả lời thay anh",
  [("MAYA", "low, steady", 16), ("VANESSA", "sweet, patronising", 17)])

S("13", "cận-trung 85mm, cao 1m55, cách VANESSA 1m7, máy sau vai TRÁI của MAYA; vai và gáy MAYA chiếm rìa trái, out nét",
  "VANESSA đứng chính diện chiếm phần lớn khung, một tay còn khoác vào khuỷu tay người đàn ông đứng ngoài khung. MAYA chỉ còn là vai và gáy "
  "ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng VANESSA là lối đi thảm đỏ và các hàng ghế.",
  "VANESSA một tay cầm chiếc clutch da đen ngang bụng, tay kia buông.",
  "VANESSA nhìn thẳng vào mặt MAYA qua vai cô.",
  "VANESSA — người đang tự giới thiệu và thích cái tên mình vang lên trong nhà thờ: cằm hếch, giọng rõ ràng, "
  "khoé môi giữ nét cười xã giao.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA mở khoá chiếc clutch",
  ["VANESSA_DO", "MAYA_CUOI"], "bậc bàn thờ",
  {"VANESSA": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh trái"},
  "cách nhau hai bước", {"VANESSA": "một tay cầm clutch ngang bụng", "MAYA": "hai tay buông, ngoài vùng nét"})
V("13", [18, 19], "OTS cận-trung 85mm · VANESSA NÉT chính diện · vai và gáy MAYA tiền cảnh trái out nét",
  [("VANESSA", "VANESSA_DO"), ("MAYA", "MAYA_CUOI")],
  "VANESSA rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA hỏi trước, VANESSA đứng thẳng lên và trả lời thong thả",
  [("MAYA", "flat, tired", 18), ("VANESSA", "poised, pleasant", 19)])

S("14", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt chếch bên bậc bàn thờ lấy cả hai người",
  "MAYA đứng ở nửa TRÁI khung, VANESSA đứng ở nửa PHẢI khung cách hai bước, tay đã đặt lên khoá chiếc clutch. "
  "Hậu cảnh là bệ bàn thờ đá trắng bên trái và lối đi thảm đỏ bên phải.",
  "MAYA hai tay buông thẳng. VANESSA hai tay cầm chiếc clutch trước bụng, ngón cái đặt lên khoá kim loại.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa hiểu ra chuyện này đã được sắp trước từ lâu: mắt hơi nheo, giọng rất bình. "
  "VANESSA — thích thú vì được hỏi đúng câu mình chờ: mày nhướn, khoé môi cong.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA bật khoá chiếc clutch",
  ["MAYA_CUOI", "VANESSA_DO"], "bậc bàn thờ",
  {"MAYA": "đứng nửa trái khung", "VANESSA": "đứng nửa phải khung"},
  "cách nhau hai bước", {"MAYA": "hai tay buông thẳng", "VANESSA": "hai tay cầm clutch, ngón cái trên khoá"})
V("14", [20, 21], "trung 50mm · MAYA NÉT trái + VANESSA NÉT phải, cả hai rõ mặt",
  [("MAYA", "MAYA_CUOI"), ("VANESSA", "VANESSA_DO")],
  "MAYA và VANESSA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA nói trước, VANESSA đặt ngón cái lên khoá chiếc clutch trong lúc trả lời",
  [("MAYA", "quiet, certain", 20), ("VANESSA", "amused, light", 21)])

S("15", "trung 50mm, cao 1m55, cách VANESSA 2m2, đặt bên bậc bàn thờ lấy VANESSA nét, RYAN và MAYA cùng khung",
  "VANESSA đứng giữa khung, chiếc clutch da đen đã MỞ NẮP trong tay trái. RYAN đứng sát bên trái cô, thấy rõ mặt. "
  "MAYA đứng ở rìa PHẢI khung cách hai bước, thấy rõ mặt. Hậu cảnh là lối đi thảm đỏ và các hàng ghế.",
  "VANESSA tay trái giữ chiếc clutch đã mở, tay phải vừa rút ra một xấp tiền giấy dày bó dải giấy trắng. "
  "RYAN một tay đưa lên định cản. MAYA hai tay buông thẳng.",
  "VANESSA nhìn xuống xấp tiền trong tay mình. RYAN nhìn VANESSA. MAYA nhìn xấp tiền.",
  "VANESSA — người sắp làm một việc mà cô cho là hào phóng: khoé môi cong, mắt sáng. "
  "RYAN — bắt đầu thấy chuyện đi quá xa: mày chau. MAYA — nhìn xấp tiền và đã biết nó sẽ bay đi đâu: mặt bất động.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA vung tay ném xấp tiền lên",
  ["VANESSA_DO", "RYAN_CUOI", "MAYA_CUOI", "PROP_TIEN"], "bậc bàn thờ",
  {"VANESSA": "đứng giữa khung", "RYAN": "đứng sát bên trái VANESSA", "MAYA": "đứng rìa phải khung"},
  "MAYA cách VANESSA hai bước", {"VANESSA": "tay trái giữ clutch mở, tay phải cầm xấp tiền",
                                 "RYAN": "một tay đưa lên định cản", "MAYA": "hai tay buông thẳng"})
V("15", [22, 23], "trung 50mm · VANESSA NÉT giữa cầm xấp tiền + RYAN NÉT trái + MAYA NÉT rìa phải",
  [("VANESSA", "VANESSA_DO"), ("RYAN", "RYAN_CUOI"), ("MAYA", "MAYA_CUOI")],
  "VANESSA, RYAN và MAYA, cả ba rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN đưa tay định cản, VANESSA rút xấp tiền ra khỏi chiếc túi cầm tay",
  [("RYAN", "uneasy, low", 22), ("VANESSA", "bright, generous", 23)],
  [("MAYA", "silent, watching the money")],
  ketclip="Cuối clip, VANESSA vung tay ném xấp tiền về phía MAYA, các cọc tiền rơi tung toé xuống bậc đá và thảm đỏ "
          "dưới chân cô. Clip dừng đúng lúc cọc tiền cuối cùng chạm sàn.")

S("16", "cận-trung 85mm, cao 1m40, cách GUEST TWO 1m6, máy đặt trong lòng hàng ghế ngang tầm người ngồi",
  "GUEST TWO ngồi ở nửa PHẢI khung trong hàng ghế, đã xoay hẳn người về phía lối đi. GUEST ONE ngồi cạnh ở nửa TRÁI "
  "khung, người ngả ra sau. Hậu cảnh là lưng ghế gỗ và một góc lối đi thảm đỏ có vài tờ tiền rơi.",
  "GUEST TWO một tay bám vào lưng ghế trước, tay kia chỉ nhanh về phía bậc bàn thờ ngoài khung. "
  "GUEST ONE hai tay đặt trên đùi.",
  "Cả hai nhìn về phía bậc bàn thờ ngoài khung. TUYỆT ĐỐI không ai nhìn vào ống kính.",
  "GUEST TWO — không tin nổi thứ vừa xảy ra trong một nhà thờ: mắt mở to, miệng mở. "
  "GUEST ONE — lắc đầu chậm, mặt cứng lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả hai người quay sang nhìn nhau",
  ["GUEST2_LUA", "GUEST1_COMLE", "PROP_TIEN"], "hàng ghế thứ hai bên trái lối đi",
  {"GUEST TWO": "ngồi nửa phải khung, xoay người ra lối đi", "GUEST ONE": "ngồi nửa trái khung, ngả ra sau"},
  "ngồi sát cạnh nhau", {"GUEST TWO": "một tay bám lưng ghế, tay kia chỉ về bậc bàn thờ",
                         "GUEST ONE": "hai tay đặt trên đùi"})
V("16", [24], "cận-trung 85mm · GUEST TWO NÉT phải + GUEST ONE NÉT trái, cùng hàng ghế",
  [("GUEST TWO", "GUEST2_LUA"), ("GUEST ONE", "GUEST1_COMLE")],
  "GUEST TWO và GUEST ONE, cả hai rõ mặt trong hàng ghế. Khách khác mờ, không ai nhìn vào camera.",
  "GUEST TWO xoay người ra lối đi và chỉ tay về phía bậc bàn thờ",
  [("GUEST TWO", "incredulous, hushed", 24)], [("GUEST ONE", "silent, shaking his head slowly")])

S("17", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt bên bậc bàn thờ lấy cả hai người và mặt sàn có tiền rơi",
  "MAYA đứng ở nửa PHẢI khung, quanh chân cô trên bậc đá và thảm đỏ là xấp tiền vừa bị ném tung, các cọc nằm rải rác. "
  "VANESSA đứng ở nửa TRÁI khung cách hai bước, chiếc clutch đã đóng lại trong tay.",
  "VANESSA một tay cầm chiếc clutch đã đóng, tay kia hất nhẹ về phía đống tiền dưới sàn. MAYA hai tay buông thẳng, "
  "chưa chạm vào gì.",
  "VANESSA nhìn xuống đống tiền rồi ngước lên nhìn MAYA. MAYA nhìn thẳng vào VANESSA, chưa nhìn xuống sàn.",
  "VANESSA — người vừa trả tiền cho một màn diễn và muốn xem nốt: cằm hếch, mắt nheo nhẹ. "
  "MAYA — đứng giữa đống tiền của người khác và không nhúc nhích: mặt phẳng, hơi thở đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA khuỵu gối xuống nhặt tờ tiền đầu tiên",
  ["MAYA_CUOI", "VANESSA_DO", "PROP_TIEN"], "bậc bàn thờ, tiền rơi rải dưới chân MAYA",
  {"MAYA": "đứng nửa phải khung giữa đống tiền", "VANESSA": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "hai tay buông thẳng, chưa chạm gì", "VANESSA": "một tay cầm clutch đã đóng"})
V("17", [25], "trung 50mm · VANESSA NÉT trái + MAYA NÉT phải đứng giữa đống tiền rơi",
  [("VANESSA", "VANESSA_DO"), ("MAYA", "MAYA_CUOI")],
  "VANESSA và MAYA, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "VANESSA hất cằm về phía đống tiền dưới chân MAYA",
  [("VANESSA", "casual, dismissive", 25)], [("MAYA", "silent, not looking down yet")],
  ketclip="Cuối clip, MAYA từ từ khuỵu một gối rồi cả hai gối xuống bậc đá và bắt đầu nhặt tờ tiền đầu tiên. "
          "Clip dừng đúng lúc bàn tay cô chạm vào tờ tiền.")

S("18", "cận 85mm, cao 0m70, cách MAYA 1m4, máy hạ thấp ngang tầm người đang quỳ, lấy MAYA nét và VANESSA phía sau",
  "MAYA quỳ hai gối trên bậc đá ở nửa PHẢI khung, đang nhặt và xếp các cọc tiền thành một chồng vuông vắn trên đùi. "
  "VANESSA đứng phía sau ở nửa TRÁI khung, cao hơn hẳn trong khung, thấy rõ mặt.",
  "MAYA hai tay gom các tờ tiền lại, ngón cái vuốt cho mép chồng tiền thẳng. VANESSA một tay chống hông.",
  "MAYA nhìn xuống chồng tiền trong tay. VANESSA nhìn xuống MAYA.",
  "MAYA — người đang đếm chính xác vì đó là việc duy nhất còn kiểm soát được: mắt tập trung, môi mấp máy theo số đếm. "
  "VANESSA — thấy đúng thứ mình chờ và thích thú: khoé môi kéo lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt cọc tiền cuối cùng lên chồng",
  ["MAYA_CUOI", "VANESSA_DO", "PROP_TIEN"], "bậc bàn thờ, MAYA quỳ dưới sàn",
  {"MAYA": "quỳ hai gối nửa phải khung", "VANESSA": "đứng phía sau nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "hai tay gom và vuốt thẳng chồng tiền", "VANESSA": "một tay chống hông"})
V("18", [26, 27], "cận 85mm hạ thấp · MAYA NÉT quỳ dưới sàn xếp tiền + VANESSA NÉT đứng phía sau",
  [("MAYA", "MAYA_CUOI"), ("VANESSA", "VANESSA_DO")],
  "MAYA rõ mặt đang quỳ dưới sàn, VANESSA rõ mặt đứng phía sau cao hơn. "
  "Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA vuốt cho mép chồng tiền thẳng rồi ngẩng lên, VANESSA quay sang nói với đám đông",
  [("MAYA", "flat, precise", 26), ("VANESSA", "gleeful, light", 27)])

S("19", "cận-trung 85mm, cao 0m80, cách MAYA 1m5, máy hạ thấp ngang tầm người đang quỳ",
  "MAYA quỳ hai gối ở nửa PHẢI khung, hai tay giữ chồng tiền đã xếp vuông vắn ngang ngực. VANESSA đứng ở nửa TRÁI "
  "khung cách hai bước, thấy rõ mặt. Hậu cảnh là bậc đá bàn thờ và thảm đỏ.",
  "MAYA hai tay giữ chồng tiền ngang ngực, chưa chìa ra. VANESSA hai tay buông, một tay cầm clutch.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đang nói ra một con số mà mình sống với nó hằng đêm: giọng rất bình, mắt không rời. "
  "VANESSA — nghe câu trả lời không giống kịch bản mình dựng: mày nhướn, cằm thụt lại nửa phân.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA chống gối đứng dậy",
  ["MAYA_CUOI", "VANESSA_DO", "PROP_TIEN"], "bậc bàn thờ, MAYA quỳ dưới sàn",
  {"MAYA": "quỳ hai gối nửa phải khung", "VANESSA": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "hai tay giữ chồng tiền ngang ngực", "VANESSA": "một tay cầm clutch"})
V("19", [28, 29], "cận-trung 85mm hạ thấp · MAYA NÉT quỳ cầm chồng tiền + VANESSA NÉT đứng đối diện",
  [("MAYA", "MAYA_CUOI"), ("VANESSA", "VANESSA_DO")],
  "MAYA rõ mặt đang quỳ, VANESSA rõ mặt đứng đối diện. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA giữ chồng tiền đã xếp vuông vắn và nói lên từ dưới sàn",
  [("MAYA", "calm, exact", 28), ("VANESSA", "thrown, clipped", 29)],
  ketclip="Cuối clip, MAYA chống gối đứng thẳng dậy và chìa chồng tiền ra trước mặt VANESSA. "
          "Clip dừng đúng lúc cánh tay cô duỗi hết.")

S("20", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt bên bậc bàn thờ lấy cả ba người",
  "MAYA đứng thẳng ở nửa PHẢI khung, một tay chìa chồng tiền ra trước mặt VANESSA. VANESSA đứng ở nửa TRÁI khung "
  "chưa cầm lấy. RYAN đứng sát sau VANESSA, thấy rõ mặt, đã bước lên nửa bước.",
  "MAYA một tay chìa chồng tiền ra, tay kia buông. VANESSA hai tay giữ nguyên bên mình. RYAN một tay đưa ra "
  "phía MAYA rồi dừng lại giữa chừng.",
  "MAYA nhìn thẳng vào VANESSA. VANESSA nhìn chồng tiền chìa ra. RYAN nhìn MAYA.",
  "MAYA — người vừa định giá lại cả cuộc mua bán này và trả hàng: giọng đều, tay không run. "
  "VANESSA — bị trả lại thứ mình ném đi: quai hàm siết. RYAN — thấy mình bị gọi tên thành một món hàng: mặt đỏ lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA giật lấy chồng tiền",
  ["MAYA_CUOI", "VANESSA_DO", "RYAN_CUOI", "PROP_TIEN"], "bậc bàn thờ",
  {"MAYA": "đứng thẳng nửa phải khung", "VANESSA": "đứng nửa trái khung", "RYAN": "đứng sát sau VANESSA"},
  "cách nhau hai bước", {"MAYA": "một tay chìa chồng tiền ra", "VANESSA": "hai tay giữ nguyên bên mình",
                         "RYAN": "một tay đưa ra rồi dừng giữa chừng"})
V("20", [30, 31], "trung 50mm · MAYA NÉT phải chìa tiền + VANESSA NÉT trái + RYAN NÉT sát sau VANESSA",
  [("MAYA", "MAYA_CUOI"), ("VANESSA", "VANESSA_DO"), ("RYAN", "RYAN_CUOI")],
  "MAYA, VANESSA và RYAN, cả ba rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA chìa chồng tiền thẳng ra trước mặt VANESSA và giữ yên tay",
  [("MAYA", "level, unhurried", 30), ("RYAN", "stung, low", 31)],
  [("VANESSA", "silent, jaw tight")])

S("21", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt chếch bên bậc bàn thờ lấy MAYA và PRIEST",
  "MAYA đứng ở nửa PHẢI khung, hai tay đã buông xuống, chồng tiền không còn trong tay. PRIEST đứng ở nửa TRÁI khung "
  "cạnh bục giảng, hai tay ôm cuốn sách lễ vào ngực. Hậu cảnh là bệ bàn thờ đá trắng và các hàng ghế có khách.",
  "MAYA hai tay buông xuôi, các ngón hơi run. PRIEST hai tay ôm sách lễ vào ngực.",
  "MAYA nhìn PRIEST khi cảm ơn rồi quay mặt ra phía các hàng ghế. PRIEST nhìn MAYA.",
  "MAYA — người đang tự tay đóng lại đám cưới của chính mình: giọng rõ ràng, mắt khô, cằm ngẩng. "
  "PRIEST — thương và bất lực: mày chau, khoé môi trễ.",
  "đúng khoảnh khắc ngay TRƯỚC khi các hàng ghế phía sau bắt đầu đứng dậy",
  ["MAYA_CUOI", "PRIEST"], "bậc bàn thờ, cạnh bục giảng",
  {"MAYA": "đứng nửa phải khung", "PRIEST": "đứng nửa trái khung cạnh bục giảng"},
  "cách nhau một bước", {"MAYA": "hai tay buông xuôi", "PRIEST": "hai tay ôm sách lễ vào ngực"})
V("21", [32], "trung 50mm · MAYA NÉT phải + PRIEST NÉT trái cạnh bục giảng",
  [("MAYA", "MAYA_CUOI"), ("PRIEST", "PRIEST")],
  "MAYA và PRIEST, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA quay sang cảm ơn PRIEST rồi quay mặt ra nói với cả gian phòng",
  [("MAYA", "clear, composed", 32)], [("PRIEST", "silent, pained")],
  ketclip="Cuối clip, VANESSA quay gót bước xuống lối đi giữa về phía cửa lớn, RYAN đi theo sau cô. "
          "Clip dừng đúng lúc hai người đi khuất khỏi khung.")

# ─────────────────────────── CUỐI LỐI ĐI: ADRIAN ───────────────────────────
S("22", "trung 50mm, cao 1m40, cách VANESSA 2m6, đặt ở cuối lối đi phía cửa lớn, hạ thấp để lấy cả người ngồi xe lăn",
  "VANESSA đang đi tới ở nửa TRÁI khung, đã xuống gần hết lối đi. ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, "
  "đỗ ngay mép lối đi cạnh hàng ghế cuối, chắn một phần đường ra. Hậu cảnh là hai cánh cửa gỗ lớn.",
  "VANESSA một tay cầm clutch, tay kia vén nhẹ vạt váy. ADRIAN hai tay đặt trên vành tay vịn của xe lăn.",
  "VANESSA nhìn xuống chiếc xe lăn chắn đường. ADRIAN nhìn thẳng vào mặt VANESSA.",
  "VANESSA — người bị một vật cản làm chậm mất ba giây: cằm hếch, mày nhíu, giọng gọn. "
  "ADRIAN — người quen bị nói về mình như nói về đồ đạc: mặt bất động, mắt tĩnh và ghi nhớ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN lùi xe lăn nhường đường",
  ["VANESSA_DO", "ADRIAN_NHATHO"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"VANESSA": "đi tới ở nửa trái khung", "ADRIAN": "ngồi xe lăn ở nửa phải khung, mép lối đi"},
  "cách nhau hai mét", {"VANESSA": "một tay cầm clutch, tay kia vén vạt váy",
                        "ADRIAN": "hai tay đặt trên vành tay vịn xe lăn"})
V("22", [33, 34], "trung 50mm hạ thấp · VANESSA NÉT trái đang đi tới + ADRIAN NÉT phải ngồi xe lăn",
  [("VANESSA", "VANESSA_DO"), ("ADRIAN", "ADRIAN_NHATHO")],
  "VANESSA và ADRIAN, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "VANESSA dừng lại trước chiếc xe lăn chắn một phần lối đi",
  [("VANESSA", "brisk, imperious", 33), ("ADRIAN", "quiet, even", 34)])

S("23", "cận-trung 85mm, cao 1m50, cách VANESSA 1m8, đặt cuối lối đi lấy VANESSA nét và RYAN phía sau",
  "VANESSA đứng chính diện ở nửa TRÁI khung. RYAN đứng phía sau bên phải cô, thấy rõ mặt, một tay còn giữ chiếc micro. "
  "Ở rìa PHẢI tiền cảnh thấy một phần vai và tay vịn xe lăn của ADRIAN, out nét.",
  "VANESSA một tay chỉ xuống phía xe lăn ngoài khung. RYAN hai tay buông, vai chùng xuống.",
  "VANESSA nhìn sang RYAN khi ra lệnh. RYAN nhìn xuống chiếc xe lăn.",
  "VANESSA — người không quen phải đi vòng qua bất cứ thứ gì: mắt lạnh, giọng gọn. "
  "RYAN — đã bắt đầu thấy mình phải làm những việc mình không muốn: mày chau, môi mím.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước một bước tránh sang bên",
  ["VANESSA_DO", "RYAN_CUOI", "ADRIAN_NHATHO"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"VANESSA": "đứng chính diện nửa trái khung", "RYAN": "đứng phía sau bên phải VANESSA",
   "ADRIAN": "một phần vai và tay vịn xe lăn ở rìa phải tiền cảnh"},
  "cách nhau một bước", {"VANESSA": "một tay chỉ xuống phía xe lăn", "RYAN": "một tay giữ micro, vai chùng",
                         "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
V("23", [35, 36], "cận-trung 85mm · VANESSA NÉT trái + RYAN NÉT phía sau phải · vai và tay vịn xe lăn ADRIAN rìa phải out nét",
  [("VANESSA", "VANESSA_DO"), ("RYAN", "RYAN_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "VANESSA và RYAN rõ mặt. ADRIAN chỉ thấy một phần VAI và tay vịn xe lăn ở rìa phải tiền cảnh, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "VANESSA chỉ tay xuống chiếc xe lăn và ra lệnh, RYAN đứng nguyên",
  [("VANESSA", "curt, imperious", 35), ("RYAN", "reluctant, low", 36)])

S("24", "cận 85mm, cao 1m30, cách ADRIAN 1m3, máy sau vai PHẢI của VANESSA; vai và gáy VANESSA chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung, ngước lên. VANESSA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, "
  "ngoài vùng nét, đứng cao hơn hẳn anh. Hậu cảnh sau lưng ADRIAN là hai cánh cửa gỗ lớn cuối nhà thờ.",
  "ADRIAN hai tay đặt hờ trên vành tay vịn xe lăn, các ngón thả lỏng.",
  "ADRIAN nhìn thẳng lên mặt VANESSA.",
  "ADRIAN — người đang nghe một câu sẽ được nhắc lại rất lâu về sau: mặt hoàn toàn bình, mắt tĩnh, không chớp.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA bước vòng qua xe lăn và đi khỏi",
  ["ADRIAN_NHATHO", "VANESSA_DO"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"ADRIAN": "ngồi xe lăn giữa khung", "VANESSA": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"ADRIAN": "hai tay đặt hờ trên vành tay vịn", "VANESSA": "một tay cầm clutch, ngoài vùng nét"})
V("24", [37], "OTS cận 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy VANESSA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_NHATHO"), ("VANESSA", "VANESSA_DO")],
  "ADRIAN rõ mặt ngồi trong xe lăn. VANESSA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "VANESSA nói xuống phía chiếc xe lăn rồi bước vòng qua",
  [("VANESSA", "imperious, amused", 37)], [("ADRIAN", "silent, perfectly still")],
  ketclip="Cuối clip, VANESSA đi khuất khỏi khung về phía cửa lớn, ADRIAN quay đầu nhìn theo rồi ngoảnh sang phải "
          "về phía hàng ghế cuối. Clip dừng đúng lúc anh quay xong.")

S("25", "two-shot cận-trung 85mm, cao 1m30, cách ADRIAN 1m8, máy hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, cạnh hàng ghế cuối. SEBASTIAN đứng ở nửa PHẢI khung, đã cúi người "
  "xuống ngang tầm tai anh, một tay chống lên lưng ghế gỗ. Hậu cảnh là hai cánh cửa gỗ lớn và các hàng ghế cuối.",
  "ADRIAN hai tay đặt trên vành tay vịn. SEBASTIAN một tay chống lưng ghế, tay kia giữ bìa kẹp hồ sơ da nâu ép sát người.",
  "ADRIAN nhìn thẳng về phía cửa lớn, không quay sang. SEBASTIAN nhìn nghiêng xuống ADRIAN.",
  "ADRIAN — người vừa quyết định xong một việc và chỉ cần nói tên người thực hiện: mặt bình, mắt thẳng. "
  "SEBASTIAN — chờ lệnh, đã nghiêng sẵn tai: mày nhướn nhẹ, môi khép.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN mở bìa kẹp hồ sơ ra",
  ["ADRIAN_NHATHO", "SEBASTIAN"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "SEBASTIAN": "đứng cúi người nửa phải khung"},
  "cách nhau nửa mét", {"ADRIAN": "hai tay trên vành tay vịn", "SEBASTIAN": "một tay chống lưng ghế, tay kia giữ bìa kẹp hồ sơ"})
V("25", [38, 39], "two-shot cận-trung 85mm · ADRIAN NÉT trái ngồi xe lăn + SEBASTIAN NÉT phải cúi người xuống",
  [("ADRIAN", "ADRIAN_NHATHO"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN và SEBASTIAN, cả hai rõ mặt. Không ai khác trong khung ngoài các hàng ghế trống phía sau.",
  "ADRIAN gọi tên mà không quay đầu, SEBASTIAN cúi xuống ngang tầm tai anh",
  [("ADRIAN", "quiet, level", 38), ("SEBASTIAN", "attentive, low", 39)])

S("26", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m6, máy hạ thấp lấy ADRIAN nét, SEBASTIAN cúi trong khung",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. SEBASTIAN vẫn cúi người ở nửa PHẢI khung, bìa kẹp hồ sơ da nâu "
  "ĐÃ MỞ trên cẳng tay, một cây bút cầm sẵn. Hậu cảnh là các hàng ghế cuối và một phần cửa gỗ lớn.",
  "ADRIAN một tay hơi nhấc lên khỏi vành tay vịn, hất nhẹ về phía lòng nhà thờ. SEBASTIAN một tay đỡ bìa kẹp hồ sơ "
  "đã mở, tay kia cầm bút chưa đặt xuống giấy.",
  "ADRIAN nhìn về phía lòng nhà thờ nơi khách đang lục tục đứng dậy. SEBASTIAN nhìn nghiêng xuống ADRIAN.",
  "ADRIAN — người đang ra một mệnh lệnh rất bình thản về những người vừa cười: giọng đều, mắt không rời đám đông. "
  "SEBASTIAN — nghề nghiệp, chờ chính xác từng chữ: mắt hơi nheo.",
  "đúng khoảnh khắc ngay TRƯỚC khi ngòi bút của SEBASTIAN chạm xuống giấy",
  ["ADRIAN_NHATHO", "SEBASTIAN"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "SEBASTIAN": "cúi người nửa phải khung, bìa hồ sơ đã mở"},
  "cách nhau nửa mét", {"ADRIAN": "một tay hất nhẹ về phía lòng nhà thờ",
                        "SEBASTIAN": "một tay đỡ bìa hồ sơ mở, tay kia cầm bút"})
V("26", [40, 41], "cận-trung 85mm · ADRIAN NÉT trái ngồi xe lăn + SEBASTIAN NÉT phải cúi cầm bút",
  [("ADRIAN", "ADRIAN_NHATHO"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN và SEBASTIAN, cả hai rõ mặt. Khách hậu cảnh mờ, không ai nhìn vào camera.",
  "ADRIAN hất nhẹ tay về phía lòng nhà thờ, SEBASTIAN mở bìa kẹp hồ sơ và cầm sẵn bút",
  [("ADRIAN", "quiet, deliberate", 40), ("SEBASTIAN", "professional, low", 41)])

S("27", "cận 85mm, cao 1m30, cách ADRIAN 1m2, máy sau vai TRÁI của SEBASTIAN; vai và gáy SEBASTIAN chiếm rìa trái, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung, mặt hướng chếch về phía bậc bàn thờ ở xa. SEBASTIAN chỉ còn là "
  "vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng ADRIAN là lối đi thảm đỏ chạy hút về bàn thờ.",
  "ADRIAN hai tay đặt lại trên vành tay vịn, các ngón khép.",
  "ADRIAN nhìn dọc lối đi về phía bậc bàn thờ ở xa.",
  "ADRIAN — người vừa tách một cái tên ra khỏi tất cả những cái tên còn lại: giọng rất nhỏ, mắt dịu đi một chút "
  "so với mọi khung trước.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN quay xe lăn về phía cửa lớn",
  ["ADRIAN_NHATHO", "SEBASTIAN"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"ADRIAN": "ngồi xe lăn giữa khung", "SEBASTIAN": "vai và gáy tiền cảnh trái"},
  "cách nhau nửa mét", {"ADRIAN": "hai tay đặt trên vành tay vịn", "SEBASTIAN": "tay cầm bút, ngoài vùng nét"})
V("27", [42], "OTS cận 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy SEBASTIAN tiền cảnh trái out nét",
  [("ADRIAN", "ADRIAN_NHATHO"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN rõ mặt ngồi trong xe lăn. SEBASTIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "ADRIAN nhìn dọc lối đi về phía bậc bàn thờ ở xa rồi nói",
  [("ADRIAN", "quiet, softer", 42)], [("SEBASTIAN", "silent, writing")])

# ─────────────────────────── NHỊP KHÉP CẢNH ───────────────────────────
S("B3", "toàn cảnh 24mm, cao 1m60, cách MAYA 18m, đặt ở cuối lối đi phía cửa lớn nhìn về bàn thờ",
  "Lòng nhà thờ đã vãn, các hàng ghế gần hết người, vài vị khách cuối cùng đang đi ra dọc lối đi. MAYA đứng một mình "
  "trên bậc bàn thờ ở cuối lối đi. ADRIAN ngồi trong xe lăn ở tiền cảnh gần, cạnh hàng ghế cuối, quay lưng lại "
  "một phần về phía máy quay và nhìn về phía cô.",
  "MAYA hai tay buông xuôi. ADRIAN hai tay đặt trên vành tay vịn xe lăn.",
  "MAYA nhìn xuống mặt thảm đỏ trước chân mình. ADRIAN nhìn dọc lối đi về phía MAYA. "
  "Khách nền không nhìn vào ống kính.",
  "MAYA — người vừa mất mọi thứ trong hai mươi phút và vẫn đang đứng: vai cân, cằm ngang, mặt trống. "
  "ADRIAN — người vừa nhìn thấy điều mình đợi sáu tháng: mắt tĩnh, môi khép.",
  "đúng khoảnh khắc ngay TRƯỚC khi vị khách cuối cùng bước qua cánh cửa lớn",
  ["MAYA_CUOI", "ADRIAN_NHATHO"], "lòng nhà thờ, từ hàng ghế cuối tới bậc bàn thờ",
  {"MAYA": "đứng một mình trên bậc bàn thờ", "ADRIAN": "ngồi xe lăn tiền cảnh gần, cạnh hàng ghế cuối"},
  "cách nhau mười tám mét", {"MAYA": "hai tay buông xuôi", "ADRIAN": "hai tay trên vành tay vịn"})
B("B3", "Khép cảnh. Nhà thờ vãn dần. MAYA đứng một mình trên bậc bàn thờ, ADRIAN ngồi xe lăn ở cuối lối đi nhìn lên.",
  "toàn cảnh 24mm · MAYA NÉT một mình trên bậc bàn thờ + ADRIAN NÉT tiền cảnh gần ngồi xe lăn · vài khách cuối mờ",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA rõ mặt ở cuối lối đi, ADRIAN rõ mặt ở tiền cảnh gần trong xe lăn. Vài vị khách cuối cùng đi ra, mờ, "
  "không ai nhìn vào camera.",
  "một gian phòng vừa chứa hai trăm người giờ chỉ còn hai người không quen nhau, và khoảng cách giữa họ chính là "
  "nội dung của khung hình này.",
  "vài vị khách cuối cùng đi ra khỏi khung; MAYA đứng yên trên bậc bàn thờ, một cánh hoa cúc trắng rơi khỏi bó hoa "
  "đầu hàng ghế; ADRIAN không nhúc nhích.",
  "Ambient tiếng vọng của gian nhà thờ đá, tiếng bước chân xa dần và tiếng cửa gỗ khép lại.",
  nhac("KÌM", "Cô đang giữ phẩm giá trước cả một gian phòng và không cho ai thấy mình gãy — nhạc phải kìm dưới mức "
              "cảm xúc thật, không được khóc thay nhân vật.",
       "Soul ballad at 62 BPM with a raw female alto sung very close to the mic, smoky and almost spoken; sparse Rhodes "
       "and upright bass only, brushed drums entering just once near the end; one held note at the midpoint then "
       "straight back down to voice and Rhodes; lyrics about standing alone at the front of a room after everyone has "
       "gone home, head up, never pleading; dry intimate mix, female vocal, soul, restrained, sparse",
       "Chamber instrumental at 58 BPM; a single cello holding one long low note under a felt-piano figure that repeats "
       "and gets quieter each time, a second cello answering a tone below, no percussion, no build, ending unresolved; "
       "very quiet, close-miked, room tone audible; cello, piano, minimal, unresolved"),
  dur=10)
