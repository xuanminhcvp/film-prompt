# -*- coding: utf-8 -*-
"""SCENE 15 — BÃI XE TOÀ ÁN (chiều mưa). Lần đầu anh gọi tên cô."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S15", "REF_BAIXETOA_CHIEU", qc=qc.S15)

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 5m, đặt dưới mái che nhìn ra bãi xe ướt",
  "MAYA đứng dưới mép mái che tôn, một tay còn giữ tập hồ sơ ép vào ngực. ADRIAN ngồi trong xe lăn ngay cạnh cô, "
  "đã ra khỏi cửa hông toà án và dừng ở đầu dốc bê tông. Ngoài mái che, mưa rơi thành sợi trên mặt bãi ướt bóng.",
  "MAYA một tay ôm tập hồ sơ, tay kia đặt trên tay đẩy xe lăn. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn ra màn mưa ngoài mái che. ADRIAN nhìn theo hướng đó.",
  "MAYA — người vừa thắng một phiên toà và chưa kịp thấy gì: mặt trống, hơi thở còn nhanh. "
  "ADRIAN — nhìn cô nhiều hơn nhìn mưa: mắt hơi nheo lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN cất tiếng gọi tên cô",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che, cạnh cửa hông toà án",
  {"MAYA": "đứng dưới mép mái che", "ADRIAN": "ngồi xe lăn ở đầu dốc bê tông"},
  "sát cạnh nhau", {"MAYA": "một tay ôm tập hồ sơ, tay kia trên tay đẩy xe lăn",
                    "ADRIAN": "hai tay trên vành tay vịn"})
B("B1", "Mở cảnh. Ngay sau phiên toà, dưới mái che bãi xe. Mưa rơi, hai người dừng lại ở đầu dốc.",
  "trung-rộng 35mm · MAYA NÉT đứng dưới mép mái che + ADRIAN NÉT ngồi xe lăn ở đầu dốc · không có ai khác",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN rõ mặt dưới mái che. Không có người nào khác trong khung.",
  "hai người vừa ra khỏi một căn phòng mà ở đó người ta cố tách họ khỏi nhau, và bây giờ chỉ có mưa và "
  "một bãi xe trống.",
  "MAYA thở ra một hơi dài; nước từ mép mái tôn nhỏ thành hàng giọt trước mặt hai người; ADRIAN quay đầu "
  "nhìn cô; đèn cao áp trên cột bật sáng sớm.",
  "Ambient tiếng mưa đều trên mái tôn và tiếng nước chảy xuống rãnh, SFX tiếng giọt nước rơi trên mặt bê tông.",
  nhac("NGHỈ", "Sau trận đánh trong phòng xử, cả hai cần một khoảng lặng — nhạc chỉ được là tiếng mưa có giai điệu.",
       "Ambient soul at 58 BPM; Rhodes chords placed far apart with heavy reverb, a female alto humming once, "
       "then one short line very close to the mic; no drums; the pull is a long gap filled only by rain-like noise; "
       "lyrics about standing under a roof edge with somebody you barely know; dry intimate mix, female vocal, "
       "Rhodes, ambient, wet",
       "Ambient instrumental at 56 BPM; a warm pad and a felt piano trading single notes with long gaps, "
       "a faint rain-like texture underneath, no percussion, thinning out to nothing; "
       "soft rainy mix, piano, pad, minimal, still"),
  dur=8)

# ── DƯỚI MÁI CHE ──
S("01", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m6, đặt bên xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, đã ngước lên. MAYA đứng ở nửa PHẢI khung cạnh anh, đã quay đầu xuống. "
  "Hậu cảnh là màn mưa ngoài mái che và hàng xe ướt bóng.",
  "ADRIAN một tay hơi nhấc lên khỏi vành tay vịn. MAYA một tay ôm tập hồ sơ, tay kia rời khỏi tay đẩy.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người vừa gọi tên cô lần đầu tiên và biết mình vừa làm gì: giọng rất nhỏ, mắt không dời. "
  "MAYA — nhận ra ngay chi tiết đó: mày nhướn, khoé môi động một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hạ tập hồ sơ xuống",
  ["ADRIAN_TUTE", "MAYA_TUTE"], "đầu dốc bê tông dưới mái che",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay nhấc lên khỏi vành tay vịn",
                    "MAYA": "một tay ôm tập hồ sơ, tay kia buông"})
V("01", [0, 1], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải đứng cạnh",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN và MAYA, cả hai rõ mặt dưới mái che. Không có ai khác trong khung.",
  "ADRIAN ngước lên gọi tên cô, MAYA quay đầu xuống nhìn anh",
  [("ADRIAN", "quiet, careful", 0), ("MAYA", "surprised, dry", 1)])

S("02", "trung 50mm, cao 1m30, cách MAYA 2m, đặt dưới mái che, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã hạ tập hồ sơ xuống ngang hông. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. "
  "Hậu cảnh là cột thép xanh rêu đỡ mái che và mặt bãi ướt phản chiếu đèn.",
  "MAYA một tay cầm tập hồ sơ hạ xuống ngang hông, tay kia gạt một sợi tóc ướt khỏi trán. "
  "ADRIAN hai tay đặt trên vành tay vịn.",
  "ADRIAN nhìn MAYA. MAYA nhìn ra màn mưa rồi quay lại nhìn anh.",
  "ADRIAN — người đang liệt kê những việc cô làm mà hợp đồng không yêu cầu: giọng đều, mắt không rời. "
  "MAYA — gạt đi bằng một câu rất thật: khoé môi kéo lệch, mắt hơi né.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA khoanh tay lại",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che",
  {"MAYA": "đứng nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay cầm tập hồ sơ hạ ngang hông, tay kia gạt tóc ướt",
                    "ADRIAN": "hai tay trên vành tay vịn"})
V("02", [2, 3], "trung 50mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải đứng cạnh",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN và MAYA, cả hai rõ mặt dưới mái che. Không có ai khác trong khung.",
  "MAYA gạt một sợi tóc ướt khỏi trán và trả lời gọn",
  [("ADRIAN", "even, observing", 2), ("MAYA", "dry, deflecting", 3)])

S("03", "cận-trung 85mm, cao 1m30, cách MAYA 1m5, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, hai tay đã khoanh trước ngực. ADRIAN chỉ còn là vai và gáy ở rìa "
  "TRÁI tiền cảnh, ngồi thấp, ngoài vùng nét. Hậu cảnh là màn mưa và hàng xe đỗ ướt.",
  "MAYA hai tay khoanh trước ngực, tập hồ sơ kẹp trong khuỷu tay.",
  "MAYA nhìn thẳng xuống mặt ADRIAN.",
  "MAYA — người thừa nhận đã làm một việc ngoài phận sự và không thấy có gì to tát: giọng bình, "
  "khoé môi kéo một chút, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN hỏi câu tiếp theo",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che",
  {"MAYA": "đứng chính diện giữa khung", "ADRIAN": "vai và gáy tiền cảnh trái, ngồi thấp"},
  "sát cạnh nhau", {"MAYA": "hai tay khoanh trước ngực, tập hồ sơ kẹp trong khuỷu tay",
                    "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
V("03", [4, 5], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA rõ mặt chính diện. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, ngồi thấp, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA khoanh hai tay trước ngực và trả lời",
  [("ADRIAN", "even, probing", 4), ("MAYA", "plain, unbothered", 5)])

S("04", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m5, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng ADRIAN là cửa hông toà án bằng gỗ sẫm và bậc đá ướt.",
  "ADRIAN một tay siết nhẹ vành tay vịn rồi thả ra.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người đang đi vòng quanh một câu hỏi mà mình sợ câu trả lời: giọng chậm, mắt tĩnh, "
  "hơi thở sâu hơn bình thường.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN hỏi vì sao",
  ["ADRIAN_TUTE", "MAYA_TUTE"], "đầu dốc bê tông dưới mái che",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "sát cạnh nhau", {"ADRIAN": "một tay siết nhẹ vành tay vịn rồi thả ra",
                    "MAYA": "hai tay khoanh trước ngực, ngoài vùng nét"})
V("04", [6, 7], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "ADRIAN siết nhẹ vành tay vịn rồi thả ra",
  [("ADRIAN", "slow, careful", 6), ("MAYA", "flat, plain", 7)])

S("05", "two-shot trung 50mm, cao 1m30, cách MAYA 1m9, đặt dưới mái che, hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã hạ hai tay xuống. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, mặt ngước lên. "
  "Hậu cảnh là màn mưa ngoài mái che, hàng xe ướt và một vũng nước phản chiếu.",
  "MAYA hai tay buông xuống, một tay còn cầm tập hồ sơ. ADRIAN hai tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — hỏi thẳng bằng hai chữ: giọng rất nhỏ, mắt không dời. "
  "MAYA — trả lời bằng thứ đơn giản nhất và vì thế nặng nhất: giọng đều, mắt thẳng, không nghẹn.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN cụp mắt xuống",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che",
  {"MAYA": "đứng nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay buông xuống, một tay cầm tập hồ sơ",
                    "ADRIAN": "hai tay trên vành tay vịn"})
V("05", [8, 9], "two-shot trung 50mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải đứng cạnh",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN và MAYA, cả hai rõ mặt dưới mái che. Không có ai khác trong khung.",
  "ADRIAN hỏi bằng hai chữ, MAYA hạ hai tay xuống và trả lời",
  [("ADRIAN", "quiet, direct", 8), ("MAYA", "plain, steady", 9)])

S("06", "cận 85mm, cao 1m20, cách ADRIAN 1m2, đặt chính diện trước xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung từ ngực trở lên. Ở rìa PHẢI khung thấy một mảng vai áo blazer "
  "của MAYA đang đứng, out nét. Hậu cảnh là màn mưa xoá phông và ánh đèn cao áp.",
  "ADRIAN một tay đặt lên vành tay vịn, ngón cái miết vào mép nhựa.",
  "ADRIAN nhìn ra màn mưa rồi quay lại nhìn MAYA.",
  "ADRIAN — người vừa nghe một câu về loài người mà anh đã tin ngược lại suốt sáu tháng: mắt hơi mở, "
  "giọng nhỏ, KHÔNG cay đắng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA xin phép nói một câu vi phạm hợp đồng",
  ["ADRIAN_TUTE", "MAYA_TUTE"], "đầu dốc bê tông dưới mái che",
  {"ADRIAN": "ngồi xe lăn chính diện giữa khung", "MAYA": "một mảng vai áo blazer ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay trên vành tay vịn, ngón cái miết mép nhựa",
                    "MAYA": "hai tay buông, ngoài vùng nét"})
V("06", [10, 11], "cận 85mm hạ thấp · ADRIAN NÉT ngồi xe lăn chính diện · một mảng vai MAYA rìa phải out nét",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN rõ mặt. MAYA chỉ thấy MỘT MẢNG VAI áo blazer ở rìa phải, out nét — KHÔNG quay mặt về camera.",
  "ADRIAN nhìn ra màn mưa rồi quay lại nhìn cô",
  [("ADRIAN", "quiet, tired", 10), ("MAYA", "level, blunt", 11)])

S("07", "two-shot cận-trung 85mm, cao 1m30, cách MAYA 1m7, đặt dưới mái che, hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã cúi người xuống ngang tầm mặt ADRIAN, một tay chống lên tay vịn xe lăn. "
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. Hậu cảnh là màn mưa và cột thép xanh rêu.",
  "MAYA một tay chống lên tay vịn xe lăn, tay kia còn cầm tập hồ sơ. ADRIAN hai tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau, rất gần.",
  "MAYA — người vừa đọc ra toàn bộ câu chuyện từ những mảnh rời và nói ra bằng giọng rất khẽ: mắt thẳng, "
  "không đắc thắng. ADRIAN — nghe đúng thứ mình chưa từng nói với ai: mắt mở to một nhịp rồi khép lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN từ chối trả lời",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che",
  {"MAYA": "đứng cúi xuống nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "rất gần nhau", {"MAYA": "một tay chống lên tay vịn xe lăn, tay kia cầm tập hồ sơ",
                   "ADRIAN": "hai tay trên vành tay vịn"})
V("07", [12, 13], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải cúi xuống + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt, rất gần nhau. Không có ai khác trong khung.",
  "MAYA cúi xuống ngang tầm mặt anh, một tay chống lên tay vịn xe lăn",
  [("ADRIAN", "careful, guarded", 12), ("MAYA", "quiet, certain", 13)])

S("08", "trung 50mm, cao 1m30, cách MAYA 2m, đặt dưới mái che, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã đứng thẳng lên và cầm một TẤM PHỦ CHÂN BẰNG VẢI DÀY màu xám đá gấp trên tay. "
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. Ngoài mái che mưa nặng hạt hơn.",
  "MAYA hai tay cầm tấm phủ chân gấp, chưa mở ra. ADRIAN một tay đặt trên vành tay vịn, tay kia buông.",
  "MAYA nhìn ra màn mưa rồi nhìn xuống hai chân ADRIAN. ADRIAN nhìn MAYA.",
  "MAYA — người kết thúc một chủ đề bằng cách chuyển sang việc cần làm: giọng bình, tay đã bắt đầu làm. "
  "ADRIAN — từ chối trả lời nhưng không phủ nhận: mặt bình, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA mở tấm phủ chân ra",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che",
  {"MAYA": "đứng nửa phải khung cầm tấm phủ chân", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay cầm tấm phủ chân gấp", "ADRIAN": "một tay trên vành tay vịn, tay kia buông"})
V("08", [14, 15], "trung 50mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải cầm tấm phủ chân",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN và MAYA, cả hai rõ mặt dưới mái che. Không có ai khác trong khung.",
  "ADRIAN từ chối trả lời, MAYA cầm tấm phủ chân lên và chuyển sang việc khác",
  [("ADRIAN", "flat, closing", 14), ("MAYA", "warm, practical", 15)],
  ketclip="Cuối clip, MAYA mở tấm phủ chân ra và phủ lên hai chân ADRIAN, rồi vuốt phẳng mép vải. "
          "Clip dừng đúng lúc tay cô rời khỏi tấm phủ.")

S("09", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m4, đặt bên xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, tấm phủ chân màu xám đá đã phủ trên hai chân. MAYA đang cúi ở "
  "nửa PHẢI khung, hai tay vừa rời khỏi mép vải. Hậu cảnh là màn mưa và mặt bãi ướt.",
  "ADRIAN một tay đặt lên mép tấm phủ. MAYA hai tay còn ở gần mép vải, chưa rút hẳn về.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người gọi tên cô lần thứ hai trong cùng một chiều: giọng rất nhỏ, mắt dịu. "
  "MAYA — dừng tay lại vì cái giọng đó: mày hơi nhướn, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN nói ra con số ngày",
  ["ADRIAN_TUTE", "MAYA_TUTE"], "đầu dốc bê tông dưới mái che",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "MAYA": "đang cúi nửa phải khung"},
  "rất gần nhau", {"ADRIAN": "một tay đặt lên mép tấm phủ chân",
                   "MAYA": "hai tay còn gần mép vải"})
V("09", [16, 17, 18], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải đang cúi xuống",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_TUTE")],
  "ADRIAN và MAYA, cả hai rõ mặt dưới mái che. Không có ai khác trong khung.",
  "ADRIAN đặt tay lên mép tấm phủ chân, MAYA dừng tay lại và ngẩng lên",
  [("ADRIAN", "very quiet, gentle", 16), ("MAYA", "soft, attentive", 17),
   ("ADRIAN", "quiet, weighted", 18)])

S("10", "two-shot cận-trung 85mm, cao 1m30, cách MAYA 1m6, đặt dưới mái che, hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đã đứng thẳng lên ở nửa PHẢI khung. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, mặt ngước lên. "
  "Hậu cảnh là màn mưa ngoài mái che và ánh đèn cao áp trắng.",
  "MAYA hai tay đặt lại trên tay đẩy xe lăn. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống ADRIAN. ADRIAN nhìn ra màn mưa phía trước.",
  "MAYA — người lại bị bỏ lại với một câu đố nữa và đã quen: khoé môi kéo lệch, mắt hơi nheo. "
  "ADRIAN — trả lời bằng hai chữ và không nói thêm: mặt bình, mắt tĩnh nhìn thẳng vào màn mưa.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đẩy chiếc xe lăn xuống dốc bê tông",
  ["MAYA_TUTE", "ADRIAN_TUTE"], "đầu dốc bê tông dưới mái che",
  {"MAYA": "đứng sau xe lăn nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay đặt trên tay đẩy xe lăn", "ADRIAN": "hai tay trên vành tay vịn"})
V("10", [19, 20], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải đứng sau xe lăn + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_TUTE"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt dưới mái che. Không có ai khác trong khung.",
  "MAYA đứng thẳng lên và đặt lại hai tay trên tay đẩy xe lăn",
  [("MAYA", "wry, tired", 19), ("ADRIAN", "quiet, certain", 20)])
