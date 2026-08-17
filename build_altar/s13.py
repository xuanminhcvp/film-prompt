# -*- coding: utf-8 -*-
"""SCENE 13 — PHÒNG CHỈ HUY KANE HOLDINGS (đêm). Bốn giây."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S13", "REF_CHIHUY_DEM", qc=qc.S13)

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách ADRIAN 8m, đặt ở đầu phòng phía cửa nhìn dọc bàn họp về bức tường màn hình",
  "ADRIAN ngồi trong xe lăn ở đầu bàn họp phía bức tường mười tám màn hình đang phát. BOARD MEMBER ONE và "
  "BOARD MEMBER TWO ngồi trên hai ghế xoay da đen gần đó, SEBASTIAN đứng sau lưng chiếc xe lăn. "
  "Các ghế xoay còn lại dọc bàn đều trống.",
  "ADRIAN hai tay đặt trên vành tay vịn. BOARD MEMBER ONE hai tay cầm một máy tính bảng màn hình tối. "
  "BOARD MEMBER TWO hai tay đặt trên một tập tài liệu bìa cứng. SEBASTIAN một tay giữ bìa kẹp hồ sơ da nâu.",
  "Cả ba người kia đều nhìn về phía ADRIAN. ADRIAN nhìn thẳng lên bức tường màn hình.",
  "ADRIAN — người ngồi ở chỗ của người ra lệnh và không cần nói to: mặt hoàn toàn bình, mắt tĩnh. "
  "BOARD MEMBER ONE và BOARD MEMBER TWO — chờ lệnh: lưng thẳng, mắt tập trung. SEBASTIAN — kín, chờ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN cất tiếng đầu tiên",
  ["ADRIAN_VESTNGOI", "BOARD MEMBER ONE", "BOARD MEMBER TWO", "SEBASTIAN"],
  "đầu bàn họp, trước bức tường màn hình",
  {"ADRIAN": "ngồi xe lăn ở đầu bàn", "BOARD MEMBER ONE": "ngồi ghế xoay gần đầu bàn",
   "BOARD MEMBER TWO": "ngồi ghế xoay đối diện", "SEBASTIAN": "đứng sau lưng chiếc xe lăn"},
  "cả bốn người trong vòng ba mét",
  {"ADRIAN": "hai tay trên vành tay vịn", "BOARD MEMBER ONE": "hai tay cầm máy tính bảng",
   "BOARD MEMBER TWO": "hai tay đặt trên tập tài liệu", "SEBASTIAN": "một tay giữ bìa kẹp hồ sơ"})
B("B1", "Mở cảnh. Phòng chỉ huy Kane Holdings. ADRIAN ngồi ở đầu bàn trước bức tường mười tám màn hình, ba người chờ lệnh.",
  "toàn cảnh 24mm · ADRIAN NÉT ngồi xe lăn ở đầu bàn + SEBASTIAN NÉT đứng sau lưng + BOARD MEMBER ONE NÉT và "
  "BOARD MEMBER TWO NÉT ngồi hai bên",
  [("ADRIAN", "ADRIAN_VESTNGOI"), ("SEBASTIAN", "SEBASTIAN"),
   ("BOARD MEMBER ONE", "BOARD MEMBER ONE"), ("BOARD MEMBER TWO", "BOARD MEMBER TWO")],
  "ADRIAN, SEBASTIAN, BOARD MEMBER ONE và BOARD MEMBER TWO rõ mặt. Không có ai khác trong phòng.",
  "cả bộ phim tới đây vẫn tin người đàn ông này là kẻ bị gia đình vứt ra nhà cổng; khung hình này nói ngược lại "
  "mà không cần một lời nào.",
  "bức tường mười tám màn hình đổi dữ liệu một lượt, ánh xanh quét ngang mặt bàn; BOARD MEMBER ONE gõ hai lần "
  "lên máy tính bảng; SEBASTIAN chỉnh lại gọng kính; ADRIAN không nhúc nhích.",
  "Ambient tiếng ù rất khẽ của dàn màn hình và điều hoà, SFX tiếng ghế xoay dịch nhẹ trên thảm.",
  nhac("NÂNG", "Đây là mốc lật danh tính của nhân vật chính — nhạc phải dựng lên và rút về mộc, không được reo mừng.",
       "Cinematic soul at 82 BPM; low strings and a slow kick building from silence, a female alto entering after "
       "eight seconds with two low lines close to the mic; the pull is when everything drops away except one held "
       "string note; lyrics about a man everyone has already written off sitting at the head of the table; "
       "warm analog mix, female vocal, strings, cinematic, controlled",
       "Cinematic instrumental at 80 BPM; low strings rising under a slow heartbeat kick, a single French horn "
       "entering at the midpoint, everything cutting away to one sustained cello note at the end; "
       "warm analog mix, strings, horn, cello, cinematic, controlled"),
  dur=8)

# ── BÁO CÁO ──
S("01", "trung 50mm, cao 1m30, cách ADRIAN 2m4, đặt bên bàn họp, hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung ở đầu bàn. BOARD MEMBER ONE ngồi ở nửa TRÁI khung trên ghế xoay, "
  "người hơi nghiêng về phía ADRIAN. Hậu cảnh là bức tường màn hình đang phát sáng xanh.",
  "BOARD MEMBER ONE một tay cầm máy tính bảng, tay kia chỉ về phía bức tường màn hình. "
  "ADRIAN hai tay đặt trên vành tay vịn.",
  "BOARD MEMBER ONE nhìn ADRIAN. ADRIAN nhìn thẳng lên bức tường màn hình.",
  "BOARD MEMBER ONE — người báo cáo gọn và chờ: giọng đều, lưng thẳng. "
  "ADRIAN — ra lệnh bằng một chữ: mặt bình, mắt không rời màn hình.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng lật một tập tài liệu ở phía bên kia bàn",
  ["ADRIAN_VESTNGOI", "BOARD MEMBER ONE"], "đầu bàn họp, trước bức tường màn hình",
  {"ADRIAN": "ngồi xe lăn nửa phải khung", "BOARD MEMBER ONE": "ngồi ghế xoay nửa trái khung"},
  "cách nhau hai mét", {"BOARD MEMBER ONE": "một tay cầm máy tính bảng, tay kia chỉ về màn hình",
                        "ADRIAN": "hai tay trên vành tay vịn"})
V("01", [0, 1], "trung 50mm hạ thấp · BOARD MEMBER ONE NÉT trái ngồi ghế xoay + ADRIAN NÉT phải ngồi xe lăn",
  [("BOARD MEMBER ONE", "BOARD MEMBER ONE"), ("ADRIAN", "ADRIAN_VESTNGOI")],
  "BOARD MEMBER ONE và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "BOARD MEMBER ONE chỉ về phía bức tường màn hình và báo cáo",
  [("BOARD MEMBER ONE", "crisp, reporting", 0), ("ADRIAN", "flat, commanding", 1)])

S("02", "trung 50mm, cao 1m30, cách ADRIAN 2m4, đặt bên bàn họp phía đối diện, hạ thấp ngang tầm người ngồi",
  "BOARD MEMBER TWO ngồi ở nửa TRÁI khung trên ghế xoay, tập tài liệu bìa cứng đã mở trên bàn trước mặt. "
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung. Hậu cảnh là tường ốp gỗ veneer tối màu có nẹp LED chân tường.",
  "BOARD MEMBER TWO một tay lần theo một dòng trong tập tài liệu, tay kia đặt trên mép bàn. "
  "ADRIAN một tay đặt trên vành tay vịn, tay kia hơi nhấc lên.",
  "BOARD MEMBER TWO nhìn xuống tài liệu rồi ngước lên nhìn ADRIAN. ADRIAN nhìn BOARD MEMBER TWO.",
  "BOARD MEMBER TWO — người thuộc số liệu tới hàng triệu: giọng nhanh, rõ, mắt sắc. "
  "ADRIAN — chặn lại bằng hai chữ: mặt bình, giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng người lên tiếng cãi lại từ phía bên kia bàn",
  ["ADRIAN_VESTNGOI", "BOARD MEMBER TWO"], "đầu bàn họp",
  {"BOARD MEMBER TWO": "ngồi ghế xoay nửa trái khung", "ADRIAN": "ngồi xe lăn nửa phải khung"},
  "cách nhau hai mét", {"BOARD MEMBER TWO": "một tay lần theo dòng tài liệu, tay kia trên mép bàn",
                        "ADRIAN": "một tay trên vành tay vịn, tay kia hơi nhấc lên"})
V("02", [2, 3], "trung 50mm hạ thấp · BOARD MEMBER TWO NÉT trái ngồi ghế xoay + ADRIAN NÉT phải ngồi xe lăn",
  [("BOARD MEMBER TWO", "BOARD MEMBER TWO"), ("ADRIAN", "ADRIAN_VESTNGOI")],
  "BOARD MEMBER TWO và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "BOARD MEMBER TWO lần ngón tay theo một dòng trong tập tài liệu và đọc lên",
  [("BOARD MEMBER TWO", "quick, precise", 2), ("ADRIAN", "quiet, checking", 3)])

S("03", "OTS cận-trung 85mm, cao 1m40, cách ADRIAN 1m7, máy sau vai TRÁI của BOARD MEMBER ONE; vai và gáy anh chiếm rìa trái, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung, thấy rõ mặt. BOARD MEMBER ONE chỉ còn là vai và gáy ở rìa TRÁI "
  "tiền cảnh, người nghiêng tới trước, ngoài vùng nét. Hậu cảnh là bức tường màn hình sáng xanh.",
  "BOARD MEMBER ONE một tay đặt máy tính bảng xuống bàn, tay kia mở ra kiểu trình bày. "
  "ADRIAN hai tay đặt trên vành tay vịn.",
  "BOARD MEMBER ONE nhìn thẳng vào ADRIAN. ADRIAN nhìn lại.",
  "BOARD MEMBER ONE — người trung thành đủ để dám cãi sếp một câu: giọng nhanh, mắt thẳng, lễ độ. "
  "ADRIAN — nghe hết, không ngắt: mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bắt đầu trả lời",
  ["BOARD MEMBER ONE", "ADRIAN_VESTNGOI"], "đầu bàn họp",
  {"BOARD MEMBER ONE": "vai và gáy tiền cảnh trái", "ADRIAN": "ngồi xe lăn giữa khung"},
  "cách nhau hai mét", {"BOARD MEMBER ONE": "một tay đặt máy tính bảng xuống bàn, tay kia mở ra",
                        "ADRIAN": "hai tay trên vành tay vịn"})
V("03", [4], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy BOARD MEMBER ONE tiền cảnh trái out nét",
  [("BOARD MEMBER ONE", "BOARD MEMBER ONE"), ("ADRIAN", "ADRIAN_VESTNGOI")],
  "ADRIAN rõ mặt ngồi trong xe lăn. BOARD MEMBER ONE chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "BOARD MEMBER ONE đặt máy tính bảng xuống bàn và nghiêng người tới trước",
  [("BOARD MEMBER ONE", "urgent, respectful", 4)], [("ADRIAN", "silent, listening")])

S("04", "cận 85mm, cao 1m30, cách ADRIAN 1m3, đặt chính diện trước chiếc xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung từ ngực trở lên ở nửa PHẢI khung. BOARD MEMBER TWO ngồi trên "
  "ghế xoay ở rìa TRÁI khung, thấy rõ mặt, người quay về phía anh. Hậu cảnh là bức tường mười tám màn hình sáng xanh.",
  "ADRIAN một tay gõ một nhịp lên vành tay vịn rồi dừng, các ngón khép lại.",
  "ADRIAN nhìn thẳng lên bức tường màn hình phía trước.",
  "ADRIAN — người đã hình dung sẵn căn phòng nơi chuyện này sẽ xảy ra và đang mô tả nó: giọng đều, chậm, "
  "mắt tĩnh, KHÔNG hằn học.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người bước tới cạnh chiếc xe lăn",
  ["ADRIAN_VESTNGOI", "BOARD MEMBER TWO"], "đầu bàn họp, trước bức tường màn hình",
  {"ADRIAN": "ngồi xe lăn nửa phải khung", "BOARD MEMBER TWO": "ngồi ghế xoay rìa trái khung"},
  "cách nhau hai mét", {"ADRIAN": "một tay gõ một nhịp lên vành tay vịn rồi dừng",
                        "BOARD MEMBER TWO": "hai tay đặt trên tập tài liệu mở"})
V("04", [5, 6], "cận 85mm hạ thấp · ADRIAN NÉT phải ngồi xe lăn + BOARD MEMBER TWO NÉT rìa trái ngồi ghế xoay",
  [("ADRIAN", "ADRIAN_VESTNGOI"), ("BOARD MEMBER TWO", "BOARD MEMBER TWO")],
  "ADRIAN và BOARD MEMBER TWO, cả hai rõ mặt. Không có ai khác trong khung.",
  "ADRIAN gõ một nhịp lên vành tay vịn rồi dừng lại và nói",
  [("ADRIAN", "even, deliberate", 5), ("BOARD MEMBER TWO", "clipped, obedient", 6)])

S("05", "trung 50mm, cao 1m30, cách ADRIAN 2m2, đặt bên chiếc xe lăn, hạ thấp ngang tầm người ngồi",
  "SEBASTIAN đứng ở nửa TRÁI khung ngay cạnh chiếc xe lăn, bìa kẹp hồ sơ da nâu đã mở trên cẳng tay. "
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung. Hậu cảnh là bàn họp dài và các ghế xoay da đen.",
  "SEBASTIAN một tay đỡ bìa kẹp hồ sơ đã mở, tay kia lần theo một dòng trong đó. "
  "ADRIAN một tay hơi nhấc lên khỏi vành tay vịn ra hiệu đọc tiếp.",
  "SEBASTIAN nhìn xuống ADRIAN. ADRIAN nhìn thẳng phía trước.",
  "SEBASTIAN — người mang tới thứ mà mình biết sẽ làm mọi thứ đổi hướng: giọng gọn, mắt cứng. "
  "ADRIAN — ra hiệu đọc tiếp bằng hai chữ: mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN bắt đầu đọc nội dung đơn",
  ["SEBASTIAN", "ADRIAN_VESTNGOI"], "cạnh chiếc xe lăn ở đầu bàn họp",
  {"SEBASTIAN": "đứng cạnh xe lăn nửa trái khung", "ADRIAN": "ngồi xe lăn nửa phải khung"},
  "sát cạnh nhau", {"SEBASTIAN": "một tay đỡ bìa hồ sơ mở, tay kia lần theo một dòng",
                    "ADRIAN": "một tay nhấc lên ra hiệu đọc tiếp"})
V("05", [7, 8], "trung 50mm hạ thấp · SEBASTIAN NÉT trái đứng cạnh xe lăn + ADRIAN NÉT phải ngồi xe lăn",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_VESTNGOI")],
  "SEBASTIAN và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "SEBASTIAN mở bìa kẹp hồ sơ và lần ngón tay theo một dòng, ADRIAN nhấc tay ra hiệu",
  [("SEBASTIAN", "crisp, grave", 7), ("ADRIAN", "flat, commanding", 8)])

S("06", "cận-trung 85mm, cao 1m40, cách SEBASTIAN 1m6, đặt cạnh chiếc xe lăn lấy SEBASTIAN nét và ADRIAN trong khung",
  "SEBASTIAN đứng ở nửa TRÁI khung, đọc từ bìa kẹp hồ sơ. ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, thấy rõ mặt, "
  "đầu hơi ngẩng lên. Hậu cảnh là bức tường màn hình sáng xanh.",
  "SEBASTIAN hai tay giữ bìa kẹp hồ sơ ngang ngực. ADRIAN hai tay đặt trên vành tay vịn, các ngón siết lại.",
  "SEBASTIAN nhìn xuống trang hồ sơ. ADRIAN nhìn thẳng lên SEBASTIAN.",
  "SEBASTIAN — đọc nguyên văn, không thêm bình luận: giọng đều, mắt trên trang giấy. "
  "ADRIAN — nghe tên người anh họ mình trong một lá đơn: quai hàm siết một nhịp, mặt vẫn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN nhắc lại hai chữ cuối cùng",
  ["SEBASTIAN", "ADRIAN_VESTNGOI"], "cạnh chiếc xe lăn ở đầu bàn họp",
  {"SEBASTIAN": "đứng cạnh xe lăn nửa trái khung", "ADRIAN": "ngồi xe lăn nửa phải khung"},
  "sát cạnh nhau", {"SEBASTIAN": "hai tay giữ bìa kẹp hồ sơ ngang ngực",
                    "ADRIAN": "hai tay siết vành tay vịn"})
V("06", [9, 10], "cận-trung 85mm · SEBASTIAN NÉT trái đọc hồ sơ + ADRIAN NÉT phải ngồi xe lăn",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_VESTNGOI")],
  "SEBASTIAN và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "SEBASTIAN giữ bìa hồ sơ ngang ngực và đọc nguyên văn lá đơn",
  [("SEBASTIAN", "even, grave", 9), ("ADRIAN", "quiet, repeating", 10)])

S("07", "trung 50mm, cao 1m30, cách ADRIAN 2m2, đặt bên bàn họp, hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung. SEBASTIAN đứng ở nửa TRÁI khung cạnh anh. Phía sau hai người, "
  "hai chiếc ghế xoay da đen đã trống và đẩy lệch ra, BOARD MEMBER ONE và BOARD MEMBER TWO đang đi ra cửa, "
  "chỉ thấy lưng, mờ ngoài vùng nét.",
  "SEBASTIAN một tay gập bìa kẹp hồ sơ lại. ADRIAN một tay hất nhẹ về phía cửa cuối phòng.",
  "ADRIAN nhìn thẳng phía trước. SEBASTIAN nhìn xuống ADRIAN. Hai người kia quay lưng đi ra, không nhìn lại.",
  "ADRIAN — người dọn phòng bằng một câu và giữ lại đúng một người: giọng đều, dứt khoát. "
  "SEBASTIAN — hiểu ngay điều sắp xảy ra và không thích nó: mày chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi cánh cửa cuối phòng khép lại",
  ["ADRIAN_VESTNGOI", "SEBASTIAN", "BOARD MEMBER ONE", "BOARD MEMBER TWO"], "đầu bàn họp",
  {"ADRIAN": "ngồi xe lăn nửa phải khung", "SEBASTIAN": "đứng cạnh xe lăn nửa trái khung",
   "BOARD MEMBER ONE": "đang đi ra cửa, chỉ thấy lưng, mờ",
   "BOARD MEMBER TWO": "đang đi ra cửa, chỉ thấy lưng, mờ"},
  "hai người kia cách sáu mét",
  {"ADRIAN": "một tay hất nhẹ về phía cửa", "SEBASTIAN": "một tay gập bìa kẹp hồ sơ",
   "BOARD MEMBER ONE": "quay lưng, tay cầm máy tính bảng", "BOARD MEMBER TWO": "quay lưng, tay ôm tập tài liệu"},
  qc="Ở nền sau, đội trực đêm đang đứng dậy rời khỏi hai dãy bàn điều hành: hai người vừa đẩy ghế ra sau, "
     "một người cầm áo khoác bước về phía cửa. TUYỆT ĐỐI không ai trong số họ nhìn vào ống kính.")
V("07", [11, 12], "trung 50mm hạ thấp · SEBASTIAN NÉT trái đứng cạnh xe lăn + ADRIAN NÉT phải ngồi xe lăn · "
                  "BOARD MEMBER ONE và BOARD MEMBER TWO chỉ thấy lưng, mờ, đang đi ra cửa",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_VESTNGOI"),
   ("BOARD MEMBER ONE", "BOARD MEMBER ONE"), ("BOARD MEMBER TWO", "BOARD MEMBER TWO")],
  "SEBASTIAN và ADRIAN rõ mặt. Hai thành viên hội đồng chỉ thấy LƯNG, mờ, đang đi ra cửa.",
  "SEBASTIAN gập bìa kẹp hồ sơ, ADRIAN hất tay về phía cửa cho hai người kia ra ngoài",
  [("SEBASTIAN", "grave, warning", 11), ("ADRIAN", "firm, commanding", 12)],
  ketclip="Cuối clip, hai người kia đi khuất qua cửa và cánh cửa khép lại; trong phòng chỉ còn ADRIAN và SEBASTIAN. "
          "Clip dừng đúng lúc cửa đóng hẳn.",
   qcv="Phía sau, đội trực đêm đang đứng dậy rời bàn đi về phía cửa,")

# ── BỐN GIÂY ──
S("08", "trung 50mm, cao 1m20, cách ADRIAN 2m, máy hạ thấp ngang tầm người ngồi, lấy cả bục thép có tay vịn",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, xe đã được đẩy tới sát BỤC THÉP MỜ THẤP CÓ TAY VỊN NGANG trước "
  "bức tường màn hình. SEBASTIAN đứng ở nửa TRÁI khung, cạnh bục.",
  "ADRIAN hai tay đặt trên vành tay vịn xe lăn, chưa chạm vào tay vịn thép. SEBASTIAN một tay đặt lên thanh "
  "tay vịn thép, tay kia đưa ra phía ADRIAN.",
  "ADRIAN nhìn thanh tay vịn thép trước mặt. SEBASTIAN nhìn ADRIAN.",
  "ADRIAN — người sắp thử một việc mà bác sĩ cấm và đã quyết từ trước: mặt bình, quai hàm siết, "
  "hơi thở sâu hơn. SEBASTIAN — can một câu vì bổn phận chứ không vì hy vọng: mày chau, giọng thấp.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai bàn tay ADRIAN rời khỏi vành tay vịn xe lăn",
  ["ADRIAN_VESTNGOI", "SEBASTIAN"], "trước bục thép có tay vịn, cạnh bức tường màn hình",
  {"ADRIAN": "ngồi xe lăn sát bục thép, nửa phải khung", "SEBASTIAN": "đứng cạnh bục nửa trái khung"},
  "sát cạnh nhau", {"ADRIAN": "hai tay còn trên vành tay vịn xe lăn",
                    "SEBASTIAN": "một tay đặt lên thanh tay vịn thép, tay kia đưa ra phía ADRIAN"}, qc="")
V("08", [13, 14], "trung 50mm hạ thấp · SEBASTIAN NÉT trái đứng cạnh bục thép + ADRIAN NÉT phải ngồi xe lăn sát bục",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_VESTNGOI")],
  "SEBASTIAN và ADRIAN, cả hai rõ mặt. ADRIAN VẪN NGỒI TRONG XE LĂN suốt clip, không đứng lên. "
  "Không có ai khác trong phòng.",
  "SEBASTIAN đặt một tay lên thanh tay vịn thép và can lại, ADRIAN nhìn thanh tay vịn",
  [("SEBASTIAN", "low, pleading", 13), ("ADRIAN", "flat, commanding", 14)], qcv="")

S("09", "cận-trung 85mm, cao 1m10, cách ADRIAN 1m5, máy hạ thấp ngang tầm người ngồi, lấy cả hai bàn tay trên tay vịn thép",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, HAI BÀN TAY ĐÃ BÁM VÀO THANH TAY VỊN THÉP trước mặt, người đổ "
  "về phía trước, VẪN CÒN NGỒI. SEBASTIAN đứng ở nửa TRÁI khung, hai tay giữ lấy thanh tay vịn cho chắc.",
  "ADRIAN hai tay bám chặt thanh tay vịn thép, các khớp ngón trắng ra. SEBASTIAN hai tay ghì thanh tay vịn "
  "xuống cho khỏi xê dịch.",
  "ADRIAN nhìn xuống hai bàn chân mình. SEBASTIAN nhìn ADRIAN.",
  "ADRIAN — người đang dồn toàn bộ ý chí vào hai cánh tay: quai hàm siết, gân cổ nổi, mắt tập trung tuyệt đối. "
  "SEBASTIAN — biết mình không cản được nữa: mặt căng, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN kéo người nhấc khỏi mặt ghế",
  ["ADRIAN_VESTNGOI", "SEBASTIAN"], "trước bục thép có tay vịn",
  {"ADRIAN": "ngồi xe lăn, hai tay đã bám thanh tay vịn thép, nửa phải khung",
   "SEBASTIAN": "đứng ghì thanh tay vịn, nửa trái khung"},
  "sát cạnh nhau", {"ADRIAN": "hai tay bám chặt thanh tay vịn thép",
                    "SEBASTIAN": "hai tay ghì thanh tay vịn xuống"}, qc="")
V("09", [15, 16, 17], "cận-trung 85mm hạ thấp · ADRIAN NÉT phải hai tay bám tay vịn thép + SEBASTIAN NÉT trái ghì thanh tay vịn",
  [("ADRIAN", "ADRIAN_VESTNGOI"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN và SEBASTIAN, cả hai rõ mặt. ADRIAN bám hai tay vào thanh tay vịn thép và tự kéo người lên, "
  "SEBASTIAN ghì thanh tay vịn cho chắc. Không có ai khác trong phòng.",
  "ADRIAN bám hai tay vào thanh tay vịn thép và dồn sức kéo người lên khỏi mặt ghế, SEBASTIAN đếm thành tiếng",
  [("ADRIAN", "strained, low", 15), ("SEBASTIAN", "tight, resisting", 16),
   ("ADRIAN", "strained, insistent", 17)],
  ketclip="Cuối clip, ADRIAN đứng được lên khỏi ghế trong vài giây rồi khuỵu xuống ngồi lại vào xe lăn, "
          "SEBASTIAN đỡ vai anh. Clip dừng đúng lúc anh ngồi lại vững.", qcv="")

S("10", "cận-trung 85mm, cao 1m10, cách ADRIAN 1m4, máy hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi lại trong xe lăn ở nửa PHẢI khung, người đổ về phía trước, thở dốc. SEBASTIAN đứng ở nửa TRÁI khung, "
  "một tay còn đỡ vai anh. Hậu cảnh là bức tường màn hình sáng xanh.",
  "ADRIAN hai tay chống lên đùi mình. SEBASTIAN một tay đỡ vai ADRIAN, tay kia buông xuống.",
  "ADRIAN nhìn xuống sàn thảm trước bánh xe. SEBASTIAN nhìn xuống ADRIAN.",
  "ADRIAN — người vừa đo được chính xác mình còn bao nhiêu: thở dốc, mồ hôi ở thái dương, giọng đứt quãng. "
  "SEBASTIAN — cố tìm ra phần tốt trong con số đó: giọng nhỏ, mắt lo.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN ngẩng đầu lên",
  ["ADRIAN_VESTNGOI", "SEBASTIAN"], "trước bục thép có tay vịn",
  {"ADRIAN": "ngồi lại trong xe lăn, đổ người về trước, nửa phải khung",
   "SEBASTIAN": "đứng đỡ vai, nửa trái khung"},
  "sát cạnh nhau", {"ADRIAN": "hai tay chống lên đùi mình", "SEBASTIAN": "một tay đỡ vai ADRIAN"}, qc="")
V("10", [18, 19], "cận-trung 85mm hạ thấp · ADRIAN NÉT phải ngồi lại trong xe lăn thở dốc + SEBASTIAN NÉT trái đỡ vai",
  [("ADRIAN", "ADRIAN_VESTNGOI"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN và SEBASTIAN, cả hai rõ mặt. ADRIAN đã ngồi lại trong xe lăn. Không có ai khác trong phòng.",
  "ADRIAN chống hai tay lên đùi và thở dốc, SEBASTIAN đỡ vai anh",
  [("ADRIAN", "breathless, flat", 18), ("SEBASTIAN", "gentle, encouraging", 19)], qcv="")

S("11", "cận 85mm, cao 1m10, cách ADRIAN 1m2, đặt chính diện trước xe lăn, hạ thấp ngang tầm người ngồi",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung từ ngực trở lên, tóc ướt mồ hôi ở thái dương. Ở rìa TRÁI khung "
  "thấy một mảng vai và cánh tay của SEBASTIAN, out nét. Hậu cảnh là bức tường màn hình sáng xanh, xoá phông.",
  "ADRIAN một tay lau ngang thái dương rồi đặt xuống vành tay vịn.",
  "ADRIAN nhìn thẳng lên bức tường màn hình phía trước.",
  "ADRIAN — người không cho phép mình lấy bốn giây làm chiến thắng: mặt bình trở lại, giọng đều, "
  "mắt đã tính sang bước tiếp theo.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN quay đầu sang phía SEBASTIAN",
  ["ADRIAN_VESTNGOI", "SEBASTIAN"], "trước bục thép có tay vịn",
  {"ADRIAN": "ngồi xe lăn chính diện giữa khung", "SEBASTIAN": "một mảng vai và cánh tay ở rìa trái"},
  "sát cạnh nhau", {"ADRIAN": "một tay lau thái dương rồi đặt xuống vành tay vịn",
                    "SEBASTIAN": "một tay đỡ vai, ngoài vùng nét"}, qc="")
V("11", [20, 21], "cận 85mm hạ thấp · ADRIAN NÉT ngồi xe lăn chính diện · một mảng vai và cánh tay SEBASTIAN rìa trái out nét",
  [("ADRIAN", "ADRIAN_VESTNGOI"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN rõ mặt. SEBASTIAN chỉ thấy MỘT MẢNG VAI và cánh tay ở rìa trái, out nét — KHÔNG quay mặt về camera.",
  "ADRIAN lau ngang thái dương rồi đặt tay xuống vành tay vịn",
  [("ADRIAN", "flat, unimpressed", 20), ("SEBASTIAN", "quiet, steady", 21)], qcv="")

S("12", "two-shot cận-trung 85mm, cao 1m20, cách ADRIAN 1m7, máy hạ thấp ngang tầm người ngồi xe lăn",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, đã ngồi thẳng lại. SEBASTIAN đứng ở nửa TRÁI khung, hai tay "
  "buông dọc thân. Hậu cảnh là bức tường mười tám màn hình đang phát.",
  "ADRIAN hai tay đặt lại trên vành tay vịn, các ngón khép. SEBASTIAN hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người vừa đặt cho mình một hạn chót mới bằng đúng số giây: mặt bình, mắt sáng lên một chút, "
  "giọng rất khẽ. SEBASTIAN — nhận ra sếp mình vừa đổi mục tiêu: mắt hơi mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi bức tường màn hình đổi sang một loạt dữ liệu mới",
  ["ADRIAN_VESTNGOI", "SEBASTIAN"], "trước bục thép có tay vịn",
  {"ADRIAN": "ngồi thẳng lại trong xe lăn, nửa phải khung", "SEBASTIAN": "đứng nửa trái khung"},
  "sát cạnh nhau", {"ADRIAN": "hai tay đặt trên vành tay vịn", "SEBASTIAN": "hai tay buông dọc thân"}, qc="")
V("12", [22], "two-shot cận-trung 85mm hạ thấp · ADRIAN NÉT phải ngồi xe lăn + SEBASTIAN NÉT trái đứng cạnh",
  [("ADRIAN", "ADRIAN_VESTNGOI"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN và SEBASTIAN, cả hai rõ mặt. ADRIAN ngồi trong xe lăn. Không có ai khác trong phòng.",
  "ADRIAN ngồi thẳng lại trong xe lăn và nói rất khẽ",
  [("ADRIAN", "quiet, resolved", 22)], [("SEBASTIAN", "silent, understanding")], qcv="")

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách ADRIAN 7m, đặt ở đầu phòng phía cửa nhìn dọc bàn họp",
  "Phòng chỉ huy chỉ còn một người: ADRIAN ngồi trong xe lăn ở đầu bàn trước BỨC TƯỜNG MƯỜI TÁM MÀN HÌNH "
  "đang phát. Mười chiếc ghế xoay da đen dọc bàn đều trống và đẩy lệch. Bục thép có tay vịn ngay cạnh anh.",
  "ADRIAN hai tay đặt trên vành tay vịn, các ngón khép.",
  "ADRIAN nhìn thẳng lên bức tường màn hình.",
  "ADRIAN — người vừa đo được mình còn bốn giây và đã đặt cho mình một hạn chót mới: mặt hoàn toàn bình, "
  "mắt tĩnh, hơi thở đã đều lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi bức tường màn hình đổi sang một loạt dữ liệu mới",
  ["ADRIAN_VESTNGOI"], "đầu bàn họp phòng chỉ huy, trước bức tường màn hình",
  {"ADRIAN": "ngồi một mình trong xe lăn ở đầu bàn"}, "một mình trong khung",
  {"ADRIAN": "hai tay đặt trên vành tay vịn"}, qc="")
B("B2", "Khép cảnh. Phòng chỉ huy đã trống. ADRIAN ngồi một mình trước bức tường mười tám màn hình.",
  "toàn cảnh 24mm · ADRIAN NÉT ngồi một mình trong xe lăn ở đầu bàn họp · không có ai khác trong khung",
  [("ADRIAN", "ADRIAN_VESTNGOI")],
  "CHỈ MỘT MÌNH ADRIAN trong khung, rõ mặt, ngồi trong xe lăn ở đầu bàn họp. Không có người nào khác trong phòng.",
  "một người ngồi một mình trước mười tám màn hình của công ty mình, có chín ngày để học lại cách đi, "
  "và không ai trong toà nhà này biết anh đang tập.",
  "bức tường màn hình đổi dữ liệu một lượt, ánh xanh quét ngang mặt bàn và mặt ADRIAN; một chiếc ghế xoay "
  "còn quay chậm rồi dừng; anh nhìn xuống thanh tay vịn thép cạnh mình một nhịp rồi nhìn lên.",
  "Ambient tiếng ù rất khẽ của dàn màn hình và điều hoà, SFX tiếng ghế xoay dừng lại trên thảm.",
  nhac("NGHỈ", "Sau nỗ lực bốn giây, cần một khoảng thở gần như ambient để khán giả ở lại với con số đó.",
       "Ambient at 54 BPM; a low organ pedal held under a felt piano placing single notes with very long gaps, "
       "a female voice humming wordlessly twice, far back in the mix; no drums; the pull is an eight-second gap of "
       "room tone; wordless and patient; cold room mix, female vocal, organ, piano, ambient, patient",
       "Ambient instrumental at 52 BPM; one sustained low organ note, a felt piano placing single notes every four "
       "seconds, a faint electrical hum underneath, no percussion, no arc, fading out; "
       "cold room mix, organ, piano, minimal, patient"),
  dur=8, qcv="")
