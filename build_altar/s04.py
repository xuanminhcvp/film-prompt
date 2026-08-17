# -*- coding: utf-8 -*-
"""SCENE 4 — HÀNG GHẾ CUỐI, NHÀ THỜ TRỐNG (chiều muộn). Bản hợp đồng mười hai tháng."""
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S4", "REF_NHATHO_CHIEU")

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách ADRIAN 12m, đặt giữa lối đi chính nhìn về phía cửa lớn",
  "Lòng nhà thờ đã trống hẳn, hoa ở đầu các hàng ghế đã rũ. ADRIAN ngồi một mình trong xe lăn ở cuối lối đi, "
  "cạnh hàng ghế cuối bên trái, quay mặt về phía bàn thờ. Không còn ai khác trong nhà thờ.",
  "ADRIAN hai tay đặt trên vành tay vịn xe lăn, các ngón thả lỏng.",
  "ADRIAN nhìn dọc lối đi về phía bậc bàn thờ ở xa.",
  "ADRIAN — người đã ngồi yên một chỗ sáu tiếng đồng hồ và không có ý định đi đâu: mặt hoàn toàn bình, "
  "mắt tĩnh, hơi thở chậm.",
  "đúng khoảnh khắc ngay TRƯỚC khi một cánh cửa gỗ lớn sau lưng anh hé mở",
  ["ADRIAN_NHATHO"], "cuối lối đi giữa, cạnh hàng ghế cuối",
  {"ADRIAN": "ngồi một mình trong xe lăn"}, "một mình trong khung",
  {"ADRIAN": "hai tay đặt trên vành tay vịn"})
B("B1", "Mở cảnh. Sáu tiếng sau. Nhà thờ trống trơn, hoa đã rũ. ADRIAN vẫn ngồi ở cuối lối đi, một mình.",
  "toàn cảnh 24mm · ADRIAN NÉT ngồi một mình trong xe lăn ở cuối lối đi · không có ai khác trong khung",
  [("ADRIAN", "ADRIAN_NHATHO")],
  "CHỈ MỘT MÌNH ADRIAN trong khung, rõ mặt, ngồi trong xe lăn ở cuối lối đi. Không có người nào khác trong nhà thờ.",
  "cùng một gian phòng, sáu tiếng sau: hai trăm người đã về hết, chỉ còn lại người mà sáng nay không ai nhìn tới.",
  "ADRIAN ngồi bất động, chỉ có ngực thở; một cánh hoa cúc trắng rụng khỏi bó hoa đầu hàng ghế và rơi xuống thảm đỏ; "
  "vệt nắng chiều trên sàn dịch đi một chút.",
  "Ambient tiếng vọng rỗng của gian nhà thờ đá và tiếng gió ngoài cửa sổ, SFX một tiếng bản lề cửa gỗ rất khẽ.",
  nhac("NGHỈ", "Bản lề của cả phim nằm ở cảnh này; trước khi lời thoại bắt đầu, khán giả cần một khoảng lặng thật sự để nhìn kỹ người đàn ông ngồi đó.",
       "Ambient folk at 54 BPM; one nylon-string guitar playing a single figure with long gaps between phrases, "
       "a female voice humming wordlessly far back in the mix, entering only twice; no drums, no bass; the pull is "
       "an eight-second gap where only room reverb remains; wordless and patient; dry cathedral mix, female vocal, "
       "folk, ambient, patient",
       "Ambient instrumental at 52 BPM; a church organ holding one very low sustained note, a felt piano placing "
       "single notes above it every four seconds with heavy sustain, no percussion, no arc, thinning to silence; "
       "large natural reverb, organ, piano, minimal, patient"),
  dur=8)

# ── HAI NGƯỜI Ở HÀNG GHẾ CUỐI ──
S("01", "trung 50mm, cao 1m40, cách MAYA 2m6, đặt trong lối đi giữa, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung ngay đầu hàng ghế cuối, một tay còn cầm chiếc áo khoác len gấp. ADRIAN ngồi trong "
  "xe lăn ở nửa TRÁI khung, đã quay mặt về phía cô. Hậu cảnh là hai cánh cửa gỗ lớn và các hàng ghế trống.",
  "MAYA một tay ôm chiếc áo khoác len gấp vào ngực, tay kia vịn lưng ghế gỗ. ADRIAN hai tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người tưởng nhà thờ đã trống và vừa thấy có người: hơi lùi nửa bước, mày nhướn, giọng lễ độ. "
  "ADRIAN — nói ra một con số như thể đã đếm từng phút: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước hẳn vào lối đi giữa hai hàng ghế",
  ["MAYA_CUOI", "ADRIAN_NHATHO"], "đầu hàng ghế cuối, cạnh lối đi giữa",
  {"MAYA": "đứng đầu hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau hai mét", {"MAYA": "một tay ôm áo khoác len, tay kia vịn lưng ghế",
                        "ADRIAN": "hai tay trên vành tay vịn"})
V("01", [0, 1], "trung 50mm hạ thấp · MAYA NÉT phải đứng đầu hàng ghế + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt. Nhà thờ trống, không có ai khác trong khung.",
  "MAYA dừng lại khi thấy có người, ADRIAN quay mặt về phía cô",
  [("MAYA", "polite, startled", 0), ("ADRIAN", "level, quiet", 1)])

S("02", "cận-trung 85mm, cao 1m40, cách MAYA 1m8, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, chiếc áo khoác len ôm trước ngực. ADRIAN chỉ còn là vai và gáy "
  "ở rìa TRÁI tiền cảnh, thấp hơn hẳn trong khung vì đang ngồi, ngoài vùng nét. Hậu cảnh sau lưng MAYA là các "
  "hàng ghế gỗ trống và lối đi thảm đỏ.",
  "MAYA hai tay ôm chiếc áo khoác len trước ngực, các ngón bấu vào vải.",
  "MAYA nhìn thẳng xuống mặt ADRIAN.",
  "MAYA — người không hiểu nổi vì sao có người ngồi lại đây suốt sáu tiếng: mày chau, đầu hơi nghiêng, "
  "giọng thật thà.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA ngồi xuống mép hàng ghế cuối",
  ["MAYA_CUOI", "ADRIAN_NHATHO"], "đầu hàng ghế cuối, cạnh lối đi giữa",
  {"MAYA": "đứng chính diện giữa khung", "ADRIAN": "vai và gáy tiền cảnh trái, ngồi thấp"},
  "cách nhau hai mét", {"MAYA": "hai tay ôm áo khoác len trước ngực",
                        "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
V("02", [2, 3], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA rõ mặt chính diện. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, ngồi thấp, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA ôm chặt chiếc áo khoác vào ngực và hỏi lại",
  [("MAYA", "puzzled, honest", 2), ("ADRIAN", "even, unhurried", 3)],
  ketclip="Cuối clip, MAYA ngồi xuống mép hàng ghế cuối, đặt chiếc áo khoác len lên đùi. "
          "Clip dừng đúng lúc cô vừa ngồi xuống.")

S("03", "two-shot trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp ngang tầm người ngồi, đặt trong lối đi",
  "MAYA ngồi ở nửa PHẢI khung trên mép hàng ghế cuối, chiếc áo khoác len đặt trên đùi. ADRIAN ngồi trong xe lăn "
  "ở nửa TRÁI khung, đầu gối gần chạm mép ghế gỗ. Hai người ngang tầm mắt nhau lần đầu tiên.",
  "MAYA hai tay đặt lên chiếc áo khoác trên đùi. ADRIAN một tay đặt trên vành tay vịn, tay kia buông xuống bên hông xe.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — vừa hiểu ra người này biết tên mình và chưa biết nên thấy thế nào: mày nhướn, mắt dò xét. "
  "ADRIAN — trả lời một câu đùa rất khô mà không cười: khoé môi phẳng, mắt hơi dịu.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay mặt đi chỗ khác",
  ["MAYA_CUOI", "ADRIAN_NHATHO"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "hai tay đặt trên áo khoác trên đùi",
                        "ADRIAN": "một tay trên vành tay vịn, tay kia buông bên hông xe"})
V("03", [4, 5], "two-shot trung 50mm hạ thấp · MAYA NÉT phải ngồi mép ghế + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt, ngồi ngang tầm mắt nhau. Không có ai khác trong khung.",
  "MAYA quay sang hỏi, ADRIAN trả lời mà không đổi nét mặt",
  [("MAYA", "wary, direct", 4), ("ADRIAN", "dry, quiet", 5)])

S("04", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m6, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng ADRIAN là hai cánh cửa gỗ lớn cuối nhà thờ.",
  "ADRIAN một tay với xuống túi bên hông xe lăn và rút ra một TẬP GIẤY A4 ba tờ, tay kia vẫn trên vành tay vịn.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người đã chuẩn bị sẵn tập giấy này từ lâu và giờ mới lấy ra: giọng đều, mắt không dời, "
  "không hề thuyết phục.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN chìa tập giấy ra",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mét", {"ADRIAN": "một tay rút tập giấy từ túi bên hông xe",
                        "MAYA": "hai tay trên đùi, ngoài vùng nét"})
V("04", [6, 7], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA nói trước, ADRIAN với xuống túi bên hông xe lăn rút ra một tập giấy",
  [("MAYA", "guarded, tired", 6), ("ADRIAN", "even, direct", 7)],
  ketclip="Cuối clip, ADRIAN chìa tập giấy sang, MAYA cầm lấy và đặt lên đùi. "
          "Clip dừng đúng lúc tập giấy nằm gọn trong tay cô.")

S("05", "two-shot trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp ngang tầm người ngồi",
  "MAYA ngồi ở nửa PHẢI khung, TẬP GIẤY A4 BA TỜ đã nằm trên đùi cô, tờ trên cùng có một dòng tiêu đề in hoa "
  "và hai dòng kẻ chân chữ ký còn trống. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung.",
  "MAYA hai tay giữ hai mép tập giấy trên đùi. ADRIAN hai tay đặt lại trên vành tay vịn.",
  "MAYA nhìn xuống tờ giấy trên đùi. ADRIAN nhìn MAYA.",
  "MAYA — người vừa đọc ba dòng đầu và ngẩng lên: mắt mở, môi hé, chưa tin. "
  "ADRIAN — đọc lại các điều khoản như đọc một danh sách: giọng đều, không nhấn chữ nào.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA lật sang tờ thứ hai",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung, tập giấy trên đùi", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "hai tay giữ hai mép tập giấy", "ADRIAN": "hai tay trên vành tay vịn"})
VX("05", "two-shot trung 50mm hạ thấp · MAYA NÉT phải cầm tập giấy + ADRIAN NÉT trái ngồi xe lăn",
   [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
   "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
   "MAYA đọc dòng đầu rồi ngẩng lên, ADRIAN bắt đầu đọc lại các điều khoản",
   [("MAYA", "disbelieving, flat", "This is a contract."),
    ("ADRIAN", "even, listing",
     "Twelve months. You become my legal wife. Separate room, separate bed, no touching.")])

S("05b", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m6, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng ADRIAN là hai cánh cửa gỗ lớn cuối nhà thờ.",
  "ADRIAN hai tay đặt trên hai vành tay vịn của xe lăn, các ngón thả lỏng.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người đọc ba điều cấm như đọc ba dòng trong hợp đồng thuê nhà: giọng đều, không nhấn chữ nào, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi cô được gì đổi lại",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mét", {"ADRIAN": "một tay đếm bằng ngón trỏ, tay kia trên vành tay vịn",
                        "MAYA": "hai tay giữ tập giấy, ngoài vùng nét"})
VX("05b", "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
   [("ADRIAN", "ADRIAN_NHATHO"), ("MAYA", "MAYA_CUOI")],
   "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
   "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
   "ADRIAN đếm ba điều cấm trên đầu ngón tay",
   [("ADRIAN", "even, listing",
     "You do not ask about my family. You do not ask about my accident. You do not ask where my money comes from.")],
   [("MAYA", "silent, reading")])

S("06", "cận-trung 85mm, cao 1m20, cách MAYA 1m6, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA ngồi chính diện chiếm phần lớn khung, tập giấy A4 ba tờ trên đùi. ADRIAN chỉ còn là vai và gáy ở rìa TRÁI "
  "tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MAYA là các hàng ghế gỗ trống.",
  "MAYA một tay đè lên mép tập giấy, tay kia rời ra và siết lại thành nắm trên đùi.",
  "MAYA nhìn thẳng vào mặt ADRIAN.",
  "MAYA — người vừa nghe đúng con số mình đang mắc nợ được nói ra bởi một người lạ: mắt mở to, "
  "hơi thở dừng một nhịp, giọng khô.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi lại vì sao là mình",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi chính diện giữa khung, tập giấy trên đùi", "ADRIAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một mét", {"MAYA": "một tay đè mép tập giấy, tay kia siết thành nắm",
                        "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
V("06", [10, 11], "OTS cận-trung 85mm · MAYA NÉT ngồi chính diện · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA rõ mặt ngồi chính diện. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA rời một tay khỏi tập giấy và siết lại thành nắm trên đùi",
  [("MAYA", "dry, careful", 10), ("ADRIAN", "flat, precise", 11)])

S("07", "two-shot cận-trung 85mm, cao 1m20, cách MAYA 1m9, máy hạ thấp ngang tầm người ngồi",
  "MAYA ngồi ở nửa PHẢI khung, ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. Tập giấy A4 vẫn trên đùi MAYA. "
  "Hai người rất gần nhau trong khung, khoảng cách giữa họ hẹp lại so với các khung trước.",
  "MAYA một tay chỉ vào một dòng trên tờ giấy. ADRIAN một tay hơi nhấc lên khỏi vành tay vịn rồi đặt xuống.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đọc to con số ra để nghe xem nó có thật không: giọng chậm, tách từng chữ. "
  "ADRIAN — sửa lại con số cho chính xác tới hàng đơn vị: mặt bình, không đùa.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt tập giấy xuống đùi và hỏi câu tiếp theo",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "một tay chỉ vào một dòng trên giấy",
                        "ADRIAN": "một tay nhấc lên rồi đặt xuống vành tay vịn"})
V("07", [12, 13], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải + ADRIAN NÉT trái, cả hai rõ mặt",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt, ngồi ngang tầm mắt nhau. Không có ai khác trong khung.",
  "MAYA chỉ vào một dòng trên tờ giấy và đọc to con số",
  [("MAYA", "slow, testing", 12), ("ADRIAN", "precise, plain", 13)])

S("08", "cận 85mm, cao 1m20, cách MAYA 1m3, đặt chếch bên, lấy MAYA nét và một mảng vai ADRIAN ở rìa trái",
  "MAYA ngồi chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai và tay vịn xe lăn của ADRIAN, "
  "out nét. Hậu cảnh là các hàng ghế gỗ trống chìm trong bóng chiều.",
  "MAYA hai tay đặt phẳng lên tập giấy trên đùi.",
  "MAYA nhìn thẳng vào mặt ADRIAN.",
  "MAYA — người hỏi câu quan trọng nhất bằng hai từ và đã chuẩn bị nghe một câu trả lời tệ: mắt thẳng, "
  "quai hàm giữ, hơi thở nông.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu trả lời",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi chính diện giữa khung", "ADRIAN": "một mảng vai và tay vịn xe lăn ở rìa trái"},
  "cách nhau một mét", {"MAYA": "hai tay đặt phẳng lên tập giấy",
                        "ADRIAN": "một tay trên vành tay vịn, ngoài vùng nét"})
V("08", [14], "cận 85mm · MAYA NÉT ngồi chính diện · một mảng vai và tay vịn xe lăn ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI và tay vịn xe lăn ở rìa trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đặt hai bàn tay phẳng lên tập giấy và hỏi",
  [("MAYA", "level, braced", 14)], [("ADRIAN", "silent, about to answer")])

S("09", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m5, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng ADRIAN là lối đi thảm đỏ chạy hút về phía bậc bàn thờ.",
  "ADRIAN một tay hơi mở ra trên vành tay vịn theo nhịp kể, tay kia bất động.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người đang kể lại đúng thứ mình nhìn thấy sáng nay, không thêm một chữ cảm thán nào: giọng đều, "
  "chậm, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN kể tới đoạn cô quỳ xuống nhặt tiền",
  ["ADRIAN_NHATHO", "MAYA_CUOI"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mét", {"ADRIAN": "một tay mở ra trên vành tay vịn",
                        "MAYA": "hai tay trên tập giấy, ngoài vùng nét"})
VX("09", "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
   [("ADRIAN", "ADRIAN_NHATHO"), ("MAYA", "MAYA_CUOI")],
   "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
   "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
   "ADRIAN kể lại chuyện sáng nay, bàn tay mở ra trên vành tay vịn theo nhịp",
   [("ADRIAN", "even, remembering",
     "Ten minutes before I spoke to you, a rich woman threw cash in your face in front of two hundred people. "
     "You had every reason to scream. To cry. To pull her hair.")],
   [("MAYA", "silent, listening")])

S("10", "cận 85mm, cao 1m20, cách ADRIAN 1m2, đặt chính diện, hậu cảnh là cánh cửa gỗ lớn xoá phông",
  "ADRIAN ngồi chiếm phần lớn khung từ ngực trở lên. Ở rìa PHẢI khung thấy một mảng vai của MAYA đang ngồi, out nét. "
  "Hậu cảnh là cánh cửa gỗ lớn cuối nhà thờ, xoá phông mềm.",
  "ADRIAN một tay làm động tác vuốt cho mép một chồng giấy tưởng tượng thẳng lại, rất chậm, rồi hạ xuống.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người đang mô tả đúng cái khoảnh khắc đã làm anh đổi ý về cả loài người: giọng nhỏ hơn hẳn các câu trước, "
  "mắt hơi nheo lại, khoé môi động một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA lắc đầu",
  ["ADRIAN_NHATHO", "MAYA_CUOI"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"ADRIAN": "ngồi chính diện giữa khung", "MAYA": "một mảng vai ở rìa phải khung"},
  "cách nhau một mét", {"ADRIAN": "một tay làm động tác vuốt thẳng mép chồng giấy",
                        "MAYA": "hai tay trên tập giấy, ngoài vùng nét"})
VX("10", "cận 85mm · ADRIAN NÉT chính diện · một mảng vai MAYA rìa phải out nét",
   [("ADRIAN", "ADRIAN_NHATHO"), ("MAYA", "MAYA_CUOI")],
   "ADRIAN rõ mặt chính diện. MAYA chỉ thấy MỘT MẢNG VAI ở rìa phải, out nét — "
   "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
   "ADRIAN làm lại rất chậm động tác vuốt thẳng mép một chồng giấy trong không khí",
   [("ADRIAN", "quiet, careful",
     "Instead you knelt down and counted it. You stacked the bills straight and you gave them back.")],
   [("MAYA", "silent, shaking her head")])

S("11", "two-shot trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp ngang tầm người ngồi",
  "MAYA ngồi ở nửa PHẢI khung, tập giấy A4 vẫn trên đùi, người hơi quay đi. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. "
  "Hậu cảnh là hàng ghế gỗ trống và một phần cánh cửa lớn.",
  "MAYA một tay đưa lên gạt một lọn tóc ra sau tai rồi đặt lại lên tập giấy. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống tập giấy rồi ngước lên nhìn ADRIAN. ADRIAN nhìn MAYA.",
  "MAYA — người thấy lý do đó vừa quá mỏng vừa quá thật: mày chau, khoé môi động. "
  "ADRIAN — nói ra hai chữ chính xác cho việc mình đang làm và không né chúng: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhìn xuống dòng kẻ chân chữ ký",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "một tay gạt tóc ra sau tai rồi đặt lại lên tập giấy",
                        "ADRIAN": "hai tay trên vành tay vịn"})
V("11", [16, 17], "two-shot trung 50mm hạ thấp · MAYA NÉT phải ngồi mép ghế + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA gạt một lọn tóc ra sau tai rồi ngước lên, ADRIAN trả lời không né",
  [("MAYA", "doubtful, quiet", 16), ("ADRIAN", "plain, unapologetic", 17)])

S("12", "cận-trung 85mm, cao 1m20, cách MAYA 1m6, đặt chếch bên, lấy MAYA nét và ADRIAN trong khung",
  "MAYA ngồi ở nửa PHẢI khung, hai vai chùng xuống. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, thấy rõ mặt. "
  "Tập giấy A4 nằm trên đùi MAYA.",
  "MAYA một tay đặt lên mép hàng ghế gỗ bên cạnh mình, các ngón bám vào cạnh gỗ.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đang nói ra trước cái nhục mình sẽ phải mang, để xem đối phương có chối không: giọng thấp, "
  "mắt thẳng. ADRIAN — không chối một chữ nào: gật một cái rất nhỏ, mặt không đổi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi câu tiếp theo",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "một tay bám vào cạnh gỗ hàng ghế", "ADRIAN": "hai tay trên vành tay vịn"})
V("12", [18, 19], "cận-trung 85mm · MAYA NÉT phải ngồi mép ghế + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA bám tay vào cạnh gỗ hàng ghế và nói ra trước điều tệ nhất, ADRIAN gật một cái rất nhỏ",
  [("MAYA", "low, testing", 18), ("ADRIAN", "plain, unflinching", 19)])

S("13", "cận-trung 85mm, cao 1m20, cách ADRIAN 1m5, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh là lối đi thảm đỏ và các hàng ghế gỗ trống.",
  "ADRIAN một tay rút từ túi ngực ra một CÂY BÚT MÁY màu đen thân trơn và giữ nó ngang ngực, chưa mở nắp.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người nói về sáu tháng bị cười nhạo bằng giọng của một người báo cáo thời tiết: mặt bình, "
  "mắt tĩnh, không một chút tự thương.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN chìa cây bút ra",
  ["ADRIAN_NHATHO", "MAYA_CUOI"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mét", {"ADRIAN": "một tay giữ cây bút máy ngang ngực, chưa mở nắp",
                        "MAYA": "hai tay trên tập giấy, ngoài vùng nét"})
V("13", [20, 21], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn cầm bút · vai và gáy MAYA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_NHATHO"), ("MAYA", "MAYA_CUOI")],
  "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA hỏi, ADRIAN rút một cây bút máy từ túi ngực và giữ nó ngang ngực",
  [("MAYA", "quiet, probing", 20), ("ADRIAN", "even, factual", 21)])

S("14", "two-shot trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp ngang tầm người ngồi",
  "MAYA ngồi ở nửa PHẢI khung, tập giấy trên đùi, một tay đã cầm cây bút máy. ADRIAN ngồi trong xe lăn ở nửa TRÁI "
  "khung. Trên lưng hàng ghế trước mặt hai người có một CUỐN SÁCH THÁNH CA bìa nâu sờn nằm sẵn.",
  "MAYA một tay cầm cây bút máy, tay kia đưa ra hai bên tìm chỗ tựa. ADRIAN một tay chỉ về phía cuốn sách thánh ca "
  "trên lưng ghế.",
  "MAYA nhìn quanh tìm mặt phẳng. ADRIAN nhìn cuốn sách thánh ca rồi nhìn MAYA.",
  "MAYA — người sắp ký một thứ lớn hơn mọi thứ mình từng ký và bận tâm về chuyện không có bàn: mày chau, giọng thật. "
  "ADRIAN — giải quyết vấn đề bằng đúng một câu: khoé môi động rất nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA với tay lấy cuốn sách thánh ca",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "một tay cầm bút máy, tay kia tìm chỗ tựa",
                        "ADRIAN": "một tay chỉ về cuốn sách thánh ca trên lưng ghế"})
V("14", [22, 23], "two-shot trung 50mm hạ thấp · MAYA NÉT phải cầm bút + ADRIAN NÉT trái chỉ về cuốn sách",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA cầm cây bút và đưa tay tìm chỗ tựa, ADRIAN chỉ về cuốn sách thánh ca trên lưng ghế",
  [("MAYA", "flustered, practical", 22), ("ADRIAN", "dry, helpful", 23)],
  ketclip="Cuối clip, MAYA với lấy cuốn sách thánh ca, đặt úp lên đùi làm bàn, kê tập giấy lên trên và bắt đầu ký. "
          "Clip dừng đúng lúc ngòi bút chạm xuống giấy.")

S("15", "cận 85mm, cao 1m10, cách MAYA 1m2, máy hạ thấp chếch bên, lấy MAYA nét và một mảng vai ADRIAN rìa trái",
  "MAYA ngồi chiếm phần lớn khung, tập giấy kê trên CUỐN SÁCH THÁNH CA úp trên đùi, chữ ký vừa xong trên dòng kẻ. "
  "Ở rìa TRÁI khung thấy một mảng vai và tay vịn xe lăn của ADRIAN, out nét.",
  "MAYA một tay giữ mép tập giấy, tay kia vừa nhấc cây bút lên khỏi mặt giấy.",
  "MAYA nhìn xuống chữ ký của chính mình rồi ngước lên nhìn ADRIAN.",
  "MAYA — người vừa ký xong và nghe rõ sự phi lý của chỗ mình vừa ký: mắt hơi mở to, khoé môi kéo lệch một chút "
  "gần thành cười, không vui.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN nói tên mình",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi chính diện giữa khung, vừa ký xong", "ADRIAN": "một mảng vai và tay vịn xe lăn ở rìa trái"},
  "cách nhau một mét", {"MAYA": "một tay giữ mép tập giấy, tay kia vừa nhấc bút lên",
                        "ADRIAN": "một tay trên vành tay vịn, ngoài vùng nét"})
V("15", [24, 25], "cận 85mm hạ thấp · MAYA NÉT vừa ký xong · một mảng vai và tay vịn xe lăn ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG VAI và tay vịn xe lăn ở rìa trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA nhấc cây bút lên khỏi mặt giấy và nhìn xuống chữ ký của chính mình",
  [("MAYA", "wry, hollow", 24), ("ADRIAN", "quiet, plain", 25)])

S("16", "two-shot cận-trung 85mm, cao 1m20, cách MAYA 1m8, máy hạ thấp ngang tầm người ngồi",
  "MAYA ngồi ở nửa PHẢI khung, đã đặt tập giấy và cuốn sách thánh ca xuống mặt ghế bên cạnh. ADRIAN ngồi trong "
  "xe lăn ở nửa TRÁI khung. Hai người ngang tầm mắt, gần nhau nhất trong cả cảnh.",
  "MAYA một tay còn đặt trên tập giấy bên cạnh, tay kia buông xuống mép ghế. ADRIAN hai tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa giao cả một năm đời mình cho một người lạ và đang nói ra điều kiện duy nhất của mình: "
  "giọng thấp, mắt không chớp. ADRIAN — nhận lời cảnh cáo đó một cách nghiêm túc: gật một cái, mắt dịu.",
  "đúng khoảnh khắc ngay TRƯỚC khi vệt nắng chiều cuối cùng trượt khỏi lưng hàng ghế",
  ["MAYA_CUOI", "ADRIAN_NHATHO", "PROP_HOPDONG"], "mép hàng ghế cuối và lối đi cạnh đó",
  {"MAYA": "ngồi mép hàng ghế nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một mét", {"MAYA": "một tay trên tập giấy bên cạnh, tay kia buông xuống mép ghế",
                        "ADRIAN": "hai tay trên vành tay vịn"})
V("16", [26, 27], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải + ADRIAN NÉT trái, cả hai rõ mặt",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN, cả hai rõ mặt, ngang tầm mắt nhau. Không có ai khác trong khung.",
  "MAYA đặt tập giấy xuống mặt ghế bên cạnh rồi quay hẳn sang nhìn ADRIAN",
  [("MAYA", "low, warning", 26), ("ADRIAN", "quiet, sincere", 27)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 14m, đặt giữa lối đi chính nhìn về phía cửa lớn",
  "Nhà thờ trống, ánh chiều đã rút gần hết. MAYA ngồi trên mép hàng ghế cuối bên trái lối đi, ADRIAN ngồi trong "
  "xe lăn ngay cạnh đầu hàng ghế đó. Hai người nhỏ trong một gian phòng rất lớn, không ai khác.",
  "MAYA hai tay đặt trên đùi. ADRIAN hai tay đặt trên vành tay vịn xe lăn.",
  "Cả hai cùng nhìn dọc lối đi về phía bậc bàn thờ ở xa.",
  "MAYA — người vừa ký xong và chưa đứng dậy được ngay: vai buông, mặt trống, mắt khô. "
  "ADRIAN — ngồi yên cạnh cô, không nói gì thêm: mặt bình, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng dậy khỏi hàng ghế",
  ["MAYA_CUOI", "ADRIAN_NHATHO"], "hàng ghế cuối và lối đi giữa",
  {"MAYA": "ngồi mép hàng ghế cuối", "ADRIAN": "ngồi xe lăn cạnh đầu hàng ghế"},
  "cách nhau một mét", {"MAYA": "hai tay đặt trên đùi", "ADRIAN": "hai tay trên vành tay vịn"})
B("B2", "Khép cảnh. Giấy tờ đã ký xong. Hai người ngồi cạnh nhau ở hàng ghế cuối một nhà thờ trống, cùng nhìn về bàn thờ.",
  "toàn cảnh 24mm · MAYA NÉT ngồi mép hàng ghế cuối + ADRIAN NÉT ngồi xe lăn cạnh đó · không có ai khác",
  [("MAYA", "MAYA_CUOI"), ("ADRIAN", "ADRIAN_NHATHO")],
  "MAYA và ADRIAN rõ mặt, ngồi cạnh nhau ở cuối nhà thờ. Không có người nào khác trong khung.",
  "hai người vừa ký xong một tờ giấy mua bán một năm đời người, và cả hai đều biết mình vừa làm gì; "
  "không ai trong hai người thấy nhẹ đi.",
  "cả hai ngồi yên nhìn dọc lối đi; vệt nắng chiều cuối cùng trượt khỏi lưng ghế và tắt; MAYA thở ra một hơi dài; "
  "ADRIAN không nhúc nhích.",
  "Ambient tiếng vọng rỗng của gian nhà thờ đá lúc chiều muộn và tiếng gió rất xa ngoài cửa sổ.",
  nhac("NÂNG", "Đây là mốc sang chương: từ đây cô là vợ anh trên giấy tờ. Nhạc phải tạo đà cho chương mới nhưng vẫn giữ nguyên sự bất an của cả hai.",
       "Cinematic folk at 80 BPM; acoustic guitar picking a rising four-note figure, a female alto entering after "
       "eight seconds singing low and close, strings swelling once at the midpoint then pulling back to guitar alone; "
       "no drums until a single soft kick in the final bars; lyrics about signing your name to something you do not "
       "understand yet because someone you love is still breathing; warm analog mix, female vocal, folk, cinematic, "
       "hopeful but uneasy",
       "Cinematic instrumental at 78 BPM; acoustic guitar arpeggio, a cello line rising underneath, one string swell "
       "at the midpoint dropping back to guitar and cello, a single soft kick entering only in the last four bars, "
       "ending open; warm analog mix, guitar, cello, strings, cinematic, unresolved"),
  dur=10)
