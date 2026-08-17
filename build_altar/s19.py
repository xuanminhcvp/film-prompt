# -*- coding: utf-8 -*-
"""SCENE 19 — HẦM ĐỖ XE TẦNG B2 (đêm). Lời nhắn của gia đình."""
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S19", "REF_HAMXE_DEM")
SB = "SEBASTIAN (off-screen, qua điện thoại)"

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m50, cách MAYA 6m, đặt giữa lối xe chạy nhìn dọc hầm về phía thang máy",
  "MAYA đang đẩy chiếc xe lăn tay cũ có ADRIAN ngồi đi dọc lối xe trong hầm B2. Phía trước bên trái là cửa thang "
  "máy inox có một tờ giấy A4 dán trên cánh. Hầm vắng, vài xe con phủ bụi đỗ hai bên.",
  "MAYA hai tay đẩy chiếc xe cũ, người hơi đổ về trước vì vành bánh trái cong. ADRIAN hai tay đặt trên vành bánh xe.",
  "MAYA nhìn về phía cửa thang máy. ADRIAN nhìn dọc theo hàng cột bê tông bên phải.",
  "MAYA — người đã đi bộ cả ngày và chỉ muốn về tới nhà: mặt mệt, vai chùng. "
  "ADRIAN — đang đếm những thứ không khớp trong hầm xe này: mắt quét, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhìn thấy tờ giấy dán trên cửa thang máy",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "giữa lối xe chạy hầm B2",
  {"MAYA": "đẩy chiếc xe cũ đi dọc lối xe", "ADRIAN": "ngồi trong chiếc xe lăn tay cũ"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay đẩy chiếc xe cũ", "ADRIAN": "hai tay đặt trên vành bánh xe"})
B("B1", "Mở cảnh. Hầm đỗ xe B2 về đêm. MAYA đẩy chiếc xe lăn tay cũ đi dọc lối xe, thang máy phía trước dán giấy.",
  "trung-rộng 35mm · MAYA NÉT đẩy chiếc xe cũ + ADRIAN NÉT ngồi trong xe · không có ai khác trong khung",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN rõ mặt. Không có người nào khác trong khung ở nhịp này.",
  "một hầm xe vắng lúc chập tối, một chiếc xe lăn hỏng vành và hai người đã kiệt sức; ba người đang đứng "
  "chờ giữa hai cột bê tông thì khán giả chưa thấy, nhưng người ngồi trong xe thì đã thấy.",
  "MAYA đẩy xe đi đều, bánh trái cong làm xe lệch nên cô phải ghì lại từng nhịp; một bóng đèn tuýp trên trần "
  "nhấp nháy hai lần; ADRIAN quay đầu nhìn về phía hàng cột bên phải và không quay lại nữa.",
  "Ambient tiếng vọng bê tông của hầm xe và tiếng ù của quạt thông gió, SFX tiếng bánh xe lăn nghiến trên nền bê tông.",
  nhac("KÌM", "Nhạc phải nén và tối để cú tấn công sắp tới không bị báo trước bằng âm nhạc kịch tính.",
       "Minimal soul at 60 BPM; an upright bass walking alone with a very quiet Rhodes chord every four bars, "
       "a female alto entering once with a single low line; no drums; the pull is when the bass stops dead; "
       "lyrics about a long day that is not over yet; dry mix, female vocal, upright bass, Rhodes, restrained, tense",
       "Minimal instrumental at 58 BPM; upright bass walking alone under one sustained low synth note, "
       "a single struck piano key every eight bars, no percussion, stopping abruptly; "
       "cold concrete-room mix, upright bass, piano, minimal, tense"),
  dur=8)

# ── BA NGƯỜI GIỮA HAI CỘT ──
S("01", "trung 50mm, cao 1m30, cách MAYA 2m2, đặt bên chiếc xe, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung sau chiếc xe cũ, đã dừng đẩy. ADRIAN ngồi trong chiếc xe tay cũ ở nửa TRÁI khung, "
  "đã quay đầu lại. Hậu cảnh là cửa thang máy inox và cột bê tông có vành sọc vàng đen.",
  "MAYA hai tay còn trên tay đẩy xe. ADRIAN một tay đưa ra sau chạm vào bàn tay MAYA trên tay đẩy.",
  "MAYA nhìn về phía cửa thang máy. ADRIAN nhìn về phía hàng cột bên phải, không quay lại nhìn cô.",
  "MAYA — chưa thấy gì bất thường: mặt mệt, giọng bình. "
  "ADRIAN — đã đếm đủ bốn phút và biết chính xác chuyện gì sắp xảy ra: giọng rất nhỏ, mắt không rời hàng cột.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay đầu nhìn theo hướng mắt anh",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "giữa lối xe chạy hầm B2, gần cửa thang máy",
  {"MAYA": "đứng sau chiếc xe cũ nửa phải khung", "ADRIAN": "ngồi xe lăn tay cũ nửa trái khung"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay trên tay đẩy xe",
                          "ADRIAN": "một tay đưa ra sau chạm vào bàn tay MAYA"})
V("01", [0, 1, 2], "trung 50mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn tay cũ + MAYA NÉT phải đứng sau xe",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA dừng đẩy, ADRIAN đưa tay ra sau chạm vào bàn tay cô trên tay đẩy",
  [("MAYA", "tired, practical", 0), ("ADRIAN", "very quiet, alert", 1), ("MAYA", "puzzled, low", 2)])

S("02", "trung 50mm, cao 1m30, cách ADRIAN 2m4, đặt chếch bên, lấy hai người tiền cảnh và ba bóng người ở hậu cảnh",
  "ADRIAN ngồi trong chiếc xe tay cũ ở nửa TRÁI khung tiền cảnh, MAYA đứng sau xe ở nửa PHẢI khung. "
  "Ở hậu cảnh giữa hai cột bê tông, THUG ONE đứng thấy rõ mặt, THUG TWO đứng lùi sau anh ta một bước, "
  "cả hai đứng yên nhìn về phía chiếc xe lăn.",
  "ADRIAN hai tay đặt trên vành bánh xe. MAYA một tay còn trên tay đẩy xe. "
  "THUG ONE hai tay đút túi áo bomber. THUG TWO hai tay đút túi hoodie.",
  "ADRIAN nhìn thẳng vào THUG ONE. MAYA nhìn theo hướng đó. Hai người kia nhìn về phía chiếc xe lăn.",
  "ADRIAN — nói ra chính xác điều mình vừa đếm: giọng đều, mặt bình. "
  "MAYA — vừa nhìn thấy ba người đứng giữa hai cột: mắt mở, tay siết lại trên tay đẩy. "
  "THUG ONE và THUG TWO — mặt hoàn toàn trống, không hằn học.",
  "đúng khoảnh khắc ngay TRƯỚC khi THUG ONE bước bước đầu tiên về phía họ",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC", "THUG ONE", "THUG TWO"], "giữa lối xe chạy hầm B2, giữa hai cột bê tông",
  {"ADRIAN": "ngồi xe lăn tay cũ nửa trái khung tiền cảnh", "MAYA": "đứng sau xe nửa phải khung",
   "THUG ONE": "đứng giữa hai cột ở hậu cảnh", "THUG TWO": "đứng lùi sau THUG ONE một bước"},
  "hai bên cách nhau sáu mét",
  {"ADRIAN": "hai tay trên vành bánh xe", "MAYA": "một tay trên tay đẩy xe",
   "THUG ONE": "hai tay đút túi áo bomber", "THUG TWO": "hai tay đút túi hoodie"})
V("02", [3, 4], "trung 50mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải sau xe + THUG ONE NÉT và THUG TWO NÉT ở hậu cảnh giữa hai cột",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC"),
   ("THUG ONE", "THUG ONE"), ("THUG TWO", "THUG TWO")],
  "ADRIAN và MAYA rõ mặt ở tiền cảnh; THUG ONE và THUG TWO rõ mặt ở hậu cảnh giữa hai cột. "
  "Không có ai khác trong khung.",
  "ADRIAN nói mà không quay đầu lại, THUG ONE bước ra khỏi bóng cột",
  [("ADRIAN", "even, exact", 3), ("THUG ONE", "flat, casual", 4)])

S("03", "trung 50mm, cao 1m30, cách THUG ONE 2m2, đặt bên lối xe, hạ thấp để lấy cả người ngồi xe lăn",
  "THUG ONE đứng ở nửa TRÁI khung, đã tới cách chiếc xe lăn hai bước. MAYA đứng ở nửa PHẢI khung, đã bước lên "
  "đứng chắn trước chiếc xe. ADRIAN ngồi trong chiếc xe tay cũ ở giữa khung phía sau cô.",
  "THUG ONE hai tay còn đút túi áo bomber. MAYA một tay đưa ra phía sau đặt lên vai ADRIAN. "
  "ADRIAN hai tay đặt trên vành bánh xe.",
  "MAYA nhìn thẳng vào THUG ONE. THUG ONE nhìn MAYA rồi nhìn xuống chiếc xe lăn. ADRIAN nhìn THUG ONE.",
  "MAYA — người bước lên chắn trước mà không kịp nghĩ: giọng bình, hơi thở nhanh. "
  "THUG ONE — trả lời một câu cho thấy họ đã theo dõi từ trước: mặt trống, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi một người thứ hai bước vào khung từ bên phải",
  ["THUG ONE", "MAYA_KHOAC", "ADRIAN_XELANTAY"], "giữa lối xe chạy hầm B2",
  {"THUG ONE": "đứng nửa trái khung, cách hai bước", "MAYA": "đứng chắn trước chiếc xe, nửa phải khung",
   "ADRIAN": "ngồi xe lăn tay cũ giữa khung phía sau MAYA"},
  "cách nhau hai bước", {"THUG ONE": "hai tay đút túi áo bomber",
                         "MAYA": "một tay đưa ra sau đặt lên vai ADRIAN",
                         "ADRIAN": "hai tay trên vành bánh xe"})
V("03", [5, 6], "trung 50mm hạ thấp · THUG ONE NÉT trái + MAYA NÉT phải đứng chắn trước xe + ADRIAN NÉT giữa ngồi xe lăn",
  [("THUG ONE", "THUG ONE"), ("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "THUG ONE, MAYA và ADRIAN, cả ba rõ mặt. Không có ai khác trong khung.",
  "MAYA bước lên đứng chắn trước chiếc xe lăn, một tay đưa ra sau đặt lên vai ADRIAN",
  [("MAYA", "steady, careful", 5), ("THUG ONE", "flat, matter-of-fact", 6)])

S("04", "cận-trung 85mm, cao 1m30, cách THUG TWO 1m8, đặt bên lối xe lấy THUG TWO nét và MAYA cùng khung",
  "THUG TWO đứng ở nửa TRÁI khung, đã tới sát chiếc xe lăn. MAYA đứng ở nửa PHẢI khung, một tay đã đưa ra "
  "chắn ngang trước tay vịn chiếc xe. Hậu cảnh là cột bê tông có vành sọc vàng đen và một xe con phủ bụi.",
  "THUG TWO một tay đưa ra đặt lên tay vịn chiếc xe lăn. MAYA một tay chắn ngang trước tay vịn đó.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "THUG TWO — nhắn lại lời của người thuê mình như đọc một tin nhắn: giọng đều, mặt trống. "
  "MAYA — chặn tay lại và nói rất chắc: mắt thẳng, giọng thấp.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay THUG TWO siết chặt lấy tay vịn",
  ["THUG TWO", "MAYA_KHOAC"], "cạnh chiếc xe lăn, giữa lối xe hầm B2",
  {"THUG TWO": "đứng nửa trái khung, tay trên tay vịn xe", "MAYA": "đứng nửa phải khung, chắn tay lại"},
  "sát nhau", {"THUG TWO": "một tay đặt lên tay vịn chiếc xe lăn",
               "MAYA": "một tay chắn ngang trước tay vịn"})
V("04", [7, 8], "cận-trung 85mm hạ thấp · THUG TWO NÉT trái tay trên tay vịn xe + MAYA NÉT phải chắn tay lại",
  [("THUG TWO", "THUG TWO"), ("MAYA", "MAYA_KHOAC")],
  "THUG TWO và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "THUG TWO đặt bàn tay lên tay vịn chiếc xe lăn, MAYA đưa tay chắn ngang lại",
  [("THUG TWO", "flat, delivering a message", 7), ("MAYA", "low, firm", 8)],
  ketclip="Cuối clip, THUG ONE gạt tay MAYA ra và hất mạnh chiếc xe lăn đổ nghiêng xuống nền bê tông. "
          "Clip dừng đúng lúc khung xe chạm nền.")

S("05", "trung 50mm, cao 0m70, cách ADRIAN 2m, máy hạ rất thấp ngang mặt nền bê tông",
  "ADRIAN nằm nghiêng trên nền bê tông ở nửa TRÁI khung, chiếc xe lăn tay cũ đổ nghiêng cạnh anh, một bánh còn quay. "
  "MAYA đứng ở nửa PHẢI khung, đã khuỵu một gối xuống. THUG ONE đứng phía trên ở rìa trái khung, thấy rõ mặt.",
  "ADRIAN một tay chống xuống nền bê tông. MAYA một tay chống xuống nền, tay kia đưa về phía ADRIAN. "
  "THUG ONE một tay còn giữ tay vịn chiếc xe đổ.",
  "ADRIAN nhìn về phía MAYA. MAYA nhìn ADRIAN. THUG ONE nhìn xuống ADRIAN.",
  "ADRIAN — ra lệnh cho vợ mình lùi lại trước khi lo cho bản thân: giọng gấp, mắt thẳng. "
  "MAYA — chưa kịp đứng dậy: mắt mở to. THUG ONE — mặt trống, không hằn học.",
  "đúng khoảnh khắc ngay TRƯỚC khi người thứ hai bước tới cạnh miệng cống",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC", "THUG ONE"], "nền bê tông hầm B2, chiếc xe lăn đổ nghiêng",
  {"ADRIAN": "nằm nghiêng trên nền bê tông nửa trái khung", "MAYA": "khuỵu một gối nửa phải khung",
   "THUG ONE": "đứng phía trên ở rìa trái khung"},
  "ba người trong vòng hai mét",
  {"ADRIAN": "một tay chống xuống nền bê tông", "MAYA": "một tay chống nền, tay kia đưa về phía ADRIAN",
   "THUG ONE": "một tay giữ tay vịn chiếc xe đổ"})
V("05", [9, 10], "trung 50mm hạ rất thấp · ADRIAN NÉT trái nằm nghiêng cạnh xe lăn đổ + MAYA NÉT phải khuỵu một gối + THUG ONE NÉT rìa trái đứng phía trên",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC"), ("THUG ONE", "THUG ONE")],
  "ADRIAN, MAYA và THUG ONE, cả ba rõ mặt. ADRIAN NẰM NGHIÊNG trên nền bê tông, chiếc xe lăn đổ cạnh anh. "
  "Không có ai khác trong khung.",
  "chiếc xe lăn đã đổ, ADRIAN chống một tay xuống nền và quay đầu về phía MAYA",
  [("THUG ONE", "flat, unbothered", 9), ("ADRIAN", "urgent, commanding", 10)])

S("06", "trung 50mm, cao 0m60, cách ADRIAN 2m2, máy hạ rất thấp, lấy miệng cống gang trên nền ở tiền cảnh",
  "ADRIAN nằm nghiêng ở giữa khung, cách MIỆNG CỐNG GANG VUÔNG trên nền bê tông một cánh tay. THUG TWO đứng ở "
  "nửa PHẢI khung phía trên anh, THUG ONE đã khuỵu một gối xuống ở nửa TRÁI khung cạnh bàn tay ADRIAN.",
  "THUG ONE một tay giữ cổ tay ADRIAN áp xuống nền bê tông. THUG TWO một tay chỉ về phía miệng cống. "
  "ADRIAN một tay còn chống nền.",
  "THUG TWO nhìn xuống ADRIAN. THUG ONE nhìn bàn tay mình đang giữ. ADRIAN nhìn thẳng lên THUG ONE.",
  "THUG TWO — bình luận như bình luận một chuyện vặt: mặt trống, giọng đều. "
  "THUG ONE — làm việc mình được thuê: mặt trống. ADRIAN — không kêu, không giãy: quai hàm siết, mắt mở.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người lao tới từ ngoài khung",
  ["ADRIAN_XELANTAY", "THUG ONE", "THUG TWO"], "nền bê tông hầm B2, cạnh miệng cống gang",
  {"ADRIAN": "nằm nghiêng giữa khung cạnh miệng cống", "THUG ONE": "khuỵu một gối nửa trái khung",
   "THUG TWO": "đứng phía trên nửa phải khung"},
  "ba người trong vòng một mét",
  {"THUG ONE": "một tay giữ cổ tay ADRIAN áp xuống nền", "THUG TWO": "một tay chỉ về phía miệng cống",
   "ADRIAN": "một tay còn chống nền bê tông"})
V("06", [11, 12], "trung 50mm hạ rất thấp · ADRIAN NÉT giữa nằm nghiêng + THUG ONE NÉT trái khuỵu gối giữ cổ tay + THUG TWO NÉT phải đứng phía trên",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("THUG ONE", "THUG ONE"), ("THUG TWO", "THUG TWO")],
  "ADRIAN, THUG ONE và THUG TWO, cả ba rõ mặt. ADRIAN nằm nghiêng trên nền bê tông. "
  "KHÔNG có cảnh đánh đấm nào diễn ra trong khung — chỉ có bàn tay bị giữ áp xuống nền.",
  "THUG ONE khuỵu một gối xuống giữ cổ tay ADRIAN áp lên nền bê tông, THUG TWO chỉ về phía miệng cống",
  [("THUG TWO", "flat, commenting", 11), ("THUG ONE", "flat, instructing", 12)])

S("07", "cận-trung 85mm, cao 0m70, cách ADRIAN 1m5, máy hạ rất thấp ngang mặt nền bê tông",
  "ADRIAN nằm nghiêng chiếm phần lớn khung, mặt hướng lên. MAYA đã lao tới ở nửa PHẢI khung, hai tay bám lấy "
  "cánh tay THUG ONE. Ở rìa TRÁI khung thấy một mảng vai áo bomber đen của THUG ONE, out nét.",
  "MAYA hai tay bám chặt lấy cẳng tay THUG ONE kéo ra. ADRIAN một tay còn bị giữ áp xuống nền.",
  "ADRIAN nhìn thẳng vào THUG ONE ngoài khung. MAYA nhìn xuống bàn tay bị giữ của ADRIAN.",
  "ADRIAN — người đổi cả bàn tay mình lấy việc họ không chạm vào cô: giọng chắc, mắt không chớp. "
  "MAYA — mất bình tĩnh lần đầu trong cả bộ phim: giọng vỡ, hai tay ghì mạnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi có bàn tay thứ hai nắm lấy cánh tay cô kéo ra",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC", "THUG ONE"], "nền bê tông hầm B2, cạnh miệng cống gang",
  {"ADRIAN": "nằm nghiêng giữa khung", "MAYA": "lao tới nửa phải khung, hai tay bám cẳng tay THUG ONE",
   "THUG ONE": "một mảng vai áo bomber ở rìa trái khung"},
  "ba người trong vòng một mét",
  {"ADRIAN": "một tay còn bị giữ áp xuống nền", "MAYA": "hai tay bám chặt cẳng tay THUG ONE",
   "THUG ONE": "một tay giữ cổ tay ADRIAN, ngoài vùng nét"})
V("07", [13, 14], "cận-trung 85mm hạ rất thấp · ADRIAN NÉT nằm nghiêng + MAYA NÉT phải bám cẳng tay · một mảng vai THUG ONE rìa trái out nét",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC"), ("THUG ONE", "THUG ONE")],
  "ADRIAN và MAYA rõ mặt. THUG ONE chỉ thấy MỘT MẢNG VAI áo bomber đen ở rìa trái, out nét — "
  "KHÔNG quay mặt về camera. KHÔNG có cảnh đánh đấm nào diễn ra trong khung.",
  "MAYA lao tới bám hai tay vào cẳng tay đang giữ cổ tay ADRIAN và ghì ra",
  [("ADRIAN", "firm, bargaining", 13), ("MAYA", "breaking, loud", 14)])

S("08", "trung 50mm, cao 0m80, cách MAYA 2m, máy hạ rất thấp ngang mặt nền bê tông",
  "MAYA quỳ ở giữa khung, người chắn giữa ADRIAN và hai người kia. THUG TWO đứng ở nửa PHẢI khung phía trên cô. "
  "ADRIAN nằm nghiêng ở nửa TRÁI khung phía sau lưng cô.",
  "MAYA hai tay dang ngang chắn phía sau lưng mình. THUG TWO một tay đưa ra phía MAYA. "
  "ADRIAN một tay chống xuống nền.",
  "MAYA nhìn thẳng lên THUG TWO. THUG TWO nhìn xuống MAYA. ADRIAN nhìn lưng MAYA.",
  "MAYA — người tự đặt mình vào giữa và nói ra điều kiện: giọng chắc, mắt không chớp, hai tay dang rộng. "
  "THUG TWO — mặt trống, giọng đều. ADRIAN — nhìn lưng vợ mình chắn trước: mắt đỏ, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay THUG TWO chạm vào vai MAYA",
  ["MAYA_KHOAC", "THUG TWO", "ADRIAN_XELANTAY"], "nền bê tông hầm B2",
  {"MAYA": "quỳ giữa khung, hai tay dang ngang chắn", "THUG TWO": "đứng phía trên nửa phải khung",
   "ADRIAN": "nằm nghiêng nửa trái khung phía sau MAYA"},
  "ba người trong vòng một mét",
  {"MAYA": "hai tay dang ngang chắn phía sau lưng", "THUG TWO": "một tay đưa ra phía MAYA",
   "ADRIAN": "một tay chống xuống nền"})
V("08", [15, 16], "trung 50mm hạ rất thấp · MAYA NÉT giữa quỳ dang tay chắn + THUG TWO NÉT phải đứng phía trên + ADRIAN NÉT trái nằm nghiêng phía sau",
  [("MAYA", "MAYA_KHOAC"), ("THUG TWO", "THUG TWO"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA, THUG TWO và ADRIAN, cả ba rõ mặt. KHÔNG có cảnh đánh đấm nào diễn ra trong khung.",
  "MAYA quỳ chắn giữa, hai tay dang ngang che phía sau lưng mình",
  [("THUG TWO", "flat, ordering", 15), ("MAYA", "firm, unmoving", 16)])

S("09", "cận-trung 85mm, cao 0m90, cách THUG ONE 1m6, máy hạ thấp, lấy hai người đứng và một mảng vai MAYA rìa dưới",
  "THUG ONE đứng ở nửa TRÁI khung, đã đứng thẳng dậy. THUG TWO đứng ở nửa PHẢI khung. Ở rìa DƯỚI khung thấy "
  "một mảng vai và búi tóc của MAYA đang quỳ, out nét.",
  "THUG ONE một tay chỉ xuống phía MAYA. THUG TWO một tay đưa xuống về phía búi tóc MAYA.",
  "Cả hai nhìn xuống MAYA ở rìa dưới khung.",
  "THUG ONE — nhận xét một cách nghề nghiệp: mặt trống, giọng đều. "
  "THUG TWO — trả lời gọn: mặt trống.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay THUG TWO chạm vào tóc MAYA",
  ["THUG ONE", "THUG TWO", "MAYA_KHOAC"], "nền bê tông hầm B2",
  {"THUG ONE": "đứng nửa trái khung", "THUG TWO": "đứng nửa phải khung",
   "MAYA": "một mảng vai và búi tóc ở rìa dưới khung"},
  "hai người đứng phía trên MAYA đang quỳ",
  {"THUG ONE": "một tay chỉ xuống phía MAYA", "THUG TWO": "một tay đưa xuống phía búi tóc MAYA",
   "MAYA": "hai tay dang ngang, ngoài vùng nét"})
V("09", [17, 18], "cận-trung 85mm hạ thấp · THUG ONE NÉT trái + THUG TWO NÉT phải · một mảng vai và búi tóc MAYA rìa dưới khung out nét",
  [("THUG ONE", "THUG ONE"), ("THUG TWO", "THUG TWO"), ("MAYA", "MAYA_KHOAC")],
  "THUG ONE và THUG TWO rõ mặt. MAYA chỉ thấy MỘT MẢNG VAI và búi tóc ở rìa dưới khung, out nét — "
  "KHÔNG thấy mặt. KHÔNG có cảnh đánh đấm nào diễn ra trong khung.",
  "THUG ONE chỉ xuống phía MAYA, THUG TWO đưa tay xuống",
  [("THUG ONE", "flat, observing", 17), ("THUG TWO", "flat, deciding", 18)],
  ketclip="Cuối clip, THUG TWO túm lấy búi tóc MAYA ghì cô áp xuống nền bê tông cạnh ADRIAN. "
          "Clip dừng đúng lúc má cô chạm nền.")

S("10", "cận 85mm, cao 0m40, cách MAYA 1m1, máy đặt sát mặt nền bê tông, ngang tầm hai gương mặt nằm",
  "MAYA nằm nghiêng áp má xuống nền bê tông ở nửa PHẢI khung. ADRIAN nằm nghiêng ở nửa TRÁI khung, mặt cách "
  "mặt cô chừng một gang. Ở rìa trên khung thấy một mảng ống quần đen của THUG ONE, out nét.",
  "MAYA một tay đưa lên phía búi tóc mình, tay kia duỗi trên nền về phía ADRIAN. "
  "ADRIAN một tay duỗi trên nền về phía MAYA.",
  "Hai người nhìn thẳng vào mắt nhau qua khoảng nền bê tông.",
  "MAYA — người đau nhưng chỉ tập trung vào việc bảo anh đừng nhìn: giọng gấp, mắt ướt. "
  "THUG ONE — mặt trống, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN gọi tên cô",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY", "THUG ONE"], "nền bê tông hầm B2, hai người nằm cạnh nhau",
  {"MAYA": "nằm nghiêng áp má xuống nền, nửa phải khung", "ADRIAN": "nằm nghiêng nửa trái khung",
   "THUG ONE": "một mảng ống quần đen ở rìa trên khung"},
  "hai gương mặt cách nhau một gang",
  {"MAYA": "một tay đưa lên phía búi tóc, tay kia duỗi về phía ADRIAN",
   "ADRIAN": "một tay duỗi trên nền về phía MAYA", "THUG ONE": "đứng phía trên, ngoài vùng nét"})
V("10", [19, 20], "cận 85mm sát mặt nền · MAYA NÉT phải nằm nghiêng + ADRIAN NÉT trái nằm nghiêng · một mảng ống quần THUG ONE rìa trên out nét",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY"), ("THUG ONE", "THUG ONE")],
  "MAYA và ADRIAN rõ mặt, cùng nằm nghiêng trên nền bê tông. THUG ONE chỉ thấy MỘT MẢNG ỐNG QUẦN ĐEN ở rìa "
  "trên khung, out nét. KHÔNG có cảnh đánh đấm nào diễn ra trong khung.",
  "MAYA nằm áp má xuống nền, một tay đưa lên phía búi tóc mình",
  [("MAYA", "gasping, urgent", 19), ("THUG ONE", "flat, ordering", 20)])

S("11", "cận 85mm, cao 0m40, cách MAYA 1m, máy đặt sát mặt nền bê tông, chính diện gương mặt MAYA",
  "MAYA nằm nghiêng chiếm phần lớn khung, má áp xuống nền bê tông, tóc xoã một bên. Ở rìa TRÁI khung thấy "
  "bàn tay và một phần vai áo len của ADRIAN đang duỗi trên nền, out nét.",
  "MAYA một bàn tay duỗi trên nền, các ngón khép lại rồi mở ra một lần.",
  "MAYA nhìn thẳng vào mắt ADRIAN qua khoảng nền bê tông.",
  "MAYA — người chỉ muốn duy nhất một điều là anh đừng phải nhìn thấy cô như thế này: mắt ướt tràn, "
  "giọng rất nhỏ, KHÔNG gào.",
  "đúng khoảnh khắc ngay TRƯỚC khi các ngón tay hai người chạm vào nhau trên nền bê tông",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "nền bê tông hầm B2, hai người nằm cạnh nhau",
  {"MAYA": "nằm nghiêng chính diện giữa khung",
   "ADRIAN": "bàn tay và một phần vai áo len ở rìa trái khung"},
  "hai gương mặt cách nhau một gang",
  {"MAYA": "một bàn tay duỗi trên nền, các ngón khép rồi mở",
   "ADRIAN": "một bàn tay duỗi trên nền, ngoài vùng nét"})
V("11", [21, 22], "cận 85mm sát mặt nền · MAYA NÉT nằm nghiêng chính diện · bàn tay và một phần vai ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA rõ mặt nằm nghiêng trên nền bê tông. ADRIAN chỉ thấy BÀN TAY và một phần vai áo len ở rìa trái, "
  "out nét — KHÔNG thấy mặt. KHÔNG có cảnh đánh đấm nào trong khung.",
  "MAYA duỗi bàn tay trên nền về phía ADRIAN, các ngón khép lại rồi mở ra",
  [("MAYA", "very small, urgent", 21), ("ADRIAN", "breaking, quiet", 22)])

S("12", "cận 85mm, cao 0m40, cách MAYA 1m, máy sát mặt nền, lấy MAYA nét và bàn tay ADRIAN ở rìa trái",
  "MAYA nằm nghiêng chiếm phần lớn khung, đã nhấc má lên khỏi nền một chút. Ở rìa TRÁI khung thấy bàn tay "
  "ADRIAN trên nền, out nét. Bàn tay phải của MAYA giơ lên trong khung, HAI NGÓN ĐANG CO LẠI BẤT THƯỜNG.",
  "MAYA một tay giơ lên trước mặt, hai ngón trỏ và giữa co lại không duỗi thẳng được; tay kia chống nền.",
  "MAYA nhìn vào bàn tay mình rồi nhìn sang ADRIAN.",
  "MAYA — người đang tự trấn an chồng mình bằng cách nói nhỏ đi mức độ chấn thương: giọng cố giữ bình, "
  "mắt ướt, KHÔNG kêu đau.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng ra lệnh rút lui từ phía trên",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "nền bê tông hầm B2, hai người nằm cạnh nhau",
  {"MAYA": "nằm nghiêng, nhấc má lên, chính diện giữa khung",
   "ADRIAN": "bàn tay trên nền ở rìa trái khung"},
  "hai gương mặt cách nhau một gang",
  {"MAYA": "một tay giơ lên trước mặt, hai ngón co lại; tay kia chống nền",
   "ADRIAN": "một bàn tay duỗi trên nền, ngoài vùng nét"})
V("12", [23], "cận 85mm sát mặt nền · MAYA NÉT nằm nghiêng nhấc má lên · bàn tay ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA rõ mặt. ADRIAN chỉ thấy BÀN TAY trên nền ở rìa trái, out nét. "
  "KHÔNG có cảnh đánh đấm nào trong khung.",
  "MAYA giơ bàn tay lên trước mặt, hai ngón co lại không duỗi thẳng được",
  [("MAYA", "steady, minimising", 23)], [("ADRIAN", "silent, watching her hand")])

S("13", "trung 50mm, cao 0m80, cách THUG ONE 2m2, máy hạ rất thấp nhìn từ nền lên hai người đứng",
  "THUG ONE đứng ở nửa TRÁI khung, đã lùi lại một bước. THUG TWO đứng ở nửa PHẢI khung. Ở rìa DƯỚI khung thấy "
  "vai MAYA và một phần khung chiếc xe lăn đổ, out nét.",
  "THUG ONE một tay hất về phía dốc xe. THUG TWO hai tay đút túi hoodie.",
  "Cả hai nhìn xuống hai người dưới nền một lượt cuối rồi nhìn về phía dốc xe.",
  "THUG ONE — kết thúc công việc và chuyển sang việc khác: mặt trống, giọng đều. "
  "THUG TWO — nhắn nốt lời của người thuê: mặt trống, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai người quay lưng đi về phía dốc xe",
  ["THUG ONE", "THUG TWO", "MAYA_KHOAC"], "nền bê tông hầm B2",
  {"THUG ONE": "đứng nửa trái khung", "THUG TWO": "đứng nửa phải khung",
   "MAYA": "vai và một phần khung xe lăn đổ ở rìa dưới khung"},
  "hai người đứng phía trên",
  {"THUG ONE": "một tay hất về phía dốc xe", "THUG TWO": "hai tay đút túi hoodie",
   "MAYA": "nằm nghiêng dưới nền, ngoài vùng nét"})
V("13", [24, 25], "trung 50mm hạ rất thấp · THUG ONE NÉT trái + THUG TWO NÉT phải · vai MAYA và khung xe lăn đổ rìa dưới out nét",
  [("THUG ONE", "THUG ONE"), ("THUG TWO", "THUG TWO"), ("MAYA", "MAYA_KHOAC")],
  "THUG ONE và THUG TWO rõ mặt. MAYA chỉ thấy VAI và một phần khung chiếc xe lăn đổ ở rìa dưới khung, out nét. "
  "KHÔNG có cảnh đánh đấm nào trong khung.",
  "THUG ONE hất tay về phía dốc xe, THUG TWO nói nốt một câu rồi cả hai quay lưng",
  [("THUG ONE", "flat, wrapping up", 24), ("THUG TWO", "flat, parting", 25)],
  ketclip="Cuối clip, hai người quay lưng đi khuất về phía dốc xe, hầm chỉ còn hai người nằm dưới nền. "
          "Clip dừng đúng lúc tiếng bước chân tắt hẳn.")

S("14", "cận-trung 85mm, cao 0m60, cách MAYA 1m5, máy sát mặt nền bê tông lấy cả hai người nằm",
  "MAYA đã chống người ngồi dậy được ở nửa PHẢI khung, một tay ôm bàn tay bị thương vào ngực. ADRIAN nằm nghiêng "
  "ở nửa TRÁI khung, chiếc xe lăn đổ phía sau anh. Hầm vắng, không còn ai khác.",
  "MAYA một tay ôm bàn tay bị thương vào ngực, tay kia đặt lên vai ADRIAN. ADRIAN một tay chống xuống nền.",
  "MAYA nhìn xuống mặt ADRIAN. ADRIAN nhìn lên MAYA.",
  "MAYA — điều dưỡng hồi sức quay lại làm việc ngay cả khi tay mình vừa gãy: giọng nhanh, gọn, "
  "mắt quét khắp người anh. ADRIAN — mắt đỏ, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN gọi tên trợ lý của mình",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "nền bê tông hầm B2, cạnh chiếc xe lăn đổ",
  {"MAYA": "ngồi dậy được, nửa phải khung", "ADRIAN": "nằm nghiêng nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay ôm bàn tay bị thương vào ngực, tay kia đặt lên vai ADRIAN",
                    "ADRIAN": "một tay chống xuống nền"})
V("14", [26], "cận-trung 85mm sát mặt nền · MAYA NÉT phải ngồi dậy + ADRIAN NÉT trái nằm nghiêng",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN, cả hai rõ mặt trên nền bê tông. Không có ai khác trong khung.",
  "MAYA chống người ngồi dậy, một tay ôm bàn tay bị thương, tay kia đặt lên vai ADRIAN",
  [("MAYA", "fast, clinical", 26)], [("ADRIAN", "silent, eyes red")])

S("15", "cận 85mm, cao 0m60, cách ADRIAN 1m2, máy sát mặt nền, lấy ADRIAN nét và một mảng vai MAYA rìa phải",
  "ADRIAN nằm nghiêng chống trên một khuỷu tay, chiếm phần lớn khung. Ở rìa PHẢI khung thấy một mảng vai và "
  "cánh tay của MAYA đang ngồi, out nét. Bên tai phải ADRIAN có một TAI NGHE KHÔNG DÂY nhỏ màu đen.",
  "ADRIAN một tay đưa lên chạm vào chiếc tai nghe không dây ở tai phải.",
  "ADRIAN nhìn thẳng về phía trước, không nhìn MAYA.",
  "ADRIAN — người vừa quyết định chấm dứt sáu tháng đóng vai: mặt hoàn toàn bình, mắt tĩnh và tối lại, "
  "giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN ra lệnh đầu tiên",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC"], "nền bê tông hầm B2, cạnh chiếc xe lăn đổ",
  {"ADRIAN": "nằm nghiêng chống khuỷu tay, giữa khung",
   "MAYA": "một mảng vai và cánh tay ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay chạm vào chiếc tai nghe không dây ở tai phải",
                    "MAYA": "một tay ôm bàn tay bị thương, ngoài vùng nét"})
V("15", [27, 28], "cận 85mm sát mặt nền · ADRIAN NÉT nằm chống khuỷu tay · một mảng vai MAYA rìa phải out nét · SEBASTIAN ngoài khung, chỉ có giọng",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC"), (SB, "SEBASTIAN")],
  "ADRIAN rõ mặt. MAYA chỉ thấy MỘT MẢNG VAI ở rìa phải, out nét. SEBASTIAN KHÔNG xuất hiện trong khung, "
  "chỉ nghe giọng qua chiếc tai nghe không dây.",
  "ADRIAN đưa tay lên chạm vào chiếc tai nghe không dây ở tai phải và gọi một cái tên",
  [("ADRIAN", "quiet, level", 27), (SB, "urgent, professional", 28)])

S("16", "cận 85mm, cao 0m60, cách ADRIAN 1m1, máy sát mặt nền, chính diện gương mặt ADRIAN",
  "ADRIAN nằm nghiêng chống trên một khuỷu tay chiếm phần lớn khung. Ở rìa PHẢI khung thấy một mảng vai áo khoác dạ "
  "màu ô liu bạc của MAYA, out nét. Hậu cảnh là nền bê tông và một bánh xe lăn đổ còn quay chậm.",
  "ADRIAN một tay giữ chiếc tai nghe ở tai phải, các ngón siết lại.",
  "ADRIAN nhìn thẳng về phía trước, mắt không chớp.",
  "ADRIAN — người ra lệnh gọi về toàn bộ thứ mình đã cất đi sáu tháng: giọng đều, rất nhỏ, mặt hoàn toàn bình, "
  "KHÔNG giận dữ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN nói ra ngày giờ",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC"], "nền bê tông hầm B2",
  {"ADRIAN": "nằm nghiêng chống khuỷu tay, chính diện giữa khung",
   "MAYA": "một mảng vai áo khoác ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay giữ chiếc tai nghe ở tai phải",
                    "MAYA": "ngồi cạnh, ngoài vùng nét"})
V("16", [29, 30], "cận 85mm sát mặt nền · ADRIAN NÉT chính diện · một mảng vai MAYA rìa phải out nét · SEBASTIAN ngoài khung, chỉ có giọng",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC"), (SB, "SEBASTIAN")],
  "ADRIAN rõ mặt. MAYA chỉ thấy MỘT MẢNG VAI ở rìa phải, out nét. SEBASTIAN KHÔNG xuất hiện trong khung, "
  "chỉ nghe giọng qua chiếc tai nghe không dây.",
  "ADRIAN siết chặt chiếc tai nghe ở tai phải và ra lệnh",
  [("ADRIAN", "quiet, absolute", 29), (SB, "professional, confirming", 30)])

S("17", "cận-trung 85mm, cao 0m60, cách ADRIAN 1m4, máy sát mặt nền lấy cả hai người",
  "ADRIAN nằm nghiêng chống khuỷu tay ở nửa TRÁI khung. MAYA ngồi ở nửa PHẢI khung, đã quay hẳn sang nhìn anh, "
  "bàn tay bị thương ôm vào ngực. Hậu cảnh là chiếc xe lăn đổ và cột bê tông.",
  "ADRIAN một tay giữ chiếc tai nghe ở tai phải. MAYA một tay ôm bàn tay bị thương vào ngực.",
  "ADRIAN nhìn thẳng về phía trước. MAYA nhìn ADRIAN.",
  "ADRIAN — người đọc ra một ngày và một địa điểm như đọc lịch hẹn: giọng đều, mặt bình. "
  "MAYA — nghe chồng mình nói vào tai nghe với một người vô hình: mắt mở to, mày chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi anh đang nói chuyện với ai",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC"], "nền bê tông hầm B2",
  {"ADRIAN": "nằm nghiêng chống khuỷu tay nửa trái khung", "MAYA": "ngồi nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay giữ chiếc tai nghe ở tai phải",
                    "MAYA": "một tay ôm bàn tay bị thương vào ngực"})
V("17", [31, 32, 33], "cận-trung 85mm sát mặt nền · ADRIAN NÉT trái nằm chống khuỷu tay + MAYA NÉT phải ngồi cạnh · SEBASTIAN ngoài khung, chỉ có giọng",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC"), (SB, "SEBASTIAN")],
  "ADRIAN và MAYA rõ mặt. SEBASTIAN KHÔNG xuất hiện trong khung, chỉ nghe giọng qua chiếc tai nghe không dây.",
  "ADRIAN nói vào chiếc tai nghe, MAYA quay hẳn sang nhìn anh",
  [("ADRIAN", "even, listing", 31), (SB, "professional, asking", 32),
   ("ADRIAN", "quiet, deciding", 33)])

S("18", "cận-trung 85mm, cao 0m60, cách MAYA 1m4, máy sát mặt nền lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung, đã chồm tới gần ADRIAN. ADRIAN nằm nghiêng chống khuỷu tay ở nửa TRÁI khung, "
  "một tay đã đưa ra phía cô. Hậu cảnh là nền bê tông và chiếc xe lăn đổ.",
  "MAYA một tay chống xuống nền, tay kia còn ôm bàn tay bị thương. ADRIAN một tay đưa ra ngửa lòng bàn tay "
  "về phía MAYA.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa nghe ba câu mà mình không hiểu chữ nào: mày chau, giọng nhanh. "
  "ADRIAN — không trả lời câu hỏi và đòi xem bàn tay: giọng chắc, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt bàn tay bị thương vào lòng bàn tay anh",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "nền bê tông hầm B2",
  {"MAYA": "ngồi chồm tới nửa phải khung", "ADRIAN": "nằm nghiêng chống khuỷu tay nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay chống nền, tay kia ôm bàn tay bị thương",
                    "ADRIAN": "một tay đưa ra ngửa lòng bàn tay"})
V("18", [34, 35], "cận-trung 85mm sát mặt nền · MAYA NÉT phải ngồi chồm tới + ADRIAN NÉT trái nằm chống khuỷu tay",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN, cả hai rõ mặt trên nền bê tông. Không có ai khác trong khung.",
  "MAYA chồm tới hỏi, ADRIAN đưa một tay ra ngửa lòng bàn tay về phía cô",
  [("MAYA", "quick, bewildered", 34), ("ADRIAN", "firm, quiet", 35)])

S("19", "cận 85mm, cao 0m60, cách MAYA 1m1, máy sát mặt nền, lấy hai bàn tay ở tiền cảnh và mặt MAYA phía sau",
  "MAYA ngồi chiếm phần lớn khung từ ngực trở lên, bàn tay bị thương đã đặt trong lòng bàn tay ADRIAN ở tiền "
  "cảnh dưới khung. Ở rìa TRÁI khung thấy một mảng vai và cánh tay ADRIAN, out nét.",
  "MAYA đặt bàn tay bị thương vào lòng bàn tay ADRIAN, hai ngón còn co lại. ADRIAN một tay đỡ dưới bàn tay cô.",
  "MAYA nhìn xuống hai bàn tay rồi ngước lên nhìn ADRIAN.",
  "MAYA — người nghe một lời cảnh báo mà chưa hiểu: mày chau, mắt dò. "
  "ADRIAN — báo trước cho vợ mình rằng cô sắp ghét anh: giọng chậm, mắt không rời, KHÔNG né.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi vì sao mình lại ghét anh",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "nền bê tông hầm B2",
  {"MAYA": "ngồi chính diện giữa khung, tay đặt trong lòng bàn tay ADRIAN",
   "ADRIAN": "một mảng vai và cánh tay ở rìa trái khung"},
  "sát cạnh nhau", {"MAYA": "đặt bàn tay bị thương vào lòng bàn tay ADRIAN",
                    "ADRIAN": "một tay đỡ dưới bàn tay MAYA"})
V("19", [36, 37], "cận 85mm sát mặt nền · MAYA NÉT chính diện · một mảng vai và cánh tay ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI và cánh tay ở rìa trái, out nét — KHÔNG quay mặt về camera.",
  "MAYA đặt bàn tay bị thương vào lòng bàn tay ADRIAN, hai ngón còn co lại",
  [("MAYA", "quiet, minimising", 36), ("ADRIAN", "slow, warning", 37)])

S("20", "cận-trung 85mm, cao 0m60, cách ADRIAN 1m3, máy sát mặt nền lấy cả hai người",
  "ADRIAN nằm nghiêng chống khuỷu tay ở nửa TRÁI khung, MAYA ngồi ở nửa PHẢI khung, hai bàn tay còn nắm nhau "
  "giữa hai người. Hậu cảnh là chiếc xe lăn đổ nghiêng và cột bê tông có vành sọc vàng đen.",
  "ADRIAN một tay giữ bàn tay bị thương của MAYA. MAYA một tay để yên trong tay anh, tay kia chống nền.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — hỏi một câu rất thật vì cô không tưởng tượng nổi lý do: mày chau, mắt ướt. "
  "ADRIAN — nói ra câu thú nhận đầu tiên của cả bộ phim: giọng rất nhỏ, mắt không rời, mặt không giấu gì nữa.",
  "đúng khoảnh khắc ngay TRƯỚC khi ánh đèn tuýp trên trần nhấp một cái rồi sáng lại",
  ["ADRIAN_XELANTAY", "MAYA_KHOAC"], "nền bê tông hầm B2",
  {"ADRIAN": "nằm nghiêng chống khuỷu tay nửa trái khung", "MAYA": "ngồi nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay giữ bàn tay bị thương của MAYA",
                    "MAYA": "một tay để yên trong tay anh, tay kia chống nền"})
V("20", [38, 39], "cận-trung 85mm sát mặt nền · ADRIAN NÉT trái nằm chống khuỷu tay + MAYA NÉT phải ngồi cạnh",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_KHOAC")],
  "ADRIAN và MAYA, cả hai rõ mặt trên nền bê tông. Không có ai khác trong khung.",
  "ADRIAN giữ bàn tay bị thương của MAYA trong tay mình và nói rất nhỏ",
  [("MAYA", "small, bewildered", 38), ("ADRIAN", "very quiet, confessing", 39)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 0m80, cách MAYA 7m, máy hạ rất thấp giữa lối xe chạy nhìn dọc hầm",
  "Hầm xe đã vắng hẳn. MAYA ngồi trên nền bê tông ở giữa khung, một tay ôm bàn tay bị thương vào ngực, "
  "tay kia đỡ sau lưng ADRIAN. ADRIAN nằm nghiêng chống trên một khuỷu tay cạnh cô. Chiếc xe lăn tay cũ "
  "đổ nghiêng phía sau hai người, một bánh còn quay chậm.",
  "MAYA một tay ôm bàn tay bị thương vào ngực, tay kia đỡ sau lưng ADRIAN. ADRIAN một tay chống xuống nền.",
  "Cả hai nhìn về phía dốc xe nơi ba người kia vừa đi khỏi.",
  "MAYA — người vừa lấy thân mình chắn cho chồng và trả giá bằng hai ngón tay: mặt trắng, hơi thở ngắn, "
  "KHÔNG khóc. ADRIAN — mắt tối lại, quai hàm siết: người vừa quyết định xong mọi thứ.",
  "đúng khoảnh khắc ngay TRƯỚC khi bánh xe lăn đổ ngừng quay hẳn",
  ["MAYA_KHOAC", "ADRIAN_XELANTAY"], "nền bê tông hầm B2, cạnh chiếc xe lăn đổ",
  {"MAYA": "ngồi trên nền bê tông giữa khung", "ADRIAN": "nằm nghiêng chống khuỷu tay cạnh cô"},
  "sát cạnh nhau", {"MAYA": "một tay ôm bàn tay bị thương, tay kia đỡ sau lưng ADRIAN",
                    "ADRIAN": "một tay chống xuống nền bê tông"})
B("B2", "Khép cảnh. Hầm xe đã vắng. Hai người ngồi lại trên nền bê tông cạnh chiếc xe lăn đổ, một bánh còn quay.",
  "toàn cảnh 24mm hạ rất thấp · MAYA NÉT ngồi trên nền + ADRIAN NÉT nằm nghiêng cạnh cô · chiếc xe lăn đổ phía sau",
  [("MAYA", "MAYA_KHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN rõ mặt trên nền bê tông, chiếc xe lăn tay cũ đổ nghiêng phía sau họ. "
  "Không có người nào khác trong khung.",
  "hai người vừa trả giá bằng một bàn tay gãy cho một phiên toà họ đã thắng; và trong đúng ba mươi giây vừa rồi, "
  "người đàn ông nằm dưới nền đã quyết định chấm dứt sáu tháng đóng vai.",
  "bánh chiếc xe lăn đổ quay chậm dần rồi dừng; một bóng đèn tuýp trên trần nhấp nháy hai lần rồi sáng đều; "
  "MAYA đỡ ADRIAN ngồi tựa vào một cột bê tông; không ai nói gì.",
  "Ambient tiếng vọng bê tông của hầm xe và tiếng quạt thông gió, SFX tiếng bánh xe lăn quay chậm rồi dừng.",
  nhac("NÂNG", "Đây là mốc bản lề của cả phim: từ giây này người đàn ông trong xe lăn bắt đầu phản công. Nhạc dựng lên nhưng phải tối, không hân hoan.",
       "Cinematic soul at 80 BPM; a low cello and an upright bass building from silence, a slow heartbeat kick "
       "entering at the midpoint, a female alto singing two low lines close to the mic; the pull is when everything "
       "cuts to one held cello note; lyrics about a decision made on a concrete floor with a broken hand; "
       "warm analog mix, female vocal, cello, upright bass, cinematic, dark",
       "Cinematic instrumental at 78 BPM; low strings rising from silence under a slow heartbeat kick, a French horn "
       "entering once at the midpoint, everything cutting to a single sustained cello note at the end; "
       "cold analog mix, strings, horn, cello, cinematic, dark"),
  dur=10)
