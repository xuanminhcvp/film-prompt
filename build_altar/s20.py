# -*- coding: utf-8 -*-
"""SCENE 20 — ĐÁM CƯỚI NHÀ HALE, NHÀ THỜ ST. MICHAEL (chiều). Điều dưỡng đứng ở cửa phục vụ."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S20", "REF_NHATHOTIEC_CHIEU", qc=qc.S20)

KHACH = ""

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 16m, đặt ở cuối lối đi phía cửa lớn nhìn về bàn thờ",
  "Nhà thờ đã được trang hoàng bằng hoa trắng và đèn pha lê, khách dự tiệc đứng thành cụm hai bên lối đi trải "
  "thảm trắng. MAYA đứng một mình ở cuối phòng bên PHẢI, sát CỬA PHỤC VỤ, trong bộ đồng phục trắng. "
  "ADRIAN ngồi trong chiếc xe lăn tay cũ cạnh CỘT ĐÁ THỨ BA, cách cô bốn mét, không ai đứng gần anh.",
  "MAYA hai tay chắp trước bụng, bàn tay phải có nẹp nhôm thấy rõ. ADRIAN hai tay đặt trên vành bánh xe.",
  "MAYA nhìn dọc lối đi về phía bàn thờ. ADRIAN nhìn về phía MAYA. Khách nền không nhìn vào ống kính.",
  "MAYA — người quay lại đúng nhà thờ đã bỏ rơi mình, trong bộ đồng phục và với một bàn tay gãy: cằm ngang, "
  "mặt bình. ADRIAN — ngồi một mình trong đám đông: mặt tĩnh, mắt không rời cô.",
  "đúng khoảnh khắc ngay TRƯỚC khi có người bước tới chỗ MAYA đứng",
  ["MAYA_TRANG", "ADRIAN_TIEC"], "cuối nhà thờ bên phải, cạnh cửa phục vụ và cột đá thứ ba",
  {"MAYA": "đứng một mình cạnh cửa phục vụ", "ADRIAN": "ngồi xe lăn tay cũ cạnh cột đá thứ ba"},
  "cách nhau bốn mét", {"MAYA": "hai tay chắp trước bụng, tay phải có nẹp nhôm",
                        "ADRIAN": "hai tay đặt trên vành bánh xe"})
B("B1", "Mở cảnh. Bốn tuần sau, cũng nhà thờ đó, đám cưới nhà Hale. MAYA đứng ở cửa phục vụ, ADRIAN ngồi cạnh cột đá.",
  "toàn cảnh 24mm · MAYA NÉT đứng cạnh cửa phục vụ + ADRIAN NÉT ngồi xe lăn tay cũ cạnh cột đá · khách hai bên mờ",
  [("MAYA", "MAYA_TRANG"), ("ADRIAN", "ADRIAN_TIEC")],
  "MAYA và ADRIAN rõ mặt. Khách dự tiệc hai bên lối đi mờ nhẹ, không ai nhìn vào camera.",
  "cùng một gian nhà thờ, cùng một lối đi, bốn tuần sau: lần này cô không đứng ở bàn thờ mà đứng ở cửa phục vụ, "
  "và người ngồi cạnh cột đá là người duy nhất trong phòng nhìn về phía cô.",
  "khách đi lại thành cụm cầm ly champagne dọc lối đi; hai người phục vụ bưng khay đi qua trước mặt MAYA "
  "mà không nhìn cô; ADRIAN quay bánh xe nửa vòng để nhìn rõ hơn về phía cô.",
  "Ambient tiếng trò chuyện dạ tiệc, tiếng ly chạm và tiếng đàn dây rất xa vọng từ phía bàn thờ.",
  nhac("KÌM", "Cả cảnh là sự sỉ nhục được bọc trong lụa trắng; nhạc phải sang và lạnh, tuyệt đối không được thương cảm.",
       "Chamber soul at 66 BPM; a string quartet playing a polite figure that keeps turning slightly sour, "
       "an upright bass underneath, a female alto entering once with a single low line; no drums; the pull is when "
       "the strings stop mid-phrase; lyrics about standing at the back of a room you were once the centre of; "
       "warm analog mix, female vocal, strings, restrained, cold",
       "Chamber instrumental at 64 BPM; a string quartet playing an elegant decorative figure with one dissonant "
       "note recurring, a harp answering, no percussion, ending on an unresolved chord; "
       "elegant and cold, strings, harp, chamber, unresolved"),
  dur=8)

# ── CỬA PHỤC VỤ ──
S("01", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt cuối nhà thờ lấy cả hai người, cửa phục vụ ở hậu cảnh",
  "WEDDING PLANNER đứng ở nửa TRÁI khung, một tay chỉ xuống chỗ MAYA đang đứng. MAYA đứng ở nửa PHẢI khung "
  "sát CỬA PHỤC VỤ. " + KHACH,
  "WEDDING PLANNER một tay chỉ xuống nền, tay kia ôm bìa kẹp hồ sơ đen. MAYA hai tay chắp trước bụng.",
  "WEDDING PLANNER nhìn xuống bìa hồ sơ rồi nhìn MAYA. MAYA nhìn thẳng vào WEDDING PLANNER.",
  "WEDDING PLANNER — người phân công vị trí như phân công một cái ghế: giọng nhanh, mắt không giữ lâu. "
  "MAYA — nhận lệnh không phản ứng: mặt bình, cằm ngang.",
  "đúng khoảnh khắc ngay TRƯỚC khi WEDDING PLANNER nhìn xuống bàn tay MAYA",
  ["WEDDING PLANNER", "MAYA_TRANG"], "cuối nhà thờ bên phải, cạnh cửa phục vụ",
  {"WEDDING PLANNER": "đứng nửa trái khung", "MAYA": "đứng sát cửa phục vụ nửa phải khung"},
  "cách nhau một bước", {"WEDDING PLANNER": "một tay chỉ xuống nền, tay kia ôm bìa kẹp hồ sơ",
                         "MAYA": "hai tay chắp trước bụng"})
V("01", [0, 1], "trung 50mm · WEDDING PLANNER NÉT trái + MAYA NÉT phải cạnh cửa phục vụ · khách nền mờ",
  [("WEDDING PLANNER", "WEDDING PLANNER"), ("MAYA", "MAYA_TRANG")],
  "WEDDING PLANNER và MAYA, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera.",
  "WEDDING PLANNER chỉ xuống chỗ MAYA phải đứng",
  [("WEDDING PLANNER", "brisk, efficient", 0), ("MAYA", "flat, obedient", 1)])

S("02", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, máy sau vai TRÁI của WEDDING PLANNER; vai và gáy cô chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, đã giơ BÀN TAY PHẢI CÓ NẸP NHÔM lên ngang ngực. WEDDING PLANNER "
  "chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là cửa phục vụ và bàn dài phủ khăn trắng.",
  "MAYA giơ bàn tay phải có nẹp nhôm lên ngang ngực cho người kia nhìn, tay trái đỡ dưới khuỷu tay phải.",
  "MAYA nhìn thẳng vào mặt WEDDING PLANNER.",
  "MAYA — người trả lời bằng một câu ngắn và không xin lỗi vì cái nẹp trên tay mình: giọng đều, "
  "mắt thẳng, khoé môi phẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hạ bàn tay xuống",
  ["MAYA_TRANG", "WEDDING PLANNER"], "cuối nhà thờ bên phải, cạnh cửa phục vụ",
  {"MAYA": "đứng chính diện giữa khung", "WEDDING PLANNER": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "giơ bàn tay phải có nẹp nhôm ngang ngực, tay trái đỡ khuỷu",
                         "WEDDING PLANNER": "một tay ôm bìa kẹp hồ sơ, ngoài vùng nét"})
V("02", [2, 3, 4, 5], "OTS cận-trung 85mm · MAYA NÉT chính diện giơ bàn tay có nẹp · vai và gáy WEDDING PLANNER tiền cảnh trái out nét",
  [("MAYA", "MAYA_TRANG"), ("WEDDING PLANNER", "WEDDING PLANNER")],
  "MAYA rõ mặt chính diện, bàn tay phải có nẹp nhôm thấy rõ. WEDDING PLANNER chỉ thấy VAI VÀ GÁY ở tiền cảnh "
  "trái, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA giơ bàn tay phải có nẹp nhôm lên ngang ngực cho người kia nhìn",
  [("WEDDING PLANNER", "brisk, checking", 2), ("MAYA", "flat, brief", 3),
   ("WEDDING PLANNER", "practical, uncaring", 4), ("MAYA", "level, final", 5)])

# ── BÀ NỘI NHÀ HALE ──
S("03", "trung 50mm, cao 1m30, cách MAYA 2m2, đặt cuối nhà thờ, hạ thấp để lấy cả người ngồi xe lăn nhẹ",
  "GRANDMOTHER HALE ngồi trong chiếc xe lăn nhẹ khung nhôm bạc ở nửa TRÁI khung, khăn len phủ trên đùi. "
  "MAYA đã bước tới và đứng cúi người ở nửa PHẢI khung cạnh bà. " + KHACH,
  "GRANDMOTHER HALE một tay vẫy MAYA lại gần. MAYA một tay đặt lên tay vịn chiếc xe lăn nhẹ, "
  "tay phải có nẹp giữ sát người.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "GRANDMOTHER HALE — bà cụ tám mươi chín tuổi vẫn còn sắc: mắt tỉnh, giọng khô. "
  "MAYA — chuyển sang giọng điều dưỡng ngay lập tức: mặt mềm hẳn, giọng ấm.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA khuỵu gối xuống ngang tầm mặt bà",
  ["GRANDMOTHER HALE", "MAYA_TRANG"], "cuối nhà thờ bên phải, cạnh chiếc xe lăn nhẹ của bà cụ",
  {"GRANDMOTHER HALE": "ngồi xe lăn nhẹ nửa trái khung", "MAYA": "đứng cúi người nửa phải khung"},
  "sát cạnh nhau", {"GRANDMOTHER HALE": "một tay vẫy MAYA lại gần",
                    "MAYA": "một tay đặt lên tay vịn xe lăn nhẹ, tay phải có nẹp giữ sát người"})
V("03", [6, 7], "trung 50mm hạ thấp · GRANDMOTHER HALE NÉT trái ngồi xe lăn nhẹ + MAYA NÉT phải cúi xuống · khách nền mờ",
  [("GRANDMOTHER HALE", "GRANDMOTHER HALE"), ("MAYA", "MAYA_TRANG")],
  "GRANDMOTHER HALE và MAYA, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera.",
  "GRANDMOTHER HALE vẫy MAYA lại gần, MAYA bước tới đặt tay lên tay vịn chiếc xe",
  [("GRANDMOTHER HALE", "dry, commanding", 6), ("MAYA", "warm, professional", 7)])

S("04", "cận-trung 85mm, cao 1m10, cách GRANDMOTHER HALE 1m5, máy hạ thấp ngang tầm hai người",
  "GRANDMOTHER HALE ngồi trong chiếc xe lăn nhẹ ở nửa TRÁI khung. MAYA đã khuỵu một gối xuống ở nửa PHẢI khung, "
  "ngang tầm mặt bà. Hậu cảnh là cột đá và khách dự tiệc mờ.",
  "GRANDMOTHER HALE một tay đặt lên mép khăn len trên đùi. MAYA hai tay đặt lên tay vịn chiếc xe lăn nhẹ, "
  "bàn tay phải có nẹp nhôm thấy rõ.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "GRANDMOTHER HALE — hỏi thẳng và nhìn kỹ: mắt sắc, mày nhướn. "
  "MAYA — trả lời tên mình bằng đúng một tiếng: mặt bình, giọng nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi GRANDMOTHER HALE nhìn xuống bàn tay có nẹp",
  ["GRANDMOTHER HALE", "MAYA_TRANG"], "cuối nhà thờ bên phải, cạnh chiếc xe lăn nhẹ",
  {"GRANDMOTHER HALE": "ngồi xe lăn nhẹ nửa trái khung", "MAYA": "khuỵu một gối nửa phải khung"},
  "ngang tầm mặt nhau", {"GRANDMOTHER HALE": "một tay đặt lên mép khăn len",
                         "MAYA": "hai tay đặt lên tay vịn xe lăn nhẹ, tay phải có nẹp"})
V("04", [8, 9, 10], "cận-trung 85mm hạ thấp · GRANDMOTHER HALE NÉT trái ngồi xe lăn nhẹ + MAYA NÉT phải khuỵu một gối",
  [("GRANDMOTHER HALE", "GRANDMOTHER HALE"), ("MAYA", "MAYA_TRANG")],
  "GRANDMOTHER HALE và MAYA, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera.",
  "MAYA khuỵu một gối xuống ngang tầm mặt bà cụ, hai tay đặt lên tay vịn chiếc xe",
  [("GRANDMOTHER HALE", "sharp, direct", 8), ("MAYA", "quiet, plain", 9),
   ("GRANDMOTHER HALE", "sharp, probing", 10)])

S("05", "cận 85mm, cao 1m10, cách MAYA 1m2, máy hạ thấp, lấy MAYA nét và một mảng vai bà cụ rìa trái",
  "MAYA khuỵu một gối chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo lụa xanh phấn "
  "và tay vịn chiếc xe lăn nhẹ của GRANDMOTHER HALE, out nét. Hậu cảnh là cột đá và ánh đèn pha lê xoá phông.",
  "MAYA một tay đặt trên tay vịn chiếc xe lăn nhẹ, bàn tay phải có nẹp đặt trên đùi mình.",
  "MAYA nhìn thẳng vào mặt GRANDMOTHER HALE.",
  "MAYA — người trả lời câu hỏi khó bằng đúng một con số và không thêm gì: giọng bình, mắt thẳng, "
  "KHÔNG kể khổ.",
  "đúng khoảnh khắc ngay TRƯỚC khi GRANDMOTHER HALE hỏi về người ngồi cạnh cột",
  ["MAYA_TRANG", "GRANDMOTHER HALE"], "cuối nhà thờ bên phải, cạnh chiếc xe lăn nhẹ",
  {"MAYA": "khuỵu một gối, chính diện giữa khung",
   "GRANDMOTHER HALE": "một mảng vai áo lụa và tay vịn xe lăn nhẹ ở rìa trái"},
  "ngang tầm mặt nhau", {"MAYA": "một tay trên tay vịn xe lăn nhẹ, tay phải có nẹp đặt trên đùi",
                         "GRANDMOTHER HALE": "một tay trên mép khăn len, ngoài vùng nét"})
V("05", [11, 12], "cận 85mm hạ thấp · MAYA NÉT chính diện · một mảng vai và tay vịn xe lăn nhẹ của GRANDMOTHER HALE rìa trái out nét",
  [("MAYA", "MAYA_TRANG"), ("GRANDMOTHER HALE", "GRANDMOTHER HALE")],
  "MAYA rõ mặt. GRANDMOTHER HALE chỉ thấy MỘT MẢNG VAI áo lụa xanh phấn và tay vịn chiếc xe lăn nhẹ ở rìa trái, "
  "out nét — KHÔNG quay mặt về camera.",
  "MAYA đặt bàn tay có nẹp lên đùi mình và trả lời",
  [("MAYA", "plain, unembellished", 11), ("GRANDMOTHER HALE", "dry, probing", 12)])

S("06", "trung 50mm, cao 1m10, cách MAYA 2m, máy hạ thấp, lấy hai người tiền cảnh và ADRIAN ở hậu cảnh cạnh cột đá",
  "MAYA khuỵu một gối ở nửa PHẢI khung, GRANDMOTHER HALE ngồi trong chiếc xe lăn nhẹ ở nửa TRÁI khung. "
  "Ở hậu cảnh, cách bốn mét, ADRIAN ngồi trong chiếc xe lăn tay cũ cạnh CỘT ĐÁ THỨ BA, thấy rõ mặt, "
  "xung quanh anh không có ai đứng gần.",
  "MAYA một tay chỉ về phía chiếc xe lăn ở hậu cảnh. GRANDMOTHER HALE một tay đặt trên tay vịn. "
  "ADRIAN hai tay đặt trên vành bánh xe.",
  "MAYA nhìn về phía ADRIAN rồi quay lại nhìn bà cụ. GRANDMOTHER HALE nhìn theo hướng tay chỉ. "
  "ADRIAN nhìn về phía hai người.",
  "MAYA — nói hai chữ chồng tôi bằng giọng rất bình: cằm ngang. GRANDMOTHER HALE — nhìn kỹ người ngồi một mình "
  "và thấy điều mình vừa nói là thật: mắt hạ xuống. ADRIAN — mặt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng thẳng dậy khỏi tư thế quỳ",
  ["MAYA_TRANG", "GRANDMOTHER HALE", "ADRIAN_TIEC"], "cuối nhà thờ bên phải, từ chỗ bà cụ tới cột đá thứ ba",
  {"MAYA": "khuỵu một gối nửa phải khung", "GRANDMOTHER HALE": "ngồi xe lăn nhẹ nửa trái khung",
   "ADRIAN": "ngồi xe lăn tay cũ cạnh cột đá ở hậu cảnh"},
  "ADRIAN cách bốn mét", {"MAYA": "một tay chỉ về phía chiếc xe lăn ở hậu cảnh",
                          "GRANDMOTHER HALE": "một tay đặt trên tay vịn",
                          "ADRIAN": "hai tay đặt trên vành bánh xe"})
V("06", [13, 14, 15], "trung 50mm hạ thấp · GRANDMOTHER HALE NÉT trái + MAYA NÉT phải khuỵu gối + ADRIAN NÉT ở hậu cảnh cạnh cột đá",
  [("GRANDMOTHER HALE", "GRANDMOTHER HALE"), ("MAYA", "MAYA_TRANG"), ("ADRIAN", "ADRIAN_TIEC")],
  "GRANDMOTHER HALE và MAYA rõ mặt ở tiền cảnh, ADRIAN rõ mặt ở hậu cảnh cạnh cột đá. "
  "Khách dự tiệc mờ, không ai nhìn vào camera.",
  "MAYA chỉ về phía chiếc xe lăn ở hậu cảnh, bà cụ nhìn theo hướng đó",
  [("MAYA", "plain, steady", 13), ("GRANDMOTHER HALE", "quiet, observing", 14),
   ("MAYA", "flat, unsurprised", 15)],
  ketclip="Cuối clip, MAYA đứng thẳng dậy và lùi về đứng lại chỗ cũ cạnh cửa phục vụ. "
          "Clip dừng đúng lúc cô đứng vào đúng vị trí đó.")

# ── RYAN ──
S("07", "trung 50mm, cao 1m55, cách MAYA 2m4, đặt cuối nhà thờ lấy cả hai người, cột đá thứ ba ở hậu cảnh",
  "RYAN đứng ở nửa TRÁI khung trong bộ tuxedo, tay cầm ly champagne. MAYA đứng ở nửa PHẢI khung sát cửa phục vụ. "
  + KHACH,
  "RYAN một tay cầm ly champagne, tay kia đút túi quần. MAYA hai tay chắp trước bụng, tay phải có nẹp nhôm.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — chú rể đang đi một vòng và dừng lại ở chỗ thú vị nhất: khoé môi kéo, mắt sáng vì rượu. "
  "MAYA — chúc mừng bằng đúng hai chữ: mặt bình, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN chỉ tay về phía cột đá thứ ba",
  ["RYAN_TUXEDO", "MAYA_TRANG"], "cuối nhà thờ bên phải, cạnh cửa phục vụ",
  {"RYAN": "đứng nửa trái khung", "MAYA": "đứng sát cửa phục vụ nửa phải khung"},
  "cách nhau một bước", {"RYAN": "một tay cầm ly champagne, tay kia đút túi",
                         "MAYA": "hai tay chắp trước bụng, tay phải có nẹp"})
V("07", [16, 17], "trung 50mm · RYAN NÉT trái cầm ly champagne + MAYA NÉT phải cạnh cửa phục vụ · khách nền mờ",
  [("RYAN", "RYAN_TUXEDO"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN dừng lại trước mặt MAYA với ly champagne trong tay",
  [("RYAN", "amused, tipsy", 16), ("MAYA", "flat, even", 17)])

S("08", "cận-trung 85mm, cao 1m55, cách RYAN 1m7, đặt cuối nhà thờ lấy RYAN nét và MAYA cùng khung",
  "RYAN đứng ở nửa TRÁI khung, một tay chỉ xuống nền đá ngay dưới chân MAYA. MAYA đứng ở nửa PHẢI khung. "
  "Hậu cảnh là cột đá thứ ba và khách dự tiệc mờ.",
  "RYAN một tay chỉ xuống nền đá dưới chân MAYA, tay kia cầm ly. MAYA hai tay chắp trước bụng.",
  "RYAN nhìn xuống nền rồi nhìn MAYA. MAYA nhìn thẳng vào RYAN.",
  "RYAN — người thích thú vì trùng hợp đó: khoé môi kéo rộng, giọng nhẹ. "
  "MAYA — trả lời hai chữ và không rời mắt: mặt hoàn toàn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN khoát tay chỉ quanh gian nhà thờ",
  ["RYAN_TUXEDO", "MAYA_TRANG"], "cuối nhà thờ bên phải, cạnh cửa phục vụ",
  {"RYAN": "đứng nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "cách nhau một bước", {"RYAN": "một tay chỉ xuống nền đá, tay kia cầm ly",
                         "MAYA": "hai tay chắp trước bụng"})
V("08", [18, 19], "cận-trung 85mm · RYAN NÉT trái chỉ xuống nền + MAYA NÉT phải đứng đối diện",
  [("RYAN", "RYAN_TUXEDO"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera.",
  "RYAN chỉ xuống đúng chỗ nền đá dưới chân MAYA",
  [("RYAN", "amused, needling", 18), ("MAYA", "flat, brief", 19)])

S("09", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, máy sau vai TRÁI của RYAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung. RYAN chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng MAYA là cửa phục vụ hẹp và bàn dài phủ khăn trắng có khay ly.",
  "MAYA hai tay chắp trước bụng, bàn tay phải có nẹp nhôm đặt lên bàn tay trái.",
  "MAYA nhìn thẳng vào mặt RYAN.",
  "MAYA — người thừa nhận đúng một điều và chính vì thế mà câu trả lời cứng như đá: giọng bình, mắt thẳng, "
  "KHÔNG cay đắng.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN quay lưng bước về phía lối đi giữa",
  ["MAYA_TRANG", "RYAN_TUXEDO"], "cuối nhà thờ bên phải, cạnh cửa phục vụ",
  {"MAYA": "đứng chính diện giữa khung", "RYAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "hai tay chắp trước bụng, tay phải có nẹp đặt trên tay trái",
                         "RYAN": "một tay cầm ly champagne, ngoài vùng nét"})
V("09", [20, 21], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy RYAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_TRANG"), ("RYAN", "RYAN_TUXEDO")],
  "MAYA rõ mặt chính diện. RYAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "RYAN khoát tay chỉ quanh gian nhà thờ, MAYA đứng yên nhìn thẳng",
  [("RYAN", "boastful, tipsy", 20), ("MAYA", "level, unbothered", 21)])

# ── HAI NGƯỜI ĐÀN ÔNG BÊN CỘT ──
S("10", "trung 50mm, cao 1m55, cách JULIAN 2m2, đặt trong lòng nhà thờ lấy cả hai người, cột đá ở hậu cảnh",
  "JULIAN đứng ở nửa TRÁI khung trong bộ tuxedo, một tay cầm ly. GERALD HALE đứng ở nửa PHẢI khung, cũng cầm ly. "
  "Ở hậu cảnh xa phía sau hai người thấy một góc cột đá và chiếc xe lăn tay cũ, MỜ, không rõ mặt người ngồi. " + KHACH,
  "JULIAN một tay cầm ly, tay kia chỉ kín đáo về phía cột đá phía sau. GERALD HALE hai tay cầm ly ngang bụng.",
  "JULIAN nhìn về phía cột đá rồi nhìn GERALD HALE. GERALD HALE nhìn theo hướng tay chỉ.",
  "JULIAN — người mách một chuyện vui trong bữa tiệc: khoé môi kéo, giọng nhẹ. "
  "GERALD HALE — khó chịu vì có thứ không thuộc về bữa tiệc của mình: mày chau, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi GERALD HALE nhấp một ngụm rượu",
  ["JULIAN_TUX", "GERALD HALE"], "trong lòng nhà thờ, cách cột đá thứ ba vài bước",
  {"JULIAN": "đứng nửa trái khung", "GERALD HALE": "đứng nửa phải khung"},
  "sát cạnh nhau", {"JULIAN": "một tay cầm ly, tay kia chỉ kín đáo về phía cột đá",
                    "GERALD HALE": "hai tay cầm ly ngang bụng"})
V("10", [22, 23], "trung 50mm · JULIAN NÉT trái chỉ về phía cột đá + GERALD HALE NÉT phải cầm ly · khách nền mờ",
  [("JULIAN", "JULIAN_TUX"), ("GERALD HALE", "GERALD HALE")],
  "JULIAN và GERALD HALE, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera. "
  "Người ngồi trong chiếc xe lăn ở hậu cảnh xa CHỈ thấy mờ, KHÔNG rõ mặt.",
  "JULIAN chỉ kín đáo về phía cột đá phía sau, GERALD HALE nhìn theo",
  [("JULIAN", "light, gossiping", 22), ("GERALD HALE", "clipped, displeased", 23)])

S("11", "cận-trung 85mm, cao 1m55, cách GERALD HALE 1m7, đặt trong lòng nhà thờ lấy GERALD nét và JULIAN cùng khung",
  "GERALD HALE đứng ở nửa PHẢI khung, đã hạ ly xuống. JULIAN đứng ở nửa TRÁI khung. Hậu cảnh là cụm khách "
  "dự tiệc mờ và một chân máy quay truyền hình.",
  "GERALD HALE một tay hạ ly xuống ngang bụng, tay kia phẩy nhẹ về phía cột đá. JULIAN một tay cầm ly nâng lên.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "JULIAN — giải thích sự có mặt của người kia như giải thích một kiện hàng đi kèm: giọng nhẹ, khoé môi kéo. "
  "GERALD HALE — chấp nhận với một điều kiện: mặt cứng, giọng gọn.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai người quay lưng đi về phía bàn thờ",
  ["GERALD HALE", "JULIAN_TUX"], "trong lòng nhà thờ, cách cột đá thứ ba vài bước",
  {"GERALD HALE": "đứng nửa phải khung", "JULIAN": "đứng nửa trái khung"},
  "sát cạnh nhau", {"GERALD HALE": "một tay hạ ly xuống, tay kia phẩy nhẹ về phía cột đá",
                    "JULIAN": "một tay cầm ly nâng lên"})
V("11", [24, 25], "cận-trung 85mm · JULIAN NÉT trái + GERALD HALE NÉT phải, đứng cạnh nhau · khách nền mờ",
  [("JULIAN", "JULIAN_TUX"), ("GERALD HALE", "GERALD HALE")],
  "JULIAN và GERALD HALE, cả hai rõ mặt. Khách dự tiệc ở hậu cảnh mờ, không ai nhìn vào camera.",
  "JULIAN nâng ly lên, GERALD HALE phẩy tay về phía cột đá",
  [("JULIAN", "light, dismissive", 24), ("GERALD HALE", "flat, conditional", 25)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "trung-rộng 35mm, cao 1m30, cách ADRIAN 5m, đặt trong lòng nhà thờ nhìn về phía cột đá thứ ba",
  "ADRIAN ngồi một mình trong chiếc xe lăn tay cũ cạnh CỘT ĐÁ THỨ BA. Quanh anh trong bán kính ba mét không có "
  "ai đứng; các cụm khách dự tiệc đứng xa hơn, quay lưng về phía anh, mờ ngoài vùng nét. "
  "MAYA đứng ở xa phía sau cạnh cửa phục vụ, nhỏ trong khung, thấy rõ mặt.",
  "ADRIAN hai tay đặt trên vành bánh xe. MAYA hai tay chắp trước bụng.",
  "ADRIAN nhìn dọc lối đi về phía bàn thờ. MAYA nhìn về phía ADRIAN. "
  "Khách nền quay lưng, TUYỆT ĐỐI không nhìn vào ống kính.",
  "ADRIAN — người ngồi giữa bốn trăm người và không ai nói với anh một câu nào suốt một tiếng: mặt hoàn toàn "
  "bình, mắt tĩnh. MAYA — nhìn anh từ xa và không tới được: mặt phẳng, quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi tiếng nhạc trong nhà thờ ngừng bặt",
  ["ADRIAN_TIEC", "MAYA_TRANG"], "cạnh cột đá thứ ba và cửa phục vụ ở xa",
  {"ADRIAN": "ngồi một mình cạnh cột đá thứ ba", "MAYA": "đứng xa phía sau cạnh cửa phục vụ"},
  "cách nhau bốn mét", {"ADRIAN": "hai tay đặt trên vành bánh xe", "MAYA": "hai tay chắp trước bụng"})
B("B2", "Khép cảnh. ADRIAN ngồi một mình cạnh cột đá giữa bốn trăm khách, MAYA nhìn anh từ chỗ cửa phục vụ.",
  "trung-rộng 35mm · ADRIAN NÉT ngồi một mình cạnh cột đá + MAYA NÉT nhỏ ở xa cạnh cửa phục vụ · khách quay lưng, mờ",
  [("ADRIAN", "ADRIAN_TIEC"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt cạnh cột đá, MAYA rõ mặt nhưng nhỏ ở xa cạnh cửa phục vụ. Khách dự tiệc quay lưng, mờ, "
  "không ai nhìn vào camera.",
  "khoảng trống ba mét quanh chiếc xe lăn giữa một gian phòng chật kín người chính là nội dung của khung hình này.",
  "một người phục vụ bưng khay đi vòng qua chiếc xe lăn mà không dừng lại; hai vị khách quay lưng lại gần hơn; "
  "ADRIAN không nhúc nhích; ở xa, MAYA đổi chân đứng một lần.",
  "Ambient tiếng trò chuyện dạ tiệc và tiếng đàn dây, SFX tiếng ly chạm nhau rất gần rồi xa dần.",
  nhac("NGHỈ", "Trước khi cả nhà thờ nổ tung ở cảnh sau, cần một nhịp gần như câm để nhìn kỹ khoảng trống quanh chiếc xe lăn.",
       "Ambient chamber at 56 BPM; one viola holding a long note under a harp placing single notes with long gaps, "
       "a female voice humming very faintly far back; no drums; the pull is a long silence before the last note; "
       "wordless and patient; large natural reverb, female vocal, viola, harp, ambient, still",
       "Ambient instrumental at 54 BPM; a solo viola holding one long note, a harp placing single notes every four "
       "seconds, a very low organ pedal underneath, no percussion, thinning to silence; "
       "large natural reverb, viola, harp, organ, minimal, patient"),
  dur=8)
