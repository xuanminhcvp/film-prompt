# -*- coding: utf-8 -*-
"""SCENE 25 — ICU, GIƯỜNG 12 (ban ngày). Bệnh nhân không tên."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S25", "REF_ICU_NGAY", qc=qc.S25)

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách HELEN 5m, đặt ở cửa buồng bệnh nhìn chếch dọc theo giường",
  "HELEN nằm trên giường bệnh giữa phòng, nắng sớm qua cửa sổ đổ một mảng sáng lớn lên ga giường. "
  "MẮT BÀ ĐANG MỞ, đầu hơi nghiêng về phía cửa sổ. Buồng bệnh không có ai khác.",
  "HELEN hai tay đặt xuôi trên chăn, các ngón một bàn tay hơi động.",
  "HELEN nhìn về phía mảng nắng trên bậu cửa sổ, mắt mở.",
  "HELEN — người vừa mở mắt sau bảy tháng và chưa biết mình đang ở đâu: mắt mở hé, chớp rất chậm, "
  "mặt yếu nhưng đã có sự sống.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng chân chạy tới ngoài hành lang",
  ["HELEN"], "buồng bệnh giường 12, ban ngày",
  {"HELEN": "nằm trên giường bệnh, mắt đã mở"}, "một mình trong khung",
  {"HELEN": "hai tay đặt xuôi trên chăn, các ngón hơi động"})
B("B1", "Mở cảnh. Bảy tháng sau. Nắng sớm tràn vào buồng giường 12 — và mắt HELEN đã mở.",
  "toàn cảnh 24mm · HELEN NÉT nằm trên giường bệnh, MẮT ĐÃ MỞ · không có ai khác trong khung",
  [("HELEN", "HELEN")],
  "CHỈ MỘT MÌNH HELEN trong khung, rõ mặt, nằm trên giường bệnh với ĐÔI MẮT ĐANG MỞ. "
  "Không có người nào khác trong phòng.",
  "cả bộ phim này bắt đầu bằng một hoá đơn hai trăm nghìn đô để giữ cho người phụ nữ này thở; "
  "khung hình đầu tiên của cảnh cuối là đôi mắt bà mở ra.",
  "các ngón tay HELEN động một nhịp trên mặt chăn; mắt bà chớp rất chậm hai lần và dõi theo mảng nắng "
  "dịch trên ga giường; ngoài cửa sổ tán cây động nhẹ.",
  "Ambient tiếng bíp đều của máy theo dõi và tiếng chim ngoài cửa sổ, SFX tiếng chăn sột soạt rất khẽ.",
  nhac("NÂNG", "Mốc mở chương cuối: sự sống trở lại. Nhạc được phép dâng nhưng phải giữ mộc, vì phần lớn cảnh này là hai người nói chuyện rất khẽ.",
       "Cinematic soul at 76 BPM; a felt piano alone for four seconds, a female alto entering low and close, "
       "strings rising underneath and one soft kick joining at the midpoint, then everything pulling back to piano "
       "and voice; lyrics about a morning that somebody paid for and nobody was told about; warm analog mix, "
       "female vocal, piano, strings, hopeful, tender",
       "Cinematic instrumental at 74 BPM; felt piano playing a rising four-note figure, a cello entering underneath, "
       "a string section swelling once at the midpoint then pulling back to piano alone, one soft kick in the last "
       "bars; warm analog mix, piano, cello, strings, hopeful, tender"),
  dur=8)

# ── HELEN TỈNH ──
S("01", "trung 50mm, cao 1m30, cách MAYA 2m2, đặt ở cửa buồng nhìn vào, lấy cả ba người",
  "MAYA vừa chạy vào và dừng ở nửa PHẢI khung cạnh giường. HELEN nằm ở giữa khung, mắt mở, đầu quay về phía cô. "
  "NURSE DIANE đứng ở nửa TRÁI khung cạnh cửa trượt, bìa kẹp bệnh án trong tay.",
  "MAYA hai tay bám vào thành chắn kim loại của giường. HELEN hai tay đặt xuôi trên chăn. "
  "NURSE DIANE một tay còn trên khung cửa trượt.",
  "MAYA nhìn xuống mặt HELEN. HELEN nhìn lên MAYA. NURSE DIANE nhìn cả hai.",
  "NURSE DIANE — người vừa chạy đi gọi và còn thở gấp: mắt sáng, giọng gấp. "
  "MAYA — chưa dám tin: mắt mở to, hai tay bám chặt thành giường. HELEN — mắt mở, chớp chậm.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA khuỵu xuống ngồi lên mép giường",
  ["MAYA_SCRUB", "HELEN", "NURSE DIANE"], "buồng bệnh giường 12, cạnh giường",
  {"MAYA": "đứng bám thành giường nửa phải khung", "HELEN": "nằm trên giường giữa khung, mắt mở",
   "NURSE DIANE": "đứng cạnh cửa trượt nửa trái khung"},
  "NURSE DIANE cách ba mét",
  {"MAYA": "hai tay bám thành chắn kim loại của giường", "HELEN": "hai tay đặt xuôi trên chăn",
   "NURSE DIANE": "một tay trên khung cửa trượt, tay kia cầm bìa kẹp bệnh án"})
V("01", [0, 1, 2], "trung 50mm · NURSE DIANE NÉT trái cạnh cửa + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải bám thành giường",
  [("NURSE DIANE", "NURSE DIANE"), ("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "NURSE DIANE, MAYA và HELEN, cả ba rõ mặt. HELEN nằm trên giường với ĐÔI MẮT ĐANG MỞ, đầu quay được về "
  "phía MAYA, KHÔNG ngồi dậy.",
  "MAYA chạy vào bám hai tay vào thành giường, NURSE DIANE dừng lại ở cửa trượt",
  [("NURSE DIANE", "breathless, bright", 0), ("MAYA", "fast, clinical", 1),
   ("NURSE DIANE", "warm, quick", 2)])

S("02", "cận-trung 85mm, cao 1m10, cách MAYA 1m5, máy hạ thấp bên thành giường lấy cả hai người",
  "MAYA đã ngồi xuống mép giường ở nửa PHẢI khung, cúi sát xuống. HELEN nằm ở nửa TRÁI khung, mắt mở, "
  "mặt quay về phía cô. Hậu cảnh là mảng nắng trên tường và cột truyền dịch inox.",
  "MAYA hai tay nắm lấy một bàn tay HELEN. HELEN một bàn tay để trong tay con gái, các ngón hơi siết lại.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người bảy tháng nay chỉ nói một chiều và bây giờ được trả lời: mắt tràn nước, giọng vỡ hẳn, "
  "khoé môi run. HELEN — gọi tên con gái bằng hơi chứ chưa thành tiếng: mắt mở, môi mấp máy.",
  "đúng khoảnh khắc ngay TRƯỚC khi HELEN cố nói câu thứ hai",
  ["MAYA_SCRUB", "HELEN"], "buồng bệnh giường 12, MAYA ngồi mép giường",
  {"MAYA": "ngồi mép giường nửa phải khung, cúi sát xuống", "HELEN": "nằm trên giường nửa trái khung, mắt mở"},
  "sát cạnh nhau", {"MAYA": "hai tay nắm lấy một bàn tay HELEN",
                    "HELEN": "một bàn tay trong tay con gái, các ngón hơi siết"})
V("02", [3, 4], "cận-trung 85mm hạ thấp · MAYA NÉT phải ngồi mép giường + HELEN NÉT trái nằm trên giường, MẮT MỞ",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "MAYA và HELEN, cả hai rõ mặt. HELEN nằm trên giường với ĐÔI MẮT ĐANG MỞ, chỉ cử động rất nhẹ, "
  "KHÔNG ngồi dậy. Không có ai khác trong khung.",
  "MAYA ngồi xuống mép giường và nắm lấy bàn tay mẹ bằng cả hai tay",
  [("MAYA", "breaking, tender", 3), ("HELEN", "faint, breathy", 4)])

S("03", "cận 85mm, cao 1m10, cách HELEN 1m2, máy hạ thấp, lấy HELEN nét và một mảng vai MAYA rìa phải",
  "HELEN nằm chiếm phần lớn khung từ ngực trở lên, mắt mở, đầu trên gối. Ở rìa PHẢI khung thấy một mảng vai áo "
  "scrub xanh mòng két và bàn tay MAYA đang nắm tay bà, out nét. Nắng sớm hắt ngang gối.",
  "HELEN một bàn tay trong tay con gái, ngón cái động một nhịp.",
  "HELEN nhìn thẳng vào mặt MAYA.",
  "HELEN — người vừa tỉnh sau bảy tháng và câu hỏi đầu tiên là về thời gian: mắt mở hé, giọng khàn đứt quãng, "
  "mặt yếu nhưng tỉnh táo.",
  "đúng khoảnh khắc ngay TRƯỚC khi HELEN hỏi câu thứ hai",
  ["HELEN", "MAYA_SCRUB"], "buồng bệnh giường 12",
  {"HELEN": "nằm trên giường, chính diện giữa khung, mắt mở",
   "MAYA": "một mảng vai áo scrub và bàn tay ở rìa phải khung"},
  "sát cạnh nhau", {"HELEN": "một bàn tay trong tay con gái, ngón cái động một nhịp",
                    "MAYA": "hai tay nắm tay HELEN, ngoài vùng nét"})
V("03", [5, 6, 7], "cận 85mm hạ thấp · HELEN NÉT nằm chính diện, MẮT MỞ · một mảng vai và bàn tay MAYA rìa phải out nét",
  [("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
  "HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. MAYA chỉ thấy MỘT MẢNG VAI áo scrub và bàn tay ở rìa "
  "phải, out nét — KHÔNG thấy mặt.",
  "HELEN nằm yên, ngón cái động một nhịp trong tay con gái",
  [("MAYA", "soft, soothing", 5), ("HELEN", "hoarse, faint", 6), ("MAYA", "quiet, steady", 7)])

S("04", "cận-trung 85mm, cao 1m10, cách MAYA 1m4, máy hạ thấp bên thành giường lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung trên mép giường. HELEN nằm ở nửa TRÁI khung, mắt mở, mặt hướng về phía cô. "
  "Hậu cảnh là cửa sổ đầy nắng và bình hoa cúc trắng trên bậu.",
  "MAYA một tay vuốt tóc bạc trên trán HELEN. HELEN một bàn tay còn trong tay con gái.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "HELEN — hỏi đúng câu mà người mẹ nào cũng hỏi: mắt mở, giọng khàn. "
  "MAYA — trả lời bằng một nửa sự thật vì chưa biết bắt đầu từ đâu: khoé môi kéo, mắt ướt.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng người từ phía cửa trượt",
  ["MAYA_SCRUB", "HELEN"], "buồng bệnh giường 12, MAYA ngồi mép giường",
  {"MAYA": "ngồi mép giường nửa phải khung", "HELEN": "nằm trên giường nửa trái khung, mắt mở"},
  "sát cạnh nhau", {"MAYA": "một tay vuốt tóc bạc trên trán HELEN",
                    "HELEN": "một bàn tay trong tay con gái"})
V("04", [8, 9, 10], "cận-trung 85mm hạ thấp · MAYA NÉT phải ngồi mép giường + HELEN NÉT trái nằm trên giường, MẮT MỞ",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "MAYA và HELEN, cả hai rõ mặt. HELEN nằm trên giường với ĐÔI MẮT ĐANG MỞ, chỉ cử động rất nhẹ. "
  "Không có ai khác trong khung.",
  "MAYA vuốt lại tóc bạc trên trán mẹ mình",
  [("HELEN", "hoarse, faint", 8), ("MAYA", "quiet, careful", 9), ("HELEN", "faint, sceptical", 10)])

S("05", "trung 50mm, cao 1m30, cách MAYA 2m2, đặt bên giường nhìn về phía cửa trượt, lấy cả ba người",
  "ADRIAN đứng ở nửa TRÁI khung ngay trong CỬA TRƯỢT, ĐỨNG THẲNG TRÊN HAI CHÂN, một tay vịn khung cửa. "
  "MAYA ngồi ở nửa PHẢI khung trên mép giường, đã quay đầu lại. HELEN nằm ở giữa khung, mắt mở.",
  "ADRIAN một tay vịn khung cửa trượt, tay kia cầm một chiếc cặp tài liệu giấy. MAYA một tay còn nắm tay HELEN. "
  "HELEN hai tay đặt xuôi trên chăn.",
  "ADRIAN nhìn về phía giường. MAYA quay đầu nhìn ADRIAN. HELEN nhìn về phía cửa.",
  "ADRIAN — người vừa tự đi bộ lên bốn tầng lầu: thở hơi nặng, mồ hôi ở thái dương, mặt bình. "
  "MAYA — thấy chồng mình đứng ở cửa: mắt mở to. HELEN — nhìn người lạ ở cửa: mày hơi chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bước hẳn vào trong buồng",
  ["ADRIAN_VEST", "MAYA_SCRUB", "HELEN"], "buồng bệnh giường 12, từ cửa trượt tới giường",
  {"ADRIAN": "đứng thẳng trong cửa trượt, nửa trái khung", "MAYA": "ngồi mép giường nửa phải khung",
   "HELEN": "nằm trên giường giữa khung, mắt mở"},
  "ADRIAN cách giường ba mét",
  {"ADRIAN": "một tay vịn khung cửa trượt, tay kia cầm chiếc cặp tài liệu giấy",
   "MAYA": "một tay nắm tay HELEN", "HELEN": "hai tay đặt xuôi trên chăn"})
V("05", [11, 12, 13], "trung 50mm · ADRIAN NÉT trái ĐỨNG THẲNG trong cửa trượt + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN trong khung cửa trượt, KHÔNG có xe lăn, KHÔNG có nạng. "
  "MAYA và HELEN rõ mặt; HELEN nằm trên giường với ĐÔI MẮT ĐANG MỞ.",
  "ADRIAN vịn khung cửa trượt và bước tới ngưỡng cửa, MAYA quay đầu lại",
  [("ADRIAN", "breathless, warm", 11), ("MAYA", "surprised, soft", 12),
   ("ADRIAN", "dry, breathless", 13)])

S("06", "trung 50mm, cao 1m20, cách ADRIAN 2m, đặt bên giường, hạ thấp lấy cả ba người",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, đã tới cạnh giường. HELEN nằm ở giữa khung, mắt mở, đầu quay về phía anh. "
  "MAYA ngồi ở nửa PHẢI khung trên mép giường.",
  "ADRIAN một tay đặt lên thành chắn kim loại của giường, tay kia cầm chiếc cặp tài liệu giấy. "
  "HELEN một bàn tay hơi nhấc lên khỏi chăn. MAYA hai tay đặt trên đùi.",
  "HELEN nhìn ADRIAN. ADRIAN nhìn HELEN. MAYA nhìn ADRIAN.",
  "HELEN — hỏi người lạ đứng cạnh giường mình là ai: mắt mở, giọng khàn. "
  "ADRIAN — tự giới thiệu bằng câu dài nhất anh nói trong cả bộ phim: giọng chậm, rõ, mắt dịu. "
  "MAYA — mày chau, chưa hiểu.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN đặt chiếc cặp tài liệu xuống mép giường",
  ["ADRIAN_VEST", "HELEN", "MAYA_SCRUB"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng cạnh giường nửa trái khung", "HELEN": "nằm trên giường giữa khung, mắt mở",
   "MAYA": "ngồi mép giường nửa phải khung"},
  "ba người trong vòng một mét",
  {"ADRIAN": "một tay đặt lên thành chắn giường, tay kia cầm chiếc cặp tài liệu giấy",
   "HELEN": "một bàn tay hơi nhấc lên khỏi chăn", "MAYA": "hai tay đặt trên đùi"})
V("06", [14, 15], "trung 50mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG cạnh giường + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. "
  "MAYA rõ mặt ngồi mép giường.",
  "ADRIAN đặt một tay lên thành chắn giường và tự giới thiệu",
  [("HELEN", "hoarse, wary", 14), ("ADRIAN", "slow, warm", 15)])

S("07", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m6, đặt bên giường, hạ thấp lấy ADRIAN nét và MAYA cùng khung",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, đã đặt một TẬP GIẤY A4 BỊ XÉ ĐÔI xuống mặt chăn. MAYA ngồi ở nửa PHẢI "
  "khung, đã nhìn xuống tập giấy. Hậu cảnh là cửa sổ đầy nắng.",
  "ADRIAN một tay còn đặt trên hai nửa tập giấy xé đôi trên mặt chăn. MAYA một tay đưa về phía tập giấy.",
  "MAYA nhìn xuống hai nửa tập giấy. ADRIAN nhìn MAYA.",
  "ADRIAN — người đặt xuống thứ đã mua một năm đời cô, và đã xé nó: giọng chậm, mắt không rời cô. "
  "MAYA — nhận ra ngay đó là tờ giấy nào: mắt mở to, tay dừng lại giữa chừng.",
  "đúng khoảnh khắc ngay TRƯỚC khi ngón tay MAYA chạm vào mép giấy xé",
  ["ADRIAN_VEST", "MAYA_SCRUB", "PROP_HOPDONGRACH"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng cạnh giường nửa trái khung", "MAYA": "ngồi mép giường nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay đặt trên hai nửa tập giấy xé đôi",
                    "MAYA": "một tay đưa về phía tập giấy"})
V("07", [16, 17], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG + MAYA NÉT phải ngồi mép giường nhìn xuống tập giấy xé đôi",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt ngồi mép giường. "
  "Trên mặt chăn giữa hai người là hai nửa của một tập giấy đã bị xé đôi.",
  "ADRIAN đặt hai nửa tập giấy xé đôi xuống mặt chăn trước mặt MAYA",
  [("MAYA", "quiet, wary", 16), ("ADRIAN", "slow, plain", 17)])

S("08", "cận-trung 85mm, cao 1m20, cách MAYA 1m5, đặt bên giường, hạ thấp lấy MAYA nét và ADRIAN cùng khung",
  "MAYA ngồi ở nửa PHẢI khung trên mép giường, một TẤM BIỂN TÊN NHỰA TRẮNG NGÀ đã ở trong tay. "
  "ADRIAN đứng thẳng ở nửa TRÁI khung. Hậu cảnh là bình hoa cúc trắng trên bậu cửa sổ.",
  "MAYA hai tay cầm tấm biển tên nhựa, nghiêng nó về phía ánh sáng. ADRIAN một tay đặt trên thành chắn giường.",
  "MAYA nhìn xuống mặt tấm biển. ADRIAN nhìn MAYA.",
  "MAYA — người vừa đọc hai dòng chữ trên một tấm biển cũ và chưa hiểu vì sao mình đang cầm nó: mày chau, "
  "giọng chậm. ADRIAN — mặt bình, mắt không rời cô.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu kể",
  ["MAYA_SCRUB", "ADRIAN_VEST", "PROP_BIENTEN"], "buồng bệnh giường 12, cạnh giường",
  {"MAYA": "ngồi mép giường nửa phải khung, cầm tấm biển tên", "ADRIAN": "đứng thẳng nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay cầm tấm biển tên nhựa nghiêng về phía ánh sáng",
                    "ADRIAN": "một tay đặt trên thành chắn giường"})
V("08", [18, 19, 20], "cận-trung 85mm hạ thấp · MAYA NÉT phải cầm tấm biển tên + ADRIAN NÉT trái ĐỨNG THẲNG",
  [("MAYA", "MAYA_SCRUB"), ("ADRIAN", "ADRIAN_VEST")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "MAYA cầm một tấm biển tên nhựa trắng ngà đã ố vàng.",
  "MAYA cầm tấm biển tên nghiêng về phía ánh sáng và đọc hai dòng chữ trên đó",
  [("MAYA", "quiet, puzzled", 18), ("ADRIAN", "slow, quiet", 19), ("MAYA", "reading, flat", 20)])

S("09", "cận 85mm, cao 1m20, cách ADRIAN 1m3, đặt bên giường, hạ thấp, lấy ADRIAN nét và một mảng vai MAYA rìa phải",
  "ADRIAN đứng thẳng chiếm phần lớn khung từ ngực trở lên. Ở rìa PHẢI khung thấy một mảng vai áo scrub và mái "
  "tóc búi của MAYA đang ngồi, out nét. Hậu cảnh là tường buồng bệnh và mảng nắng, xoá phông.",
  "ADRIAN một tay đặt lên thành chắn kim loại của giường, các ngón siết nhẹ.",
  "ADRIAN nhìn xuống MAYA.",
  "ADRIAN — người kể lại chín ngày mình không có tên bằng giọng của người kể chuyện người khác: giọng chậm, "
  "đều, mắt tĩnh, KHÔNG tự thương.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA ngẩng phắt lên nhìn anh",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng chính diện giữa khung",
   "MAYA": "một mảng vai áo scrub và mái tóc búi ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay đặt lên thành chắn giường, các ngón siết nhẹ",
                    "MAYA": "hai tay cầm tấm biển tên, ngoài vùng nét"})
VX("09", "cận 85mm hạ thấp · ADRIAN NÉT ĐỨNG THẲNG chính diện · một mảng vai và mái tóc búi MAYA rìa phải out nét",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA chỉ thấy MỘT MẢNG VAI áo scrub và mái tóc búi ở rìa phải, "
   "out nét — KHÔNG quay mặt về camera.",
   "ADRIAN siết nhẹ tay trên thành chắn giường và kể",
   [("ADRIAN", "slow, even",
     "Six months before your wedding, a man was brought into this unit with no wallet, no phone, and a spine "
     "broken in two places.")],
   [("MAYA", "silent, listening")])

S("09b", "trung 50mm, cao 1m20, cách ADRIAN 2m, đặt bên giường, hạ thấp lấy cả ba người",
  "ADRIAN đứng thẳng ở nửa TRÁI khung cạnh giường. HELEN nằm ở giữa khung, mắt mở, đầu quay về phía anh. "
  "MAYA ngồi ở nửa PHẢI khung trên mép giường, đã ngẩng lên nhìn anh.",
  "ADRIAN một tay đặt trên thành chắn giường, tay kia buông. HELEN hai tay đặt xuôi trên chăn. "
  "MAYA hai tay đặt trên đùi.",
  "ADRIAN nhìn thẳng phía trước. MAYA nhìn ADRIAN. HELEN nhìn ADRIAN.",
  "ADRIAN — người kể ra chi tiết mà cả sáu tháng nay không ai được biết: giọng chậm, đều, mắt tĩnh, "
  "KHÔNG tự thương. MAYA — bắt đầu đếm lại các mốc thời gian trong đầu: mày chau. HELEN — mắt mở, theo dõi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhìn xuống chiếc giường mình đang ngồi",
  ["ADRIAN_VEST", "HELEN", "MAYA_SCRUB"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng cạnh giường nửa trái khung", "HELEN": "nằm trên giường giữa khung, mắt mở",
   "MAYA": "ngồi mép giường nửa phải khung"},
  "ba người trong vòng một mét",
  {"ADRIAN": "một tay đặt trên thành chắn giường", "HELEN": "hai tay đặt xuôi trên chăn",
   "MAYA": "hai tay đặt trên đùi"})
VX("09b", "trung 50mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải ngồi mép giường",
   [("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. "
   "MAYA rõ mặt ngồi mép giường.",
   "ADRIAN giữ nguyên tay trên thành chắn giường và kể tiếp",
   [("ADRIAN", "slow, even",
     "His family had already told the press he was dead so the share price would settle. "
     "For nine days he had no name.")],
   [("MAYA", "silent, counting back"), ("HELEN", "silent, watching him")])

S("10", "trung 50mm, cao 1m20, cách MAYA 2m, đặt bên giường, hạ thấp lấy cả ba người",
  "MAYA ngồi ở nửa PHẢI khung trên mép giường, đã ngẩng phắt lên và một tay đặt lên mặt ga giường. "
  "ADRIAN đứng thẳng ở nửa TRÁI khung. HELEN nằm ở giữa khung, mắt mở, nhìn hai người.",
  "MAYA một tay đặt lên mặt ga giường ngay dưới chỗ mình ngồi, tay kia còn cầm tấm biển tên. "
  "ADRIAN một tay đặt trên thành chắn giường. HELEN hai tay đặt xuôi trên chăn.",
  "MAYA nhìn xuống chiếc giường mình đang ngồi rồi ngẩng lên nhìn ADRIAN. ADRIAN nhìn MAYA. HELEN nhìn cả hai.",
  "MAYA — người vừa hiểu ra chiếc giường mình đang ngồi là chiếc giường nào: mắt mở to, tay áp xuống ga giường. "
  "ADRIAN — xác nhận bằng hai chữ rồi kể tiếp: mặt bình. HELEN — mắt mở, theo dõi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đưa tay lên che miệng",
  ["MAYA_SCRUB", "ADRIAN_VEST", "HELEN", "PROP_BIENTEN"], "buồng bệnh giường 12, cạnh giường",
  {"MAYA": "ngồi mép giường nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung",
   "HELEN": "nằm trên giường giữa khung, mắt mở"},
  "ba người trong vòng một mét",
  {"MAYA": "một tay đặt lên mặt ga giường, tay kia cầm tấm biển tên",
   "ADRIAN": "một tay đặt trên thành chắn giường", "HELEN": "hai tay đặt xuôi trên chăn"})
V("10", [22, 23], "trung 50mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. "
  "MAYA rõ mặt ngồi mép giường.",
  "MAYA áp một bàn tay xuống mặt ga giường mình đang ngồi và ngẩng lên",
  [("MAYA", "quiet, realising", 22), ("ADRIAN", "slow, tender", 23)])

S("11", "cận 85mm, cao 1m20, cách MAYA 1m2, đặt bên giường, hạ thấp, lấy MAYA nét và một mảng vai ADRIAN rìa trái",
  "MAYA ngồi chiếm phần lớn khung từ ngực trở lên, một tay đã đưa lên che ngang miệng. Ở rìa TRÁI khung thấy "
  "một mảng vai áo vest đen của ADRIAN đang đứng, out nét. Hậu cảnh là nắng trên tường, xoá phông.",
  "MAYA một tay che ngang miệng, tay kia còn cầm tấm biển tên trên đùi.",
  "MAYA nhìn thẳng lên mặt ADRIAN.",
  "MAYA — người đang lục lại trí nhớ của bốn trăm bệnh nhân và không tìm thấy anh: mày chau, mắt ướt, "
  "giọng nhỏ, lắc đầu một cái rất nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu giải thích vì sao cô không nhớ",
  ["MAYA_SCRUB", "ADRIAN_VEST", "PROP_BIENTEN"], "buồng bệnh giường 12",
  {"MAYA": "ngồi mép giường, chính diện giữa khung",
   "ADRIAN": "một mảng vai áo vest đen ở rìa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay che ngang miệng, tay kia cầm tấm biển tên trên đùi",
                    "ADRIAN": "một tay trên thành chắn giường, ngoài vùng nét"})
VX("11", "cận 85mm hạ thấp · MAYA NÉT chính diện · một mảng vai áo vest ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_SCRUB"), ("ADRIAN", "ADRIAN_VEST")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI áo vest đen ở rìa trái, out nét — KHÔNG quay mặt về camera.",
  "MAYA đưa một tay lên che ngang miệng và lắc đầu một cái rất nhẹ",
  [("MAYA", "small, searching", "I do not remember."),
   ("ADRIAN", "slow, gentle", "You would not. You had four hundred patients that year. But you called me sir.")])

S("11b", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m5, đặt bên giường, hạ thấp lấy cả hai người",
  "ADRIAN đứng thẳng ở nửa TRÁI khung cạnh giường. MAYA ngồi ở nửa PHẢI khung trên mép giường, một tay "
  "đã rời khỏi miệng. Hậu cảnh là cửa sổ đầy nắng và bình hoa cúc trắng.",
  "ADRIAN một tay đặt lên thành chắn giường, các ngón siết nhẹ. MAYA một tay đặt xuống mặt chăn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người nhớ chính xác chín đêm và cách cô gọi mình: giọng chậm, mắt ướt, khoé môi động. "
  "MAYA — nghe lại chính giọng mình của một năm trước: mắt tràn nước, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi có phải chỉ có thế",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng cạnh giường nửa trái khung", "MAYA": "ngồi mép giường nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay đặt trên thành chắn giường, các ngón siết nhẹ",
                    "MAYA": "một tay đặt xuống mặt chăn"})
VX("11b", "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG + MAYA NÉT phải ngồi mép giường",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt ngồi mép giường. Không có ai khác rõ mặt trong khung.",
   "ADRIAN siết nhẹ tay trên thành chắn giường và kể nốt",
   [("ADRIAN", "slow, gentle",
     "Nine nights, and you never once called me the bed, or the injury, or the case. You said, good evening, sir.")],
   [("MAYA", "silent, eyes overflowing")])

S("12", "cận-trung 85mm, cao 1m20, cách MAYA 1m5, đặt bên giường, hạ thấp lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung trên mép giường, hai tay đã đặt xuống đùi. ADRIAN đứng thẳng ở nửa TRÁI khung. "
  "Hậu cảnh là cửa sổ đầy nắng và bình hoa cúc trắng.",
  "MAYA hai tay đặt xuống đùi, tấm biển tên nằm ngửa trên đó. ADRIAN một tay rời khỏi thành chắn giường.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — hỏi ba chữ vì cô vẫn chưa tin lý do lại nhỏ tới thế: giọng nhỏ, mắt ướt. "
  "ADRIAN — trả lời hai chữ và trong hai chữ đó là cả bộ phim: giọng rất nhỏ, mắt ướt, mặt vẫn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN kể tiếp về buổi sáng đám cưới",
  ["MAYA_SCRUB", "ADRIAN_VEST", "PROP_BIENTEN"], "buồng bệnh giường 12, cạnh giường",
  {"MAYA": "ngồi mép giường nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay đặt xuống đùi, tấm biển tên nằm ngửa trên đó",
                    "ADRIAN": "một tay rời khỏi thành chắn giường"})
V("12", [26], "cận-trung 85mm hạ thấp · MAYA NÉT phải ngồi mép giường + ADRIAN NÉT trái ĐỨNG THẲNG",
  [("MAYA", "MAYA_SCRUB"), ("ADRIAN", "ADRIAN_VEST")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. Không có ai khác rõ mặt trong khung.",
  "MAYA đặt hai tay xuống đùi với tấm biển tên nằm ngửa trên đó",
  [("MAYA", "small, disbelieving", 26)], [("ADRIAN", "silent, about to answer")])

S("13", "cận 85mm, cao 1m20, cách ADRIAN 1m3, đặt bên giường, hạ thấp, lấy ADRIAN nét và một mảng vai MAYA rìa phải",
  "ADRIAN đứng thẳng chiếm phần lớn khung từ ngực trở lên. Ở rìa PHẢI khung thấy một mảng vai áo scrub của "
  "MAYA đang ngồi, out nét. Hậu cảnh là tường buồng bệnh và mảng nắng lớn, xoá phông.",
  "ADRIAN một tay đưa vào túi trong áo vest rồi rút ra, các ngón khép lại quanh một thứ không thấy rõ.",
  "ADRIAN nhìn thẳng xuống mặt MAYA.",
  "ADRIAN — người kể ra lý do thật của việc mình có mặt ở nhà thờ hôm đó: giọng chậm, rất nhỏ, mắt ướt hẳn, "
  "khoé môi động một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nói ra tên người đã bước vào hôm đó",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng chính diện giữa khung", "MAYA": "một mảng vai áo scrub ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay đưa vào túi trong áo vest rồi rút ra",
                    "MAYA": "hai tay trên đùi, ngoài vùng nét"})
VX("13", "cận 85mm hạ thấp · ADRIAN NÉT ĐỨNG THẲNG chính diện · một mảng vai áo scrub MAYA rìa phải out nét",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA chỉ thấy MỘT MẢNG VAI áo scrub ở rìa phải, out nét — "
   "KHÔNG quay mặt về camera.",
   "ADRIAN đưa một tay vào túi trong áo vest rồi rút ra",
   [("ADRIAN", "slow, confessing",
     "That is everything. Do you understand now? I did not come to that church on your wedding day to marry you, "
     "Maya.")],
   [("MAYA", "silent, listening")])

S("13b", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m6, đặt bên giường, hạ thấp lấy cả hai người",
  "ADRIAN đứng thẳng ở nửa TRÁI khung cạnh giường, một tay còn trong túi áo vest. MAYA ngồi ở nửa PHẢI khung "
  "trên mép giường, đã ngẩng hẳn lên. Hậu cảnh là mảng nắng lớn trên tường buồng bệnh.",
  "ADRIAN một tay rút khỏi túi áo vest và mở lòng bàn tay ra, trống không. MAYA hai tay đặt trên đùi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người kể ra chi tiết tấm séc trong túi áo mình hôm đó: giọng chậm, rất nhỏ, mắt ướt, "
  "khoé môi động một nhịp. MAYA — nghe và ghép nốt mảnh cuối: mắt tràn nước.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nói ra cái tên đã bước vào hôm đó",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đứng thẳng cạnh giường nửa trái khung", "MAYA": "ngồi mép giường nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay rút khỏi túi áo vest, mở lòng bàn tay trống",
                    "MAYA": "hai tay đặt trên đùi"})
VX("13b", "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG + MAYA NÉT phải ngồi mép giường",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt ngồi mép giường. Không có ai khác rõ mặt trong khung.",
   "ADRIAN rút tay khỏi túi áo vest và mở lòng bàn tay ra, trống không",
   [("ADRIAN", "slow, confessing",
     "I came to say thank you and go home. I sat in the back row with a check in my pocket for a nurse whose name "
     "I finally learned from a hospital roster.")],
   [("MAYA", "silent, tears falling")])

S("14", "two-shot cận-trung 85mm, cao 1m20, cách MAYA 1m5, đặt bên giường, hạ thấp lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung trên mép giường. ADRIAN đứng thẳng ở nửa TRÁI khung. Hậu cảnh là cửa sổ đầy nắng.",
  "MAYA một tay đưa lên chạm vào cổ mình rồi hạ xuống. ADRIAN hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người nói ra cái tên đã cắt đôi cuộc đời mình bằng giọng rất bình: mắt ướt, khoé môi động. "
  "ADRIAN — nhắc lại đúng câu đó, không thêm gì: giọng nhỏ, mắt không rời cô.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu hạ người xuống",
  ["MAYA_SCRUB", "ADRIAN_VEST"], "buồng bệnh giường 12, cạnh giường",
  {"MAYA": "ngồi mép giường nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay chạm vào cổ mình rồi hạ xuống", "ADRIAN": "hai tay buông dọc thân"})
V("14", [28, 29], "two-shot cận-trung 85mm hạ thấp · ADRIAN NÉT trái ĐỨNG THẲNG + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt ngồi mép giường. Không có ai khác rõ mặt trong khung.",
  "MAYA đưa tay lên chạm vào cổ mình rồi hạ xuống, ADRIAN nhắc lại đúng câu của cô",
  [("MAYA", "quiet, flat", 28), ("ADRIAN", "quiet, echoing", 29)])

S("15", "trung 50mm, cao 1m20, cách ADRIAN 2m, đặt bên giường, hạ thấp lấy cả ba người",
  "ADRIAN đứng ở nửa TRÁI khung, đã bắt đầu hạ người xuống, một tay bám vào thành chắn kim loại của giường. "
  "MAYA ngồi ở nửa PHẢI khung, đã nhổm lên. HELEN nằm ở giữa khung, mắt mở, đầu quay theo.",
  "ADRIAN một tay bám thành chắn giường, tay kia chống lên đầu gối mình. MAYA hai tay đưa ra phía anh. "
  "HELEN một bàn tay nhấc lên khỏi chăn.",
  "MAYA nhìn xuống hai chân ADRIAN. ADRIAN nhìn xuống sàn. HELEN nhìn ADRIAN.",
  "MAYA — điều dưỡng thấy ngay việc anh đang làm là không nên: mày chau, giọng gấp. "
  "ADRIAN — xin đúng một giây: quai hàm siết, hơi thở nặng. HELEN — mắt mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi đầu gối ADRIAN chạm xuống sàn vinyl",
  ["ADRIAN_VEST", "MAYA_SCRUB", "HELEN"], "buồng bệnh giường 12, cạnh giường",
  {"ADRIAN": "đang hạ người xuống cạnh giường, nửa trái khung", "MAYA": "ngồi nhổm lên, nửa phải khung",
   "HELEN": "nằm trên giường giữa khung, mắt mở"},
  "ba người trong vòng một mét",
  {"ADRIAN": "một tay bám thành chắn giường, tay kia chống lên đầu gối mình",
   "MAYA": "hai tay đưa ra phía anh", "HELEN": "một bàn tay nhấc lên khỏi chăn"})
V("15", [30, 31], "trung 50mm hạ thấp · ADRIAN NÉT trái đang hạ người xuống cạnh giường + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải nhổm lên",
  [("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, đang tự hạ người xuống bằng hai chân mình, một tay bám thành chắn giường. "
  "HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. MAYA rõ mặt.",
  "ADRIAN bám một tay vào thành chắn giường và bắt đầu hạ người xuống",
  [("MAYA", "quick, alarmed", 30), ("ADRIAN", "strained, quiet", 31)],
  ketclip="Cuối clip, ADRIAN quỳ một gối xuống sàn vinyl cạnh giường, một tay còn bám thành chắn. "
          "Clip dừng đúng lúc đầu gối anh chạm sàn.")

S("16", "trung 50mm, cao 1m00, cách ADRIAN 2m, máy hạ rất thấp ngang tầm người quỳ một gối",
  "ADRIAN quỳ MỘT GỐI xuống sàn vinyl ở nửa TRÁI khung cạnh giường, một tay còn bám thành chắn. "
  "HELEN nằm ở giữa khung trên giường, mắt mở, đầu nghiêng nhìn xuống. MAYA ngồi ở nửa PHẢI khung trên mép giường.",
  "ADRIAN một tay bám thành chắn giường, tay kia đặt trên đầu gối đang chống. "
  "HELEN một bàn tay đưa về phía mép giường. MAYA hai tay đặt trên đùi.",
  "HELEN nhìn xuống ADRIAN. MAYA nhìn ADRIAN. ADRIAN nhìn lên MAYA.",
  "HELEN — bà mẹ tưởng con rể mình vừa ngã: mắt mở to, giọng khàn gấp. "
  "MAYA — sửa lại cho mẹ bằng một chữ: khoé môi kéo lên, mắt ướt. ADRIAN — thở nặng, mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu nói với MAYA",
  ["ADRIAN_VEST", "HELEN", "MAYA_SCRUB"], "buồng bệnh giường 12, ADRIAN quỳ một gối cạnh giường",
  {"ADRIAN": "quỳ một gối cạnh giường, nửa trái khung", "HELEN": "nằm trên giường giữa khung, mắt mở",
   "MAYA": "ngồi mép giường nửa phải khung"},
  "ba người trong vòng một mét",
  {"ADRIAN": "một tay bám thành chắn giường, tay kia đặt trên đầu gối đang chống",
   "HELEN": "một bàn tay đưa về phía mép giường", "MAYA": "hai tay đặt trên đùi"})
V("16", [32, 33], "trung 50mm hạ rất thấp · ADRIAN NÉT trái QUỲ MỘT GỐI cạnh giường + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, đang QUỲ MỘT GỐI trên sàn vinyl cạnh giường, KHÔNG có xe lăn. "
  "HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. MAYA rõ mặt.",
  "HELEN đưa một bàn tay về phía mép giường, MAYA quay sang trả lời mẹ",
  [("HELEN", "hoarse, alarmed", 32), ("MAYA", "warm, correcting", 33)])

S("17", "cận-trung 85mm, cao 1m00, cách ADRIAN 1m5, máy hạ rất thấp ngang tầm người quỳ một gối",
  "ADRIAN quỳ một gối chiếm phần lớn khung ở nửa TRÁI, mặt ngước lên. MAYA ngồi ở nửa PHẢI khung trên mép giường, "
  "cúi xuống nhìn anh. Hậu cảnh là mảng nắng lớn trên tường và một góc cột truyền dịch.",
  "ADRIAN một tay đặt trên đầu gối đang chống, tay kia ngửa ra về phía MAYA. MAYA hai tay đặt trên đùi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người xin lỗi trước rồi mới hỏi, và biết mình không có gì để mặc cả: giọng chậm, rõ, mắt ướt, "
  "hơi thở nặng. MAYA — nghe từng chữ: mắt tràn nước, môi mím lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đưa tay chạm vào bàn tay anh",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, ADRIAN quỳ một gối cạnh giường",
  {"ADRIAN": "quỳ một gối nửa trái khung", "MAYA": "ngồi mép giường cúi xuống, nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay trên đầu gối chống, tay kia ngửa ra về phía MAYA",
                    "MAYA": "hai tay đặt trên đùi"})
VX("17", "cận-trung 85mm hạ rất thấp · ADRIAN NÉT trái QUỲ MỘT GỐI + MAYA NÉT phải ngồi mép giường cúi xuống",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, đang QUỲ MỘT GỐI trên sàn vinyl. MAYA rõ mặt ngồi mép giường. "
   "Không có ai khác rõ mặt trong khung.",
   "ADRIAN ngửa một bàn tay ra về phía MAYA và nói chậm",
   [("ADRIAN", "slow, apologising",
     "Maya Bennett. I bought a year of your life with money because I did not think anybody would give it to me "
     "for free.")],
   [("MAYA", "silent, eyes overflowing")])

S("17b", "cận 85mm, cao 1m00, cách ADRIAN 1m3, máy hạ rất thấp, lấy ADRIAN nét và một mảng đầu gối MAYA rìa phải",
  "ADRIAN quỳ một gối chiếm phần lớn khung từ ngực trở lên, mặt ngước lên. Ở rìa PHẢI khung thấy một mảng "
  "đầu gối và bàn tay MAYA đang ngồi trên mép giường, out nét. Hậu cảnh là nắng trên tường, xoá phông.",
  "ADRIAN một tay đặt lên ngực mình rồi hạ xuống đầu gối đang chống.",
  "ADRIAN nhìn thẳng lên mặt MAYA.",
  "ADRIAN — người xin lỗi bằng đúng chữ xin lỗi, không kèm lý do nào: giọng chậm, rõ, mắt ướt, "
  "hơi thở nặng vì hai chân đang gánh cả người.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN chuyển sang câu hỏi của mình",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, ADRIAN quỳ một gối",
  {"ADRIAN": "quỳ một gối, chính diện giữa khung",
   "MAYA": "một mảng đầu gối và bàn tay ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay đặt lên ngực rồi hạ xuống đầu gối đang chống",
                    "MAYA": "hai tay trên đùi, ngoài vùng nét"})
VX("17b", "cận 85mm hạ rất thấp · ADRIAN NÉT QUỲ MỘT GỐI chính diện · một mảng đầu gối và bàn tay MAYA rìa phải out nét",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, đang QUỲ MỘT GỐI. MAYA chỉ thấy MỘT MẢNG ĐẦU GỐI và bàn tay ở rìa phải, out nét — "
   "KHÔNG thấy mặt.",
   "ADRIAN đặt một tay lên ngực mình rồi hạ xuống đầu gối đang chống",
   [("ADRIAN", "slow, apologising",
     "That was the most arrogant thing I have ever done, and I am sorry.")],
   [("MAYA", "silent, eyes overflowing")])

S("18", "cận 85mm, cao 1m00, cách ADRIAN 1m2, máy hạ rất thấp, lấy ADRIAN nét và một mảng đầu gối MAYA rìa phải",
  "ADRIAN quỳ một gối chiếm phần lớn khung từ ngực trở lên, mặt ngước lên. Ở rìa PHẢI khung thấy một mảng đầu gối "
  "và bàn tay MAYA đang ngồi trên mép giường, out nét. Hậu cảnh là nắng trên tường, xoá phông.",
  "ADRIAN một bàn tay ngửa ra về phía MAYA, tay kia đặt trên đầu gối đang chống.",
  "ADRIAN nhìn thẳng lên mặt MAYA.",
  "ADRIAN — người cầu hôn lần thứ hai, lần này không có gì trong tay: giọng chậm, rõ, mắt ướt, "
  "hơi thở nặng vì hai chân đang gánh cả người, KHÔNG hề bi luỵ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA mở miệng trả lời",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, ADRIAN quỳ một gối",
  {"ADRIAN": "quỳ một gối, chính diện giữa khung",
   "MAYA": "một mảng đầu gối và bàn tay ở rìa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một bàn tay ngửa ra về phía MAYA, tay kia trên đầu gối chống",
                    "MAYA": "hai tay trên đùi, ngoài vùng nét"})
VX("18", "cận 85mm hạ rất thấp · ADRIAN NÉT QUỲ MỘT GỐI chính diện · một mảng đầu gối và bàn tay MAYA rìa phải out nét",
   [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
   "ADRIAN rõ mặt, đang QUỲ MỘT GỐI. MAYA chỉ thấy MỘT MẢNG ĐẦU GỐI và bàn tay ở rìa phải, out nét — "
   "KHÔNG thấy mặt.",
   "ADRIAN giữ nguyên bàn tay ngửa ra về phía MAYA",
   [("ADRIAN", "slow, asking",
     "So I am asking properly this time, on my own two legs, in front of your mother, with nothing to offer you "
     "that you cannot walk away from.")],
   [("MAYA", "silent, about to answer")])

S("19", "two-shot cận-trung 85mm, cao 1m00, cách MAYA 1m5, máy hạ rất thấp lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung trên mép giường, cúi xuống. ADRIAN quỳ một gối ở nửa TRÁI khung. "
  "Hậu cảnh là cửa sổ đầy nắng và bình hoa cúc trắng trên bậu.",
  "MAYA một tay đưa ra chạm vào bàn tay đang ngửa của ADRIAN. ADRIAN một bàn tay ngửa nhận lấy tay cô.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người nhắc lại quy mô tài sản của anh chỉ để cho thấy nó không liên quan: khoé môi kéo lệch, "
  "mắt ướt. ADRIAN — trả lời bằng ba chữ về chính chiếc giường này: giọng nhỏ, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi các ngón tay hai người siết vào nhau",
  ["MAYA_SCRUB", "ADRIAN_VEST"], "buồng bệnh giường 12, ADRIAN quỳ một gối cạnh giường",
  {"MAYA": "ngồi mép giường cúi xuống, nửa phải khung", "ADRIAN": "quỳ một gối nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay đưa ra chạm vào bàn tay ADRIAN",
                    "ADRIAN": "một bàn tay ngửa nhận lấy tay cô"})
V("19", [35, 36], "two-shot cận-trung 85mm hạ rất thấp · ADRIAN NÉT trái QUỲ MỘT GỐI + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, đang QUỲ MỘT GỐI. MAYA rõ mặt ngồi mép giường. Không có ai khác rõ mặt trong khung.",
  "MAYA đưa tay ra chạm vào bàn tay đang ngửa của ADRIAN",
  [("MAYA", "wry, tearful", 35), ("ADRIAN", "quiet, plain", 36)])

S("20", "cận-trung 85mm, cao 1m00, cách MAYA 1m4, máy hạ rất thấp lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung, hai bàn tay đã nắm lấy bàn tay ADRIAN. ADRIAN quỳ một gối ở nửa TRÁI khung. "
  "Hậu cảnh là mảng nắng lớn trên tường buồng bệnh.",
  "MAYA hai tay nắm lấy bàn tay ADRIAN. ADRIAN một tay để trong tay cô, tay kia còn chống trên đầu gối.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người hỏi lại một điều khoản, và lần này để đùa chứ không để phòng thân: khoé môi kéo lên, mắt ướt. "
  "ADRIAN — trả lời bằng một câu mở toang: giọng nhỏ, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi câu cuối cùng của mình",
  ["MAYA_SCRUB", "ADRIAN_VEST"], "buồng bệnh giường 12, ADRIAN quỳ một gối cạnh giường",
  {"MAYA": "ngồi mép giường nửa phải khung", "ADRIAN": "quỳ một gối nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay nắm lấy bàn tay ADRIAN",
                    "ADRIAN": "một tay trong tay cô, tay kia chống trên đầu gối"})
V("20", [37, 38], "cận-trung 85mm hạ rất thấp · ADRIAN NÉT trái QUỲ MỘT GỐI + MAYA NÉT phải nắm lấy tay anh",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, đang QUỲ MỘT GỐI. MAYA rõ mặt ngồi mép giường. Không có ai khác rõ mặt trong khung.",
  "MAYA nắm lấy bàn tay ADRIAN bằng cả hai tay",
  [("MAYA", "wry, warm", 37), ("ADRIAN", "quiet, open", 38)])

S("21", "cận 85mm, cao 1m00, cách MAYA 1m2, máy hạ rất thấp, lấy MAYA nét và một mảng vai ADRIAN rìa trái",
  "MAYA ngồi cúi xuống chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo vest đen "
  "của ADRIAN đang quỳ, out nét. Hậu cảnh là nắng trên tường, xoá phông.",
  "MAYA hai tay còn nắm lấy bàn tay ADRIAN, ngón cái miết một nhịp trên mu bàn tay anh.",
  "MAYA nhìn thẳng xuống mặt ADRIAN.",
  "MAYA — người hỏi một câu vừa đùa vừa thật vì cô là điều dưỡng và cô đang lo cho hai chân anh: "
  "khoé môi kéo lên, mắt tràn nước, giọng vỡ nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN trả lời",
  ["MAYA_SCRUB", "ADRIAN_VEST"], "buồng bệnh giường 12",
  {"MAYA": "ngồi cúi xuống, chính diện giữa khung",
   "ADRIAN": "một mảng vai áo vest đen ở rìa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay nắm bàn tay ADRIAN, ngón cái miết trên mu bàn tay",
                    "ADRIAN": "một tay trong tay cô, ngoài vùng nét"})
V("21", [39, 40, 41], "cận 85mm hạ rất thấp · MAYA NÉT chính diện · một mảng vai áo vest ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_SCRUB"), ("ADRIAN", "ADRIAN_VEST")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI áo vest đen ở rìa trái, out nét — KHÔNG quay mặt về camera.",
  "MAYA miết ngón cái một nhịp trên mu bàn tay ADRIAN",
  [("MAYA", "wry, tearful", 39), ("ADRIAN", "quiet, ready", 40), ("MAYA", "wry, tearful", 41)])

S("22", "two-shot cận-trung 85mm, cao 1m00, cách ADRIAN 1m4, máy hạ rất thấp lấy cả hai người",
  "ADRIAN quỳ một gối ở nửa TRÁI khung, mặt ngước lên. MAYA ngồi cúi xuống ở nửa PHẢI khung, hai tay còn nắm "
  "tay anh. Hậu cảnh là cửa sổ đầy nắng.",
  "ADRIAN một tay trong hai tay MAYA, tay kia chống trên đầu gối. MAYA hai tay nắm chặt lấy tay anh.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — trả lời câu hỏi về hai chân mình bằng bốn chữ: khoé môi kéo lên lần đầu trong cả bộ phim, "
  "mắt sáng. MAYA — nói ra hai chữ mà cả bộ phim chờ: mắt tràn nước, khoé môi kéo rộng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng gọi khàn cất lên từ trên giường",
  ["ADRIAN_VEST", "MAYA_SCRUB"], "buồng bệnh giường 12, ADRIAN quỳ một gối cạnh giường",
  {"ADRIAN": "quỳ một gối nửa trái khung", "MAYA": "ngồi cúi xuống nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay trong hai tay MAYA, tay kia chống trên đầu gối",
                    "MAYA": "hai tay nắm chặt lấy tay anh"})
V("22", [42, 43], "two-shot cận-trung 85mm hạ rất thấp · ADRIAN NÉT trái QUỲ MỘT GỐI + MAYA NÉT phải nắm chặt tay anh",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, đang QUỲ MỘT GỐI. MAYA rõ mặt ngồi mép giường. Không có ai khác rõ mặt trong khung.",
  "MAYA nắm chặt lấy bàn tay ADRIAN bằng cả hai tay",
  [("ADRIAN", "warm, certain", 42), ("MAYA", "tearful, smiling", 43)])

S("23", "trung 50mm, cao 1m00, cách HELEN 2m, máy hạ rất thấp lấy cả ba người",
  "HELEN nằm ở giữa khung trên giường, mắt mở, đầu nghiêng nhìn xuống mép giường. MAYA ngồi ở nửa PHẢI khung "
  "trên mép giường, đã quay đầu lại phía mẹ. ADRIAN quỳ một gối ở nửa TRÁI khung, hai tay còn trong tay MAYA.",
  "HELEN một bàn tay đưa về phía hai người. MAYA một tay còn nắm tay ADRIAN, tay kia đưa về phía mẹ. "
  "ADRIAN một tay trong tay MAYA.",
  "HELEN nhìn ADRIAN đang quỳ. MAYA nhìn mẹ. ADRIAN nhìn HELEN.",
  "HELEN — bà mẹ có ý kiến cuối cùng và đó là một câu rất đời: mắt mở, khoé môi động, giọng khàn. "
  "MAYA — bật cười thành tiếng lần đầu trong cả bộ phim: mắt tràn nước. ADRIAN — khoé môi kéo lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đưa hai tay đỡ ADRIAN đứng lên",
  ["HELEN", "MAYA_SCRUB", "ADRIAN_VEST"], "buồng bệnh giường 12",
  {"HELEN": "nằm trên giường giữa khung, mắt mở", "MAYA": "ngồi mép giường nửa phải khung",
   "ADRIAN": "quỳ một gối nửa trái khung"},
  "ba người trong vòng một mét",
  {"HELEN": "một bàn tay đưa về phía hai người", "MAYA": "một tay nắm tay ADRIAN, tay kia đưa về phía mẹ",
   "ADRIAN": "một tay trong tay MAYA"})
V("23", [44, 45, 46], "trung 50mm hạ rất thấp · ADRIAN NÉT trái QUỲ MỘT GỐI + HELEN NÉT giữa nằm trên giường, MẮT MỞ + MAYA NÉT phải ngồi mép giường",
  [("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN"), ("MAYA", "MAYA_SCRUB")],
  "ADRIAN rõ mặt, đang QUỲ MỘT GỐI. HELEN rõ mặt, nằm trên giường với ĐÔI MẮT ĐANG MỞ. "
  "MAYA rõ mặt ngồi mép giường.",
  "HELEN đưa một bàn tay về phía hai người, MAYA quay đầu lại phía mẹ",
  [("HELEN", "hoarse, warm", 44), ("MAYA", "tearful, laughing", 45), ("HELEN", "hoarse, dry", 46)])

# ── NHỊP KHÉP PHIM ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 5m, đặt ở cửa buồng bệnh nhìn chếch qua cả phòng",
  "Trong buồng bệnh ngập nắng: HELEN nằm trên giường, mắt mở, đầu quay về phía hai người. MAYA đứng cạnh giường, "
  "hai tay đỡ dưới cánh tay ADRIAN. ADRIAN đứng thẳng trên hai chân cạnh cô, một tay còn vịn thành chắn giường.",
  "MAYA hai tay đỡ dưới cánh tay ADRIAN. ADRIAN một tay vịn thành chắn giường, tay kia đặt trên vai MAYA. "
  "HELEN hai tay đặt xuôi trên chăn.",
  "MAYA và ADRIAN nhìn nhau. HELEN nhìn hai người.",
  "MAYA — người đỡ chồng mình đứng lên như đã đỡ anh suốt bảy tháng: mắt ướt, khoé môi kéo rộng. "
  "ADRIAN — đứng được nhờ có cô: mặt bình, mắt sáng. HELEN — mắt mở, khoé môi động.",
  "đúng khoảnh khắc ngay TRƯỚC khi ba người cùng im lặng trong mảng nắng",
  ["MAYA_SCRUB", "ADRIAN_VEST", "HELEN"], "buồng bệnh giường 12, ngập nắng",
  {"MAYA": "đứng cạnh giường đỡ ADRIAN", "ADRIAN": "đứng thẳng cạnh cô, một tay vịn thành chắn giường",
   "HELEN": "nằm trên giường, mắt mở"},
  "ba người trong vòng một mét",
  {"MAYA": "hai tay đỡ dưới cánh tay ADRIAN",
   "ADRIAN": "một tay vịn thành chắn giường, tay kia đặt trên vai MAYA",
   "HELEN": "hai tay đặt xuôi trên chăn"})
B("B2", "[NHỊP] Khép phim. MAYA đỡ ADRIAN đứng dậy cạnh giường 12, HELEN nằm nhìn hai người, cả phòng ngập nắng.",
  "toàn cảnh 24mm · MAYA NÉT đỡ ADRIAN đứng lên + ADRIAN NÉT ĐỨNG THẲNG cạnh cô + HELEN NÉT nằm trên giường, MẮT MỞ",
  [("MAYA", "MAYA_SCRUB"), ("ADRIAN", "ADRIAN_VEST"), ("HELEN", "HELEN")],
  "MAYA, ADRIAN và HELEN rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN, một tay vịn thành chắn giường. "
  "HELEN nằm trên giường với ĐÔI MẮT ĐANG MỞ. Không có người nào khác trong phòng.",
  "cả bộ phim bắt đầu bằng một người đàn ông bị đẩy sang bên lề một lối đi và một người phụ nữ quỳ xuống nhặt "
  "tiền của người khác; nó kết thúc bằng hai người cùng đứng trong một căn phòng ngập nắng, và không ai trong "
  "hai người còn phải một mình.",
  "MAYA đỡ ADRIAN đứng vững rồi vuốt lại vạt áo cho anh; ADRIAN đặt bàn tay lên vai cô; HELEN nhìn hai người "
  "rồi nhắm mắt lại một nhịp dài; mảng nắng dịch chậm trên mặt chăn.",
  "Ambient tiếng bíp đều của máy theo dõi và tiếng chim ngoài cửa sổ, SFX tiếng vải áo vuốt phẳng.",
  nhac("ĐẨY", "Chỗ cuối cùng của cả phim — nhạc được phép chiếm sân khấu hoàn toàn và kết mở, để khán giả ngồi lại với khung hình cuối.",
       "Cinematic soul at 78 BPM; a female alto entering alone close to the mic over a felt piano, strings and a "
       "choir rising slowly underneath from the halfway point, everything reaching one long held chord and then "
       "dropping to piano and a single voice for the last eight seconds; lyrics about two people standing up in the "
       "same room where one of them had no name, grateful and unhurried, never triumphant; warm analog mix, "
       "female vocal, choir, strings, piano, cinematic, luminous",
       "Cinematic instrumental at 78 BPM; felt piano alone, a cello line rising underneath, full strings and a "
       "French horn swelling to one long held chord at the two-thirds point, then everything falling away to piano "
       "and one sustained violin note that fades out unresolved; warm analog mix, piano, cello, strings, horn, "
       "cinematic, luminous"),
  dur=12)
