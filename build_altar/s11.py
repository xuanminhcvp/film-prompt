# -*- coding: utf-8 -*-
"""SCENE 11 — TRONG NHÀ CỔNG (đêm). Mười bốn vết mổ và một phong bì kraft."""
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S11", "REF_NHACONG_DEM")

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m40, cách MAYA 4m, đặt ở góc phòng phía cửa nhìn chéo vào chỗ bàn gỗ",
  "MAYA quỳ một gối trên tấm thảm cạnh chiếc xe lăn ở giữa phòng, chậu nước inox và chồng khăn bông trắng "
  "đặt trên bàn gỗ vuông ngay cạnh. ADRIAN ngồi trong xe lăn, ống quần vải đã được xắn lên tới gối.",
  "MAYA một tay vắt chiếc khăn bông trong chậu nước, tay kia đỡ mép chậu. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống chậu nước. ADRIAN nhìn ra phía cửa sổ tối.",
  "MAYA — người vào ca chăm sóc như mọi tối: mặt tập trung, tay quen việc. "
  "ADRIAN — chịu đựng việc được chăm sóc: quai hàm giữ, mắt nhìn đi chỗ khác.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA áp chiếc khăn ấm lên vệt đỏ trên chân anh",
  ["MAYA_ONHA", "ADRIAN_NHA"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"MAYA": "quỳ một gối cạnh chiếc xe lăn", "ADRIAN": "ngồi trong xe lăn, ống quần xắn tới gối"},
  "sát cạnh nhau", {"MAYA": "một tay vắt khăn trong chậu nước, tay kia đỡ mép chậu",
                    "ADRIAN": "hai tay trên vành tay vịn"})
B("B1", "Mở cảnh. Đêm trong nhà cổng. MAYA quỳ cạnh xe lăn thay băng, ADRIAN nhìn ra cửa sổ tối.",
  "trung-rộng 35mm · MAYA NÉT quỳ cạnh xe lăn + ADRIAN NÉT ngồi trong xe · không có ai khác",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN rõ mặt. ADRIAN mặc nguyên áo thun dài tay, chỉ có ống quần xắn lên tới gối. "
  "Không có người nào khác trong khung.",
  "buổi tối thứ mười mấy của một thoả thuận mười hai tháng; việc chăm sóc đã thành thói quen, và đêm nay "
  "thói quen đó sắp chạm phải một thứ không nên chạm.",
  "MAYA vắt chiếc khăn, hơi nước bốc lên trong quầng đèn bàn; ADRIAN nhìn ra cửa sổ tối và không nói gì; "
  "ngọn đèn trần bóng đơn đung đưa rất khẽ.",
  "Ambient tiếng gỗ nhà cũ kêu khẽ và tiếng gió ngoài cửa sổ, SFX tiếng nước vắt trong chậu inox.",
  nhac("NGHỈ", "Cảnh riêng tư nhất giữa hai người tới lúc này — nhạc phải gần như ambient để không xâm phạm nó.",
       "Ambient soul at 56 BPM; a female alto humming very close to the mic over sparse Rhodes chords, one short "
       "line of lyric near the end; no drums, no bass; the pull is a long gap of room tone before that line; "
       "lyrics about hands doing quiet work at the end of a long day; dry intimate mix, female vocal, Rhodes, "
       "ambient, tender",
       "Ambient instrumental at 54 BPM; Rhodes piano placing chords with long gaps, a warm pad underneath breathing "
       "slowly, a single upright bass note every few bars, no percussion, fading out mid-phrase; "
       "very soft night mix, Rhodes, pad, upright bass, minimal, warm"),
  dur=6)

# ── THAY BĂNG ──
S("01", "cận-trung 85mm, cao 1m00, cách MAYA 1m5, máy hạ thấp ngang tầm người quỳ, lấy cả hai người",
  "MAYA quỳ ở nửa PHẢI khung, chiếc khăn bông ấm trong tay đang áp lên phần ống chân ADRIAN. ADRIAN ngồi trong "
  "xe lăn ở nửa TRÁI khung, áo thun dài tay còn nguyên. Hậu cảnh là giường đơn khung sắt trắng và đèn bàn.",
  "MAYA một tay áp chiếc khăn lên ống chân ADRIAN, tay kia giữ cổ chân anh. ADRIAN một tay bám vành tay vịn.",
  "MAYA nhìn xuống chỗ mình đang làm. ADRIAN nhìn xuống MAYA.",
  "MAYA — người báo trước cơn xót vì đó là phép lịch sự nghề nghiệp: giọng đều, tay chắc. "
  "ADRIAN — nói ra câu mình vẫn nói suốt sáu tháng: mặt bình, giọng phẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi quai hàm ADRIAN động một nhịp",
  ["MAYA_ONHA", "ADRIAN_NHA"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"MAYA": "quỳ nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay áp khăn lên ống chân, tay kia giữ cổ chân",
                    "ADRIAN": "một tay bám vành tay vịn"})
V("01", [0, 1], "cận-trung 85mm hạ thấp · MAYA NÉT phải quỳ + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN mặc nguyên áo, chỉ xắn ống quần. Không có ai khác trong khung.",
  "MAYA áp chiếc khăn ấm lên ống chân ADRIAN, quai hàm anh động một nhịp",
  [("MAYA", "even, warning", 0), ("ADRIAN", "flat, automatic", 1)])

S("02", "cận 85mm, cao 1m10, cách ADRIAN 1m2, máy hạ thấp chếch bên, lấy ADRIAN nét và một mảng vai MAYA rìa dưới",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung từ ngực trở lên. Ở rìa DƯỚI khung thấy một mảng vai và mái tóc xoăn xoã "
  "của MAYA đang quỳ, out nét. Hậu cảnh là cửa sổ tối và rèm vải mỏng màu ngà.",
  "ADRIAN một tay đưa lên chỉnh lại cổ áo thun rồi đặt xuống vành tay vịn.",
  "ADRIAN nhìn xuống MAYA rồi nhìn ra chỗ khác.",
  "ADRIAN — người vừa bị bắt quả tang là mình có cảm giác: mắt dời đi một nhịp, khoé môi động, "
  "giọng khô hơn bình thường.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhấc chiếc khăn ra khỏi chân anh",
  ["ADRIAN_NHA", "MAYA_ONHA"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "một mảng vai và mái tóc xoã ở rìa dưới khung"},
  "sát cạnh nhau", {"ADRIAN": "một tay chỉnh cổ áo rồi đặt xuống vành tay vịn",
                    "MAYA": "hai tay đang làm việc dưới khung, ngoài vùng nét"})
V("02", [2, 3], "cận 85mm hạ thấp · ADRIAN NÉT ngồi xe lăn · một mảng vai và mái tóc xoã MAYA rìa dưới khung out nét",
  [("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_ONHA")],
  "ADRIAN rõ mặt. MAYA chỉ thấy MỘT MẢNG VAI và mái tóc xoăn XOÃ ở rìa dưới khung, out nét — KHÔNG quay mặt về camera.",
  "MAYA nói từ dưới khung, ADRIAN chỉnh lại cổ áo và nhìn đi chỗ khác",
  [("MAYA", "dry, observant", 2), ("ADRIAN", "dry, deflecting", 3)])

S("03", "cận-trung 85mm, cao 1m00, cách MAYA 1m4, máy hạ thấp ngang tầm người quỳ, lấy cả hai người",
  "MAYA quỳ ở nửa PHẢI khung, hai tay đang đỡ ống chân trái ADRIAN nhấc lên khỏi bàn để chân. ADRIAN ngồi trong "
  "xe lăn ở nửa TRÁI khung. Trên bàn gỗ cạnh đó có chồng khăn bông và cuộn băng gạc.",
  "MAYA hai tay đỡ dưới ống chân ADRIAN, các ngón dừng lại trên một đường sẹo. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống các vết sẹo trên chân anh. ADRIAN nhìn xuống MAYA.",
  "MAYA — người vừa đọc ra một thứ mà nghề của cô không cho phép bỏ qua: tay dừng lại, mày chau, "
  "giọng chậm hẳn. ADRIAN — cảnh giác ngay: mắt hơi nheo.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA lần ngón tay dọc theo đường sẹo",
  ["MAYA_ONHA", "ADRIAN_NHA"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"MAYA": "quỳ nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay đỡ dưới ống chân, ngón dừng trên một đường sẹo",
                    "ADRIAN": "hai tay trên vành tay vịn"})
V("03", [4, 5], "cận-trung 85mm hạ thấp · MAYA NÉT phải quỳ + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN mặc nguyên áo, chỉ xắn ống quần. Không có ai khác trong khung.",
  "MAYA đỡ ống chân ADRIAN lên và dừng ngón tay lại trên một đường sẹo",
  [("MAYA", "slowing, focused", 4), ("ADRIAN", "guarded, quiet", 5)])

S("04", "cận 85mm, cao 1m00, cách MAYA 1m2, máy hạ thấp chếch bên, lấy MAYA nét và một mảng đùi cùng tay vịn xe lăn rìa trái",
  "MAYA quỳ chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng ống quần xắn và tay vịn xe lăn "
  "của ADRIAN, out nét. Hậu cảnh là góc bếp nhỏ và tủ bếp gỗ sơn trắng.",
  "MAYA một tay đếm bằng đầu ngón trỏ dọc theo chân ADRIAN, tay kia đỡ.",
  "MAYA nhìn xuống chỗ ngón tay mình đang đếm.",
  "MAYA — điều dưỡng hồi sức đang đọc một bệnh án bằng tay và biết con số này không khớp với chuyện tai nạn: "
  "mày chau sâu, giọng thấp và chắc, mắt tính toán.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA ngẩng lên nhìn ADRIAN",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"MAYA": "quỳ chính diện giữa khung", "ADRIAN": "một mảng ống quần xắn và tay vịn xe lăn ở rìa trái"},
  "sát cạnh nhau", {"MAYA": "một tay đếm bằng ngón trỏ, tay kia đỡ chân",
                    "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
VX("04", "cận 85mm hạ thấp · MAYA NÉT quỳ chính diện · một mảng ống quần và tay vịn xe lăn ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA rõ mặt. ADRIAN chỉ thấy MỘT MẢNG ỐNG QUẦN XẮN và tay vịn xe lăn ở rìa trái, out nét — "
  "KHÔNG quay mặt về camera.",
  "MAYA lần ngón tay đếm dọc theo các vết sẹo và đọc ra con số",
  [("MAYA", "low, certain",
    "This is not a car crash pattern. This is fourteen surgical entries.")],
  [("ADRIAN", "silent, going still")])

S("04b", "cận-trung 85mm, cao 1m00, cách MAYA 1m5, máy hạ thấp ngang tầm người quỳ, lấy cả hai người",
  "MAYA quỳ ở nửa PHẢI khung, một tay còn đặt trên ống chân ADRIAN. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, "
  "đã cúi người xuống nhìn cô. Hậu cảnh là bàn gỗ vuông có chậu nước inox và chồng khăn bông.",
  "MAYA một tay đặt trên ống chân ADRIAN, tay kia chỉ lên phía hông anh. ADRIAN một tay bám vành tay vịn.",
  "MAYA nhìn lên mặt ADRIAN. ADRIAN nhìn xuống MAYA.",
  "MAYA — người vừa đọc xong một bệnh án bằng đầu ngón tay và biết nó không khớp với chuyện tai nạn: "
  "giọng chậm, chắc, mắt không rời. ADRIAN — cảnh giác hẳn: quai hàm siết.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng dậy khỏi tư thế quỳ",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"MAYA": "quỳ nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung, cúi xuống"},
  "sát cạnh nhau", {"MAYA": "một tay trên ống chân ADRIAN, tay kia chỉ lên phía hông",
                    "ADRIAN": "một tay bám vành tay vịn"})
VX("04b", "cận-trung 85mm hạ thấp · MAYA NÉT phải quỳ + ADRIAN NÉT trái ngồi xe lăn cúi xuống",
   [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
   "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN mặc nguyên áo, chỉ xắn ống quần. Không có ai khác trong khung.",
   "MAYA chỉ lên phía hông ADRIAN rồi ngẩng lên nhìn anh",
   [("MAYA", "low, certain",
     "Two rods, six screws, and a plate here at the hip. Somebody very expensive put you back together."),
    ("ADRIAN", "guarded, flat", "Is that a question?")],
   ketclip="Cuối clip, MAYA đứng dậy, với lấy chiếc PHONG BÌ GIẤY KRAFT đặt trên mặt bàn gỗ và cầm nó lên. "
           "Clip dừng đúng lúc chiếc phong bì rời khỏi mặt bàn.")

S("05", "trung 50mm, cao 1m30, cách MAYA 2m, đặt trong phòng, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung cạnh bàn gỗ, trên tay là một PHONG BÌ GIẤY KRAFT khổ lớn đã mở nắp. ADRIAN ngồi "
  "trong xe lăn ở nửa TRÁI khung, đã quay hẳn người về phía cô.",
  "MAYA hai tay cầm chiếc phong bì kraft, một ngón đang giữ mép miệng phong bì. ADRIAN một tay siết vành tay vịn.",
  "MAYA nhìn ADRIAN. ADRIAN nhìn chiếc phong bì trong tay cô.",
  "MAYA — người hỏi thẳng và không giấu rằng mình đã thấy: giọng đều, mắt thẳng. "
  "ADRIAN — thấy đúng thứ mình cất kỹ nhất đang nằm trong tay cô: quai hàm siết, giọng cứng lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA rút tấm ảnh ra khỏi phong bì",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng nửa phải khung cầm phong bì", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một bước", {"MAYA": "hai tay cầm chiếc phong bì kraft", "ADRIAN": "một tay siết vành tay vịn"})
V("05", [8, 9], "trung 50mm hạ thấp · MAYA NÉT phải cầm phong bì + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA giơ chiếc phong bì kraft lên, ADRIAN siết chặt vành tay vịn",
  [("MAYA", "level, direct", 8), ("ADRIAN", "hard, quiet", 9)])

S("06", "cận-trung 85mm, cao 1m30, cách MAYA 1m6, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, chiếc phong bì kraft trong tay, mặt phong bì hướng về phía ADRIAN. "
  "ADRIAN chỉ còn là vai và gáy ở rìa TRÁI tiền cảnh, ngồi thấp, ngoài vùng nét.",
  "MAYA một tay cầm chiếc phong bì, ngón trỏ tay kia gõ vào ô chữ in trên mặt phong bì.",
  "MAYA nhìn thẳng xuống mặt ADRIAN.",
  "MAYA — người kể lại chính xác mình tìm thấy nó thế nào, không xin lỗi và cũng không đắc thắng: giọng đều, "
  "mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN ra lệnh cho cô cất nó đi",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng chính diện giữa khung", "ADRIAN": "vai và gáy tiền cảnh trái, ngồi thấp"},
  "cách nhau một bước", {"MAYA": "một tay cầm phong bì, tay kia gõ vào ô chữ trên phong bì",
                         "ADRIAN": "hai tay trên vành tay vịn, ngoài vùng nét"})
V("06", [10, 11], "OTS cận-trung 85mm · MAYA NÉT chính diện cầm phong bì · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA rõ mặt chính diện. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, ngồi thấp, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA gõ ngón tay vào ô chữ in trên mặt chiếc phong bì kraft",
  [("MAYA", "even, factual", 10), ("ADRIAN", "hard, clipped", 11)])

S("07", "cận-trung 85mm, cao 1m30, cách MAYA 1m5, đặt chếch bên, lấy MAYA nét và ADRIAN trong khung",
  "MAYA đứng ở nửa PHẢI khung, TẤM ẢNH CHỤP ĐOẠN ỐNG DẦU PHANH đã được rút ra khỏi phong bì và cầm trên tay, "
  "mặt ảnh hướng về phía ADRIAN. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, thấy rõ mặt.",
  "MAYA hai tay cầm tấm ảnh giơ ngang ngực, một ngón chỉ vào chỗ vết cắt trên ảnh. ADRIAN hai tay siết vành tay vịn.",
  "MAYA nhìn thẳng vào ADRIAN. ADRIAN nhìn tấm ảnh rồi nhìn lên mặt cô.",
  "MAYA — người vừa gọi tên một tội ác bằng kiến thức nghề nghiệp của mình: giọng chậm, rõ, mắt cứng. "
  "ADRIAN — nghe đúng thứ mình đã biết từ lâu nói ra bởi người khác: mặt bình, mắt tối lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN gọi tên cô",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng nửa phải khung cầm tấm ảnh", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một bước", {"MAYA": "hai tay cầm tấm ảnh, một ngón chỉ vào vết cắt",
                         "ADRIAN": "hai tay siết vành tay vịn"})
V("07", [12, 13], "cận-trung 85mm · MAYA NÉT phải cầm tấm ảnh + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA giơ tấm ảnh lên ngang ngực và chỉ vào chỗ vết cắt trên đoạn ống",
  [("MAYA", "slow, hard", 12), ("ADRIAN", "quiet, warning", 13)])

S("08", "trung 50mm, cao 1m30, cách MAYA 2m, đặt trong phòng, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, tấm ảnh đã hạ xuống ngang đùi. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. "
  "Hậu cảnh là cửa sổ tối và một góc giường đơn khung sắt trắng.",
  "MAYA một tay cầm tấm ảnh hạ xuống ngang đùi, tay kia nắm lại thành nắm. ADRIAN một tay giơ lên ngang ngực "
  "rồi hạ xuống.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa ghép xong toàn bộ câu chuyện và giận thay cho người ngồi trước mặt: giọng run một nhịp "
  "rồi vững lại, mắt đỏ. ADRIAN — chặn lại bằng số điều khoản chứ không bằng lý do: mặt bình, giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt tấm ảnh trở lại vào phong bì",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay cầm tấm ảnh hạ xuống, tay kia nắm lại",
                         "ADRIAN": "một tay giơ lên ngang ngực rồi hạ xuống"})
V("08", [14, 15], "trung 50mm hạ thấp · MAYA NÉT phải + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA hạ tấm ảnh xuống ngang đùi, ADRIAN giơ tay lên ngang ngực rồi hạ xuống",
  [("MAYA", "shaking, furious", 14), ("ADRIAN", "quiet, closing", 15)])

S("09", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m5, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh là tường vữa xanh xám nhạt và tấm gương viền gỗ mộc.",
  "ADRIAN một tay đặt lại trên vành tay vịn, các ngón duỗi ra.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người xác nhận điều khoản bằng đúng một chữ và không giải thích thêm: mặt bình, mắt tĩnh, "
  "hơi thở chậm lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay người về phía chậu nước",
  ["ADRIAN_NHA", "MAYA_ONHA"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"ADRIAN": "một tay đặt lại trên vành tay vịn",
                         "MAYA": "một tay cầm phong bì, ngoài vùng nét"})
V("09", [16, 17], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_ONHA")],
  "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA đọc lại đúng số điều khoản, ADRIAN xác nhận bằng một chữ",
  [("MAYA", "flat, reciting", 16), ("ADRIAN", "quiet, plain", 17)])

S("10", "trung 50mm, cao 1m20, cách MAYA 1m9, máy hạ thấp, MAYA đã quỳ lại cạnh chiếc xe lăn",
  "MAYA đã quỳ lại một gối ở nửa PHẢI khung, chiếc phong bì kraft đặt úp trên mặt bàn gỗ phía sau cô. "
  "ADRIAN ngồi trong xe lăn ở nửa TRÁI khung. Trên bàn có chậu nước và cuộn băng gạc.",
  "MAYA hai tay quấn một vòng băng gạc quanh ống chân ADRIAN, động tác chắc và nhanh. "
  "ADRIAN một tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống chỗ mình đang quấn băng. ADRIAN nhìn xuống MAYA.",
  "MAYA — người nuốt cơn giận xuống và quay lại làm việc, nhưng tay quấn băng chặt hơn bình thường một chút: "
  "quai hàm siết, mắt đỏ, giọng đều. ADRIAN — nhận ra cô đang giận: mày hơi chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA cắt cuộn băng gạc",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"MAYA": "quỳ một gối nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "hai tay quấn băng gạc quanh ống chân", "ADRIAN": "một tay trên vành tay vịn"})
V("10", [18, 19], "trung 50mm hạ thấp · MAYA NÉT phải quỳ quấn băng + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN mặc nguyên áo, chỉ xắn ống quần. Không có ai khác trong khung.",
  "MAYA quỳ lại và quấn băng gạc quanh ống chân ADRIAN, tay chặt hơn bình thường một chút",
  [("MAYA", "even, contained", 18), ("ADRIAN", "quiet, observing", 19)])

S("11", "cận-trung 85mm, cao 1m10, cách MAYA 1m4, máy hạ thấp ngang tầm người quỳ, lấy cả hai người",
  "MAYA quỳ ở nửa PHẢI khung, hai tay đang buộc nốt mối băng. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, "
  "đã cúi người xuống một chút về phía cô.",
  "MAYA hai tay thắt nốt mối băng rồi vuốt phẳng. ADRIAN một tay đưa xuống chạm vào tay vịn phía cô.",
  "MAYA ngẩng lên nhìn ADRIAN. ADRIAN nhìn xuống MAYA.",
  "MAYA — người thừa nhận mình đang giận nhưng nói rõ giận ai: giọng chắc, mắt thẳng. "
  "ADRIAN — gọi tên cô lần nữa, lần này bằng một giọng khác hẳn: mắt dịu, khoé môi động.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đứng thẳng dậy",
  ["MAYA_ONHA", "ADRIAN_NHA"], "giữa gian phòng, cạnh chiếc xe lăn",
  {"MAYA": "quỳ nửa phải khung", "ADRIAN": "ngồi xe lăn nửa trái khung, cúi xuống một chút"},
  "sát cạnh nhau", {"MAYA": "hai tay thắt nốt mối băng", "ADRIAN": "một tay đưa xuống chạm vào tay vịn"})
V("11", [20, 21, 22], "cận-trung 85mm hạ thấp · MAYA NÉT phải quỳ + ADRIAN NÉT trái ngồi xe lăn cúi xuống",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA thắt nốt mối băng và vuốt phẳng, ADRIAN cúi xuống một chút về phía cô",
  [("MAYA", "firm, honest", 20), ("ADRIAN", "quiet, softer", 21), ("MAYA", "gentle, tired", 22)])

S("12", "two-shot cận-trung 85mm, cao 1m20, cách MAYA 1m6, máy hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đã đứng lên và đứng ở nửa PHẢI khung, một tay cầm chiếc chậu inox. ADRIAN ngồi trong xe lăn ở nửa TRÁI "
  "khung, mặt ngước lên. Trên bàn gỗ phía sau có một đĩa thức ăn còn nguyên và chiếc phong bì kraft úp mặt.",
  "MAYA một tay bê chiếc chậu inox, tay kia chỉ về phía đĩa thức ăn trên bàn. ADRIAN một tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người cảm ơn không phải vì được chăm mà vì không bị hỏi: giọng rất nhỏ, mắt dịu hẳn, "
  "lần đầu trong cả cảnh. MAYA — nhận lời cảm ơn và lập tức chuyển sang việc tiếp theo: khoé môi kéo một chút.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt đĩa thức ăn xuống trước mặt anh",
  ["MAYA_ONHA", "ADRIAN_NHA", "PROP_HOSO"], "giữa gian phòng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng nửa phải khung bê chậu inox", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay bê chậu inox, tay kia chỉ về đĩa thức ăn",
                         "ADRIAN": "một tay trên vành tay vịn"})
V("12", [23, 24], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải đứng bê chậu + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_ONHA"), ("ADRIAN", "ADRIAN_NHA")],
  "MAYA và ADRIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "ADRIAN ngước lên nói rất nhỏ, MAYA chỉ về phía đĩa thức ăn còn nguyên trên bàn",
  [("ADRIAN", "quiet, sincere", 23), ("MAYA", "warm, brisk", 24)])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m50, cách MAYA 5m, đặt ở góc phòng phía cửa nhìn chéo vào bàn gỗ",
  "Trong gian phòng sáng đèn vàng: ADRIAN ngồi trong xe lăn kéo sát bàn gỗ vuông, trước mặt là đĩa thức ăn "
  "đã ăn dở. MAYA ngồi trên chiếc ghế gỗ đối diện anh qua mặt bàn, hai tay ôm một cốc nước. "
  "Chiếc phong bì kraft nằm úp ở mép bàn.",
  "ADRIAN một tay cầm dĩa. MAYA hai tay ôm cốc nước trước ngực.",
  "ADRIAN nhìn xuống đĩa. MAYA nhìn ADRIAN.",
  "ADRIAN — người đang ăn vì có người bắt mình ăn: mặt bình, vai đã buông. "
  "MAYA — ngồi canh cho tới khi anh ăn hết: mắt còn đỏ, khoé môi kéo lên một chút.",
  "đúng khoảnh khắc ngay TRƯỚC khi ngọn đèn trần đung đưa dừng hẳn",
  ["ADRIAN_NHA", "MAYA_ONHA", "PROP_HOSO"], "giữa gian phòng nhà cổng, hai bên bàn gỗ vuông",
  {"ADRIAN": "ngồi xe lăn sát bàn gỗ", "MAYA": "ngồi ghế gỗ đối diện qua mặt bàn"},
  "cách nhau một mặt bàn", {"ADRIAN": "một tay cầm dĩa", "MAYA": "hai tay ôm cốc nước trước ngực"})
B("B2", "Khép cảnh. ADRIAN ăn nốt đĩa thức ăn, MAYA ngồi đối diện canh anh; chiếc phong bì nằm úp ở mép bàn.",
  "toàn cảnh 24mm · ADRIAN NÉT ngồi xe lăn cạnh bàn + MAYA NÉT ngồi ghế đối diện · không có ai khác",
  [("ADRIAN", "ADRIAN_NHA"), ("MAYA", "MAYA_ONHA")],
  "ADRIAN và MAYA rõ mặt, ngồi hai bên chiếc bàn gỗ vuông. Không có người nào khác trong khung.",
  "hai người vừa đi qua một chuyện lẽ ra phải làm họ xa nhau, và kết quả là họ ngồi ăn cùng một bàn; "
  "cái phong bì thì nằm úp ở mép bàn, chưa ai nhắc lại.",
  "ADRIAN ăn thêm một miếng; MAYA đẩy đĩa lại gần anh hơn một chút rồi ngồi yên; ngọn đèn trần bóng đơn "
  "đung đưa chậm dần rồi đứng lại; ngoài cửa sổ là đêm.",
  "Ambient tiếng gỗ nhà cũ và tiếng gió ngoài cửa sổ, SFX tiếng dĩa chạm đĩa sứ rất khẽ.",
  nhac("NÂNG", "Đây là lần đầu hai người ngồi cùng bàn như một gia đình — nhạc được phép ấm lên, nhưng vẫn phải mộc.",
       "Warm folk at 80 BPM; acoustic guitar picking a gentle rising figure, a female alto entering after eight "
       "seconds low and close, a cello joining under the last phrase; brushes on a snare very light; the pull is "
       "when the guitar lands on one warm chord and holds; lyrics about eating dinner with somebody you were paid "
       "to look after; warm analog mix, female vocal, guitar, cello, tender",
       "Instrumental at 78 BPM; acoustic guitar arpeggio with a cello line rising underneath, a soft brushed snare "
       "entering halfway, one warm held chord near the end then thinning to guitar alone; "
       "warm analog mix, guitar, cello, brushes, tender"),
  dur=8)
