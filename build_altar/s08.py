# -*- coding: utf-8 -*-
"""SCENE 8 — PHÒNG ĂN DINH THỰ KANE (đêm). Bữa tối mười chín người."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S8", "REF_PHONGAN_DEM", qc=qc.S8, qcv=qc.S8V)

KHACH = ""

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 9m, đặt ở đầu phòng phía cửa vòm nhìn dọc bàn ăn",
  "Bàn ăn dài kín người, mọi ghế đều có người ngồi. MAYA vừa đẩy chiếc xe lăn có ADRIAN ngồi qua cửa vòm và "
  "dừng lại ở đầu phòng. JULIAN đứng ở đầu bàn phía trong, tay cầm ly, đã quay lại nhìn về phía họ. "
  "Sát tường phải cạnh cửa bếp là một BÀN VUÔNG NHỎ kê riêng với đúng một chiếc ghế.",
  "MAYA hai tay đặt trên tay đẩy xe lăn. ADRIAN hai tay đặt trên vành tay vịn. JULIAN một tay cầm ly rượu vang.",
  "MAYA nhìn dọc bàn ăn. ADRIAN nhìn thẳng về phía JULIAN. JULIAN nhìn về phía hai người. "
  "Khách nền không nhìn vào ống kính.",
  "MAYA — người vừa bước vào một căn phòng mà mọi người trong đó đã bàn về mình từ trước: cằm ngang, mắt quét. "
  "ADRIAN — về lại ngôi nhà đã đẩy mình đi: mặt bình. JULIAN — chủ nhà đang chờ đúng khoảnh khắc này: khoé môi kéo lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả bàn ăn im tiếng",
  ["MAYA_DEN", "ADRIAN_TUTE", "JULIAN"], "đầu phòng ăn phía cửa vòm",
  {"MAYA": "đứng sau xe lăn ở đầu phòng", "ADRIAN": "ngồi xe lăn trước MAYA",
   "JULIAN": "đứng ở đầu bàn phía trong"},
  "MAYA sát sau ADRIAN, JULIAN cách mười mét",
  {"MAYA": "hai tay trên tay đẩy xe lăn", "ADRIAN": "hai tay trên vành tay vịn",
   "JULIAN": "một tay cầm ly rượu vang"})
B("B1", "Mở cảnh. Bữa tối gia tộc Kane. MAYA đẩy ADRIAN qua cửa vòm vào phòng ăn kín người; cạnh cửa bếp có một bàn nhỏ kê riêng.",
  "toàn cảnh 24mm · MAYA NÉT đẩy xe lăn ở đầu phòng + ADRIAN NÉT ngồi trong xe + JULIAN NÉT ở đầu bàn · khách hai bên mờ",
  [("MAYA", "MAYA_DEN"), ("ADRIAN", "ADRIAN_TUTE"), ("JULIAN", "JULIAN")],
  "MAYA, ADRIAN và JULIAN rõ mặt. Các thành viên gia tộc dọc bàn ăn mờ nhẹ, không ai nhìn vào camera.",
  "một căn phòng đầy người thân, một bàn ăn hai mươi chỗ, và một cái bàn con kê riêng cạnh cửa bếp mà ai cũng "
  "biết là dành cho ai.",
  "tiếng nói chuyện dọc bàn tắt dần khi hai người vào; vài cái đầu quay lại; JULIAN nâng ly lên ngang ngực; "
  "MAYA đưa mắt từ bàn dài sang chiếc bàn con cạnh cửa bếp và dừng lại ở đó.",
  "Ambient tiếng dao dĩa và tiếng trò chuyện dạ tiệc tắt dần, SFX tiếng bánh xe lăn trên sàn đá cẩm thạch.",
  nhac("KÌM", "Cả phòng sắp làm nhục hai người này bằng phép lịch sự; nhạc phải sang trọng và lạnh, tuyệt đối không được gằn.",
       "Chamber soul at 68 BPM; a muted upright bass walking under a Rhodes playing sparse chords, a female alto "
       "entering once with a single low line; brushed drums very quiet; the pull is when everything stops for a beat "
       "on the wide shot; lyrics about walking into a room that has already decided about you; warm analog mix, "
       "female vocal, soul, restrained, cold",
       "Chamber instrumental at 66 BPM; a string quartet playing a polite, almost decorative figure that turns "
       "slightly sour in the third bar, an upright bass underneath, no percussion, ending on an unresolved chord; "
       "elegant and cold, strings, upright bass, chamber, unresolved"),
  dur=8)

# ── BÀN ĂN ──
S("01", "trung 50mm, cao 1m50, cách JULIAN 2m6, đặt bên bàn ăn lấy JULIAN nét và AUNT MARGARET cùng khung",
  "JULIAN đứng ở nửa TRÁI khung ở đầu bàn, tay cầm ly. AUNT MARGARET ngồi ở nửa PHẢI khung tại chỗ của bà bên bàn, "
  "đã quay người về phía cửa vòm. " + KHACH,
  "JULIAN một tay cầm ly rượu vang, tay kia gõ nhẹ vào thành ly. AUNT MARGARET hai tay đặt trên mép bàn, "
  "một tay còn cầm khăn ăn.",
  "JULIAN nhìn về phía cửa vòm ngoài khung. AUNT MARGARET cũng nhìn về phía đó rồi quay sang JULIAN.",
  "JULIAN — chủ toạ đang giới thiệu một màn diễn: giọng vang, khoé môi kéo lên. "
  "AUNT MARGARET — nhận ra người trong ảnh báo và thấy khó xử: mày chau, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN chỉ tay về phía chiếc bàn con cạnh cửa bếp",
  ["JULIAN", "AUNT MARGARET"], "đầu bàn ăn phía trong",
  {"JULIAN": "đứng đầu bàn nửa trái khung", "AUNT MARGARET": "ngồi bên bàn nửa phải khung"},
  "cách nhau hai ghế", {"JULIAN": "một tay cầm ly, tay kia gõ nhẹ thành ly",
                        "AUNT MARGARET": "hai tay trên mép bàn, một tay cầm khăn ăn"})
V("01", [0, 1], "trung 50mm · JULIAN NÉT trái đứng đầu bàn + AUNT MARGARET NÉT phải ngồi bên bàn · khách nền mờ",
  [("JULIAN", "JULIAN"), ("AUNT MARGARET", "AUNT MARGARET")],
  "JULIAN và AUNT MARGARET, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN gõ nhẹ vào thành ly cho cả bàn im, AUNT MARGARET quay người về phía cửa vòm",
  [("JULIAN", "loud, hosting", 0), ("AUNT MARGARET", "low, uneasy", 1)])

S("02", "trung 50mm, cao 1m40, cách ADRIAN 2m4, đặt bên bàn ăn, hạ thấp để lấy cả người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, MAYA đứng ngay sau anh, thấy rõ mặt. JULIAN đứng ở nửa TRÁI khung, "
  "một tay chỉ về phía CHIẾC BÀN VUÔNG NHỎ kê riêng cạnh cửa bếp ở rìa phải khung. " + KHACH,
  "JULIAN một tay chỉ về phía chiếc bàn nhỏ, tay kia cầm ly. ADRIAN hai tay đặt trên vành tay vịn. "
  "MAYA hai tay còn trên tay đẩy xe lăn.",
  "JULIAN nhìn ADRIAN. ADRIAN nhìn theo hướng tay chỉ về phía chiếc bàn nhỏ. MAYA nhìn chiếc bàn nhỏ.",
  "JULIAN — người sắp xếp chỗ ngồi cho một người bằng giọng chu đáo: khoé môi kéo lên, mắt sáng. "
  "ADRIAN — nhắc lại ba chữ về vị trí của mình: mặt bình, giọng đều. MAYA — quai hàm siết một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay đầu nhìn JULIAN",
  ["ADRIAN_TUTE", "MAYA_DEN", "JULIAN"], "đầu phòng ăn, gần cửa bếp",
  {"ADRIAN": "ngồi xe lăn nửa phải khung", "MAYA": "đứng sau xe lăn", "JULIAN": "đứng nửa trái khung"},
  "JULIAN cách hai bước", {"JULIAN": "một tay chỉ về chiếc bàn nhỏ, tay kia cầm ly",
                           "ADRIAN": "hai tay trên vành tay vịn", "MAYA": "hai tay trên tay đẩy xe lăn"})
V("02", [2, 3], "trung 50mm hạ thấp · JULIAN NÉT trái chỉ về bàn nhỏ + ADRIAN NÉT phải ngồi xe lăn + MAYA NÉT đứng sau anh",
  [("JULIAN", "JULIAN"), ("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_DEN")],
  "JULIAN, ADRIAN và MAYA, cả ba rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN chỉ tay về phía chiếc bàn vuông nhỏ kê riêng cạnh cửa bếp",
  [("JULIAN", "warm, hosting", 2), ("ADRIAN", "flat, even", 3)])

S("03", "cận-trung 85mm, cao 1m50, cách JULIAN 1m8, đặt bên bàn ăn lấy JULIAN nét và AUNT MARGARET trong khung",
  "JULIAN đứng ở nửa TRÁI khung, đã đặt ly xuống mặt bàn. AUNT MARGARET ngồi ở nửa PHẢI khung, người quay hẳn "
  "về phía ông. " + KHACH,
  "JULIAN hai tay mở ra hai bên rồi khép lại, kiểu người đang giải thích một chuyện hiển nhiên. "
  "AUNT MARGARET một tay đặt lên cánh tay JULIAN rồi rút về.",
  "JULIAN nhìn quanh bàn ăn khi nói. AUNT MARGARET nhìn thẳng vào mặt JULIAN.",
  "JULIAN — người biến sự tàn nhẫn thành một quyết định hậu cần: giọng nhẹ, tay khoát, mắt sáng. "
  "AUNT MARGARET — can một câu rồi tự thấy mình yếu: giọng nhỏ, mắt dời đi.",
  "đúng khoảnh khắc ngay TRƯỚC khi chủ nhà quay sang phía cửa vòm",
  ["JULIAN", "AUNT MARGARET"], "đầu bàn ăn phía trong",
  {"JULIAN": "đứng đầu bàn nửa trái khung", "AUNT MARGARET": "ngồi bên bàn nửa phải khung"},
  "cách nhau một ghế", {"JULIAN": "hai tay mở ra rồi khép lại",
                        "AUNT MARGARET": "một tay đặt lên cánh tay JULIAN rồi rút về"})
V("03", [4, 5], "cận-trung 85mm · JULIAN NÉT trái + AUNT MARGARET NÉT phải ngồi bên bàn · khách nền mờ",
  [("JULIAN", "JULIAN"), ("AUNT MARGARET", "AUNT MARGARET")],
  "JULIAN và AUNT MARGARET, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN khoát tay giải thích với cả bàn, AUNT MARGARET đặt tay lên cánh tay ông rồi rút về",
  [("JULIAN", "light, reasonable", 4), ("AUNT MARGARET", "small, chiding", 5)])

S("04", "trung 50mm, cao 1m50, cách JULIAN 2m4, đặt bên bàn ăn lấy JULIAN nét và MAYA cùng khung",
  "JULIAN đứng ở nửa TRÁI khung, một tay chìa ra về phía MAYA như đang giới thiệu. MAYA đứng ở nửa PHẢI khung "
  "cạnh chiếc xe lăn, thấy rõ mặt. " + KHACH,
  "JULIAN một tay chìa ngửa về phía MAYA, tay kia đút túi quần. MAYA hai tay buông xuống hai bên.",
  "JULIAN nhìn quanh bàn ăn rồi nhìn MAYA. MAYA nhìn thẳng vào JULIAN.",
  "JULIAN — người đang giới thiệu một người như giới thiệu một món lạ: giọng vang, khoé môi kéo lên. "
  "MAYA — bị đem ra làm trò trước mười chín người và không cụp mắt: cằm ngang, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng cười khẽ chạy dọc bàn ăn",
  ["JULIAN", "MAYA_DEN"], "đầu phòng ăn, cạnh bàn dài",
  {"JULIAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung cạnh xe lăn"},
  "cách nhau hai bước", {"JULIAN": "một tay chìa ngửa về phía MAYA, tay kia đút túi",
                         "MAYA": "hai tay buông xuống hai bên"})
V("04", [6], "trung 50mm · JULIAN NÉT trái chìa tay giới thiệu + MAYA NÉT phải đứng cạnh xe lăn · khách nền mờ",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_DEN")],
  "JULIAN và MAYA, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN chìa tay về phía MAYA và giới thiệu cô với cả bàn ăn",
  [("JULIAN", "loud, performative", 6)], [("MAYA", "silent, holding his gaze")])

S("05", "trung 50mm, cao 1m50, cách MAYA 2m2, đặt bên bàn ăn lấy MAYA nét và UNCLE PETER cùng khung",
  "MAYA đứng ở nửa PHẢI khung. UNCLE PETER ngồi ở nửa TRÁI khung tại chỗ của ông bên bàn ăn, người ngả ra sau ghế, "
  "một tay cầm ly. " + KHACH,
  "UNCLE PETER một tay cầm ly rượu vang xoay nhẹ, tay kia đặt trên bụng. MAYA hai tay buông xuống hai bên.",
  "UNCLE PETER nhìn thẳng vào MAYA. MAYA nhìn lại ông.",
  "UNCLE PETER — người hỏi câu tục nhất bằng giọng vui vẻ nhất: khoé môi kéo ngang, mắt nheo. "
  "MAYA — trả lời tới hàng đơn vị, không né: giọng đều, mắt không chớp.",
  "đúng khoảnh khắc ngay TRƯỚC khi dao dĩa dọc bàn ngừng hẳn",
  ["MAYA_DEN", "UNCLE PETER"], "cạnh bàn ăn dài, phía đầu phòng",
  {"MAYA": "đứng nửa phải khung", "UNCLE PETER": "ngồi bên bàn nửa trái khung"},
  "cách nhau hai bước", {"UNCLE PETER": "một tay cầm ly xoay nhẹ, tay kia đặt trên bụng",
                         "MAYA": "hai tay buông xuống hai bên"})
V("05", [7, 8], "trung 50mm · UNCLE PETER NÉT trái ngồi bên bàn + MAYA NÉT phải đứng · khách nền mờ",
  [("UNCLE PETER", "UNCLE PETER"), ("MAYA", "MAYA_DEN")],
  "UNCLE PETER và MAYA, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "UNCLE PETER xoay ly rượu và hỏi thẳng, MAYA trả lời ngay không nghĩ",
  [("UNCLE PETER", "amused, blunt", 7), ("MAYA", "level, exact", 8)])

S("06", "cận-trung 85mm, cao 1m50, cách MAYA 1m7, máy sau vai PHẢI của UNCLE PETER; vai và gáy ông chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. UNCLE PETER chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng MAYA là cửa vòm ra đại sảnh và một phần bàn ăn có khách ngồi mờ.",
  "MAYA một tay đưa lên chỉ về phía chiếc xe lăn ngoài khung rồi hạ xuống.",
  "MAYA nhìn thẳng vào mặt UNCLE PETER qua vai ông.",
  "MAYA — người vừa biến câu hỏi làm nhục thành một câu trả lời hành chính và hỏi ngược lại: giọng bình, "
  "mắt thẳng, không hề gay gắt.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng người cất lên từ đầu bàn",
  ["MAYA_DEN", "UNCLE PETER"], "cạnh bàn ăn dài, phía đầu phòng",
  {"MAYA": "đứng chính diện giữa khung", "UNCLE PETER": "vai và gáy tiền cảnh trái"},
  "cách nhau hai bước", {"MAYA": "một tay chỉ về phía chiếc xe lăn rồi hạ xuống",
                         "UNCLE PETER": "một tay cầm ly, ngoài vùng nét"})
V("06", [9, 10], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy UNCLE PETER tiền cảnh trái out nét",
  [("MAYA", "MAYA_DEN"), ("UNCLE PETER", "UNCLE PETER")],
  "MAYA rõ mặt chính diện. UNCLE PETER chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "UNCLE PETER thốt lên một câu với người bên cạnh, MAYA chỉ về phía chiếc xe lăn rồi hạ tay xuống",
  [("UNCLE PETER", "surprised, amused", 9), ("MAYA", "even, unbothered", 10)])

S("07", "trung 50mm, cao 1m50, cách JULIAN 2m4, đặt bên bàn ăn lấy JULIAN nét và MAYA cùng khung",
  "JULIAN đứng ở nửa TRÁI khung ở đầu bàn, một tay đặt lên lưng CHIẾC GHẾ CHỦ TOẠ. MAYA đứng ở nửa PHẢI khung, "
  "đã bước tới gần bàn dài hơn một bước. " + KHACH,
  "JULIAN một tay đặt lên lưng ghế chủ toạ, tay kia chỉ về phía chiếc bàn nhỏ cạnh cửa bếp. "
  "MAYA một tay đặt lên lưng một chiếc ghế bên bàn dài.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JULIAN — người vừa nghe một chữ NO trong ngôi nhà của mình: mày nhướn, khoé môi cứng lại. "
  "MAYA — nói một chữ và giữ nguyên nét mặt: mắt thẳng, cằm ngang.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA kéo chiếc ghế đầu tiên ra khỏi bàn",
  ["JULIAN", "MAYA_DEN"], "đầu bàn ăn phía trong",
  {"JULIAN": "đứng đầu bàn nửa trái khung", "MAYA": "đứng nửa phải khung cạnh bàn dài"},
  "cách nhau ba bước", {"JULIAN": "một tay trên lưng ghế chủ toạ, tay kia chỉ về bàn nhỏ",
                        "MAYA": "một tay đặt lên lưng một chiếc ghế"})
V("07", [11, 12, 13], "trung 50mm · JULIAN NÉT trái ở đầu bàn + MAYA NÉT phải cạnh bàn dài · khách nền mờ",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_DEN")],
  "JULIAN và MAYA, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN chỉ về phía chiếc bàn nhỏ, MAYA đặt tay lên lưng một chiếc ghế bên bàn dài",
  [("JULIAN", "smooth, amused", 11), ("MAYA", "flat, final", 12), ("JULIAN", "clipped, thrown", 13)])

S("08", "trung 50mm, cao 1m50, cách MAYA 2m2, đặt dọc bàn ăn lấy MAYA nét và JULIAN phía sau",
  "MAYA đứng ở giữa khung bên cạnh bàn ăn dài, hai tay đặt lên lưng hai chiếc ghế cạnh nhau. JULIAN đứng ở nửa "
  "TRÁI khung phía sau, cạnh ghế chủ toạ. " + KHACH,
  "MAYA hai tay đặt lên lưng hai chiếc ghế cạnh nhau, chưa kéo ra. JULIAN một tay còn trên lưng ghế chủ toạ.",
  "MAYA nhìn dọc bàn ăn tìm chỗ trống. JULIAN nhìn theo tay MAYA.",
  "MAYA — người đang dọn chỗ giữa một bàn tiệc mà không xin phép ai: giọng lịch sự, tay dứt khoát. "
  "JULIAN — chưa kịp phản ứng: mày nhướn, miệng hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai chiếc ghế bị kéo lệch ra khỏi bàn",
  ["MAYA_DEN", "JULIAN"], "dọc bàn ăn dài, gần đầu bàn chủ toạ",
  {"MAYA": "đứng giữa khung cạnh bàn dài", "JULIAN": "đứng nửa trái khung phía sau, cạnh ghế chủ toạ"},
  "cách nhau ba bước", {"MAYA": "hai tay đặt lên lưng hai chiếc ghế",
                        "JULIAN": "một tay trên lưng ghế chủ toạ"})
V("08", [14], "trung 50mm · MAYA NÉT giữa cạnh bàn dài + JULIAN NÉT trái phía sau · khách nền mờ",
  [("MAYA", "MAYA_DEN"), ("JULIAN", "JULIAN")],
  "MAYA và JULIAN, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "MAYA đặt tay lên lưng hai chiếc ghế và nói với những người đang ngồi",
  [("MAYA", "polite, decisive", 14)], [("JULIAN", "silent, caught off guard")],
  ketclip="Cuối clip, MAYA kéo hai chiếc ghế lệch ra hai bên, tạo một khoảng trống ở đầu bàn, rồi đẩy chiếc xe lăn "
          "vào đúng chỗ đó. Clip dừng đúng lúc bánh xe lăn dừng lại ở đầu bàn.")

S("09", "cận-trung 85mm, cao 1m50, cách JULIAN 1m7, máy sau vai TRÁI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "JULIAN đứng chính diện chiếm phần lớn khung, cạnh chiếc ghế chủ toạ lưng cao. MAYA chỉ còn là vai và gáy ở rìa "
  "PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng JULIAN là lò sưởi đá trắng và bức tranh sơn dầu khung vàng.",
  "JULIAN một tay nắm lấy lưng ghế chủ toạ, các khớp ngón hơi trắng.",
  "JULIAN nhìn thẳng vào mặt MAYA qua vai cô.",
  "JULIAN — người vừa bị lấy mất cái ghế của mình trước mặt cả họ: khoé môi cứng, giọng vẫn êm, mắt lạnh đi.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN buông tay khỏi lưng ghế",
  ["JULIAN", "MAYA_DEN"], "đầu bàn ăn, cạnh ghế chủ toạ",
  {"JULIAN": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau hai bước", {"JULIAN": "một tay nắm lưng ghế chủ toạ",
                         "MAYA": "một tay trên tay đẩy xe lăn, ngoài vùng nét"})
V("09", [15, 16], "OTS cận-trung 85mm · JULIAN NÉT chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_DEN")],
  "JULIAN rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "JULIAN nắm chặt lưng chiếc ghế chủ toạ, MAYA đáp lại bằng một câu ngắn",
  [("JULIAN", "smooth, warning", 15), ("MAYA", "flat, precise", 16)])

S("10", "trung 50mm, cao 1m40, cách MAYA 2m2, đặt bên đầu bàn, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung ngay cạnh chiếc xe lăn đã vào chỗ ở đầu bàn, một tay cầm dao ăn. ADRIAN ngồi trong "
  "xe lăn ở giữa khung, trước mặt anh là một đĩa sứ trắng. JULIAN đứng ở nửa TRÁI khung. " + KHACH,
  "MAYA một tay cầm dao ăn, tay kia giữ mép đĩa trước mặt ADRIAN. ADRIAN hai tay đặt trên mặt bàn. "
  "JULIAN hai tay buông xuống hai bên.",
  "MAYA nhìn JULIAN khi nói rồi nhìn xuống đĩa. ADRIAN nhìn MAYA. JULIAN nhìn MAYA.",
  "MAYA — người vừa gọi đúng tên việc mà cả bàn này đã làm suốt sáu tháng: giọng bình, tay không run. "
  "ADRIAN — bị chăm sóc công khai trước mặt cả họ: mắt hơi động. JULIAN — mặt cứng lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi lưỡi dao chạm xuống miếng thịt trong đĩa",
  ["MAYA_DEN", "ADRIAN_TUTE", "JULIAN"], "đầu bàn ăn, chỗ chiếc xe lăn vừa vào",
  {"MAYA": "đứng nửa phải khung cạnh xe lăn", "ADRIAN": "ngồi xe lăn giữa khung trước đĩa ăn",
   "JULIAN": "đứng nửa trái khung"},
  "MAYA sát cạnh ADRIAN, JULIAN cách hai bước",
  {"MAYA": "một tay cầm dao ăn, tay kia giữ mép đĩa", "ADRIAN": "hai tay đặt trên mặt bàn",
   "JULIAN": "hai tay buông xuống hai bên"})
V("10", [17, 18], "trung 50mm hạ thấp · MAYA NÉT phải cầm dao ăn + ADRIAN NÉT giữa ngồi xe lăn + JULIAN NÉT trái",
  [("MAYA", "MAYA_DEN"), ("ADRIAN", "ADRIAN_TUTE"), ("JULIAN", "JULIAN")],
  "MAYA, ADRIAN và JULIAN, cả ba rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN hỏi, MAYA cầm dao ăn lên và giữ mép đĩa trước mặt ADRIAN",
  [("JULIAN", "low, threatening but polite", 17), ("MAYA", "even, unimpressed", 18)])

S("11", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m5, đặt bên đầu bàn, hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung trước chiếc đĩa sứ trắng. MAYA đứng ở nửa PHẢI khung, hơi cúi xuống, "
  "một tay cầm dao ăn dừng trên đĩa. Hậu cảnh là mép bàn dài và các thành viên gia tộc mờ.",
  "MAYA một tay cầm dao ăn dừng lơ lửng trên đĩa, tay kia cầm dĩa. ADRIAN một tay đặt trên mặt bàn cạnh đĩa.",
  "ADRIAN ngước lên nhìn MAYA. MAYA nhìn xuống ADRIAN.",
  "ADRIAN — người đang muốn cô dừng lại vì thấy ngượng thay cho cả hai: mày chau, giọng rất khẽ. "
  "MAYA — không dừng, chỉ hỏi lại đúng câu hỏi kỹ thuật: mắt thẳng, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN trả lời cô",
  ["ADRIAN_TUTE", "MAYA_DEN"], "đầu bàn ăn, chỗ chiếc xe lăn",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "MAYA": "đứng cúi xuống nửa phải khung"},
  "sát cạnh nhau", {"MAYA": "một tay cầm dao ăn dừng trên đĩa, tay kia cầm dĩa",
                    "ADRIAN": "một tay đặt trên mặt bàn cạnh đĩa"})
V("11", [19, 20, 21], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải cúi xuống cầm dao ăn",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_DEN")],
  "ADRIAN và MAYA, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "ADRIAN gọi khẽ tên cô để cô dừng lại, MAYA không dừng và hỏi lại",
  [("ADRIAN", "quiet, embarrassed", 19), ("MAYA", "even, insistent", 20), ("ADRIAN", "quiet, giving in", 21)])

S("12", "trung 50mm, cao 1m50, cách MAYA 2m4, đặt ở đầu bàn nhìn dọc theo bàn ăn dài",
  "MAYA đứng ở nửa PHẢI khung cạnh chiếc xe lăn, đã đặt dao dĩa xuống và quay hẳn người ra phía bàn dài. "
  "ADRIAN ngồi trong xe lăn ở rìa phải khung, thấy rõ mặt. Dọc bàn dài phía sau là các thành viên gia tộc ngồi im, "
  "mờ ngoài vùng nét, TUYỆT ĐỐI không nhìn vào ống kính.",
  "MAYA một tay chỉ dọc theo bàn ăn, tay kia đặt lên lưng ghế xe lăn. ADRIAN hai tay đặt trên mặt bàn.",
  "MAYA nhìn dọc bàn ăn, quét qua từng chỗ ngồi. ADRIAN nhìn MAYA.",
  "MAYA — người vừa cắt ngang bữa tối để nói ra một phép đếm rất đơn giản: giọng rõ, đều, mắt không rời bàn ăn. "
  "ADRIAN — nghe người khác nói thay mình lần đầu sau sáu tháng: mắt hơi đỏ, mặt vẫn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng ghế đẩy lùi ở cuối bàn",
  ["MAYA_DEN", "ADRIAN_TUTE"], "đầu bàn ăn, quay ra phía bàn dài",
  {"MAYA": "đứng nửa phải khung quay ra bàn dài", "ADRIAN": "ngồi xe lăn rìa phải khung"},
  "sát cạnh nhau", {"MAYA": "một tay chỉ dọc bàn ăn, tay kia trên lưng ghế xe lăn",
                    "ADRIAN": "hai tay đặt trên mặt bàn"})
V("12", [22], "trung 50mm · MAYA NÉT phải quay ra bàn dài + ADRIAN NÉT rìa phải ngồi xe lăn · khách dọc bàn mờ",
  [("MAYA", "MAYA_DEN"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt. Các thành viên gia tộc dọc bàn mờ, không ai nhìn vào camera.",
  "MAYA đặt dao dĩa xuống, quay hẳn ra phía bàn dài và chỉ dọc theo bàn",
  [("MAYA", "clear, level", 22)], [("ADRIAN", "silent, eyes reddening")])

S("13", "cận-trung 85mm, cao 1m50, cách AUNT MARGARET 1m7, đặt bên bàn ăn lấy bà nét và MAYA cùng khung",
  "AUNT MARGARET ngồi ở nửa TRÁI khung, đã nghiêng hẳn người ra phía lối đi. MAYA đứng ở nửa PHẢI khung, "
  "quay về phía bà. Hậu cảnh là bàn ăn dài và các thành viên khác mờ.",
  "AUNT MARGARET một tay đặt lên mép bàn, tay kia siết chiếc khăn ăn. MAYA hai tay buông xuống hai bên.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "AUNT MARGARET — người muốn bảo vệ nếp nhà và tự biết mình đang bảo vệ điều gì: giọng nhỏ, mắt né một nhịp. "
  "MAYA — nghe câu đó và không phản ứng ngay: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA trả lời bà",
  ["AUNT MARGARET", "MAYA_DEN"], "cạnh bàn ăn dài, phía đầu bàn",
  {"AUNT MARGARET": "ngồi bên bàn nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau hai bước", {"AUNT MARGARET": "một tay trên mép bàn, tay kia siết khăn ăn",
                         "MAYA": "hai tay buông xuống hai bên"})
V("13", [23], "cận-trung 85mm · AUNT MARGARET NÉT trái ngồi bên bàn + MAYA NÉT phải đứng · khách nền mờ",
  [("AUNT MARGARET", "AUNT MARGARET"), ("MAYA", "MAYA_DEN")],
  "AUNT MARGARET và MAYA, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "AUNT MARGARET nghiêng người ra phía lối đi và nói với MAYA",
  [("AUNT MARGARET", "gentle, chiding", 23)], [("MAYA", "silent, unmoved")])

S("14", "cận 85mm, cao 1m50, cách MAYA 1m3, đặt bên bàn ăn, lấy MAYA nét và một mảng vai AUNT MARGARET rìa trái",
  "MAYA đứng chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai và mái tóc bạc của "
  "AUNT MARGARET đang ngồi, out nét. Hậu cảnh là bàn ăn dài và đèn chùm pha lê xoá phông.",
  "MAYA một tay đưa lên ngang ngực, lòng bàn tay ngửa, rồi hạ xuống chậm.",
  "MAYA nhìn thẳng vào mặt AUNT MARGARET.",
  "MAYA — người đang nói ra thứ luật duy nhất mà sáu năm ở khoa hồi sức dạy cô: giọng chậm, rõ từng chữ, "
  "mắt không rời, KHÔNG to tiếng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng tay đập xuống mặt bàn ở đầu kia",
  ["MAYA_DEN", "AUNT MARGARET"], "cạnh bàn ăn dài, phía đầu bàn",
  {"MAYA": "đứng chính diện giữa khung", "AUNT MARGARET": "một mảng vai và mái tóc bạc ở rìa trái"},
  "cách nhau hai bước", {"MAYA": "một tay đưa lên ngang ngực ngửa rồi hạ xuống",
                         "AUNT MARGARET": "một tay siết khăn ăn, ngoài vùng nét"})
V("14", [24], "cận 85mm · MAYA NÉT chính diện · một mảng vai AUNT MARGARET rìa trái out nét",
  [("MAYA", "MAYA_DEN"), ("AUNT MARGARET", "AUNT MARGARET")],
  "MAYA rõ mặt. AUNT MARGARET chỉ thấy MỘT MẢNG VAI và mái tóc bạc ở rìa trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đưa tay lên ngang ngực rồi hạ xuống rất chậm trong lúc nói",
  [("MAYA", "slow, deliberate", 24)], [("AUNT MARGARET", "silent, looking away")])

S("15", "trung 50mm, cao 1m50, cách JULIAN 2m4, đặt bên bàn ăn lấy JULIAN nét và MAYA cùng khung",
  "JULIAN đứng ở nửa TRÁI khung ở đầu bàn, một tay đã đặt xuống mặt bàn. MAYA đứng ở nửa PHẢI khung cạnh chiếc "
  "xe lăn, một tay đặt lên lưng ghế xe. " + KHACH,
  "JULIAN một tay chống xuống mặt bàn, tay kia chỉ về phía cửa vòm. MAYA một tay đặt lên lưng ghế xe lăn, "
  "tay kia cầm lại chiếc dĩa trên bàn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JULIAN — người vừa hết cách và chuyển sang đuổi thẳng: giọng gằn xuống, mặt cứng. "
  "MAYA — không nhúc nhích và trả lời bằng một câu rất bình: mắt thẳng, tay đã cầm lại chiếc dĩa.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA cắt miếng thịt đầu tiên trong đĩa",
  ["JULIAN", "MAYA_DEN"], "đầu bàn ăn",
  {"JULIAN": "đứng đầu bàn nửa trái khung", "MAYA": "đứng nửa phải khung cạnh xe lăn"},
  "cách nhau ba bước", {"JULIAN": "một tay chống mặt bàn, tay kia chỉ về cửa vòm",
                        "MAYA": "một tay trên lưng ghế xe lăn, tay kia cầm dĩa"})
V("15", [25, 26], "trung 50mm · JULIAN NÉT trái ở đầu bàn + MAYA NÉT phải cạnh xe lăn · khách nền mờ",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_DEN")],
  "JULIAN và MAYA, cả hai rõ mặt. Các thành viên khác dọc bàn mờ, không ai nhìn vào camera.",
  "JULIAN chống tay xuống mặt bàn và chỉ về phía cửa vòm, MAYA cầm lại chiếc dĩa",
  [("JULIAN", "low, dismissing", 25), ("MAYA", "calm, immovable", 26)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 8m, đặt ở đầu phòng phía cửa vòm nhìn dọc bàn ăn",
  "Bàn ăn dài kín người vẫn ngồi nguyên, dao dĩa đã ngừng. Ở đầu bàn, ADRIAN ngồi trong xe lăn đúng chỗ ghế "
  "chủ toạ, đĩa thức ăn đã cắt nhỏ trước mặt. MAYA đứng ngay cạnh anh, tay còn cầm dao dĩa. "
  "JULIAN đứng lùi lại một bước, không còn chỗ ngồi.",
  "MAYA một tay cầm dao, tay kia cầm dĩa. ADRIAN hai tay đặt trên mặt bàn. JULIAN hai tay buông dọc thân.",
  "MAYA nhìn xuống đĩa thức ăn. ADRIAN nhìn thẳng dọc bàn. JULIAN nhìn hai người. "
  "Khách nền TUYỆT ĐỐI không nhìn vào ống kính.",
  "MAYA — người vừa dọn lại chỗ ngồi cho chồng mình giữa mười chín người và không xin phép ai: vai cân, mặt bình. "
  "ADRIAN — ngồi ở đầu bàn lần đầu sau sáu tháng: mặt tĩnh, mắt hơi đỏ. JULIAN — mặt cứng lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người ở cuối bàn đứng dậy bỏ đi",
  ["MAYA_DEN", "ADRIAN_TUTE", "JULIAN"], "đầu bàn ăn dinh thự Kane",
  {"MAYA": "đứng cạnh xe lăn ở đầu bàn", "ADRIAN": "ngồi xe lăn đúng chỗ ghế chủ toạ",
   "JULIAN": "đứng lùi lại một bước"},
  "ba người trong vòng hai mét",
  {"MAYA": "một tay cầm dao, tay kia cầm dĩa", "ADRIAN": "hai tay đặt trên mặt bàn",
   "JULIAN": "hai tay buông dọc thân"})
B("B2", "Khép cảnh. ADRIAN ngồi ở đầu bàn ăn gia tộc, MAYA đứng cạnh cắt thịt, JULIAN mất chỗ ngồi của mình.",
  "toàn cảnh 24mm · ADRIAN NÉT ngồi xe lăn ở đầu bàn + MAYA NÉT đứng cạnh anh + JULIAN NÉT lùi một bước · khách dọc bàn mờ",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_DEN"), ("JULIAN", "JULIAN")],
  "ADRIAN, MAYA và JULIAN rõ mặt. Các thành viên gia tộc dọc bàn mờ, không ai nhìn vào camera.",
  "một người phụ nữ quen bốn ngày vừa làm được thứ mà cả một gia tộc mười chín người không làm trong sáu tháng, "
  "và không ai ở bàn này dám nói gì.",
  "MAYA cắt nốt miếng thịt trong đĩa rồi đặt dao dĩa xuống; một người ở cuối bàn đẩy ghế đứng dậy; "
  "ADRIAN nhìn dọc bàn ăn một lượt; ngọn nến trên bàn cháy nghiêng đi vì luồng gió cửa mở.",
  "Ambient tiếng đèn chùm pha lê rung rất khẽ và tiếng ghế gỗ đẩy lùi, SFX tiếng dao dĩa đặt xuống đĩa sứ.",
  nhac("NÂNG", "Lần đầu tiên trong phim nhân vật chính thắng một trận — nhỏ, trong một phòng ăn, nhưng là mốc chuyển thật.",
       "Cinematic soul at 84 BPM; a muted trumpet carrying the melody over Rhodes and upright bass, brushed drums "
       "entering at the midpoint, a female alto joining for two lines near the end; the pull is when the trumpet "
       "drops out and only voice and Rhodes remain; lyrics about somebody setting a place at a table for a man "
       "everyone had pushed to the wall; warm analog mix, female vocal, trumpet, Rhodes, uplifting but restrained",
       "Cinematic instrumental at 82 BPM; muted trumpet over Rhodes and upright bass, brushed drums entering at the "
       "midpoint, a small string section rising once then pulling back to trumpet alone; "
       "warm analog mix, trumpet, Rhodes, upright bass, strings, uplifting, restrained"),
  dur=8)
