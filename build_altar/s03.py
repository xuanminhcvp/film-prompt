# -*- coding: utf-8 -*-
"""SCENE 3 — TIỆM CẦM ĐỒ và SẢNH NGÂN HÀNG (ban ngày)."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S3", "REF_CAMDO_NGAY", qc=qc.S3)
NH = "REF_NGANHANG_NGAY"

# ── NHỊP MỞ CẢNH: TIỆM CẦM ĐỒ ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 5m, đặt sau quầy kính nhìn ra phía cửa tiệm",
  "MAYA vừa đẩy cửa kính bước vào tiệm, dừng lại ngay trong cửa, vẫn nguyên váy cưới. Trước mặt cô là quầy kính dài "
  "và giá tường treo đầy đồ cũ.",
  "MAYA một tay còn giữ mép cánh cửa kính, tay kia nắm chặt một chiếc túi nhung nhỏ màu đỏ sẫm.",
  "MAYA nhìn thẳng vào mặt quầy kính trước mặt.",
  "MAYA — người đang mang thứ cuối cùng mình có đi bán và biết rõ điều đó: cằm ngẩng, môi mím, mắt tỉnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi cánh cửa kính sau lưng cô khép lại",
  ["MAYA_CUOI"], "ngay trong cửa tiệm cầm đồ",
  {"MAYA": "đứng một mình trong cửa"}, "một mình trong khung",
  {"MAYA": "một tay giữ mép cửa, tay kia nắm túi nhung đỏ"})
B("B1", "Mở cảnh. MAYA đẩy cửa bước vào tiệm cầm đồ, vẫn nguyên váy cưới, tay nắm một chiếc túi nhung nhỏ.",
  "trung-rộng 35mm · MAYA NÉT đứng một mình trong cửa tiệm · không có ai khác trong khung",
  [("MAYA", "MAYA_CUOI")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, đứng ngay trong cửa tiệm. Không có người nào khác trong tiệm.",
  "một người vừa đi bộ tới đây trong bộ váy cưới của chính mình để bán nốt thứ cuối cùng còn bán được.",
  "MAYA đứng lại một nhịp trong cửa, đưa mắt qua các giá đồ cũ rồi bước tới quầy; cánh cửa kính sau lưng khép lại "
  "và chiếc chuông nhỏ trên cửa rung.",
  "SFX tiếng chuông cửa nhỏ và tiếng gót giày trên nền gạch, Ambient tiếng quạt trần và tiếng phố rất xa.",
  nhac("NGHỈ", "Chương mới của một ngày dài — cần một nhịp thở trước chuỗi từ chối liên tiếp sắp tới.",
       "Sparse blues at 62 BPM; one electric guitar played clean and very quiet with lots of room, a female voice "
       "entering half-spoken after eight seconds; brushed snare only in the last third; the pull is a bar where the "
       "guitar stops and only the room remains; lyrics about carrying the last thing you own into a shop; "
       "warm analog mix, female vocal, blues, sparse, dusty",
       "Instrumental at 60 BPM; clean electric guitar with tape delay playing one repeating figure, an upright bass "
       "walking very slowly underneath, no drums, ending on an unresolved chord left to ring out; "
       "warm analog mix, guitar, upright bass, dusty, unresolved"),
  dur=8)

# ── TIỆM CẦM ĐỒ ──
S("01", "two-shot trung 50mm, cao 1m50, cách MAYA 2m2, đặt chếch bên quầy để lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung trước quầy kính, PAWN BROKER đứng ở nửa TRÁI khung sau quầy. Trên tấm đệm nhung xám "
  "giữa quầy có MỘT CHIẾC NHẪN VÀNG TRƠN BẢN MẢNH ĐÃ XỈN và chiếc túi nhung đỏ đã mở miệng nằm cạnh.",
  "PAWN BROKER một tay cầm chiếc kính lúp thợ kim hoàn đưa lên hốc mắt, tay kia kẹp chiếc nhẫn giữa hai ngón. "
  "MAYA hai tay đặt lên mép quầy kính.",
  "PAWN BROKER nhìn vào chiếc nhẫn qua kính lúp. MAYA nhìn chiếc nhẫn trong tay ông.",
  "PAWN BROKER — người đã định giá hàng nghìn thứ như thế này: mặt phẳng, giọng nghề nghiệp. "
  "MAYA — nhìn thứ mẹ mình đeo bốn mươi năm nằm trong tay người lạ: quai hàm siết, mắt không rời chiếc nhẫn.",
  "đúng khoảnh khắc ngay TRƯỚC khi PAWN BROKER hạ kính lúp xuống",
  ["MAYA_CUOI", "PAWN BROKER", "PROP_NHAN"], "hai bên quầy kính tiệm cầm đồ",
  {"MAYA": "đứng trước quầy nửa phải khung", "PAWN BROKER": "đứng sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "hai tay đặt lên mép quầy kính",
                             "PAWN BROKER": "một tay cầm kính lúp, tay kia kẹp chiếc nhẫn"})
V("01", [0, 1], "two-shot trung 50mm · PAWN BROKER NÉT trái sau quầy + MAYA NÉT phải trước quầy",
  [("MAYA", "MAYA_CUOI"), ("PAWN BROKER", "PAWN BROKER")],
  "PAWN BROKER và MAYA, cả hai rõ mặt hai bên quầy kính. Không có ai khác trong tiệm.",
  "PAWN BROKER soi chiếc nhẫn qua kính lúp rồi hạ xuống, MAYA nhìn theo chiếc nhẫn",
  [("PAWN BROKER", "matter-of-fact", 0), ("MAYA", "quiet, precise", 1)])

S("02", "cận-trung 85mm, cao 1m50, cách MAYA 1m7, máy sau vai TRÁI của PAWN BROKER; vai và gáy ông chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, phía sau lưng cô là mặt tiền kính sáng của tiệm. PAWN BROKER chỉ còn "
  "là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Trên mặt quầy giữa hai người là chiếc nhẫn vàng đã được đặt xuống.",
  "MAYA một tay chống lên mép quầy, tay kia đưa về phía chiếc nhẫn rồi dừng lại giữa chừng.",
  "MAYA nhìn thẳng vào mặt PAWN BROKER qua vai ông.",
  "MAYA — người vừa nghe một con số nhỏ hơn nhiều so với thứ mình mang tới: mày nhíu, môi hé, giọng vẫn lễ độ.",
  "đúng khoảnh khắc ngay TRƯỚC khi PAWN BROKER nhắc lại con số",
  ["MAYA_CUOI", "PAWN BROKER", "PROP_NHAN"], "hai bên quầy kính tiệm cầm đồ",
  {"MAYA": "đứng chính diện giữa khung", "PAWN BROKER": "vai và gáy tiền cảnh trái"},
  "cách nhau một mặt quầy", {"MAYA": "một tay chống mép quầy, tay kia đưa về phía chiếc nhẫn",
                             "PAWN BROKER": "hai tay đặt trên quầy, ngoài vùng nét"})
V("02", [2, 3, 4], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy PAWN BROKER tiền cảnh trái out nét",
  [("MAYA", "MAYA_CUOI"), ("PAWN BROKER", "PAWN BROKER")],
  "MAYA rõ mặt chính diện. PAWN BROKER chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "PAWN BROKER đặt chiếc nhẫn xuống mặt đệm nhung, MAYA đưa tay về phía nó rồi dừng lại",
  [("PAWN BROKER", "flat, final", 2), ("MAYA", "measured, hopeful", 3),
   ("PAWN BROKER", "unmoved, even", 4)])

S("03", "trung 50mm, cao 1m50, cách MAYA 2m2, đặt chếch bên quầy để lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, đã lùi nửa bước khỏi quầy. PAWN BROKER đứng ở nửa TRÁI khung sau quầy, đã bỏ kính lúp "
  "xuống mặt quầy. Chiếc nhẫn vàng vẫn nằm trên tấm đệm nhung xám giữa hai người.",
  "MAYA một tay chỉ ra phía cửa kính sau lưng mình rồi hạ xuống. PAWN BROKER hai tay chống lên mép quầy.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đang lục ra mọi thứ còn có thể bán: giọng nhanh, mắt tính toán. "
  "PAWN BROKER — nghe câu này mỗi ngày: lắc đầu một cái rất nhỏ, mặt không đổi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hạ tay xuống",
  ["MAYA_CUOI", "PAWN BROKER", "PROP_NHAN"], "hai bên quầy kính tiệm cầm đồ",
  {"MAYA": "đứng lùi nửa bước nửa phải khung", "PAWN BROKER": "đứng sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "một tay chỉ ra phía cửa", "PAWN BROKER": "hai tay chống mép quầy"})
V("03", [5, 6], "trung 50mm · MAYA NÉT phải trước quầy + PAWN BROKER NÉT trái sau quầy",
  [("MAYA", "MAYA_CUOI"), ("PAWN BROKER", "PAWN BROKER")],
  "MAYA và PAWN BROKER, cả hai rõ mặt hai bên quầy kính. Không có ai khác trong tiệm.",
  "MAYA chỉ tay ra phía cửa tiệm, PAWN BROKER lắc đầu một cái rất nhỏ",
  [("MAYA", "quick, practical", 5), ("PAWN BROKER", "flat, tired", 6)])

S("04", "cận-trung 85mm, cao 1m50, cách MAYA 1m6, đặt chếch bên quầy lấy MAYA nét và PAWN BROKER trong khung",
  "MAYA đứng ở nửa PHẢI khung, hai vai chùng xuống. PAWN BROKER đứng ở nửa TRÁI khung sau quầy, đã dừng tay lại. "
  "Chiếc nhẫn vàng nằm giữa hai người trên tấm đệm nhung.",
  "MAYA hai tay buông xuống hai bên, các ngón mở ra. PAWN BROKER một tay đặt hờ cạnh chiếc nhẫn.",
  "MAYA nhìn xuống chiếc nhẫn trên quầy. PAWN BROKER nhìn MAYA.",
  "MAYA — người đang giải thích không phải để mặc cả mà để có một người biết mình đã thử hết cách: giọng đều, "
  "mắt khô. PAWN BROKER — lần đầu trong cảnh này thật sự nhìn kỹ người đối diện: mày hơi chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi PAWN BROKER nhìn xuống bộ váy cưới của cô",
  ["MAYA_CUOI", "PAWN BROKER", "PROP_NHAN"], "hai bên quầy kính tiệm cầm đồ",
  {"MAYA": "đứng nửa phải khung, vai chùng", "PAWN BROKER": "đứng sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "hai tay buông xuống hai bên", "PAWN BROKER": "một tay đặt hờ cạnh chiếc nhẫn"})
V("04", [7, 8], "cận-trung 85mm · MAYA NÉT phải trước quầy + PAWN BROKER NÉT trái sau quầy",
  [("MAYA", "MAYA_CUOI"), ("PAWN BROKER", "PAWN BROKER")],
  "MAYA và PAWN BROKER, cả hai rõ mặt. Không có ai khác trong tiệm.",
  "MAYA nói ra hết một hơi rồi im, PAWN BROKER nhìn kỹ bộ váy cô đang mặc",
  [("MAYA", "plain, exhausted", 7), ("PAWN BROKER", "gentle, blunt", 8)])

S("05", "cận 85mm, cao 1m50, cách MAYA 1m2, đặt chính diện, hậu cảnh là giá tường treo đồ cũ xoá phông",
  "MAYA đứng chính diện chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai của PAWN BROKER "
  "đứng sau quầy, out nét. Hậu cảnh là giá tường treo nhạc cụ và va li cũ, xoá phông mềm.",
  "MAYA một tay đưa lên chạm vào cổ mình rồi hạ xuống.",
  "MAYA nhìn thẳng vào mặt PAWN BROKER.",
  "MAYA — người vừa bị nhắc rằng mình vẫn đang mặc váy cưới và không có gì để nói thêm về chuyện đó: "
  "mắt chớp một cái, khoé môi động một nhịp gần thành nụ cười rồi thôi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đưa tay ra nhận tiền",
  ["MAYA_CUOI", "PAWN BROKER"], "trước quầy kính tiệm cầm đồ",
  {"MAYA": "đứng chính diện giữa khung", "PAWN BROKER": "một mảng vai rìa trái khung, sau quầy"},
  "cách nhau một mặt quầy", {"MAYA": "một tay chạm vào cổ rồi hạ xuống", "PAWN BROKER": "hai tay trên quầy, ngoài vùng nét"})
V("05", [9], "cận 85mm · MAYA NÉT chính diện · một mảng vai PAWN BROKER rìa trái out nét",
  [("MAYA", "MAYA_CUOI"), ("PAWN BROKER", "PAWN BROKER")],
  "MAYA rõ mặt chính diện. PAWN BROKER chỉ thấy MỘT MẢNG VAI ở rìa trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đưa tay chạm vào cổ mình rồi trả lời rất khẽ",
  [("MAYA", "quiet, wry", 9)], [("PAWN BROKER", "silent, counting out notes")])

# ── NHỊP CẦU NỐI SANG NGÂN HÀNG ──
S("B2", "trung-rộng 35mm, cao 1m60, cách MAYA 6m, đặt giữa sảnh ngân hàng nhìn về khu tư vấn", "",
  "", "", "", "",
  ["MAYA_CUOI"], "", {}, "", {}, bg=NH)
SFS[-1]["prompt"] = (
    "MÁY QUAY: trung-rộng 35mm, ống kính cao 1m60, cách MAYA 6m, đặt giữa sảnh ngân hàng nhìn chếch về khu tư vấn\n\n"
    "AI VÀ ĐANG LÀM GÌ: MAYA ngồi một mình trên chiếc ghế khách bọc nỉ xám trước một bàn tư vấn trống, vẫn nguyên "
    "váy cưới. Trên mặt bàn trước mặt cô là một tập giấy tờ và một xấp phiếu lương đã kẹp lại. Ghế bên kia bàn "
    "chưa có ai ngồi. Sảnh ngân hàng vắng.\n\n"
    "TAY: MAYA hai tay đặt chồng lên nhau trên mép bàn, ngón cái miết vào mép tập giấy.\n\n"
    "HƯỚNG NHÌN: MAYA nhìn xuống tập giấy tờ trước mặt.\n\n"
    "BIỂU CẢM: MAYA — người đã ngồi ở cái ghế này ba lần trong tám ngày và vẫn phải ngồi thêm lần nữa: "
    "vai giữ thẳng, mặt bình, mắt hơi đỏ.\n\n"
    "ĐÓNG BĂNG: đúng khoảnh khắc ngay TRƯỚC khi có người kéo chiếc ghế bên kia bàn ra ngồi xuống")
SFS[-1]["pose"] = {"zone": "khu tư vấn sảnh ngân hàng", "who": {"MAYA": "ngồi một mình trước bàn tư vấn"},
                   "dist": "một mình trong khung", "hands": {"MAYA": "hai tay chồng lên nhau trên mép bàn"}}
B("B2", "Cầu nối sang ngân hàng. MAYA ngồi một mình trước bàn tư vấn trống, giấy tờ và phiếu lương đã bày sẵn.",
  "trung-rộng 35mm · MAYA NÉT ngồi một mình trước bàn tư vấn · không có ai khác trong khung",
  [("MAYA", "MAYA_CUOI")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, ngồi trước một bàn tư vấn trống. Không có nhân viên nào trong khung.",
  "vẫn là buổi sáng đó, vẫn bộ váy đó, chỉ đổi cái ghế: cô đã chuyển từ chỗ bán đồ sang chỗ đi vay, và đây là "
  "lần thứ ba trong tám ngày.",
  "MAYA vuốt phẳng mép tập giấy tờ, xếp lại xấp phiếu lương cho thẳng cạnh; một bóng người mờ đi ngang phía sau "
  "vách kính; cô ngẩng lên nhìn về phía ghế trống bên kia bàn.",
  "Ambient tiếng máy lạnh và tiếng máy in xa trong sảnh ngân hàng, SFX tiếng giấy vuốt phẳng.",
  nhac("NGHỈ", "Nhịp trước là blues guitar; nhịp này phải khác nhạc cụ dẫn và vẫn giữ vai NGHỈ để không cướp sân của chuỗi từ chối.",
       "Minimal piano ballad at 64 BPM; a single upright piano playing three notes over and over with the sustain "
       "pedal down, a female voice entering very late with two short lines sung almost under the breath; no drums, "
       "no bass; the pull is a long silence before the final note; lyrics about sitting in the same chair for the "
       "third time and asking again; dry intimate mix, female vocal, piano, minimal, quiet",
       "Instrumental at 62 BPM; upright piano alone, three notes repeating with heavy sustain, a very low synth pad "
       "fading in underneath after eight seconds, no percussion, thinning out to nothing; "
       "soft office-quiet mix, piano, pad, minimal, still"),
  dur=8)

# ── NGÂN HÀNG ──
S("06", "two-shot trung 50mm, cao 1m40, cách MAYA 2m2, đặt chếch bên bàn tư vấn lấy cả hai người ngồi",
  "MAYA ngồi ở nửa PHẢI khung trên ghế khách, LOAN OFFICER ngồi ở nửa TRÁI khung sau bàn tư vấn, màn hình máy tính "
  "quay nghiêng giữa hai người. Trên bàn là tập giấy tờ và xấp phiếu lương của MAYA.",
  "LOAN OFFICER một tay đặt trên chuột máy tính, tay kia lật một tờ giấy. MAYA hai tay đặt trên đùi.",
  "LOAN OFFICER nhìn vào màn hình. MAYA nhìn thẳng vào mặt LOAN OFFICER.",
  "LOAN OFFICER — người đọc hồ sơ nhiều hơn đọc mặt người: giọng lịch sự, mắt không rời màn hình. "
  "MAYA — đã chuẩn bị sẵn từng tờ và biết mình vẫn sẽ thua: lưng thẳng, giọng nhanh và rõ.",
  "đúng khoảnh khắc ngay TRƯỚC khi LOAN OFFICER xoay hẳn màn hình về phía mình",
  ["MAYA_CUOI", "LOAN OFFICER"], "hai bên bàn tư vấn sảnh ngân hàng",
  {"MAYA": "ngồi ghế khách nửa phải khung", "LOAN OFFICER": "ngồi sau bàn nửa trái khung"},
  "cách nhau một mặt bàn", {"MAYA": "hai tay đặt trên đùi", "LOAN OFFICER": "một tay trên chuột, tay kia lật giấy"},
  bg=NH)
V("06", [10, 11], "two-shot trung 50mm · LOAN OFFICER NÉT trái sau bàn + MAYA NÉT phải trên ghế khách",
  [("MAYA", "MAYA_CUOI"), ("LOAN OFFICER", "LOAN OFFICER")],
  "LOAN OFFICER và MAYA, cả hai rõ mặt hai bên bàn tư vấn. Không có ai khác trong khung.",
  "LOAN OFFICER lật một tờ giấy trong tập hồ sơ, MAYA đẩy xấp phiếu lương về phía anh",
  [("LOAN OFFICER", "polite, procedural", 10), ("MAYA", "quick, prepared", 11)])

S("07", "cận-trung 85mm, cao 1m40, cách MAYA 1m6, máy sau vai PHẢI của LOAN OFFICER; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA ngồi chính diện chiếm phần lớn khung, lưng thẳng trên ghế khách. LOAN OFFICER chỉ còn là vai và gáy ở rìa "
  "TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MAYA là mặt tiền kính sáng và kệ tờ rơi.",
  "MAYA một tay đặt lên tập giấy tờ trên bàn, các ngón ấn nhẹ xuống.",
  "MAYA nhìn thẳng vào mặt LOAN OFFICER qua vai anh.",
  "MAYA — người vừa nghe rằng sáu năm học của mình không được tính là gì cả: quai hàm siết, mắt thẳng, "
  "giọng vẫn giữ được lễ độ.",
  "đúng khoảnh khắc ngay TRƯỚC khi LOAN OFFICER quay màn hình lại về phía mình",
  ["MAYA_CUOI", "LOAN OFFICER"], "hai bên bàn tư vấn sảnh ngân hàng",
  {"MAYA": "ngồi chính diện giữa khung", "LOAN OFFICER": "vai và gáy tiền cảnh trái"},
  "cách nhau một mặt bàn", {"MAYA": "một tay đặt lên tập giấy tờ", "LOAN OFFICER": "một tay trên chuột, ngoài vùng nét"},
  bg=NH)
V("07", [12, 13], "OTS cận-trung 85mm · MAYA NÉT ngồi chính diện · vai và gáy LOAN OFFICER tiền cảnh trái out nét",
  [("MAYA", "MAYA_CUOI"), ("LOAN OFFICER", "LOAN OFFICER")],
  "MAYA rõ mặt ngồi chính diện. LOAN OFFICER chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "LOAN OFFICER đọc từ màn hình, MAYA đặt bàn tay lên tập giấy tờ của mình",
  [("LOAN OFFICER", "neutral, factual", 12), ("MAYA", "firm, contained", 13)])

S("08", "trung 50mm, cao 1m40, cách MAYA 2m2, đặt chếch bên bàn tư vấn lấy cả hai người ngồi",
  "MAYA ngồi ở nửa PHẢI khung, đã nghiêng người tới trước. LOAN OFFICER ngồi ở nửa TRÁI khung sau bàn, người hơi ngả "
  "ra sau ghế. Giữa hai người là màn hình máy tính và tập giấy tờ.",
  "MAYA hai tay đặt lên mép bàn, các ngón khép. LOAN OFFICER hai tay rút về đặt trên đùi.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa dồn một mạng người vào một câu nói và biết nó sẽ không đổi được gì: giọng thấp, mắt đỏ, "
  "không to tiếng. LOAN OFFICER — bắt đầu thấy khó chịu vì cuộc trò chuyện đi khỏi quy trình: mày nhíu, môi mím.",
  "đúng khoảnh khắc ngay TRƯỚC khi LOAN OFFICER đưa mắt về phía cửa tìm bảo vệ",
  ["MAYA_CUOI", "LOAN OFFICER"], "hai bên bàn tư vấn sảnh ngân hàng",
  {"MAYA": "ngồi nghiêng người tới trước nửa phải khung", "LOAN OFFICER": "ngồi ngả ra sau nửa trái khung"},
  "cách nhau một mặt bàn", {"MAYA": "hai tay đặt lên mép bàn", "LOAN OFFICER": "hai tay rút về đặt trên đùi"},
  bg=NH)
V("08", [14, 15], "trung 50mm · MAYA NÉT phải nghiêng người tới trước + LOAN OFFICER NÉT trái ngả ra sau",
  [("MAYA", "MAYA_CUOI"), ("LOAN OFFICER", "LOAN OFFICER")],
  "MAYA và LOAN OFFICER, cả hai rõ mặt hai bên bàn tư vấn. Không có ai khác trong khung.",
  "MAYA nghiêng người tới trước đặt hai tay lên mép bàn, LOAN OFFICER ngả ra sau ghế",
  [("MAYA", "low, urgent", 14), ("LOAN OFFICER", "uncomfortable, formal", 15)])

S("09", "cận-trung 85mm, cao 1m40, cách LOAN OFFICER 1m6, máy sau vai TRÁI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "LOAN OFFICER ngồi chính diện chiếm phần lớn khung sau bàn tư vấn. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, "
  "ngoài vùng nét. Hậu cảnh sau lưng LOAN OFFICER là dãy quầy giao dịch và mảng tường ốp gỗ.",
  "LOAN OFFICER một tay đưa lên ra hiệu về phía cửa sảnh, tay kia gấp tập hồ sơ lại.",
  "LOAN OFFICER nhìn thẳng vào mặt MAYA qua vai cô.",
  "LOAN OFFICER — người đang kết thúc một cuộc hẹn theo đúng quy trình và muốn nó xong nhanh: giọng đều, "
  "mắt không giữ lâu, mày hơi nhíu.",
  "đúng khoảnh khắc ngay TRƯỚC khi tập hồ sơ trên bàn được đẩy trả về phía MAYA",
  ["LOAN OFFICER", "MAYA_CUOI"], "hai bên bàn tư vấn sảnh ngân hàng",
  {"LOAN OFFICER": "ngồi chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mặt bàn", {"LOAN OFFICER": "một tay ra hiệu về phía cửa, tay kia gấp hồ sơ",
                            "MAYA": "hai tay trên mép bàn, ngoài vùng nét"},
  bg=NH)
V("09", [16], "OTS cận-trung 85mm · LOAN OFFICER NÉT ngồi chính diện · vai và gáy MAYA tiền cảnh phải out nét",
  [("LOAN OFFICER", "LOAN OFFICER"), ("MAYA", "MAYA_CUOI")],
  "LOAN OFFICER rõ mặt ngồi chính diện. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "LOAN OFFICER gấp tập hồ sơ lại và ra hiệu về phía cửa sảnh",
  [("LOAN OFFICER", "flat, procedural", 16)], [("MAYA", "silent, not moving")])

S("10", "trung 50mm, cao 1m40, cách MAYA 2m4, đặt chếch bên bàn tư vấn lấy cả hai người",
  "MAYA ngồi ở nửa PHẢI khung, lưng đã tựa hẳn vào lưng ghế, hai tay buông xuống. LOAN OFFICER ngồi ở nửa TRÁI khung, "
  "đã đứng lên được nửa người, một tay chống bàn. Tập hồ sơ nằm giữa bàn.",
  "MAYA hai tay đặt trên đùi, lòng bàn tay ngửa. LOAN OFFICER một tay chống mép bàn, tay kia đẩy tập hồ sơ về phía cô.",
  "MAYA nhìn xuống mặt bàn trước mặt. LOAN OFFICER nhìn MAYA.",
  "MAYA — người đã hết chỗ để đi và đang tự nói cho mình nghe nhiều hơn nói với ai: giọng rất bình, mắt khô, "
  "vai buông. LOAN OFFICER — dừng lại nửa chừng vì câu trả lời không giống thứ anh chờ: mày nhướn.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng dậy khỏi ghế",
  ["MAYA_CUOI", "LOAN OFFICER"], "hai bên bàn tư vấn sảnh ngân hàng",
  {"MAYA": "ngồi tựa lưng ghế nửa phải khung", "LOAN OFFICER": "đứng lên nửa người nửa trái khung"},
  "cách nhau một mặt bàn", {"MAYA": "hai tay đặt ngửa trên đùi",
                            "LOAN OFFICER": "một tay chống bàn, tay kia đẩy hồ sơ về phía MAYA"},
  bg=NH)
V("10", [17], "trung 50mm · MAYA NÉT phải ngồi tựa lưng ghế + LOAN OFFICER NÉT trái đứng lên nửa người",
  [("MAYA", "MAYA_CUOI"), ("LOAN OFFICER", "LOAN OFFICER")],
  "MAYA và LOAN OFFICER, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA tựa hẳn lưng vào ghế, hai tay ngửa trên đùi, nói rất bình tĩnh",
  [("MAYA", "calm, spent", 17)], [("LOAN OFFICER", "silent, half standing")],
  ketclip="Cuối clip, MAYA đứng dậy, ôm tập hồ sơ vào ngực và đi ra phía cửa kính sảnh. "
          "Clip dừng đúng lúc cô quay lưng đi được hai bước.")

# ── NHỊP KHÉP CẢNH ──
S("B3", "toàn cảnh 24mm, cao 1m60, cách MAYA 10m, đặt ở khu tư vấn nhìn về phía mặt tiền kính sảnh",
  "MAYA đi một mình về phía mặt tiền kính lớn ở cuối sảnh, ôm tập hồ sơ trước ngực, váy cưới quét trên sàn đá mài. "
  "Sảnh ngân hàng rộng và trống bao quanh cô; dãy quầy giao dịch bên trái chỉ còn lác đác người.",
  "MAYA hai tay ôm tập hồ sơ ép vào ngực.",
  "MAYA nhìn thẳng ra phía cửa kính sáng cuối sảnh.",
  "MAYA — người vừa nghe câu từ chối thứ ba trong tám ngày và vẫn tự đi ra bằng chân mình: vai cân lại được, "
  "cằm ngang, mặt trống.",
  "đúng khoảnh khắc ngay TRƯỚC khi cánh cửa tự động cuối sảnh mở ra",
  ["MAYA_CUOI"], "lối đi giữa sảnh ngân hàng, hướng ra cửa kính",
  {"MAYA": "đi một mình về phía cửa kính"}, "một mình trong khung",
  {"MAYA": "hai tay ôm tập hồ sơ trước ngực"}, bg=NH)
B("B3", "Khép cảnh. MAYA đi một mình qua sảnh ngân hàng trống về phía cửa kính, ôm tập hồ sơ trước ngực.",
  "toàn cảnh 24mm · MAYA NÉT đi một mình giữa sảnh · không có ai khác trong khung",
  [("MAYA", "MAYA_CUOI")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, đi giữa sảnh ngân hàng trống. Không có người nào khác.",
  "ba lần bị từ chối trong một buổi sáng, và tỷ lệ giữa một người với một cái sảnh đá bóng loáng chính là "
  "nội dung của khung hình này.",
  "MAYA đi đều bước về phía cửa kính, gấu váy quét trên sàn đá; ánh sáng ban ngày ngoài cửa mỗi lúc một trắng hơn "
  "khi cô tới gần; cánh cửa tự động bắt đầu tách ra.",
  "Ambient tiếng máy lạnh trong sảnh và tiếng phố vọng vào khi cửa mở, SFX tiếng gót giày trên sàn đá.",
  nhac("KÌM", "Kết một chuỗi thất bại — nhạc phải ở dưới mức cảm xúc thật vì nhân vật đang không cho phép mình gãy nơi công cộng.",
       "Soul ballad at 64 BPM with a female alto very close to the mic, smoky and worn, almost spoken in places; "
       "Rhodes and upright bass underneath, brushed drums entering only in the last eight seconds; one restrained "
       "string swell at the peak then straight back to voice and Rhodes; lyrics about walking out of a building with "
       "nothing and your head still up, never triumphant; warm analog mix, female vocal, soul, intimate, restrained",
       "Instrumental at 62 BPM; Rhodes piano playing a slow four-chord figure, an upright bass entering on the second "
       "pass, one muted trumpet note held long at the midpoint then gone, no drums, ending on the Rhodes alone; "
       "warm analog mix, Rhodes, upright bass, trumpet, restrained, night-quiet"),
  dur=10)
