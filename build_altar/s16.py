# -*- coding: utf-8 -*-
"""SCENE 16 — NHÀ CỔNG, BUỔI SÁNG BỊ TRỤC XUẤT. Bốn tiếng và một chiếc xe lăn cũ."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S16", "REF_CONGNHA_SANG", qc=qc.S16)

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 8m, đặt trên đường phục vụ nhìn về phía căn nhà cổng",
  "MAYA đứng ở chân ba bậc đá trước cửa nhà cổng, giữa bốn thùng carton và hai túi vải đã dọn ra sân. "
  "ADRIAN ngồi trong xe lăn điện cạnh cô. Trên đường phục vụ phía sau đỗ một xe tải nhỏ màu trắng mở thùng.",
  "MAYA một tay giữ mép một thùng carton, tay kia buông. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn về phía đường phục vụ. ADRIAN nhìn theo hướng đó.",
  "MAYA — người đang dọn nhà từ sáng sớm và chưa biết chuyện gì sắp tới: tóc buộc vội, tay áo xắn, mặt tập trung. "
  "ADRIAN — mặt bình, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi một chiếc xe khác rẽ vào đường phục vụ",
  ["MAYA_THUONG", "ADRIAN_XANHREU"], "sân trước căn nhà cổng, cạnh ba bậc đá",
  {"MAYA": "đứng giữa đống thùng carton", "ADRIAN": "ngồi xe lăn điện cạnh cô"},
  "sát cạnh nhau", {"MAYA": "một tay giữ mép thùng carton", "ADRIAN": "hai tay trên vành tay vịn"})
B("B1", "Mở cảnh. Sáng hôm sau. Đồ đạc đã dọn ra sân trước nhà cổng, một xe tải nhỏ đỗ trên đường phục vụ.",
  "toàn cảnh 24mm · MAYA NÉT đứng giữa đống thùng carton + ADRIAN NÉT ngồi xe lăn điện cạnh cô",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XANHREU")],
  "MAYA và ADRIAN rõ mặt. Không có người nào khác trong khung.",
  "phiên toà thắng được hai ngày, và cái giá của nó đang nằm ngoài sân dưới dạng bốn thùng carton.",
  "MAYA đặt một thùng carton lên chồng, phủi tay rồi nhìn ra đường phục vụ; ADRIAN quay đầu nhìn theo; "
  "cỏ còn ướt sương, trời xám ít mây.",
  "Ambient tiếng chim buổi sáng và tiếng gió qua hàng cây phong, SFX tiếng bìa carton cọ vào nhau.",
  nhac("KÌM", "Hai người vừa thắng ở toà và bị đuổi khỏi nhà ngay sáng hôm sau — nhạc phải nén, không được bi luỵ.",
       "Soul ballad at 62 BPM with a female alto very close to the mic, dry and half-spoken; Rhodes and upright bass "
       "only, no drums; one held note at the midpoint then straight back to voice; lyrics about packing a house that "
       "was never yours at seven in the morning, never self-pitying; dry intimate mix, female vocal, soul, "
       "restrained, sparse",
       "Chamber instrumental at 60 BPM; a cello holding one long low note under a felt-piano figure repeating and "
       "thinning, a viola answering once, no percussion, ending unresolved; very quiet morning mix, cello, viola, "
       "piano, minimal"),
  dur=8)

# ── LỆNH TRỤC XUẤT ──
S("01", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt trên sân trước nhà cổng lấy cả hai người",
  "SHERIFF'S DEPUTY đứng ở nửa TRÁI khung, đã chìa ra một TỜ GIẤY MÀU VÀNG CANARY. MAYA đứng ở nửa PHẢI khung "
  "trước đống thùng carton, chưa cầm lấy tờ giấy. Hậu cảnh là tường gạch đỏ và ba bậc đá.",
  "SHERIFF'S DEPUTY một tay chìa tờ giấy vàng ra, tay kia giữ một bìa kẹp hồ sơ. MAYA hai tay còn phủi bụi carton.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "SHERIFF'S DEPUTY — người chỉ đang làm việc và biết việc này khó coi: mắt né một nhịp, giọng đều, lễ độ. "
  "MAYA — nhận ra sắc giấy đó nghĩa là gì: mặt cứng lại, tay dừng phủi bụi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA cầm lấy tờ giấy",
  ["SHERIFF'S DEPUTY", "MAYA_THUONG", "PROP_THONGBAO"], "sân trước căn nhà cổng",
  {"SHERIFF'S DEPUTY": "đứng nửa trái khung, chìa tờ giấy", "MAYA": "đứng nửa phải khung trước đống thùng"},
  "cách nhau một bước", {"SHERIFF'S DEPUTY": "một tay chìa tờ giấy vàng, tay kia giữ bìa kẹp hồ sơ",
                         "MAYA": "hai tay phủi bụi carton"})
V("01", [0, 1, 2], "trung 50mm · SHERIFF'S DEPUTY NÉT trái chìa tờ giấy + MAYA NÉT phải đứng trước đống thùng",
  [("SHERIFF'S DEPUTY", "SHERIFF'S DEPUTY"), ("MAYA", "MAYA_THUONG")],
  "SHERIFF'S DEPUTY và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "SHERIFF'S DEPUTY chìa tờ giấy màu vàng ra, MAYA dừng tay phủi bụi",
  [("SHERIFF'S DEPUTY", "polite, formal", 0), ("MAYA", "flat, steady", 1),
   ("SHERIFF'S DEPUTY", "even, uncomfortable", 2)])

S("02", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, máy sau vai TRÁI của SHERIFF'S DEPUTY; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, TỜ GIẤY MÀU VÀNG CANARY đã ở trong tay cô. SHERIFF'S DEPUTY chỉ còn "
  "là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là tường gạch đỏ loang rêu.",
  "MAYA hai tay cầm tờ giấy vàng, một ngón lần theo dòng chữ in đậm ở đầu trang.",
  "MAYA đọc tờ giấy rồi ngẩng lên nhìn thẳng vào mặt SHERIFF'S DEPUTY.",
  "MAYA — người vừa thắng ở toà hai ngày trước và không hiểu nổi tờ giấy này: mày chau sâu, giọng nhanh, "
  "mắt quét lại tờ giấy một lần nữa.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng xe khác dừng lại trên đường phục vụ",
  ["MAYA_THUONG", "SHERIFF'S DEPUTY", "PROP_THONGBAO"], "sân trước căn nhà cổng",
  {"MAYA": "đứng chính diện giữa khung, cầm tờ giấy vàng",
   "SHERIFF'S DEPUTY": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "hai tay cầm tờ giấy vàng, một ngón lần theo dòng chữ",
                         "SHERIFF'S DEPUTY": "một tay giữ bìa kẹp hồ sơ, ngoài vùng nét"})
V("02", [3, 4], "OTS cận-trung 85mm · MAYA NÉT chính diện cầm tờ giấy vàng · vai và gáy SHERIFF'S DEPUTY tiền cảnh trái out nét",
  [("MAYA", "MAYA_THUONG"), ("SHERIFF'S DEPUTY", "SHERIFF'S DEPUTY")],
  "MAYA rõ mặt chính diện. SHERIFF'S DEPUTY chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đọc tờ giấy vàng rồi ngẩng phắt lên",
  [("MAYA", "fast, incredulous", 3), ("SHERIFF'S DEPUTY", "even, procedural", 4)])

S("03", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt trên sân trước nhà cổng lấy cả hai người",
  "JULIAN đứng ở nửa TRÁI khung, vừa từ phía đường phục vụ bước tới, tay đút túi quần. MAYA đứng ở nửa PHẢI khung, "
  "tờ giấy vàng còn trong tay. Hậu cảnh là cổng sắt uốn đen và toà nhà chính trên đồi.",
  "JULIAN một tay đút túi quần, tay kia chỉnh lại cổ tay áo. MAYA một tay cầm tờ giấy vàng hạ xuống ngang hông.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JULIAN — người đến tận nơi để xem bằng mắt: khoé môi kéo lên, mắt sáng. "
  "MAYA — không ngạc nhiên một chút nào: mặt phẳng, giọng khô.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN bước thêm một bước tới gần",
  ["JULIAN", "MAYA_THUONG", "PROP_THONGBAO"], "sân trước căn nhà cổng",
  {"JULIAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau hai bước", {"JULIAN": "một tay đút túi quần, tay kia chỉnh cổ tay áo",
                         "MAYA": "một tay cầm tờ giấy vàng hạ ngang hông"})
V("03", [5, 6], "trung 50mm · JULIAN NÉT trái + MAYA NÉT phải cầm tờ giấy vàng · cổng sắt ở hậu cảnh",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_THUONG")],
  "JULIAN và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "JULIAN bước tới từ phía đường phục vụ và chỉnh lại cổ tay áo",
  [("JULIAN", "pleasant, gloating", 5), ("MAYA", "dry, unsurprised", 6)])

S("04", "cận-trung 85mm, cao 1m55, cách JULIAN 1m7, đặt trên sân lấy JULIAN nét và MAYA cùng khung",
  "JULIAN đứng ở nửa TRÁI khung, đã tới sát. MAYA đứng ở nửa PHẢI khung. Hậu cảnh là tường gạch đỏ nhà cổng "
  "và cửa nhà kho gỗ mở toang.",
  "JULIAN hai tay đút túi quần âu. MAYA hai tay buông xuống, tờ giấy trong một tay.",
  "JULIAN nhìn MAYA rồi liếc về phía chiếc xe lăn ngoài khung. MAYA nhìn thẳng vào JULIAN.",
  "JULIAN — người đọc ra ba biện pháp như đọc thực đơn: giọng nhẹ, đều, khoé môi giữ nét cười. "
  "MAYA — bắt lỗi ngay câu cuối: mày nhướn, giọng gọn.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN quay hẳn sang phía chiếc xe lăn",
  ["JULIAN", "MAYA_THUONG"], "sân trước căn nhà cổng",
  {"JULIAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau một bước", {"JULIAN": "một tay đếm bằng ngón tay, tay kia đút túi",
                         "MAYA": "hai tay buông, một tay cầm tờ giấy"})
V("04", [7, 8], "cận-trung 85mm · JULIAN NÉT trái + MAYA NÉT phải, đứng đối diện trên sân",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_THUONG")],
  "JULIAN và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "JULIAN đếm ba biện pháp trên đầu ngón tay",
  [("JULIAN", "light, listing", 7), ("MAYA", "clipped, correcting", 8)])

S("05", "trung 50mm, cao 1m40, cách ADRIAN 2m4, đặt trên sân, hạ thấp để lấy cả người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn điện ở nửa PHẢI khung. JULIAN đứng ở nửa TRÁI khung, một tay chỉ thẳng vào chiếc xe lăn. "
  "MAYA đứng giữa khung phía sau, thấy rõ mặt. Hậu cảnh là ba bậc đá và cửa gỗ nâu.",
  "JULIAN một tay chỉ vào chiếc xe lăn. ADRIAN hai tay đặt trên vành tay vịn. MAYA một tay đưa ra phía trước cản.",
  "JULIAN nhìn chiếc xe lăn. ADRIAN nhìn JULIAN. MAYA nhìn JULIAN.",
  "JULIAN — người gọi một thiết bị y tế là tài sản gia đình: giọng nhẹ, mắt sáng. "
  "MAYA — bước lên chắn: mày chau, giọng cứng. ADRIAN — mặt hoàn toàn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai người mặc đồ bảo hộ bước vào khung từ phía xe tải",
  ["ADRIAN_XANHREU", "JULIAN", "MAYA_THUONG"], "sân trước căn nhà cổng, cạnh chiếc xe lăn",
  {"ADRIAN": "ngồi xe lăn điện nửa phải khung", "JULIAN": "đứng nửa trái khung",
   "MAYA": "đứng giữa khung phía sau"},
  "ba người trong vòng hai mét",
  {"JULIAN": "một tay chỉ vào chiếc xe lăn", "ADRIAN": "hai tay trên vành tay vịn",
   "MAYA": "một tay đưa ra phía trước cản"})
V("05", [9, 10, 11], "trung 50mm hạ thấp · JULIAN NÉT trái chỉ vào xe lăn + MAYA NÉT giữa + ADRIAN NÉT phải ngồi xe lăn điện",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XANHREU")],
  "JULIAN, MAYA và ADRIAN, cả ba rõ mặt. ADRIAN ngồi trong CHIẾC XE LĂN ĐIỆN màu đen. Không có ai khác trong khung.",
  "JULIAN chỉ thẳng vào chiếc xe lăn, MAYA bước lên chắn một bước",
  [("JULIAN", "light, cold", 9), ("MAYA", "hard, correcting", 10), ("JULIAN", "smooth, final", 11)])

S("06", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m6, đặt bên xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn điện ở nửa TRÁI khung. MAYA đứng ở nửa PHẢI khung, đã quay hẳn xuống nhìn anh, "
  "một tay bám vào tay đẩy xe. Hậu cảnh là tường gạch đỏ và đống thùng carton.",
  "ADRIAN một tay đưa lên đặt trên bàn tay MAYA đang bám tay đẩy xe. MAYA một tay bám tay đẩy xe, tay kia nắm lại.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người quyết định không giữ lại thứ có thể bị lấy: giọng rất bình, mắt tĩnh. "
  "MAYA — không chịu nổi việc đứng nhìn: mắt đỏ, quai hàm siết, giọng vỡ một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA buông tay khỏi tay đẩy xe",
  ["ADRIAN_XANHREU", "MAYA_THUONG"], "sân trước căn nhà cổng, cạnh chiếc xe lăn",
  {"ADRIAN": "ngồi xe lăn điện nửa trái khung", "MAYA": "đứng cúi xuống nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay đặt lên bàn tay MAYA trên tay đẩy xe",
                    "MAYA": "một tay bám tay đẩy xe, tay kia nắm lại"})
V("06", [12, 13, 14], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn điện + MAYA NÉT phải cúi xuống",
  [("ADRIAN", "ADRIAN_XANHREU"), ("MAYA", "MAYA_THUONG")],
  "ADRIAN và MAYA, cả hai rõ mặt. ADRIAN ngồi trong CHIẾC XE LĂN ĐIỆN màu đen. Không có ai khác trong khung.",
  "ADRIAN đặt tay lên bàn tay MAYA đang bám tay đẩy xe",
  [("ADRIAN", "quiet, resigned", 12), ("MAYA", "breaking, low", 13), ("ADRIAN", "firm, gentle", 14)],
  ketclip="Cuối clip, hai người mặc đồ bảo hộ khiêng chiếc xe lăn điện đi khỏi khung, ADRIAN được đặt sang một "
          "CHIẾC XE LĂN TAY CŨ khung thép xám vành trái cong. Clip dừng đúng lúc anh ngồi vững trong chiếc xe cũ.")

# ── CHIẾC XE TAY CŨ ──
S("07", "trung 50mm, cao 1m40, cách ADRIAN 2m2, đặt trên sân, hạ thấp để lấy cả người ngồi xe lăn",
  "ADRIAN ngồi trong CHIẾC XE LĂN TAY CŨ khung thép xám ở nửa PHẢI khung, xe hơi nghiêng vì vành bánh trái cong. "
  "JULIAN đứng ở nửa TRÁI khung. MAYA đứng giữa khung phía sau chiếc xe, một tay đặt lên lưng ghế.",
  "JULIAN một tay chỉ về phía nhà kho gỗ, tay kia đút túi. ADRIAN hai tay đặt trên vành bánh xe. "
  "MAYA một tay đặt lên lưng ghế xe lăn.",
  "JULIAN nhìn chiếc xe cũ. MAYA nhìn xuống bánh xe trái. ADRIAN nhìn thẳng phía trước.",
  "JULIAN — người tặng một món đồ hỏng và gọi đó là quà: khoé môi kéo rộng. "
  "MAYA — nhìn ra ngay khuyết tật của chiếc xe: mày chau. ADRIAN — mặt hoàn toàn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quỳ xuống xem bánh xe",
  ["ADRIAN_XELANTAY", "JULIAN", "MAYA_THUONG"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"ADRIAN": "ngồi xe lăn tay cũ nửa phải khung", "JULIAN": "đứng nửa trái khung",
   "MAYA": "đứng sau chiếc xe, giữa khung"},
  "ba người trong vòng hai mét",
  {"JULIAN": "một tay chỉ về phía nhà kho, tay kia đút túi", "ADRIAN": "hai tay đặt trên vành bánh xe",
   "MAYA": "một tay đặt lên lưng ghế xe lăn"})
V("07", [15, 16], "trung 50mm hạ thấp · JULIAN NÉT trái + MAYA NÉT giữa sau xe + ADRIAN NÉT phải ngồi xe lăn tay cũ",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "JULIAN, MAYA và ADRIAN, cả ba rõ mặt. ADRIAN đã ngồi trong CHIẾC XE LĂN TAY CŨ khung thép xám, vành bánh "
  "trái cong nên xe hơi nghiêng. Không có ai khác trong khung.",
  "JULIAN chỉ về phía nhà kho gỗ, MAYA nhìn xuống bánh xe trái của chiếc xe cũ",
  [("JULIAN", "pleasant, mocking", 15), ("MAYA", "flat, observing", 16)])

S("08", "cận-trung 85mm, cao 1m55, cách JULIAN 1m6, đặt trên sân lấy JULIAN nét và MAYA cùng khung",
  "JULIAN đứng ở nửa TRÁI khung, đã rút một tờ giấy gập tư từ túi áo trong ra và giữ nó trong tay. "
  "MAYA đứng ở nửa PHẢI khung. Hậu cảnh là cổng sắt uốn đen và bãi cỏ ướt sương.",
  "JULIAN một tay giơ tờ giấy gập tư lên ngang ngực, tay kia đút túi. MAYA hai tay buông xuống hai bên.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JULIAN — người vừa lôi ra lá bài bẩn nhất và dùng giọng ôn tồn nhất: khoé môi kéo lên, mắt lạnh. "
  "MAYA — không chớp mắt: mặt phẳng, cằm ngang.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN gập tờ giấy lại và cất vào túi",
  ["JULIAN", "MAYA_THUONG"], "sân trước căn nhà cổng",
  {"JULIAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau một bước", {"JULIAN": "một tay giơ tờ giấy gập tư ngang ngực, tay kia đút túi",
                         "MAYA": "hai tay buông xuống hai bên"})
V("08", [17], "cận-trung 85mm · JULIAN NÉT trái giơ tờ giấy gập tư + MAYA NÉT phải đứng đối diện",
  [("JULIAN", "JULIAN"), ("MAYA", "MAYA_THUONG")],
  "JULIAN và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "JULIAN rút một tờ giấy gập tư từ túi áo trong ra và giơ lên ngang ngực",
  [("JULIAN", "smooth, threatening", 17)], [("MAYA", "silent, not blinking")])

S("09", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, máy sau vai TRÁI của JULIAN; vai và gáy ông chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. JULIAN chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng MAYA là ba bậc đá, tấm ván ép và đống thùng carton.",
  "MAYA hai tay buông dọc thân, các ngón duỗi thẳng.",
  "MAYA nhìn thẳng vào mặt JULIAN.",
  "MAYA — người không buồn tranh cãi về cách người ta gọi tên chuyện của mình: giọng rất bình, "
  "mắt không dời, KHÔNG hằn học.",
  "đúng khoảnh khắc ngay TRƯỚC khi JULIAN đưa ra lời đề nghị cuối cùng",
  ["MAYA_THUONG", "JULIAN"], "sân trước căn nhà cổng",
  {"MAYA": "đứng chính diện giữa khung", "JULIAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "hai tay buông dọc thân",
                         "JULIAN": "một tay cầm tờ giấy gập tư, ngoài vùng nét"})
V("09", [18, 19], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy JULIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_THUONG"), ("JULIAN", "JULIAN")],
  "MAYA rõ mặt chính diện. JULIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đứng yên, hai tay buông dọc thân, trả lời rất bình",
  [("MAYA", "level, unbothered", 18), ("JULIAN", "soft, tempting", 19)])

S("10", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt trên sân lấy MAYA nét và SHERIFF'S DEPUTY cùng khung",
  "MAYA đứng ở nửa PHẢI khung, đã quay hẳn người sang phía SHERIFF'S DEPUTY. SHERIFF'S DEPUTY đứng ở nửa TRÁI "
  "khung, bìa kẹp hồ sơ trong tay. Hậu cảnh là xe tải nhỏ màu trắng đỗ trên đường phục vụ.",
  "MAYA một tay giơ tờ giấy vàng lên ngang ngực. SHERIFF'S DEPUTY một tay giữ bìa kẹp hồ sơ, tay kia buông.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người bỏ qua lời đề nghị và quay sang hỏi đúng cái mình cần biết: giọng gọn, mắt thẳng. "
  "SHERIFF'S DEPUTY — trả lời ngắn, hơi ngại: mắt hạ xuống một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay lại phía chiếc xe lăn",
  ["MAYA_THUONG", "SHERIFF'S DEPUTY", "PROP_THONGBAO"], "sân trước căn nhà cổng",
  {"MAYA": "đứng nửa phải khung", "SHERIFF'S DEPUTY": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "một tay giơ tờ giấy vàng ngang ngực",
                         "SHERIFF'S DEPUTY": "một tay giữ bìa kẹp hồ sơ"})
V("10", [20, 21], "trung 50mm · SHERIFF'S DEPUTY NÉT trái + MAYA NÉT phải giơ tờ giấy vàng",
  [("SHERIFF'S DEPUTY", "SHERIFF'S DEPUTY"), ("MAYA", "MAYA_THUONG")],
  "SHERIFF'S DEPUTY và MAYA, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA quay sang phía viên phó cảnh sát và giơ tờ giấy vàng lên ngang ngực",
  [("MAYA", "brisk, practical", 20), ("SHERIFF'S DEPUTY", "quiet, uncomfortable", 21)])

S("11", "trung 50mm, cao 1m30, cách MAYA 2m, đặt trên sân, hạ thấp để lấy cả người ngồi xe lăn tay cũ",
  "MAYA đứng ở nửa PHẢI khung sau chiếc xe lăn tay cũ, hai tay đã đặt lên tay đẩy. ADRIAN ngồi trong chiếc xe "
  "tay cũ ở nửa TRÁI khung. Hậu cảnh là đống thùng carton và ba bậc đá.",
  "MAYA hai tay đặt trên tay đẩy chiếc xe cũ. ADRIAN hai tay đặt trên vành bánh xe.",
  "MAYA nhìn xuống ADRIAN. ADRIAN nhìn thẳng phía trước.",
  "MAYA — người vừa gạt phăng lời đề nghị và chuyển sang kế hoạch tiếp theo trong đúng một câu: giọng nhanh, "
  "gọn, thực tế. ADRIAN — nghe cô nói về một căn phòng bốn mươi mốt đô: mắt hơi động.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đẩy chiếc xe cũ về phía xe tải",
  ["MAYA_THUONG", "ADRIAN_XELANTAY"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"MAYA": "đứng sau chiếc xe cũ nửa phải khung", "ADRIAN": "ngồi xe lăn tay cũ nửa trái khung"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay đặt trên tay đẩy chiếc xe cũ",
                          "ADRIAN": "hai tay đặt trên vành bánh xe"})
V("11", [22], "trung 50mm hạ thấp · MAYA NÉT phải đứng sau xe lăn tay cũ + ADRIAN NÉT trái ngồi trong xe",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN ngồi trong CHIẾC XE LĂN TAY CŨ khung thép xám. Không có ai khác trong khung.",
  "MAYA đặt hai tay lên tay đẩy chiếc xe cũ và nói xuống",
  [("MAYA", "brisk, planning", 22)], [("ADRIAN", "silent, listening")])

S("12", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m5, đặt bên chiếc xe cũ, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong chiếc xe lăn tay cũ ở nửa TRÁI khung, đã quay đầu lại nhìn lên. MAYA đứng ở nửa PHẢI khung "
  "sau chiếc xe, đã cúi xuống. Hậu cảnh là bãi cỏ ướt sương và hàng cây phong.",
  "ADRIAN một tay bám vành bánh xe, tay kia đưa lên chạm vào bàn tay MAYA trên tay đẩy. "
  "MAYA hai tay còn trên tay đẩy xe.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người mở đúng cánh cửa để cô đi ra nếu cô muốn: giọng rất nhỏ, mắt thẳng, KHÔNG tự thương. "
  "MAYA — trả lời hai chữ và không nói thêm: mặt bình, mắt không dời.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN hỏi câu tiếp theo",
  ["ADRIAN_XELANTAY", "MAYA_THUONG"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"ADRIAN": "ngồi xe lăn tay cũ nửa trái khung", "MAYA": "đứng cúi xuống sau xe, nửa phải khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay bám vành bánh xe, tay kia chạm vào bàn tay MAYA",
                    "MAYA": "hai tay trên tay đẩy xe"})
V("12", [23, 24, 25], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn tay cũ + MAYA NÉT phải cúi xuống",
  [("ADRIAN", "ADRIAN_XELANTAY"), ("MAYA", "MAYA_THUONG")],
  "ADRIAN và MAYA, cả hai rõ mặt. ADRIAN ngồi trong chiếc xe lăn tay cũ. Không có ai khác trong khung.",
  "ADRIAN đưa tay lên chạm vào bàn tay MAYA đang đặt trên tay đẩy xe",
  [("ADRIAN", "quiet, offering", 23), ("MAYA", "flat, plain", 24), ("ADRIAN", "quiet, pressing", 25)])

S("13", "cận 85mm, cao 1m20, cách MAYA 1m2, đặt bên chiếc xe cũ, hạ thấp, lấy MAYA nét và một mảng vai ADRIAN rìa trái",
  "MAYA cúi chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo len xanh rêu và tay vịn "
  "chiếc xe lăn tay cũ của ADRIAN, out nét. Hậu cảnh là tường gạch đỏ xoá phông.",
  "MAYA một tay còn trên tay đẩy xe, tay kia đưa lên chạm vào cằm ADRIAN xoay mặt anh về phía mình.",
  "MAYA nhìn thẳng vào mặt ADRIAN.",
  "MAYA — người đã đếm được cả những lần anh nhìn đi chỗ khác và giờ nói ra: giọng chậm, ấm, mắt không dời, "
  "KHÔNG trách móc.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nói ra chỗ mình sẽ kê chiếc giường",
  ["MAYA_THUONG", "ADRIAN_XELANTAY"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"MAYA": "cúi xuống, chính diện giữa khung",
   "ADRIAN": "một mảng vai áo len và tay vịn xe lăn cũ ở rìa trái"},
  "rất gần nhau", {"MAYA": "một tay trên tay đẩy xe, tay kia chạm vào cằm ADRIAN",
                   "ADRIAN": "hai tay trên vành bánh xe, ngoài vùng nét"})
V("13", [26], "cận 85mm hạ thấp · MAYA NÉT cúi xuống chính diện · một mảng vai và tay vịn xe lăn cũ của ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI áo len xanh rêu và tay vịn chiếc xe lăn cũ ở rìa trái, out nét — "
  "KHÔNG quay mặt về camera.",
  "MAYA đưa tay lên chạm vào cằm ADRIAN và xoay mặt anh về phía mình",
  [("MAYA", "slow, warm", 26)], [("ADRIAN", "silent, held there")])

S("14", "two-shot trung 50mm, cao 1m20, cách MAYA 1m9, đặt trên sân, hạ thấp ngang tầm người ngồi xe lăn tay cũ",
  "MAYA đứng ở nửa PHẢI khung sau chiếc xe cũ, đã đứng thẳng lại. ADRIAN ngồi trong chiếc xe tay cũ ở nửa TRÁI "
  "khung, mặt ngước lên. Hậu cảnh là căn nhà cổng và bầu trời xám sáng.",
  "MAYA một tay chỉ về phía một hướng ngoài khung, tay kia đặt trên tay đẩy xe. "
  "ADRIAN một tay bám vành bánh xe.",
  "MAYA nhìn về hướng mình đang chỉ rồi nhìn xuống ADRIAN. ADRIAN nhìn MAYA.",
  "MAYA — người mô tả hai tiếng nắng như mô tả một liều thuốc: giọng bình, mắt sáng lên, khoé môi động. "
  "ADRIAN — nghe một người nói về hai giờ đồng hồ của mình như thể chúng quan trọng: mắt đỏ lên, mặt vẫn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đẩy chiếc xe cũ đi về phía xe tải",
  ["MAYA_THUONG", "ADRIAN_XELANTAY"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"MAYA": "đứng sau chiếc xe cũ nửa phải khung", "ADRIAN": "ngồi xe lăn tay cũ nửa trái khung"},
  "MAYA sát sau ADRIAN", {"MAYA": "một tay chỉ ra ngoài khung, tay kia trên tay đẩy xe",
                          "ADRIAN": "một tay bám vành bánh xe"})
V("14", [27], "two-shot trung 50mm hạ thấp · MAYA NÉT phải đứng sau xe lăn tay cũ + ADRIAN NÉT trái ngồi trong xe",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XELANTAY")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN ngồi trong chiếc xe lăn tay cũ. Không có ai khác trong khung.",
  "MAYA chỉ tay về một hướng ngoài khung và nói xuống phía anh",
  [("ADRIAN", "quiet, asking", 27)],
  [("MAYA", "silent, pointing")])

S("14b", "cận-trung 85mm, cao 1m20, cách MAYA 1m5, máy hạ thấp, lấy MAYA nét và ADRIAN trong khung",
  "MAYA đứng ở nửa PHẢI khung sau chiếc xe lăn tay cũ, đã cúi xuống ngang tầm mặt ADRIAN, một tay còn chỉ "
  "về hướng vừa nãy. ADRIAN ngồi trong chiếc xe tay cũ ở nửa TRÁI khung, mặt ngước lên.",
  "MAYA một tay chỉ về hướng ngoài khung, tay kia đặt trên vai ADRIAN. ADRIAN một tay bám vành bánh xe.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người mô tả hai tiếng nắng như mô tả một liều thuốc và biết đó là tất cả những gì mình có: "
  "giọng ấm, chắc, mắt sáng. ADRIAN — nghe ai đó nói về hai giờ đồng hồ của mình như thể chúng quan trọng: "
  "mắt đỏ lên, mặt vẫn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng thẳng lại và đẩy chiếc xe đi",
  ["MAYA_THUONG", "ADRIAN_XELANTAY"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"MAYA": "đứng cúi xuống sau chiếc xe cũ, nửa phải khung", "ADRIAN": "ngồi xe lăn tay cũ nửa trái khung"},
  "sát nhau", {"MAYA": "một tay chỉ ra ngoài khung, tay kia đặt trên vai ADRIAN",
               "ADRIAN": "một tay bám vành bánh xe"})
VX("14b", "cận-trung 85mm hạ thấp · MAYA NÉT phải cúi xuống + ADRIAN NÉT trái ngồi xe lăn tay cũ",
   [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XELANTAY")],
   "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN ngồi trong chiếc xe lăn tay cũ. Không có ai khác trong khung.",
   "MAYA cúi xuống ngang tầm mặt anh, một tay đặt lên vai anh",
   [("MAYA", "warm, certain",
     "Because in the afternoon the sun comes over that building and it lands right there for two hours.")],
   [("ADRIAN", "silent, eyes reddening")])

S("14c", "cận 85mm, cao 1m20, cách MAYA 1m3, máy hạ thấp, lấy MAYA nét và một mảng vai ADRIAN rìa trái",
  "MAYA cúi xuống chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo len xanh rêu và "
  "tay vịn chiếc xe lăn tay cũ của ADRIAN, out nét. Hậu cảnh là căn nhà cổng và bầu trời xám sáng.",
  "MAYA một tay còn đặt trên vai ADRIAN, tay kia mở ra ngang hông rồi hạ xuống.",
  "MAYA nhìn thẳng xuống mặt ADRIAN.",
  "MAYA — người biết hai tiếng nắng là tất cả những gì mình có thể cho và vẫn nói ra: giọng ấm, chậm, "
  "mắt sáng, KHÔNG áy náy.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng thẳng lại và đẩy chiếc xe đi",
  ["MAYA_THUONG", "ADRIAN_XELANTAY"], "sân trước căn nhà cổng, cạnh chiếc xe lăn tay cũ",
  {"MAYA": "cúi xuống, chính diện giữa khung",
   "ADRIAN": "một mảng vai áo len và tay vịn xe lăn cũ ở rìa trái"},
  "rất gần nhau", {"MAYA": "một tay trên vai ADRIAN, tay kia mở ra ngang hông rồi hạ xuống",
                   "ADRIAN": "một tay bám vành bánh xe, ngoài vùng nét"})
VX("14c", "cận 85mm hạ thấp · MAYA NÉT cúi xuống chính diện · một mảng vai và tay vịn xe lăn cũ ADRIAN rìa trái out nét",
   [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_XELANTAY")],
   "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI áo len xanh rêu và tay vịn chiếc xe lăn cũ ở rìa trái, out nét — "
   "KHÔNG quay mặt về camera.",
   "MAYA mở một bàn tay ra ngang hông rồi hạ xuống",
   [("MAYA", "warm, certain",
     "You have been in the dark for six months. Two hours is not much, but it is what I have.")],
   [("ADRIAN", "silent, eyes reddening")])
