# -*- coding: utf-8 -*-
"""SCENE 2 — BÃI ĐỖ XE NHÀ THỜ (sáng). Cuộc gọi viện phí và cú quỳ xin tiền."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S2", "REF_BAIDOXE_SANG", qc=qc.S2)
DT = "BILLING CLERK (off-screen, qua điện thoại)"

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 6m, đặt giữa bãi nhìn về cửa hông nhà thờ",
  "MAYA vừa bước xuống ba bậc đá của cửa hông nhà thờ và đang đứng lại ở mép bãi đỗ xe, váy cưới quét trên mặt nhựa. "
  "Sau lưng cô là tường đá và cánh cửa hông còn mở hé. Bãi xe phía trước có mấy hàng xe đỗ.",
  "MAYA một tay giữ vạt váy khỏi chạm đất, tay kia cầm một chiếc điện thoại smartphone vỏ đen đã trầy, "
  "màn hình ÚP XUỐNG lòng bàn tay.",
  "MAYA nhìn thẳng ra phía lối ra bãi xe.",
  "MAYA — người vừa bước ra khỏi đám cưới của chính mình và chưa biết đi đâu: mặt trống, mắt khô, vai vẫn cân.",
  "đúng khoảnh khắc ngay TRƯỚC khi chiếc điện thoại trong tay cô rung lên",
  ["MAYA_CUOI"], "mép bãi đỗ xe, chân ba bậc đá cửa hông nhà thờ",
  {"MAYA": "đứng một mình ở mép bãi"}, "một mình trong khung",
  {"MAYA": "một tay giữ vạt váy, tay kia cầm điện thoại úp màn hình"})
B("B1", "Mở cảnh. MAYA bước ra bãi đỗ xe nắng chang, vẫn nguyên váy cưới, điện thoại trong tay.",
  "trung-rộng 35mm · MAYA NÉT đứng một mình ở mép bãi đỗ xe · không có ai khác",
  [("MAYA", "MAYA_CUOI")],
  "MAYA rõ mặt, đứng một mình ở mép bãi đỗ xe. Không có người nào khác trong bãi.",
  "một người vừa bước từ trong nhà thờ ra ngoài nắng, và ngoài này thì mọi thứ vẫn y như cũ: xe vẫn đỗ, nắng vẫn gắt, "
  "không ai biết chuyện gì vừa xảy ra.",
  "MAYA đứng lại một nhịp, hít vào một hơi dài rồi thở ra; gió thổi một dải ruy băng trắng lăn qua mặt nhựa; "
  "chiếc điện thoại trong tay cô sáng lên và rung.",
  "SFX tiếng gót giày trên mặt nhựa và tiếng điện thoại rung, Ambient tiếng xe chạy rất xa và tiếng chim.",
  nhac("NGHỈ", "Ngay sau cú sụp đổ trong nhà thờ, khán giả cần một khoảng thở trước khi cú thứ hai giáng xuống.",
       "Sparse folk at 60 BPM; one nylon-string guitar picking a slow repeating figure, a female voice entering late, "
       "low and almost spoken, only a handful of words; no drums, no bass; the pull is a full bar of silence before "
       "the last phrase; lyrics about walking out into ordinary daylight after the worst hour of your life; "
       "dry intimate mix, female vocal, folk, sparse, quiet",
       "Ambient instrumental at 58 BPM; a single warm pad breathing slowly under one felt-piano note repeating every "
       "four seconds, a faint traffic-like hum underneath, no percussion, no arc, simply thinning out; "
       "extremely soft daylight mix, piano, pad, minimal, still"),
  dur=8)

# ── CUỘC GỌI ──
S("01", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, đặt chếch bên phải, hậu cảnh là hàng xe đỗ",
  "MAYA đứng một mình giữa lối đi của bãi xe, đã đưa chiếc điện thoại lên áp vào tai PHẢI. Hậu cảnh là hàng xe đỗ "
  "và hàng cây phong ngoài rào.",
  "MAYA tay phải áp điện thoại vào tai, tay trái buông xuống giữ hờ vạt váy.",
  "MAYA nhìn xuống mặt nhựa cách chân mình chừng một mét.",
  "MAYA — người vừa nhấc máy và nhận ra giọng bên kia là ai: mày hơi nhíu, quai hàm siết nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA cất tiếng chào",
  ["MAYA_CUOI"], "giữa lối đi bãi xe",
  {"MAYA": "đứng một mình, điện thoại áp tai phải"}, "một mình trong khung",
  {"MAYA": "tay phải cầm điện thoại áp tai, tay trái giữ vạt váy"})
V("01", [0], "cận-trung 85mm · MAYA NÉT một mình, điện thoại áp tai phải · BILLING CLERK ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_CUOI"), (DT, "BILLING CLERK")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, điện thoại áp tai phải. Người gọi KHÔNG xuất hiện, chỉ nghe giọng qua điện thoại.",
  "MAYA nhấc máy lên tai và trả lời",
  [("MAYA", "tired, polite", 0)])

S("02", "cận 85mm, cao 1m55, cách MAYA 1m2, đặt chính diện, hậu cảnh là tường đá nhà thờ xoá phông",
  "MAYA đứng một mình, chiếm phần lớn khung từ ngực trở lên, điện thoại áp tai PHẢI. Hậu cảnh là mảng tường đá "
  "màu mật ong xoá phông.",
  "MAYA tay phải giữ điện thoại, các ngón siết chặt dần trên vỏ máy.",
  "MAYA nhìn vào một điểm cố định ngoài khung, không di chuyển mắt.",
  "MAYA — người vừa nghe thấy tên mẹ mình và số giường: mắt mở, hơi thở dừng lại một nhịp, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi lại",
  ["MAYA_CUOI"], "giữa lối đi bãi xe",
  {"MAYA": "đứng một mình, điện thoại áp tai phải"}, "một mình trong khung",
  {"MAYA": "tay phải siết chặt điện thoại"})
V("02", [1, 2], "cận 85mm · MAYA NÉT một mình, điện thoại áp tai phải · BILLING CLERK ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_CUOI"), (DT, "BILLING CLERK")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt. Người gọi KHÔNG xuất hiện, chỉ nghe giọng qua điện thoại.",
  "MAYA đứng yên nghe, các ngón tay siết chặt dần trên vỏ điện thoại",
  [(DT, "apologetic, careful", 1), ("MAYA", "quiet, alert", 2)])

S("03", "cận 85mm, cao 1m55, cách MAYA 1m2, đặt chếch bên trái, hậu cảnh là hàng xe đỗ xoá phông",
  "MAYA đứng một mình chiếm phần lớn khung từ ngực trở lên, điện thoại vẫn áp tai PHẢI. Hậu cảnh là hàng xe đỗ "
  "xoá phông mềm.",
  "MAYA tay trái buông thõng, các ngón duỗi ra rồi khép lại một lần.",
  "MAYA nhìn xuống thấp, mắt không tập trung vào vật gì.",
  "MAYA — người đang nghe một cái hạn chót cho mạng sống của mẹ mình đọc ra thành ngày và giờ: mắt đứng tròng, "
  "cằm run rất nhẹ một nhịp rồi giữ lại được, KHÔNG khóc.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhẩm ra số giờ còn lại",
  ["MAYA_CUOI"], "giữa lối đi bãi xe",
  {"MAYA": "đứng một mình, điện thoại áp tai phải"}, "một mình trong khung",
  {"MAYA": "tay trái duỗi rồi khép lại một lần"})
V("03", [3], "cận 85mm · MAYA NÉT một mình, điện thoại áp tai phải · BILLING CLERK ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_CUOI"), (DT, "BILLING CLERK")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt. Người gọi KHÔNG xuất hiện, chỉ nghe giọng qua điện thoại.",
  "MAYA đứng bất động nghe hết câu, chỉ có bàn tay trái duỗi ra rồi khép lại",
  [(DT, "regretful, formal", 3)], [("MAYA", "silent, absolutely still")])

S("04", "cận-trung 85mm, cao 1m55, cách MAYA 1m5, đặt chính diện, hậu cảnh là bãi xe xoá phông",
  "MAYA đứng một mình, điện thoại áp tai PHẢI, người hơi nghiêng về một bên. Hậu cảnh là bãi xe xoá phông.",
  "MAYA tay trái đưa lên ôm lấy khuỷu tay phải, giữ cho cánh tay cầm điện thoại khỏi run.",
  "MAYA nhìn thẳng ra phía trước, qua đầu người xem.",
  "MAYA — người vừa đổi một cái hạn chót thành một con số giờ vì đếm được thì dễ chịu hơn: giọng rất khẽ, mắt đỏ "
  "nhưng chưa rơi.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hít vào để nói tiếp",
  ["MAYA_CUOI"], "giữa lối đi bãi xe",
  {"MAYA": "đứng một mình, điện thoại áp tai phải"}, "một mình trong khung",
  {"MAYA": "tay trái ôm khuỷu tay phải"})
V("04", [4, 5], "cận-trung 85mm · MAYA NÉT một mình, điện thoại áp tai phải · BILLING CLERK ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_CUOI"), (DT, "BILLING CLERK")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt. Người gọi KHÔNG xuất hiện, chỉ nghe giọng qua điện thoại.",
  "MAYA ôm lấy khuỷu tay mình cho khỏi run rồi nói ra con số",
  [("MAYA", "very quiet, counting", 4), (DT, "weary, human", 5)])

S("05", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, đặt chếch bên phải, hậu cảnh là tường đá nhà thờ",
  "MAYA đứng một mình, đã quay người lại nhìn về phía toà nhà thờ phía sau, điện thoại vẫn áp tai PHẢI. "
  "Hậu cảnh là tường đá màu mật ong và một cửa sổ kính màu hẹp trên cao.",
  "MAYA tay trái giơ lên ngang ngực, lòng bàn tay ngửa, như đang trình bày với một người ngồi trước mặt.",
  "MAYA nhìn lên mảng tường đá phía trên đầu.",
  "MAYA — người đang kể ra bốn trăm ca đêm của mình như kể một tờ hoá đơn: giọng nhanh hơn, hơi gấp, "
  "vẫn giữ lịch sự.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay trái của MAYA hạ xuống",
  ["MAYA_CUOI"], "giữa lối đi bãi xe, quay về phía tường nhà thờ",
  {"MAYA": "đứng một mình, điện thoại áp tai phải"}, "một mình trong khung",
  {"MAYA": "tay trái giơ ngang ngực ngửa lên"})
V("05", [6], "cận-trung 85mm · MAYA NÉT một mình, điện thoại áp tai phải · BILLING CLERK ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_CUOI"), (DT, "BILLING CLERK")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt. Người gọi KHÔNG xuất hiện, chỉ nghe giọng qua điện thoại.",
  "MAYA quay người về phía toà nhà thờ, tay trái giơ lên trình bày với người ở đầu dây bên kia",
  [("MAYA", "urgent, still polite", 6)])

S("06", "cận 85mm, cao 1m55, cách MAYA 1m2, đặt chính diện, hậu cảnh là bãi xe xoá phông",
  "MAYA đứng một mình chiếm phần lớn khung, điện thoại đã rời khỏi tai và đang hạ xuống ngang ngực. "
  "Hậu cảnh là bãi xe xoá phông.",
  "MAYA tay phải hạ chiếc điện thoại xuống ngang ngực, màn hình còn sáng; tay trái buông thõng.",
  "MAYA nhìn xuống màn hình điện thoại đang sáng trong tay mình.",
  "MAYA — người vừa nghe câu trả lời cuối cùng và hiểu rằng không còn ai để gọi nữa: mặt phẳng, mắt chớp chậm.",
  "đúng khoảnh khắc ngay TRƯỚC khi màn hình điện thoại tắt",
  ["MAYA_CUOI"], "giữa lối đi bãi xe",
  {"MAYA": "đứng một mình, điện thoại hạ ngang ngực"}, "một mình trong khung",
  {"MAYA": "tay phải hạ điện thoại xuống ngang ngực"})
V("06", [7], "cận 85mm · MAYA NÉT một mình, điện thoại hạ ngang ngực · BILLING CLERK ngoài khung, chỉ có giọng",
  [("MAYA", "MAYA_CUOI"), (DT, "BILLING CLERK")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt. Người gọi KHÔNG xuất hiện, chỉ nghe giọng qua điện thoại.",
  "giọng bên kia nói nốt câu cuối, MAYA hạ chiếc điện thoại xuống khỏi tai",
  [(DT, "flat, final", 7)], [("MAYA", "silent, lowering the phone")],
  ketclip="Cuối clip, một chiếc xe sedan đen ở cuối bãi nổ máy và bắt đầu lăn bánh về phía lối ra; MAYA ngẩng lên "
          "nhìn về phía đó rồi bước nhanh sang bên. Clip dừng đúng lúc cô bước bước đầu tiên.")

# ── NHỊP: CHẠY THEO XE ──
S("B2", "trung-rộng 35mm, cao 1m60, cách MAYA 7m, đặt phía lối ra bãi nhìn ngược lại",
  "MAYA đang bước nhanh giữa hai hàng xe, một tay vén cao vạt váy cưới. Phía trước cô, cách chừng bốn mét, một "
  "CHIẾC SEDAN ĐEN BÓNG đang lăn bánh chậm về phía lối ra, kính sau đã đóng, biển số làm mờ.",
  "MAYA một tay vén vạt váy lên khỏi mặt nhựa, tay kia còn nắm chiếc điện thoại.",
  "MAYA nhìn thẳng vào cửa kính sau bên phải của chiếc xe đang chạy.",
  "MAYA — người vừa nghĩ ra một chỗ cuối cùng để hỏi và biết mình chỉ có vài giây: mắt mở to, môi hé, chân bước gấp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đuổi kịp cửa kính sau của chiếc xe",
  ["MAYA_CUOI"], "giữa hai hàng xe đỗ, phía lối ra",
  {"MAYA": "bước nhanh giữa hai hàng xe"}, "cách chiếc xe bốn mét",
  {"MAYA": "một tay vén vạt váy, tay kia cầm điện thoại"})
B("B2", "MAYA nhìn thấy chiếc sedan đen của nhà Prescott đang lăn bánh ra cổng và bước gấp theo giữa hai hàng xe.",
  "trung-rộng 35mm · MAYA NÉT bước nhanh giữa hai hàng xe · không có ai khác trong khung",
  [("MAYA", "MAYA_CUOI")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt. Chiếc xe đen chạy phía trước KHÔNG nhìn thấy người bên trong.",
  "một người vừa hết cách và vừa nhìn thấy cánh cửa cuối cùng đang đóng lại trước mặt mình.",
  "MAYA vén váy bước gấp hơn, gấu váy quét trên mặt nhựa; chiếc xe đen chạy chậm dần rồi dừng lại chờ ở lối ra.",
  "SFX tiếng gót giày gõ gấp trên mặt nhựa và tiếng động cơ xe chạy chậm, Ambient tiếng gió.",
  nhac("NÂNG", "Đây là mốc chuyển từ mất mát sang cầu xin — nhạc tạo đà đi cùng bước chân nhưng không được lấn lời thoại sắp tới.",
       "Indie folk at 84 BPM building from a single muted acoustic guitar to guitar plus brushed snare and a low hum "
       "of strings, a female voice half-singing half-speaking one line every four bars; the pull is when the drums "
       "drop out entirely and only the guitar keeps walking; lyrics about running toward one last door with nothing "
       "left to offer; warm analog mix, female vocal, folk, driving, restrained",
       "Instrumental at 86 BPM; muted acoustic guitar walking in eighth notes, a low synth pad rising underneath, "
       "one shaker entering halfway and stopping abruptly near the end, leaving the guitar alone; "
       "warm analog mix, acoustic guitar, pad, shaker, walking pace, unresolved"),
  dur=8)

# ── QUỲ TRƯỚC CỬA XE ──
S("07", "trung 50mm, cao 1m40, cách MAYA 2m4, đặt bên hông xe lấy MAYA đứng và MRS. PRESCOTT trong khung cửa kính đã hạ",
  "MAYA đứng ở nửa PHẢI khung, cúi người xuống bên hông một chiếc sedan đen. Ở nửa TRÁI khung, qua Ô CỬA KÍNH SAU "
  "ĐÃ HẠ XUỐNG, thấy rõ MRS. PRESCOTT ngồi trong ghế sau, người quay ra.",
  "MAYA một bàn tay đặt lên khung cửa kính đã hạ, tay kia giữ vạt váy. MRS. PRESCOTT hai tay đặt trên chiếc túi da "
  "màu kem trên đùi.",
  "Hai người nhìn thẳng vào mắt nhau qua ô cửa kính.",
  "MAYA — người vừa chạy tới và đang cố nói cho gọn trước khi bị đuổi: thở gấp, mắt khẩn khoản, giọng nhanh. "
  "MRS. PRESCOTT — bị chặn lại bởi đúng người mình muốn tránh: cằm hếch, mí mắt hạ, mặt không động.",
  "đúng khoảnh khắc ngay TRƯỚC khi MRS. PRESCOTT quay hẳn mặt ra phía MAYA",
  ["MAYA_CUOI", "MRS. PRESCOTT"], "bên hông chiếc sedan đen, cạnh cửa sau",
  {"MAYA": "đứng cúi người nửa phải khung", "MRS. PRESCOTT": "ngồi ghế sau, thấy qua ô cửa kính đã hạ nửa trái khung"},
  "cách nhau một cánh tay", {"MAYA": "một tay đặt lên khung cửa kính", "MRS. PRESCOTT": "hai tay đặt trên túi da trên đùi"})
V("07", [8, 9], "trung 50mm · MAYA NÉT phải cúi bên hông xe + MRS. PRESCOTT NÉT trái ngồi trong ghế sau qua ô cửa kính đã hạ",
  [("MAYA", "MAYA_CUOI"), ("MRS. PRESCOTT", "MRS. PRESCOTT")],
  "MAYA và MRS. PRESCOTT, cả hai rõ mặt. Không thấy người lái xe.",
  "MAYA đặt tay lên khung cửa kính vừa hạ xuống, MRS. PRESCOTT quay mặt ra",
  [("MAYA", "breathless, pleading", 8), ("MRS. PRESCOTT", "clipped, weary", 9)])

S("08", "cận-trung 85mm, cao 1m30, cách MAYA 1m6, máy sau vai TRÁI của MRS. PRESCOTT; vai và gáy bà chiếm rìa trái, out nét",
  "MAYA chiếm phần lớn khung, đã hạ thấp người xuống ngang tầm cửa kính, một tay bám vào khung cửa. "
  "MRS. PRESCOTT chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh trong lòng xe, ngoài vùng nét. "
  "Hậu cảnh sau lưng MAYA là hàng xe đỗ và tường đá nhà thờ.",
  "MAYA một tay bám vào khung cửa kính, tay kia đưa ra phía trước, lòng bàn tay ngửa.",
  "MAYA nhìn thẳng vào mặt MRS. PRESCOTT qua ô cửa.",
  "MAYA — người đang mặc cả xuống một phần mười và sẵn sàng ký bất cứ thứ gì: giọng nhanh, mắt không chớp, "
  "cằm hơi run.",
  "đúng khoảnh khắc ngay TRƯỚC khi MRS. PRESCOTT nhìn xuống bàn tay đang bám khung cửa",
  ["MAYA_CUOI", "MRS. PRESCOTT"], "bên hông chiếc sedan đen, cạnh cửa sau",
  {"MAYA": "hạ thấp người, bám khung cửa kính", "MRS. PRESCOTT": "vai và gáy tiền cảnh trái trong lòng xe"},
  "cách nhau một cánh tay", {"MAYA": "một tay bám khung cửa, tay kia ngửa ra trước",
                             "MRS. PRESCOTT": "hai tay trên túi da, ngoài vùng nét"})
V("08", [10, 11], "OTS cận-trung 85mm · MAYA NÉT bên ngoài cửa xe · vai và gáy MRS. PRESCOTT tiền cảnh trái out nét",
  [("MAYA", "MAYA_CUOI"), ("MRS. PRESCOTT", "MRS. PRESCOTT")],
  "MAYA rõ mặt bên ngoài cửa xe. MRS. PRESCOTT chỉ thấy VAI VÀ GÁY ở tiền cảnh trái trong lòng xe, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA hạ người xuống ngang tầm cửa kính, một tay bám vào khung cửa",
  [("MAYA", "fast, pleading", 10), ("MRS. PRESCOTT", "flat, controlled", 11)])

S("09", "cận-trung 85mm, cao 0m80, cách MAYA 1m5, máy hạ thấp ngang tầm người đang quỳ bên hông xe",
  "MAYA đã quỳ hai gối trên mặt nhựa bên hông chiếc sedan đen, chiếm nửa PHẢI khung, đầu ngang tầm ô cửa kính. "
  "Qua ô cửa kính đã hạ ở nửa TRÁI khung thấy rõ mặt MRS. PRESCOTT nhìn xuống.",
  "MAYA một bàn tay vẫn đặt trên khung cửa kính, tay kia buông xuống đùi. MRS. PRESCOTT một tay đặt lên nút bấm "
  "cửa kính trên tay tựa.",
  "MAYA ngước lên nhìn thẳng vào mặt MRS. PRESCOTT. MRS. PRESCOTT nhìn xuống MAYA.",
  "MAYA — người chưa từng quỳ xin ai và đang làm việc đó trong bộ váy cưới giữa bãi xe: giọng vỡ nhẹ, mắt ướt, "
  "cằm vẫn ngẩng. MRS. PRESCOTT — nhìn xuống như nhìn một thứ vừa rơi vào tầm mắt: mặt hoàn toàn không động.",
  "đúng khoảnh khắc ngay TRƯỚC khi ngón tay MRS. PRESCOTT bấm xuống nút cửa kính",
  ["MAYA_CUOI", "MRS. PRESCOTT"], "bên hông chiếc sedan đen, MAYA quỳ trên mặt nhựa",
  {"MAYA": "quỳ hai gối nửa phải khung", "MRS. PRESCOTT": "ngồi ghế sau, thấy qua ô cửa kính nửa trái khung"},
  "cách nhau một cánh tay", {"MAYA": "một tay đặt trên khung cửa kính",
                             "MRS. PRESCOTT": "một tay đặt lên nút bấm cửa kính"})
V("09", [12], "cận-trung 85mm hạ thấp · MAYA NÉT phải quỳ bên hông xe + MRS. PRESCOTT NÉT trái nhìn xuống qua ô cửa kính",
  [("MAYA", "MAYA_CUOI"), ("MRS. PRESCOTT", "MRS. PRESCOTT")],
  "MAYA rõ mặt đang quỳ bên hông xe, MRS. PRESCOTT rõ mặt trong lòng xe qua ô cửa kính đã hạ.",
  "MAYA quỳ xuống mặt nhựa bên hông xe và ngước lên",
  [("MAYA", "breaking, honest", 12)], [("MRS. PRESCOTT", "silent, looking down")])

S("10", "cận 85mm, cao 0m90, cách MRS. PRESCOTT 1m2, máy hạ thấp nhìn hơi chếch lên qua ô cửa kính vào lòng xe",
  "MRS. PRESCOTT chiếm phần lớn khung, ngồi trong ghế sau bọc da sáng màu, người quay ra phía ô cửa kính đã hạ. "
  "Ở rìa DƯỚI khung thấy một phần vai và mái tóc búi của MAYA đang quỳ bên ngoài, out nét.",
  "MRS. PRESCOTT một tay giữ quai chiếc túi da màu kem, ngón trỏ tay kia đặt lên nút bấm cửa kính.",
  "MRS. PRESCOTT nhìn xuống thẳng vào mặt MAYA.",
  "MRS. PRESCOTT — người đang nói ra điều mình thật sự nghĩ bằng giọng của một buổi trà chiều: mí mắt hạ, "
  "khoé môi phẳng, không hề to tiếng.",
  "đúng khoảnh khắc ngay TRƯỚC khi tấm kính cửa bắt đầu dâng lên",
  ["MRS. PRESCOTT", "MAYA_CUOI"], "trong lòng chiếc sedan đen, cạnh ô cửa kính đã hạ",
  {"MRS. PRESCOTT": "ngồi ghế sau giữa khung", "MAYA": "một phần vai và tóc ở rìa dưới khung, đang quỳ bên ngoài"},
  "cách nhau một cánh tay", {"MRS. PRESCOTT": "một tay giữ quai túi, ngón trỏ trên nút bấm cửa kính",
                             "MAYA": "một tay trên khung cửa, ngoài vùng nét"})
V("10", [13], "cận 85mm · MRS. PRESCOTT NÉT trong lòng xe · vai và tóc MAYA rìa dưới khung out nét",
  [("MRS. PRESCOTT", "MRS. PRESCOTT"), ("MAYA", "MAYA_CUOI")],
  "MRS. PRESCOTT rõ mặt trong lòng xe. MAYA chỉ thấy MỘT PHẦN VAI VÀ MÁI TÓC ở rìa dưới khung, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MRS. PRESCOTT nhìn xuống người đang quỳ bên ngoài cửa xe và trả lời",
  [("MRS. PRESCOTT", "even, dismissive", 13)], [("MAYA", "silent, kneeling")])

S("11", "trung 50mm, cao 0m90, cách MAYA 2m, máy hạ thấp bên hông xe lấy cả hai người",
  "MAYA quỳ ở nửa PHẢI khung bên hông xe, một bàn tay ĐANG ĐẶT TRONG KHE CỬA KÍNH đã hạ. Ở nửa TRÁI khung, "
  "qua ô cửa, thấy MRS. PRESCOTT ngồi trong ghế sau, mặt quay ra.",
  "MAYA một bàn tay đặt hẳn vào khe cửa kính, các ngón bám lên mép kính; tay kia chống xuống mặt nhựa. "
  "MRS. PRESCOTT ngón trỏ vẫn đặt trên nút bấm.",
  "Hai người nhìn thẳng vào mắt nhau qua ô cửa.",
  "MAYA — người nói ra sự thật ngắn nhất mà mình có: giọng khàn, mắt thẳng. "
  "MRS. PRESCOTT — nghe xong và không đổi nét mặt một chút nào: mắt lạnh, môi mỏng khép.",
  "đúng khoảnh khắc ngay TRƯỚC khi tấm kính chạm vào các ngón tay của MAYA",
  ["MAYA_CUOI", "MRS. PRESCOTT"], "bên hông chiếc sedan đen, MAYA quỳ trên mặt nhựa",
  {"MAYA": "quỳ nửa phải khung, tay đặt trong khe cửa kính",
   "MRS. PRESCOTT": "ngồi ghế sau, thấy qua ô cửa nửa trái khung"},
  "cách nhau một cánh tay", {"MAYA": "một bàn tay đặt trong khe cửa kính, tay kia chống mặt nhựa",
                             "MRS. PRESCOTT": "ngón trỏ trên nút bấm cửa kính"})
V("11", [14, 15], "trung 50mm hạ thấp · MAYA NÉT phải quỳ, tay trong khe cửa kính + MRS. PRESCOTT NÉT trái trong lòng xe",
  [("MAYA", "MAYA_CUOI"), ("MRS. PRESCOTT", "MRS. PRESCOTT")],
  "MAYA và MRS. PRESCOTT, cả hai rõ mặt qua ô cửa kính đã hạ. Không thấy người lái xe.",
  "MAYA đặt hẳn bàn tay vào khe cửa kính, MRS. PRESCOTT giữ nguyên ngón tay trên nút bấm",
  [("MAYA", "hoarse, plain", 14), ("MRS. PRESCOTT", "even, final", 15)])

S("12", "cận 85mm, cao 0m90, cách MAYA 1m1, máy hạ thấp bên ngoài xe, lấy mặt MAYA và một phần ô cửa kính",
  "MAYA chiếm phần lớn khung, vẫn quỳ, mặt ngang tầm ô cửa kính đang DÂNG LÊN, bàn tay còn kẹt giữa mép kính "
  "và khung cửa. Qua phần ô cửa còn hở ở rìa TRÁI khung thấy một phần mặt MRS. PRESCOTT bên trong.",
  "MAYA một bàn tay kẹt trong khe cửa, các ngón căng ra; tay kia bám vào thân xe.",
  "MAYA nhìn vào phần mặt còn thấy được của MRS. PRESCOTT qua khe cửa đang hẹp dần.",
  "MAYA — người vừa hiểu chuyện gì đang xảy ra với bàn tay mình: mắt mở to, miệng hé, mặt tái đi. "
  "MRS. PRESCOTT — không nhìn xuống bàn tay đó: mặt phẳng lặng.",
  "đúng khoảnh khắc ngay TRƯỚC khi chiếc xe bắt đầu lăn bánh",
  ["MAYA_CUOI", "MRS. PRESCOTT"], "bên hông chiếc sedan đen, MAYA quỳ trên mặt nhựa",
  {"MAYA": "quỳ, tay kẹt trong khe cửa kính đang dâng",
   "MRS. PRESCOTT": "thấy một phần mặt qua khe cửa còn hở, rìa trái khung"},
  "cách nhau một cánh tay", {"MAYA": "một bàn tay kẹt trong khe cửa, tay kia bám thân xe",
                             "MRS. PRESCOTT": "một tay còn trên nút bấm"})
V("12", [16, 17], "cận 85mm hạ thấp · MAYA NÉT quỳ bên ngoài xe · MRS. PRESCOTT thấy một phần mặt qua khe cửa rìa trái",
  [("MAYA", "MAYA_CUOI"), ("MRS. PRESCOTT", "MRS. PRESCOTT")],
  "MAYA rõ mặt bên ngoài xe. MRS. PRESCOTT chỉ thấy MỘT PHẦN MẶT qua khe cửa kính còn hở ở rìa trái, không phải "
  "trọng tâm khung.",
  "tấm kính cửa dâng lên và ép vào các ngón tay MAYA còn kẹt trong khe",
  [("MAYA", "alarmed, urgent", 16), ("MRS. PRESCOTT", "flat, unmoved", 17)],
  ketclip="Cuối clip, MAYA rút phắt bàn tay ra khỏi khe cửa, tấm kính đóng kín, chiếc xe lăn bánh đi khỏi khung; "
          "cô ngã ngồi lại trên hai gót chân giữa lối đi. Clip dừng đúng lúc chiếc xe ra khỏi khung.")

# ── NHỊP KHÉP CẢNH ──
S("B3", "toàn cảnh 24mm, cao 1m60, cách MAYA 9m, đặt phía cửa hông nhà thờ nhìn ra lối ra bãi",
  "MAYA ngồi lại một mình trên hai gót chân giữa lối đi của bãi xe, váy cưới xoè trên mặt nhựa xám. Ô đỗ xe trước "
  "mặt cô đã trống. Bãi xe rộng và vắng bao quanh cô từ mọi phía.",
  "MAYA hai tay đặt trên đùi, bàn tay phải ôm lấy các ngón tay trái.",
  "MAYA nhìn theo phía lối ra bãi nơi chiếc xe vừa đi khỏi.",
  "MAYA — người vừa quỳ xin và bị từ chối, còn ba mươi mốt tiếng để tìm hai trăm nghìn: mặt trống, "
  "vai bắt đầu chùng xuống lần đầu tiên trong cả buổi sáng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA chống tay xuống mặt nhựa để đứng dậy",
  ["MAYA_CUOI"], "giữa lối đi bãi xe, ô đỗ trước mặt đã trống",
  {"MAYA": "ngồi lại trên hai gót chân giữa lối đi"}, "một mình trong khung",
  {"MAYA": "hai tay đặt trên đùi, tay phải ôm các ngón tay trái"})
B("B3", "Khép cảnh. Chiếc xe đã đi. MAYA ngồi lại một mình giữa bãi đỗ xe trống, váy cưới xoè trên mặt nhựa.",
  "toàn cảnh 24mm · MAYA NÉT ngồi một mình giữa bãi xe · không có ai khác trong khung",
  [("MAYA", "MAYA_CUOI")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, ngồi giữa lối đi bãi xe. Không có người nào khác.",
  "tỷ lệ giữa một người và một bãi xe trống chính là nội dung của khung hình này: cô vừa dùng hết chỗ cuối cùng "
  "mình có thể hỏi, và không ai ở lại để nhìn thấy điều đó.",
  "MAYA ngồi yên vài giây, ôm lấy các ngón tay vừa bị kẹp; gió thổi gấu váy cưới động nhẹ trên mặt nhựa; "
  "cô chống tay xuống định đứng lên.",
  "Ambient tiếng gió qua bãi trống và tiếng xe chạy rất xa ngoài đường, SFX tiếng vải váy quét trên mặt nhựa.",
  nhac("KÌM", "Cô không được phép khóc ở đây — nhạc phải nhỏ hơn cảm xúc thật, đúng như cách cô đang gồng.",
       "Soul ballad at 60 BPM with a female alto sung very close to the mic, dry and almost spoken; Rhodes and upright "
       "bass only, no drums at any point; one single string note swelling at the midpoint then gone; lyrics about "
       "kneeling in a parking lot in a borrowed dress and getting back up because there is no one else to do it; "
       "dry intimate mix, female vocal, soul, restrained, sparse",
       "Chamber instrumental at 56 BPM; one violin holding a long note over a barely audible piano pedal, a cello "
       "answering four seconds later a fifth below, no percussion, no build, fading before it resolves; "
       "very quiet, close-miked, violin, cello, piano, minimal, unresolved"),
  dur=10)
