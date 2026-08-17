# -*- coding: utf-8 -*-
"""SCENE 23 — CÂY BÚA (nhà thờ St. Michael, chiều)."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S23", "REF_NHATHOTIEC_CHIEU", qc=qc.S23, qcv=qc.S23V)

KHACH = ""

S("01", "trung 50mm, cao 1m55, cách ADRIAN 2m4, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "ADRIAN đứng thẳng ở nửa PHẢI khung, áo khoác dạ đen trên vai. SEBASTIAN đứng ở nửa TRÁI khung, một tay đưa lên "
  "ra hiệu về phía màn chiếu sau bàn thờ. " + KHACH,
  "ADRIAN một tay hất nhẹ về phía màn chiếu. SEBASTIAN một tay giơ lên ra hiệu, tay kia giữ bìa kẹp hồ sơ.",
  "ADRIAN nhìn về phía màn chiếu ngoài khung. SEBASTIAN nhìn ADRIAN.",
  "ADRIAN — người ra lệnh bằng hai chữ: mặt hoàn toàn bình, giọng đều. "
  "SEBASTIAN — thực hiện ngay: mặt bình, tay đã ra hiệu.",
  "đúng khoảnh khắc ngay TRƯỚC khi đèn trong nhà thờ tối đi một bậc",
  ["ADRIAN_VEST", "SEBASTIAN"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa phải khung", "SEBASTIAN": "đứng nửa trái khung"},
  "cách nhau một bước", {"ADRIAN": "một tay hất nhẹ về phía màn chiếu",
                         "SEBASTIAN": "một tay giơ lên ra hiệu, tay kia giữ bìa kẹp hồ sơ"})
V("01", [0, 1], "trung 50mm · SEBASTIAN NÉT trái ra hiệu + ADRIAN NÉT phải đứng thẳng · khách nền mờ",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_VEST")],
  "SEBASTIAN và ADRIAN, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN hất nhẹ tay về phía màn chiếu, SEBASTIAN giơ tay ra hiệu cho người phía sau",
  [("ADRIAN", "flat, commanding", 0), ("SEBASTIAN", "crisp, executing", 1)])

S("02", "cận-trung 85mm, cao 1m55, cách GUEST ONE 1m7, đặt trong vòng người vây quanh",
  "GUEST ONE đứng ở nửa TRÁI khung, GUEST TWO đứng ở nửa PHẢI khung sát cạnh, cả hai đang ngẩng nhìn lên. "
  "Trên mặt hai người có ánh sáng xanh trắng nhấp nháy hắt xuống từ một màn chiếu ngoài khung.",
  "GUEST ONE một tay chỉ lên phía màn chiếu. GUEST TWO hai tay ôm chiếc clutch nhung trước ngực.",
  "Cả hai ngẩng nhìn lên phía màn chiếu ngoài khung. TUYỆT ĐỐI không ai nhìn vào ống kính.",
  "GUEST ONE — người đang đọc ra thành tiếng đúng thứ mình nhìn thấy: mắt mở to, giọng khàn dần. "
  "GUEST TWO — mặt cứng lại từng nhịp: môi mím.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả một vùng phòng rộ lên tiếng xì xào",
  ["GUEST1_TUX", "GUEST2_DAHOI"], "trong vòng người vây quanh, cuối nhà thờ",
  {"GUEST ONE": "đứng nửa trái khung", "GUEST TWO": "đứng nửa phải khung"},
  "sát cạnh nhau", {"GUEST ONE": "một tay chỉ lên phía màn chiếu",
                    "GUEST TWO": "hai tay ôm chiếc clutch nhung trước ngực"})
V("02", [2, 3, 4], "cận-trung 85mm · GUEST ONE NÉT trái chỉ lên màn chiếu + GUEST TWO NÉT phải · ánh màn chiếu hắt lên mặt",
  [("GUEST ONE", "GUEST1_TUX"), ("GUEST TWO", "GUEST2_DAHOI")],
  "GUEST ONE và GUEST TWO, cả hai rõ mặt, có ánh sáng xanh trắng của màn chiếu hắt lên mặt. "
  "Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GUEST ONE chỉ lên phía màn chiếu, ánh sáng nhấp nháy hắt lên mặt hai người",
  [("GUEST ONE", "hushed, reading", 2), ("GUEST TWO", "hushed, hardening", 3),
   ("GUEST ONE", "louder, damning", 4)])

S("03", "trung 50mm, cao 1m55, cách VANESSA 2m2, đặt trong lòng nhà thờ lấy cả hai người",
  "VANESSA đứng ở nửa PHẢI khung trong váy cưới, một tay giơ lên che mặt khỏi ánh màn chiếu. ADRIAN đứng thẳng "
  "ở nửa TRÁI khung, mặt hướng lên phía màn chiếu. " + KHACH,
  "VANESSA một tay giơ lên ngang mặt, tay kia nắm lấy vạt váy. ADRIAN một tay hất nhẹ ra hiệu chiếu lại.",
  "VANESSA nhìn về phía cha mình ngoài khung. ADRIAN nhìn lên màn chiếu ngoài khung.",
  "VANESSA — người vừa thấy chính mình trên màn hình: mặt trắng, giọng vỡ, tay run. "
  "ADRIAN — ra lệnh chiếu lại chậm hơn: mặt hoàn toàn bình, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi đoạn băng bắt đầu chạy lại từ đầu",
  ["VANESSA_CODAUXO", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"VANESSA": "đứng nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung"},
  "cách nhau ba bước", {"VANESSA": "một tay giơ ngang mặt, tay kia nắm vạt váy",
                        "ADRIAN": "một tay hất nhẹ ra hiệu chiếu lại"})
V("03", [5, 6], "trung 50mm · ADRIAN NÉT trái đứng thẳng + VANESSA NÉT phải giơ tay che mặt · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("VANESSA", "VANESSA_CODAUXO")],
  "ADRIAN và VANESSA, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "VANESSA giơ tay lên che mặt khỏi ánh màn chiếu, ADRIAN hất nhẹ tay ra hiệu",
  [("VANESSA", "cracking, panicked", 5), ("ADRIAN", "flat, commanding", 6)])

S("04", "cận-trung 85mm, cao 1m55, cách VANESSA 1m6, đặt trong lòng nhà thờ lấy cả hai người",
  "GERALD HALE đứng ở nửa TRÁI khung, đã quay hẳn về phía con gái. VANESSA đứng ở nửa PHẢI khung, hai tay "
  "đã buông xuống. Hậu cảnh là cột hoa trắng và ánh màn chiếu nhấp nháy.",
  "GERALD HALE hai tay nắm lấy hai cánh tay VANESSA. VANESSA hai tay buông xuống hai bên.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "GERALD HALE — người vừa hiểu ra con gái mình đã làm gì: mặt xám lại, giọng vỡ. "
  "VANESSA — vẫn đang cố gọi nó là một trò đùa: mắt tràn nước, giọng run, cằm run.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng bước chân cảnh sát tới từ phía cửa lớn",
  ["GERALD HALE", "VANESSA_CODAUXO"], "giữa lòng nhà thờ, gần bàn thờ",
  {"GERALD HALE": "đứng nửa trái khung", "VANESSA": "đứng nửa phải khung"},
  "sát nhau", {"GERALD HALE": "hai tay nắm lấy hai cánh tay VANESSA",
               "VANESSA": "hai tay buông xuống hai bên"})
V("04", [7, 8], "cận-trung 85mm · GERALD HALE NÉT trái nắm hai cánh tay con gái + VANESSA NÉT phải",
  [("GERALD HALE", "GERALD HALE"), ("VANESSA", "VANESSA_CODAUXO")],
  "GERALD HALE và VANESSA, cả hai rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "GERALD HALE nắm lấy hai cánh tay con gái mình",
  [("GERALD HALE", "broken, quiet", 7), ("VANESSA", "shaking, pleading", 8)])

S("05", "trung 50mm, cao 1m55, cách ADRIAN 2m2, đặt trong lòng nhà thờ lấy cả hai người",
  "ADRIAN đứng thẳng ở nửa TRÁI khung. POLICE OFFICER đứng ở nửa PHẢI khung, vừa tới, một tay đặt trên bao "
  "còng tay ở thắt lưng. " + KHACH,
  "ADRIAN một tay chỉ về phía cô dâu ngoài khung. POLICE OFFICER một tay đặt trên bao còng tay, "
  "tay kia đưa lên bộ đàm ở cầu vai.",
  "ADRIAN nhìn POLICE OFFICER. POLICE OFFICER nhìn theo hướng tay chỉ.",
  "ADRIAN — người đọc ra tội danh như đọc một điều khoản: giọng đều, chậm, mặt bình. "
  "POLICE OFFICER — nghe và bước ngay: mặt trung tính, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi POLICE OFFICER bước về phía cô dâu",
  ["ADRIAN_VEST", "POLICE OFFICER"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "POLICE OFFICER": "đứng nửa phải khung"},
  "cách nhau một bước", {"ADRIAN": "một tay chỉ về phía cô dâu ngoài khung",
                         "POLICE OFFICER": "một tay trên bao còng tay, tay kia trên bộ đàm"})
V("05", [9], "trung 50mm · ADRIAN NÉT trái đứng thẳng + POLICE OFFICER NÉT phải · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("POLICE OFFICER", "POLICE OFFICER")],
  "ADRIAN và POLICE OFFICER, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN chỉ về phía cô dâu và đọc ra tội danh",
  [("ADRIAN", "even, procedural", 9)], [("POLICE OFFICER", "silent, stepping forward")])

S("06", "trung 50mm, cao 1m55, cách VANESSA 2m, đặt trong lòng nhà thờ lấy cả hai người",
  "POLICE OFFICER đứng ở nửa TRÁI khung, đã tới sát. VANESSA đứng ở nửa PHẢI khung trong váy cưới, "
  "đã lùi lại nửa bước. " + KHACH,
  "POLICE OFFICER một tay đưa ra phía VANESSA, tay kia rút còng tay khỏi bao ở thắt lưng. "
  "VANESSA hai tay giơ lên ngang ngực đẩy ra.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "POLICE OFFICER — làm đúng thủ tục, giọng bình: mặt trung tính. "
  "VANESSA — lôi cha mình ra làm lá chắn cuối cùng: mắt tràn nước, giọng cao.",
  "đúng khoảnh khắc ngay TRƯỚC khi chiếc còng chạm vào cổ tay VANESSA",
  ["POLICE OFFICER", "VANESSA_CODAUXO"], "giữa lòng nhà thờ",
  {"POLICE OFFICER": "đứng nửa trái khung", "VANESSA": "đứng lùi nửa bước, nửa phải khung"},
  "sát nhau", {"POLICE OFFICER": "một tay đưa ra, tay kia rút còng tay khỏi bao",
               "VANESSA": "hai tay giơ lên ngang ngực đẩy ra"})
V("06", [10, 11], "trung 50mm · POLICE OFFICER NÉT trái rút còng tay + VANESSA NÉT phải giơ tay đẩy ra",
  [("POLICE OFFICER", "POLICE OFFICER"), ("VANESSA", "VANESSA_CODAUXO")],
  "POLICE OFFICER và VANESSA, cả hai rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "POLICE OFFICER rút còng tay khỏi bao ở thắt lưng, VANESSA giơ hai tay lên đẩy ra",
  [("POLICE OFFICER", "flat, procedural", 10), ("VANESSA", "shrill, pleading", 11)])

S("07", "cận-trung 85mm, cao 1m55, cách POLICE OFFICER 1m6, máy sau vai PHẢI của VANESSA; vai và gáy cô chiếm rìa phải, out nét",
  "POLICE OFFICER đứng chính diện chiếm phần lớn khung. VANESSA chỉ còn là vai và một mảng váy cưới trắng ở rìa "
  "PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh là cột hoa trắng và khách vây quanh mờ.",
  "POLICE OFFICER hai tay đưa ra phía trước, chiếc còng tay mở sẵn trong một tay.",
  "POLICE OFFICER nhìn thẳng vào mặt VANESSA.",
  "POLICE OFFICER — trả lời một câu rất bình và chính vì bình mà nó nặng: mặt trung tính, mắt thẳng, "
  "KHÔNG mỉa mai.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai cổ tay VANESSA bị đưa ra sau lưng",
  ["POLICE OFFICER", "VANESSA_CODAUXO"], "giữa lòng nhà thờ",
  {"POLICE OFFICER": "đứng chính diện giữa khung", "VANESSA": "vai và mảng váy cưới ở rìa phải tiền cảnh"},
  "sát nhau", {"POLICE OFFICER": "hai tay đưa ra phía trước, còng tay mở sẵn",
               "VANESSA": "hai tay giơ lên, ngoài vùng nét"})
V("07", [12], "OTS cận-trung 85mm · POLICE OFFICER NÉT chính diện · vai và mảng váy cưới VANESSA tiền cảnh phải out nét",
  [("POLICE OFFICER", "POLICE OFFICER"), ("VANESSA", "VANESSA_CODAUXO")],
  "POLICE OFFICER rõ mặt chính diện. VANESSA chỉ thấy VAI và một mảng váy cưới trắng ở tiền cảnh phải, "
  "out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "POLICE OFFICER đưa hai tay ra phía trước với chiếc còng mở sẵn",
  [("POLICE OFFICER", "flat, factual", 12)], [("VANESSA", "silent, hands raised")])

S("08", "trung 50mm, cao 1m55, cách ADRIAN 2m2, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "ADRIAN đứng thẳng ở nửa TRÁI khung. BOARD CHAIRMAN CRANE đứng ở nửa PHẢI khung, đã bước tới một bước. "
  + KHACH,
  "ADRIAN hai tay buông dọc thân. BOARD CHAIRMAN CRANE hai tay giữ chiếc áo khoác gấp trước bụng.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — gọi một cái tên và nói ra một con số: giọng đều, mặt bình. "
  "BOARD CHAIRMAN CRANE — đáp bằng đúng một chữ rồi chờ: mặt trang trọng.",
  "đúng khoảnh khắc ngay TRƯỚC khi BOARD CHAIRMAN CRANE sửa lại con số",
  ["ADRIAN_VEST", "BOARD CHAIRMAN CRANE"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "BOARD CHAIRMAN CRANE": "đứng nửa phải khung"},
  "cách nhau một bước", {"ADRIAN": "hai tay buông dọc thân",
                         "BOARD CHAIRMAN CRANE": "hai tay giữ chiếc áo khoác gấp trước bụng"})
V("08", [13, 14, 15], "trung 50mm · ADRIAN NÉT trái đứng thẳng + BOARD CHAIRMAN CRANE NÉT phải · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("BOARD CHAIRMAN CRANE", "BOARD CHAIRMAN CRANE")],
  "ADRIAN và BOARD CHAIRMAN CRANE, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN gọi tên và nói ra con số, BOARD CHAIRMAN CRANE bước tới một bước",
  [("ADRIAN", "flat, calling", 13), ("BOARD CHAIRMAN CRANE", "formal, ready", 14),
   ("ADRIAN", "even, exact", 15)])

S("09", "cận-trung 85mm, cao 1m55, cách BOARD CHAIRMAN CRANE 1m6, đặt trong lòng nhà thờ lấy cả hai người",
  "BOARD CHAIRMAN CRANE đứng ở nửa PHẢI khung. ADRIAN đứng thẳng ở nửa TRÁI khung. Hậu cảnh là lối đi trải "
  "thảm trắng và các cụm khách mờ.",
  "BOARD CHAIRMAN CRANE một tay rút một chiếc điện thoại mỏng khỏi túi ngực. ADRIAN hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "BOARD CHAIRMAN CRANE — sửa con số tới hàng triệu mà không nhìn giấy: mặt trang trọng, giọng rõ. "
  "ADRIAN — ra lệnh bằng hai chữ: mặt hoàn toàn bình, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi ngón tay BOARD CHAIRMAN CRANE chạm vào màn hình điện thoại",
  ["BOARD CHAIRMAN CRANE", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"BOARD CHAIRMAN CRANE": "đứng nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung"},
  "cách nhau một bước", {"BOARD CHAIRMAN CRANE": "một tay rút chiếc điện thoại mỏng khỏi túi ngực",
                         "ADRIAN": "hai tay buông dọc thân"})
V("09", [16, 17], "cận-trung 85mm · ADRIAN NÉT trái đứng thẳng + BOARD CHAIRMAN CRANE NÉT phải rút điện thoại",
  [("ADRIAN", "ADRIAN_VEST"), ("BOARD CHAIRMAN CRANE", "BOARD CHAIRMAN CRANE")],
  "ADRIAN và BOARD CHAIRMAN CRANE, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "BOARD CHAIRMAN CRANE rút chiếc điện thoại mỏng khỏi túi ngực",
  [("BOARD CHAIRMAN CRANE", "precise, formal", 16), ("ADRIAN", "flat, absolute", 17)])

S("10", "trung 50mm, cao 1m55, cách BOARD CHAIRMAN CRANE 2m2, đặt trong lòng nhà thờ lấy cả hai người",
  "BOARD CHAIRMAN CRANE đứng ở nửa TRÁI khung, chiếc điện thoại mỏng đã ở tai. GERALD HALE đứng ở nửa PHẢI khung, "
  "đã bước tới, một tay đưa ra. " + KHACH,
  "BOARD CHAIRMAN CRANE một tay giữ điện thoại ở tai, tay kia buông. GERALD HALE một tay đưa ra phía CRANE, "
  "tay kia nắm lại.",
  "BOARD CHAIRMAN CRANE nhìn thẳng phía trước khi nói vào điện thoại. GERALD HALE nhìn CRANE.",
  "BOARD CHAIRMAN CRANE — đọc lệnh vào điện thoại như đọc giờ: mặt trang trọng, giọng đều. "
  "GERALD HALE — người vừa nghe cả công ty mình bị đóng băng trong một câu: mặt trắng, giọng vỡ.",
  "đúng khoảnh khắc ngay TRƯỚC khi GERALD HALE khuỵu một gối xuống nền đá",
  ["BOARD CHAIRMAN CRANE", "GERALD HALE"], "giữa nền đá cuối nhà thờ",
  {"BOARD CHAIRMAN CRANE": "đứng nửa trái khung, điện thoại ở tai", "GERALD HALE": "đứng nửa phải khung"},
  "cách nhau một bước", {"BOARD CHAIRMAN CRANE": "một tay giữ điện thoại ở tai",
                         "GERALD HALE": "một tay đưa ra phía CRANE, tay kia nắm lại"})
V("10", [18, 19], "trung 50mm · BOARD CHAIRMAN CRANE NÉT trái nói vào điện thoại + GERALD HALE NÉT phải",
  [("BOARD CHAIRMAN CRANE", "BOARD CHAIRMAN CRANE"), ("GERALD HALE", "GERALD HALE")],
  "BOARD CHAIRMAN CRANE và GERALD HALE, cả hai rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "BOARD CHAIRMAN CRANE đưa điện thoại lên tai và đọc lệnh, GERALD HALE đưa tay ra chặn lại",
  [("BOARD CHAIRMAN CRANE", "formal, executing", 18), ("GERALD HALE", "cracking, desperate", 19)])

S("11", "trung 50mm, cao 1m20, cách ADRIAN 2m2, máy hạ thấp, lấy ADRIAN đứng và GERALD đã khuỵu một gối",
  "ADRIAN đứng thẳng ở nửa TRÁI khung. GERALD HALE đã khuỵu một gối xuống nền đá ở nửa PHẢI khung, một tay "
  "chống nền. " + KHACH,
  "ADRIAN hai tay buông dọc thân. GERALD HALE một tay chống xuống nền đá, tay kia ôm lấy ngực.",
  "ADRIAN nhìn xuống GERALD HALE. GERALD HALE ngẩng lên nhìn ADRIAN.",
  "ADRIAN — người trả lời bằng ba chữ ở thì quá khứ: mặt hoàn toàn bình, giọng rất nhỏ. "
  "GERALD HALE — người vừa mất tất cả trong bốn mươi giây: mặt xám, giọng khàn.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bước một bước lại gần",
  ["ADRIAN_VEST", "GERALD HALE"], "nền đá cẩm thạch cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "GERALD HALE": "khuỵu một gối nửa phải khung"},
  "cách nhau hai bước", {"ADRIAN": "hai tay buông dọc thân",
                         "GERALD HALE": "một tay chống nền đá, tay kia ôm ngực"})
V("11", [20, 21], "trung 50mm hạ thấp · ADRIAN NÉT trái đứng thẳng + GERALD HALE NÉT phải khuỵu một gối xuống nền",
  [("ADRIAN", "ADRIAN_VEST"), ("GERALD HALE", "GERALD HALE")],
  "ADRIAN và GERALD HALE, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN, GERALD HALE khuỵu một gối xuống nền đá. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "GERALD HALE khuỵu một gối xuống nền đá, một tay chống nền",
  [("ADRIAN", "quiet, past-tense", 20), ("GERALD HALE", "hoarse, broken", 21)])

S("12", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m7, máy hạ thấp nhìn hơi chếch lên phía ADRIAN đứng",
  "ADRIAN đứng thẳng chiếm phần lớn khung, nhìn xuống. Ở rìa DƯỚI khung thấy vai và mái tóc bạc của GERALD HALE "
  "đang khuỵu gối, out nét. Hậu cảnh là trần vòm nhọn và đèn pha lê.",
  "ADRIAN một tay hơi mở ra ngang hông theo nhịp nói.",
  "ADRIAN nhìn xuống GERALD HALE.",
  "ADRIAN — người nói ra một câu mà bốn trăm người sẽ nhớ suốt đời: giọng đều, chậm, mắt tĩnh, "
  "KHÔNG lớn tiếng, KHÔNG hả hê.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN quay người sang phía người đàn ông đứng cuối lối đi",
  ["ADRIAN_VEST", "GERALD HALE"], "nền đá cẩm thạch cuối nhà thờ",
  {"ADRIAN": "đứng thẳng chính diện giữa khung",
   "GERALD HALE": "vai và mái tóc bạc ở rìa dưới khung, đang khuỵu gối"},
  "cách nhau một bước", {"ADRIAN": "một tay hơi mở ra ngang hông",
                         "GERALD HALE": "một tay chống nền, ngoài vùng nét"})
VX("12", "cận-trung 85mm hạ thấp · ADRIAN NÉT đứng thẳng chính diện · vai và mái tóc bạc GERALD HALE rìa dưới out nét",
   [("ADRIAN", "ADRIAN_VEST"), ("GERALD HALE", "GERALD HALE")],
   "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. GERALD HALE chỉ thấy VAI và mái tóc bạc ở rìa dưới khung, out nét — "
   "KHÔNG quay mặt về camera.",
   "ADRIAN mở một bàn tay ra ngang hông và nói xuống",
   [("ADRIAN", "even, final",
     "You will be bankrupt by midnight. You kicked a man out of a wheelchair forty minutes ago and four hundred "
     "people watched you do it.")],
   [("GERALD HALE", "silent, on one knee")])

S("12b", "trung 50mm, cao 1m20, cách ADRIAN 2m2, máy hạ thấp lấy ADRIAN đứng và GERALD khuỵu một gối",
  "ADRIAN đứng thẳng ở nửa TRÁI khung. GERALD HALE khuỵu một gối trên nền đá ở nửa PHẢI khung, hai tay chống nền. "
  + KHACH,
  "ADRIAN một tay chỉ xuống nền đá trước mũi giày mình. GERALD HALE hai tay chống xuống nền đá.",
  "ADRIAN nhìn xuống GERALD HALE. GERALD HALE ngẩng lên nhìn ADRIAN.",
  "ADRIAN — người nói câu cuối cùng với đối thủ bằng giọng của người dặn dò sức khoẻ: giọng đều, chậm, "
  "mắt tĩnh, KHÔNG hả hê. GERALD HALE — mặt xám, hai vai sụp.",
  "đúng khoảnh khắc ngay TRƯỚC khi GERALD HALE chống tay định đứng lên",
  ["ADRIAN_VEST", "GERALD HALE"], "nền đá cẩm thạch cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "GERALD HALE": "khuỵu một gối nửa phải khung"},
  "cách nhau hai bước", {"ADRIAN": "một tay chỉ xuống nền đá trước mũi giày",
                         "GERALD HALE": "hai tay chống xuống nền đá"})
VX("12b", "trung 50mm hạ thấp · ADRIAN NÉT trái đứng thẳng + GERALD HALE NÉT phải khuỵu một gối trên nền đá",
   [("ADRIAN", "ADRIAN_VEST"), ("GERALD HALE", "GERALD HALE")],
   "ADRIAN và GERALD HALE, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN, GERALD HALE khuỵu một gối xuống nền đá. "
   "Khách vây quanh mờ, không ai nhìn vào camera.",
   "ADRIAN chỉ xuống nền đá trước mũi giày mình và nói xuống",
   [("ADRIAN", "even, final", "Get up off the floor, Mr. Hale. Your knees are going to hurt later.")],
   [("GERALD HALE", "silent, on one knee")])

S("13", "trung 50mm, cao 1m55, cách JULIAN 2m2, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "JULIAN đứng ở nửa PHẢI khung, đã bước tới, hai tay đưa ra phía trước. ADRIAN đứng thẳng ở nửa TRÁI khung. "
  + KHACH,
  "JULIAN hai tay đưa ra phía trước, lòng bàn tay ngửa. ADRIAN một tay hất nhẹ về phía cuối lối đi.",
  "JULIAN nhìn ADRIAN. ADRIAN nhìn về phía cuối lối đi ngoài khung.",
  "JULIAN — người lần đầu tiên trong đời phải xin: mặt tái, giọng nhanh, hai tay ngửa. "
  "ADRIAN — không nhìn anh ta, chỉ gọi một chức danh: mặt bình, giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng bước chân nặng tới từ phía cuối lối đi",
  ["JULIAN_TUX", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"JULIAN": "đứng nửa phải khung, hai tay đưa ra", "ADRIAN": "đứng thẳng nửa trái khung"},
  "cách nhau hai bước", {"JULIAN": "hai tay đưa ra phía trước, lòng bàn tay ngửa",
                         "ADRIAN": "một tay hất nhẹ về phía cuối lối đi"})
V("13", [23, 24], "trung 50mm · ADRIAN NÉT trái đứng thẳng + JULIAN NÉT phải hai tay đưa ra · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("JULIAN", "JULIAN_TUX")],
  "ADRIAN và JULIAN, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "JULIAN đưa hai tay ra phía trước, ADRIAN hất nhẹ tay về phía cuối lối đi mà không nhìn anh ta",
  [("JULIAN", "fast, pleading", 23), ("ADRIAN", "quiet, calling", 24)])

S("14", "trung 50mm, cao 1m55, cách DETECTIVE MOORE 2m2, đặt trong lòng nhà thờ lấy cả hai người",
  "DETECTIVE MOORE đứng ở nửa TRÁI khung trong áo măng tô xám, một tay cầm cuốn sổ tay bìa đen đã mở. "
  "JULIAN đứng ở nửa PHẢI khung, hai tay đã hạ xuống. " + KHACH,
  "DETECTIVE MOORE một tay cầm cuốn sổ tay mở, tay kia đưa ra phía JULIAN. JULIAN hai tay hạ xuống hai bên.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "DETECTIVE MOORE — đọc lệnh bắt bằng giọng của người đã đọc nó một nghìn lần: chậm, chắc, mặt mệt. "
  "JULIAN — nghe ba tội danh: mặt trắng bệch, giọng cao lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi DETECTIVE MOORE lật sang trang tiếp theo của cuốn sổ",
  ["DETECTIVE MOORE", "JULIAN_TUX"], "giữa nền đá cuối nhà thờ",
  {"DETECTIVE MOORE": "đứng nửa trái khung", "JULIAN": "đứng nửa phải khung"},
  "cách nhau một bước", {"DETECTIVE MOORE": "một tay cầm cuốn sổ tay mở, tay kia đưa ra phía JULIAN",
                         "JULIAN": "hai tay hạ xuống hai bên"})
V("14", [25, 26], "trung 50mm · DETECTIVE MOORE NÉT trái cầm sổ tay + JULIAN NÉT phải · khách nền mờ",
  [("DETECTIVE MOORE", "DETECTIVE MOORE"), ("JULIAN", "JULIAN_TUX")],
  "DETECTIVE MOORE và JULIAN, cả hai rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "DETECTIVE MOORE mở cuốn sổ tay bìa đen và đọc lệnh bắt",
  [("DETECTIVE MOORE", "slow, procedural", 25), ("JULIAN", "shrill, denying", 26)])

S("15", "cận-trung 85mm, cao 1m55, cách DETECTIVE MOORE 1m6, đặt trong lòng nhà thờ lấy cả hai người",
  "DETECTIVE MOORE đứng ở nửa TRÁI khung, cuốn sổ tay đã lật sang trang mới. JULIAN đứng ở nửa PHẢI khung, "
  "đã lùi lại nửa bước. Hậu cảnh là cột đá và khách vây quanh mờ.",
  "DETECTIVE MOORE một tay lần theo một dòng trong cuốn sổ. JULIAN một tay đưa lên nới cổ nơ.",
  "DETECTIVE MOORE nhìn xuống cuốn sổ rồi ngước lên nhìn JULIAN. JULIAN nhìn cuốn sổ.",
  "DETECTIVE MOORE — đọc ra bằng chứng từng món một: giọng chậm, chắc. "
  "JULIAN — mỗi món làm anh ta lùi thêm nửa bước: mặt trắng, tay run ở cổ nơ.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN quay đầu về phía cuối lối đi",
  ["DETECTIVE MOORE", "JULIAN_TUX"], "giữa nền đá cuối nhà thờ",
  {"DETECTIVE MOORE": "đứng nửa trái khung", "JULIAN": "đứng lùi nửa bước, nửa phải khung"},
  "cách nhau một bước", {"DETECTIVE MOORE": "một tay lần theo một dòng trong cuốn sổ",
                         "JULIAN": "một tay đưa lên nới cổ nơ"})
V("15", [27, 28], "cận-trung 85mm · DETECTIVE MOORE NÉT trái lần theo dòng sổ tay + JULIAN NÉT phải lùi nửa bước",
  [("DETECTIVE MOORE", "DETECTIVE MOORE"), ("JULIAN", "JULIAN_TUX")],
  "DETECTIVE MOORE và JULIAN, cả hai rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "DETECTIVE MOORE lần ngón tay theo một dòng trong cuốn sổ và đọc",
  [("DETECTIVE MOORE", "slow, factual", 27), ("JULIAN", "thin, denying", 28)])

S("16", "trung 50mm, cao 1m55, cách JULIAN 2m2, đặt trong lòng nhà thờ lấy cả ba người",
  "JULIAN đứng ở giữa khung, đã quay hẳn về phía ADRIAN. DETECTIVE MOORE đứng ở nửa TRÁI khung, cuốn sổ đã gập. "
  "ADRIAN đứng thẳng ở nửa PHẢI khung. " + KHACH,
  "JULIAN hai tay đưa ra phía ADRIAN. DETECTIVE MOORE một tay gập cuốn sổ lại. ADRIAN hai tay buông dọc thân.",
  "JULIAN nhìn ADRIAN. ADRIAN nhìn JULIAN. DETECTIVE MOORE nhìn JULIAN.",
  "DETECTIVE MOORE — đọc nốt con số cuối cùng: giọng chậm, mặt mệt. "
  "JULIAN — gọi tên người anh em họ và nhắc tới tuổi thơ: mặt tan ra, giọng vỡ. ADRIAN — mặt hoàn toàn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu trả lời",
  ["JULIAN_TUX", "DETECTIVE MOORE", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"JULIAN": "đứng giữa khung", "DETECTIVE MOORE": "đứng nửa trái khung",
   "ADRIAN": "đứng thẳng nửa phải khung"},
  "ba người trong vòng hai mét",
  {"JULIAN": "hai tay đưa ra phía ADRIAN", "DETECTIVE MOORE": "một tay gập cuốn sổ lại",
   "ADRIAN": "hai tay buông dọc thân"})
V("16", [29, 30], "trung 50mm · DETECTIVE MOORE NÉT trái + JULIAN NÉT giữa đưa hai tay ra + ADRIAN NÉT phải đứng thẳng",
  [("DETECTIVE MOORE", "DETECTIVE MOORE"), ("JULIAN", "JULIAN_TUX"), ("ADRIAN", "ADRIAN_VEST")],
  "DETECTIVE MOORE, JULIAN và ADRIAN, cả ba rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "DETECTIVE MOORE gập cuốn sổ lại, JULIAN quay hẳn sang đưa hai tay về phía ADRIAN",
  [("DETECTIVE MOORE", "slow, damning", 29), ("JULIAN", "breaking, pleading", 30)])

S("17", "cận 85mm, cao 1m55, cách ADRIAN 1m3, máy sau vai PHẢI của JULIAN; vai và gáy anh chiếm rìa phải, out nét",
  "ADRIAN đứng thẳng chính diện chiếm phần lớn khung. JULIAN chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, "
  "ngoài vùng nét. Hậu cảnh là lối đi trải thảm trắng và khách vây quanh mờ.",
  "ADRIAN một tay hơi mở ra rồi khép lại bên hông.",
  "ADRIAN nhìn thẳng vào mặt JULIAN.",
  "ADRIAN — người nhắc lại chính câu của anh họ mình rồi nói ra lý do mình đã đợi lâu như vậy: "
  "giọng rất nhỏ, chậm, mắt ướt một nhịp rồi khô lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi có bàn tay đặt lên vai JULIAN từ phía sau",
  ["ADRIAN_VEST", "JULIAN_TUX"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng chính diện giữa khung", "JULIAN": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"ADRIAN": "một tay hơi mở ra rồi khép lại bên hông",
                         "JULIAN": "hai tay đưa ra, ngoài vùng nét"})
V("17", [31], "OTS cận 85mm · ADRIAN NÉT chính diện đứng thẳng · vai và gáy JULIAN tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_VEST"), ("JULIAN", "JULIAN_TUX")],
  "ADRIAN rõ mặt chính diện, ĐỨNG THẲNG TRÊN HAI CHÂN. JULIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "ADRIAN mở một bàn tay ra rồi khép lại bên hông trong lúc nói",
  [("ADRIAN", "very quiet, weighted", 31)], [("JULIAN", "silent, hands out")])

S("18", "cận-trung 85mm, cao 1m55, cách GUEST ONE 1m7, đặt trong vòng người vây quanh",
  "GUEST ONE đứng ở nửa TRÁI khung, GUEST TWO đứng ở nửa PHẢI khung sát cạnh. Cả hai đã hạ ly xuống. "
  "Hậu cảnh là các cụm khách khác đứng im, mờ.",
  "GUEST ONE hai tay đan lại trước bụng, ly đã đặt xuống. GUEST TWO một tay ôm chiếc clutch nhung.",
  "Cả hai nhìn về phía ADRIAN ngoài khung. TUYỆT ĐỐI không ai nhìn vào ống kính.",
  "GUEST ONE — người vừa nhận ra cả phòng đang im vì xấu hổ chứ không vì sợ: mắt hạ xuống, giọng nhỏ. "
  "GUEST TWO — mặt cứng, mắt ướt.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả hai người cùng cúi đầu xuống",
  ["GUEST1_TUX", "GUEST2_DAHOI"], "trong vòng người vây quanh, cuối nhà thờ",
  {"GUEST ONE": "đứng nửa trái khung", "GUEST TWO": "đứng nửa phải khung"},
  "sát cạnh nhau", {"GUEST ONE": "hai tay đan lại trước bụng", "GUEST TWO": "một tay ôm chiếc clutch nhung"})
V("18", [32], "cận-trung 85mm · GUEST ONE NÉT trái + GUEST TWO NÉT phải, cùng nhìn về phía ADRIAN · khách nền mờ",
  [("GUEST ONE", "GUEST1_TUX"), ("GUEST TWO", "GUEST2_DAHOI")],
  "GUEST ONE và GUEST TWO, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GUEST ONE đan hai tay lại trước bụng và nói rất nhỏ với người bên cạnh",
  [("GUEST ONE", "small, ashamed", 32)], [("GUEST TWO", "silent, eyes wet")])

S("19", "trung 50mm, cao 1m55, cách ADRIAN 2m2, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, một tay chìa về phía MAYA. MAYA đứng ở nửa PHẢI khung, áo vest đen "
  "khoác trên vai. " + KHACH,
  "ADRIAN một tay chìa ngửa về phía MAYA. MAYA hai tay giữ hai vạt áo vest trước ngực.",
  "ADRIAN nhìn quét qua vòng khách vây quanh. MAYA nhìn ADRIAN.",
  "ADRIAN — người quay sang nói về vợ mình chứ không nói về mình: giọng chậm, rõ, mắt quét khắp phòng. "
  "MAYA — bị cả bốn trăm người nhìn cùng lúc: cằm ngang, mắt ướt, không cụp xuống.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN hạ bàn tay đang chìa xuống",
  ["ADRIAN_VEST", "MAYA_TRANG"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "MAYA": "đứng nửa phải khung, áo vest khoác trên vai"},
  "cách nhau một bước", {"ADRIAN": "một tay chìa ngửa về phía MAYA",
                         "MAYA": "hai tay giữ hai vạt áo vest trước ngực"})
V("19", [33], "trung 50mm · ADRIAN NÉT trái đứng thẳng chìa tay + MAYA NÉT phải khoác áo vest · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN và MAYA, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN chìa một bàn tay ngửa về phía MAYA và nói với cả gian phòng",
  [("ADRIAN", "slow, damning", 33)], [("MAYA", "silent, chin level")])

S("20", "trung 50mm, cao 1m55, cách ADRIAN 2m4, đặt trong lòng nhà thờ lấy cả ba người",
  "ADRIAN đứng thẳng ở nửa TRÁI khung. GUEST TWO đứng ở nửa PHẢI khung, đã bước lên nửa bước từ vòng người. "
  "MAYA đứng ở giữa khung phía sau ADRIAN, thấy rõ mặt. " + KHACH,
  "ADRIAN hai tay buông dọc thân. GUEST TWO một tay đưa lên ngang ngực. MAYA hai tay giữ vạt áo vest.",
  "GUEST TWO nhìn ADRIAN. ADRIAN nhìn GUEST TWO. MAYA nhìn ADRIAN.",
  "GUEST TWO — nói ra câu biện hộ tệ nhất mà không biết mình đang tự tố: giọng nhỏ, mắt né. "
  "ADRIAN — chỉ ra đúng chỗ hỏng trong câu đó: giọng chậm, mắt tĩnh, KHÔNG lớn tiếng. MAYA — mắt ướt.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN quay người về phía MAYA",
  ["ADRIAN_VEST", "GUEST2_DAHOI", "MAYA_TRANG"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "GUEST TWO": "bước lên nửa bước, nửa phải khung",
   "MAYA": "đứng giữa khung phía sau ADRIAN"},
  "ba người trong vòng hai mét",
  {"ADRIAN": "hai tay buông dọc thân", "GUEST TWO": "một tay đưa lên ngang ngực",
   "MAYA": "hai tay giữ vạt áo vest"})
VX("20", "trung 50mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT giữa phía sau anh + GUEST TWO NÉT phải",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG"), ("GUEST TWO", "GUEST2_DAHOI")],
  "ADRIAN, MAYA và GUEST TWO, cả ba rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GUEST TWO bước lên nửa bước và đưa tay lên ngang ngực, ADRIAN trả lời cả gian phòng",
  [("GUEST TWO", "small, excusing", "Sir, we did not know who you were."),
   ("ADRIAN", "slow, final",
    "That is the whole problem. You needed to know who I was before you would be decent.")])

S("20b", "cận-trung 85mm, cao 1m55, cách ADRIAN 1m5, đặt trong lòng nhà thờ, lấy ADRIAN nét và MAYA cùng khung",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, đã quay hẳn về phía MAYA. MAYA đứng ở nửa PHẢI khung, áo vest đen "
  "khoác trên vai. Hậu cảnh là vòng khách vây quanh, mờ.",
  "ADRIAN một tay đưa về phía MAYA, lòng bàn tay ngửa. MAYA hai tay giữ hai vạt áo vest trước ngực.",
  "ADRIAN nhìn quét qua vòng khách rồi nhìn MAYA. MAYA nhìn ADRIAN.",
  "ADRIAN — người chốt lại bằng một phép so sánh về thời gian: giọng chậm, rõ, mắt tĩnh, KHÔNG lớn tiếng. "
  "MAYA — nghe câu nói về bốn tuần của chính mình: mắt ướt, cằm ngang.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả gian nhà thờ im hẳn",
  ["ADRIAN_VEST", "MAYA_TRANG"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "sát nhau", {"ADRIAN": "một tay đưa về phía MAYA, lòng bàn tay ngửa",
               "MAYA": "hai tay giữ hai vạt áo vest trước ngực"})
VX("20b", "cận-trung 85mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT phải khoác áo vest",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
   "ADRIAN và MAYA, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
   "Khách vây quanh mờ, không ai nhìn vào camera.",
   "ADRIAN đưa một bàn tay ngửa về phía MAYA và nói nốt câu cuối",
   [("ADRIAN", "slow, final",
     "You humiliated my wife for four weeks. It took me four minutes to end all of you.")],
   [("MAYA", "silent, chin level")])

# ── NHỊP KHÉP CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách ADRIAN 10m, đặt ở cuối lối đi phía cửa lớn nhìn về bàn thờ",
  "Lòng nhà thờ nhìn từ cuối lối đi: ADRIAN đứng thẳng giữa nền đá cẩm thạch, MAYA đứng sát cạnh anh, "
  "áo vest đen khoác trên vai cô. Quanh hai người, khách dự tiệc đứng thành vòng rộng và đã lùi ra xa, "
  "mờ ngoài vùng nét. Chiếc xe lăn tay cũ còn đổ nghiêng trên nền đá phía sau.",
  "ADRIAN một tay đặt trên vai MAYA. MAYA một tay giữ vạt áo vest trước ngực.",
  "Hai người cùng nhìn dọc lối đi về phía cửa lớn. Khách nền TUYỆT ĐỐI không nhìn vào ống kính.",
  "ADRIAN — người vừa kết thúc mọi thứ trong bốn phút và không hề thấy nhẹ đi: mặt bình, hơi thở nặng. "
  "MAYA — đứng cạnh anh giữa một gian phòng vừa đổi chủ: mặt trống, mắt ướt, vai cân.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai cánh cửa lớn cuối nhà thờ được mở toang",
  ["ADRIAN_VEST", "MAYA_TRANG"], "lòng nhà thờ, giữa nền đá cẩm thạch",
  {"ADRIAN": "đứng thẳng giữa nền đá", "MAYA": "đứng sát cạnh anh"},
  "sát nhau", {"ADRIAN": "một tay đặt trên vai MAYA", "MAYA": "một tay giữ vạt áo vest trước ngực"})
B("B1", "Khép cảnh. ADRIAN và MAYA đứng giữa nhà thờ, vòng khách đã lùi ra xa; chiếc xe lăn cũ còn đổ trên nền đá.",
  "toàn cảnh 24mm · ADRIAN NÉT ĐỨNG THẲNG giữa nền đá + MAYA NÉT đứng sát cạnh anh · khách vây quanh mờ, đã lùi xa",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN và MAYA rõ mặt, đứng sát nhau giữa nền đá. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách dự tiệc đứng thành vòng rộng, mờ, không ai nhìn vào camera.",
  "bốn phút trước, cả gian phòng này còn đang cười hai người họ; bây giờ không ai dám đứng gần trong phạm vi "
  "năm mét, và đó chính là nội dung của khung hình.",
  "vòng người vây quanh lùi thêm nửa bước; một chiếc ly champagne bị bỏ lại trên nền đá; MAYA nghiêng đầu "
  "tựa nhẹ vào vai ADRIAN một nhịp rồi đứng thẳng lại; đèn pha lê trên cao rung rất khẽ.",
  "Ambient tiếng vọng của một gian nhà thờ đá đang im, SFX tiếng bước chân lùi lại trên nền đá cẩm thạch.",
  nhac("NGHỈ", "Sau bốn phút liên tiếp toàn giọng nói và án lệnh, khán giả cần một khoảng gần như câm trước khi ra tới bậc thềm.",
       "Ambient chamber at 56 BPM; a viola holding one long note under a harp placing single notes with long gaps, "
       "a female voice humming wordlessly twice far back in the mix; no drums; the pull is a long gap of cathedral "
       "reverb; wordless and spent; large natural reverb, female vocal, viola, harp, ambient, still",
       "Ambient instrumental at 54 BPM; a solo viola holding one long note, a harp placing single notes every four "
       "seconds, a very low organ pedal underneath, no percussion, fading into reverb; "
       "large natural reverb, viola, harp, organ, minimal, spent"),
  dur=10)
