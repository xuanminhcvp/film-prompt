# -*- coding: utf-8 -*-
"""SCENE 12 — PHÒNG KÍNH TẦNG 40 (ban ngày). Hai mươi phút để sa thải một người."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S12", "REF_VANPHONG_NGAY", qc=qc.S12)

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách SEBASTIAN 5m, đặt ở góc phòng phía vách kính ngoài trời",
  "SEBASTIAN đứng giữa phòng làm việc, chưa ngồi, bìa kẹp hồ sơ da nâu kẹp dưới cánh tay. MR. HALLORAN đứng "
  "sau bàn làm việc, một tay còn đặt trên lưng chiếc ghế da đen, chưa ngồi xuống. Cửa kính ra hành lang đã đóng.",
  "SEBASTIAN một tay giữ bìa kẹp hồ sơ dưới cánh tay, tay kia buông. MR. HALLORAN một tay đặt trên lưng ghế da, "
  "tay kia cầm chiếc vest gấp.",
  "SEBASTIAN nhìn thẳng vào MR. HALLORAN. MR. HALLORAN nhìn lại SEBASTIAN.",
  "SEBASTIAN — người đến đây với đúng một việc và không có ý định giải thích: mặt hoàn toàn bình. "
  "MR. HALLORAN — chủ nhà nhưng đang là người phải chờ: mồ hôi rịn ở thái dương, mắt hơi nheo.",
  "đúng khoảnh khắc ngay TRƯỚC khi MR. HALLORAN kéo ghế ngồi xuống",
  ["SEBASTIAN", "MR. HALLORAN"], "giữa phòng làm việc, trước bàn",
  {"SEBASTIAN": "đứng giữa phòng", "MR. HALLORAN": "đứng sau bàn làm việc"},
  "cách nhau một mặt bàn", {"SEBASTIAN": "một tay giữ bìa hồ sơ dưới cánh tay",
                            "MR. HALLORAN": "một tay trên lưng ghế da, tay kia cầm vest gấp"})
B("B1", "Mở cảnh. Tầng bốn mươi. SEBASTIAN đứng giữa phòng kính, MR. HALLORAN chưa dám ngồi xuống.",
  "trung-rộng 35mm · SEBASTIAN NÉT đứng giữa phòng + MR. HALLORAN NÉT đứng sau bàn · không có ai khác",
  [("SEBASTIAN", "SEBASTIAN"), ("MR. HALLORAN", "MR. HALLORAN")],
  "SEBASTIAN và MR. HALLORAN rõ mặt. Không có người nào khác trong phòng; qua vách kính hành lang phía sau "
  "không thấy ai.",
  "một người đứng trong phòng của người khác và chưa nói câu nào, nhưng ai là chủ căn phòng này thì đã rõ ngay "
  "từ giây đầu tiên.",
  "SEBASTIAN đứng yên, mắt quét một lượt qua bàn làm việc; MR. HALLORAN chuyển chiếc vest từ tay này sang tay kia "
  "rồi đặt xuống lưng ghế; ánh sáng ban ngày trắng tràn qua vách kính.",
  "Ambient tiếng ù rất khẽ của điều hoà trên tầng cao và tiếng thành phố xa dưới kính.",
  nhac("KÌM", "Cả cảnh là quyền lực nói bằng giọng lịch sự; nhạc phải lạnh và nén, không được kịch tính hoá.",
       "Minimal soul at 70 BPM; an upright bass walking alone under one sustained Rhodes chord, a female alto "
       "entering once with a single low line; brushed drums extremely quiet; the pull is when the bass stops for "
       "a full bar; lyrics about a room changing owner without anyone raising their voice; dry mix, female vocal, "
       "upright bass, Rhodes, cold, restrained",
       "Minimal instrumental at 68 BPM; upright bass walking alone, a single sustained synth pad above it, "
       "one muted trumpet note near the end, no drums, stopping rather than resolving; "
       "cold clean mix, upright bass, pad, trumpet, restrained"),
  dur=6)

# ── SEBASTIAN VÀ HALLORAN ──
S("01", "two-shot trung 50mm, cao 1m40, cách SEBASTIAN 2m4, đặt bên bàn làm việc lấy cả hai người ngồi",
  "SEBASTIAN ngồi ở nửa PHẢI khung trên ghế khách bọc da đen, lưng thẳng. MR. HALLORAN ngồi ở nửa TRÁI khung "
  "sau bàn làm việc mặt gỗ veneer. Hậu cảnh là vách kính nhìn ra thành phố.",
  "SEBASTIAN hai tay đặt chồng lên bìa kẹp hồ sơ da nâu trên đùi. MR. HALLORAN hai tay đặt trên mặt bàn, "
  "các ngón đan vào nhau.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "SEBASTIAN — người mở đầu bằng một câu hỏi mà mình đã biết câu trả lời: giọng đều, mắt tĩnh. "
  "MR. HALLORAN — người không được báo trước và đang dò xem mình đang nói chuyện với ai: mày nhướn, giọng thận trọng.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN mở bìa kẹp hồ sơ ra",
  ["SEBASTIAN", "MR. HALLORAN"], "hai bên bàn làm việc",
  {"SEBASTIAN": "ngồi ghế khách nửa phải khung", "MR. HALLORAN": "ngồi sau bàn nửa trái khung"},
  "cách nhau một mặt bàn", {"SEBASTIAN": "hai tay đặt chồng lên bìa kẹp hồ sơ trên đùi",
                            "MR. HALLORAN": "hai tay đan vào nhau trên mặt bàn"})
V("01", [0, 1], "two-shot trung 50mm · MR. HALLORAN NÉT trái sau bàn + SEBASTIAN NÉT phải trên ghế khách",
  [("SEBASTIAN", "SEBASTIAN"), ("MR. HALLORAN", "MR. HALLORAN")],
  "SEBASTIAN và MR. HALLORAN, cả hai rõ mặt. Không có ai khác trong phòng.",
  "SEBASTIAN ngồi thẳng lưng và hỏi trước, MR. HALLORAN đan hai tay lại trên mặt bàn",
  [("SEBASTIAN", "even, opening", 0), ("MR. HALLORAN", "cautious, probing", 1)])

S("02", "cận-trung 85mm, cao 1m40, cách SEBASTIAN 1m6, máy sau vai TRÁI của MR. HALLORAN; vai và gáy ông chiếm rìa trái, out nét",
  "SEBASTIAN ngồi chính diện chiếm phần lớn khung, bìa kẹp hồ sơ đã mở trên đùi. MR. HALLORAN chỉ còn là vai và "
  "gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng SEBASTIAN là vách kính hành lang và ghế băng chờ.",
  "SEBASTIAN một tay giữ bìa kẹp hồ sơ đã mở, ngón trỏ tay kia đặt lên một dòng trong đó.",
  "SEBASTIAN nhìn xuống trang hồ sơ rồi ngước lên nhìn thẳng vào mặt MR. HALLORAN.",
  "SEBASTIAN — người đọc ra một cái tên như đọc một mục trong danh sách: giọng đều, không nhấn, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MR. HALLORAN ngả người ra sau ghế",
  ["SEBASTIAN", "MR. HALLORAN"], "hai bên bàn làm việc",
  {"SEBASTIAN": "ngồi chính diện giữa khung", "MR. HALLORAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một mặt bàn", {"SEBASTIAN": "một tay giữ bìa hồ sơ mở, tay kia chỉ vào một dòng",
                            "MR. HALLORAN": "hai tay trên mặt bàn, ngoài vùng nét"})
V("02", [2, 3, 4], "OTS cận-trung 85mm · SEBASTIAN NÉT chính diện · vai và gáy MR. HALLORAN tiền cảnh trái out nét",
  [("SEBASTIAN", "SEBASTIAN"), ("MR. HALLORAN", "MR. HALLORAN")],
  "SEBASTIAN rõ mặt chính diện. MR. HALLORAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "SEBASTIAN mở bìa kẹp hồ sơ, đặt ngón tay lên một dòng và đọc lên",
  [("SEBASTIAN", "even, flat", 2), ("MR. HALLORAN", "neutral, professional", 3),
   ("SEBASTIAN", "level, final", 4)])

S("03", "cận-trung 85mm, cao 1m40, cách MR. HALLORAN 1m6, máy sau vai PHẢI của SEBASTIAN; vai và gáy ông chiếm rìa phải, out nét",
  "MR. HALLORAN ngồi chính diện chiếm phần lớn khung sau bàn làm việc. SEBASTIAN chỉ còn là vai và gáy ở rìa "
  "PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MR. HALLORAN là mảng tường ốp gỗ veneer và bức tranh trừu tượng.",
  "MR. HALLORAN một tay đưa lên nới cà vạt thêm một nấc, tay kia chống lên mép bàn.",
  "MR. HALLORAN nhìn thẳng vào mặt SEBASTIAN.",
  "MR. HALLORAN — người đang giải thích quy trình cho một người rõ ràng không quan tâm tới quy trình: "
  "mồ hôi rịn thêm ở thái dương, giọng cao lên nửa bậc.",
  "đúng khoảnh khắc ngay TRƯỚC khi MR. HALLORAN liếc đồng hồ đeo tay",
  ["MR. HALLORAN", "SEBASTIAN"], "hai bên bàn làm việc",
  {"MR. HALLORAN": "ngồi chính diện giữa khung", "SEBASTIAN": "vai và gáy tiền cảnh phải"},
  "cách nhau một mặt bàn", {"MR. HALLORAN": "một tay nới cà vạt, tay kia chống mép bàn",
                            "SEBASTIAN": "hai tay trên bìa hồ sơ, ngoài vùng nét"})
V("03", [5, 6], "OTS cận-trung 85mm · MR. HALLORAN NÉT chính diện · vai và gáy SEBASTIAN tiền cảnh phải out nét",
  [("MR. HALLORAN", "MR. HALLORAN"), ("SEBASTIAN", "SEBASTIAN")],
  "MR. HALLORAN rõ mặt chính diện. SEBASTIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MR. HALLORAN nới cà vạt thêm một nấc và chống tay lên mép bàn",
  [("MR. HALLORAN", "strained, procedural", 5), ("SEBASTIAN", "flat, immovable", 6)])

S("04", "two-shot trung 50mm, cao 1m40, cách SEBASTIAN 2m2, đặt bên bàn làm việc lấy cả hai người ngồi",
  "SEBASTIAN ngồi ở nửa PHẢI khung, bìa hồ sơ đã gập lại trên đùi. MR. HALLORAN ngồi ở nửa TRÁI khung sau bàn, "
  "một tay đã đặt lên chiếc điện thoại bàn màu ghi. Hậu cảnh là vách kính nhìn ra thành phố.",
  "SEBASTIAN hai tay đặt chồng lên bìa hồ sơ đã gập. MR. HALLORAN một tay đặt lên ống nghe điện thoại bàn, "
  "chưa nhấc lên.",
  "MR. HALLORAN nhìn SEBASTIAN. SEBASTIAN nhìn lại, không chớp mắt.",
  "MR. HALLORAN — người hỏi câu cuối cùng mà mình còn dám hỏi: giọng nhỏ, mắt dò. "
  "SEBASTIAN — trả lời bằng đúng một chữ và không thêm gì: mặt hoàn toàn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi MR. HALLORAN nhấc ống nghe lên",
  ["SEBASTIAN", "MR. HALLORAN"], "hai bên bàn làm việc",
  {"SEBASTIAN": "ngồi ghế khách nửa phải khung", "MR. HALLORAN": "ngồi sau bàn nửa trái khung"},
  "cách nhau một mặt bàn", {"SEBASTIAN": "hai tay đặt chồng lên bìa hồ sơ đã gập",
                            "MR. HALLORAN": "một tay đặt lên ống nghe điện thoại bàn"})
V("04", [7, 8], "two-shot trung 50mm · MR. HALLORAN NÉT trái sau bàn + SEBASTIAN NÉT phải trên ghế khách",
  [("SEBASTIAN", "SEBASTIAN"), ("MR. HALLORAN", "MR. HALLORAN")],
  "SEBASTIAN và MR. HALLORAN, cả hai rõ mặt. Không có ai khác trong phòng.",
  "MR. HALLORAN đặt tay lên ống nghe chiếc điện thoại bàn và hỏi câu cuối",
  [("MR. HALLORAN", "quiet, probing", 7), ("SEBASTIAN", "flat, final", 8)],
  ketclip="Cuối clip, MR. HALLORAN nhấc ống nghe lên gọi một câu ngắn, rồi SEBASTIAN đứng dậy đi ra ngoài "
          "và đứng phía sau vách kính hành lang. Clip dừng đúng lúc ông dừng lại sau tấm kính.")

# ── RYAN VÀO PHÒNG ──
S("05", "trung 50mm, cao 1m55, cách RYAN 2m4, đặt trong phòng nhìn ra phía cửa kính đang mở",
  "RYAN đứng ở nửa PHẢI khung ngay trong CỬA KÍNH ĐANG MỞ, một tay còn trên tay nắm cửa. MR. HALLORAN ngồi ở "
  "nửa TRÁI khung sau bàn. Qua vách kính phía sau RYAN thấy SEBASTIAN đứng ngoài hành lang, mờ, quay lưng lại.",
  "RYAN một tay giữ tay nắm cửa kính, tay kia cầm điện thoại di động. MR. HALLORAN hai tay đặt trên mặt bàn.",
  "RYAN nhìn ra phía hành lang rồi quay vào nhìn MR. HALLORAN. MR. HALLORAN nhìn RYAN. "
  "SEBASTIAN quay lưng, không nhìn vào phòng.",
  "RYAN — người vừa thấy nhân sự đứng ngoài cửa và bắt đầu thấy sai sai: mày chau, giọng nhanh. "
  "MR. HALLORAN — mặt cứng lại: mắt không rời mặt bàn quá một giây.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN đẩy cánh cửa kính khép lại",
  ["RYAN_COMLE", "MR. HALLORAN", "SEBASTIAN"], "cửa kính vào phòng làm việc",
  {"RYAN": "đứng trong cửa kính đang mở, nửa phải khung", "MR. HALLORAN": "ngồi sau bàn nửa trái khung",
   "SEBASTIAN": "đứng ngoài hành lang sau vách kính, quay lưng, mờ"},
  "RYAN cách bàn ba mét", {"RYAN": "một tay giữ tay nắm cửa, tay kia cầm điện thoại",
                           "MR. HALLORAN": "hai tay đặt trên mặt bàn", "SEBASTIAN": "hai tay buông, quay lưng"})
V("05", [9, 10], "trung 50mm · RYAN NÉT phải trong cửa kính + MR. HALLORAN NÉT trái sau bàn · SEBASTIAN mờ quay lưng ngoài hành lang",
  [("RYAN", "RYAN_COMLE"), ("MR. HALLORAN", "MR. HALLORAN"), ("SEBASTIAN", "SEBASTIAN")],
  "RYAN và MR. HALLORAN rõ mặt. SEBASTIAN chỉ thấy dáng người MỜ phía sau vách kính hành lang, QUAY LƯNG, "
  "TUYỆT ĐỐI KHÔNG quay mặt lại.",
  "MR. HALLORAN gọi RYAN vào, RYAN đứng lại ở cửa và nhìn ra phía hành lang",
  [("MR. HALLORAN", "tight, formal", 9), ("RYAN", "quick, uneasy", 10)])

S("06", "two-shot trung 50mm, cao 1m50, cách RYAN 2m2, đặt bên bàn làm việc lấy cả hai người",
  "RYAN đứng ở nửa PHẢI khung trước bàn, chưa ngồi. MR. HALLORAN ngồi ở nửa TRÁI khung sau bàn. "
  "Hậu cảnh là vách kính nhìn ra thành phố ban ngày.",
  "RYAN hai tay buông dọc thân, một tay còn nắm chiếc điện thoại. MR. HALLORAN hai tay đặt phẳng trên mặt bàn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MR. HALLORAN — người đọc ra một câu đã được soạn sẵn trong đầu: giọng đều, mắt không rời mặt bàn quá lâu. "
  "RYAN — chưa tin nổi thứ mình vừa nghe: mày nhướn cao, miệng hé, giọng bật lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN đặt chiếc điện thoại xuống mặt bàn",
  ["RYAN_COMLE", "MR. HALLORAN"], "trước bàn làm việc",
  {"RYAN": "đứng trước bàn nửa phải khung", "MR. HALLORAN": "ngồi sau bàn nửa trái khung"},
  "cách nhau một mặt bàn", {"RYAN": "hai tay buông, một tay nắm điện thoại",
                            "MR. HALLORAN": "hai tay đặt phẳng trên mặt bàn"})
V("06", [11, 12], "two-shot trung 50mm · MR. HALLORAN NÉT trái sau bàn + RYAN NÉT phải đứng trước bàn",
  [("MR. HALLORAN", "MR. HALLORAN"), ("RYAN", "RYAN_COMLE")],
  "MR. HALLORAN và RYAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MR. HALLORAN đặt hai bàn tay phẳng trên mặt bàn và nói ra câu đã soạn sẵn",
  [("MR. HALLORAN", "flat, rehearsed", 11), ("RYAN", "incredulous, raised", 12)])

S("07", "cận-trung 85mm, cao 1m50, cách RYAN 1m7, máy sau vai TRÁI của MR. HALLORAN; vai và gáy ông chiếm rìa trái, out nét",
  "RYAN đứng chính diện chiếm phần lớn khung, hai tay đã chống lên mép bàn. MR. HALLORAN chỉ còn là vai và gáy "
  "ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng RYAN là vách kính hành lang, không thấy ai.",
  "RYAN hai tay chống lên mép bàn, người chồm tới.",
  "RYAN nhìn thẳng xuống mặt MR. HALLORAN.",
  "RYAN — người đang tìm ra chỗ hở trong câu chuyện và đuổi theo nó: mắt quét, giọng nhanh, "
  "cằm hất về phía trước.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN quay đầu nhìn ra phía hành lang",
  ["RYAN_COMLE", "MR. HALLORAN"], "trước bàn làm việc",
  {"RYAN": "đứng chống tay lên mép bàn, chính diện giữa khung", "MR. HALLORAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một mặt bàn", {"RYAN": "hai tay chống lên mép bàn",
                            "MR. HALLORAN": "hai tay trên mặt bàn, ngoài vùng nét"})
V("07", [13, 14], "OTS cận-trung 85mm · RYAN NÉT chính diện chống tay lên bàn · vai và gáy MR. HALLORAN tiền cảnh trái out nét",
  [("RYAN", "RYAN_COMLE"), ("MR. HALLORAN", "MR. HALLORAN")],
  "RYAN rõ mặt chính diện. MR. HALLORAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "RYAN chống hai tay lên mép bàn và chồm tới",
  [("MR. HALLORAN", "flat, evasive", 13), ("RYAN", "fast, pressing", 14)])

S("08", "trung 50mm, cao 1m50, cách RYAN 2m2, đặt bên bàn làm việc lấy cả hai người và vách kính hành lang",
  "RYAN đứng ở nửa PHẢI khung, đã quay nửa người về phía vách kính hành lang. MR. HALLORAN ngồi ở nửa TRÁI khung "
  "sau bàn. Qua vách kính phía sau thấy một dáng người mờ đứng quay lưng ngoài hành lang.",
  "RYAN một tay chỉ về phía vách kính hành lang, tay kia còn chống mép bàn. MR. HALLORAN hai tay rút về đặt trên đùi.",
  "RYAN nhìn về phía dáng người ngoài hành lang rồi quay lại nhìn MR. HALLORAN. MR. HALLORAN nhìn xuống mặt bàn.",
  "RYAN — người vừa nối được hai chuyện với nhau: mắt mở to, giọng cao lên. "
  "MR. HALLORAN — không dám nhìn lên: mắt hạ xuống, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi MR. HALLORAN ngước lên trả lời",
  ["RYAN_COMLE", "MR. HALLORAN", "SEBASTIAN"], "trước bàn làm việc, quay về phía vách kính hành lang",
  {"RYAN": "đứng nửa phải khung, quay nửa người về vách kính", "MR. HALLORAN": "ngồi sau bàn nửa trái khung",
   "SEBASTIAN": "dáng người mờ quay lưng ngoài hành lang, sau vách kính"},
  "cách nhau một mặt bàn", {"RYAN": "một tay chỉ về vách kính, tay kia chống mép bàn",
                            "MR. HALLORAN": "hai tay rút về đặt trên đùi", "SEBASTIAN": "quay lưng, hai tay buông"})
V("08", [15, 16], "trung 50mm · RYAN NÉT phải chỉ về vách kính + MR. HALLORAN NÉT trái sau bàn · SEBASTIAN mờ quay lưng ngoài hành lang",
  [("RYAN", "RYAN_COMLE"), ("MR. HALLORAN", "MR. HALLORAN"), ("SEBASTIAN", "SEBASTIAN")],
  "RYAN và MR. HALLORAN rõ mặt. SEBASTIAN chỉ thấy dáng người MỜ phía sau vách kính, QUAY LƯNG, "
  "TUYỆT ĐỐI KHÔNG quay mặt lại.",
  "RYAN chỉ tay về phía dáng người mờ ngoài hành lang",
  [("MR. HALLORAN", "quiet, admitting", 15), ("RYAN", "loud, accusing", 16)])

S("09", "two-shot trung 50mm, cao 1m50, cách MR. HALLORAN 2m2, đặt bên bàn làm việc lấy cả hai người",
  "MR. HALLORAN đã đứng dậy khỏi ghế và đứng ở nửa TRÁI khung sau bàn. RYAN đứng ở nửa PHẢI khung trước bàn, "
  "hai tay đã rời khỏi mặt bàn. Hậu cảnh là vách kính nhìn ra thành phố.",
  "MR. HALLORAN một tay chìa ngửa ra về phía RYAN, tay kia chỉ về phía cửa. RYAN hai tay buông dọc thân, "
  "một tay nắm lại.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MR. HALLORAN — người muốn chuyện này kết thúc trước khi mình nói ra thứ không nên nói: giọng đều, mắt né. "
  "RYAN — không chấp nhận và đòi lên tới tận cùng: cằm hất, giọng vang.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước một bước về phía cửa",
  ["MR. HALLORAN", "RYAN_COMLE"], "hai bên bàn làm việc",
  {"MR. HALLORAN": "đứng sau bàn nửa trái khung", "RYAN": "đứng trước bàn nửa phải khung"},
  "cách nhau một mặt bàn", {"MR. HALLORAN": "một tay chìa ngửa, tay kia chỉ về phía cửa",
                            "RYAN": "hai tay buông, một tay nắm lại"})
V("09", [17, 18], "two-shot trung 50mm · MR. HALLORAN NÉT trái đứng sau bàn + RYAN NÉT phải đứng trước bàn",
  [("MR. HALLORAN", "MR. HALLORAN"), ("RYAN", "RYAN_COMLE")],
  "MR. HALLORAN và RYAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MR. HALLORAN đứng dậy khỏi ghế, một tay chìa ngửa ra, tay kia chỉ về phía cửa",
  [("MR. HALLORAN", "weary, formal", 17), ("RYAN", "loud, demanding", 18)])

S("10", "cận-trung 85mm, cao 1m50, cách MR. HALLORAN 1m6, đặt bên bàn, lấy MR. HALLORAN nét và RYAN trong khung",
  "MR. HALLORAN đứng ở nửa TRÁI khung, một tay chống xuống mặt bàn. RYAN đứng ở nửa PHẢI khung, người chồm tới. "
  "Hậu cảnh là mảng tường ốp gỗ veneer và bức tranh trừu tượng.",
  "MR. HALLORAN một tay chống xuống mặt bàn, tay kia đưa lên xoa gáy. RYAN một tay chỉ vào chính mình.",
  "MR. HALLORAN nhìn RYAN. RYAN nhìn lại.",
  "MR. HALLORAN — người đang cố cảnh báo một thằng bé mà không được phép nói rõ: giọng thấp, mắt mệt. "
  "RYAN — vẫn đang cậy vào một cái tên: cằm hất, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MR. HALLORAN đi vòng qua bàn",
  ["MR. HALLORAN", "RYAN_COMLE"], "hai bên bàn làm việc",
  {"MR. HALLORAN": "đứng nửa trái khung, chống tay xuống bàn", "RYAN": "đứng nửa phải khung, chồm tới"},
  "cách nhau một mặt bàn", {"MR. HALLORAN": "một tay chống mặt bàn, tay kia xoa gáy",
                            "RYAN": "một tay chỉ vào chính mình"})
V("10", [19, 20], "cận-trung 85mm · MR. HALLORAN NÉT trái chống tay xuống bàn + RYAN NÉT phải chồm tới",
  [("MR. HALLORAN", "MR. HALLORAN"), ("RYAN", "RYAN_COMLE")],
  "MR. HALLORAN và RYAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MR. HALLORAN chống một tay xuống mặt bàn và xoa gáy, RYAN chỉ vào chính mình",
  [("MR. HALLORAN", "low, warning", 19), ("RYAN", "loud, boastful", 20)])

S("11", "cận-trung 85mm, cao 1m50, cách MR. HALLORAN 1m5, máy sau vai PHẢI của RYAN; vai và gáy anh chiếm rìa phải, out nét",
  "MR. HALLORAN đứng chính diện chiếm phần lớn khung, đã đi vòng ra trước bàn. RYAN chỉ còn là vai và gáy ở "
  "rìa PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MR. HALLORAN là vách kính và thành phố ban ngày.",
  "MR. HALLORAN một tay đặt lên vai RYAN rồi rút về ngay, tay kia buông.",
  "MR. HALLORAN nhìn thẳng vào mặt RYAN.",
  "MR. HALLORAN — người sắp làm việc tử tế cuối cùng mình còn làm được và biết nó chẳng cứu được ai: "
  "giọng chậm, thấp, mắt thẳng và mệt.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN hỏi tên người đó",
  ["MR. HALLORAN", "RYAN_COMLE"], "trước bàn làm việc",
  {"MR. HALLORAN": "đứng chính diện giữa khung, đã ra trước bàn", "RYAN": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"MR. HALLORAN": "một tay đặt lên vai RYAN rồi rút về",
                         "RYAN": "hai tay buông, ngoài vùng nét"})
V("11", [21], "OTS cận-trung 85mm · MR. HALLORAN NÉT chính diện · vai và gáy RYAN tiền cảnh phải out nét",
  [("MR. HALLORAN", "MR. HALLORAN"), ("RYAN", "RYAN_COMLE")],
  "MR. HALLORAN rõ mặt chính diện. RYAN chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MR. HALLORAN đặt tay lên vai RYAN một nhịp rồi rút về và nói chậm",
  [("MR. HALLORAN", "slow, warning", 21)], [("RYAN", "silent, listening")])

S("12", "two-shot trung 50mm, cao 1m50, cách RYAN 2m, đặt trước bàn làm việc lấy cả hai người đứng",
  "RYAN đứng ở nửa PHẢI khung, MR. HALLORAN đứng ở nửa TRÁI khung, cả hai cùng đứng trước bàn, cách một bước. "
  "Hậu cảnh là vách kính hành lang, ngoài đó không còn ai.",
  "RYAN hai tay buông dọc thân, các ngón mở ra. MR. HALLORAN hai tay đút túi quần.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — người vừa nhận ra mình đang đứng trước một thứ mình không hiểu nổi: mặt tái đi, giọng nhỏ hẳn. "
  "MR. HALLORAN — thú nhận sự bất lực của chính mình: khoé môi trễ, mắt mệt.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN quay lưng đi ra cửa",
  ["RYAN_COMLE", "MR. HALLORAN"], "trước bàn làm việc",
  {"RYAN": "đứng nửa phải khung", "MR. HALLORAN": "đứng nửa trái khung"},
  "cách nhau một bước", {"RYAN": "hai tay buông, các ngón mở ra", "MR. HALLORAN": "hai tay đút túi quần"})
V("12", [22, 23], "two-shot trung 50mm · MR. HALLORAN NÉT trái + RYAN NÉT phải, cả hai đứng trước bàn",
  [("MR. HALLORAN", "MR. HALLORAN"), ("RYAN", "RYAN_COMLE")],
  "MR. HALLORAN và RYAN, cả hai rõ mặt. Không có ai khác trong khung; ngoài vách kính hành lang không còn ai.",
  "RYAN hỏi câu cuối, MR. HALLORAN đút hai tay vào túi quần và trả lời",
  [("RYAN", "quiet, shaken", 22), ("MR. HALLORAN", "flat, honest", 23)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "trung-rộng 35mm, cao 1m60, cách RYAN 5m, đặt trong phòng nhìn ra vách kính hành lang",
  "RYAN đứng một mình ngoài hành lang phía sau VÁCH KÍNH TRONG SUỐT, quay lưng lại phía phòng làm việc, "
  "một tay còn cầm chiếc thẻ nhân viên. Trong phòng làm việc tiền cảnh không còn ai, chiếc ghế da đen quay ngang.",
  "RYAN một tay cầm chiếc thẻ nhân viên, tay kia buông dọc thân.",
  "RYAN nhìn dọc hành lang về phía thang máy, KHÔNG quay đầu lại phía phòng làm việc.",
  "RYAN — người vừa mất việc và chưa biết mình đang đứng ở đầu cái gì: vai chùng, lưng quay lại, "
  "đầu hơi cúi.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước bước đầu tiên về phía thang máy",
  ["RYAN_COMLE"], "hành lang sau vách kính, nhìn từ trong phòng làm việc ra",
  {"RYAN": "đứng một mình ngoài hành lang, quay lưng lại"}, "một mình trong khung",
  {"RYAN": "một tay cầm chiếc thẻ nhân viên, tay kia buông"})
B("B2", "Khép cảnh. RYAN đứng một mình ngoài hành lang sau vách kính, thẻ nhân viên trong tay, quay lưng lại.",
  "trung-rộng 35mm · RYAN QUAY LƯNG đứng một mình ngoài hành lang sau vách kính · phòng làm việc tiền cảnh trống",
  [("RYAN", "RYAN_COMLE")],
  "CHỈ MỘT MÌNH RYAN trong khung, chỉ thấy TỪ PHÍA SAU, quay lưng lại — TUYỆT ĐỐI KHÔNG quay mặt về camera. "
  "Không có người nào khác trong khung.",
  "một người vừa bị lấy mất chỗ đứng của mình trong hai mươi phút và không hiểu vì sao; "
  "khán giả thì đã biết vì sao từ ba cảnh trước.",
  "RYAN đứng yên rất lâu quay lưng lại, tay còn cầm chiếc thẻ; ánh sáng ban ngày trắng từ vách kính ngoài trời "
  "hắt dài trên sàn thảm xám than; chiếc ghế da đen trong phòng quay chậm nửa vòng rồi dừng.",
  "Ambient tiếng ù rất khẽ của điều hoà trên tầng cao và tiếng chuông thang máy rất xa.",
  nhac("NGHỈ", "Sau một cảnh toàn giọng nói, cần một khoảng câm để cú sa thải này ngấm — và nhạc phải trung tính, không thương hại kẻ vừa mất việc.",
       "Minimal piano at 60 BPM; an upright piano placing single notes with long gaps and the sustain pedal down, "
       "a female voice humming once very faintly near the end; no drums, no bass; the pull is a long silence before "
       "the final note; wordless and neutral; dry office mix, female vocal, piano, minimal, cold",
       "Minimal instrumental at 58 BPM; upright piano placing three notes with heavy sustain, a very low synth pad "
       "underneath, no percussion, no arc, thinning to nothing; cold clean mix, piano, pad, minimal"),
  dur=8)
