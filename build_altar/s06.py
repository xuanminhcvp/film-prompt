# -*- coding: utf-8 -*-
"""SCENE 6 — PHÒNG HỘ TỊCH TOÀ THỊ CHÍNH (ban ngày). Bốn phút và một cái tên mới."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S6", "REF_UBND_NGAY", qc=qc.S6)

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 6m, đặt phía sau bàn hộ tịch nhìn ra cửa gỗ hai cánh",
  "MAYA đứng ở giữa phòng hộ tịch, ADRIAN ngồi trong xe lăn ngay bên trái cô, cả hai vừa vào và còn đứng cách bàn "
  "hộ tịch một quãng. Phía sau họ, cạnh cửa gỗ hai cánh, SEBASTIAN đứng lùi hẳn vào tường.",
  "MAYA hai tay nắm nhau trước bụng. ADRIAN hai tay đặt trên vành tay vịn. SEBASTIAN một tay ôm bìa kẹp hồ sơ da nâu.",
  "MAYA và ADRIAN cùng nhìn về phía bàn hộ tịch. SEBASTIAN nhìn về phía cửa gỗ hai cánh sau lưng.",
  "MAYA — người sắp ký giấy kết hôn với một người quen bốn ngày và đang cố coi đây là một thủ tục: cằm ngang, "
  "môi mím. ADRIAN — bình thản như đi làm giấy tờ: mặt tĩnh. SEBASTIAN — cảnh giác: mắt quét ra cửa.",
  "đúng khoảnh khắc ngay TRƯỚC khi cán bộ hộ tịch gọi hai người tới bàn",
  ["MAYA_TUTE", "ADRIAN_TUTE", "SEBASTIAN"], "giữa phòng hộ tịch, trước bàn",
  {"MAYA": "đứng giữa phòng", "ADRIAN": "ngồi xe lăn bên trái MAYA", "SEBASTIAN": "đứng lùi vào tường cạnh cửa"},
  "MAYA sát cạnh ADRIAN, SEBASTIAN cách bốn mét",
  {"MAYA": "hai tay nắm nhau trước bụng", "ADRIAN": "hai tay trên vành tay vịn",
   "SEBASTIAN": "một tay ôm bìa kẹp hồ sơ"})
B("B1", "Mở cảnh. Bốn ngày sau. MAYA và ADRIAN vào phòng hộ tịch toà thị chính, SEBASTIAN đứng lùi cạnh cửa.",
  "trung-rộng 35mm · MAYA NÉT giữa phòng + ADRIAN NÉT ngồi xe lăn bên trái + SEBASTIAN NÉT lùi cạnh cửa",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA, ADRIAN và SEBASTIAN rõ mặt. Không có ai khác trong phòng.",
  "một đám cưới không có hoa, không có khách, không có nhạc — chỉ có một cái bàn gỗ và bốn phút đồng hồ.",
  "MAYA và ADRIAN dừng lại giữa phòng, cô đưa mắt nhìn quanh căn phòng ốp gỗ; SEBASTIAN đứng yên cạnh cửa, "
  "liếc ra ngoài hành lang một lần; bụi bay trong cột nắng qua hai cửa sổ cao.",
  "Ambient tiếng vọng của một công thự cũ, tiếng máy đánh chữ và tiếng bước chân ngoài hành lang.",
  nhac("NGHỈ", "Cảnh này ngắn và khô như thủ tục hành chính; nhạc phải giữ khoảng cách, không được lãng mạn hoá một cuộc hôn nhân trên giấy.",
       "Minimal folk at 62 BPM; one acoustic guitar picking a plain repeating figure with no ornament, a female voice "
       "entering only once with a single short line, half-spoken; no drums, no bass; the pull is the silence after "
       "that line; lyrics about signing a name in a room with no flowers in it; dry mix, female vocal, folk, plain, "
       "unsentimental",
       "Instrumental at 60 BPM; upright piano playing a plain four-note figure with no pedal, a clarinet answering "
       "once low and dry, no percussion, no build, stopping rather than ending; dry office mix, piano, clarinet, "
       "plain, unsentimental"),
  dur=8)

# ── THỦ TỤC ──
S("01", "trung 50mm, cao 1m40, cách MAYA 2m4, đặt bên bàn hộ tịch, hạ thấp để lấy cả người ngồi xe lăn",
  "CLERK ngồi ở nửa TRÁI khung sau bàn gỗ sẫm, cuốn sổ đăng ký bìa da mở trước mặt. MAYA đứng ở nửa PHẢI khung "
  "trước bàn, ADRIAN ngồi trong xe lăn ngay sát bên trái cô, thấp hơn trong khung.",
  "CLERK một tay đặt lên trang sổ đang mở, tay kia cầm bút. MAYA hai tay nắm nhau trước bụng. "
  "ADRIAN hai tay đặt trên vành tay vịn.",
  "CLERK nhìn lần lượt từ MAYA sang ADRIAN. Hai người nhìn lại CLERK.",
  "CLERK — người đã hỏi câu này mười nghìn lần: giọng đều, mắt nhanh. "
  "MAYA — nghe từ ràng buộc pháp lý và nuốt một cái: cằm ngẩng. ADRIAN — trả lời gọn: mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi CLERK đánh dấu vào cuốn sổ",
  ["MAYA_TUTE", "ADRIAN_TUTE", "CLERK"], "hai bên bàn hộ tịch",
  {"CLERK": "ngồi sau bàn nửa trái khung", "MAYA": "đứng trước bàn nửa phải khung",
   "ADRIAN": "ngồi xe lăn sát bên trái MAYA"},
  "cách nhau một mặt bàn", {"CLERK": "một tay trên trang sổ, tay kia cầm bút",
                            "MAYA": "hai tay nắm nhau trước bụng", "ADRIAN": "hai tay trên vành tay vịn"})
V("01", [0, 1, 2], "trung 50mm hạ thấp · CLERK NÉT trái sau bàn + MAYA NÉT phải đứng + ADRIAN NÉT ngồi xe lăn cạnh cô",
  [("CLERK", "CLERK"), ("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "CLERK, MAYA và ADRIAN, cả ba rõ mặt. Không có ai khác trong khung.",
  "CLERK ngước lên khỏi cuốn sổ và hỏi lần lượt hai người",
  [("CLERK", "brisk, formal", 0), ("ADRIAN", "level, clear", 1), ("MAYA", "steady, quiet", 2)])

S("02", "cận-trung 85mm, cao 1m40, cách MAYA 1m8, đặt chếch bên bàn lấy MAYA nét và CLERK trong khung",
  "MAYA đứng ở nửa PHẢI khung, đã cúi xuống ký vào cuốn sổ đăng ký đặt trên bàn. CLERK ngồi ở nửa TRÁI khung, "
  "một tay giữ trang sổ, tay kia chỉ vào chỗ ký thứ hai.",
  "MAYA một tay cầm bút đặt trên trang sổ, tay kia chống lên mép bàn. CLERK một tay giữ trang sổ, tay kia chỉ.",
  "MAYA nhìn xuống trang sổ. CLERK nhìn tay MAYA rồi ngước lên nhìn cô.",
  "MAYA — người vừa ký tên mình vào một chỗ mà cả đời cô hình dung khác hẳn: mắt tập trung, quai hàm siết. "
  "CLERK — hài lòng vì hồ sơ trôi nhanh: khoé môi kéo lên một chút.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhấc bút lên khỏi trang sổ",
  ["MAYA_TUTE", "CLERK"], "hai bên bàn hộ tịch",
  {"MAYA": "cúi xuống ký, nửa phải khung", "CLERK": "ngồi sau bàn nửa trái khung"},
  "cách nhau một mặt bàn", {"MAYA": "một tay cầm bút, tay kia chống mép bàn",
                            "CLERK": "một tay giữ trang sổ, tay kia chỉ chỗ ký"})
V("02", [3, 4, 5], "cận-trung 85mm · MAYA NÉT phải cúi xuống ký + CLERK NÉT trái sau bàn",
  [("MAYA", "MAYA_TUTE"), ("CLERK", "CLERK")],
  "MAYA và CLERK, cả hai rõ mặt. Không có ai khác trong khung.",
  "CLERK hỏi nốt một câu thủ tục rồi chỉ vào hai chỗ ký trên cuốn sổ",
  [("CLERK", "routine, quick", 3), ("MAYA", "quiet, clear", 4), ("CLERK", "pleasant, brisk", 5)])

S("03", "trung 50mm, cao 1m30, cách ADRIAN 2m2, đặt bên bàn hộ tịch, hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung trước bàn, MAYA đứng ngay sau bên phải anh, thấy rõ mặt. "
  "CLERK ngồi ở nửa TRÁI khung sau bàn, tay cầm hai tờ giấy chứng nhận vừa in.",
  "ADRIAN một tay đưa lên ngang ngực, hai ngón giơ ra. MAYA một tay đặt lên lưng ghế xe lăn. "
  "CLERK hai tay cầm hai tờ giấy chứng nhận.",
  "ADRIAN nhìn thẳng vào CLERK. MAYA nhìn ADRIAN. CLERK nhìn ADRIAN.",
  "ADRIAN — người trả lời một câu thủ tục nhưng kèm theo một chi tiết cố ý: giọng đều, mắt thẳng. "
  "MAYA — nghe hai chữ vợ tôi lần đầu tiên trong đời: mắt chớp một cái, môi hé. CLERK — gật, ghi chú.",
  "đúng khoảnh khắc ngay TRƯỚC khi CLERK đưa một tờ chứng nhận sang phía MAYA",
  ["ADRIAN_TUTE", "MAYA_TUTE", "CLERK"], "trước bàn hộ tịch",
  {"ADRIAN": "ngồi xe lăn nửa phải khung", "MAYA": "đứng sau bên phải ADRIAN",
   "CLERK": "ngồi sau bàn nửa trái khung"},
  "MAYA sát cạnh ADRIAN, CLERK cách một mặt bàn",
  {"ADRIAN": "một tay đưa ra phía quầy, lòng bàn tay ngửa", "MAYA": "một tay đặt lên lưng ghế xe lăn",
   "CLERK": "hai tay cầm hai tờ giấy chứng nhận"})
V("03", [6, 7, 8], "trung 50mm hạ thấp · ADRIAN NÉT phải ngồi xe lăn + MAYA NÉT đứng sau anh + CLERK NÉT trái sau bàn",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE"), ("CLERK", "CLERK")],
  "ADRIAN, MAYA và CLERK, cả ba rõ mặt. Không có ai khác trong khung.",
  "MAYA cảm ơn, CLERK cầm hai tờ chứng nhận vừa in lên hỏi, ADRIAN đưa tay ra phía quầy",
  [("MAYA", "quiet, polite", 6), ("CLERK", "routine, helpful", 7), ("ADRIAN", "level, deliberate", 8)])

S("04", "cận-trung 85mm, cao 1m40, cách MAYA 1m6, đặt chếch bên, lấy MAYA nét và ADRIAN trong khung",
  "MAYA đứng ở nửa PHẢI khung, đã quay nửa người về phía cửa gỗ hai cánh phía sau. ADRIAN ngồi trong xe lăn "
  "ở nửa TRÁI khung, không quay đầu lại. Hậu cảnh là góc phòng và một phần cửa gỗ hai cánh.",
  "MAYA một tay cầm tờ giấy chứng nhận đã gấp đôi, tay kia đặt lên lưng ghế xe lăn. "
  "ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn về phía cửa gỗ hai cánh phía sau. ADRIAN nhìn thẳng về phía trước, không quay đầu.",
  "MAYA — người vừa để ý thấy một người lạ đang chụp ảnh mình và thấy sai sai: mày chau, giọng hạ thấp. "
  "ADRIAN — biết chuyện đó từ trước: mặt hoàn toàn không đổi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay hẳn người về phía cửa",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "trước bàn hộ tịch",
  {"MAYA": "đứng nửa phải khung, quay nửa người về cửa", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay cầm tờ chứng nhận gấp đôi, tay kia trên lưng ghế xe lăn",
                    "ADRIAN": "hai tay trên vành tay vịn"})
V("04", [9, 10], "cận-trung 85mm · MAYA NÉT phải quay nửa người về cửa + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA hạ giọng nói vào tai ADRIAN mà mắt vẫn nhìn về phía cửa",
  [("MAYA", "low, alert", 9), ("ADRIAN", "flat, unsurprised", 10)])

S("05", "two-shot cận-trung 85mm, cao 1m30, cách MAYA 1m8, máy hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã cúi người xuống ngang tai ADRIAN. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. "
  "Hậu cảnh là bàn hộ tịch và dãy tủ hồ sơ gỗ.",
  "MAYA một tay chống lên lưng ghế xe lăn, tay kia còn cầm tờ chứng nhận. ADRIAN một tay nhấc lên khỏi vành tay vịn.",
  "MAYA nhìn ADRIAN. ADRIAN nhìn thẳng về phía trước rồi quay sang nhìn cô.",
  "MAYA — người vừa nhận ra người kia là luật sư chứ không phải phóng viên: mắt hơi nheo, giọng nhanh. "
  "ADRIAN — gọi tên trợ lý mà không cần nhìn ra sau: mặt bình, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người từ phía cửa bước tới cạnh xe lăn",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "trước bàn hộ tịch",
  {"MAYA": "đứng cúi người nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay chống lưng ghế xe lăn, tay kia cầm tờ chứng nhận",
                    "ADRIAN": "một tay nhấc lên khỏi vành tay vịn"})
V("05", [11, 12], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải cúi xuống + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA cúi xuống ngang tai ADRIAN nói nhanh, ADRIAN gọi tên trợ lý mà không quay đầu",
  [("MAYA", "quick, low", 11), ("ADRIAN", "quiet, level", 12)],
  ketclip="Cuối clip, SEBASTIAN từ chỗ đứng cạnh cửa bước tới và dừng lại ngay sau lưng chiếc xe lăn. "
          "Clip dừng đúng lúc ông dừng chân.")

S("06", "trung 50mm, cao 1m40, cách SEBASTIAN 2m, đặt chếch bên lấy cả ba người",
  "SEBASTIAN đứng ở nửa TRÁI khung ngay sau lưng chiếc xe lăn, bìa kẹp hồ sơ da nâu đã mở trên cẳng tay. "
  "ADRIAN ngồi trong xe lăn ở giữa khung phía trước ông. MAYA đứng ở nửa PHẢI khung, quay mặt về phía SEBASTIAN.",
  "SEBASTIAN một tay đỡ bìa kẹp hồ sơ đã mở, tay kia chỉ vào một dòng ghi trong đó. ADRIAN hai tay trên vành tay vịn. "
  "MAYA một tay cầm tờ chứng nhận ép vào ngực.",
  "SEBASTIAN nhìn xuống ADRIAN khi báo cáo. ADRIAN nhìn thẳng phía trước. MAYA nhìn SEBASTIAN.",
  "SEBASTIAN — người đã ghi xong biển số trước cả khi được hỏi: giọng gọn, nghề nghiệp. "
  "ADRIAN — nghe và không phản ứng: mặt bình. MAYA — nghe một câu cho thấy quanh mình có cả một bộ máy: mắt mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN gập bìa kẹp hồ sơ lại",
  ["SEBASTIAN", "ADRIAN_TUTE", "MAYA_TUTE"], "trước bàn hộ tịch",
  {"SEBASTIAN": "đứng sau lưng xe lăn nửa trái khung", "ADRIAN": "ngồi xe lăn giữa khung",
   "MAYA": "đứng nửa phải khung"},
  "SEBASTIAN sát sau xe lăn, MAYA cách một bước",
  {"SEBASTIAN": "một tay đỡ bìa hồ sơ mở, tay kia chỉ vào một dòng",
   "ADRIAN": "hai tay trên vành tay vịn", "MAYA": "một tay ép tờ chứng nhận vào ngực"})
V("06", [13], "trung 50mm · SEBASTIAN NÉT trái đứng sau xe lăn + ADRIAN NÉT giữa ngồi xe lăn + MAYA NÉT phải",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "SEBASTIAN, ADRIAN và MAYA, cả ba rõ mặt. Không có ai khác trong khung.",
  "SEBASTIAN mở bìa kẹp hồ sơ và báo cáo xuống phía chiếc xe lăn",
  [("SEBASTIAN", "crisp, professional", 13)],
  [("ADRIAN", "silent, unmoved"), ("MAYA", "silent, eyes widening")])

S("07", "cận-trung 85mm, cao 1m40, cách MAYA 1m6, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. ADRIAN chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngồi thấp, "
  "ngoài vùng nét. Hậu cảnh sau lưng MAYA là cửa gỗ hai cánh và băng ghế chờ.",
  "MAYA một tay chỉ nhanh về phía cửa gỗ hai cánh rồi hạ xuống.",
  "MAYA nhìn thẳng xuống mặt ADRIAN.",
  "MAYA — người vừa đặt đúng câu hỏi mà hợp đồng cấm cô hỏi: mày chau, giọng nhanh, mắt dò xét.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN nhắc tới điều khoản ba",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "trước bàn hộ tịch",
  {"MAYA": "đứng chính diện giữa khung", "ADRIAN": "vai và gáy tiền cảnh trái, ngồi thấp"},
  "sát cạnh nhau", {"MAYA": "một tay chỉ về phía cửa rồi hạ xuống",
                    "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
V("07", [14, 15], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA rõ mặt chính diện. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, ngồi thấp, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA chỉ nhanh về phía cửa rồi hạ tay xuống và hỏi",
  [("MAYA", "quick, probing", 14), ("ADRIAN", "flat, closing", 15)])

S("08", "two-shot trung 50mm, cao 1m30, cách MAYA 2m, máy hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, hai tay khoanh lại trước ngực, tờ chứng nhận kẹp trong khuỷu tay. ADRIAN ngồi trong "
  "xe lăn ở nửa TRÁI khung. Hậu cảnh là bàn hộ tịch và cửa sổ cao có nắng.",
  "MAYA hai tay khoanh trước ngực, tờ chứng nhận kẹp trong khuỷu tay. ADRIAN hai tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đọc lại đúng điều khoản mình đã ký để cho thấy mình nhớ: giọng đều, khoé môi hơi kéo. "
  "ADRIAN — xác nhận bằng một chữ: mặt bình, mắt hơi dịu.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nói ra cái tên mới của mình",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "trước bàn hộ tịch",
  {"MAYA": "đứng khoanh tay nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay khoanh trước ngực, tờ chứng nhận kẹp trong khuỷu tay",
                    "ADRIAN": "hai tay trên vành tay vịn"})
V("08", [16, 17, 18], "two-shot trung 50mm hạ thấp · MAYA NÉT phải khoanh tay + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA khoanh tay lại và đọc thuộc lòng điều khoản, rồi nói thêm một câu",
  [("MAYA", "even, pointed", 16), ("ADRIAN", "quiet, plain", 17), ("MAYA", "dry, testing", 18)])

S("09", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m5, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng ADRIAN là dãy tủ hồ sơ gỗ và tấm bản đồ tường.",
  "ADRIAN một tay gõ nhẹ hai lần lên vành tay vịn rồi dừng.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người vừa để lọt ra một chi tiết mà mình không định nói, và đóng lại ngay: mắt hơi dời đi một nhịp "
  "rồi trở lại, giọng nhỏ hơn.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi lại chín ngày là chín ngày gì",
  ["ADRIAN_TUTE", "MAYA_TUTE"], "trước bàn hộ tịch",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "sát cạnh nhau", {"ADRIAN": "một tay gõ nhẹ hai lần lên vành tay vịn",
                    "MAYA": "hai tay khoanh trước ngực, ngoài vùng nét"})
V("09", [19, 20, 21], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "ADRIAN gõ nhẹ hai lần lên vành tay vịn rồi để lọt ra một chi tiết, và đóng lại ngay",
  [("ADRIAN", "quiet, slipping", 19), ("MAYA", "quick, curious", 20), ("ADRIAN", "flat, closing", 21)])

S("10", "two-shot cận-trung 85mm, cao 1m30, cách MAYA 1m8, máy hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã bước vòng ra sau chiếc xe lăn và đặt hai tay lên tay đẩy. ADRIAN ngồi ở nửa TRÁI "
  "khung, mặt quay chếch lên về phía cô. Hậu cảnh là cửa gỗ hai cánh đang khép.",
  "MAYA hai tay đặt lên hai tay đẩy phía sau lưng ghế xe lăn. ADRIAN một tay đặt trên vành tay vịn, tay kia buông.",
  "MAYA nhìn xuống ADRIAN. ADRIAN ngước lên nhìn MAYA.",
  "MAYA — người vừa tìm được cách duy nhất để chịu đựng chuyện này là biến nó thành một câu đùa: "
  "khoé môi kéo lệch, mắt sáng lên lần đầu trong cảnh. ADRIAN — nhận câu đùa và trả lại đúng nhịp: mắt dịu hẳn.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đẩy chiếc xe lăn tiến lên",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "trước bàn hộ tịch, MAYA đã ra sau xe lăn",
  {"MAYA": "đứng sau xe lăn nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát nhau", {"MAYA": "hai tay đặt lên tay đẩy xe lăn",
               "ADRIAN": "một tay trên vành tay vịn, tay kia buông"})
V("10", [22, 23], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải đứng sau xe lăn + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA bước vòng ra sau xe lăn, đặt hai tay lên tay đẩy và nói xuống",
  [("MAYA", "dry, amused", 22), ("ADRIAN", "quiet, amused", 23)],
  ketclip="Cuối clip, MAYA đẩy chiếc xe lăn đi về phía cửa gỗ hai cánh, SEBASTIAN mở sẵn một cánh cửa cho hai người. "
          "Clip dừng đúng lúc bánh xe lăn qua ngưỡng cửa.")

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 8m, đặt phía bàn hộ tịch nhìn ra cửa gỗ hai cánh",
  "MAYA đẩy chiếc xe lăn có ADRIAN ngồi đi ngang qua phòng về phía cửa gỗ hai cánh đang mở. SEBASTIAN đứng giữ "
  "một cánh cửa, người hơi nghiêng. Phòng hộ tịch rộng phía sau họ, bàn hộ tịch đã không còn ai.",
  "MAYA hai tay đẩy xe lăn. ADRIAN hai tay đặt trên vành tay vịn. SEBASTIAN một tay giữ cánh cửa gỗ.",
  "MAYA và ADRIAN cùng nhìn về phía cửa. SEBASTIAN nhìn ra hành lang phía ngoài.",
  "MAYA — người vừa đổi họ trong bốn phút và chưa kịp nghĩ về điều đó: mặt bình, mắt mở. "
  "ADRIAN — mặt tĩnh. SEBASTIAN — cảnh giác, mắt quét ra ngoài hành lang.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả ba người khuất sau cánh cửa",
  ["MAYA_TUTE", "ADRIAN_TUTE", "SEBASTIAN"], "lối ra cửa gỗ hai cánh phòng hộ tịch",
  {"MAYA": "đẩy xe lăn về phía cửa", "ADRIAN": "ngồi trong xe lăn", "SEBASTIAN": "đứng giữ cánh cửa"},
  "MAYA sát sau ADRIAN, SEBASTIAN cách hai mét",
  {"MAYA": "hai tay đẩy xe lăn", "ADRIAN": "hai tay trên vành tay vịn", "SEBASTIAN": "một tay giữ cánh cửa"})
B("B2", "Khép cảnh. Bốn phút và xong. MAYA đẩy xe lăn ra khỏi phòng hộ tịch, SEBASTIAN giữ cửa.",
  "toàn cảnh 24mm · MAYA NÉT đẩy xe lăn + ADRIAN NÉT ngồi trong xe + SEBASTIAN NÉT giữ cánh cửa",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA, ADRIAN và SEBASTIAN rõ mặt. Không có ai khác trong khung.",
  "một cuộc hôn nhân vừa được lập ra trong bốn phút bằng hai chữ ký; không ai trong ba người có vẻ vừa dự "
  "một đám cưới.",
  "MAYA đẩy xe lăn đi đều qua phòng; SEBASTIAN giữ cánh cửa và liếc ra hành lang; cột nắng qua cửa sổ cao "
  "quét ngang người họ một lần rồi thôi.",
  "SFX tiếng bánh xe lăn trên nền đá hoa và tiếng bản lề cửa gỗ, Ambient tiếng bước chân vọng ngoài hành lang.",
  nhac("NGHỈ", "Nhịp trước cùng scene đã là guitar mộc; nhịp này đổi sang dây kéo và giữ vai NGHỈ để cả cảnh vẫn khô như một thủ tục.",
       "Chamber folk at 66 BPM; a viola playing a simple rising figure, an acoustic guitar answering underneath, "
       "a female voice entering only at the very end with one line half-spoken; no drums; the pull is when the viola "
       "stops mid-phrase; lyrics about walking out of a building married to a stranger; dry mix, female vocal, "
       "viola, folk, plain",
       "Chamber instrumental at 64 BPM; viola and cello trading a simple four-note figure over a quiet guitar, "
       "no percussion, one long held note near the end then stopping rather than resolving; "
       "dry natural mix, viola, cello, guitar, plain, open"),
  dur=8)
