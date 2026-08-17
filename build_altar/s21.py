# -*- coding: utf-8 -*-
"""SCENE 21 — CÚ GÀI VÒNG CỔ (nhà thờ St. Michael, chiều)."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S21", "REF_NHATHOTIEC_CHIEU", qc=qc.S21)

KHACH = ""

S("01", "trung 50mm, cao 1m55, cách VANESSA 2m4, đặt trong lòng nhà thờ lấy cả hai người",
  "VANESSA đứng ở nửa TRÁI khung trong váy cưới, một tay giơ lên. GERALD HALE đứng ở nửa PHẢI khung, "
  "đã quay hẳn về phía cô. " + KHACH,
  "VANESSA một tay giơ lên ngang đầu ra hiệu dừng, tay kia nắm lấy phần cổ áo trống của mình. "
  "GERALD HALE một tay đưa ra phía con gái.",
  "VANESSA nhìn quanh gian nhà thờ. GERALD HALE nhìn VANESSA.",
  "VANESSA — người vừa phát hiện ra thứ mình cần cả phòng chú ý: mắt mở to, giọng vang. "
  "GERALD HALE — quay ngay sang con gái: mày chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi tiếng đàn trong nhà thờ tắt hẳn",
  ["VANESSA_CODAU", "GERALD HALE"], "giữa lòng nhà thờ, gần bàn thờ",
  {"VANESSA": "đứng nửa trái khung", "GERALD HALE": "đứng nửa phải khung"},
  "sát cạnh nhau", {"VANESSA": "một tay giơ ngang đầu ra hiệu dừng, tay kia nắm cổ áo trống",
                    "GERALD HALE": "một tay đưa ra phía con gái"})
V("01", [0, 1], "trung 50mm · VANESSA NÉT trái giơ tay ra hiệu + GERALD HALE NÉT phải · khách nền mờ",
  [("VANESSA", "VANESSA_CODAU"), ("GERALD HALE", "GERALD HALE")],
  "VANESSA và GERALD HALE, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA giơ tay lên ra hiệu cho nhạc dừng, GERALD HALE quay sang con gái",
  [("VANESSA", "loud, alarmed", 0), ("GERALD HALE", "quick, concerned", 1)])

S("02", "cận-trung 85mm, cao 1m55, cách VANESSA 1m7, đặt trong lòng nhà thờ lấy VANESSA nét và GERALD cùng khung",
  "VANESSA đứng ở nửa TRÁI khung, một bàn tay đặt lên phần cổ trống trên ngực mình. GERALD HALE đứng ở nửa PHẢI "
  "khung. Hậu cảnh là cột hoa trắng cao và khách dự tiệc mờ.",
  "VANESSA một bàn tay đặt lên phần cổ trống trên ngực, tay kia chỉ về phía cửa phục vụ ở cuối phòng. "
  "GERALD HALE một tay giơ lên ra hiệu cho người của mình.",
  "VANESSA nhìn GERALD HALE rồi quét mắt về cuối phòng. GERALD HALE nhìn về phía cuối phòng.",
  "VANESSA — người diễn hoảng hốt rất khéo: mắt mở to, giọng vỡ đúng chỗ. "
  "GERALD HALE — ra lệnh ngay lập tức: mặt cứng, giọng vang.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai cánh cửa lớn cuối nhà thờ được đóng lại",
  ["VANESSA_CODAU", "GERALD HALE"], "giữa lòng nhà thờ, gần bàn thờ",
  {"VANESSA": "đứng nửa trái khung", "GERALD HALE": "đứng nửa phải khung"},
  "sát cạnh nhau", {"VANESSA": "một bàn tay đặt lên phần cổ trống, tay kia chỉ về cuối phòng",
                    "GERALD HALE": "một tay giơ lên ra hiệu"})
V("02", [2, 3], "cận-trung 85mm · VANESSA NÉT trái tay đặt lên cổ trống + GERALD HALE NÉT phải · khách nền mờ",
  [("VANESSA", "VANESSA_CODAU"), ("GERALD HALE", "GERALD HALE")],
  "VANESSA và GERALD HALE, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA đặt bàn tay lên phần cổ trống trên ngực mình và chỉ về cuối phòng",
  [("VANESSA", "alarmed, performing", 2), ("GERALD HALE", "loud, commanding", 3)])

S("03", "trung 50mm, cao 1m55, cách SECURITY CHIEF 2m2, đặt trong lòng nhà thờ lấy cả hai người",
  "SECURITY CHIEF đứng ở nửa PHẢI khung, một tay đưa lên tai nghe xoắn dây. VANESSA đứng ở nửa TRÁI khung, "
  "đã quay hẳn về phía cuối phòng. " + KHACH,
  "SECURITY CHIEF một tay đưa lên tai nghe, tay kia chỉ về phía nhóm phục vụ. VANESSA một tay chỉ thẳng "
  "về phía cửa phục vụ.",
  "SECURITY CHIEF nhìn VANESSA chờ lệnh. VANESSA nhìn về phía cuối phòng, không nhìn ông.",
  "SECURITY CHIEF — đề xuất theo đúng quy trình: mặt trung tính, giọng gọn. "
  "VANESSA — chỉ đích danh một người: cằm hếch, mắt sáng, giọng dứt khoát.",
  "đúng khoảnh khắc ngay TRƯỚC khi SECURITY CHIEF bước về phía cuối phòng",
  ["SECURITY CHIEF", "VANESSA_CODAU"], "giữa lòng nhà thờ",
  {"SECURITY CHIEF": "đứng nửa phải khung", "VANESSA": "đứng nửa trái khung"},
  "cách nhau một bước", {"SECURITY CHIEF": "một tay đưa lên tai nghe, tay kia chỉ về nhóm phục vụ",
                         "VANESSA": "một tay chỉ thẳng về phía cửa phục vụ"})
V("03", [4, 5], "trung 50mm · VANESSA NÉT trái chỉ về cuối phòng + SECURITY CHIEF NÉT phải · khách nền mờ",
  [("VANESSA", "VANESSA_CODAU"), ("SECURITY CHIEF", "SECURITY CHIEF")],
  "VANESSA và SECURITY CHIEF, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "SECURITY CHIEF đưa tay lên tai nghe chờ lệnh, VANESSA chỉ thẳng về phía cửa phục vụ",
  [("SECURITY CHIEF", "flat, procedural", 4), ("VANESSA", "clipped, pointed", 5)])

S("04", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt cuối nhà thờ lấy cả hai người, cửa phục vụ ở hậu cảnh",
  "MAYA đứng ở nửa PHẢI khung sát cửa phục vụ, chiếc TÚI VẢI của cô đặt trên mặt bàn dài phủ khăn trắng cạnh đó. "
  "VANESSA đứng ở nửa TRÁI khung, đã đi xuống tới nơi, váy cưới kéo lê phía sau. " + KHACH,
  "MAYA hai tay chắp trước bụng, tay phải có nẹp nhôm. VANESSA một tay chỉ vào chiếc túi vải trên bàn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người biết mình đang bị chỉ mặt và trả lời bằng dữ kiện: giọng bình, mắt thẳng. "
  "VANESSA — người đã biết trong túi có gì: khoé môi cong, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA chạm vào chiếc túi vải của mình",
  ["MAYA_TRANG", "VANESSA_CODAU"], "cuối nhà thờ bên phải, cạnh cửa phục vụ và bàn dài",
  {"MAYA": "đứng sát cửa phục vụ nửa phải khung", "VANESSA": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "hai tay chắp trước bụng, tay phải có nẹp",
                         "VANESSA": "một tay chỉ vào chiếc túi vải trên bàn"})
V("04", [6, 7], "trung 50mm · VANESSA NÉT trái chỉ vào chiếc túi + MAYA NÉT phải cạnh cửa phục vụ · khách nền mờ",
  [("VANESSA", "VANESSA_CODAU"), ("MAYA", "MAYA_TRANG")],
  "VANESSA và MAYA, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA chỉ vào chiếc túi vải đặt trên bàn dài cạnh MAYA",
  [("MAYA", "level, factual", 6), ("VANESSA", "sweet, baiting", 7)])

S("05", "cận-trung 85mm, cao 1m40, cách MAYA 1m7, đặt cuối nhà thờ, lấy MAYA nét và SECURITY CHIEF cùng khung",
  "SECURITY CHIEF đứng ở nửa TRÁI khung cạnh bàn dài, một tay đưa ra phía chiếc TÚI VẢI. MAYA đứng ở nửa PHẢI "
  "khung, đã đặt bàn tay trái lên chiếc túi. Hậu cảnh là cửa phục vụ hẹp và khăn bàn trắng.",
  "SECURITY CHIEF một tay đưa ra phía chiếc túi vải. MAYA bàn tay trái đặt lên chiếc túi, tay phải có nẹp "
  "giữ sát người.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "SECURITY CHIEF — làm đúng quy trình, không thù ghét: mặt trung tính, giọng lễ độ. "
  "MAYA — đẩy chiếc túi ra không do dự một giây: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi SECURITY CHIEF mở miệng chiếc túi ra",
  ["SECURITY CHIEF", "MAYA_TRANG"], "cuối nhà thờ bên phải, cạnh bàn dài phủ khăn trắng",
  {"SECURITY CHIEF": "đứng cạnh bàn dài nửa trái khung", "MAYA": "đứng nửa phải khung, tay đặt lên chiếc túi"},
  "cách nhau một bước", {"SECURITY CHIEF": "một tay đưa ra phía chiếc túi vải",
                         "MAYA": "bàn tay trái đặt lên chiếc túi, tay phải có nẹp giữ sát người"})
V("05", [8, 9], "cận-trung 85mm · SECURITY CHIEF NÉT trái + MAYA NÉT phải tay đặt lên chiếc túi",
  [("SECURITY CHIEF", "SECURITY CHIEF"), ("MAYA", "MAYA_TRANG")],
  "SECURITY CHIEF và MAYA, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "SECURITY CHIEF đưa tay ra phía chiếc túi, MAYA đẩy chiếc túi về phía ông",
  [("SECURITY CHIEF", "polite, procedural", 8), ("MAYA", "flat, immediate", 9)],
  ketclip="Cuối clip, SECURITY CHIEF mở miệng chiếc túi vải, thò tay vào ngăn bên và rút ra một DÂY CHUYỀN "
          "KIM CƯƠNG lớn, giơ lên. Clip dừng đúng lúc dây chuyền lơ lửng trong tay ông.")

S("06", "trung 50mm, cao 1m55, cách SECURITY CHIEF 2m2, đặt cuối nhà thờ lấy cả ba người",
  "SECURITY CHIEF đứng ở nửa TRÁI khung, một tay giơ cao DÂY CHUYỀN KIM CƯƠNG. MAYA đứng ở nửa PHẢI khung, "
  "bất động. GUEST ONE đứng ở rìa phải khung phía sau, đã quay hẳn lại nhìn, thấy rõ mặt.",
  "SECURITY CHIEF một tay giơ cao dây chuyền kim cương, tay kia còn giữ miệng chiếc túi. "
  "MAYA hai tay buông xuống hai bên. GUEST ONE một tay đưa lên miệng.",
  "SECURITY CHIEF nhìn dây chuyền trong tay mình. MAYA nhìn dây chuyền. GUEST ONE nhìn dây chuyền.",
  "SECURITY CHIEF — báo cáo một sự thật vật lý: mặt trung tính. "
  "MAYA — nhìn thứ mình chưa từng thấy trong đời nằm trong túi mình: mắt mở to, mặt trắng ra. "
  "GUEST ONE — thốt lên: miệng mở, mắt tròn.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả một vùng phòng quay đầu lại",
  ["SECURITY CHIEF", "MAYA_TRANG", "GUEST1_TUX", "PROP_VONGCO"],
  "cuối nhà thờ bên phải, cạnh bàn dài phủ khăn trắng",
  {"SECURITY CHIEF": "đứng nửa trái khung giơ dây chuyền", "MAYA": "đứng nửa phải khung",
   "GUEST ONE": "đứng rìa phải khung phía sau"},
  "ba người trong vòng hai mét",
  {"SECURITY CHIEF": "một tay giơ cao dây chuyền, tay kia giữ miệng chiếc túi",
   "MAYA": "hai tay buông xuống hai bên", "GUEST ONE": "một tay đưa lên miệng"})
V("06", [10, 11], "trung 50mm · SECURITY CHIEF NÉT trái giơ dây chuyền + MAYA NÉT phải + GUEST ONE NÉT rìa phải phía sau",
  [("SECURITY CHIEF", "SECURITY CHIEF"), ("MAYA", "MAYA_TRANG"), ("GUEST ONE", "GUEST1_TUX")],
  "SECURITY CHIEF, MAYA và GUEST ONE, cả ba rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "SECURITY CHIEF rút dây chuyền kim cương ra khỏi ngăn bên chiếc túi và giơ cao lên",
  [("SECURITY CHIEF", "flat, reporting", 10), ("GUEST ONE", "shocked, hushed", 11)])

S("07", "trung 50mm, cao 1m55, cách GERALD HALE 2m4, đặt cuối nhà thờ lấy cả hai người",
  "GERALD HALE đứng ở nửa TRÁI khung, đã đi xuống tới nơi. RYAN đứng ở nửa PHẢI khung cạnh ông, ly champagne "
  "đã hạ xuống. " + KHACH,
  "GERALD HALE một tay chỉ về phía dây chuyền ngoài khung, tay kia nắm lại. "
  "RYAN một tay cầm ly hạ xuống ngang đùi.",
  "GERALD HALE nhìn về phía cuối phòng ngoài khung. RYAN cũng nhìn về hướng đó.",
  "GERALD HALE — người vừa có một vụ trộm trước ống kính truyền hình trong đám cưới con gái mình: "
  "mặt đỏ lên, giọng vang. RYAN — chưa kịp hiểu và đã chọn phe: mày chau, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước một bước về phía cuối phòng",
  ["GERALD HALE", "RYAN_TUXEDO"], "cuối nhà thờ, giữa lối đi",
  {"GERALD HALE": "đứng nửa trái khung", "RYAN": "đứng nửa phải khung cạnh ông"},
  "sát cạnh nhau", {"GERALD HALE": "một tay chỉ về phía dây chuyền ngoài khung, tay kia nắm lại",
                    "RYAN": "một tay cầm ly hạ xuống ngang đùi"})
V("07", [12, 13], "trung 50mm · GERALD HALE NÉT trái + RYAN NÉT phải, đứng cạnh nhau · khách nền mờ",
  [("GERALD HALE", "GERALD HALE"), ("RYAN", "RYAN_TUXEDO")],
  "GERALD HALE và RYAN, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GERALD HALE chỉ về phía dây chuyền, RYAN hạ ly champagne xuống",
  [("GERALD HALE", "loud, outraged", 12), ("RYAN", "stricken, loud", 13)])

S("08", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, đặt cuối nhà thờ lấy MAYA nét và RYAN cùng khung",
  "MAYA đứng ở nửa PHẢI khung, RYAN đứng ở nửa TRÁI khung cách một bước, đã quay hẳn về phía cô. "
  "Hậu cảnh là cửa phục vụ và một chân máy quay truyền hình có đèn LED tròn đang sáng.",
  "MAYA hai tay buông xuống hai bên, bàn tay phải có nẹp thấy rõ. RYAN một tay chỉ về phía chiếc túi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người nhắc lại bốn năm bằng bốn chữ: giọng thấp, mắt không rời. "
  "RYAN — quay hẳn sang phía ống kính truyền hình: mắt sáng lên, giọng cao.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN vẫy tay gọi máy quay lại gần",
  ["MAYA_TRANG", "RYAN_TUXEDO"], "cuối nhà thờ bên phải, cạnh cửa phục vụ",
  {"MAYA": "đứng nửa phải khung", "RYAN": "đứng nửa trái khung"},
  "cách nhau một bước", {"MAYA": "hai tay buông xuống, tay phải có nẹp",
                         "RYAN": "một tay chỉ về phía chiếc túi"})
V("08", [14, 15], "cận-trung 85mm · RYAN NÉT trái + MAYA NÉT phải, đứng đối diện · đèn máy quay ở hậu cảnh",
  [("RYAN", "RYAN_TUXEDO"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "MAYA nói một câu rất thấp, RYAN quay hẳn sang phía đèn máy quay truyền hình",
  [("MAYA", "low, plain", 14), ("RYAN", "raised, performing", 15)])

S("09", "trung 50mm, cao 1m55, cách VANESSA 2m2, đặt cuối nhà thờ lấy cả hai người",
  "VANESSA đứng ở nửa TRÁI khung, váy cưới trắng xoè lớn, một tay chỉ xuống nền đá trước mặt MAYA. "
  "MAYA đứng ở nửa PHẢI khung, chưa nhúc nhích. " + KHACH,
  "VANESSA một tay chỉ xuống nền đá, tay kia vén nhẹ vạt váy. MAYA hai tay buông xuống hai bên.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "VANESSA — người ra lệnh cho một người quỳ xuống giữa nhà thờ: cằm hếch, giọng vang, mắt sáng. "
  "MAYA — trả lời một chữ và không nhúc nhích: mặt hoàn toàn bình, hai chân đứng nguyên.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA nhắc lại mệnh lệnh to hơn",
  ["VANESSA_CODAU", "MAYA_TRANG"], "cuối nhà thờ bên phải, giữa lối đi cạnh cửa phục vụ",
  {"VANESSA": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau một bước", {"VANESSA": "một tay chỉ xuống nền đá, tay kia vén vạt váy",
                         "MAYA": "hai tay buông xuống hai bên"})
V("09", [16, 17, 18], "trung 50mm · VANESSA NÉT trái chỉ xuống nền + MAYA NÉT phải đứng nguyên · khách nền mờ",
  [("VANESSA", "VANESSA_CODAU"), ("MAYA", "MAYA_TRANG")],
  "VANESSA và MAYA, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA chỉ xuống nền đá trước mặt MAYA, MAYA đứng nguyên không nhúc nhích",
  [("VANESSA", "loud, commanding", 16), ("MAYA", "flat, immovable", 17),
   ("VANESSA", "louder, insisting", 18)])

S("10", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, máy sau vai TRÁI của VANESSA; vai và gáy cô chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. VANESSA chỉ còn là vai và một mảng váy cưới trắng ở rìa TRÁI "
  "tiền cảnh, ngoài vùng nét. Hậu cảnh là cửa phục vụ và bàn dài phủ khăn trắng.",
  "MAYA hai tay buông xuống hai bên, các ngón duỗi thẳng.",
  "MAYA nhìn thẳng vào mặt VANESSA.",
  "MAYA — người nói ra một sự thật đơn giản và không giải thích thêm: giọng bình, mắt không chớp, "
  "hai chân đứng nguyên.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng một người đàn ông cắt ngang từ ngoài khung bên trái",
  ["MAYA_TRANG", "VANESSA_CODAU"], "cuối nhà thờ bên phải, giữa lối đi",
  {"MAYA": "đứng chính diện giữa khung", "VANESSA": "vai và một mảng váy cưới ở rìa trái tiền cảnh"},
  "cách nhau một bước", {"MAYA": "hai tay buông xuống hai bên",
                         "VANESSA": "một tay chỉ xuống nền, ngoài vùng nét"})
V("10", [19, 20, 21], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và mảng váy cưới VANESSA tiền cảnh trái out nét · GERALD HALE ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_TRANG"), ("VANESSA", "VANESSA_CODAU"), ("GERALD HALE", "GERALD HALE")],
  "MAYA rõ mặt chính diện. VANESSA chỉ thấy VAI và một mảng váy cưới trắng ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera. GERALD HALE KHÔNG xuất hiện trong khung, chỉ nghe tiếng ông vọng "
  "tới từ ngoài khung bên trái.",
  "MAYA đứng nguyên, hai tay buông xuống, trả lời từng câu một",
  [("MAYA", "flat, plain", 19), ("GERALD HALE (off-screen, vọng từ phía lối đi)", "loud, accusing", 20),
   ("MAYA", "level, unchanged", 21)])

S("11", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt cuối nhà thờ lấy cả ba người",
  "MAYA đứng ở giữa khung. VANESSA đứng ở nửa TRÁI khung, một tay hất về phía RYAN. RYAN đứng ở nửa PHẢI khung, "
  "đã bước tới và nắm lấy TAY ÁO TRÁI của MAYA. " + KHACH,
  "VANESSA một tay hất về phía RYAN. RYAN một tay nắm lấy tay áo trái MAYA. "
  "MAYA một tay gỡ tay áo mình ra, bàn tay phải có nẹp giữ sát người.",
  "MAYA nhìn xuống bàn tay đang nắm tay áo mình. RYAN nhìn VANESSA. VANESSA nhìn MAYA.",
  "VANESSA — ra lệnh cho chồng mình giữ một người phụ nữ khác: giọng nhẹ, mắt sáng. "
  "RYAN — làm theo ngay: mặt cứng. MAYA — nghe tiếng vải rách: mày chau, giọng thấp.",
  "đúng khoảnh khắc ngay TRƯỚC khi đường chỉ vai áo MAYA bục ra",
  ["MAYA_TRANG", "VANESSA_CODAU", "RYAN_TUXEDO"], "cuối nhà thờ bên phải, giữa lối đi",
  {"MAYA": "đứng giữa khung", "VANESSA": "đứng nửa trái khung", "RYAN": "đứng nửa phải khung, nắm tay áo MAYA"},
  "ba người trong vòng một mét",
  {"VANESSA": "một tay hất về phía RYAN", "RYAN": "một tay nắm tay áo trái MAYA",
   "MAYA": "một tay gỡ tay áo, tay phải có nẹp giữ sát người"})
V("11", [22, 23], "trung 50mm · VANESSA NÉT trái + MAYA NÉT giữa + RYAN NÉT phải nắm tay áo cô · khách nền mờ",
  [("VANESSA", "VANESSA_CODAU"), ("MAYA", "MAYA_TRANG"), ("RYAN", "RYAN_TUXEDO")],
  "VANESSA, MAYA và RYAN, cả ba rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA hất tay ra lệnh, RYAN nắm lấy tay áo trái của MAYA và giữ",
  [("VANESSA", "light, ordering", 22), ("MAYA", "low, warning", 23)],
  ketclip="Cuối clip, đường chỉ ở vai áo trái MAYA bục ra một đoạn ngắn, mép vải sờn ra. "
          "Clip dừng đúng lúc tiếng vải rách vừa dứt.")

S("12", "cận-trung 85mm, cao 1m55, cách MAYA 1m5, đặt cuối nhà thờ lấy MAYA nét và RYAN cùng khung",
  "MAYA đứng ở nửa PHẢI khung, TAY ÁO TRÁI đã rách một đoạn ở vai, mép vải sờn ra. RYAN đứng ở nửa TRÁI khung, "
  "một tay còn giữ chỗ vải rách. Hậu cảnh là cột đá và đèn máy quay truyền hình.",
  "RYAN một tay còn giữ chỗ vải rách trên vai MAYA. MAYA hai tay buông xuống hai bên, không giằng lại.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — đưa ra điều kiện để dừng lại: giọng thấp, mắt né một nhịp. "
  "MAYA — nói ra nguyên tắc của cả đời mình bằng giọng rất bình: mắt thẳng, cằm ngang, KHÔNG run.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người bước tới sát sau lưng MAYA",
  ["MAYA_TRANG", "RYAN_TUXEDO"], "cuối nhà thờ bên phải, giữa lối đi",
  {"MAYA": "đứng nửa phải khung, tay áo trái đã rách", "RYAN": "đứng nửa trái khung, tay giữ chỗ vải rách"},
  "sát nhau", {"RYAN": "một tay giữ chỗ vải rách trên vai MAYA",
               "MAYA": "hai tay buông xuống hai bên"})
VX("12", "cận-trung 85mm · RYAN NÉT trái giữ chỗ vải rách + MAYA NÉT phải, tay áo trái đã rách",
  [("RYAN", "RYAN_TUXEDO"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. Tay áo trái của MAYA đã rách một đoạn ở vai, mép vải sờn ra. "
  "Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "RYAN giữ nguyên tay ở chỗ vải rách, MAYA không giằng lại",
  [("RYAN", "low, bargaining", "Then kneel and it stops."),
   ("MAYA", "level, absolute", "I am not going to apologize for something I did not do.")])

S("12b", "cận 85mm, cao 1m55, cách MAYA 1m3, máy sau vai TRÁI của RYAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, tay áo trái đã rách một đoạn ở vai. RYAN chỉ còn là vai và gáy "
  "ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là cột đá và đèn máy quay truyền hình.",
  "MAYA hai tay buông dọc thân, bàn tay phải có nẹp nhôm thấy rõ.",
  "MAYA nhìn thẳng vào mặt RYAN.",
  "MAYA — người nói ra nguyên tắc của cả đời mình giữa một nhà thờ đầy người: giọng bình, rõ từng chữ, "
  "cằm ngang, KHÔNG run.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người bước tới sát sau lưng MAYA",
  ["MAYA_TRANG", "RYAN_TUXEDO"], "cuối nhà thờ bên phải, giữa lối đi",
  {"MAYA": "đứng chính diện giữa khung, tay áo trái đã rách", "RYAN": "vai và gáy tiền cảnh trái"},
  "sát nhau", {"MAYA": "hai tay buông dọc thân, tay phải có nẹp",
               "RYAN": "một tay giữ chỗ vải rách, ngoài vùng nét"})
VX("12b", "OTS cận 85mm · MAYA NÉT chính diện, tay áo trái đã rách · vai và gáy RYAN tiền cảnh trái out nét",
   [("MAYA", "MAYA_TRANG"), ("RYAN", "RYAN_TUXEDO")],
   "MAYA rõ mặt chính diện, tay áo trái đã rách một đoạn ở vai. RYAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, "
   "out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
   "MAYA đứng nguyên, hai tay buông dọc thân, không giằng lại",
   [("MAYA", "level, absolute",
     "I have never apologized for something I did not do in my life and I am not starting in this church.")],
   [("RYAN", "silent, still holding the sleeve")])

S("13", "trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp, lấy MAYA đang đứng và VANESSA phía sau",
  "MAYA đứng ở giữa khung, hai chân còn đứng. VANESSA đứng ngay sau lưng cô ở nửa TRÁI khung, hai tay đã đặt "
  "lên hai vai MAYA. RYAN đứng ở nửa PHẢI khung, tay còn giữ tay áo rách.",
  "VANESSA hai tay đặt lên hai vai MAYA ấn xuống. MAYA hai tay buông, đầu gối chưa khuỵu. "
  "RYAN một tay giữ tay áo rách.",
  "MAYA nhìn thẳng phía trước. VANESSA nhìn xuống gáy MAYA. RYAN nhìn xuống nền.",
  "VANESSA — người quyết định tự tay làm việc đó: khoé môi kéo, mắt sáng. "
  "MAYA — hai chân còn trụ: quai hàm siết, mắt nhìn thẳng. RYAN — không dám nhìn: mắt hạ.",
  "đúng khoảnh khắc ngay TRƯỚC khi đầu gối MAYA chạm xuống nền đá",
  ["MAYA_TRANG", "VANESSA_CODAU", "RYAN_TUXEDO"], "cuối nhà thờ bên phải, giữa lối đi",
  {"MAYA": "đứng giữa khung, chưa khuỵu gối", "VANESSA": "đứng sau lưng MAYA nửa trái khung",
   "RYAN": "đứng nửa phải khung"},
  "ba người trong vòng một mét",
  {"VANESSA": "hai tay đặt lên hai vai MAYA ấn xuống", "MAYA": "hai tay buông, đầu gối chưa khuỵu",
   "RYAN": "một tay giữ tay áo rách"})
V("13", [26, 27], "trung 50mm hạ thấp · MAYA NÉT giữa còn đứng + VANESSA NÉT trái sau lưng cô + RYAN NÉT phải",
  [("MAYA", "MAYA_TRANG"), ("VANESSA", "VANESSA_CODAU"), ("RYAN", "RYAN_TUXEDO")],
  "MAYA, VANESSA và RYAN, cả ba rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA đặt hai tay lên vai MAYA và ấn xuống, MAYA khuỵu hai gối xuống nền đá",
  [("VANESSA", "light, deciding", 26), ("MAYA", "low, alarmed", 27)],
  ketclip="Cuối clip, MAYA quỳ hai gối xuống nền đá, bàn tay phải có nẹp chống xuống nền, và gót giày "
          "VANESSA đặt lên đúng chỗ đó. Clip dừng đúng lúc gót giày chạm lên chiếc nẹp.")

S("14", "cận-trung 85mm, cao 0m80, cách MAYA 1m5, máy hạ rất thấp ngang tầm người đang quỳ",
  "MAYA quỳ hai gối ở nửa PHẢI khung, bàn tay phải có NẸP NHÔM chống xuống nền đá. VANESSA đứng phía trên ở "
  "nửa TRÁI khung. GRANDMOTHER HALE ngồi trong chiếc xe lăn nhẹ ở rìa TRÁI khung phía sau, thấy rõ mặt.",
  "MAYA bàn tay phải có nẹp chống xuống nền đá, tay trái chống nền. VANESSA một tay vén vạt váy cưới. "
  "GRANDMOTHER HALE một tay giơ lên phía trước.",
  "MAYA nhìn xuống bàn tay mình. VANESSA nhìn xuống MAYA. GRANDMOTHER HALE nhìn VANESSA.",
  "MAYA — người vừa nhận ra sức nặng đặt lên đúng chỗ xương gãy: mắt mở to, hơi thở đứt, KHÔNG kêu to. "
  "VANESSA — thấy buồn cười: khoé môi kéo. GRANDMOTHER HALE — bà cụ duy nhất trong phòng lên tiếng: mắt sắc.",
  "đúng khoảnh khắc ngay TRƯỚC khi GRANDMOTHER HALE đẩy bánh xe lăn của mình tiến lên",
  ["MAYA_TRANG", "VANESSA_CODAU", "GRANDMOTHER HALE"], "cuối nhà thờ bên phải, MAYA quỳ trên nền đá",
  {"MAYA": "quỳ hai gối nửa phải khung", "VANESSA": "đứng phía trên nửa trái khung",
   "GRANDMOTHER HALE": "ngồi xe lăn nhẹ ở rìa trái khung phía sau"},
  "ba người trong vòng hai mét",
  {"MAYA": "bàn tay phải có nẹp chống xuống nền đá, tay trái chống nền",
   "VANESSA": "một tay vén vạt váy cưới", "GRANDMOTHER HALE": "một tay giơ lên phía trước"})
V("14", [28, 29], "cận-trung 85mm hạ rất thấp · MAYA NÉT phải quỳ trên nền đá + VANESSA NÉT trái đứng phía trên + GRANDMOTHER HALE NÉT rìa trái phía sau",
  [("MAYA", "MAYA_TRANG"), ("VANESSA", "VANESSA_CODAU"), ("GRANDMOTHER HALE", "GRANDMOTHER HALE")],
  "MAYA, VANESSA và GRANDMOTHER HALE, cả ba rõ mặt. MAYA quỳ hai gối trên nền đá, bàn tay phải có nẹp chống "
  "xuống nền. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA vén vạt váy cưới và đứng nguyên, GRANDMOTHER HALE giơ tay lên từ chiếc xe lăn nhẹ phía sau",
  [("VANESSA", "light, cruel", 28), ("GRANDMOTHER HALE", "sharp, commanding", 29)])

S("15", "trung 50mm, cao 0m90, cách VANESSA 2m, máy hạ thấp, lấy VANESSA đứng và ADRIAN đang tới ở hậu cảnh",
  "VANESSA đứng ở nửa TRÁI khung, đã quay đầu về phía bà cụ ngoài khung. Ở hậu cảnh nửa PHẢI khung, ADRIAN "
  "đang tự quay bánh chiếc xe lăn tay cũ tiến tới, thấy rõ mặt. Ở rìa dưới khung thấy vai MAYA đang quỳ, out nét.",
  "VANESSA một tay phẩy về phía sau. ADRIAN hai tay đẩy vành bánh xe tiến tới. MAYA quỳ dưới nền.",
  "VANESSA nhìn ra phía sau. ADRIAN nhìn thẳng vào VANESSA. MAYA nhìn xuống nền.",
  "VANESSA — gạt bà mình đi bằng ba chữ: giọng nhẹ, không quay hẳn người. "
  "ADRIAN — người vừa quyết định chấm dứt việc ngồi yên: mặt hoàn toàn bình, mắt tối lại, hai tay đẩy đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi bánh chiếc xe lăn tay cũ dừng lại cạnh chỗ MAYA quỳ",
  ["VANESSA_CODAU", "ADRIAN_TIEC", "MAYA_TRANG"], "cuối nhà thờ bên phải, giữa lối đi",
  {"VANESSA": "đứng nửa trái khung", "ADRIAN": "tự quay bánh xe tiến tới ở hậu cảnh nửa phải khung",
   "MAYA": "vai đang quỳ ở rìa dưới khung"},
  "ADRIAN cách bốn mét", {"VANESSA": "một tay phẩy về phía sau",
                          "ADRIAN": "hai tay đẩy vành bánh xe", "MAYA": "quỳ dưới nền, ngoài vùng nét"})
V("15", [30, 31], "trung 50mm hạ thấp · VANESSA NÉT trái + ADRIAN NÉT phải tự quay bánh xe tiến tới · vai MAYA rìa dưới out nét",
  [("VANESSA", "VANESSA_CODAU"), ("ADRIAN", "ADRIAN_TIEC"), ("MAYA", "MAYA_TRANG")],
  "VANESSA và ADRIAN rõ mặt. MAYA chỉ thấy VAI ở rìa dưới khung, đang quỳ, out nét. "
  "Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA phẩy tay về phía sau, ADRIAN tự quay bánh chiếc xe lăn tay cũ tiến tới",
  [("VANESSA", "light, dismissive", 30), ("ADRIAN", "quiet, absolute", 31)])

S("16", "trung 50mm, cao 1m20, cách ADRIAN 2m2, máy hạ thấp, lấy ADRIAN ngồi xe lăn và GERALD đứng phía trên",
  "ADRIAN ngồi trong chiếc xe lăn tay cũ ở nửa PHẢI khung, đã tới sát chỗ người phụ nữ quỳ dưới nền. GERALD HALE đứng ở nửa "
  "TRÁI khung, cao hơn hẳn trong khung, đã quay hẳn về phía anh. " + KHACH,
  "ADRIAN hai tay đặt trên vành bánh xe. GERALD HALE một tay chỉ xuống chiếc xe lăn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "GERALD HALE — người thấy một vật cản biết nói: mặt đỏ, giọng vang. "
  "ADRIAN — nhắc lại nguyên văn câu vừa nói: mặt hoàn toàn bình, mắt không chớp.",
  "đúng khoảnh khắc ngay TRƯỚC khi GERALD HALE bước một bước về phía chiếc xe lăn",
  ["ADRIAN_TIEC", "GERALD HALE"], "cuối nhà thờ bên phải, cạnh chỗ MAYA quỳ",
  {"ADRIAN": "ngồi xe lăn tay cũ nửa phải khung", "GERALD HALE": "đứng nửa trái khung"},
  "cách nhau hai bước", {"ADRIAN": "hai tay đặt trên vành bánh xe",
                         "GERALD HALE": "một tay chỉ xuống chiếc xe lăn"})
V("16", [32, 33], "trung 50mm hạ thấp · GERALD HALE NÉT trái đứng phía trên + ADRIAN NÉT phải ngồi xe lăn tay cũ",
  [("GERALD HALE", "GERALD HALE"), ("ADRIAN", "ADRIAN_TIEC")],
  "GERALD HALE và ADRIAN, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GERALD HALE chỉ xuống chiếc xe lăn, ADRIAN nhắc lại nguyên văn câu của mình",
  [("GERALD HALE", "loud, contemptuous", 32), ("ADRIAN", "flat, repeating", 33)])

S("17", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m6, máy hạ thấp, lấy ADRIAN nét và GERALD phía trên",
  "ADRIAN ngồi trong chiếc xe lăn tay cũ chiếm phần lớn khung ở nửa PHẢI. GERALD HALE đứng ở nửa TRÁI khung "
  "cao hơn hẳn, đã bước tới sát. Hậu cảnh là cột đá và đèn máy quay truyền hình.",
  "ADRIAN hai tay đặt trên vành bánh xe, các ngón khép. GERALD HALE một tay đặt lên tay vịn chiếc xe lăn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "GERALD HALE — người sắp làm một việc mà bốn trăm người sẽ nhìn thấy: quai hàm siết, mắt tối. "
  "ADRIAN — không lùi nửa phân: mặt hoàn toàn bình, mắt tĩnh, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi mũi giày GERALD HALE chạm vào khung chiếc xe lăn",
  ["ADRIAN_TIEC", "GERALD HALE"], "cuối nhà thờ bên phải, cạnh chỗ MAYA quỳ",
  {"ADRIAN": "ngồi xe lăn tay cũ nửa phải khung", "GERALD HALE": "đứng sát nửa trái khung"},
  "sát nhau", {"ADRIAN": "hai tay đặt trên vành bánh xe",
               "GERALD HALE": "một tay đặt lên tay vịn chiếc xe lăn"})
V("17", [34, 35], "cận-trung 85mm hạ thấp · GERALD HALE NÉT trái đứng sát + ADRIAN NÉT phải ngồi xe lăn tay cũ",
  [("GERALD HALE", "GERALD HALE"), ("ADRIAN", "ADRIAN_TIEC")],
  "GERALD HALE và ADRIAN, cả hai rõ mặt. Khách dự tiệc mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GERALD HALE đặt một tay lên tay vịn chiếc xe lăn, ADRIAN không lùi",
  [("GERALD HALE", "loud, contemptuous", 34), ("ADRIAN", "level, unmoved", 35)],
  ketclip="Cuối clip, GERALD HALE đá vào khung chiếc xe lăn làm nó đổ nghiêng, ADRIAN ngã ra khỏi ghế xuống "
          "nền đá cẩm thạch. Clip dừng đúng lúc vai anh chạm nền.")

S("18", "trung 50mm, cao 0m70, cách ADRIAN 2m2, máy hạ rất thấp ngang mặt nền đá cẩm thạch",
  "ADRIAN nằm nghiêng trên nền đá cẩm thạch ở nửa PHẢI khung, chiếc xe lăn tay cũ đổ nghiêng cạnh anh. "
  "GERALD HALE đứng ở nửa TRÁI khung phía trên. GUEST TWO đứng ở rìa trái khung phía sau, thấy rõ mặt, "
  "một tay đưa lên miệng.",
  "ADRIAN một tay chống xuống nền đá. GERALD HALE hai tay buông dọc thân. GUEST TWO một tay đưa lên miệng.",
  "ADRIAN nhìn thẳng lên GERALD HALE. GERALD HALE nhìn xuống ADRIAN. GUEST TWO nhìn xuống ADRIAN.",
  "ADRIAN — không kêu, không giãy: mặt hoàn toàn bình, mắt tĩnh. "
  "GERALD HALE — vừa nhận ra cả phòng đang nhìn: mặt cứng lại. GUEST TWO — thốt lên: mắt mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng máy ảnh chụp từ phía lối đi",
  ["ADRIAN_TIEC", "GERALD HALE", "GUEST2_DAHOI"], "cuối nhà thờ bên phải, nền đá cẩm thạch",
  {"ADRIAN": "nằm nghiêng trên nền đá nửa phải khung", "GERALD HALE": "đứng phía trên nửa trái khung",
   "GUEST TWO": "đứng rìa trái khung phía sau"},
  "ba người trong vòng hai mét",
  {"ADRIAN": "một tay chống xuống nền đá", "GERALD HALE": "hai tay buông dọc thân",
   "GUEST TWO": "một tay đưa lên miệng"})
V("18", [36, 37], "trung 50mm hạ rất thấp · ADRIAN NÉT phải nằm nghiêng trên nền đá + GERALD HALE NÉT trái đứng phía trên + GUEST TWO NÉT rìa trái phía sau",
  [("ADRIAN", "ADRIAN_TIEC"), ("GERALD HALE", "GERALD HALE"), ("GUEST TWO", "GUEST2_DAHOI")],
  "ADRIAN, GERALD HALE và GUEST TWO, cả ba rõ mặt. ADRIAN NẰM NGHIÊNG trên nền đá cẩm thạch, chiếc xe lăn "
  "đổ cạnh anh. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "chiếc xe lăn đã đổ, ADRIAN chống một tay xuống nền đá và nhìn thẳng lên",
  [("GERALD HALE", "loud, taunting", 36), ("GUEST TWO", "shocked, hushed", 37)])

S("19", "trung 50mm, cao 0m80, cách JULIAN 2m2, máy hạ rất thấp nhìn từ nền lên hai người đứng",
  "JULIAN đứng ở nửa TRÁI khung, một tay chỉ xuống. VANESSA đứng ở nửa PHẢI khung trong váy cưới. "
  "Ở rìa DƯỚI khung thấy vai ADRIAN đang nằm và một phần khung chiếc xe lăn đổ, out nét.",
  "JULIAN một tay chỉ xuống phía ADRIAN, tay kia cầm ly. VANESSA hai tay đan trước bụng.",
  "Cả hai nhìn xuống phía ADRIAN ở rìa dưới khung.",
  "JULIAN — người kêu gọi chụp ảnh chính người anh em họ của mình: khoé môi kéo rộng, giọng vang. "
  "VANESSA — nói câu cuối cùng của mình trước khi mọi thứ đổi chiều: khoé môi cong, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng một người phụ nữ gọi lên từ phía dưới nền",
  ["JULIAN_TUX", "VANESSA_CODAU", "ADRIAN_TIEC"], "cuối nhà thờ bên phải, nền đá cẩm thạch",
  {"JULIAN": "đứng nửa trái khung", "VANESSA": "đứng nửa phải khung",
   "ADRIAN": "vai và một phần khung xe lăn đổ ở rìa dưới khung"},
  "hai người đứng phía trên",
  {"JULIAN": "một tay chỉ xuống, tay kia cầm ly", "VANESSA": "hai tay đan trước bụng",
   "ADRIAN": "nằm nghiêng dưới nền, ngoài vùng nét"})
V("19", [38, 39], "trung 50mm hạ rất thấp · JULIAN NÉT trái chỉ xuống + VANESSA NÉT phải · vai ADRIAN và khung xe lăn đổ rìa dưới out nét",
  [("JULIAN", "JULIAN_TUX"), ("VANESSA", "VANESSA_CODAU"), ("ADRIAN", "ADRIAN_TIEC")],
  "JULIAN và VANESSA rõ mặt. ADRIAN chỉ thấy VAI và một phần khung chiếc xe lăn đổ ở rìa dưới khung, out nét.",
  "JULIAN chỉ xuống phía ADRIAN và gọi người chụp ảnh",
  [("JULIAN", "loud, gloating", 38), ("VANESSA", "light, cruel", 39)])

S("20", "cận-trung 85mm, cao 0m60, cách MAYA 1m6, máy sát mặt nền đá lấy cả hai người",
  "MAYA quỳ ở nửa PHẢI khung, đã chống hai tay xuống nền đá định lao tới. ADRIAN nằm nghiêng chống trên một "
  "khuỷu tay ở nửa TRÁI khung, cách cô hai mét. Hậu cảnh là chân người đứng vòng quanh, mờ.",
  "MAYA hai tay chống xuống nền đá, bàn tay phải có nẹp. ADRIAN một tay chống nền, tay kia giơ lên "
  "ra hiệu cho cô dừng lại.",
  "Hai người nhìn thẳng vào mắt nhau qua khoảng nền đá.",
  "MAYA — người chỉ muốn tới chỗ chồng mình: mắt ướt, giọng gấp. "
  "ADRIAN — ra lệnh cho cô đứng yên bằng ba chữ, và trong mắt anh có thứ mà cô chưa từng thấy: mặt bình, "
  "mắt sáng lên, giọng rất rõ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN đặt lòng bàn tay xuống nền đá để chống người lên",
  ["MAYA_TRANG", "ADRIAN_TIEC"], "cuối nhà thờ bên phải, nền đá cẩm thạch",
  {"MAYA": "quỳ nửa phải khung", "ADRIAN": "nằm nghiêng chống khuỷu tay nửa trái khung"},
  "cách nhau hai mét", {"MAYA": "hai tay chống xuống nền đá, tay phải có nẹp",
                        "ADRIAN": "một tay chống nền, tay kia giơ lên ra hiệu dừng"})
V("20", [40, 41, 42, 43], "cận-trung 85mm sát mặt nền · MAYA NÉT phải quỳ + ADRIAN NÉT trái nằm chống khuỷu tay",
  [("MAYA", "MAYA_TRANG"), ("ADRIAN", "ADRIAN_TIEC")],
  "MAYA và ADRIAN, cả hai rõ mặt trên nền đá cẩm thạch. Khách vây quanh chỉ thấy chân, mờ, "
  "không ai nhìn vào camera.",
  "MAYA chống hai tay xuống nền định lao tới, ADRIAN giơ một tay lên ra hiệu cho cô đứng yên",
  [("MAYA", "urgent, tearful", 40), ("ADRIAN", "firm, quiet", 41),
   ("MAYA", "small, confused", 42), ("ADRIAN", "steady, resolved", 43)])
