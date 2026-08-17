# -*- coding: utf-8 -*-
"""SCENE 14 — PHÒNG XỬ ÁN HẠT (ban ngày). Phiên giám hộ."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S14", "REF_TOAAN_NGAY", qc=qc.S14)

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 10m, đặt cuối phòng xử nhìn về phía bục thẩm phán",
  "JUDGE WHITMORE ngồi trên bục thẩm phán gỗ sồi cao ở cuối phòng. Ở khu xử phía dưới, JULIAN và luật sư của ông "
  "ngồi ở bàn luật sư bên trái; MAYA ngồi ở bàn bên phải, ADRIAN đỗ xe lăn ngay cạnh cô ở đầu bàn.",
  "JUDGE WHITMORE hai tay đặt trên mặt bục, một tay cạnh chiếc búa gỗ. JULIAN hai tay đan trên mặt bàn. "
  "Người luật sư cạnh ông đặt một tay lên cặp da đen. MAYA hai tay đặt trên một tập hồ sơ.",
  "Tất cả những người ở khu xử đều nhìn về phía bục thẩm phán. JUDGE WHITMORE nhìn xuống hồ sơ trước mặt.",
  "JUDGE WHITMORE — uy nghiêm và chưa nghiêng về bên nào: mặt bình, mắt đọc. JULIAN — tự tin: khoé môi kéo nhẹ. "
  "MAYA — căng nhưng ngồi rất thẳng: cằm ngang. ADRIAN — mặt tĩnh, mắt nhìn thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi JUDGE WHITMORE gõ búa mở phiên",
  ["JUDGE WHITMORE", "JULIAN", "MAYA_TUTE", "ADRIAN_TUTE"], "khu xử phòng xử án",
  {"JUDGE WHITMORE": "ngồi trên bục thẩm phán", "JULIAN": "ngồi bàn luật sư bên trái",
   "MAYA": "ngồi bàn bên phải", "ADRIAN": "ngồi xe lăn cạnh MAYA ở đầu bàn"},
  "hai bàn luật sư cách nhau ba mét",
  {"JUDGE WHITMORE": "hai tay trên mặt bục", "JULIAN": "hai tay đan trên mặt bàn",
   "MAYA": "hai tay đặt trên tập hồ sơ", "ADRIAN": "hai tay trên vành tay vịn"})
B("B1", "Mở cảnh. Phiên toà giám hộ. JUDGE WHITMORE trên bục, JULIAN và luật sư một bên, MAYA và ADRIAN bên kia.",
  "toàn cảnh 24mm · JUDGE WHITMORE NÉT trên bục + JULIAN NÉT bàn trái + MAYA NÉT bàn phải + ADRIAN NÉT ngồi xe lăn cạnh MAYA",
  [("JUDGE WHITMORE", "JUDGE WHITMORE"), ("JULIAN", "JULIAN"), ("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "JUDGE WHITMORE, JULIAN, MAYA và ADRIAN rõ mặt. Vài người ngồi ở hàng ghế khán giả phía sau mờ, "
  "không ai nhìn vào camera.",
  "hai bên bàn cách nhau ba mét và cách nhau cả một thế giới: một bên là tiền của gia tộc, một bên là "
  "hai mươi chín ngày ghi chép của một điều dưỡng.",
  "JUDGE WHITMORE lật một trang hồ sơ; JULIAN'S LAWYER mở khoá cặp da; MAYA vuốt phẳng mép tập hồ sơ của mình; "
  "cột nắng qua cửa sổ vòm quét ngang lối đi giữa.",
  "Ambient tiếng vọng của một phòng xử trần cao, tiếng giấy lật và tiếng ghế gỗ dịch.",
  nhac("KÌM", "Cả cảnh là một trận đánh bằng giấy tờ và giọng nói bình tĩnh; nhạc phải nén, tuyệt đối không kịch tính hoá.",
       "Chamber soul at 66 BPM; upright bass and a muted Rhodes only, a female alto entering once with a single low "
       "line; no drums; the pull is one full bar of silence before the last chord; lyrics about walking into a room "
       "where somebody is trying to take a person away from himself; dry mix, female vocal, Rhodes, upright bass, "
       "restrained, tense",
       "Chamber instrumental at 64 BPM; a string quartet playing a tight repeating figure with no vibrato, "
       "an upright bass under it, no percussion, one held dissonant chord at the midpoint resolving late; "
       "dry natural mix, strings, upright bass, chamber, tense"),
  dur=8)

# ── BÊN NGUYÊN ──
S("01", "trung 50mm, cao 1m70, cách JUDGE WHITMORE 3m, đặt trong khu xử nhìn chếch lên bục thẩm phán",
  "JUDGE WHITMORE ngồi trên bục thẩm phán ở nửa TRÁI khung, cao hơn hẳn trong khung. JULIAN'S LAWYER đứng ở "
  "nửa PHẢI khung dưới bục, đã đứng dậy khỏi bàn. Hậu cảnh là tường ốp gỗ sồi và hai lá cờ trơn.",
  "JUDGE WHITMORE một tay đặt cạnh chiếc búa gỗ, tay kia lật một trang hồ sơ. "
  "JULIAN'S LAWYER một tay cầm một tập giấy, tay kia cài cúc áo vest.",
  "JUDGE WHITMORE nhìn xuống JULIAN'S LAWYER. JULIAN'S LAWYER nhìn lên bục.",
  "JUDGE WHITMORE — mở phiên bằng giọng của người đã làm việc này ba mươi năm: đều, rõ, không màu mè. "
  "JULIAN'S LAWYER — sẵn sàng: cằm hơi ngẩng, khoé môi phẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN'S LAWYER bước ra khỏi bàn",
  ["JUDGE WHITMORE", "JULIAN'S LAWYER"], "trước bục thẩm phán",
  {"JUDGE WHITMORE": "ngồi trên bục nửa trái khung", "JULIAN'S LAWYER": "đứng dưới bục nửa phải khung"},
  "cách nhau ba mét", {"JUDGE WHITMORE": "một tay cạnh búa gỗ, tay kia lật trang hồ sơ",
                       "JULIAN'S LAWYER": "một tay cầm tập giấy, tay kia cài cúc vest"})
V("01", [0], "trung 50mm · JUDGE WHITMORE NÉT trái trên bục + JULIAN'S LAWYER NÉT phải đứng dưới bục",
  [("JUDGE WHITMORE", "JUDGE WHITMORE"), ("JULIAN'S LAWYER", "JULIAN'S LAWYER")],
  "JUDGE WHITMORE và JULIAN'S LAWYER, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JUDGE WHITMORE lật một trang hồ sơ rồi ngước lên mở phiên",
  [("JUDGE WHITMORE", "even, formal", 0)], [("JULIAN'S LAWYER", "silent, buttoning his jacket")])

S("02", "trung 50mm, cao 1m55, cách JULIAN'S LAWYER 2m4, đặt bên khu xử lấy luật sư nét và JULIAN ngồi sau",
  "JULIAN'S LAWYER đứng ở nửa PHẢI khung giữa khu xử. JULIAN ngồi ở nửa TRÁI khung tại bàn luật sư phía sau ông, "
  "thấy rõ mặt. Hậu cảnh là hàng rào gỗ thấp và các hàng ghế khán giả.",
  "JULIAN'S LAWYER hai tay cầm tập giấy ngang ngực. JULIAN hai tay đan trên mặt bàn.",
  "JULIAN'S LAWYER nhìn lên phía bục thẩm phán ngoài khung. JULIAN nhìn theo luật sư của mình.",
  "JULIAN'S LAWYER — trình bày trơn tru một thứ mình không tin: giọng đều, mắt không dừng lâu ở đâu. "
  "JULIAN — hài lòng: khoé môi kéo nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN'S LAWYER lật sang trang thứ hai",
  ["JULIAN'S LAWYER", "JULIAN"], "giữa khu xử, trước bàn luật sư bên nguyên",
  {"JULIAN'S LAWYER": "đứng giữa khu xử nửa phải khung", "JULIAN": "ngồi bàn luật sư nửa trái khung"},
  "cách nhau hai bước", {"JULIAN'S LAWYER": "một tay cầm tập giấy, tay kia đếm bằng ngón trỏ",
                         "JULIAN": "hai tay đan trên mặt bàn"})
VX("02", "trung 50mm · JULIAN'S LAWYER NÉT phải đứng giữa khu xử + JULIAN NÉT trái ngồi bàn luật sư",
   [("JULIAN'S LAWYER", "JULIAN'S LAWYER"), ("JULIAN", "JULIAN")],
   "JULIAN'S LAWYER và JULIAN, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
   "JULIAN'S LAWYER đếm ra từng ý trên đầu ngón tay",
   [("JULIAN'S LAWYER", "smooth, professional",
     "Your Honor, our position is simple. Adrian Kane sustained catastrophic spinal trauma six months ago. "
     "He is non-ambulatory.")],
   [("JULIAN", "silent, satisfied")])

S("03", "cận-trung 85mm, cao 1m40, cách ADRIAN 1m8, đặt bên bàn bị đơn, hạ thấp lấy ADRIAN nét và MAYA cùng khung",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung ở đầu bàn luật sư bên phải. MAYA ngồi ở nửa PHẢI khung ngay cạnh anh. "
  "Hậu cảnh là hàng rào gỗ thấp và các hàng ghế khán giả mờ.",
  "ADRIAN hai tay đặt trên vành tay vịn, các ngón khép. MAYA một tay đặt lên mép bàn, tay kia trên tập hồ sơ.",
  "Cả hai cùng nhìn về phía người luật sư đang nói ở giữa phòng, ngoài khung.",
  "ADRIAN — nghe người ta mô tả mình như mô tả một tài sản hỏng: mặt hoàn toàn bình, mắt tĩnh. "
  "MAYA — nghe từng chữ và ghi nhớ: mày chau, quai hàm siết. Trong khung KHÔNG có ai khác ngoài hai người.",
  "đúng khoảnh khắc ngay TRƯỚC khi tập hồ sơ trên bàn được mở ra",
  ["ADRIAN_TUTE", "MAYA_TUTE"], "đầu bàn luật sư bên phải",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "MAYA": "ngồi cạnh anh nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "hai tay trên vành tay vịn",
                    "MAYA": "một tay trên mép bàn, tay kia trên tập hồ sơ"})
VX("03", "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải ngồi cạnh · giọng luật sư ngoài khung",
   [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE"), ("JULIAN'S LAWYER", "JULIAN'S LAWYER")],
   "ADRIAN và MAYA rõ mặt. JULIAN'S LAWYER KHÔNG xuất hiện trong khung, chỉ nghe giọng ông vọng tới từ ngoài khung.",
   "ADRIAN và MAYA ngồi nghe, MAYA đặt tay lên tập hồ sơ của mình",
   [("JULIAN'S LAWYER (off-screen, vọng từ giữa phòng qua micro)", "smooth, procedural",
     "He lives alone in an unheated outbuilding. He has no professional care, no medical supervision, "
     "and no capacity to manage a multi-billion dollar estate.")],
   [("ADRIAN", "silent, perfectly still"), ("MAYA", "silent, jaw tightening")])

S("04", "trung 50mm, cao 1m70, cách JUDGE WHITMORE 3m, đặt trong khu xử nhìn chếch lên bục thẩm phán",
  "JUDGE WHITMORE ngồi trên bục ở nửa TRÁI khung. JULIAN đứng ở nửa PHẢI khung, đã đứng dậy khỏi bàn luật sư, "
  "một tay đặt lên mặt bàn trước mình. Hậu cảnh là tường ốp gỗ sồi.",
  "JUDGE WHITMORE một tay đặt trên hồ sơ. JULIAN một tay đặt lên mặt bàn, tay kia cài cúc áo vest.",
  "JUDGE WHITMORE nhìn xuống JULIAN. JULIAN nhìn lên bục.",
  "JUDGE WHITMORE — hỏi thẳng người đứng đơn: giọng đều, mắt sắc. "
  "JULIAN — chuẩn bị sẵn một bài về tình thân: mặt buồn đúng liều, mắt ướt vừa đủ.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN bắt đầu nói",
  ["JUDGE WHITMORE", "JULIAN"], "trước bục thẩm phán",
  {"JUDGE WHITMORE": "ngồi trên bục nửa trái khung", "JULIAN": "đứng dưới bục nửa phải khung"},
  "cách nhau ba mét", {"JUDGE WHITMORE": "một tay đặt trên hồ sơ",
                       "JULIAN": "một tay trên mặt bàn, tay kia cài cúc vest"})
V("04", [2], "trung 50mm · JUDGE WHITMORE NÉT trái trên bục + JULIAN NÉT phải đứng dưới bục",
  [("JUDGE WHITMORE", "JUDGE WHITMORE"), ("JULIAN", "JULIAN")],
  "JUDGE WHITMORE và JULIAN, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JUDGE WHITMORE ngước lên hỏi thẳng người đứng đơn",
  [("JUDGE WHITMORE", "even, direct", 2)], [("JULIAN", "silent, preparing")])

S("05", "cận-trung 85mm, cao 1m55, cách JULIAN 1m7, đặt bên khu xử lấy JULIAN nét và ADRIAN mờ phía sau",
  "JULIAN đứng chính diện chiếm phần lớn khung. Ở nửa PHẢI khung phía sau, thấy ADRIAN ngồi trong xe lăn ở "
  "bàn bên kia, MỜ ngoài vùng nét. Hậu cảnh là hàng rào gỗ thấp và ghế khán giả.",
  "JULIAN một tay đặt lên ngực mình rồi hạ xuống, tay kia bám mép bàn.",
  "JULIAN nhìn lên phía bục thẩm phán ngoài khung, thỉnh thoảng liếc về phía ADRIAN.",
  "JULIAN — người diễn nỗi đau gia đình rất khéo: giọng chùng xuống, mắt ướt, khoé môi trễ.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN quay hẳn mặt về phía ADRIAN",
  ["JULIAN", "ADRIAN_TUTE"], "giữa khu xử, trước bàn luật sư bên nguyên",
  {"JULIAN": "đứng chính diện giữa khung", "ADRIAN": "ngồi xe lăn ở bàn bên kia, mờ ở nửa phải khung"},
  "cách nhau ba mét", {"JULIAN": "một tay đặt lên ngực rồi hạ xuống, tay kia bám mép bàn",
                       "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
VX("05", "cận-trung 85mm · JULIAN NÉT chính diện · ADRIAN mờ ngồi xe lăn ở nửa phải khung",
   [("JULIAN", "JULIAN"), ("ADRIAN", "ADRIAN_TUTE")],
   "JULIAN rõ mặt chính diện. ADRIAN chỉ thấy MỜ ở nửa phải khung, ngồi trong xe lăn, KHÔNG rõ mặt.",
   "JULIAN đặt tay lên ngực mình một nhịp rồi hạ xuống",
   [("JULIAN", "soft, performing grief",
     "Only that this is painful for our family, Your Honor. We love Adrian. But love means admitting when someone "
     "can no longer take care of himself.")],
   [("ADRIAN", "silent, out of focus")])

S("06", "trung 50mm, cao 1m55, cách JULIAN 2m2, đặt bên khu xử lấy JULIAN nét và MAYA cùng khung",
  "JULIAN đứng ở nửa TRÁI khung, đã quay nửa người về phía bàn bên kia. MAYA ngồi ở nửa PHẢI khung tại bàn "
  "luật sư bên phải, đã ngẩng lên nhìn ông. Hậu cảnh là hàng rào gỗ thấp và ghế khán giả.",
  "JULIAN một tay chỉ về phía MAYA rồi hạ xuống. MAYA hai tay đặt phẳng lên tập hồ sơ trước mặt.",
  "JULIAN nhìn về phía bục thẩm phán rồi liếc sang MAYA. MAYA nhìn thẳng vào JULIAN.",
  "JULIAN — đưa ra lá bài mà ông cho là mạnh nhất: giọng nhẹ, mắt liếc. "
  "MAYA — bị chỉ đích danh và không cụp mắt: cằm ngang, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng nói vọng xuống từ trên bục",
  ["JULIAN", "MAYA_TUTE"], "giữa khu xử, giữa hai bàn luật sư",
  {"JULIAN": "đứng nửa trái khung", "MAYA": "ngồi bàn luật sư nửa phải khung"},
  "cách nhau ba mét", {"JULIAN": "một tay chỉ về phía MAYA rồi hạ xuống",
                       "MAYA": "hai tay đặt phẳng lên tập hồ sơ"})
VX("06", "trung 50mm · JULIAN NÉT trái đứng giữa khu xử + MAYA NÉT phải ngồi bàn luật sư",
   [("JULIAN", "JULIAN"), ("MAYA", "MAYA_TUTE")],
   "JULIAN và MAYA, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
   "JULIAN chỉ về phía bàn bên kia rồi hạ tay xuống",
   [("JULIAN", "soft, pointed",
     "He recently married a stranger four days after meeting her. That alone should concern this court.")],
   [("MAYA", "silent, holding his gaze")])

# ── MAYA LÊN TIẾNG ──
S("07", "trung 50mm, cao 1m50, cách MAYA 2m4, đặt trong khu xử lấy MAYA nét và JUDGE WHITMORE trên bục phía sau",
  "MAYA đã đứng dậy khỏi ghế và đứng ở nửa PHẢI khung cạnh bàn luật sư. JUDGE WHITMORE ngồi trên bục ở nửa TRÁI "
  "khung phía sau, cao hơn trong khung. Hậu cảnh là tường ốp gỗ và hai lá cờ trơn.",
  "MAYA hai tay đặt lên mép bàn trước mình. JUDGE WHITMORE một tay đặt trên mặt bục.",
  "MAYA nhìn lên bục thẩm phán. JUDGE WHITMORE nhìn xuống MAYA.",
  "JUDGE WHITMORE — điểm danh người có mặt: giọng đều. "
  "MAYA — đứng dậy đúng lúc được gọi, không sớm không muộn: lưng thẳng, giọng rõ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bắt đầu đọc tên và nghề nghiệp",
  ["MAYA_TUTE", "JUDGE WHITMORE"], "cạnh bàn luật sư bên phải, dưới bục thẩm phán",
  {"MAYA": "đứng cạnh bàn nửa phải khung", "JUDGE WHITMORE": "ngồi trên bục nửa trái khung"},
  "cách nhau bốn mét", {"MAYA": "hai tay đặt lên mép bàn", "JUDGE WHITMORE": "một tay đặt trên mặt bục"})
V("07", [4, 5], "trung 50mm · JUDGE WHITMORE NÉT trái trên bục + MAYA NÉT phải đứng cạnh bàn luật sư",
  [("JUDGE WHITMORE", "JUDGE WHITMORE"), ("MAYA", "MAYA_TUTE")],
  "JUDGE WHITMORE và MAYA, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JUDGE WHITMORE hỏi xuống, MAYA đứng dậy khỏi ghế và đặt hai tay lên mép bàn",
  [("JUDGE WHITMORE", "even, formal", 4), ("MAYA", "clear, steady", 5)])

S("08", "cận-trung 85mm, cao 1m50, cách MAYA 1m7, đặt trong khu xử, lấy MAYA nét và một mảng bục thẩm phán rìa trái",
  "MAYA đứng chính diện chiếm phần lớn khung. Ở rìa TRÁI khung thấy một mảng gỗ của bục thẩm phán và bàn tay "
  "JUDGE WHITMORE đặt trên đó, out nét. Hậu cảnh là hàng ghế khán giả mờ.",
  "MAYA một tay đặt trên tập hồ sơ, tay kia buông dọc thân.",
  "MAYA nhìn thẳng lên bục thẩm phán.",
  "MAYA — người đọc tên và bằng cấp của mình như đọc một dòng bệnh án: giọng rõ, đều, không nhấn.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng phản đối cắt ngang từ bàn bên kia",
  ["MAYA_TUTE", "JUDGE WHITMORE"], "cạnh bàn luật sư bên phải",
  {"MAYA": "đứng chính diện giữa khung", "JUDGE WHITMORE": "một mảng bục và bàn tay ở rìa trái khung"},
  "cách nhau bốn mét", {"MAYA": "một tay trên tập hồ sơ, tay kia buông dọc thân",
                        "JUDGE WHITMORE": "một tay đặt trên mặt bục, ngoài vùng nét"})
V("08", [6, 7], "cận-trung 85mm · MAYA NÉT chính diện · một mảng bục và bàn tay JUDGE WHITMORE rìa trái out nét",
  [("MAYA", "MAYA_TUTE"), ("JUDGE WHITMORE", "JUDGE WHITMORE")],
  "MAYA rõ mặt chính diện. JUDGE WHITMORE chỉ thấy MỘT MẢNG BỤC GỖ và bàn tay ở rìa trái, out nét — "
  "KHÔNG thấy mặt.",
  "MAYA đặt một tay lên tập hồ sơ và đọc tên cùng nghề nghiệp của mình",
  [("JUDGE WHITMORE", "even, formal", 6), ("MAYA", "clear, professional", 7)])

S("09", "trung 50mm, cao 1m70, cách JUDGE WHITMORE 3m, đặt trong khu xử nhìn chếch lên bục",
  "JUDGE WHITMORE ngồi trên bục ở nửa PHẢI khung. JULIAN'S LAWYER đứng ở nửa TRÁI khung dưới bục, một tay giơ lên "
  "xin phát biểu. Hậu cảnh là tường ốp gỗ sồi và một lá cờ trơn.",
  "JULIAN'S LAWYER một tay giơ lên ngang vai. JUDGE WHITMORE một tay đưa ra gạt ngang, lòng bàn tay úp xuống.",
  "JULIAN'S LAWYER nhìn lên bục. JUDGE WHITMORE nhìn xuống ông rồi quay sang phía bàn bên kia, ngoài khung.",
  "JULIAN'S LAWYER — chặn nhân chứng bằng thủ tục: giọng nhanh. "
  "JUDGE WHITMORE — bác trong đúng một giây, không cần suy nghĩ: mặt bình, tay gạt dứt khoát.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN'S LAWYER ngồi xuống lại",
  ["JUDGE WHITMORE", "JULIAN'S LAWYER"], "trước bục thẩm phán",
  {"JUDGE WHITMORE": "ngồi trên bục nửa phải khung", "JULIAN'S LAWYER": "đứng dưới bục nửa trái khung"},
  "cách nhau ba mét", {"JULIAN'S LAWYER": "một tay giơ lên ngang vai",
                       "JUDGE WHITMORE": "một tay đưa ra gạt ngang"})
V("09", [8, 9], "trung 50mm · JULIAN'S LAWYER NÉT trái đứng dưới bục + JUDGE WHITMORE NÉT phải trên bục",
  [("JULIAN'S LAWYER", "JULIAN'S LAWYER"), ("JUDGE WHITMORE", "JUDGE WHITMORE")],
  "JULIAN'S LAWYER và JUDGE WHITMORE, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JULIAN'S LAWYER giơ tay xin phản đối, JUDGE WHITMORE gạt tay bác ngay",
  [("JULIAN'S LAWYER", "quick, procedural", 8), ("JUDGE WHITMORE", "flat, decisive", 9)])

S("10", "cận-trung 85mm, cao 1m50, cách MAYA 1m6, đặt trong khu xử, lấy MAYA nét và ADRIAN ngồi xe lăn rìa phải",
  "MAYA đứng ở giữa khung, tập hồ sơ mở trên mép bàn trước mặt. Ở rìa PHẢI khung thấy ADRIAN ngồi trong xe lăn "
  "cạnh bàn, thấy rõ mặt. Hậu cảnh là hàng rào gỗ thấp và ghế khán giả mờ.",
  "MAYA một tay lần theo một dòng trong tập hồ sơ, tay kia đặt trên mép bàn. ADRIAN hai tay trên vành tay vịn.",
  "MAYA nhìn lên bục thẩm phán ngoài khung. ADRIAN nhìn MAYA.",
  "MAYA — điều dưỡng hồi sức đọc bệnh án cho cả phòng nghe, không một chữ thừa: giọng đều, rõ, chuyên môn. "
  "ADRIAN — nghe người ta nói về cơ thể mình bằng những con số chính xác lần đầu tiên: mắt hơi mở.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA lật sang trang thứ hai của tập hồ sơ",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "cạnh bàn luật sư bên phải",
  {"MAYA": "đứng giữa khung cạnh bàn", "ADRIAN": "ngồi xe lăn rìa phải khung"},
  "sát cạnh nhau", {"MAYA": "một tay lần theo dòng hồ sơ, tay kia trên mép bàn",
                    "ADRIAN": "hai tay trên vành tay vịn"})
VX("10", "cận-trung 85mm · MAYA NÉT giữa khung đứng đọc hồ sơ + ADRIAN NÉT rìa phải ngồi xe lăn",
   [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
   "MAYA và ADRIAN, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
   "MAYA lần ngón tay theo một dòng trong tập hồ sơ và đọc lên",
   [("MAYA", "clinical, clear",
     "Patient is a thirty-four year old male, six months post incomplete spinal injury at T-eleven and T-twelve. "
     "He has partial sensation in both legs and measurable motor response in the right quadriceps.")],
   [("ADRIAN", "silent, eyes widening slightly")])

S("11", "trung 50mm, cao 1m50, cách MAYA 2m2, đặt trong khu xử lấy MAYA nét và JULIAN mờ ở bàn bên kia",
  "MAYA đứng ở nửa PHẢI khung cạnh bàn, tập hồ sơ mở. Ở nửa TRÁI khung phía sau, JULIAN ngồi ở bàn luật sư bên "
  "kia, MỜ ngoài vùng nét. Hậu cảnh là cột nắng qua cửa sổ vòm.",
  "MAYA một tay giơ tập hồ sơ lên ngang ngực, tay kia lật một trang. JULIAN hai tay đan trên mặt bàn.",
  "MAYA nhìn lên bục thẩm phán ngoài khung. JULIAN nhìn về phía MAYA.",
  "MAYA — đọc danh sách thuốc thuộc lòng, không cần nhìn giấy: giọng nhanh, chắc. "
  "JULIAN — bắt đầu thấy phiên toà trượt khỏi tay: khoé môi cứng lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hạ tập hồ sơ xuống",
  ["MAYA_TUTE", "JULIAN"], "cạnh bàn luật sư bên phải",
  {"MAYA": "đứng cạnh bàn nửa phải khung", "JULIAN": "ngồi bàn luật sư bên kia, mờ ở nửa trái khung"},
  "cách nhau ba mét", {"MAYA": "một tay giơ tập hồ sơ ngang ngực, tay kia lật trang",
                       "JULIAN": "hai tay đan trên mặt bàn, ngoài vùng nét"})
VX("11", "trung 50mm · MAYA NÉT phải đứng đọc hồ sơ · JULIAN mờ ngồi bàn luật sư bên kia ở nửa trái khung",
   [("MAYA", "MAYA_TUTE"), ("JULIAN", "JULIAN")],
   "MAYA rõ mặt. JULIAN chỉ thấy MỜ ở nửa trái khung, ngồi tại bàn luật sư bên kia, KHÔNG rõ mặt.",
   "MAYA giơ tập hồ sơ lên ngang ngực và đọc thuộc lòng danh sách thuốc",
   [("MAYA", "fast, exact",
     "His medication list is baclofen ten milligrams three times daily, gabapentin three hundred at night, "
     "and a low dose blood thinner. Blood pressure this morning was one twenty-four over eighty.")],
   [("JULIAN", "silent, out of focus")])

S("12", "cận 85mm, cao 1m50, cách MAYA 1m3, đặt trong khu xử, lấy MAYA nét và một mảng vai ADRIAN rìa phải",
  "MAYA đứng chiếm phần lớn khung từ ngực trở lên, đã hạ tập hồ sơ xuống. Ở rìa PHẢI khung thấy một mảng vai "
  "và tay vịn xe lăn của ADRIAN, out nét. Hậu cảnh là hàng ghế khán giả xoá phông.",
  "MAYA một tay hạ tập hồ sơ xuống mép bàn, tay kia buông.",
  "MAYA nhìn thẳng lên bục thẩm phán.",
  "MAYA — người vừa nói xong phần chuyên môn và chuyển sang phần của con người: giọng chậm lại, "
  "mắt không rời bục, cằm ngẩng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng hỏi về sổ ghi chép vọng xuống từ trên bục",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "cạnh bàn luật sư bên phải",
  {"MAYA": "đứng chính diện giữa khung", "ADRIAN": "một mảng vai và tay vịn xe lăn ở rìa phải"},
  "sát cạnh nhau", {"MAYA": "một tay hạ tập hồ sơ xuống mép bàn, tay kia buông",
                    "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
VX("12", "cận 85mm · MAYA NÉT chính diện · một mảng vai và tay vịn xe lăn ADRIAN rìa phải out nét",
   [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
   "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI và tay vịn xe lăn ở rìa phải, out nét — KHÔNG quay mặt về camera.",
   "MAYA hạ tập hồ sơ xuống mép bàn và nói chậm lại",
   [("MAYA", "slower, weighted",
     "Skin is intact with no pressure ulcers, which after six months is not luck. It is care.")],
   [("ADRIAN", "silent, out of focus")])

S("13", "trung 50mm, cao 1m70, cách JUDGE WHITMORE 3m, đặt trong khu xử nhìn chếch lên bục",
  "JUDGE WHITMORE ngồi trên bục ở nửa TRÁI khung, người hơi chồm tới. MAYA đứng ở nửa PHẢI khung dưới bục, "
  "tập hồ sơ trong tay. Hậu cảnh là tường ốp gỗ sồi và một lá cờ trơn.",
  "JUDGE WHITMORE một tay chống lên mặt bục, người chồm tới. MAYA hai tay giơ tập hồ sơ lên ngang ngực.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JUDGE WHITMORE — lần đầu trong phiên tỏ ra chú ý thật sự: mày nhướn, người chồm tới. "
  "MAYA — đưa ra thứ mình có: giọng rõ, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng luật sư cắt ngang từ bàn bên kia",
  ["JUDGE WHITMORE", "MAYA_TUTE"], "trước bục thẩm phán",
  {"JUDGE WHITMORE": "ngồi trên bục nửa trái khung, chồm tới", "MAYA": "đứng dưới bục nửa phải khung"},
  "cách nhau bốn mét", {"JUDGE WHITMORE": "một tay chống lên mặt bục",
                        "MAYA": "hai tay giơ tập hồ sơ ngang ngực"})
V("13", [11, 12], "trung 50mm · JUDGE WHITMORE NÉT trái trên bục chồm tới + MAYA NÉT phải đứng dưới bục",
  [("JUDGE WHITMORE", "JUDGE WHITMORE"), ("MAYA", "MAYA_TUTE")],
  "JUDGE WHITMORE và MAYA, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JUDGE WHITMORE chồm người tới trước hỏi, MAYA giơ tập hồ sơ lên ngang ngực",
  [("JUDGE WHITMORE", "interested, direct", 11), ("MAYA", "clear, prepared", 12)])

S("14", "trung 50mm, cao 1m55, cách JULIAN'S LAWYER 2m2, đặt bên khu xử lấy luật sư nét và MAYA cùng khung",
  "JULIAN'S LAWYER đứng ở nửa TRÁI khung, đã đứng dậy lần nữa. MAYA đứng ở nửa PHẢI khung cạnh bàn bên kia. "
  "Hậu cảnh là hàng rào gỗ thấp và các hàng ghế khán giả.",
  "JULIAN'S LAWYER một tay chỉ về phía tập hồ sơ trong tay MAYA. MAYA hai tay giữ tập hồ sơ.",
  "Hai người nhìn thẳng vào mắt nhau qua khoảng giữa khu xử.",
  "JULIAN'S LAWYER — đánh vào chỗ yếu nhất của cô: giọng gọn, khoé môi hơi kéo. "
  "MAYA — nhận đòn và không chối: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước một bước ra khỏi bàn",
  ["JULIAN'S LAWYER", "MAYA_TUTE"], "giữa khu xử, giữa hai bàn luật sư",
  {"JULIAN'S LAWYER": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau ba mét", {"JULIAN'S LAWYER": "một tay chỉ về phía tập hồ sơ",
                       "MAYA": "hai tay giữ tập hồ sơ"})
V("14", [13], "trung 50mm · JULIAN'S LAWYER NÉT trái đứng giữa khu xử + MAYA NÉT phải đứng cạnh bàn",
  [("JULIAN'S LAWYER", "JULIAN'S LAWYER"), ("MAYA", "MAYA_TUTE")],
  "JULIAN'S LAWYER và MAYA, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JULIAN'S LAWYER chỉ về phía tập hồ sơ trong tay MAYA",
  [("JULIAN'S LAWYER", "clipped, dismissive", 13)], [("MAYA", "silent, unshaken")])

S("15", "cận-trung 85mm, cao 1m50, cách MAYA 1m6, đặt trong khu xử, lấy MAYA nét và JULIAN'S LAWYER mờ rìa trái",
  "MAYA đứng chính diện chiếm phần lớn khung, đã bước ra khỏi bàn một bước. Ở rìa TRÁI khung thấy JULIAN'S LAWYER "
  "đứng, MỜ ngoài vùng nét. Hậu cảnh là cột nắng qua cửa sổ vòm và ghế khán giả.",
  "MAYA một tay giữ tập hồ sơ ép vào người, tay kia mở ra ngang hông.",
  "MAYA nhìn lên bục thẩm phán ngoài khung.",
  "MAYA — người vừa nhận đòn và lập tức xoay nó thành đường vào: giọng chậm, rõ, mắt sáng lên, "
  "KHÔNG hề gay gắt.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt câu hỏi về chủ sở hữu căn nhà",
  ["MAYA_TUTE", "JULIAN'S LAWYER"], "giữa khu xử, trước bàn luật sư bên phải",
  {"MAYA": "đứng chính diện giữa khung", "JULIAN'S LAWYER": "đứng mờ ở rìa trái khung"},
  "cách nhau ba mét", {"MAYA": "một tay giữ tập hồ sơ, tay kia mở ra ngang hông",
                       "JULIAN'S LAWYER": "hai tay buông, ngoài vùng nét"})
VX("15", "cận-trung 85mm · MAYA NÉT chính diện · JULIAN'S LAWYER mờ ở rìa trái khung",
   [("MAYA", "MAYA_TUTE"), ("JULIAN'S LAWYER", "JULIAN'S LAWYER")],
   "MAYA rõ mặt chính diện. JULIAN'S LAWYER chỉ thấy MỜ ở rìa trái khung, KHÔNG rõ mặt.",
   "MAYA bước ra khỏi bàn một bước và mở bàn tay ra ngang hông",
   [("MAYA", "slow, opening",
     "You are right. So let me tell you about the five months before I got there. His counsel just told this court "
     "that Mr. Kane lives in an unheated building with no ramp.")],
   [("JULIAN'S LAWYER", "silent, out of focus")])

S("16", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt trong khu xử lấy MAYA nét và JULIAN đứng bên kia",
  "MAYA đứng ở nửa PHẢI khung giữa khu xử. JULIAN đứng ở nửa TRÁI khung, đã đứng bật dậy khỏi ghế, một tay "
  "chống lên mặt bàn. Hậu cảnh là bục thẩm phán mờ ở phía sau.",
  "MAYA một tay rút một tờ giấy ra khỏi tập hồ sơ. JULIAN một tay chống mặt bàn, tay kia giơ lên nửa chừng.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — đặt câu hỏi mà cô đã biết câu trả lời: giọng bình, mắt thẳng. "
  "JULIAN — bật dậy vì biết câu tiếp theo là gì: mặt cứng, giọng vội.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA giơ tờ giấy lên",
  ["MAYA_TUTE", "JULIAN"], "giữa khu xử, giữa hai bàn luật sư",
  {"MAYA": "đứng nửa phải khung", "JULIAN": "đứng bật dậy nửa trái khung"},
  "cách nhau ba mét", {"MAYA": "một tay rút một tờ giấy khỏi tập hồ sơ",
                       "JULIAN": "một tay chống mặt bàn, tay kia giơ lên nửa chừng"})
VX("16", "trung 50mm · MAYA NÉT phải giữa khu xử + JULIAN NÉT trái đứng bật dậy khỏi ghế",
   [("MAYA", "MAYA_TUTE"), ("JULIAN", "JULIAN")],
   "MAYA và JULIAN, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
   "MAYA rút một tờ giấy ra khỏi tập hồ sơ, JULIAN bật dậy khỏi ghế",
   [("MAYA", "level, leading", "That is true. Would you like to know who owns that building?"),
    ("JULIAN", "quick, alarmed", "Your Honor."),
    ("MAYA", "even, factual", "Julian Kane does. He signed the transfer. I have the county record.")])

S("17", "cận-trung 85mm, cao 1m50, cách MAYA 1m5, đặt trong khu xử, lấy MAYA nét và JULIAN mờ rìa trái",
  "MAYA đứng chính diện chiếm phần lớn khung, một tờ giấy giơ ngang ngực. Ở rìa TRÁI khung thấy JULIAN đang đứng, "
  "MỜ ngoài vùng nét. Hậu cảnh là hàng ghế khán giả và cột nắng.",
  "MAYA một tay giơ tờ giấy ngang ngực, tay kia nắm hờ bên hông.",
  "MAYA nhìn lên bục thẩm phán ngoài khung.",
  "MAYA — người liệt kê ba việc bằng giọng của một bảng kê, và chính sự bình tĩnh đó mới là đòn: "
  "giọng đều, chậm, mắt thẳng, KHÔNG to tiếng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng phản đối cắt ngang lần nữa",
  ["MAYA_TUTE", "JULIAN"], "giữa khu xử",
  {"MAYA": "đứng chính diện giữa khung", "JULIAN": "đứng mờ ở rìa trái khung"},
  "cách nhau ba mét", {"MAYA": "một tay giơ tờ giấy ngang ngực, tay kia đếm bằng ngón tay",
                       "JULIAN": "hai tay buông, ngoài vùng nét"})
VX("17", "cận-trung 85mm · MAYA NÉT chính diện giơ tờ giấy · JULIAN mờ ở rìa trái khung",
   [("MAYA", "MAYA_TUTE"), ("JULIAN", "JULIAN")],
   "MAYA rõ mặt chính diện. JULIAN chỉ thấy MỜ ở rìa trái khung, KHÔNG rõ mặt.",
   "MAYA giơ tờ giấy lên ngang ngực và đếm ba việc trên đầu ngón tay",
   [("MAYA", "even, damning",
     "This man cut off my husband's heat, took away his ramp, and then came to court and used the cold house "
     "as evidence that he cannot take care of himself.")],
   [("JULIAN", "silent, out of focus")])

S("18", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt bên khu xử lấy cả luật sư và MAYA",
  "JULIAN'S LAWYER đứng ở nửa TRÁI khung, một tay giơ lên. MAYA đứng ở nửa PHẢI khung, tờ giấy đã hạ xuống. "
  "Hậu cảnh là hàng rào gỗ thấp và ghế khán giả.",
  "JULIAN'S LAWYER một tay giơ lên ngang vai. MAYA một tay hạ tờ giấy xuống ngang hông.",
  "Hai người nhìn về phía bục thẩm phán ngoài khung.",
  "JULIAN'S LAWYER — dùng nốt thủ tục cuối cùng mình còn: giọng nhanh, mắt liếc lên bục. "
  "MAYA — trả lời bằng một chữ rồi nói tiếp: mặt bình, giọng chắc.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng búa gỗ vang lên từ trên bục",
  ["JULIAN'S LAWYER", "MAYA_TUTE"], "giữa khu xử, giữa hai bàn luật sư",
  {"JULIAN'S LAWYER": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau ba mét", {"JULIAN'S LAWYER": "một tay giơ lên ngang vai",
                       "MAYA": "một tay hạ tờ giấy xuống ngang hông"})
V("18", [17, 18], "trung 50mm · JULIAN'S LAWYER NÉT trái + MAYA NÉT phải, cả hai đứng giữa khu xử",
  [("JULIAN'S LAWYER", "JULIAN'S LAWYER"), ("MAYA", "MAYA_TUTE")],
  "JULIAN'S LAWYER và MAYA, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JULIAN'S LAWYER giơ tay phản đối, MAYA hạ tờ giấy xuống và nói tiếp",
  [("JULIAN'S LAWYER", "quick, procedural", 17), ("MAYA", "firm, closing", 18)])

S("19", "trung 50mm, cao 1m70, cách JUDGE WHITMORE 2m8, đặt trong khu xử nhìn chếch lên bục thẩm phán",
  "JUDGE WHITMORE ngồi trên bục chiếm phần lớn khung ở nửa TRÁI. Ở nửa PHẢI khung phía dưới thấy JULIAN đứng "
  "cạnh bàn luật sư, thấy rõ mặt. Hậu cảnh là tường ốp gỗ và hai lá cờ trơn.",
  "JUDGE WHITMORE một tay cầm chiếc búa gỗ, tay kia đặt trên hồ sơ. JULIAN hai tay buông dọc thân.",
  "JUDGE WHITMORE nhìn xuống JULIAN. JULIAN nhìn lên bục.",
  "JUDGE WHITMORE — tuyên bằng giọng không cần nhấn mạnh: đều, rõ, dứt khoát. "
  "JULIAN — nghe đơn của mình bị bác: mặt cứng lại, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi chiếc búa gỗ chạm xuống đế",
  ["JUDGE WHITMORE", "JULIAN"], "trước bục thẩm phán",
  {"JUDGE WHITMORE": "ngồi trên bục nửa trái khung", "JULIAN": "đứng cạnh bàn luật sư nửa phải khung"},
  "cách nhau ba mét", {"JUDGE WHITMORE": "một tay cầm búa gỗ, tay kia trên hồ sơ",
                       "JULIAN": "hai tay buông dọc thân"})
V("19", [19], "trung 50mm · JUDGE WHITMORE NÉT trái trên bục cầm búa + JULIAN NÉT phải đứng cạnh bàn luật sư",
  [("JUDGE WHITMORE", "JUDGE WHITMORE"), ("JULIAN", "JULIAN")],
  "JUDGE WHITMORE và JULIAN, cả hai rõ mặt. Người ở hàng ghế khán giả mờ, không ai nhìn vào camera.",
  "JUDGE WHITMORE cầm chiếc búa gỗ lên và tuyên",
  [("JUDGE WHITMORE", "even, final", 19)], [("JULIAN", "silent, jaw tightening")],
  ketclip="Cuối clip, JUDGE WHITMORE gõ búa, mọi người đứng dậy, JULIAN đi vòng qua bàn tới gần chỗ MAYA đứng. "
          "Clip dừng đúng lúc ông dừng chân trước mặt cô.")

S("20", "cận-trung 85mm, cao 1m55, cách MAYA 1m7, đặt giữa khu xử lấy cả hai người đứng đối diện",
  "JULIAN đứng ở nửa TRÁI khung, đã tới sát trước mặt MAYA. MAYA đứng ở nửa PHẢI khung, tập hồ sơ ôm trước ngực. "
  "Hậu cảnh là hàng rào gỗ thấp và ghế khán giả đang vãn người, mờ.",
  "JULIAN một tay cài lại cúc áo vest. MAYA hai tay ôm tập hồ sơ trước ngực.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JULIAN — người vừa thua và đang nói bằng giọng lịch sự nhất của mình: khoé môi kéo lên, mắt lạnh đi. "
  "MAYA — không lùi nửa bước: cằm ngang, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN nói câu cuối",
  ["JULIAN", "MAYA_TUTE"], "giữa khu xử, sau khi phiên toà kết thúc",
  {"JULIAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau một bước", {"JULIAN": "một tay cài lại cúc áo vest", "MAYA": "hai tay ôm tập hồ sơ trước ngực"})
V("20", [20, 21], "cận-trung 85mm · JULIAN NÉT trái + MAYA NÉT phải, đứng đối diện giữa khu xử",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_TUTE")],
  "JULIAN và MAYA, cả hai rõ mặt. Người ở hàng ghế khán giả đang vãn, mờ, không ai nhìn vào camera.",
  "JULIAN đi vòng qua bàn tới trước mặt MAYA và cài lại cúc áo vest",
  [("JULIAN", "smooth, cold", 20), ("MAYA", "flat, unmoving", 21)])

S("21", "cận 85mm, cao 1m55, cách JULIAN 1m3, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "JULIAN đứng chính diện chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng JULIAN là bục thẩm phán đã trống và hai lá cờ trơn.",
  "JULIAN một tay đưa lên chỉnh khăn túi ngực rồi hạ xuống.",
  "JULIAN nhìn thẳng vào mặt MAYA.",
  "JULIAN — người vừa quyết định làm một việc khác và đang báo trước cho cô biết: giọng rất nhẹ, "
  "khoé môi kéo lên, mắt hoàn toàn lạnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN quay lưng bước ra khỏi phòng xử",
  ["JULIAN", "MAYA_TUTE"], "giữa khu xử, sau khi phiên toà kết thúc",
  {"JULIAN": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"JULIAN": "một tay chỉnh khăn túi ngực rồi hạ xuống",
                         "MAYA": "hai tay ôm tập hồ sơ, ngoài vùng nét"})
V("21", [22], "OTS cận 85mm · JULIAN NÉT chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_TUTE")],
  "JULIAN rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "JULIAN chỉnh lại khăn túi ngực và nói rất nhẹ trước khi quay đi",
  [("JULIAN", "soft, threatening", 22)], [("MAYA", "silent, not moving")])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 9m, đặt ở khu xử nhìn về phía cửa gỗ hai cánh cuối phòng",
  "Phòng xử đã vãn, hai bàn luật sư trống, bục thẩm phán không còn ai. MAYA đang đẩy chiếc xe lăn có ADRIAN "
  "ngồi đi dọc lối đi giữa về phía cửa gỗ hai cánh cuối phòng, tập hồ sơ kẹp dưới cánh tay.",
  "MAYA hai tay đẩy xe lăn, tập hồ sơ kẹp dưới cánh tay. ADRIAN hai tay đặt trên vành tay vịn.",
  "Cả hai nhìn thẳng về phía cửa gỗ hai cánh phía trước, KHÔNG ai quay đầu lại.",
  "MAYA — người vừa thắng một phiên toà bằng hai mươi chín ngày ghi chép: vai cân, bước đều, cằm ngang. "
  "ADRIAN — vừa được giữ lại quyền tự quyết về chính mình: lưng thẳng, mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi bánh xe lăn chạm ngưỡng cửa gỗ",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "lối đi giữa phòng xử án, hướng ra cửa",
  {"MAYA": "đẩy xe lăn đi dọc lối đi giữa", "ADRIAN": "ngồi trong xe lăn"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay đẩy xe lăn, tập hồ sơ kẹp dưới cánh tay",
                          "ADRIAN": "hai tay trên vành tay vịn"})
B("B2", "Khép cảnh. Phòng xử đã vãn. MAYA đẩy ADRIAN đi dọc lối đi giữa ra cửa, tập hồ sơ kẹp dưới cánh tay.",
  "toàn cảnh 24mm · MAYA NÉT đẩy xe lăn dọc lối đi giữa + ADRIAN NÉT ngồi trong xe · phòng xử trống phía sau",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN rõ mặt. Phòng xử đã vãn người, không có ai khác rõ mặt trong khung.",
  "hai mươi chín ngày ghi chép vừa thắng cả một hãng luật; và người phụ nữ vừa làm được điều đó đang đẩy "
  "chồng mình ra cửa như mọi ngày, không ai vỗ tay.",
  "MAYA đẩy xe đi đều dọc lối đi trải thảm xanh rêu; cột nắng qua cửa sổ vòm quét ngang hai người một lần; "
  "một cánh cửa gỗ hai cánh phía trước hé mở sẵn.",
  "Ambient tiếng vọng của phòng xử trần cao và tiếng bước chân xa dần, SFX tiếng bánh xe lăn trên thảm và đá hoa.",
  nhac("NÂNG", "Mốc thắng đầu tiên có trọng lượng pháp lý của cả phim — nhạc được phép dâng, nhưng phải rút về mộc vì trận sau còn nặng hơn.",
       "Cinematic folk at 84 BPM; acoustic guitar picking a rising figure, low strings entering underneath after "
       "eight seconds, a female alto singing two lines low and close, one soft kick joining near the end; "
       "the pull is when the strings drop away and only guitar and voice remain; lyrics about winning something "
       "with nothing but a notebook, quiet and unshowy; warm analog mix, female vocal, guitar, strings, hopeful",
       "Cinematic instrumental at 82 BPM; acoustic guitar arpeggio, cello rising underneath, a small string section "
       "swelling once at the midpoint then pulling back to guitar alone, one soft kick in the final bars; "
       "warm analog mix, guitar, cello, strings, hopeful, restrained"),
  dur=8)
