# -*- coding: utf-8 -*-
"""SCENE 17 — PHÒNG CÔ DÂU, TOÀ THÁP HALE (ban ngày). Ba nghìn đô một ngày."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S17", "REF_SUITE_NGAY", qc=qc.S17)

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 5m, đặt trong phòng nhìn ra cửa đôi sơn trắng",
  "MAYA đứng lại ngay trong khung CỬA ĐÔI SƠN TRẮNG vừa mở, tay ôm một chiếc túi vải. VANESSA ngồi trên ghế đôn "
  "nhung ngà trước bàn trang điểm ở phía trong, đã quay nửa người ra. Phòng ngập ánh sáng ban ngày qua vách kính.",
  "MAYA hai tay ôm chiếc túi vải trước bụng. VANESSA một tay cầm một chiếc lược, tay kia đặt trên mặt đá bàn trang điểm.",
  "MAYA nhìn quanh căn phòng một lượt. VANESSA nhìn MAYA qua gương rồi quay hẳn người lại.",
  "MAYA — người vừa bước vào một căn phòng đắt hơn cả năm lương của mình: mặt bình, mắt quét, cằm ngang. "
  "VANESSA — chủ nhà đang thưởng thức khoảnh khắc này: khoé môi cong, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước hẳn vào trong phòng",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "khung cửa đôi và khu bàn trang điểm",
  {"MAYA": "đứng trong khung cửa đôi", "VANESSA": "ngồi ghế đôn trước bàn trang điểm"},
  "cách nhau sáu mét", {"MAYA": "hai tay ôm chiếc túi vải trước bụng",
                        "VANESSA": "một tay cầm lược, tay kia đặt trên mặt đá"})
B("B1", "Mở cảnh. Phòng cô dâu trên toà tháp Hale. MAYA dừng lại trong khung cửa, VANESSA ngồi trước gương quay ra.",
  "trung-rộng 35mm · MAYA NÉT đứng trong khung cửa đôi + VANESSA NÉT ngồi ghế đôn trước bàn trang điểm",
  [("MAYA", "MAYA_CARDIGAN"), ("VANESSA", "VANESSA_LUA")],
  "MAYA và VANESSA rõ mặt. Không có người nào khác trong phòng.",
  "một người mất nhà tuần trước bước vào căn phòng của người vừa đặt cả một nhà thờ cho đám cưới của mình; "
  "khoảng cách sáu mét giữa hai người chính là nội dung của khung hình.",
  "MAYA dừng lại trong khung cửa và đưa mắt qua bàn trang điểm, giá treo váy, xe đẩy champagne; "
  "VANESSA đặt chiếc lược xuống mặt đá và quay hẳn người ra.",
  "Ambient tiếng điều hoà rất khẽ trên tầng cao và tiếng thành phố xa dưới kính, SFX tiếng lược đặt xuống mặt đá.",
  nhac("KÌM", "Cả cảnh là một cuộc mua bán được gói trong phép lịch sự; nhạc phải sang, lạnh và nén.",
       "Chamber soul at 68 BPM; Rhodes and upright bass only, a female alto entering once with a single low line "
       "close to the mic; no drums; the pull is when everything drops for one bar; lyrics about walking into a room "
       "you will be paid to stand in the corner of; dry mix, female vocal, Rhodes, restrained, cold",
       "Chamber instrumental at 66 BPM; a harp figure repeating politely over a sustained cello note, an upright bass "
       "underneath, no percussion, ending on an unresolved chord; elegant and cold, harp, cello, upright bass, "
       "chamber, unresolved"),
  dur=6)

# ── LỜI ĐỀ NGHỊ ──
S("01", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt trong phòng lấy cả hai người",
  "VANESSA ngồi ở nửa TRÁI khung trên ghế đôn nhung ngà, người xoay hẳn ra. MAYA đứng ở nửa PHẢI khung, "
  "đã vào giữa phòng, chiếc túi vải còn trên tay. Hậu cảnh là bộ sofa nhung ngà và bàn trà mặt đá tròn.",
  "VANESSA một tay vắt lên lưng ghế đôn, tay kia đặt trên đùi. MAYA hai tay ôm chiếc túi vải trước bụng.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "VANESSA — người mời khách vào bằng giọng của người ban ơn: khoé môi cong, cằm hếch. "
  "MAYA — vào thẳng việc, không chào hỏi: mặt bình, giọng gọn.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA đứng dậy khỏi ghế đôn",
  ["VANESSA_LUA", "MAYA_CARDIGAN"], "giữa phòng cô dâu",
  {"VANESSA": "ngồi ghế đôn nửa trái khung", "MAYA": "đứng giữa phòng nửa phải khung"},
  "cách nhau ba mét", {"VANESSA": "một tay vắt lưng ghế đôn, tay kia trên đùi",
                       "MAYA": "hai tay ôm chiếc túi vải"})
V("01", [0, 1], "trung 50mm · VANESSA NÉT trái ngồi ghế đôn + MAYA NÉT phải đứng giữa phòng",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "VANESSA vẫy tay mời vào, MAYA bước vào giữa phòng và đứng lại",
  [("VANESSA", "bright, patronising", 0), ("MAYA", "flat, businesslike", 1)])

S("02", "cận-trung 85mm, cao 1m55, cách VANESSA 1m7, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "VANESSA đứng chính diện chiếm phần lớn khung, đã đứng dậy khỏi ghế đôn. MAYA chỉ còn là vai và gáy ở rìa PHẢI "
  "tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng VANESSA là gương lớn viền bóng đèn tròn.",
  "VANESSA một tay đặt lên mặt đá bàn trang điểm, tay kia khoát nhẹ trong không khí theo nhịp nói.",
  "VANESSA nhìn thẳng vào mặt MAYA.",
  "VANESSA — người trình bày lý do bằng giọng của một người rất biết điều: giọng nhẹ, đều, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nêu ra bốn mươi công ty dịch vụ",
  ["VANESSA_LUA", "MAYA_CARDIGAN"], "trước bàn trang điểm",
  {"VANESSA": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau ba mét", {"VANESSA": "một tay trên mặt đá bàn trang điểm, tay kia khoát nhẹ",
                       "MAYA": "hai tay ôm chiếc túi vải, ngoài vùng nét"})
V("02", [2], "OTS cận-trung 85mm · VANESSA NÉT chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "VANESSA đứng dậy khỏi ghế đôn, một tay chống lên mặt đá bàn trang điểm",
  [("VANESSA", "smooth, reasonable", 2)], [("MAYA", "silent, listening")])

S("03", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt trong phòng lấy cả hai người đứng",
  "MAYA đứng ở nửa PHẢI khung giữa phòng, VANESSA đứng ở nửa TRÁI khung trước bàn trang điểm. "
  "Hậu cảnh là vách kính suốt trần tới sàn và bầu trời ban ngày.",
  "MAYA một tay chỉ ra phía cửa rồi hạ xuống. VANESSA hai tay khoanh nhẹ trước ngực.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đưa ra lối thoát hợp lý nhất cho cả hai: giọng bình, mắt thẳng. "
  "VANESSA — không nhận lối thoát đó: khoé môi cong, giọng nhẹ và dứt khoát.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi một chữ",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "giữa phòng cô dâu",
  {"MAYA": "đứng giữa phòng nửa phải khung", "VANESSA": "đứng trước bàn trang điểm nửa trái khung"},
  "cách nhau ba mét", {"MAYA": "một tay chỉ ra phía cửa rồi hạ xuống",
                       "VANESSA": "hai tay khoanh nhẹ trước ngực"})
V("03", [3, 4, 5], "trung 50mm · VANESSA NÉT trái trước bàn trang điểm + MAYA NÉT phải đứng giữa phòng",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "MAYA chỉ ra phía cửa rồi hạ tay xuống, VANESSA khoanh tay lại",
  [("MAYA", "even, practical", 3), ("VANESSA", "light, final", 4), ("MAYA", "flat, direct", 5)])

S("04", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, máy sau vai TRÁI của VANESSA; vai và gáy cô chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. VANESSA chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng MAYA là cửa đôi sơn trắng và xe đẩy phục vụ bằng đồng.",
  "MAYA hai tay đặt chiếc túi vải xuống thành sofa cạnh mình.",
  "MAYA nhìn thẳng vào mặt VANESSA.",
  "MAYA — người nghe con số và không phản ứng gì trên mặt: mặt hoàn toàn bình, mắt thẳng, giọng gọn.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA bắt đầu đọc ra các điều kiện",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "giữa phòng cô dâu, cạnh bộ sofa",
  {"MAYA": "đứng chính diện giữa khung", "VANESSA": "vai và gáy tiền cảnh trái"},
  "cách nhau ba mét", {"MAYA": "hai tay đặt chiếc túi vải xuống thành sofa",
                       "VANESSA": "hai tay khoanh trước ngực, ngoài vùng nét"})
V("04", [6, 7], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy VANESSA tiền cảnh trái out nét",
  [("MAYA", "MAYA_CARDIGAN"), ("VANESSA", "VANESSA_LUA")],
  "MAYA rõ mặt chính diện. VANESSA chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đặt chiếc túi vải xuống thành sofa và hỏi lại",
  [("VANESSA", "brisk, transactional", 6), ("MAYA", "flat, unreadable", 7)])

S("05", "trung 50mm, cao 1m55, cách VANESSA 2m2, đặt trong phòng lấy VANESSA nét và MAYA cùng khung",
  "VANESSA đứng ở nửa TRÁI khung, đã bước ra giữa phòng. MAYA đứng ở nửa PHẢI khung cạnh bộ sofa. "
  "Hậu cảnh là giá treo váy bằng đồng có túi vải trắng dài đựng váy cưới.",
  "VANESSA một tay giữ ly champagne ngang ngực, tay kia chống hông. MAYA hai tay buông dọc thân.",
  "VANESSA nhìn MAYA. MAYA nhìn lại VANESSA.",
  "VANESSA — người ra điều kiện như đọc nội quy cho nhân viên: giọng đều, nhẹ, khoé môi giữ nét cười. "
  "MAYA — nghe từng chữ và không chớp mắt: mặt phẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA quay hẳn lưng lại phía MAYA",
  ["VANESSA_LUA", "MAYA_CARDIGAN"], "giữa phòng cô dâu",
  {"VANESSA": "đứng giữa phòng nửa trái khung", "MAYA": "đứng cạnh bộ sofa nửa phải khung"},
  "cách nhau hai bước", {"VANESSA": "một tay đếm bằng ngón tay, tay kia chống hông",
                         "MAYA": "hai tay buông dọc thân"})
V("05", [8], "trung 50mm · VANESSA NÉT trái đứng giữa phòng ra điều kiện + MAYA NÉT phải cạnh bộ sofa",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "VANESSA đếm từng điều kiện trên đầu ngón tay",
  [("VANESSA", "light, listing", 8)], [("MAYA", "silent, not blinking")])

S("06", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, đặt trong phòng lấy MAYA nét và VANESSA cùng khung",
  "MAYA đứng ở nửa PHẢI khung, VANESSA đứng ở nửa TRÁI khung cách hai bước. Hậu cảnh là vách kính và "
  "chậu cây lá cọ lớn.",
  "MAYA một tay chỉ vào chính bộ đồ mình đang mặc rồi hạ xuống. VANESSA một tay xoay chiếc nhẫn ở ngón áp út.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người nói ra thành lời đúng bức tranh mà cô kia đang vẽ: giọng bình, chậm, mắt thẳng. "
  "VANESSA — bọc lại bằng lý do y tế: khoé môi cong, giọng ngọt.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng cửa đôi mở ra phía sau MAYA",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "giữa phòng cô dâu",
  {"MAYA": "đứng nửa phải khung", "VANESSA": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "một tay chỉ vào bộ đồ mình đang mặc rồi hạ xuống",
                         "VANESSA": "một tay xoay chiếc nhẫn ở ngón áp út"})
V("06", [9, 10], "cận-trung 85mm · VANESSA NÉT trái + MAYA NÉT phải, đứng đối diện giữa phòng",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "MAYA chỉ vào bộ đồ mình đang mặc rồi hạ tay xuống",
  [("MAYA", "slow, level", 9), ("VANESSA", "sweet, deflecting", 10)])

S("07", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt trong phòng lấy cả ba người",
  "RYAN đứng ở nửa TRÁI khung ngay trong khung cửa đôi vừa mở, một tay còn trên tay nắm. MAYA đứng ở giữa khung, "
  "đã quay nửa người lại về phía cửa. VANESSA đứng ở nửa PHẢI khung, thấy rõ mặt.",
  "RYAN một tay giữ tay nắm cửa, tay kia đút túi quần. MAYA hai tay buông dọc thân. VANESSA hai tay khoanh trước ngực.",
  "RYAN nhìn MAYA. MAYA quay lại nhìn RYAN. VANESSA nhìn cả hai.",
  "RYAN — người xen vào bằng giọng thân mật giả tạo: khoé môi kéo, mắt sáng. "
  "MAYA — quay lại và chỉ gọi đúng tên anh ta: mặt phẳng. VANESSA — thích thú: mày nhướn.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước hẳn vào phòng",
  ["RYAN_SOMI", "MAYA_CARDIGAN", "VANESSA_LUA"], "giữa phòng cô dâu, phía cửa đôi",
  {"RYAN": "đứng trong khung cửa đôi nửa trái khung", "MAYA": "đứng giữa khung, quay nửa người lại",
   "VANESSA": "đứng nửa phải khung"},
  "ba người trong vòng ba mét",
  {"RYAN": "một tay giữ tay nắm cửa, tay kia đút túi", "MAYA": "hai tay buông dọc thân",
   "VANESSA": "hai tay khoanh trước ngực"})
V("07", [11, 12, 13], "trung 50mm · RYAN NÉT trái trong khung cửa + MAYA NÉT giữa + VANESSA NÉT phải",
  [("RYAN", "RYAN_SOMI"), ("MAYA", "MAYA_CARDIGAN"), ("VANESSA", "VANESSA_LUA")],
  "RYAN, MAYA và VANESSA, cả ba rõ mặt. Không có ai khác trong phòng.",
  "RYAN đẩy cửa đôi bước vào, MAYA quay nửa người lại nhìn anh ta",
  [("RYAN", "false-friendly, easy", 11), ("MAYA", "flat, warning", 12),
   ("RYAN", "boastful, light", 13)])

S("08", "cận-trung 85mm, cao 1m55, cách MAYA 1m5, đặt trong phòng lấy MAYA nét và VANESSA mờ rìa trái",
  "MAYA đứng chính diện chiếm phần lớn khung. Ở rìa TRÁI khung thấy VANESSA đứng, MỜ ngoài vùng nét. "
  "Hậu cảnh là bàn trang điểm và gương viền bóng đèn tròn, xoá phông.",
  "MAYA hai tay buông dọc thân, một bàn tay khép lại rất chậm.",
  "MAYA nhìn thẳng về phía VANESSA.",
  "MAYA — người vừa ghép ra một chi tiết mà cô kia tưởng cô không biết: mắt hơi nheo, giọng chậm hẳn, "
  "mặt không đổi.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA hỏi lại một chữ",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "giữa phòng cô dâu",
  {"MAYA": "đứng chính diện giữa khung", "VANESSA": "đứng mờ ở rìa trái khung"},
  "cách nhau hai bước", {"MAYA": "hai tay buông dọc thân, một bàn tay khép lại chậm",
                         "VANESSA": "hai tay khoanh trước ngực, ngoài vùng nét"})
V("08", [14, 15, 16], "cận-trung 85mm · MAYA NÉT chính diện · VANESSA mờ ở rìa trái khung",
  [("MAYA", "MAYA_CARDIGAN"), ("VANESSA", "VANESSA_LUA")],
  "MAYA rõ mặt chính diện. VANESSA chỉ thấy MỜ ở rìa trái khung, KHÔNG rõ mặt.",
  "MAYA đứng yên, bàn tay khép lại rất chậm trong lúc nói",
  [("MAYA", "slowing, quiet", 14), ("VANESSA", "clipped, thrown", 15), ("MAYA", "flat, precise", 16)])

S("09", "trung 50mm, cao 1m55, cách VANESSA 2m2, đặt trong phòng lấy cả hai người",
  "VANESSA đứng ở nửa TRÁI khung, một tay chống lên thành sofa. MAYA đứng ở nửa PHẢI khung. "
  "Hậu cảnh là vách kính suốt trần tới sàn và bầu trời ban ngày.",
  "VANESSA một tay chống lên thành sofa, tay kia phẩy nhẹ. MAYA hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "VANESSA — người thừa nhận rất thoải mái vì không thấy có gì phải giấu: khoé môi cong, giọng nhẹ. "
  "MAYA — nói ra đúng bản chất của việc đặt chỗ đó: giọng thấp, chậm, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA bật cười một tiếng ngắn",
  ["VANESSA_LUA", "MAYA_CARDIGAN"], "giữa phòng cô dâu, cạnh bộ sofa",
  {"VANESSA": "đứng cạnh sofa nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau hai bước", {"VANESSA": "một tay chống thành sofa, tay kia phẩy nhẹ",
                         "MAYA": "hai tay buông dọc thân"})
V("09", [17, 18], "trung 50mm · VANESSA NÉT trái cạnh sofa + MAYA NÉT phải đứng đối diện",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA và MAYA, cả hai rõ mặt. Không có ai khác trong phòng.",
  "VANESSA chống một tay lên thành sofa và phẩy tay kia",
  [("VANESSA", "light, careless", 17), ("MAYA", "low, precise", 18)])

S("10", "cận-trung 85mm, cao 1m55, cách VANESSA 1m6, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "VANESSA đứng chính diện chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng VANESSA là giá treo váy bằng đồng và túi vải trắng đựng váy cưới.",
  "VANESSA một tay đưa lên vuốt nhẹ mái tóc, tay kia buông.",
  "VANESSA nhìn thẳng vào mặt MAYA.",
  "VANESSA — người dùng giọng dịu dàng nhất để nói câu ác nhất: đầu nghiêng, khoé môi cong, mắt sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhắc lại con số ba nghìn",
  ["VANESSA_LUA", "MAYA_CARDIGAN"], "giữa phòng cô dâu",
  {"VANESSA": "đứng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau hai bước", {"VANESSA": "một tay vuốt nhẹ mái tóc, tay kia buông",
                         "MAYA": "hai tay buông dọc thân, ngoài vùng nét"})
V("10", [19], "OTS cận-trung 85mm · VANESSA NÉT chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "VANESSA vuốt nhẹ mái tóc và nói bằng giọng dịu dàng nhất của mình",
  [("VANESSA", "sweet, cutting", 19)], [("MAYA", "silent, not moving")])

S("11", "cận-trung 85mm, cao 1m55, cách MAYA 1m5, đặt trong phòng lấy MAYA nét và VANESSA cùng khung",
  "MAYA đứng ở nửa PHẢI khung, VANESSA đứng ở nửa TRÁI khung cách hai bước. Hậu cảnh là cửa đôi sơn trắng "
  "và xe đẩy phục vụ bằng đồng.",
  "MAYA một tay siết lại rồi mở ra, tay kia cầm quai chiếc túi vải trên thành sofa. "
  "VANESSA hai tay đan trước bụng.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người nói ra lý do thật của mình mà không hạ giọng: giọng đều, mắt thẳng, KHÔNG xin xỏ. "
  "VANESSA — nhận được đúng thứ mình muốn: khoé môi kéo rộng.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA quay sang phía người đàn ông đứng cạnh cửa",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "giữa phòng cô dâu, cạnh bộ sofa",
  {"MAYA": "đứng nửa phải khung", "VANESSA": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "một tay siết lại rồi mở ra, tay kia cầm quai túi vải",
                         "VANESSA": "hai tay đan trước bụng"})
V("11", [20, 21, 22], "cận-trung 85mm · VANESSA NÉT trái + MAYA NÉT phải, đứng đối diện giữa phòng",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA nhắc lại con số, siết bàn tay lại rồi mở ra và nhận lời",
  [("MAYA", "flat, checking", 20), ("VANESSA", "light, confirming", 21),
   ("MAYA", "plain, unashamed", 22)])

S("12", "trung 50mm, cao 1m55, cách VANESSA 2m4, đặt trong phòng lấy cả ba người",
  "VANESSA đứng ở giữa khung, đã quay sang phía RYAN. RYAN đứng ở nửa TRÁI khung, đã rút điện thoại ra. "
  "MAYA đứng ở nửa PHẢI khung, tay cầm quai chiếc túi vải. Hậu cảnh là bàn trang điểm và gương.",
  "VANESSA một tay hất về phía RYAN. RYAN hai tay cầm chiếc điện thoại, ngón cái đang gõ. "
  "MAYA một tay cầm quai chiếc túi vải.",
  "VANESSA nhìn RYAN. RYAN nhìn xuống màn hình điện thoại. MAYA nhìn VANESSA.",
  "VANESSA — người ghi tên một người vào lịch như ghi một món đồ thuê: giọng vui, nhẹ. "
  "RYAN — gõ vào điện thoại và nhắc lại như một thư ký: mặt phẳng. MAYA — mặt không đổi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay người về phía cửa đôi",
  ["VANESSA_LUA", "RYAN_SOMI", "MAYA_CARDIGAN"], "giữa phòng cô dâu",
  {"VANESSA": "đứng giữa khung", "RYAN": "đứng nửa trái khung cầm điện thoại",
   "MAYA": "đứng nửa phải khung"},
  "ba người trong vòng ba mét",
  {"VANESSA": "một tay hất về phía RYAN", "RYAN": "hai tay cầm điện thoại, ngón cái gõ",
   "MAYA": "một tay cầm quai chiếc túi vải"})
V("12", [23, 24], "trung 50mm · RYAN NÉT trái cầm điện thoại + VANESSA NÉT giữa + MAYA NÉT phải",
  [("RYAN", "RYAN_SOMI"), ("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "RYAN, VANESSA và MAYA, cả ba rõ mặt. Không có ai khác trong phòng.",
  "VANESSA hất tay về phía RYAN, RYAN rút điện thoại ra gõ vào đó",
  [("VANESSA", "bright, brisk", 23), ("RYAN", "flat, secretarial", 24)],
  ketclip="Cuối clip, MAYA xách chiếc túi vải lên và quay người bước về phía cửa đôi. "
          "Clip dừng đúng lúc cô quay lưng lại được một bước.")

S("13", "cận-trung 85mm, cao 1m55, cách VANESSA 1m7, đặt trong phòng lấy VANESSA nét và MAYA đang quay lưng ở rìa phải",
  "VANESSA đứng chính diện ở nửa TRÁI khung, đã nói với theo. MAYA đứng ở rìa PHẢI khung, đã quay lưng lại "
  "về phía cửa đôi, chỉ thấy VAI VÀ GÁY, đang dừng bước.",
  "VANESSA một tay giơ lên ngang vai gọi với theo, tay kia chống hông. MAYA một tay cầm quai chiếc túi vải.",
  "VANESSA nhìn theo lưng MAYA. MAYA dừng lại, không quay đầu.",
  "VANESSA — người ném thêm một câu cuối chỉ để cho vui: khoé môi kéo rộng, mắt sáng. "
  "MAYA — dừng bước, vai cứng lại, KHÔNG quay đầu.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước tiếp ra cửa",
  ["VANESSA_LUA", "MAYA_CARDIGAN"], "giữa phòng cô dâu, phía cửa đôi",
  {"VANESSA": "đứng chính diện nửa trái khung", "MAYA": "quay lưng ở rìa phải khung, đang dừng bước"},
  "cách nhau ba mét", {"VANESSA": "một tay giơ ngang vai gọi với theo, tay kia chống hông",
                       "MAYA": "một tay cầm quai chiếc túi vải"})
V("13", [25], "cận-trung 85mm · VANESSA NÉT trái chính diện · MAYA chỉ thấy VAI VÀ GÁY ở rìa phải, đang quay lưng",
  [("VANESSA", "VANESSA_LUA"), ("MAYA", "MAYA_CARDIGAN")],
  "VANESSA rõ mặt chính diện. MAYA chỉ thấy VAI VÀ GÁY ở rìa phải khung, đang quay lưng về phía cửa — "
  "TUYỆT ĐỐI KHÔNG quay mặt lại về camera.",
  "VANESSA giơ tay gọi với theo lưng MAYA, MAYA dừng bước nhưng không quay đầu",
  [("VANESSA", "bright, cruel", 25)], [("MAYA", "silent, back turned, stopping")])

# ── NHỊP KHÉP CẢNH ──
S("B2", "trung-rộng 35mm, cao 1m60, cách MAYA 6m, đặt trong phòng nhìn ra cửa đôi sơn trắng đang mở",
  "MAYA đã ra tới ngưỡng CỬA ĐÔI SƠN TRẮNG, quay lưng lại phía trong phòng, một tay còn trên tay nắm cửa. "
  "Phía sau cô trong phòng, VANESSA đứng quay lưng lại phía cửa, đối diện với gương lớn ở bàn trang điểm.",
  "MAYA một tay trên tay nắm cửa, tay kia xách chiếc túi vải. VANESSA hai tay chỉnh lại mái tóc trước gương.",
  "MAYA nhìn thẳng ra hành lang phía trước. VANESSA nhìn vào gương, KHÔNG quay lại.",
  "MAYA — người vừa nhận ba nghìn đô để đứng góc phòng ở đám cưới của người đã cướp chồng mình: vai cân, "
  "lưng thẳng, KHÔNG quay đầu lại. VANESSA — đã quên cô ngay khi việc xong: mặt bình trong gương.",
  "đúng khoảnh khắc ngay TRƯỚC khi cánh cửa đôi khép lại sau lưng MAYA",
  ["MAYA_CARDIGAN", "VANESSA_LUA"], "ngưỡng cửa đôi phòng cô dâu",
  {"MAYA": "đứng ở ngưỡng cửa, quay lưng lại phía trong phòng",
   "VANESSA": "đứng quay lưng lại phía cửa, trước gương bàn trang điểm"},
  "cách nhau sáu mét", {"MAYA": "một tay trên tay nắm cửa, tay kia xách chiếc túi vải",
                        "VANESSA": "hai tay chỉnh lại mái tóc trước gương"})
B("B2", "Khép cảnh. MAYA ra tới cửa, quay lưng lại; phía sau, VANESSA đứng trước gương và đã quên cô.",
  "trung-rộng 35mm · MAYA QUAY LƯNG ở ngưỡng cửa đôi + VANESSA QUAY LƯNG đứng trước gương phía trong phòng",
  [("MAYA", "MAYA_CARDIGAN"), ("VANESSA", "VANESSA_LUA")],
  "MAYA và VANESSA đều chỉ thấy TỪ PHÍA SAU, cả hai QUAY LƯNG lại — TUYỆT ĐỐI KHÔNG ai quay mặt về camera. "
  "Không có người nào khác trong khung.",
  "một người vừa bán ba nghìn đô lấy chỗ đứng ở góc phòng trong ngày cưới của kẻ đã lấy đi mọi thứ của mình, "
  "và người kia đã quên chuyện đó trước cả khi cửa khép lại.",
  "MAYA đứng lại một nhịp ở ngưỡng cửa rồi bước ra hành lang; VANESSA vuốt lại một lọn tóc trước gương và "
  "không quay lại; cánh cửa đôi từ từ khép.",
  "Ambient tiếng điều hoà trên tầng cao và tiếng thành phố rất xa dưới kính, SFX tiếng bản lề cửa và tiếng khoá cửa.",
  nhac("NGHỈ", "Không được cho khán giả một cú giải toả ở đây; nhạc phải trung tính và lạnh để cơn giận dồn tiếp sang cảnh sau.",
       "Minimal piano at 62 BPM; upright piano placing four notes with heavy sustain, a female voice entering once "
       "with a single half-spoken line near the end; no drums, no bass; the pull is a long silence before that line; "
       "lyrics about taking the money because the medication costs what it costs; dry mix, female vocal, piano, "
       "minimal, cold",
       "Minimal instrumental at 60 BPM; upright piano and a very low synth pad, four notes repeating with heavy "
       "sustain, one harp note near the end, no percussion, thinning to nothing; cold clean mix, piano, pad, harp, "
       "minimal"),
  dur=8)
