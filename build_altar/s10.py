# -*- coding: utf-8 -*-
"""SCENE 10 — VỈA HÈ TRƯỚC QUÁN CÀ PHÊ (ban ngày). Cốc cà phê và cú hất xe lăn."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S10", "REF_VIAHE_NGAY", qc=qc.S10)

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 6m, đặt trên vỉa hè nhìn dọc về phía mặt tiền quán",
  "MAYA đang đẩy chiếc xe lăn có ADRIAN ngồi đi dọc vỉa hè về phía mái hiên bạt xanh của quán cà phê. "
  "Dưới mái hiên có hai ba khách ngồi ở bàn tròn, mờ ngoài vùng nét, không ai nhìn vào ống kính.",
  "MAYA hai tay đặt trên tay đẩy xe lăn. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn về phía dốc xe lăn bằng bê tông trước cửa quán. ADRIAN nhìn thẳng phía trước.",
  "MAYA — người đang có một buổi chiều bình thường đầu tiên sau nhiều tuần: mặt giãn ra, khoé môi hơi kéo. "
  "ADRIAN — thoải mái hơn mọi cảnh trước: vai buông, mắt nheo nhẹ vì nắng.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng gọi tên vọng tới từ đầu phố",
  ["MAYA_CARO", "ADRIAN_NHA"], "giữa vỉa hè trước quán cà phê",
  {"MAYA": "đẩy xe lăn đi dọc vỉa hè", "ADRIAN": "ngồi trong xe lăn"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay trên tay đẩy xe lăn", "ADRIAN": "hai tay trên vành tay vịn"})
B("B1", "Mở cảnh. Một buổi chiều bình thường: MAYA đẩy ADRIAN dọc vỉa hè về phía quán cà phê.",
  "trung-rộng 35mm · MAYA NÉT đẩy xe lăn + ADRIAN NÉT ngồi trong xe · khách quán mờ ở hậu cảnh",
  [("MAYA", "MAYA_CARO"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN rõ mặt. Vài khách ngồi dưới mái hiên quán mờ ở hậu cảnh, không ai nhìn vào camera.",
  "lần đầu tiên trong phim hai người này ra ngoài đường mà không phải để giải quyết một khủng hoảng nào; "
  "sự bình thường ấy sắp bị lấy đi trong ba mươi giây.",
  "MAYA đẩy xe đi đều, nghiêng người tránh một ô gạch nứt; ADRIAN đưa tay che nắng một nhịp; "
  "một chiếc xe chạy qua phía lòng đường.",
  "Ambient tiếng phố ban ngày, tiếng xe chạy và tiếng cốc chén lách cách dưới mái hiên quán.",
  nhac("NGHỈ", "Khoảng thở duy nhất giữa hai chương nặng — nhạc phải nhẹ và ấm để cú tấn công ngay sau đó đau hơn.",
       "Warm folk at 72 BPM; acoustic guitar picking a light figure, brushes on a snare very quietly, a female voice "
       "entering with two short lines sung easily; the pull is when the guitar lands on one bright chord and holds; "
       "lyrics about an ordinary afternoon that costs nothing; warm analog mix, female vocal, guitar, folk, easy",
       "Instrumental at 70 BPM; acoustic guitar and a soft upright bass walking together, a brushed snare very light, "
       "one clarinet line entering warm and unhurried, no build, ending easily; warm daylight mix, guitar, bass, "
       "clarinet, easy, light"),
  dur=6)

# ── HAI PHÍA GẶP NHAU ──
S("01", "trung 50mm, cao 1m55, cách VANESSA 2m4, đặt trên vỉa hè lấy cả hai người, hậu cảnh là hàng xe đỗ",
  "VANESSA đứng ở nửa TRÁI khung trên vỉa hè, đã dừng chân và quay hẳn về phía máy. RYAN đứng ở nửa PHẢI khung "
  "sát cạnh cô, cũng đã dừng lại. Hậu cảnh là hàng xe đỗ dọc đường và dãy nhà phố gạch nâu bên kia đường.",
  "VANESSA một tay nắm cánh tay RYAN kéo lại, tay kia cầm quai chiếc túi da. RYAN một tay đút túi quần.",
  "VANESSA nhìn về phía chiếc xe lăn ngoài khung. RYAN nhìn theo hướng đó.",
  "VANESSA — người vừa nhìn thấy một món giải trí: mắt sáng lên, khoé môi kéo. "
  "RYAN — người muốn đi tiếp và biết chuyện này sẽ tệ: quai hàm siết, mắt dời đi.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA bước một bước về phía chiếc xe lăn",
  ["VANESSA_NGAY", "RYAN_ADO"], "vỉa hè phía đầu phố, cách quán cà phê vài bước",
  {"VANESSA": "đứng nửa trái khung", "RYAN": "đứng nửa phải khung sát cạnh VANESSA"},
  "sát cạnh nhau", {"VANESSA": "một tay nắm cánh tay RYAN, tay kia cầm quai túi",
                    "RYAN": "một tay đút túi quần"})
V("01", [0, 1], "trung 50mm · VANESSA NÉT trái + RYAN NÉT phải, cả hai đứng trên vỉa hè",
  [("VANESSA", "VANESSA_NGAY"), ("RYAN", "RYAN_ADO")],
  "VANESSA và RYAN, cả hai rõ mặt trên vỉa hè. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA nắm cánh tay RYAN kéo lại và hất cằm về phía chiếc xe lăn",
  [("VANESSA", "delighted, malicious", 0), ("RYAN", "flat, reluctant", 1)])

S("02", "trung 50mm, cao 1m40, cách MAYA 2m4, đặt trên vỉa hè, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung sau chiếc xe lăn, đã dừng đẩy. ADRIAN ngồi trong xe lăn ở giữa khung. "
  "VANESSA đứng ở nửa TRÁI khung phía trước, cách hai bước, thấy rõ mặt.",
  "MAYA hai tay ghì lại trên tay đẩy xe lăn. ADRIAN hai tay đặt trên vành tay vịn. "
  "VANESSA một tay cầm quai túi, tay kia chỉ về phía chiếc xe.",
  "VANESSA nhìn thẳng vào MAYA. MAYA nhìn lại VANESSA. ADRIAN nhìn thẳng phía trước.",
  "VANESSA — người đang thưởng thức đúng thứ mình muốn thấy: cằm hếch, khoé môi cong. "
  "MAYA — vừa nhận ra ai đang đứng chắn phía trước: quai hàm siết, giọng hạ xuống. ADRIAN — mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA xoay chiếc xe lăn sang hướng khác",
  ["MAYA_CARO", "ADRIAN_NHA", "VANESSA_NGAY"], "giữa vỉa hè trước quán cà phê",
  {"MAYA": "đứng sau xe lăn nửa phải khung", "ADRIAN": "ngồi xe lăn giữa khung",
   "VANESSA": "đứng nửa trái khung phía trước"},
  "VANESSA cách hai bước", {"MAYA": "hai tay ghì trên tay đẩy xe lăn", "ADRIAN": "hai tay trên vành tay vịn",
                            "VANESSA": "một tay cầm quai túi, tay kia chỉ về chiếc xe"})
V("02", [2, 3], "trung 50mm hạ thấp · VANESSA NÉT trái + ADRIAN NÉT giữa ngồi xe lăn + MAYA NÉT phải sau xe",
  [("VANESSA", "VANESSA_NGAY"), ("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_CARO")],
  "VANESSA, ADRIAN và MAYA, cả ba rõ mặt. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA chỉ tay về phía chiếc xe lăn, MAYA ghì tay đẩy lại và định xoay xe sang hướng khác",
  [("VANESSA", "amused, cutting", 2), ("MAYA", "low, to Adrian", 3)])

S("03", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m6, đặt bên hông xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, đã ngẩng lên. MAYA đứng ở nửa PHẢI khung ngay sau vai anh, "
  "cúi xuống. VANESSA đứng mờ ở hậu cảnh phía sau, thấy dáng người và một phần mặt, ngoài vùng nét.",
  "ADRIAN một tay siết chặt vành tay vịn. MAYA một tay đặt lên vai ADRIAN.",
  "ADRIAN nhìn thẳng về phía VANESSA phía trước. MAYA nhìn xuống ADRIAN.",
  "ADRIAN — người quyết định không tránh nữa: mặt hoàn toàn bình, mắt tĩnh, giọng rất nhỏ. "
  "MAYA — nghe một chữ NO và hiểu ngay: mày chau, tay siết lại trên vai anh.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA bước tới sát chiếc xe lăn",
  ["ADRIAN_NHA", "MAYA_CARO", "VANESSA_NGAY"], "giữa vỉa hè trước quán cà phê",
  {"ADRIAN": "ngồi xe lăn nửa trái khung", "MAYA": "đứng cúi xuống sau vai ADRIAN, nửa phải khung",
   "VANESSA": "đứng mờ ở hậu cảnh phía sau, ngoài vùng nét"},
  "VANESSA cách hai bước", {"ADRIAN": "một tay siết vành tay vịn", "MAYA": "một tay đặt lên vai ADRIAN",
                            "VANESSA": "một tay cầm quai túi, ngoài vùng nét"})
V("03", [4, 5], "cận-trung 85mm hạ thấp · ADRIAN NÉT trái ngồi xe lăn + MAYA NÉT phải cúi xuống · VANESSA mờ ở hậu cảnh",
  [("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_CARO"), ("VANESSA", "VANESSA_NGAY")],
  "ADRIAN và MAYA rõ mặt. VANESSA chỉ thấy dáng người MỜ ở hậu cảnh, ngoài vùng nét, KHÔNG rõ mặt.",
  "ADRIAN siết vành tay vịn và trả lời một chữ, VANESSA tiến lại gần hơn",
  [("ADRIAN", "quiet, final", 4), ("VANESSA", "sing-song, mocking", 5)])

S("04", "cận-trung 85mm, cao 1m55, cách MAYA 1m7, máy sau vai TRÁI của RYAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, một tay còn trên tay đẩy xe lăn ở rìa dưới khung. RYAN chỉ còn là "
  "vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MAYA là mái hiên bạt xanh của quán.",
  "MAYA một tay giữ tay đẩy xe lăn, tay kia đưa lên ngang ngực, lòng bàn tay hướng ra ngoài.",
  "MAYA nhìn thẳng vào mặt RYAN qua vai anh.",
  "MAYA — người chỉ muốn đi qua và không muốn cãi nhau giữa phố: giọng bình, mắt thẳng, không hằn học.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bước chắn sang một bên",
  ["MAYA_CARO", "RYAN_ADO"], "giữa vỉa hè trước quán cà phê, cạnh dốc xe lăn",
  {"MAYA": "đứng chính diện giữa khung", "RYAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "một tay giữ tay đẩy xe lăn, tay kia đưa ngang ngực",
                         "RYAN": "một tay đút túi quần, ngoài vùng nét"})
V("04", [6, 7], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy RYAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_CARO"), ("RYAN", "RYAN_ADO")],
  "MAYA rõ mặt chính diện. RYAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đưa tay lên ngang ngực xin đường, RYAN bước chắn sang một bên",
  [("MAYA", "even, tired", 6), ("RYAN", "wounded, sharpish", 7)])

S("05", "trung 50mm, cao 1m55, cách MAYA 2m2, đặt trên vỉa hè lấy MAYA và RYAN, hậu cảnh là mặt tiền quán",
  "MAYA đứng ở nửa PHẢI khung, RYAN đứng ở nửa TRÁI khung cách một bước, người hơi chồm tới. "
  "Hậu cảnh là mặt tiền kính của quán cà phê và tấm bảng đen chữ A cạnh cửa.",
  "MAYA hai tay đặt lại trên tay đẩy xe lăn. RYAN một tay chỉ vào chính mình rồi hạ xuống.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người trả lời bằng đúng sự thật, không thêm gia vị: giọng đều, mắt thẳng. "
  "RYAN — người thấy mình là nạn nhân trong câu chuyện của chính mình: mày chau, giọng cao lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN lùi lại nửa bước",
  ["MAYA_CARO", "RYAN_ADO"], "giữa vỉa hè trước quán cà phê",
  {"MAYA": "đứng nửa phải khung sau xe lăn", "RYAN": "đứng nửa trái khung, chồm tới"},
  "cách nhau một bước", {"MAYA": "hai tay trên tay đẩy xe lăn",
                         "RYAN": "một tay chỉ vào chính mình rồi hạ xuống"})
V("05", [8, 9], "trung 50mm · MAYA NÉT phải + RYAN NÉT trái, cả hai đứng trên vỉa hè",
  [("MAYA", "MAYA_CARO"), ("RYAN", "RYAN_ADO")],
  "MAYA và RYAN, cả hai rõ mặt. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "RYAN chồm tới chỉ vào chính mình, MAYA giữ nguyên hai tay trên tay đẩy xe",
  [("MAYA", "level, plain", 8), ("RYAN", "defensive, raised", 9)])

S("06", "trung 50mm, cao 1m40, cách VANESSA 2m2, đặt bên hông xe lăn, hạ thấp để lấy cả ba người",
  "VANESSA đứng ở nửa TRÁI khung, đã bước tới sát trước chiếc xe lăn và cúi người xuống. ADRIAN ngồi trong "
  "xe lăn ở giữa khung. MAYA đứng ở nửa PHẢI khung sau xe, một tay đã rời tay đẩy.",
  "VANESSA một tay chống lên đầu gối, tay kia cầm cốc cà phê giấy có nắp. ADRIAN hai tay đặt trên vành tay vịn. "
  "MAYA một tay đưa ra phía trước cảnh cáo.",
  "VANESSA nhìn xuống mặt ADRIAN. ADRIAN nhìn thẳng lên VANESSA. MAYA nhìn bàn tay VANESSA.",
  "VANESSA — người đang chọc một con vật trong chuồng: mắt sáng, khoé môi cong. "
  "ADRIAN — không né mắt: mặt bình. MAYA — thấy nguy hiểm và bước lên: mày chau, giọng gằn xuống.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay VANESSA chạm vào tay vịn của chiếc xe",
  ["VANESSA_NGAY", "ADRIAN_NHA", "MAYA_CARO"], "giữa vỉa hè, sát trước chiếc xe lăn",
  {"VANESSA": "đứng cúi xuống nửa trái khung", "ADRIAN": "ngồi xe lăn giữa khung",
   "MAYA": "đứng sau xe lăn nửa phải khung"},
  "VANESSA cách ADRIAN nửa mét",
  {"VANESSA": "một tay chống đầu gối, tay kia cầm cốc cà phê giấy",
   "ADRIAN": "hai tay trên vành tay vịn", "MAYA": "một tay đưa ra phía trước cảnh cáo"})
V("06", [10, 11], "trung 50mm hạ thấp · VANESSA NÉT trái cúi xuống + ADRIAN NÉT giữa ngồi xe lăn + MAYA NÉT phải sau xe",
  [("VANESSA", "VANESSA_NGAY"), ("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_CARO")],
  "VANESSA, ADRIAN và MAYA, cả ba rõ mặt. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "MAYA nói xong, VANESSA cúi hẳn xuống trước chiếc xe lăn, tay kia cầm cốc cà phê giấy",
  [("MAYA", "flat, weary", 10), ("VANESSA", "mocking, sweet", 11)])

S("07", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m4, đặt bên hông xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. VANESSA đứng ở nửa TRÁI khung phía trên anh, một bàn tay "
  "ĐÃ ĐẶT LÊN TAY VỊN của chiếc xe. MAYA thấy một phần vai ở rìa PHẢI khung, out nét.",
  "VANESSA một bàn tay đặt lên tay vịn xe lăn, tay kia cầm cốc cà phê giấy. ADRIAN hai tay siết vành tay vịn. ",
  "ADRIAN nhìn thẳng lên mặt VANESSA. VANESSA nhìn xuống ADRIAN.",
  "ADRIAN — người ra lệnh bằng đúng một chữ, không to tiếng: mắt tĩnh, quai hàm siết. "
  "VANESSA — thấy buồn cười vì cái ghế biết nói: mày nhướn, khoé môi cong.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA đẩy mạnh chiếc xe lăn",
  ["ADRIAN_NHA", "VANESSA_NGAY", "MAYA_CARO"], "giữa vỉa hè, sát trước chiếc xe lăn",
  {"ADRIAN": "ngồi xe lăn giữa khung", "VANESSA": "đứng phía trên nửa trái khung, tay đặt lên tay vịn",
   "MAYA": "một phần vai ở rìa phải khung"},
  "sát nhau", {"ADRIAN": "hai tay siết vành tay vịn", "VANESSA": "một tay đặt trên tay vịn xe, tay kia cầm cốc cà phê",
               "MAYA": "một tay đưa ra phía trước, ngoài vùng nét"})
V("07", [12, 13, 14, 15], "cận-trung 85mm hạ thấp · ADRIAN NÉT ngồi xe lăn + VANESSA NÉT trái phía trên · một phần vai MAYA rìa phải out nét",
  [("ADRIAN", "ADRIAN_NHA"), ("VANESSA", "VANESSA_NGAY"), ("MAYA", "MAYA_CARO")],
  "ADRIAN và VANESSA rõ mặt. MAYA chỉ thấy MỘT PHẦN VAI ở rìa phải, out nét — KHÔNG quay mặt về camera.",
  "VANESSA đặt bàn tay lên tay vịn chiếc xe lăn và giữ nguyên ở đó",
  [("ADRIAN", "quiet, commanding", 12), ("VANESSA", "amused, light", 13),
   ("MAYA", "sharp, warning", 14), ("VANESSA", "light, careless", 15)],
  ketclip="Cuối clip, VANESSA đẩy mạnh chiếc xe lăn về phía mép vỉa hè, xe nghiêng đổ và ADRIAN ngã ra khỏi ghế "
          "xuống mặt bê tông. Clip dừng đúng lúc vai anh chạm vỉa hè.")

S("08", "trung 50mm, cao 0m70, cách MAYA 2m, máy hạ rất thấp ngang mặt vỉa hè",
  "ADRIAN nằm nghiêng trên mặt vỉa hè ở nửa TRÁI khung, chiếc xe lăn đổ nghiêng cạnh anh, một bánh xe còn quay. "
  "MAYA đã quỳ xuống bên cạnh anh ở giữa khung. VANESSA đứng ở nửa PHẢI khung phía trên hai người.",
  "MAYA một tay đỡ sau gáy ADRIAN, tay kia đưa MỘT ngón trỏ lên trước mắt anh. ADRIAN một tay chống xuống mặt vỉa hè. "
  "VANESSA một tay cầm cốc cà phê giấy, tay kia chống hông.",
  "MAYA nhìn thẳng vào mắt ADRIAN. ADRIAN nhìn theo đầu ngón tay cô. VANESSA nhìn xuống hai người.",
  "MAYA — điều dưỡng hồi sức đang kiểm tra cột sống cổ, không có thời gian cho cảm xúc: giọng nhanh, gọn, "
  "mắt quét. ADRIAN — đau nhưng không kêu: quai hàm siết. VANESSA — thấy phản ứng đó thừa thãi: mắt đảo.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA nghiêng cốc cà phê xuống",
  ["MAYA_CARO", "ADRIAN_NHA", "VANESSA_NGAY"], "mặt vỉa hè, ADRIAN nằm nghiêng, xe lăn đổ cạnh đó",
  {"MAYA": "quỳ giữa khung bên cạnh ADRIAN", "ADRIAN": "nằm nghiêng trên vỉa hè nửa trái khung",
   "VANESSA": "đứng phía trên nửa phải khung"},
  "MAYA sát cạnh ADRIAN, VANESSA đứng cách một bước",
  {"MAYA": "một tay đỡ sau gáy ADRIAN, tay kia đưa một ngón trỏ lên", "ADRIAN": "một tay chống xuống mặt vỉa hè",
   "VANESSA": "một tay cầm cốc cà phê, tay kia chống hông"})
V("08", [16, 17], "trung 50mm hạ rất thấp · MAYA NÉT giữa quỳ trên vỉa hè + ADRIAN NÉT trái nằm nghiêng + VANESSA NÉT phải đứng phía trên",
  [("MAYA", "MAYA_CARO"), ("ADRIAN", "ADRIAN_NHA"), ("VANESSA", "VANESSA_NGAY")],
  "MAYA, ADRIAN và VANESSA, cả ba rõ mặt. ADRIAN NẰM NGHIÊNG trên mặt vỉa hè, chiếc xe lăn đổ cạnh anh. "
  "Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "MAYA quỳ xuống đỡ gáy ADRIAN và đưa một ngón trỏ lên trước mắt anh để kiểm tra",
  [("MAYA", "fast, clinical", 16), ("VANESSA", "bored, dismissive", 17)])

S("09", "cận-trung 85mm, cao 0m80, cách MAYA 1m5, máy hạ rất thấp ngang mặt vỉa hè",
  "MAYA quỳ chiếm phần lớn khung, đã ngẩng phắt lên. Ở rìa TRÁI khung thấy vai ADRIAN nằm và một phần khung xe lăn "
  "đổ, out nét. Ở rìa PHẢI khung thấy chân và tà áo khoác của VANESSA đứng phía trên, out nét.",
  "MAYA một tay vẫn đỡ sau gáy ADRIAN, tay kia nắm chặt lại trên đùi mình.",
  "MAYA nhìn thẳng lên mặt VANESSA.",
  "MAYA — người vừa gọi đúng tên việc vừa xảy ra: giọng thấp, rõ từng chữ, mắt không chớp.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA mở nắp cốc cà phê",
  ["MAYA_CARO", "ADRIAN_NHA", "VANESSA_NGAY"], "mặt vỉa hè, MAYA quỳ cạnh ADRIAN",
  {"MAYA": "quỳ chính diện giữa khung", "ADRIAN": "vai và một phần khung xe lăn đổ ở rìa trái",
   "VANESSA": "chân và tà áo khoác ở rìa phải khung"},
  "sát nhau", {"MAYA": "một tay đỡ gáy ADRIAN, tay kia nắm chặt trên đùi",
               "ADRIAN": "nằm nghiêng, ngoài vùng nét", "VANESSA": "một tay cầm cốc cà phê, ngoài vùng nét"})
V("09", [18], "cận-trung 85mm hạ rất thấp · MAYA NÉT quỳ chính diện · vai ADRIAN và khung xe lăn đổ rìa trái out nét · chân VANESSA rìa phải out nét",
  [("MAYA", "MAYA_CARO"), ("ADRIAN", "ADRIAN_NHA"), ("VANESSA", "VANESSA_NGAY")],
  "MAYA rõ mặt đang quỳ. ADRIAN chỉ thấy VAI ở rìa trái cùng khung xe lăn đổ, out nét. VANESSA chỉ thấy CHÂN "
  "và tà áo khoác ở rìa phải, out nét — KHÔNG ai trong hai người quay mặt về camera.",
  "MAYA ngẩng phắt lên nhìn thẳng lên phía trên và nói",
  [("MAYA", "low, precise", 18)], [("VANESSA", "silent, opening the cup")])

S("10", "trung 50mm, cao 0m90, cách VANESSA 2m, máy hạ thấp bên vỉa hè lấy cả ba người",
  "VANESSA đứng ở nửa PHẢI khung, cốc cà phê giấy ĐÃ MỞ NẮP trong tay, nghiêng nhẹ. ADRIAN nằm nghiêng ở "
  "nửa TRÁI khung, MAYA quỳ giữa khung cạnh anh, mặt ngẩng lên.",
  "VANESSA một tay cầm cốc cà phê đã mở nắp nghiêng nhẹ về phía trước, tay kia buông. "
  "MAYA một tay đỡ gáy ADRIAN, tay kia chống xuống mặt vỉa hè. ADRIAN một tay chống xuống vỉa hè.",
  "VANESSA nhìn xuống hai chân ADRIAN. MAYA nhìn cốc cà phê trong tay VANESSA. ADRIAN nhìn thẳng lên VANESSA.",
  "VANESSA — người vừa nghĩ ra một trò và thấy nó buồn cười: khoé môi kéo, mắt sáng. "
  "MAYA — thấy trước chuyện sắp xảy ra: mắt mở to. ADRIAN — không rời mắt khỏi mặt VANESSA: mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi giọt cà phê đầu tiên rời khỏi miệng cốc",
  ["VANESSA_NGAY", "MAYA_CARO", "ADRIAN_NHA"], "mặt vỉa hè, ADRIAN nằm nghiêng, MAYA quỳ cạnh anh",
  {"VANESSA": "đứng nửa phải khung, cốc đã mở nắp", "MAYA": "quỳ giữa khung",
   "ADRIAN": "nằm nghiêng nửa trái khung"},
  "VANESSA đứng cách một bước",
  {"VANESSA": "một tay cầm cốc cà phê đã mở nắp nghiêng về phía trước",
   "MAYA": "một tay đỡ gáy ADRIAN, tay kia chống mặt vỉa hè", "ADRIAN": "một tay chống xuống vỉa hè"})
V("10", [19], "trung 50mm hạ thấp · VANESSA NÉT phải cầm cốc cà phê + MAYA NÉT giữa quỳ + ADRIAN NÉT trái nằm nghiêng",
  [("VANESSA", "VANESSA_NGAY"), ("MAYA", "MAYA_CARO"), ("ADRIAN", "ADRIAN_NHA")],
  "VANESSA, MAYA và ADRIAN, cả ba rõ mặt. ADRIAN nằm nghiêng trên vỉa hè cạnh chiếc xe lăn đổ. "
  "Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA mở nắp cốc cà phê và nghiêng nó xuống phía hai chân ADRIAN",
  [("VANESSA", "light, cruel", 19)],
  [("MAYA", "silent, seeing it coming"), ("ADRIAN", "silent, holding her gaze")])

S("11", "cận-trung 85mm, cao 1m55, cách RYAN 1m7, đặt trên vỉa hè lấy RYAN nét và VANESSA trong khung",
  "RYAN đứng ở nửa TRÁI khung, đã bước lên một bước. VANESSA đứng ở nửa PHẢI khung, cốc cà phê đã cạn trong tay, "
  "quay đầu lại nhìn anh. Hậu cảnh là mặt tiền quán cà phê và mái hiên bạt xanh.",
  "RYAN một tay đưa ra định giữ cánh tay VANESSA rồi dừng giữa chừng. VANESSA một tay cầm cốc giấy đã cạn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — người vừa thấy chuyện đi quá xa và chỉ dám nói một câu: mày chau, giọng nhỏ. "
  "VANESSA — không hiểu vì sao phải dừng: mày nhướn, khoé môi cong, giọng nhẹ như đùa.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay RYAN hạ xuống",
  ["RYAN_ADO", "VANESSA_NGAY"], "trên vỉa hè, cách chỗ chiếc xe lăn đổ một bước",
  {"RYAN": "đứng nửa trái khung", "VANESSA": "đứng nửa phải khung"},
  "sát cạnh nhau", {"RYAN": "một tay đưa ra rồi dừng giữa chừng", "VANESSA": "một tay cầm cốc giấy đã cạn"})
V("11", [20, 21], "cận-trung 85mm · RYAN NÉT trái + VANESSA NÉT phải, cả hai đứng trên vỉa hè",
  [("RYAN", "RYAN_ADO"), ("VANESSA", "VANESSA_NGAY")],
  "RYAN và VANESSA, cả hai rõ mặt. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "RYAN đưa tay ra định giữ cánh tay VANESSA rồi dừng lại giữa chừng",
  [("RYAN", "uneasy, quiet", 20), ("VANESSA", "light, unrepentant", 21)])

S("12", "trung 50mm, cao 1m50, cách MAYA 2m, đặt trên vỉa hè lấy cả ba người",
  "MAYA đã đứng dậy và ở nửa PHẢI khung, người quay hẳn về phía VANESSA, một tay còn buông dọc thân. "
  "VANESSA đứng ở nửa TRÁI khung. RYAN đứng lùi sau VANESSA nửa bước, thấy rõ mặt.",
  "MAYA hai tay buông dọc thân, bàn tay phải mở ra. VANESSA một tay còn cầm cốc giấy. RYAN hai tay buông.",
  "MAYA nhìn thẳng vào mặt VANESSA. VANESSA nhìn lại MAYA. RYAN nhìn MAYA.",
  "MAYA — người vừa đứng dậy khỏi chỗ chồng mình nằm và nói ra lý do trước: giọng rất bình, mắt thẳng, "
  "không hề gào. VANESSA — chưa hiểu chuyện gì sắp xảy ra: mày nhướn. RYAN — mắt mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay MAYA rời khỏi thân mình",
  ["MAYA_CARO", "VANESSA_NGAY", "RYAN_ADO"], "trên vỉa hè, cạnh chỗ chiếc xe lăn đổ",
  {"MAYA": "đứng nửa phải khung", "VANESSA": "đứng nửa trái khung", "RYAN": "đứng lùi sau VANESSA nửa bước"},
  "cách nhau một bước", {"MAYA": "hai tay buông dọc thân, bàn tay phải mở ra",
                         "VANESSA": "một tay cầm cốc giấy", "RYAN": "hai tay buông"})
V("12", [22, 23], "trung 50mm · MAYA NÉT phải + VANESSA NÉT trái + RYAN NÉT lùi sau VANESSA",
  [("MAYA", "MAYA_CARO"), ("VANESSA", "VANESSA_NGAY"), ("RYAN", "RYAN_ADO")],
  "MAYA, VANESSA và RYAN, cả ba rõ mặt. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "MAYA đứng dậy, nói một câu rồi tát thẳng vào mặt VANESSA; VANESSA lảo đảo nửa bước",
  [("MAYA", "level, deliberate", 22), ("VANESSA", "shocked, loud", 23)])

S("13", "trung 50mm, cao 1m50, cách RYAN 2m, đặt trên vỉa hè lấy RYAN nét và MAYA trong khung",
  "RYAN đứng ở nửa TRÁI khung, đã bước hẳn tới trước mặt MAYA. MAYA đứng ở nửa PHẢI khung, chưa lùi. "
  "Hậu cảnh là hàng xe đỗ dọc đường và cây phong trong ô đất vuông.",
  "RYAN một tay đã nắm lấy cổ tay MAYA. MAYA một tay bị nắm, tay kia đưa lên gỡ.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — người đang làm điều mình chưa từng nghĩ mình sẽ làm và vẫn làm: quai hàm siết, mắt cứng. "
  "MAYA — không sợ, chỉ nhìn xuống bàn tay đang nắm cổ tay mình: mắt hạ xuống rồi ngước lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN ghì tay MAYA xuống",
  ["RYAN_ADO", "MAYA_CARO"], "trên vỉa hè, cạnh chỗ chiếc xe lăn đổ",
  {"RYAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "sát nhau", {"RYAN": "một tay nắm cổ tay MAYA", "MAYA": "một tay bị nắm, tay kia đưa lên gỡ"})
V("13", [24, 25], "trung 50mm · RYAN NÉT trái nắm cổ tay + MAYA NÉT phải, cả hai đứng trên vỉa hè",
  [("RYAN", "RYAN_ADO"), ("MAYA", "MAYA_CARO")],
  "RYAN và MAYA, cả hai rõ mặt. Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "RYAN nắm lấy cổ tay MAYA, MAYA đưa tay kia lên gỡ ra",
  [("RYAN", "hard, low", 24), ("MAYA", "flat, unafraid", 25)],
  ketclip="Cuối clip, RYAN ghì cổ tay MAYA xuống làm cô khuỵu một gối xuống mặt vỉa hè, ngay cạnh chỗ ADRIAN nằm. "
          "Clip dừng đúng lúc đầu gối cô chạm bê tông.")

S("14", "trung 50mm, cao 0m80, cách MAYA 2m, máy hạ rất thấp ngang mặt vỉa hè lấy cả ba người",
  "MAYA quỳ một gối ở giữa khung, cổ tay còn bị RYAN giữ. RYAN đứng ở nửa TRÁI khung cúi xuống. ADRIAN nằm "
  "nghiêng ở nửa PHẢI khung, cách cô một cánh tay, chiếc xe lăn đổ phía sau anh.",
  "RYAN một tay giữ cổ tay MAYA ghì xuống. MAYA một gối chống xuống vỉa hè, tay kia chống đất. "
  "ADRIAN một tay chống xuống vỉa hè, người nhổm lên một chút.",
  "RYAN nhìn xuống MAYA. MAYA nhìn xuống mặt vỉa hè. ADRIAN nhìn thẳng vào RYAN.",
  "RYAN — người đang tận hưởng việc cả phố nhìn thấy: giọng cao, mắt sáng. "
  "MAYA — không đáp lại một chữ: mặt phẳng. ADRIAN — nhìn kỹ mặt RYAN như đang ghi lại: mắt tĩnh, "
  "quai hàm siết chặt.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN cất tiếng gọi tên hai người",
  ["MAYA_CARO", "RYAN_ADO", "ADRIAN_NHA"], "mặt vỉa hè, MAYA quỳ một gối, ADRIAN nằm nghiêng cạnh đó",
  {"MAYA": "quỳ một gối giữa khung", "RYAN": "đứng cúi xuống nửa trái khung",
   "ADRIAN": "nằm nghiêng nửa phải khung"},
  "ba người trong vòng một mét",
  {"RYAN": "một tay giữ cổ tay MAYA ghì xuống", "MAYA": "một tay chống đất, một tay bị giữ",
   "ADRIAN": "một tay chống xuống vỉa hè"})
V("14", [26, 27], "trung 50mm hạ rất thấp · MAYA NÉT giữa quỳ một gối + RYAN NÉT trái cúi xuống + ADRIAN NÉT phải nằm nghiêng",
  [("MAYA", "MAYA_CARO"), ("RYAN", "RYAN_ADO"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA, RYAN và ADRIAN, cả ba rõ mặt. ADRIAN nằm nghiêng trên vỉa hè cạnh chiếc xe lăn đổ. "
  "Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "RYAN ghì cổ tay MAYA xuống, ADRIAN nhổm người lên trên khuỷu tay và nói ra hai cái tên",
  [("RYAN", "raised, triumphant", 26), ("ADRIAN", "quiet, level", 27)])

S("15", "cận-trung 85mm, cao 0m90, cách VANESSA 1m6, máy hạ thấp nhìn hơi chếch lên phía VANESSA đứng",
  "VANESSA đứng chiếm phần lớn khung, nhìn xuống. Ở rìa DƯỚI khung thấy vai và một phần đầu của ADRIAN đang "
  "nằm nghiêng trên vỉa hè, out nét.",
  "VANESSA một tay chống hông, tay kia buông cốc giấy đã cạn xuống cạnh đùi.",
  "VANESSA nhìn xuống mặt ADRIAN.",
  "VANESSA — người thấy một người nằm dưới đất ra lệnh và cho đó là chuyện hài nhất năm: mày nhướn, "
  "khoé môi kéo rộng, giọng nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN trả lời cô",
  ["VANESSA_NGAY", "ADRIAN_NHA"], "trên vỉa hè, VANESSA đứng phía trên ADRIAN nằm",
  {"VANESSA": "đứng chính diện giữa khung", "ADRIAN": "vai và một phần đầu ở rìa dưới khung"},
  "cách nhau một bước", {"VANESSA": "một tay chống hông, tay kia buông cốc giấy",
                         "ADRIAN": "nằm nghiêng, ngoài vùng nét"})
V("15", [28, 29], "cận-trung 85mm hạ thấp · VANESSA NÉT chính diện · vai và một phần đầu ADRIAN rìa dưới khung out nét",
  [("VANESSA", "VANESSA_NGAY"), ("ADRIAN", "ADRIAN_NHA")],
  "VANESSA rõ mặt. ADRIAN chỉ thấy VAI và MỘT PHẦN ĐẦU ở rìa dưới khung, out nét — KHÔNG quay mặt về camera.",
  "VANESSA nhìn xuống người đang nằm dưới vỉa hè và bật cười",
  [("VANESSA", "amused, mocking", 28), ("ADRIAN", "quiet, precise", 29)])

S("16", "trung 50mm, cao 0m80, cách ADRIAN 2m, máy hạ rất thấp ngang mặt vỉa hè lấy cả ba người",
  "ADRIAN nằm nghiêng chống trên một khuỷu tay ở nửa PHẢI khung. MAYA quỳ một gối ở giữa khung, cổ tay đã được "
  "buông ra. VANESSA đứng ở nửa TRÁI khung phía trên, đang cười.",
  "ADRIAN một tay chống xuống vỉa hè, tay kia đưa về phía MAYA. MAYA hai tay chống xuống mặt vỉa hè. "
  "VANESSA một tay chống hông.",
  "ADRIAN nhìn thẳng vào MAYA. MAYA nhìn ADRIAN. VANESSA nhìn xuống cả hai người.",
  "ADRIAN — người ra lệnh cho vợ mình đứng dậy trước khi lo cho bản thân: giọng rõ, mắt thẳng. "
  "MAYA — nghe lệnh đó và làm theo: quai hàm siết, mắt ướt. VANESSA — vẫn đang cười: khoé môi kéo rộng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA chống tay đứng thẳng dậy",
  ["ADRIAN_NHA", "MAYA_CARO", "VANESSA_NGAY"], "mặt vỉa hè, ADRIAN nằm nghiêng, MAYA quỳ một gối",
  {"ADRIAN": "nằm nghiêng chống khuỷu tay nửa phải khung", "MAYA": "quỳ một gối giữa khung",
   "VANESSA": "đứng phía trên nửa trái khung"},
  "ba người trong vòng một mét rưỡi",
  {"ADRIAN": "một tay chống vỉa hè, tay kia đưa về phía MAYA", "MAYA": "hai tay chống xuống mặt vỉa hè",
   "VANESSA": "một tay chống hông"})
V("16", [30, 31], "trung 50mm hạ rất thấp · ADRIAN NÉT phải nằm nghiêng + MAYA NÉT giữa quỳ một gối + VANESSA NÉT trái đứng phía trên",
  [("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_CARO"), ("VANESSA", "VANESSA_NGAY")],
  "ADRIAN, MAYA và VANESSA, cả ba rõ mặt. ADRIAN nằm nghiêng chống trên một khuỷu tay. "
  "Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA cười xuống phía hai người đang nằm và quỳ dưới vỉa hè",
  [("VANESSA", "gleeful, mocking", 30)],
  [("ADRIAN", "silent, pushing up onto his elbow"), ("MAYA", "silent, on one knee")])

S("16b", "cận-trung 85mm, cao 0m70, cách ADRIAN 1m4, máy hạ rất thấp ngang mặt vỉa hè",
  "ADRIAN nằm nghiêng chống trên một khuỷu tay chiếm phần lớn khung. MAYA quỳ một gối ở nửa PHẢI khung, "
  "đã quay hẳn mặt về phía anh. Ở rìa TRÁI khung thấy một phần chân và tà áo khoác của VANESSA, out nét.",
  "ADRIAN một tay chống xuống vỉa hè, tay kia đưa về phía MAYA. MAYA hai tay chống xuống mặt vỉa hè.",
  "ADRIAN nhìn thẳng vào MAYA. MAYA nhìn ADRIAN.",
  "ADRIAN — người ra lệnh cho vợ mình đứng dậy trước khi lo cho bản thân: giọng rõ, mắt thẳng. "
  "MAYA — nghe lệnh đó và làm theo: quai hàm siết, mắt ướt.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA chống tay đứng thẳng dậy",
  ["ADRIAN_NHA", "MAYA_CARO", "VANESSA_NGAY"], "mặt vỉa hè, ADRIAN nằm nghiêng, MAYA quỳ một gối",
  {"ADRIAN": "nằm nghiêng chống khuỷu tay giữa khung", "MAYA": "quỳ một gối nửa phải khung",
   "VANESSA": "một phần chân và tà áo khoác ở rìa trái khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay chống vỉa hè, tay kia đưa về phía MAYA",
                    "MAYA": "hai tay chống xuống mặt vỉa hè", "VANESSA": "đứng phía trên, ngoài vùng nét"})
VX("16b", "cận-trung 85mm hạ rất thấp · ADRIAN NÉT nằm nghiêng chống khuỷu tay + MAYA NÉT phải quỳ một gối · "
          "chân và tà áo VANESSA rìa trái out nét",
   [("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_CARO"), ("VANESSA", "VANESSA_NGAY")],
   "ADRIAN và MAYA rõ mặt. VANESSA chỉ thấy CHÂN và tà áo khoác ở rìa trái, out nét — KHÔNG thấy mặt.",
   "ADRIAN chống người lên khuỷu tay và đưa một tay về phía MAYA",
   [("ADRIAN", "firm, commanding", "Maya. Get up. Do not let them see you on the ground.")],
   [("MAYA", "silent, gathering herself")],
   ketclip="Cuối clip, MAYA đứng thẳng dậy, dựng chiếc xe lăn lên, đỡ ADRIAN ngồi lại vào ghế. "
           "Clip dừng đúng lúc anh ngồi vững trong xe.")

S("17", "cận-trung 85mm, cao 1m30, cách MAYA 1m7, đặt phía sau chiếc xe lăn, hạ thấp ngang tầm người ngồi",
  "MAYA đứng ở nửa PHẢI khung phía sau chiếc xe lăn đã dựng lại, hai tay trên tay đẩy. ADRIAN ngồi lại trong "
  "xe lăn ở nửa TRÁI khung, quần áo có một vệt cà phê sẫm ở đùi. Hậu cảnh là vỉa hè và hàng cây phong.",
  "MAYA hai tay nắm chặt tay đẩy xe lăn, các khớp ngón trắng. ADRIAN một tay đặt lên bàn tay MAYA trên tay đẩy.",
  "MAYA nhìn xuống ADRIAN. ADRIAN nhìn thẳng phía trước, không quay lại nhìn hai người kia.",
  "MAYA — người vừa đứng dậy được và đang run: mắt đỏ, hơi thở gấp, giọng cố giữ bình. "
  "ADRIAN — người biết đúng thứ cần nói lúc này và nói rất ngắn: giọng đều, mắt thẳng về phía trước.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đẩy chiếc xe lăn đi khỏi",
  ["MAYA_CARO", "ADRIAN_NHA"], "trên vỉa hè, chiếc xe lăn đã dựng lại",
  {"MAYA": "đứng sau xe lăn nửa phải khung", "ADRIAN": "ngồi lại trong xe lăn nửa trái khung"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay nắm chặt tay đẩy xe lăn",
                          "ADRIAN": "một tay đặt lên bàn tay MAYA trên tay đẩy"})
V("17", [32, 33], "cận-trung 85mm hạ thấp · MAYA NÉT phải đứng sau xe lăn + ADRIAN NÉT trái ngồi lại trong xe",
  [("MAYA", "MAYA_CARO"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN đã ngồi lại trong chiếc xe lăn. "
  "Người qua đường mờ ở hậu cảnh, không ai nhìn vào camera.",
  "ADRIAN đặt bàn tay lên bàn tay MAYA trên tay đẩy xe và nói mà không quay đầu lại",
  [("MAYA", "shaking, holding on", 32), ("ADRIAN", "steady, quiet", 33)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 9m, đặt trên vỉa hè nhìn theo hướng hai người đi khỏi",
  "MAYA đẩy chiếc xe lăn có ADRIAN ngồi đi xa dần dọc vỉa hè, quay lưng lại phía máy quay. Trên mặt bê tông "
  "phía tiền cảnh còn một VŨNG CÀ PHÊ SẪM và một chiếc cốc giấy nằm nghiêng. Không còn ai khác trong khung.",
  "MAYA hai tay đẩy xe lăn, người hơi đổ về trước. ADRIAN hai tay đặt trên vành tay vịn.",
  "Cả hai nhìn thẳng về phía trước, KHÔNG ai quay đầu lại.",
  "MAYA — người vừa bị ghì xuống vỉa hè và đang đẩy chồng mình đi tiếp: vai cân lại được, bước đều. "
  "ADRIAN — không quay đầu lại một lần nào: lưng thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai người khuất sau góc phố",
  ["MAYA_CARO", "ADRIAN_NHA"], "vỉa hè trước quán cà phê, hướng đi khỏi",
  {"MAYA": "đẩy xe lăn đi xa dần, quay lưng lại", "ADRIAN": "ngồi trong xe lăn, quay lưng lại"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay đẩy xe lăn", "ADRIAN": "hai tay trên vành tay vịn"})
B("B2", "Khép cảnh. MAYA đẩy ADRIAN đi khỏi, cả hai quay lưng lại; trên vỉa hè còn vũng cà phê và chiếc cốc giấy.",
  "toàn cảnh 24mm · MAYA và ADRIAN QUAY LƯNG đi xa dần dọc vỉa hè · vũng cà phê ở tiền cảnh · không có ai khác",
  [("MAYA", "MAYA_CARO"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN chỉ thấy TỪ PHÍA SAU, cả hai QUAY LƯNG lại và đi xa dần — TUYỆT ĐỐI KHÔNG ai quay mặt lại "
  "về camera. Không có người nào khác trong khung.",
  "hai người vừa bị làm nhục giữa ban ngày trước mặt cả một khu phố, và việc duy nhất họ làm là đi tiếp; "
  "vết cà phê trên vỉa hè ở lại thay cho họ.",
  "MAYA đẩy xe đi đều, không quay đầu; một chiếc xe chạy qua phía lòng đường; vũng cà phê trên bê tông loang "
  "rộng thêm một chút rồi ngấm xuống; chiếc cốc giấy lăn nửa vòng theo gió.",
  "Ambient tiếng phố ban ngày và tiếng xe chạy, SFX tiếng bánh xe lăn trên vỉa hè bê tông xa dần.",
  nhac("KÌM", "Không được phép cho khán giả một cú giải toả ở đây — nhạc phải nén để cơn giận dồn sang cảnh sau.",
       "Soul ballad at 64 BPM with a female alto very close to the mic, dry and worn, half-spoken; Rhodes and upright "
       "bass only, brushed drums entering once at the end; one restrained string swell at the peak then straight back "
       "to voice; lyrics about walking away down a street where everybody watched and nobody moved; "
       "warm analog mix, female vocal, soul, restrained, dusty",
       "Instrumental at 62 BPM; Rhodes playing a slow four-chord figure, upright bass entering on the second pass, "
       "one muted trumpet note held long at the midpoint then gone, no drums, ending on the Rhodes alone; "
       "warm analog mix, Rhodes, upright bass, trumpet, restrained"),
  dur=10)
