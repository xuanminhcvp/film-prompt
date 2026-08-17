# -*- coding: utf-8 -*-
"""SCENE 18 — PHÒNG NHÂN SỰ ST. AGNES · HÀNH LANG · PHÒNG TRỌ (ngày → đêm)."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S18", "REF_HR_NGAY", qc=qc.S18)
HL = "REF_HANHLANG_NGAY"
TRO = "REF_PHONGTRO_DEM"

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 4m, đặt ở góc phòng nhân sự nhìn về bàn làm việc",
  "HR DIRECTOR ngồi sau bàn làm việc gỗ nhạt, hồ sơ mở trước mặt. MAYA đứng ở giữa phòng trước hai chiếc ghế "
  "khách khung thép, chưa ngồi xuống, vẫn mặc bộ scrub và đeo thẻ nhân viên.",
  "HR DIRECTOR hai tay đặt trên một tập hồ sơ mở. MAYA một tay còn giữ quai chiếc túi đeo vai.",
  "HR DIRECTOR nhìn xuống tập hồ sơ. MAYA nhìn HR DIRECTOR.",
  "HR DIRECTOR — người đã đọc trước kịch bản cuộc gặp này và không muốn nó: mắt không ngẩng lên, quai hàm siết. "
  "MAYA — chưa biết chuyện gì, còn đang vội vì sắp tới ca: mày hơi nhướn.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA ngồi xuống ghế khách",
  ["HR DIRECTOR", "MAYA_SCRUB"], "phòng nhân sự, trước bàn làm việc",
  {"HR DIRECTOR": "ngồi sau bàn làm việc", "MAYA": "đứng trước hai ghế khách"},
  "cách nhau một mặt bàn", {"HR DIRECTOR": "hai tay đặt trên tập hồ sơ mở",
                            "MAYA": "một tay giữ quai chiếc túi đeo vai"})
B("B1", "Mở cảnh. Phòng nhân sự bệnh viện. HR DIRECTOR ngồi sau bàn với một tập hồ sơ mở, MAYA vừa được gọi lên.",
  "trung-rộng 35mm · HR DIRECTOR NÉT ngồi sau bàn + MAYA NÉT đứng trước ghế khách · không có ai khác",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA rõ mặt. Không có người nào khác trong phòng.",
  "một cuộc gặp đã có kết luận từ trước khi người bị gọi lên bước vào phòng.",
  "HR DIRECTOR gấp một góc tập hồ sơ lại rồi mở ra; MAYA đứng lại trước ghế, tay còn trên quai túi; "
  "dải nắng qua cửa sổ chớp lật nằm ngang trên tường sau lưng.",
  "Ambient tiếng ù đèn huỳnh quang và tiếng máy in xa ngoài hành lang, SFX tiếng giấy gấp.",
  nhac("KÌM", "Một người tử tế sắp làm một việc không tử tế vì sợ mất việc; nhạc phải nén y như bà ta đang nén.",
       "Minimal soul at 64 BPM; Rhodes chords placed sparsely over an upright bass, a female alto entering once "
       "with a single line half-spoken; no drums; the pull is a bar of silence before the last chord; lyrics about "
       "a room where somebody has already decided and is only reading it out; dry office mix, female vocal, Rhodes, "
       "restrained, cold",
       "Minimal instrumental at 62 BPM; upright piano playing four notes with no pedal, an upright bass entering "
       "late, one clarinet note held and cut off, no percussion, stopping rather than resolving; "
       "dry office mix, piano, upright bass, clarinet, cold"),
  dur=6)

# ── PHÒNG NHÂN SỰ ──
S("01", "two-shot trung 50mm, cao 1m40, cách MAYA 2m2, đặt bên bàn làm việc lấy cả hai người ngồi",
  "HR DIRECTOR ngồi ở nửa TRÁI khung sau bàn. MAYA ngồi ở nửa PHẢI khung trên ghế khách khung thép, "
  "lưng thẳng, chiếc túi đeo vai đặt trên đùi. Hậu cảnh là cửa gỗ laminate và tủ hồ sơ.",
  "HR DIRECTOR hai tay đan lại trên tập hồ sơ. MAYA hai tay đặt trên chiếc túi trên đùi.",
  "HR DIRECTOR nhìn MAYA. MAYA nhìn lại.",
  "HR DIRECTOR — mở đầu bằng câu đã soạn sẵn: giọng đều, mắt không giữ lâu. "
  "MAYA — còn tưởng đây là chuyện lịch trực: mặt bình, giọng gọn.",
  "đúng khoảnh khắc ngay TRƯỚC khi HR DIRECTOR lật tập hồ sơ sang trang",
  ["HR DIRECTOR", "MAYA_SCRUB"], "hai bên bàn làm việc phòng nhân sự",
  {"HR DIRECTOR": "ngồi sau bàn nửa trái khung", "MAYA": "ngồi ghế khách nửa phải khung"},
  "cách nhau một mặt bàn", {"HR DIRECTOR": "hai tay đan trên tập hồ sơ",
                            "MAYA": "hai tay đặt trên chiếc túi trên đùi"})
V("01", [0, 1], "two-shot trung 50mm · HR DIRECTOR NÉT trái sau bàn + MAYA NÉT phải trên ghế khách",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "HR DIRECTOR chỉ vào ghế khách, MAYA ngồi xuống và đặt chiếc túi lên đùi",
  [("HR DIRECTOR", "even, rehearsed", 0), ("MAYA", "brisk, unsuspecting", 1)])

S("02", "cận-trung 85mm, cao 1m40, cách MAYA 1m6, máy sau vai TRÁI của HR DIRECTOR; vai và gáy bà chiếm rìa trái, out nét",
  "MAYA ngồi chính diện chiếm phần lớn khung trên ghế khách. HR DIRECTOR chỉ còn là vai và gáy ở rìa TRÁI "
  "tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MAYA là cửa gỗ laminate có ô kính vuông.",
  "MAYA một tay siết lấy quai chiếc túi trên đùi.",
  "MAYA nhìn thẳng vào mặt HR DIRECTOR.",
  "MAYA — người vừa nghe hai chữ đình chỉ và đang tính rất nhanh: mày chau, giọng gọn, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi HR DIRECTOR đọc lý do",
  ["MAYA_SCRUB", "HR DIRECTOR"], "hai bên bàn làm việc phòng nhân sự",
  {"MAYA": "ngồi chính diện giữa khung", "HR DIRECTOR": "vai và gáy tiền cảnh trái"},
  "cách nhau một mặt bàn", {"MAYA": "một tay siết quai chiếc túi trên đùi",
                            "HR DIRECTOR": "hai tay trên tập hồ sơ, ngoài vùng nét"})
V("02", [2, 3], "OTS cận-trung 85mm · MAYA NÉT ngồi chính diện · vai và gáy HR DIRECTOR tiền cảnh trái out nét",
  [("MAYA", "MAYA_SCRUB"), ("HR DIRECTOR", "HR DIRECTOR")],
  "MAYA rõ mặt ngồi chính diện. HR DIRECTOR chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA siết lấy quai chiếc túi trên đùi và hỏi lại",
  [("HR DIRECTOR", "flat, formal", 2), ("MAYA", "clipped, alert", 3)])

S("03", "two-shot trung 50mm, cao 1m40, cách MAYA 2m, đặt bên bàn làm việc lấy cả hai người ngồi",
  "HR DIRECTOR ngồi ở nửa TRÁI khung, một tay đặt lên tập hồ sơ mở. MAYA ngồi ở nửa PHẢI khung, người đã "
  "nghiêng tới trước. Hậu cảnh là tường treo ba khung bằng khen và tủ hồ sơ gỗ.",
  "HR DIRECTOR một tay đặt phẳng lên tập hồ sơ như để giữ nó lại. MAYA một tay chỉ vào tập hồ sơ đó.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "HR DIRECTOR — đọc ra một cáo buộc mà chính bà không tin: giọng đều, mắt hạ xuống trang giấy. "
  "MAYA — nghe cụm từ làm giả hồ sơ bệnh án: mặt trắng ra một nhịp rồi cứng lại, giọng nhanh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng nhổm khỏi mặt ghế",
  ["HR DIRECTOR", "MAYA_SCRUB"], "hai bên bàn làm việc phòng nhân sự",
  {"HR DIRECTOR": "ngồi sau bàn nửa trái khung", "MAYA": "ngồi nghiêng tới trước nửa phải khung"},
  "cách nhau một mặt bàn", {"HR DIRECTOR": "một tay đặt phẳng lên tập hồ sơ",
                            "MAYA": "một tay chỉ vào tập hồ sơ"})
V("03", [4, 5, 6], "two-shot trung 50mm · HR DIRECTOR NÉT trái sau bàn + MAYA NÉT phải nghiêng tới trước",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "HR DIRECTOR đặt bàn tay phẳng lên tập hồ sơ, MAYA nghiêng tới trước chỉ vào nó",
  [("HR DIRECTOR", "flat, reading", 4), ("MAYA", "fast, sharpening", 5),
   ("HR DIRECTOR", "evasive, formal", 6)])

S("04", "cận-trung 85mm, cao 1m40, cách MAYA 1m5, đặt bên bàn, lấy MAYA nét và HR DIRECTOR trong khung",
  "MAYA ngồi ở nửa PHẢI khung, đã chồm hẳn tới mép bàn. HR DIRECTOR ngồi ở nửa TRÁI khung, người hơi ngả ra sau. "
  "Hậu cảnh là cửa sổ chớp lật với các dải nắng nằm ngang.",
  "MAYA hai tay đặt lên mép bàn. HR DIRECTOR một tay kéo tập hồ sơ về phía mình.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đòi được xem đúng thứ mà người ta buộc tội mình: giọng chắc, mắt thẳng, KHÔNG gào. "
  "HR DIRECTOR — gọi tên cô một tiếng để xin cô dừng lại: mắt né, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi HR DIRECTOR kéo hẳn tập hồ sơ ra khỏi tầm tay MAYA",
  ["MAYA_SCRUB", "HR DIRECTOR"], "hai bên bàn làm việc phòng nhân sự",
  {"MAYA": "ngồi chồm tới mép bàn nửa phải khung", "HR DIRECTOR": "ngồi ngả ra sau nửa trái khung"},
  "cách nhau một mặt bàn", {"MAYA": "hai tay đặt lên mép bàn",
                            "HR DIRECTOR": "một tay kéo tập hồ sơ về phía mình"})
V("04", [7, 8, 9], "cận-trung 85mm · HR DIRECTOR NÉT trái ngả ra sau + MAYA NÉT phải chồm tới mép bàn",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "MAYA chồm tới đặt hai tay lên mép bàn, HR DIRECTOR kéo tập hồ sơ về phía mình",
  [("MAYA", "firm, demanding", 7), ("HR DIRECTOR", "small, pleading", 8),
   ("MAYA", "steady, pressing", 9)])

S("05", "cận-trung 85mm, cao 1m40, cách HR DIRECTOR 1m6, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "HR DIRECTOR ngồi chính diện chiếm phần lớn khung sau bàn. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, "
  "ngoài vùng nét. Hậu cảnh sau lưng HR DIRECTOR là tường treo ba khung bằng khen.",
  "HR DIRECTOR hai tay rút hẳn khỏi mặt bàn và đặt xuống đùi.",
  "HR DIRECTOR nhìn thẳng vào mặt MAYA rồi hạ mắt xuống.",
  "HR DIRECTOR — người thừa nhận mình không có gì để đưa ra: mắt hạ, quai hàm siết, giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi HR DIRECTOR đổi sang chuyện khoản tài trợ",
  ["HR DIRECTOR", "MAYA_SCRUB"], "hai bên bàn làm việc phòng nhân sự",
  {"HR DIRECTOR": "ngồi chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mặt bàn", {"HR DIRECTOR": "hai tay rút khỏi mặt bàn, đặt xuống đùi",
                            "MAYA": "hai tay trên mép bàn, ngoài vùng nét"})
V("05", [10, 11], "OTS cận-trung 85mm · HR DIRECTOR NÉT ngồi chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR rõ mặt ngồi chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "HR DIRECTOR rút hai tay khỏi mặt bàn và đặt xuống đùi",
  [("HR DIRECTOR", "very quiet, cornered", 10), ("MAYA", "level, pressing", 11)])

S("06", "two-shot trung 50mm, cao 1m40, cách MAYA 2m, đặt bên bàn làm việc lấy cả hai người ngồi",
  "HR DIRECTOR ngồi ở nửa TRÁI khung, đã ngẩng lên. MAYA ngồi ở nửa PHẢI khung, đã ngồi thẳng lại. "
  "Hậu cảnh là cửa gỗ laminate và tủ hồ sơ gỗ bốn ngăn.",
  "HR DIRECTOR một tay xoay chiếc bút bi trên mặt bàn. MAYA hai tay đặt lại trên đùi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "HR DIRECTOR — đưa ra một dữ kiện thay cho câu trả lời và để cô tự ghép: giọng đều, mắt thẳng lần đầu. "
  "MAYA — ghép xong trong một giây: mắt hơi mở, giọng phẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi HR DIRECTOR nhắc lại đúng câu vừa nói",
  ["HR DIRECTOR", "MAYA_SCRUB"], "hai bên bàn làm việc phòng nhân sự",
  {"HR DIRECTOR": "ngồi sau bàn nửa trái khung", "MAYA": "ngồi thẳng lại nửa phải khung"},
  "cách nhau một mặt bàn", {"HR DIRECTOR": "một tay xoay chiếc bút bi trên mặt bàn",
                            "MAYA": "hai tay đặt trên đùi"})
V("06", [12, 13], "two-shot trung 50mm · HR DIRECTOR NÉT trái sau bàn + MAYA NÉT phải ngồi thẳng",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "HR DIRECTOR xoay chiếc bút bi trên mặt bàn và đưa ra một dữ kiện",
  [("HR DIRECTOR", "even, loaded", 12), ("MAYA", "flat, connecting it", 13)])

S("07", "cận 85mm, cao 1m40, cách MAYA 1m2, đặt bên bàn, lấy MAYA nét và một mảng vai HR DIRECTOR rìa trái",
  "MAYA ngồi chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo blazer xám của "
  "HR DIRECTOR, out nét. Hậu cảnh là cửa gỗ laminate xoá phông.",
  "MAYA một tay đặt lên mép bàn, các ngón duỗi ra rất chậm.",
  "MAYA nhìn thẳng vào mặt HR DIRECTOR.",
  "MAYA — người yêu cầu đối phương gọi đúng tên việc mình đang làm: giọng chậm, thấp, mắt không rời, "
  "KHÔNG to tiếng.",
  "đúng khoảnh khắc ngay TRƯỚC khi HR DIRECTOR đứng dậy khỏi ghế xoay",
  ["MAYA_SCRUB", "HR DIRECTOR"], "hai bên bàn làm việc phòng nhân sự",
  {"MAYA": "ngồi chính diện giữa khung", "HR DIRECTOR": "một mảng vai áo blazer ở rìa trái"},
  "cách nhau một mặt bàn", {"MAYA": "một tay đặt lên mép bàn, các ngón duỗi chậm",
                            "HR DIRECTOR": "hai tay trên đùi, ngoài vùng nét"})
V("07", [14, 15], "cận 85mm · MAYA NÉT ngồi chính diện · một mảng vai HR DIRECTOR rìa trái out nét",
  [("MAYA", "MAYA_SCRUB"), ("HR DIRECTOR", "HR DIRECTOR")],
  "MAYA rõ mặt. HR DIRECTOR chỉ thấy MỘT MẢNG VAI áo blazer ở rìa trái, out nét — KHÔNG quay mặt về camera.",
  "MAYA đặt tay lên mép bàn, các ngón duỗi ra rất chậm",
  [("HR DIRECTOR", "flat, repeating", 14), ("MAYA", "slow, demanding", 15)])

S("08", "two-shot trung 50mm, cao 1m40, cách MAYA 2m2, đặt bên bàn làm việc lấy cả hai người",
  "HR DIRECTOR đã đứng dậy và đứng ở nửa TRÁI khung sau bàn. MAYA vẫn ngồi ở nửa PHẢI khung trên ghế khách. "
  "Hậu cảnh là cửa gỗ laminate và mắc áo đứng cạnh cửa.",
  "HR DIRECTOR một tay chống lên mặt bàn, tay kia chỉ về phía cửa. MAYA hai tay đặt trên chiếc túi trên đùi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "HR DIRECTOR — nói ra lý do thật của mình và đó là lý do của một người sợ: giọng nhỏ, mắt ướt, mặt xấu hổ. "
  "MAYA — hiểu và không trách, chỉ hỏi về đường đi ra: mặt bình, giọng thấp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng dậy khỏi ghế",
  ["HR DIRECTOR", "MAYA_SCRUB"], "hai bên bàn làm việc phòng nhân sự",
  {"HR DIRECTOR": "đứng sau bàn nửa trái khung", "MAYA": "ngồi ghế khách nửa phải khung"},
  "cách nhau một mặt bàn", {"HR DIRECTOR": "một tay chống mặt bàn, tay kia chỉ về phía cửa",
                            "MAYA": "hai tay đặt trên chiếc túi trên đùi"})
V("08", [16, 17], "two-shot trung 50mm · HR DIRECTOR NÉT trái đứng sau bàn + MAYA NÉT phải còn ngồi ghế khách",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "HR DIRECTOR đứng dậy, một tay chống mặt bàn, tay kia chỉ về phía cửa",
  [("HR DIRECTOR", "small, ashamed", 16), ("MAYA", "low, steady", 17)])

S("09", "cận-trung 85mm, cao 1m50, cách MAYA 1m6, đặt bên bàn, lấy MAYA nét và HR DIRECTOR cùng khung",
  "MAYA đã đứng dậy và đứng ở nửa PHẢI khung, chiếc túi đeo vai trong tay. HR DIRECTOR đứng ở nửa TRÁI khung "
  "sau bàn, một tay cầm THẺ NHÂN VIÊN vừa nhận. Hậu cảnh là tường treo ba khung bằng khen.",
  "MAYA hai tay đeo lại quai túi lên vai. HR DIRECTOR một tay cầm chiếc thẻ nhân viên, tay kia buông.",
  "MAYA nhìn chiếc thẻ trong tay HR DIRECTOR. HR DIRECTOR nhìn MAYA.",
  "MAYA — người vừa mất việc và đang đeo lại quai túi cho ngay ngắn: mặt bình, tay không run. "
  "HR DIRECTOR — không dám nhìn xuống chiếc thẻ: mắt ướt, môi mím.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước ra phía cửa phòng",
  ["MAYA_SCRUB", "HR DIRECTOR"], "trước bàn làm việc phòng nhân sự",
  {"MAYA": "đứng nửa phải khung", "HR DIRECTOR": "đứng sau bàn nửa trái khung"},
  "cách nhau một mặt bàn", {"MAYA": "hai tay đeo lại quai túi lên vai",
                            "HR DIRECTOR": "một tay cầm chiếc thẻ nhân viên"})
V("09", [18], "cận-trung 85mm · HR DIRECTOR NÉT trái cầm thẻ nhân viên + MAYA NÉT phải đứng đeo túi",
  [("HR DIRECTOR", "HR DIRECTOR"), ("MAYA", "MAYA_SCRUB")],
  "HR DIRECTOR và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "MAYA đeo lại quai túi lên vai, HR DIRECTOR cầm chiếc thẻ nhân viên trong tay",
  [("HR DIRECTOR", "quiet, apologetic", 18)], [("MAYA", "silent, steady")],
  ketclip="Cuối clip, MAYA quay người mở cửa phòng bước ra hành lang. "
          "Clip dừng đúng lúc cô bước qua ngưỡng cửa.")

# ── NHỊP CHUYỂN RA HÀNH LANG ──
S("B2", "trung-rộng 35mm, cao 1m60, cách MAYA 6m, đặt giữa hành lang nhìn về phía sảnh trước",
  "MAYA đi giữa hành lang bệnh viện về phía mảng cửa kính sáng ở cuối, chiếc túi đeo vai, hai tay trống. "
  "Hai bên hành lang là dãy cửa phòng và băng ghế nhựa xanh.",
  "MAYA hai tay buông dọc thân, một tay giữ quai túi.",
  "MAYA nhìn thẳng về phía cửa kính sáng cuối hành lang.",
  "MAYA — người vừa bị lấy mất nghề của mình và đang đi ra bằng chân mình: cằm ngang, vai cân, "
  "mắt đỏ nhưng khô.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng gọi tên cô từ phía sau",
  ["MAYA_SCRUB"], "giữa hành lang bệnh viện, hướng ra sảnh trước",
  {"MAYA": "đi một mình giữa hành lang"}, "một mình trong khung",
  {"MAYA": "hai tay buông dọc thân, một tay giữ quai túi"}, bg=HL)
B("B2", "Nhịp chuyển ra hành lang. MAYA đi một mình giữa hành lang bệnh viện về phía cửa kính sáng.",
  "trung-rộng 35mm · MAYA NÉT đi một mình giữa hành lang · không có ai khác trong khung",
  [("MAYA", "MAYA_SCRUB")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, đi giữa hành lang. Không có người nào khác.",
  "sáu năm ở toà nhà này kết thúc bằng một đoạn hành lang đi ra cửa trước, giữa ban ngày, cho mọi người nhìn.",
  "MAYA đi đều bước, không nhìn hai bên; ánh sáng trắng từ mảng cửa kính cuối hành lang mỗi lúc một mạnh hơn "
  "khi cô tới gần; một xe đẩy dụng cụ inox đứng im sát tường.",
  "Ambient tiếng ù đèn huỳnh quang và tiếng loa thông báo rất xa, SFX tiếng giày y tế trên sàn vinyl.",
  nhac("KÌM", "Nhịp trước cùng phim đã dùng Rhodes; ở đây đổi sang dây kéo, vẫn giữ vai KÌM vì cô đang không cho phép mình gục giữa hành lang.",
       "Soul ballad at 62 BPM with a female alto very close to the mic, dry and worn; a single cello under the voice, "
       "no drums, no bass; one held note at the midpoint then straight back down; lyrics about walking out of the "
       "building you gave six years to, head up; dry intimate mix, female vocal, cello, restrained, sparse",
       "Chamber instrumental at 60 BPM; a solo cello playing a slow descending line, a viola joining a tone below "
       "halfway, no percussion, no build, fading unresolved; very quiet corridor mix, cello, viola, minimal"),
  dur=8)

# ── HÀNH LANG ──
S("10", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt giữa hành lang lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung giữa hành lang, đã dừng bước và quay lại. NURSE DIANE đứng ở nửa TRÁI khung, "
  "vừa chạy tới, một tay còn cầm bìa kẹp bệnh án. Hậu cảnh là dãy cửa phòng và tay vịn inox.",
  "NURSE DIANE một tay cầm bìa kẹp bệnh án, tay kia đưa ra phía MAYA. MAYA một tay giữ quai túi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "NURSE DIANE — vừa thấy bạn mình bị áp giải ra và chưa hiểu gì: mắt mở to, giọng gấp. "
  "MAYA — dừng lại và chuyển ngay sang việc quan trọng nhất: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nắm lấy cổ tay NURSE DIANE",
  ["MAYA_SCRUB", "NURSE DIANE"], "giữa hành lang bệnh viện",
  {"MAYA": "đứng nửa phải khung, đã quay lại", "NURSE DIANE": "đứng nửa trái khung, vừa chạy tới"},
  "cách nhau một bước", {"NURSE DIANE": "một tay cầm bìa kẹp bệnh án, tay kia đưa ra",
                         "MAYA": "một tay giữ quai túi"}, bg=HL)
V("10", [19], "trung 50mm · NURSE DIANE NÉT trái vừa chạy tới + MAYA NÉT phải đã quay lại · hành lang bệnh viện",
  [("NURSE DIANE", "NURSE DIANE"), ("MAYA", "MAYA_SCRUB")],
  "NURSE DIANE và MAYA, cả hai rõ mặt giữa hành lang. Không có ai khác trong khung.",
  "NURSE DIANE chạy tới và đưa tay ra phía MAYA",
  [("NURSE DIANE", "urgent, bewildered", 19)], [("MAYA", "silent, stopping")])

S("11", "cận-trung 85mm, cao 1m55, cách MAYA 1m5, đặt giữa hành lang, lấy MAYA nét và NURSE DIANE cùng khung",
  "MAYA đứng ở nửa PHẢI khung, đã nắm lấy cổ tay NURSE DIANE. NURSE DIANE đứng ở nửa TRÁI khung, thấy rõ mặt. "
  "Hậu cảnh là mảng cửa kính sáng cuối hành lang, xoá phông.",
  "MAYA hai tay nắm lấy cổ tay NURSE DIANE. NURSE DIANE một tay còn cầm bìa kẹp bệnh án.",
  "Hai người nhìn thẳng vào mắt nhau, rất gần.",
  "MAYA — người không nói một chữ nào về mình mà chỉ bàn giao một ca bệnh: giọng nhanh, chính xác, "
  "mắt không rời. NURSE DIANE — nghe bạn mình dặn về gót chân trái của mẹ cô: mắt ướt.",
  "đúng khoảnh khắc ngay TRƯỚC khi NURSE DIANE gọi tên cô lần nữa",
  ["MAYA_SCRUB", "NURSE DIANE"], "giữa hành lang bệnh viện",
  {"MAYA": "đứng nửa phải khung, nắm cổ tay NURSE DIANE", "NURSE DIANE": "đứng nửa trái khung"},
  "rất gần nhau", {"MAYA": "hai tay nắm lấy cổ tay NURSE DIANE",
                   "NURSE DIANE": "một tay cầm bìa kẹp bệnh án"}, bg=HL)
V("11", [20], "cận-trung 85mm · NURSE DIANE NÉT trái + MAYA NÉT phải nắm cổ tay bà · hành lang bệnh viện",
  [("NURSE DIANE", "NURSE DIANE"), ("MAYA", "MAYA_SCRUB")],
  "NURSE DIANE và MAYA, cả hai rõ mặt giữa hành lang. Không có ai khác trong khung.",
  "MAYA nắm chặt lấy cổ tay NURSE DIANE",
  [("MAYA", "fast, precise", 20)], [("NURSE DIANE", "silent, eyes filling")])

S("12", "cận 85mm, cao 1m55, cách MAYA 1m2, đặt giữa hành lang, lấy MAYA nét và một mảng vai NURSE DIANE rìa trái",
  "MAYA đứng chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo scrub xanh mòng két "
  "của NURSE DIANE, out nét. Hậu cảnh là hành lang hun hút và các cửa phòng, xoá phông.",
  "MAYA hai tay nắm lấy hai cổ tay NURSE DIANE.",
  "MAYA nhìn thẳng vào mặt NURSE DIANE.",
  "MAYA — người xin một lời hứa vì đó là thứ duy nhất cô còn có thể xin: giọng vỡ một nhịp rồi vững lại, "
  "mắt ướt, KHÔNG khóc thành tiếng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA buông hai cổ tay ra",
  ["MAYA_SCRUB", "NURSE DIANE"], "giữa hành lang bệnh viện",
  {"MAYA": "đứng chính diện giữa khung", "NURSE DIANE": "một mảng vai áo scrub ở rìa trái"},
  "rất gần nhau", {"MAYA": "hai tay nắm hai cổ tay NURSE DIANE",
                   "NURSE DIANE": "hai tay để yên, ngoài vùng nét"}, bg=HL)
V("12", [21, 22, 23], "cận 85mm · MAYA NÉT chính diện · một mảng vai NURSE DIANE rìa trái out nét",
  [("MAYA", "MAYA_SCRUB"), ("NURSE DIANE", "NURSE DIANE")],
  "MAYA rõ mặt. NURSE DIANE chỉ thấy MỘT MẢNG VAI áo scrub ở rìa trái, out nét — KHÔNG quay mặt về camera.",
  "MAYA nắm lấy cả hai cổ tay NURSE DIANE và xin một lời hứa",
  [("NURSE DIANE", "small, shaken", 21), ("MAYA", "cracking, insistent", 22),
   ("NURSE DIANE", "quiet, promising", 23)])

# ── NHỊP CHUYỂN VỀ PHÒNG TRỌ ──
S("B3", "trung-rộng 35mm, cao 1m50, cách MAYA 4m, đặt ở góc phòng trọ nhìn về phía cửa ra vào",
  "MAYA vừa mở cửa phòng trọ bước vào, một tay còn trên tay nắm cửa, chiếc túi đeo vai. ADRIAN ngồi trong "
  "chiếc xe lăn tay cũ cạnh bàn gỗ tròn giữa phòng, đã quay đầu ra phía cửa. Đèn bàn ở tủ đầu giường đang bật.",
  "MAYA một tay còn trên tay nắm cửa, tay kia giữ quai túi. ADRIAN một tay đặt trên vành bánh xe.",
  "MAYA nhìn vào trong phòng. ADRIAN nhìn ra phía cửa.",
  "MAYA — người đã lau sạch mặt trước khi tra chìa vào ổ: mặt bình, khoé môi kéo lên một chút, mắt còn đỏ. "
  "ADRIAN — nhận ra ngay có gì đó sai: mày hơi chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA khép cánh cửa lại sau lưng",
  ["MAYA_SCRUBKHOAC", "ADRIAN_XELANTAY"], "cửa ra vào phòng trọ, nhìn từ trong phòng",
  {"MAYA": "đứng trong cửa, tay còn trên tay nắm", "ADRIAN": "ngồi xe lăn tay cũ cạnh bàn gỗ tròn"},
  "cách nhau ba mét", {"MAYA": "một tay trên tay nắm cửa, tay kia giữ quai túi",
                       "ADRIAN": "một tay đặt trên vành bánh xe"}, bg=TRO)
B("B3", "Nhịp chuyển về đêm. MAYA mở cửa phòng trọ bước vào, ADRIAN đang ngồi cạnh bàn gỗ tròn quay đầu ra.",
  "trung-rộng 35mm · MAYA NÉT đứng trong cửa + ADRIAN NÉT ngồi xe lăn tay cũ cạnh bàn · không có ai khác",
  [("MAYA", "MAYA_SCRUBKHOAC"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN rõ mặt trong phòng trọ. Không có người nào khác trong khung.",
  "cô đã lau mặt ở hành lang trước khi về tới đây, và trong ba mươi giây tới cô sẽ nói dối lần đầu tiên "
  "trong cả bộ phim.",
  "MAYA đứng lại một nhịp trong cửa rồi khép cửa sau lưng, đặt chiếc túi lên ghế; ADRIAN quay bánh xe "
  "một vòng để xoay người về phía cô; ngoài cửa sổ là đêm, vệt đèn đường cam hắt lên tường.",
  "Ambient tiếng phố đêm rất xa và tiếng tủ lạnh mini chạy, SFX tiếng chìa khoá và tiếng cửa khép.",
  nhac("NGHỈ", "Trước cảnh nói dối, khán giả cần một khoảng thở ấm để thấy được cô đang giấu điều gì.",
       "Ambient soul at 58 BPM; Rhodes chords with long gaps and a female alto humming softly, one short line only "
       "at the end; no drums; the pull is a long silence before that line; lyrics about coming home and deciding "
       "not to say it tonight; dry intimate night mix, female vocal, Rhodes, ambient, warm",
       "Ambient instrumental at 56 BPM; a warm pad breathing slowly, a felt piano placing single notes with heavy "
       "sustain, a faint refrigerator-like hum underneath, no percussion, fading out; extremely soft night mix, "
       "piano, pad, minimal, warm"),
  dur=8)

# ── PHÒNG TRỌ ──
S("13", "two-shot trung 50mm, cao 1m30, cách MAYA 2m, đặt trong phòng trọ, hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung cạnh bàn gỗ tròn, đã bỏ túi xuống ghế. ADRIAN ngồi trong chiếc xe lăn tay cũ ở "
  "nửa TRÁI khung. Hậu cảnh là góc bếp nhỏ và giá úp bát đĩa.",
  "MAYA một tay đặt lên lưng ghế gỗ, tay kia vén tóc ra sau tai. ADRIAN hai tay đặt trên vành bánh xe.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người đếm giờ và biết cô về sớm hơn ba tiếng: giọng bình, mắt dò. "
  "MAYA — nói dối lần đầu tiên trong cả bộ phim và nói rất trơn: khoé môi kéo lên, mắt hơi né một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay sang phía góc bếp",
  ["MAYA_SCRUBKHOAC", "ADRIAN_XELANTAY"], "giữa phòng trọ, cạnh bàn gỗ tròn",
  {"MAYA": "đứng cạnh bàn gỗ tròn nửa phải khung", "ADRIAN": "ngồi xe lăn tay cũ nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay đặt lên lưng ghế gỗ, tay kia vén tóc ra sau tai",
                         "ADRIAN": "hai tay đặt trên vành bánh xe"}, bg=TRO)
V("13", [24, 25], "two-shot trung 50mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn tay cũ + MAYA NÉT phải đứng cạnh bàn",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_SCRUBKHOAC")],
  "ADRIAN và MAYA, cả hai rõ mặt trong phòng trọ. Không có ai khác trong khung.",
  "MAYA đặt tay lên lưng ghế gỗ và vén tóc ra sau tai",
  [("ADRIAN", "quiet, checking", 24), ("MAYA", "light, lying smoothly", 25)])

S("14", "cận-trung 85mm, cao 1m30, cách MAYA 1m5, đặt trong phòng trọ, lấy MAYA nét và ADRIAN trong khung",
  "MAYA đứng ở nửa PHẢI khung, đã quay nửa người về phía góc bếp, một tay với lấy chiếc chảo trên giá. "
  "ADRIAN ngồi trong chiếc xe lăn tay cũ ở nửa TRÁI khung, mặt hướng theo cô.",
  "MAYA một tay với lấy chiếc chảo trên giá, tay kia mở cửa tủ lạnh mini. ADRIAN một tay bám vành bánh xe.",
  "MAYA nhìn vào trong tủ lạnh. ADRIAN nhìn MAYA.",
  "MAYA — người lấp đầy im lặng bằng việc nấu ăn: giọng nhẹ, tay đã bận. "
  "ADRIAN — nhắc lại hai chữ của cô và để nguyên đó, không truy: mặt bình, mắt tĩnh, giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt chiếc chảo lên bếp điện",
  ["MAYA_SCRUBKHOAC", "ADRIAN_XELANTAY"], "góc bếp nhỏ trong phòng trọ",
  {"MAYA": "đứng quay về góc bếp nửa phải khung", "ADRIAN": "ngồi xe lăn tay cũ nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay với chiếc chảo trên giá, tay kia mở cửa tủ lạnh mini",
                         "ADRIAN": "một tay bám vành bánh xe"}, bg=TRO)
V("14", [26, 27], "cận-trung 85mm · ADRIAN NÉT trái ngồi xe lăn tay cũ + MAYA NÉT phải quay về góc bếp",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_SCRUBKHOAC")],
  "ADRIAN và MAYA, cả hai rõ mặt trong phòng trọ. Không có ai khác trong khung.",
  "ADRIAN nhắc lại hai chữ của cô, MAYA với lấy chiếc chảo và mở cửa tủ lạnh mini",
  [("ADRIAN", "very quiet, not pushing", 26), ("MAYA", "light, busy", 27)])
