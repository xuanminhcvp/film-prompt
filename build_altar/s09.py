# -*- coding: utf-8 -*-
"""SCENE 9 — KHOA HỒI SỨC ICU, BUỒNG 4 (đêm). Giường 12."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S9", "REF_ICU_DEM", qc=qc.S9)

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 5m, đặt ở cửa buồng bệnh nhìn chếch dọc theo giường",
  "HELEN nằm trên giường bệnh giữa phòng, mắt nhắm, chăn kéo ngang ngực. MAYA đứng bên thành giường phía đầu, "
  "vừa vào ca và còn khoác túi. Buồng bệnh không có ai khác.",
  "MAYA một tay đặt lên thành chắn kim loại của giường, tay kia còn giữ quai chiếc túi vải đeo vai. "
  "HELEN hai tay đặt xuôi trên chăn.",
  "MAYA nhìn xuống mặt HELEN. HELEN nhắm mắt.",
  "MAYA — người vừa hết một ngày dài và tới đây trước cả giờ vào ca: mặt mềm hẳn ra so với mọi cảnh trước, "
  "mắt hơi ướt, vai buông. HELEN — đang hôn mê, mặt hoàn toàn tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt chiếc túi xuống ghế và bắt đầu làm việc",
  ["MAYA_SCRUB", "HELEN"], "cạnh giường bệnh, phía đầu giường",
  {"MAYA": "đứng bên thành giường phía đầu", "HELEN": "nằm trên giường bệnh, mắt nhắm"},
  "sát cạnh nhau", {"MAYA": "một tay trên thành chắn giường, tay kia giữ quai túi",
                    "HELEN": "hai tay đặt xuôi trên chăn"})
B("B1", "Mở cảnh. Ca đêm ở khoa hồi sức. MAYA vào buồng giường 12, mẹ cô vẫn nằm đó, mắt nhắm.",
  "toàn cảnh 24mm · MAYA NÉT đứng bên thành giường + HELEN NÉT nằm trên giường · không có ai khác",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "MAYA rõ mặt đứng bên giường, HELEN rõ mặt nằm trên giường, mắt nhắm. Không có người nào khác trong khung.",
  "đây là chỗ duy nhất trong cả bộ phim mà người phụ nữ này được phép mềm ra, và người duy nhất thấy điều đó "
  "thì đang hôn mê.",
  "MAYA đặt túi xuống ghế, xoa hai tay cho ấm rồi kéo lại mép chăn cho ngay ngắn; màn hình theo dõi trên đầu "
  "giường chạy một đường sóng đều; ngoài cửa sổ là đêm.",
  "Ambient tiếng bíp đều của máy theo dõi và tiếng máy lạnh, SFX tiếng vải chăn kéo lại.",
  nhac("NGHỈ", "Cả phim đang dồn; đây là chỗ cho khán giả thở cùng nhân vật trong căn phòng duy nhất cô thấy an toàn.",
       "Ambient lullaby at 54 BPM; a female alto humming wordlessly very close to the mic over a felt piano placing "
       "single notes, one line of lyric only at the very end; no drums, no bass; the pull is when the humming stops "
       "and the piano finishes alone; lyrics about talking to someone who cannot answer; extremely soft late-night "
       "mix, female vocal, ambient, piano, tender",
       "Ambient instrumental at 52 BPM; one warm pad breathing very slowly, a felt-piano phrase repeating with heavy "
       "sustain and getting quieter each pass, a faint monitor-like pulse underneath, no percussion, simply fading; "
       "extremely soft mix, piano, pad, minimal, sleepy"),
  dur=8)

# ── BÊN GIƯỜNG 12 ──
S("01", "cận-trung 85mm, cao 1m20, cách MAYA 1m6, máy hạ thấp bên thành giường, lấy MAYA nét và HELEN trong khung",
  "MAYA ngồi trên chiếc ghế bọc nhựa xanh kéo sát thành giường ở nửa PHẢI khung. HELEN nằm ở nửa TRÁI khung, "
  "mặt nghiêng về phía cô, mắt nhắm. Màn hình theo dõi ở đầu giường sáng xanh nhạt trong khung.",
  "MAYA một tay nắm bàn tay HELEN đặt trên chăn, tay kia vuốt phẳng mép chăn. HELEN hai tay đặt xuôi trên chăn.",
  "MAYA nhìn xuống mặt HELEN, thỉnh thoảng liếc lên màn hình theo dõi. HELEN nhắm mắt.",
  "MAYA — người kể chuyện với mẹ mình bằng giọng báo cáo vì đó là cách duy nhất cô không khóc: giọng nhẹ, "
  "khoé môi động, mắt ướt. HELEN — mặt hoàn toàn tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng gọi tên cô từ phía cửa buồng",
  ["MAYA_SCRUB", "HELEN"], "cạnh giường bệnh, MAYA ngồi ghế sát thành giường",
  {"MAYA": "ngồi ghế sát thành giường nửa phải khung", "HELEN": "nằm trên giường nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay nắm bàn tay HELEN, tay kia vuốt mép chăn",
                    "HELEN": "hai tay đặt xuôi trên chăn"})
V("01", [0], "cận-trung 85mm hạ thấp · MAYA NÉT phải ngồi cạnh giường + HELEN NÉT trái nằm trên giường, mắt nhắm",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "MAYA rõ mặt ngồi cạnh giường, HELEN rõ mặt nằm trên giường và NHẮM MẮT suốt clip, không cử động. "
  "Không có ai khác trong khung.",
  "MAYA nắm bàn tay mẹ và đọc các chỉ số cho bà nghe như đọc một bản tin",
  [("MAYA", "gentle, matter-of-fact", 0)], [("HELEN", "silent, unconscious, eyes closed")])

S("02", "trung 50mm, cao 1m30, cách MAYA 2m2, đặt phía cửa buồng nhìn vào, lấy cả ba người",
  "MAYA ngồi ở nửa PHẢI khung cạnh giường. HELEN nằm trên giường ở giữa khung, mắt nhắm. NURSE DIANE đứng ở "
  "nửa TRÁI khung ngay trong cửa trượt, một tay còn trên khung cửa.",
  "NURSE DIANE một tay đặt trên khung cửa trượt, tay kia cầm một bìa kẹp bệnh án. MAYA một tay còn nắm tay HELEN. "
  "HELEN hai tay đặt xuôi trên chăn.",
  "NURSE DIANE nhìn MAYA. MAYA quay đầu nhìn NURSE DIANE. HELEN nhắm mắt.",
  "NURSE DIANE — người vừa nhắc giờ vào ca nhưng thật ra đang nhắc bạn mình nghỉ tay: giọng ấm, mày hơi chau. "
  "MAYA — không rời tay khỏi giường: mặt bình, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi NURSE DIANE bước hẳn vào trong buồng",
  ["MAYA_SCRUB", "HELEN", "NURSE DIANE"], "buồng bệnh, từ cửa trượt tới thành giường",
  {"MAYA": "ngồi cạnh giường nửa phải khung", "HELEN": "nằm trên giường giữa khung",
   "NURSE DIANE": "đứng trong cửa trượt nửa trái khung"},
  "NURSE DIANE cách giường ba mét",
  {"MAYA": "một tay nắm tay HELEN", "HELEN": "hai tay xuôi trên chăn",
   "NURSE DIANE": "một tay trên khung cửa, tay kia cầm bìa kẹp bệnh án"})
V("02", [1, 2, 3, 4], "trung 50mm · NURSE DIANE NÉT trái trong cửa + HELEN NÉT giữa nằm trên giường + MAYA NÉT phải ngồi cạnh giường",
  [("NURSE DIANE", "NURSE DIANE"), ("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "NURSE DIANE và MAYA rõ mặt, HELEN rõ mặt nằm trên giường và NHẮM MẮT suốt clip, không cử động.",
  "NURSE DIANE dừng lại ở cửa trượt, MAYA quay đầu lại nhưng không rời tay khỏi giường",
  [("NURSE DIANE", "warm, reminding", 1), ("MAYA", "quiet, firm", 2),
   ("NURSE DIANE", "gentle, offering", 3), ("MAYA", "quiet, final", 4)])

S("03", "trung 50mm, cao 1m50, cách NURSE PAULA 2m, đặt ngoài hành lang nhìn vào chỗ hai điều dưỡng đứng cạnh cửa buồng",
  "NURSE PAULA đứng ở nửa PHẢI khung ngay ngoài cửa trượt buồng bệnh, đã ghé sát vào NURSE DIANE. NURSE DIANE "
  "đứng ở nửa TRÁI khung, người quay nửa về phía trong buồng. Qua khe cửa trượt mở hé phía sau thấy một mảng "
  "ánh sáng ấm của buồng bệnh.",
  "NURSE PAULA một tay khum lại che một bên miệng, tay kia bám vào cạnh cửa. NURSE DIANE một tay giơ lên "
  "ra hiệu nhỏ tiếng.",
  "NURSE PAULA nhìn qua khe cửa vào trong buồng. NURSE DIANE nhìn thẳng vào mặt NURSE PAULA.",
  "NURSE PAULA — người đang kể một chuyện hay mà không nghĩ mình đang làm gì: mắt sáng, môi hé, người chồm tới. "
  "NURSE DIANE — khó chịu vì bạn mình đang đứng nói ngay ngoài cửa: mày chau, giọng gằn xuống rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi NURSE PAULA hạ bàn tay khỏi miệng",
  ["NURSE PAULA", "NURSE DIANE"], "hành lang ngay ngoài cửa trượt buồng bệnh",
  {"NURSE PAULA": "đứng nửa phải khung sát cửa trượt", "NURSE DIANE": "đứng nửa trái khung"},
  "sát cạnh nhau", {"NURSE PAULA": "một tay khum che miệng, tay kia bám cạnh cửa",
                    "NURSE DIANE": "một tay giơ lên ra hiệu nhỏ tiếng"})
V("03", [5, 6], "trung 50mm · NURSE PAULA NÉT phải sát cửa + NURSE DIANE NÉT trái · không thấy ai trong buồng",
  [("NURSE PAULA", "NURSE PAULA"), ("NURSE DIANE", "NURSE DIANE")],
  "NURSE PAULA và NURSE DIANE, cả hai rõ mặt ngoài hành lang. Không thấy ai khác trong khung.",
  "NURSE PAULA ghé sát vào NURSE DIANE, một tay khum che miệng",
  [("NURSE PAULA", "eager, gossiping", 5), ("NURSE DIANE", "low, warning", 6)])

S("04", "cận-trung 85mm, cao 1m50, cách NURSE PAULA 1m6, đặt ngoài hành lang, lấy PAULA nét và DIANE trong khung",
  "NURSE PAULA đứng ở nửa PHẢI khung, đã bỏ tay khỏi miệng và nói bình thường. NURSE DIANE đứng ở nửa TRÁI khung, "
  "người đã xoay hẳn về phía bà. Hậu cảnh là tường hành lang sơn xanh bạc hà và khe cửa trượt sáng.",
  "NURSE PAULA hai tay khoanh trước ngực. NURSE DIANE một tay đặt lên cánh tay NURSE PAULA.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "NURSE PAULA — người nói ra con số như nói về giá một chiếc xe: mắt tròn, giọng hào hứng. "
  "NURSE DIANE — gọi tên bạn mình một tiếng để chặn lại: quai hàm siết, mắt cứng.",
  "đúng khoảnh khắc ngay TRƯỚC khi NURSE PAULA nhún vai",
  ["NURSE PAULA", "NURSE DIANE"], "hành lang ngay ngoài cửa trượt buồng bệnh",
  {"NURSE PAULA": "đứng nửa phải khung", "NURSE DIANE": "đứng nửa trái khung"},
  "sát cạnh nhau", {"NURSE PAULA": "hai tay khoanh trước ngực",
                    "NURSE DIANE": "một tay đặt lên cánh tay NURSE PAULA"})
V("04", [7, 8], "cận-trung 85mm · NURSE PAULA NÉT phải + NURSE DIANE NÉT trái · ngoài hành lang",
  [("NURSE PAULA", "NURSE PAULA"), ("NURSE DIANE", "NURSE DIANE")],
  "NURSE PAULA và NURSE DIANE, cả hai rõ mặt ngoài hành lang. Không thấy ai khác trong khung.",
  "NURSE PAULA khoanh tay lại và nói bình thường, NURSE DIANE đặt tay lên cánh tay bà",
  [("NURSE PAULA", "excited, gossiping", 7), ("NURSE DIANE", "low, cutting her off", 8)])

S("05", "cận-trung 85mm, cao 1m50, cách NURSE DIANE 1m6, máy sau vai PHẢI của NURSE PAULA; vai và gáy bà chiếm rìa phải, out nét",
  "NURSE DIANE đứng chính diện chiếm phần lớn khung ngoài hành lang. NURSE PAULA chỉ còn là vai và gáy ở rìa "
  "PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng NURSE DIANE là hành lang và một xe đẩy dụng cụ inox.",
  "NURSE DIANE hai tay buông xuống, một tay còn cầm bìa kẹp bệnh án ép vào đùi.",
  "NURSE DIANE nhìn thẳng vào mặt NURSE PAULA.",
  "NURSE DIANE — người nghe câu đùa đó và không cười một chút nào: mặt cứng lại, mắt không chớp, môi mím.",
  "đúng khoảnh khắc ngay TRƯỚC khi NURSE DIANE quay lưng đi vào buồng bệnh",
  ["NURSE DIANE", "NURSE PAULA"], "hành lang ngay ngoài cửa trượt buồng bệnh",
  {"NURSE DIANE": "đứng chính diện giữa khung", "NURSE PAULA": "vai và gáy tiền cảnh phải"},
  "sát cạnh nhau", {"NURSE DIANE": "hai tay buông, một tay cầm bìa kẹp bệnh án",
                    "NURSE PAULA": "hai tay khoanh trước ngực, ngoài vùng nét"})
V("05", [9], "OTS cận-trung 85mm · NURSE DIANE NÉT chính diện · vai và gáy NURSE PAULA tiền cảnh phải out nét",
  [("NURSE DIANE", "NURSE DIANE"), ("NURSE PAULA", "NURSE PAULA")],
  "NURSE DIANE rõ mặt chính diện. NURSE PAULA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "NURSE PAULA nói nốt câu đùa của mình, NURSE DIANE không cười",
  [("NURSE PAULA", "light, joking", 9)], [("NURSE DIANE", "silent, stone-faced")],
  ketclip="Cuối clip, NURSE DIANE quay lưng bỏ NURSE PAULA lại ngoài hành lang và bước vào trong buồng bệnh, "
          "dừng lại ở cuối giường. Clip dừng đúng lúc bà dừng chân.")

S("06", "trung 50mm, cao 1m30, cách MAYA 2m, đặt trong buồng bệnh, lấy cả ba người",
  "MAYA ngồi ở nửa PHẢI khung cạnh giường, đã kéo chăn xuống ngang đùi HELEN và đang chuẩn bị trở người cho bà. "
  "HELEN nằm ở giữa khung, mắt nhắm. NURSE DIANE đứng ở nửa TRÁI khung ở cuối giường.",
  "MAYA một tay đỡ dưới vai HELEN, tay kia chìa ra phía NURSE DIANE. NURSE DIANE một tay cầm một tuýp kem "
  "trên bàn đẩy. HELEN hai tay đặt xuôi.",
  "MAYA nhìn vào gót chân trái của HELEN. NURSE DIANE nhìn MAYA. HELEN nhắm mắt.",
  "MAYA — người không đáp lại chuyện vừa nghe ngoài cửa và chỉ làm nốt việc của mình: giọng nghiệp vụ, "
  "mắt tập trung. NURSE DIANE — muốn bạn mình được phép giận: mày chau, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi tuýp kem được đặt vào tay MAYA",
  ["MAYA_SCRUB", "HELEN", "NURSE DIANE"], "cạnh giường bệnh",
  {"MAYA": "ngồi cạnh giường nửa phải khung", "HELEN": "nằm trên giường giữa khung",
   "NURSE DIANE": "đứng ở cuối giường nửa trái khung"},
  "NURSE DIANE cách hai bước",
  {"MAYA": "một tay đỡ dưới vai HELEN, tay kia chìa ra", "HELEN": "hai tay đặt xuôi trên chăn",
   "NURSE DIANE": "một tay cầm tuýp kem"})
V("06", [10, 11], "trung 50mm · MAYA NÉT phải ngồi cạnh giường + HELEN NÉT giữa nằm trên giường + NURSE DIANE NÉT trái ở cuối giường",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN"), ("NURSE DIANE", "NURSE DIANE")],
  "MAYA và NURSE DIANE rõ mặt, HELEN rõ mặt nằm trên giường và NHẮM MẮT suốt clip, không cử động.",
  "MAYA đỡ vai mẹ để trở người và chìa tay xin tuýp kem, NURSE DIANE cầm nó lên",
  [("MAYA", "clinical, even", 10), ("NURSE DIANE", "gentle, careful", 11)])

S("07", "cận 85mm, cao 1m10, cách MAYA 1m2, máy hạ thấp sát thành giường, lấy MAYA nét và một mảng vai NURSE DIANE rìa trái",
  "MAYA ngồi chiếm phần lớn khung từ ngực trở lên, cúi xuống phía chân giường. Ở rìa TRÁI khung thấy một mảng vai "
  "áo scrub của NURSE DIANE, out nét. Ở rìa DƯỚI khung thấy mép chăn trắng và bàn chân HELEN dưới chăn.",
  "MAYA một tay còn chìa ra chờ, các ngón khép lại rồi mở ra một lần.",
  "MAYA nhìn xuống gót chân trái của HELEN.",
  "MAYA — người đang cố giữ mọi thứ ở mức một ca trực bình thường: giọng đều, mắt tập trung, quai hàm siết "
  "chặt hơn cần thiết.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng người vọng vào từ ngoài hành lang",
  ["MAYA_SCRUB", "NURSE DIANE", "HELEN"], "cạnh giường bệnh, phía cuối giường",
  {"MAYA": "ngồi cúi xuống giữa khung", "NURSE DIANE": "một mảng vai áo scrub ở rìa trái",
   "HELEN": "chỉ thấy mép chăn và bàn chân ở rìa dưới khung"},
  "sát nhau", {"MAYA": "một tay chìa ra chờ, các ngón khép rồi mở",
               "NURSE DIANE": "một tay cầm tuýp kem, ngoài vùng nét", "HELEN": "nằm yên dưới chăn"})
V("07", [12], "cận 85mm hạ thấp · MAYA NÉT cúi xuống · một mảng vai NURSE DIANE rìa trái out nét · HELEN chỉ thấy chăn và bàn chân rìa dưới",
  [("MAYA", "MAYA_SCRUB"), ("NURSE DIANE", "NURSE DIANE"), ("HELEN", "HELEN")],
  "MAYA rõ mặt. NURSE DIANE chỉ thấy MỘT MẢNG VAI ở rìa trái, out nét. HELEN chỉ thấy mép chăn và bàn chân "
  "ở rìa dưới khung, KHÔNG thấy mặt. Không ai quay mặt về camera ngoài MAYA.",
  "MAYA giữ nguyên bàn tay chìa ra chờ và nhắc lại yêu cầu của mình",
  [("MAYA", "even, insistent", 12)], [("NURSE DIANE", "silent, handing it over")])

S("08", "cận-trung 85mm, cao 1m50, cách NURSE PAULA 1m6, đặt ngoài hành lang lấy PAULA nét và DIANE trong khung",
  "NURSE PAULA đứng ở nửa TRÁI khung ngoài hành lang, một tay hất về phía cửa buồng bệnh. NURSE DIANE đứng ở nửa "
  "PHẢI khung, đã quay hẳn người ra phía bà, tay còn cầm tuýp kem.",
  "NURSE PAULA một tay hất về phía cửa buồng, tay kia chống hông. NURSE DIANE một tay cầm tuýp kem siết chặt lại.",
  "NURSE PAULA nhìn về phía cửa buồng bệnh. NURSE DIANE nhìn NURSE PAULA.",
  "NURSE PAULA — người lấy sự im lặng của người khác làm bằng chứng: mắt sáng, khoé môi kéo. "
  "NURSE DIANE — siết chặt tuýp kem trong tay: quai hàm siết, mắt lạnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi NURSE DIANE quay hẳn vào trong buồng",
  ["NURSE PAULA", "NURSE DIANE"], "hành lang ngay ngoài cửa trượt buồng bệnh",
  {"NURSE PAULA": "đứng nửa trái khung", "NURSE DIANE": "đứng nửa phải khung"},
  "sát cạnh nhau", {"NURSE PAULA": "một tay hất về phía cửa buồng, tay kia chống hông",
                    "NURSE DIANE": "một tay siết chặt tuýp kem"})
V("08", [13], "cận-trung 85mm · NURSE PAULA NÉT trái + NURSE DIANE NÉT phải · ngoài hành lang",
  [("NURSE PAULA", "NURSE PAULA"), ("NURSE DIANE", "NURSE DIANE")],
  "NURSE PAULA và NURSE DIANE, cả hai rõ mặt ngoài hành lang. Không thấy ai khác trong khung.",
  "NURSE PAULA hất tay về phía cửa buồng bệnh và nói với NURSE DIANE",
  [("NURSE PAULA", "smug, certain", 13)], [("NURSE DIANE", "silent, gripping the tube")])

S("09", "cận-trung 85mm, cao 1m20, cách MAYA 1m5, máy hạ thấp bên thành giường, lấy MAYA nét và HELEN trong khung",
  "MAYA ngồi ở nửa PHẢI khung, đã bôi kem xong và kéo chăn lên lại cho HELEN. HELEN nằm ở nửa TRÁI khung, "
  "mắt nhắm. Hậu cảnh là màn hình theo dõi sáng xanh và cột truyền dịch inox.",
  "MAYA một tay giữ bàn tay HELEN, tay kia vuốt lại mép chăn ngang ngực bà.",
  "MAYA nhìn xuống mặt HELEN.",
  "MAYA — người đang nói chuyện với mẹ về một vết đỏ ở gót chân vì đó là thứ duy nhất cô sửa được trong cả "
  "cuộc đời mình lúc này: giọng nhỏ dần, mắt đỏ, một giọt nước mắt chưa rơi.",
  "đúng khoảnh khắc ngay TRƯỚC khi các khớp ngón tay MAYA siết trắng lại",
  ["MAYA_SCRUB", "HELEN"], "cạnh giường bệnh, MAYA ngồi ghế sát thành giường",
  {"MAYA": "ngồi cạnh giường nửa phải khung", "HELEN": "nằm trên giường nửa trái khung"},
  "sát cạnh nhau", {"MAYA": "một tay giữ bàn tay HELEN, tay kia vuốt mép chăn",
                    "HELEN": "hai tay đặt xuôi trên chăn"})
V("09", [14], "cận-trung 85mm hạ thấp · MAYA NÉT phải ngồi cạnh giường + HELEN NÉT trái nằm trên giường, mắt nhắm",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "MAYA rõ mặt ngồi cạnh giường, HELEN rõ mặt nằm trên giường và NHẮM MẮT suốt clip, không cử động. "
  "Không có ai khác trong khung.",
  "MAYA vuốt lại mép chăn cho mẹ và nói xuống mặt bà, bàn tay siết chặt dần",
  [("MAYA", "quiet, breaking underneath", 14)], [("HELEN", "silent, unconscious, eyes closed")])

S("10", "trung 50mm, cao 1m30, cách MAYA 2m, đặt trong buồng bệnh lấy cả ba người",
  "MAYA ngồi ở nửa PHẢI khung cạnh giường, bàn tay đang nắm chặt bàn tay HELEN. HELEN nằm ở giữa khung, mắt nhắm. "
  "NURSE DIANE đứng ở nửa TRÁI khung sát thành giường bên kia, đã cúi người xuống.",
  "NURSE DIANE một tay đưa ra đặt lên cổ tay MAYA. MAYA một tay nắm chặt bàn tay HELEN, các khớp ngón trắng ra. "
  "HELEN hai tay đặt xuôi.",
  "NURSE DIANE nhìn xuống bàn tay MAYA rồi nhìn mặt cô. MAYA nhìn xuống bàn tay mình. HELEN nhắm mắt.",
  "NURSE DIANE — người nhìn thấy chỗ vỡ và gọi nó ra bằng một chi tiết rất nhỏ: giọng ấm, mắt lo. "
  "MAYA — không hề biết tay mình đang siết: mắt mở, giọng ngơ ngác.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nới các ngón tay ra",
  ["MAYA_SCRUB", "HELEN", "NURSE DIANE"], "cạnh giường bệnh, hai bên thành giường",
  {"MAYA": "ngồi cạnh giường nửa phải khung", "HELEN": "nằm trên giường giữa khung",
   "NURSE DIANE": "đứng cúi xuống bên thành giường kia, nửa trái khung"},
  "hai người sát hai bên giường",
  {"MAYA": "một tay nắm chặt bàn tay HELEN", "HELEN": "hai tay đặt xuôi trên chăn",
   "NURSE DIANE": "một tay đặt lên cổ tay MAYA"})
V("10", [15, 16], "trung 50mm · NURSE DIANE NÉT trái cúi xuống + HELEN NÉT giữa nằm trên giường + MAYA NÉT phải ngồi cạnh giường",
  [("NURSE DIANE", "NURSE DIANE"), ("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "NURSE DIANE và MAYA rõ mặt, HELEN rõ mặt nằm trên giường và NHẮM MẮT suốt clip, không cử động.",
  "NURSE DIANE cúi xuống đặt tay lên cổ tay MAYA",
  [("NURSE DIANE", "warm, careful", 15), ("MAYA", "dazed, small", 16)])

S("11", "cận 85mm, cao 1m20, cách MAYA 1m1, máy hạ thấp bên thành giường, lấy MAYA nét và một mảng vai NURSE DIANE rìa trái",
  "MAYA ngồi chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung thấy một mảng vai áo scrub và bàn tay của "
  "NURSE DIANE đang đặt trên cổ tay cô, out nét. Ở rìa DƯỚI khung thấy mép chăn trắng và bàn tay HELEN.",
  "MAYA một tay còn nắm bàn tay HELEN, các ngón bắt đầu nới ra rất chậm.",
  "MAYA nhìn xuống hai bàn tay đang nắm nhau.",
  "MAYA — người vừa được cho phép buông tay ra một giây và thấy điều đó khó hơn mọi thứ khác trong ngày: "
  "mắt ướt hẳn, môi run một nhịp, KHÔNG khóc thành tiếng.",
  "đúng khoảnh khắc ngay TRƯỚC khi các ngón tay MAYA rời hẳn khỏi bàn tay mẹ",
  ["MAYA_SCRUB", "NURSE DIANE", "HELEN"], "cạnh giường bệnh",
  {"MAYA": "ngồi chính diện giữa khung", "NURSE DIANE": "một mảng vai và bàn tay ở rìa trái",
   "HELEN": "chỉ thấy mép chăn và bàn tay ở rìa dưới khung"},
  "sát nhau", {"MAYA": "một tay nắm bàn tay HELEN, các ngón nới ra chậm",
               "NURSE DIANE": "một tay đặt trên cổ tay MAYA, ngoài vùng nét", "HELEN": "bàn tay nằm ngửa trên chăn"})
V("11", [17], "cận 85mm hạ thấp · MAYA NÉT chính diện · một mảng vai và bàn tay NURSE DIANE rìa trái out nét · HELEN chỉ thấy bàn tay rìa dưới",
  [("MAYA", "MAYA_SCRUB"), ("NURSE DIANE", "NURSE DIANE"), ("HELEN", "HELEN")],
  "MAYA rõ mặt. NURSE DIANE chỉ thấy MỘT MẢNG VAI và bàn tay ở rìa trái, out nét. HELEN chỉ thấy bàn tay và "
  "mép chăn ở rìa dưới khung, KHÔNG thấy mặt.",
  "NURSE DIANE giữ nguyên bàn tay trên cổ tay MAYA và nói rất khẽ",
  [("NURSE DIANE", "soft, coaxing", 17)], [("MAYA", "silent, eyes filling, letting go")])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 5m, đặt ở cửa buồng bệnh nhìn chếch dọc theo giường",
  "Buồng bệnh chỉ còn hai người: HELEN nằm trên giường, mắt nhắm, chăn đã kéo phẳng. MAYA ngồi trên chiếc ghế "
  "nhựa xanh kéo sát thành giường, người gập về phía trước, trán gần chạm mép chăn.",
  "MAYA hai tay đặt trên mép giường, trán tựa lên mu bàn tay mình. HELEN hai tay đặt xuôi trên chăn.",
  "MAYA nhìn xuống mặt chăn trước trán mình. HELEN nhắm mắt.",
  "MAYA — người vừa được cho phép buông tay ra và ngay lập tức gục xuống: vai rung một nhịp, mặt khuất, "
  "KHÔNG khóc thành tiếng. HELEN — mặt hoàn toàn tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA ngẩng đầu lên khỏi mép giường",
  ["MAYA_SCRUB", "HELEN"], "buồng bệnh giường 12, MAYA ngồi ghế sát thành giường",
  {"MAYA": "ngồi ghế gập người về phía giường", "HELEN": "nằm trên giường, mắt nhắm"},
  "sát cạnh nhau", {"MAYA": "hai tay trên mép giường, trán tựa lên mu bàn tay",
                    "HELEN": "hai tay đặt xuôi trên chăn"})
B("B2", "Khép cảnh. Buồng bệnh chỉ còn hai mẹ con. MAYA gục trán xuống mép giường, mẹ cô vẫn nhắm mắt.",
  "toàn cảnh 24mm · MAYA NÉT ngồi gập người bên giường + HELEN NÉT nằm trên giường, mắt nhắm · không có ai khác",
  [("MAYA", "MAYA_SCRUB"), ("HELEN", "HELEN")],
  "MAYA và HELEN rõ mặt. HELEN nằm trên giường và NHẮM MẮT suốt clip, không cử động. "
  "Không có người nào khác trong khung.",
  "cả ngày hôm nay cô không được phép gãy ở bất cứ đâu; đây là căn phòng duy nhất cô làm được điều đó, "
  "và người duy nhất ở đây thì không thấy.",
  "MAYA gục trán xuống mu bàn tay mình, vai rung một nhịp rồi im; màn hình theo dõi chạy một đường sóng đều; "
  "ngoài cửa sổ, đèn thành phố nhấp nháy rất xa.",
  "Ambient tiếng bíp đều của máy theo dõi và tiếng máy lạnh, SFX tiếng ghế nhựa cọ nhẹ trên sàn vinyl.",
  nhac("KÌM", "Cô đang cố không phát ra tiếng nào — nhạc phải nhỏ hơn nỗi đau thật, đúng như cách cô đang nén.",
       "Soul ballad at 58 BPM with a female alto sung very close to the mic, almost whispered; a single cello under "
       "the voice, no drums, no bass; one held note at the midpoint then straight back down; lyrics about breaking "
       "quietly in the only room where nobody can see you; dry intimate night mix, female vocal, cello, restrained",
       "Chamber instrumental at 56 BPM; a solo cello playing a slow descending figure, a felt piano placing one note "
       "every four bars, no percussion, no build, fading before it resolves; very quiet night mix, cello, piano, minimal"),
  dur=10)
