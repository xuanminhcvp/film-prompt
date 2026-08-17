# -*- coding: utf-8 -*-
"""SCENE 24 — BẬC THỀM NHÀ THỜ (chập tối). Trả lại mười một nghìn đô."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S24", "REF_BACTHEM_CHAPTOI", qc=qc.S24)

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách VANESSA 12m, đặt dưới lòng đường nhìn chếch lên bậc thềm",
  "Trên dãy bậc đá trước cửa nhà thờ, VANESSA đang bị dẫn xuống, hai tay BỊ CÒNG ra sau lưng. REPORTER đứng ở chân bậc "
  "chĩa micro lên. Dưới lòng đường là hai xe tin tức và hai xe cảnh sát bật đèn hiệu nhấp nháy.",
  "VANESSA hai tay bị còng ra sau lưng, đầu cúi. REPORTER một tay giơ micro lên, tay kia giữ dây tai nghe.",
  "VANESSA nhìn xuống mặt bậc đá. REPORTER nhìn thẳng vào VANESSA.",
  "VANESSA — người đi xuống chính dãy bậc mà bốn tiếng trước cô đi lên trong váy cưới: đầu cúi, tóc xoã, "
  "mặt trắng. REPORTER — đang săn khung hình lớn nhất đời mình: mắt sáng, người chồm tới.",
  "đúng khoảnh khắc ngay TRƯỚC khi đèn pha truyền hình quét lên mặt VANESSA",
  ["VANESSA_CODAUBAN", "REPORTER"], "dãy bậc đá trước cửa nhà thờ",
  {"VANESSA": "bị dẫn xuống bậc thềm, hai tay bị còng ra sau lưng", "REPORTER": "đứng ở chân bậc chĩa micro lên"},
  "cách nhau ba bậc", {"VANESSA": "hai tay bị còng ra sau lưng", "REPORTER": "một tay giơ micro, tay kia giữ dây tai nghe"})
B("B1", "Mở cảnh. Chập tối trên bậc thềm nhà thờ. VANESSA bị dẫn xuống giữa đèn pha truyền hình và đèn xe cảnh sát.",
  "toàn cảnh 24mm · VANESSA NÉT bị dẫn xuống bậc thềm + REPORTER NÉT ở chân bậc chĩa micro lên",
  [("VANESSA", "VANESSA_CODAUBAN"), ("REPORTER", "REPORTER")],
  "VANESSA và REPORTER rõ mặt. Không có ai khác rõ mặt trong khung; các bóng người khác trên bậc thềm đều mờ "
  "và không nhìn vào camera.",
  "cùng một dãy bậc đá, bốn tiếng trước cô đi lên trong váy cưới giữa tiếng vỗ tay; bây giờ cô đi xuống giữa "
  "đèn pha và ống kính, trong đúng bộ váy đó.",
  "đèn hiệu xanh đỏ của hai xe cảnh sát quét ngang mặt tiền đá; một cánh hoa hồng trắng bị giẫm nát trên bậc; "
  "REPORTER chồm lên một bậc; VANESSA cúi thấp đầu hơn.",
  "Ambient tiếng phố chập tối và tiếng bộ đàm cảnh sát lách tách, SFX tiếng màn trập máy ảnh liên tiếp.",
  nhac("KÌM", "Sự sụp đổ này không cần nhạc reo mừng — nhạc phải nén lại để khán giả tự thấy cái giá của nó.",
       "Soul ballad at 62 BPM with a female alto very close to the mic, dry and worn; Rhodes and upright bass only, "
       "brushed drums entering once near the end; one held string note at the midpoint then gone; lyrics about "
       "walking down the same steps you walked up, never gloating; dry night mix, female vocal, soul, restrained",
       "Chamber instrumental at 60 BPM; a cello playing a slow descending line under a felt piano, one muted trumpet "
       "note held long at the midpoint then gone, no percussion, ending unresolved; cold night mix, cello, piano, "
       "trumpet, restrained"),
  dur=8)

# ── TRƯỚC ỐNG KÍNH ──
S("01", "trung 50mm, cao 1m55, cách VANESSA 2m4, đặt trên bậc thềm lấy cả hai người",
  "VANESSA đứng ở nửa PHẢI khung trên bậc thềm, hai tay bị còng ra sau lưng, váy cưới lấm bụi ở gấu. REPORTER đứng ở "
  "nửa TRÁI khung thấp hơn một bậc, micro chĩa lên. Hậu cảnh là cửa gỗ lớn hé mở và đèn lồng đồng thau.",
  "REPORTER một tay chĩa micro về phía VANESSA. VANESSA hai tay bị còng ra sau lưng, vai xoay né đi.",
  "REPORTER nhìn thẳng vào VANESSA. VANESSA quay mặt tránh ống kính.",
  "REPORTER — hỏi liên tiếp không cho đối phương kịp thở: giọng nhanh, mắt sáng. "
  "VANESSA — chỉ còn muốn một điều là không ai quay được hai bàn tay mình: mặt trắng, giọng vỡ.",
  "đúng khoảnh khắc ngay TRƯỚC khi VANESSA quay hẳn lưng lại phía máy quay",
  ["VANESSA_CODAUBAN", "REPORTER"], "dãy bậc đá trước cửa nhà thờ",
  {"VANESSA": "đứng trên bậc thềm nửa phải khung", "REPORTER": "đứng thấp hơn một bậc nửa trái khung"},
  "cách nhau một bậc", {"REPORTER": "một tay chĩa micro về phía VANESSA",
                        "VANESSA": "hai tay bị còng ra sau lưng, vai xoay né đi"})
V("01", [0, 1], "trung 50mm · REPORTER NÉT trái chĩa micro + VANESSA NÉT phải hai tay bị còng ra sau lưng",
  [("REPORTER", "REPORTER"), ("VANESSA", "VANESSA_CODAUBAN")],
  "REPORTER và VANESSA, cả hai rõ mặt trên bậc thềm. Các bóng người khác mờ, không ai nhìn vào camera.",
  "REPORTER chĩa micro lên phía VANESSA, VANESSA xoay vai né ống kính",
  [("REPORTER", "fast, hunting", 0), ("VANESSA", "cracking, panicked", 1)])

S("02", "trung 50mm, cao 1m55, cách GERALD HALE 2m2, đặt trên bậc thềm lấy cả hai người",
  "GERALD HALE đứng ở nửa PHẢI khung trên bậc thềm, một tay che ngang mặt khỏi đèn pha. REPORTER đứng ở nửa TRÁI "
  "khung, micro chĩa lên. Hậu cảnh là lòng đường có xe tin tức và đèn hiệu nhấp nháy.",
  "REPORTER một tay chĩa micro về phía GERALD HALE. GERALD HALE một tay che ngang mặt, tay kia gạt micro ra.",
  "REPORTER nhìn GERALD HALE. GERALD HALE nhìn xuống bậc đá dưới chân.",
  "REPORTER — hỏi thẳng vào chỗ đau nhất: giọng nhanh, mắt sáng. "
  "GERALD HALE — người vừa mất tất cả và chỉ còn hai chữ để nói: mặt xám, giọng khàn.",
  "đúng khoảnh khắc ngay TRƯỚC khi GERALD HALE bước xuống bậc tiếp theo",
  ["GERALD HALE", "REPORTER"], "dãy bậc đá trước cửa nhà thờ",
  {"GERALD HALE": "đứng trên bậc thềm nửa phải khung", "REPORTER": "đứng nửa trái khung"},
  "cách nhau một bậc", {"REPORTER": "một tay chĩa micro về phía GERALD HALE",
                        "GERALD HALE": "một tay che ngang mặt, tay kia gạt micro ra"})
V("02", [2, 3], "trung 50mm · REPORTER NÉT trái chĩa micro + GERALD HALE NÉT phải che mặt khỏi đèn pha",
  [("REPORTER", "REPORTER"), ("GERALD HALE", "GERALD HALE")],
  "REPORTER và GERALD HALE, cả hai rõ mặt trên bậc thềm. Các bóng người khác mờ, không ai nhìn vào camera.",
  "REPORTER chĩa micro về phía GERALD HALE, ông đưa tay gạt nó ra",
  [("REPORTER", "fast, pressing", 2), ("GERALD HALE", "hoarse, empty", 3)])

# ── RYAN QUỲ TRÊN BẬC ──
S("03", "trung 50mm, cao 1m20, cách MAYA 2m2, máy hạ thấp trên bậc thềm lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung trên bậc thềm, một chiếc áo vest đen của đàn ông khoác trên vai. RYAN đã khuỵu hai gối xuống "
  "bậc đá ở nửa TRÁI khung, một tay nắm lấy gấu chiếc áo đồng phục trắng của cô.",
  "RYAN một tay nắm lấy gấu áo đồng phục của MAYA. MAYA một tay giữ vạt áo vest, tay kia gỡ tay anh ta ra.",
  "MAYA nhìn xuống bàn tay đang nắm gấu áo mình. RYAN ngước lên nhìn MAYA.",
  "RYAN — người quỳ trên bậc đá của chính nhà thờ nơi mình từng đứng làm chú rể: mặt tan ra, giọng gấp. "
  "MAYA — nói bằng giọng của người đã hết chuyện để nói: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay RYAN rời khỏi gấu áo cô",
  ["MAYA_TRANG", "RYAN_TUXEDOROI"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng trên bậc thềm nửa phải khung", "RYAN": "khuỵu hai gối trên bậc đá nửa trái khung"},
  "sát nhau", {"RYAN": "một tay nắm gấu áo đồng phục của MAYA",
               "MAYA": "một tay giữ vạt áo vest, tay kia gỡ tay anh ta ra"})
V("03", [4, 5], "trung 50mm hạ thấp · RYAN NÉT trái quỳ trên bậc đá + MAYA NÉT phải đứng, áo vest khoác trên vai",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt trên bậc thềm. RYAN đang QUỲ HAI GỐI trên bậc đá. "
  "Các bóng người khác mờ, không ai nhìn vào camera.",
  "RYAN nắm lấy gấu chiếc áo đồng phục của MAYA, cô gỡ tay anh ta ra",
  [("RYAN", "desperate, fast", 4), ("MAYA", "flat, tired", 5)])

S("04", "cận-trung 85mm, cao 1m20, cách MAYA 1m6, máy hạ thấp, lấy MAYA đứng và RYAN quỳ",
  "MAYA đứng ở nửa PHẢI khung, RYAN quỳ hai gối ở nửa TRÁI khung phía dưới cô. Hậu cảnh là cánh cửa gỗ lớn "
  "hé mở và một đèn lồng đồng thau đang sáng.",
  "RYAN hai tay chắp lại trước ngực. MAYA hai tay giữ hai vạt áo vest trước ngực.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "RYAN — xin đúng một giây: giọng gấp, mắt ướt. "
  "MAYA — chỉ ra tư thế của anh ta bằng một câu tả sự thật: giọng bình, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN bắt đầu kể lại tám tuần của mình",
  ["MAYA_TRANG", "RYAN_TUXEDOROI"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng nửa phải khung", "RYAN": "quỳ hai gối nửa trái khung"},
  "sát nhau", {"RYAN": "hai tay chắp lại trước ngực", "MAYA": "hai tay giữ hai vạt áo vest trước ngực"})
V("04", [6, 7], "cận-trung 85mm hạ thấp · RYAN NÉT trái quỳ chắp tay + MAYA NÉT phải đứng nhìn xuống",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. RYAN đang QUỲ HAI GỐI trên bậc đá. "
  "Các bóng người khác mờ, không ai nhìn vào camera.",
  "RYAN chắp hai tay lại trước ngực, MAYA nhìn xuống anh ta",
  [("RYAN", "pleading, fast", 6), ("MAYA", "flat, observing", 7)])

S("05", "cận-trung 85mm, cao 1m10, cách RYAN 1m5, máy hạ thấp, lấy RYAN nét và một mảng vạt áo vest rìa phải",
  "RYAN quỳ hai gối chiếm phần lớn khung, mặt ngước lên. Ở rìa PHẢI khung thấy một mảng vạt áo vest đen và "
  "gấu áo đồng phục trắng của MAYA, out nét. Hậu cảnh là bậc đá và đèn pha truyền hình hắt từ dưới lên.",
  "RYAN hai tay đưa ra phía trước, lòng bàn tay ngửa.",
  "RYAN ngước lên nhìn thẳng vào mặt MAYA.",
  "RYAN — người kể lại tám tuần của mình như kể một tai nạn giao thông: giọng nhanh, mắt ướt, "
  "hai tay ngửa ra như đang chứng minh mình vô hại.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA cắt ngang bằng một câu",
  ["RYAN_TUXEDOROI", "MAYA_TRANG"], "dãy bậc đá trước cửa nhà thờ",
  {"RYAN": "quỳ hai gối, chính diện giữa khung",
   "MAYA": "một mảng vạt áo vest và gấu áo đồng phục ở rìa phải khung"},
  "sát nhau", {"RYAN": "hai tay đưa ra phía trước ngửa lòng bàn tay",
               "MAYA": "hai tay giữ vạt áo vest, ngoài vùng nét"})
V("05", [8], "cận-trung 85mm hạ thấp · RYAN NÉT quỳ chính diện · một mảng vạt áo vest và gấu áo MAYA rìa phải out nét",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN rõ mặt, đang QUỲ HAI GỐI. MAYA chỉ thấy MỘT MẢNG VẠT ÁO VEST và gấu áo đồng phục ở rìa phải, out nét — "
  "KHÔNG thấy mặt.",
  "RYAN đưa hai bàn tay ra phía trước ngửa lên và kể một mạch",
  [("RYAN", "fast, self-pitying", 8)], [("MAYA", "silent, unmoved")])

S("06", "cận-trung 85mm, cao 1m20, cách MAYA 1m5, máy hạ thấp, lấy MAYA đứng và RYAN quỳ",
  "MAYA đứng ở nửa PHẢI khung, RYAN quỳ hai gối ở nửa TRÁI khung. Hậu cảnh là cửa gỗ lớn và đèn lồng đồng thau.",
  "MAYA một tay buông xuống, các ngón duỗi thẳng. RYAN hai tay hạ xuống đùi mình.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người nhắc lại đúng câu mà anh ta đã nói trước hai trăm người: giọng thấp, chậm, mắt không rời. "
  "RYAN — chối bằng câu chối tệ nhất có thể: mắt né, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nói ra chi tiết chiếc micro",
  ["MAYA_TRANG", "RYAN_TUXEDOROI"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng nửa phải khung", "RYAN": "quỳ hai gối nửa trái khung"},
  "sát nhau", {"MAYA": "một tay buông xuống, các ngón duỗi thẳng", "RYAN": "hai tay hạ xuống đùi mình"})
V("06", [9, 10], "cận-trung 85mm hạ thấp · RYAN NÉT trái quỳ + MAYA NÉT phải đứng nhìn xuống",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. RYAN đang QUỲ HAI GỐI trên bậc đá. "
  "Các bóng người khác mờ, không ai nhìn vào camera.",
  "MAYA buông một tay xuống, các ngón duỗi thẳng, và nhắc lại đúng câu cũ",
  [("MAYA", "low, precise", 9), ("RYAN", "small, denying", 10)])

S("07", "cận 85mm, cao 1m30, cách MAYA 1m2, máy hạ thấp, lấy MAYA nét và một mảng vai RYAN rìa trái",
  "MAYA đứng chiếm phần lớn khung từ ngực trở lên. Ở rìa TRÁI khung phía dưới thấy một mảng vai tuxedo đen "
  "của RYAN đang quỳ, out nét. Hậu cảnh là mặt tiền đá và đèn lồng đồng thau xoá phông.",
  "MAYA một tay đưa lên làm động tác cầm một chiếc micro tưởng tượng rồi hạ xuống.",
  "MAYA nhìn xuống mặt RYAN.",
  "MAYA — người nhớ chính xác từng chi tiết của buổi sáng hôm đó và trả lại nó không thêm một chữ nào: "
  "giọng chậm, rõ, mắt khô, KHÔNG gào.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN nói tới chuyện ngân hàng",
  ["MAYA_TRANG", "RYAN_TUXEDOROI"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng chính diện giữa khung", "RYAN": "một mảng vai tuxedo ở rìa trái khung phía dưới"},
  "sát nhau", {"MAYA": "một tay làm động tác cầm micro tưởng tượng rồi hạ xuống",
               "RYAN": "hai tay trên đùi, ngoài vùng nét"})
V("07", [11], "cận 85mm hạ thấp · MAYA NÉT chính diện · một mảng vai tuxedo RYAN rìa trái phía dưới out nét",
  [("MAYA", "MAYA_TRANG"), ("RYAN", "RYAN_TUXEDOROI")],
  "MAYA rõ mặt. RYAN chỉ thấy MỘT MẢNG VAI tuxedo ở rìa trái phía dưới khung, out nét — "
  "KHÔNG quay mặt về camera.",
  "MAYA đưa tay lên làm động tác cầm một chiếc micro rồi hạ xuống",
  [("MAYA", "slow, exact", 11)], [("RYAN", "silent, kneeling")])

S("08", "cận-trung 85mm, cao 1m10, cách RYAN 1m5, máy hạ thấp, lấy RYAN nét và MAYA đứng trong khung",
  "RYAN quỳ hai gối ở nửa TRÁI khung, hai tay bám vào bậc đá phía trước. MAYA đứng ở nửa PHẢI khung. "
  "Hậu cảnh là lòng đường có đèn hiệu xanh đỏ nhấp nháy.",
  "RYAN hai tay bám vào mép bậc đá phía trước mình. MAYA hai tay buông dọc thân.",
  "RYAN ngước lên nhìn MAYA. MAYA nhìn xuống RYAN.",
  "RYAN — người cuối cùng cũng nói ra thứ mình thật sự tới đây để xin: giọng gấp, mắt ướt, tay bám bậc đá. "
  "MAYA — nghe hết, không cắt ngang: mặt bình, mắt thẳng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bảo anh ta đứng dậy",
  ["RYAN_TUXEDOROI", "MAYA_TRANG"], "dãy bậc đá trước cửa nhà thờ",
  {"RYAN": "quỳ hai gối nửa trái khung", "MAYA": "đứng nửa phải khung"},
  "sát nhau", {"RYAN": "hai tay bám vào mép bậc đá phía trước", "MAYA": "hai tay buông dọc thân"})
VX("08", "cận-trung 85mm hạ thấp · RYAN NÉT trái quỳ bám bậc đá + MAYA NÉT phải đứng",
   [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
   "RYAN và MAYA, cả hai rõ mặt. RYAN đang QUỲ HAI GỐI trên bậc đá. "
   "Các bóng người khác mờ, không ai nhìn vào camera.",
   "RYAN bám hai tay vào mép bậc đá phía trước và nói một mạch",
   [("RYAN", "desperate, fast",
     "Tell him to stop it. That is all. Just tell your husband to stop the bank.")],
   [("MAYA", "silent, listening")])

S("08b", "cận 85mm, cao 1m10, cách RYAN 1m2, máy hạ thấp, lấy RYAN nét và một mảng vạt áo vest MAYA rìa phải",
  "RYAN quỳ hai gối chiếm phần lớn khung từ ngực trở lên, mặt ngước lên. Ở rìa PHẢI khung thấy một mảng vạt áo "
  "vest đen và gấu áo đồng phục trắng của MAYA, out nét. Hậu cảnh là bậc đá và đèn pha truyền hình hắt lên.",
  "RYAN một tay bấu vào mép bậc đá, tay kia đưa lên ngang ngực rồi rơi xuống đùi.",
  "RYAN ngước lên nhìn thẳng vào mặt MAYA.",
  "RYAN — người cuối cùng cũng nói ra thứ mình sợ nhất: mắt tràn nước, giọng vỡ, vai rung.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bảo anh ta đứng dậy",
  ["RYAN_TUXEDOROI", "MAYA_TRANG"], "dãy bậc đá trước cửa nhà thờ",
  {"RYAN": "quỳ hai gối, chính diện giữa khung",
   "MAYA": "một mảng vạt áo vest và gấu áo đồng phục ở rìa phải khung"},
  "sát nhau", {"RYAN": "một tay bấu mép bậc đá, tay kia đưa lên ngang ngực rồi rơi xuống đùi",
               "MAYA": "hai tay buông dọc thân, ngoài vùng nét"})
VX("08b", "cận 85mm hạ thấp · RYAN NÉT quỳ chính diện · một mảng vạt áo vest và gấu áo MAYA rìa phải out nét",
   [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
   "RYAN rõ mặt, đang QUỲ HAI GỐI. MAYA chỉ thấy MỘT MẢNG VẠT ÁO VEST và gấu áo đồng phục ở rìa phải, out nét — "
   "KHÔNG thấy mặt.",
   "RYAN đưa một tay lên ngang ngực rồi để nó rơi xuống đùi",
   [("RYAN", "desperate, fast",
     "My name is on those accounts too. I signed things, Maya. I will go to prison for things I did not even read.")],
   [("MAYA", "silent, listening")])

S("09", "trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp trên bậc thềm lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, một tay đưa ra phía RYAN. RYAN quỳ hai gối ở nửa TRÁI khung, đã ngẩng lên. "
  "Hậu cảnh là cánh cửa gỗ lớn hé mở.",
  "MAYA một tay đưa ra phía RYAN, lòng bàn tay ngửa lên. RYAN hai tay còn bám bậc đá.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người ra lệnh cho anh ta đứng dậy vì chính cô biết quỳ là thế nào: giọng chắc, mắt thẳng, "
  "KHÔNG thương hại. RYAN — không hiểu ngay: mày nhướn, miệng hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN chống tay đứng lên",
  ["MAYA_TRANG", "RYAN_TUXEDOROI"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng nửa phải khung", "RYAN": "quỳ hai gối nửa trái khung"},
  "sát nhau", {"MAYA": "một tay đưa ra phía RYAN, lòng bàn tay ngửa",
               "RYAN": "hai tay còn bám bậc đá"})
V("09", [13, 14], "trung 50mm hạ thấp · RYAN NÉT trái quỳ ngẩng lên + MAYA NÉT phải chìa tay ra",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt. RYAN đang QUỲ HAI GỐI trên bậc đá. "
  "Các bóng người khác mờ, không ai nhìn vào camera.",
  "MAYA đưa một tay ra phía RYAN, lòng bàn tay ngửa lên",
  [("MAYA", "firm, level", 13), ("RYAN", "confused, small", 14)])

S("10", "trung 50mm, cao 1m55, cách MAYA 2m, đặt trên bậc thềm lấy cả hai người đứng",
  "MAYA đứng ở nửa PHẢI khung, RYAN đã đứng lên ở nửa TRÁI khung, quần tuxedo còn dính bụi ở hai đầu gối. "
  "Hậu cảnh là đèn pha truyền hình hắt từ dưới lên và mặt tiền đá.",
  "MAYA một tay còn đưa ra, tay kia đã đưa vào trong áo vest lấy một thứ. RYAN hai tay phủi bụi ở hai đầu gối.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người giải thích rất ngắn vì sao mình bắt anh ta đứng lên: giọng bình, mắt thẳng. "
  "RYAN — vừa đứng lên và chưa biết chuyện gì tiếp theo: mày chau, giọng nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA rút xấp tiền ra khỏi trong áo vest",
  ["MAYA_TRANG", "RYAN_TUXEDOROI", "PROP_TIEN"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng nửa phải khung", "RYAN": "đã đứng lên, nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay đưa ra, tay kia đưa vào trong áo vest",
                         "RYAN": "hai tay phủi bụi ở hai đầu gối"})
V("10", [15, 16], "trung 50mm · RYAN NÉT trái vừa đứng lên + MAYA NÉT phải · đèn pha hắt từ dưới lên",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt, cùng đứng trên bậc thềm. Các bóng người khác mờ, không ai nhìn vào camera.",
  "RYAN đứng lên phủi bụi ở hai đầu gối, MAYA đưa một tay vào trong áo vest",
  [("MAYA", "firm, plain", 15), ("RYAN", "small, obedient", 16)])

S("11", "cận-trung 85mm, cao 1m55, cách MAYA 1m6, đặt trên bậc thềm lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, một XẤP TIỀN GIẤY dày bó dải giấy trắng đã ở trong tay cô, chìa ra. "
  "RYAN đứng ở nửa TRÁI khung, hai tay chưa đưa ra nhận. Hậu cảnh là cửa gỗ lớn và đèn lồng đồng thau.",
  "MAYA một tay chìa xấp tiền ra ngang ngực. RYAN một tay đưa lên nửa chừng rồi dừng.",
  "RYAN nhìn xấp tiền trong tay MAYA. MAYA nhìn thẳng vào mặt RYAN.",
  "MAYA — người trả lại một món đồ đã giữ bốn tuần: mặt bình, tay không run, mắt thẳng. "
  "RYAN — nhận ra đó là xấp tiền nào: mắt mở to, miệng hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN chạm vào xấp tiền",
  ["MAYA_TRANG", "RYAN_TUXEDOROI", "PROP_TIEN"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng nửa phải khung chìa xấp tiền", "RYAN": "đứng nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay chìa xấp tiền ra ngang ngực",
                         "RYAN": "một tay đưa lên nửa chừng rồi dừng"})
V("11", [17, 18, 19], "cận-trung 85mm · RYAN NÉT trái + MAYA NÉT phải chìa xấp tiền ra",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt trên bậc thềm. Các bóng người khác mờ, không ai nhìn vào camera.",
  "MAYA rút xấp tiền ra khỏi trong áo vest và chìa nó ra ngang ngực",
  [("MAYA", "flat, offering", 17), ("RYAN", "small, uncomprehending", 18),
   ("MAYA", "level, plain", 19)])

S("12", "cận-trung 85mm, cao 1m55, cách MAYA 1m5, máy sau vai TRÁI của RYAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, xấp tiền còn chìa ra ở tiền cảnh dưới khung. RYAN chỉ còn là "
  "vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là mặt tiền đá và đèn lồng đồng thau.",
  "MAYA một tay chìa xấp tiền, tay kia giữ vạt áo vest trước ngực.",
  "MAYA nhìn thẳng vào mặt RYAN.",
  "MAYA — người trả lại đúng câu mà cô đã nói bốn tuần trước, không thêm một chữ: giọng bình, mắt thẳng, "
  "KHÔNG hả hê.",
  "đúng khoảnh khắc ngay TRƯỚC khi RYAN cầm lấy xấp tiền",
  ["MAYA_TRANG", "RYAN_TUXEDOROI", "PROP_TIEN"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng chính diện giữa khung, tay chìa xấp tiền", "RYAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "một tay chìa xấp tiền, tay kia giữ vạt áo vest",
                         "RYAN": "một tay đưa lên, ngoài vùng nét"})
V("12", [20, 21], "OTS cận-trung 85mm · MAYA NÉT chính diện chìa xấp tiền · vai và gáy RYAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_TRANG"), ("RYAN", "RYAN_TUXEDOROI")],
  "MAYA rõ mặt chính diện. RYAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA giữ nguyên xấp tiền chìa ra cho tới khi anh ta cầm lấy",
  [("RYAN", "small, disbelieving", 20), ("MAYA", "level, final", 21)])

S("13", "trung 50mm, cao 1m55, cách MAYA 2m, đặt trên bậc thềm lấy cả hai người đứng",
  "MAYA đứng ở nửa PHẢI khung, đã quay nửa người đi về phía cửa lớn. RYAN đứng ở nửa TRÁI khung, xấp tiền "
  "trong tay, một tay đưa ra phía cô. Hậu cảnh là đèn hiệu xanh đỏ dưới lòng đường.",
  "MAYA hai tay giữ vạt áo vest, người đã quay đi nửa vòng. RYAN một tay cầm xấp tiền, tay kia đưa ra phía cô.",
  "RYAN nhìn theo MAYA. MAYA nhìn về phía cửa lớn phía trên bậc thềm.",
  "RYAN — gọi tên cô lần cuối cùng: giọng gấp, mắt ướt. "
  "MAYA — trả lời không quay đầu lại quá nửa vòng: mặt bình, giọng đều, mắt đã hướng đi chỗ khác.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước hẳn lên bậc trên",
  ["MAYA_TRANG", "RYAN_TUXEDOROI", "PROP_TIEN"], "dãy bậc đá trước cửa nhà thờ",
  {"MAYA": "đứng nửa phải khung, đã quay nửa người đi", "RYAN": "đứng nửa trái khung, cầm xấp tiền"},
  "cách nhau một bước", {"MAYA": "hai tay giữ vạt áo vest",
                         "RYAN": "một tay cầm xấp tiền, tay kia đưa ra phía cô"})
V("13", [22, 23], "trung 50mm · RYAN NÉT trái cầm xấp tiền + MAYA NÉT phải đã quay nửa người đi",
  [("RYAN", "RYAN_TUXEDOROI"), ("MAYA", "MAYA_TRANG")],
  "RYAN và MAYA, cả hai rõ mặt trên bậc thềm. Các bóng người khác mờ, không ai nhìn vào camera.",
  "RYAN đưa tay ra gọi với theo, MAYA quay nửa người đi về phía cửa lớn",
  [("RYAN", "urgent, pleading", 22), ("MAYA", "even, closed", 23)],
  ketclip="Cuối clip, MAYA bước lên hai bậc tới chỗ ADRIAN đang đứng vịn lan can đá, RYAN đứng lại phía sau. "
          "Clip dừng đúng lúc cô dừng chân cạnh anh.")

S("14", "cận-trung 85mm, cao 1m55, cách ADRIAN 1m6, đặt trên bậc thềm lấy cả hai người đứng",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, một tay vịn LAN CAN ĐÁ THẤP, hai chân hơi rộng để giữ thăng bằng. "
  "MAYA đứng ở nửa PHẢI khung sát cạnh anh. Hậu cảnh là cánh cửa gỗ lớn hé mở và đèn lồng đồng thau.",
  "ADRIAN một tay vịn lan can đá, tay kia buông. MAYA một tay đặt lên lưng ADRIAN.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người đã đứng năm mươi phút và hai chân bắt đầu không nghe lời nữa: mồ hôi ở thái dương, "
  "hơi thở nặng, mặt vẫn bình. MAYA — điều dưỡng nhìn ra ngay: mày chau, tay đã đặt lên lưng anh.",
  "đúng khoảnh khắc ngay TRƯỚC khi đầu gối ADRIAN khuỵu xuống một nhịp",
  ["ADRIAN_VEST", "MAYA_TRANG"], "dãy bậc đá trước cửa nhà thờ, cạnh lan can đá",
  {"ADRIAN": "đứng thẳng vịn lan can đá, nửa trái khung", "MAYA": "đứng sát cạnh nửa phải khung"},
  "sát nhau", {"ADRIAN": "một tay vịn lan can đá, tay kia buông",
               "MAYA": "một tay đặt lên lưng ADRIAN"})
V("14", [24, 25], "cận-trung 85mm · ADRIAN NÉT trái đứng vịn lan can đá + MAYA NÉT phải đặt tay lên lưng anh",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN và MAYA, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN, một tay vịn lan can đá. "
  "Các bóng người khác mờ, không ai nhìn vào camera.",
  "MAYA đặt một tay lên lưng ADRIAN, anh vịn chặt hơn vào lan can đá",
  [("ADRIAN", "breathless, dry", 24), ("MAYA", "warm, firm", 25)])

S("15", "two-shot cận-trung 85mm, cao 1m55, cách MAYA 1m5, đặt trên bậc thềm lấy cả hai người đứng",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, đã buông lan can đá. MAYA đứng ở nửa PHẢI khung, đã kéo cánh tay anh "
  "vắt qua vai mình. Hậu cảnh là đèn pha truyền hình hắt từ dưới lên và bầu trời chập tối xanh mực.",
  "MAYA một tay kéo cánh tay ADRIAN vắt qua vai mình, tay kia vòng ra sau lưng anh. "
  "ADRIAN một tay đặt trên vai MAYA.",
  "Hai người nhìn thẳng vào mắt nhau, rất gần.",
  "ADRIAN — người sợ mình sẽ đè cô ngã: mày chau, giọng nhỏ. "
  "MAYA — trả lời bằng câu chốt của cả bộ phim: giọng chắc, mắt sáng, khoé môi kéo lên một chút.",
  "đúng khoảnh khắc ngay TRƯỚC khi hai người bước bước đầu tiên cùng nhau xuống bậc",
  ["ADRIAN_VEST", "MAYA_TRANG"], "dãy bậc đá trước cửa nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "MAYA": "đứng sát cạnh nửa phải khung, đỡ anh"},
  "sát nhau", {"MAYA": "một tay kéo cánh tay ADRIAN vắt qua vai mình, tay kia vòng ra sau lưng anh",
               "ADRIAN": "một tay đặt trên vai MAYA"})
V("15", [26, 27], "two-shot cận-trung 85mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT phải đỡ tay anh qua vai mình",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN và MAYA, cả hai rõ mặt, đứng sát nhau trên bậc thềm. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Các bóng người khác mờ, không ai nhìn vào camera.",
  "MAYA kéo cánh tay ADRIAN vắt qua vai mình và vòng tay ra sau lưng anh",
  [("ADRIAN", "quiet, afraid", 26), ("MAYA", "warm, certain", 27)])
