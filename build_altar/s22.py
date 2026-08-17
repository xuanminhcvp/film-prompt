# -*- coding: utf-8 -*-
"""SCENE 22 — ANH ĐỨNG DẬY (nhà thờ St. Michael, chiều)."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S22", "REF_NHATHOTIEC_CHIEU", qc=qc.S22, qcv=qc.S22V)

KHACH = ""

S("01", "cận-trung 85mm, cao 1m55, cách GUEST ONE 1m7, đặt trong vòng người vây quanh",
  "GUEST ONE đứng ở nửa TRÁI khung, GUEST TWO đứng ở nửa PHẢI khung sát cạnh, cả hai đang nhìn xuống nền. "
  "Hậu cảnh là cột đá và các cụm khách khác mờ.",
  "GUEST ONE một tay giữ ly champagne quên nâng lên. GUEST TWO một tay bám vào cánh tay GUEST ONE.",
  "Cả hai nhìn xuống nền đá ngoài khung. TUYỆT ĐỐI không ai nhìn vào ống kính.",
  "GUEST ONE — người vừa thấy một thứ không nên xảy ra: mày nhướn cao, miệng hé. "
  "GUEST TWO — bám lấy cánh tay người bên cạnh: mắt mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả hai người cùng lùi lại nửa bước",
  ["GUEST1_TUX", "GUEST2_DAHOI"], "trong vòng người vây quanh, cuối nhà thờ bên phải",
  {"GUEST ONE": "đứng nửa trái khung", "GUEST TWO": "đứng nửa phải khung"},
  "sát cạnh nhau", {"GUEST ONE": "một tay giữ ly champagne", "GUEST TWO": "một tay bám cánh tay GUEST ONE"})
V("01", [0, 1], "cận-trung 85mm · GUEST ONE NÉT trái + GUEST TWO NÉT phải, cùng nhìn xuống nền · khách nền mờ",
  [("GUEST ONE", "GUEST1_TUX"), ("GUEST TWO", "GUEST2_DAHOI")],
  "GUEST ONE và GUEST TWO, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GUEST TWO bám lấy cánh tay GUEST ONE, cả hai nhìn xuống nền đá",
  [("GUEST ONE", "bewildered, hushed", 0), ("GUEST TWO", "hushed, disbelieving", 1)])

S("02", "trung 50mm, cao 0m80, cách ADRIAN 2m2, máy hạ rất thấp ngang mặt nền đá cẩm thạch",
  "ADRIAN nằm nghiêng trên nền đá ở nửa PHẢI khung, đã chống được cả hai lòng bàn tay xuống nền, người nhấc lên "
  "khỏi mặt sàn một chút. JULIAN đứng ở nửa TRÁI khung phía trên, ly champagne trong tay. " + KHACH,
  "ADRIAN hai lòng bàn tay chống xuống nền đá, hai cánh tay căng. JULIAN một tay cầm ly, tay kia chỉ xuống.",
  "ADRIAN nhìn xuống mặt nền trước mặt mình. JULIAN nhìn xuống ADRIAN.",
  "ADRIAN — người đang dồn toàn bộ sức vào hai cánh tay: quai hàm siết, gân cổ nổi, mắt tập trung tuyệt đối. "
  "JULIAN — vẫn còn đang cười: khoé môi kéo, giọng nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi đầu gối ADRIAN rời khỏi mặt nền",
  ["ADRIAN_TIEC", "JULIAN_TUX"], "nền đá cẩm thạch cuối nhà thờ bên phải",
  {"ADRIAN": "nằm nghiêng chống hai lòng bàn tay, nửa phải khung", "JULIAN": "đứng phía trên nửa trái khung"},
  "cách nhau hai bước", {"ADRIAN": "hai lòng bàn tay chống xuống nền đá",
                         "JULIAN": "một tay cầm ly, tay kia chỉ xuống"})
V("02", [2], "trung 50mm hạ rất thấp · ADRIAN NÉT phải chống hai tay xuống nền đá + JULIAN NÉT trái đứng phía trên",
  [("ADRIAN", "ADRIAN_TIEC"), ("JULIAN", "JULIAN_TUX")],
  "ADRIAN và JULIAN, cả hai rõ mặt. ADRIAN đang chống hai lòng bàn tay xuống nền đá, người nhấc lên khỏi sàn. "
  "Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "ADRIAN chống hai lòng bàn tay xuống nền đá và nhấc người lên khỏi mặt sàn",
  [("JULIAN", "light, dismissive", 2)], [("ADRIAN", "silent, straining")])

S("03", "cận-trung 85mm, cao 1m55, cách GUEST TWO 1m7, đặt trong vòng người vây quanh",
  "GUEST TWO đứng ở nửa PHẢI khung, một tay đưa lên miệng. GUEST ONE đứng ở nửa TRÁI khung, người đã ngả về sau. "
  "Hậu cảnh là các cụm khách khác mờ và đèn pha lê.",
  "GUEST TWO một tay đưa lên miệng, tay kia buông rơi chiếc clutch xuống bên hông. "
  "GUEST ONE một tay đưa ra sau tìm chỗ vịn.",
  "Cả hai nhìn xuống nền đá ngoài khung. TUYỆT ĐỐI không ai nhìn vào ống kính.",
  "GUEST ONE — đếm ra thành tiếng từng nấc anh ta thấy: mắt mở to, giọng khàn. "
  "GUEST TWO — thốt lên một câu: miệng mở, mắt không chớp.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả một vùng phòng im bặt",
  ["GUEST2_DAHOI", "GUEST1_TUX"], "trong vòng người vây quanh, cuối nhà thờ bên phải",
  {"GUEST TWO": "đứng nửa phải khung", "GUEST ONE": "đứng nửa trái khung"},
  "sát cạnh nhau", {"GUEST TWO": "một tay đưa lên miệng", "GUEST ONE": "một tay đưa ra sau tìm chỗ vịn"})
V("03", [3, 4], "cận-trung 85mm · GUEST ONE NÉT trái + GUEST TWO NÉT phải, cùng nhìn xuống nền · khách nền mờ",
  [("GUEST ONE", "GUEST1_TUX"), ("GUEST TWO", "GUEST2_DAHOI")],
  "GUEST ONE và GUEST TWO, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "GUEST TWO đưa tay lên miệng, GUEST ONE ngả người ra sau tìm chỗ vịn",
  [("GUEST ONE", "hoarse, counting", 3), ("GUEST TWO", "stunned, hushed", 4)])

S("04", "trung 50mm, cao 0m90, cách MAYA 2m2, máy hạ thấp, lấy MAYA quỳ và JULIAN đứng",
  "MAYA quỳ ở nửa PHẢI khung trên nền đá, đã ngẩng phắt lên. JULIAN đứng ở nửa TRÁI khung, ly champagne "
  "đã hạ xuống. Ở rìa TRÁI khung thấy một phần lưng và vai ADRIAN đang chống người lên, out nét.",
  "MAYA hai tay chống xuống nền đá, người nhổm lên. JULIAN một tay hạ ly xuống, tay kia chỉ xuống nền.",
  "MAYA nhìn về phía ADRIAN ngoài vùng nét. JULIAN nhìn xuống nền.",
  "MAYA — người vừa gọi tên chồng mình và nghe chính giọng mình vỡ ra: mắt mở to, miệng hé. "
  "JULIAN — lần đầu tiên trong cả bộ phim mất nhịp: mắt hơi mở, giọng cao lên.",
  "đúng khoảnh khắc ngay TRƯỚC khi cả gian nhà thờ im bặt hoàn toàn",
  ["MAYA_TRANG", "JULIAN_TUX", "ADRIAN_TIEC"], "nền đá cẩm thạch cuối nhà thờ bên phải",
  {"MAYA": "quỳ nửa phải khung, nhổm lên", "JULIAN": "đứng nửa trái khung",
   "ADRIAN": "một phần lưng và vai ở rìa trái khung, đang chống người lên"},
  "ba người trong vòng hai mét",
  {"MAYA": "hai tay chống xuống nền đá", "JULIAN": "một tay hạ ly xuống, tay kia chỉ xuống nền",
   "ADRIAN": "hai lòng bàn tay chống nền, ngoài vùng nét"})
V("04", [5, 6], "trung 50mm hạ thấp · MAYA NÉT phải quỳ nhổm lên + JULIAN NÉT trái · một phần lưng và vai ADRIAN rìa trái out nét",
  [("MAYA", "MAYA_TRANG"), ("JULIAN", "JULIAN_TUX"), ("ADRIAN", "ADRIAN_TIEC")],
  "MAYA và JULIAN rõ mặt. ADRIAN chỉ thấy MỘT PHẦN LƯNG VÀ VAI ở rìa trái khung, out nét — "
  "KHÔNG quay mặt về camera.",
  "MAYA nhổm lên khỏi tư thế quỳ, JULIAN hạ ly champagne xuống",
  [("MAYA", "breaking, small", 5), ("JULIAN", "raised, unsettled", 6)],
  ketclip="Cuối clip, ADRIAN chống một gối lên rồi từ từ đứng thẳng dậy trên hai chân giữa nền đá. "
          "Clip dừng đúng lúc anh đứng thẳng người.")

# ── NHỊP: ANH ĐỨNG DẬY ──
S("B1", "trung-rộng 35mm, cao 1m60, cách ADRIAN 5m, đặt trong lòng nhà thờ nhìn về phía anh đứng",
  "ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN giữa nền đá cẩm thạch, chiếc xe lăn tay cũ đổ nghiêng phía sau anh. "
  "MAYA quỳ dưới nền ở nửa PHẢI khung, ngẩng nhìn lên. Vòng khách vây quanh đã lùi ra, đứng im, mờ ngoài vùng nét.",
  "ADRIAN hai tay buông dọc thân, các ngón hơi run. MAYA hai tay chống xuống nền đá.",
  "ADRIAN nhìn dọc lối đi về phía bàn thờ. MAYA nhìn lên ADRIAN. "
  "Khách nền TUYỆT ĐỐI không nhìn vào ống kính.",
  "ADRIAN — người vừa đứng dậy sau sáu tháng, hai chân còn run mà lưng thì thẳng: quai hàm siết, mắt sáng, "
  "hơi thở sâu. MAYA — nhìn thứ mình được bảo là không thể: mắt mở to, một giọt nước mắt chưa rơi.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bước bước đầu tiên",
  ["ADRIAN_VEST", "MAYA_TRANG"], "nền đá cẩm thạch cuối nhà thờ, chiếc xe lăn đổ phía sau",
  {"ADRIAN": "đứng thẳng trên hai chân giữa nền đá", "MAYA": "quỳ dưới nền nửa phải khung"},
  "cách nhau hai mét", {"ADRIAN": "hai tay buông dọc thân, các ngón hơi run",
                        "MAYA": "hai tay chống xuống nền đá"})
B("B1", "[NHỊP] Cao trào. ADRIAN đứng thẳng trên hai chân giữa nhà thờ, chiếc xe lăn đổ phía sau, cả phòng chết lặng.",
  "trung-rộng 35mm · ADRIAN NÉT đứng thẳng trên hai chân giữa nền đá + MAYA NÉT quỳ dưới nền · khách vây quanh mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN, KHÔNG có nạng, KHÔNG có gậy, chiếc xe lăn đổ nghiêng phía sau anh. "
  "MAYA rõ mặt đang quỳ dưới nền. Khách vây quanh mờ, không ai nhìn vào camera.",
  "sáu tháng cả một gia tộc tin rằng người đàn ông này đã hỏng; khung hình này là chỗ niềm tin đó vỡ, "
  "và nó vỡ trong im lặng tuyệt đối chứ không phải bằng tiếng hét.",
  "ADRIAN đứng thẳng, hai vai cân lại, ngực thở một nhịp rất dài; một chiếc ly champagne trong tay ai đó "
  "nghiêng đi và rượu sánh ra sàn; vòng người vây quanh lùi thêm nửa bước; MAYA đưa một tay lên miệng.",
  "Ambient tiếng vọng của một gian nhà thờ đá vừa im bặt hoàn toàn, SFX một tiếng ly champagne chạm nền rất khẽ.",
  nhac("ĐẨY", "Đỉnh cảm xúc lớn nhất của cả phim — đây là một trong ba chỗ duy nhất nhạc được phép chiếm sân khấu.",
       "Cinematic soul at 80 BPM; a lone female alto entering on the downbeat close to the mic, low strings and a "
       "slow heartbeat kick building underneath, a choir humming very low joining at the midpoint and rising to one "
       "held chord; the pull is the last four seconds where everything cuts to the solo voice; lyrics from a man "
       "standing up in a room that had already buried him, never triumphant, only immense; warm analog mix, "
       "female vocal, choir, strings, cinematic, overwhelming",
       "Cinematic instrumental at 80 BPM; low strings rising from silence under a slow heartbeat kick, a French horn "
       "carrying the line at the midpoint, full string section and timpani reaching one held chord, then everything "
       "cutting away to a single sustained cello note; warm analog mix, strings, horn, timpani, cello, cinematic, "
       "overwhelming"),
  dur=10)

# ── HAI BƯỚC ──
S("05", "trung 50mm, cao 1m55, cách ADRIAN 2m4, đặt trong lòng nhà thờ lấy cả hai người",
  "ADRIAN đứng thẳng trên hai chân ở nửa PHẢI khung, đã bước được hai bước. GERALD HALE đứng ở nửa TRÁI khung, "
  "đã lùi lại một bước. " + KHACH,
  "ADRIAN hai tay buông dọc thân, một tay hơi mở ra để giữ thăng bằng. GERALD HALE một tay chỉ về phía ADRIAN, "
  "tay kia nắm lại.",
  "ADRIAN nhìn thẳng về phía cuối lối đi ngoài khung. GERALD HALE nhìn ADRIAN.",
  "ADRIAN — người đếm từng bước một và nói ra thành tiếng: giọng đều, hơi thở nặng, mặt bình. "
  "GERALD HALE — bắt đầu tìm một lời giải thích khác: mắt đảo, giọng cao.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN bước bước thứ ba",
  ["ADRIAN_VEST", "GERALD HALE"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng trên hai chân nửa phải khung", "GERALD HALE": "đứng lùi lại nửa trái khung"},
  "cách nhau ba bước", {"ADRIAN": "hai tay buông dọc thân, một tay hơi mở giữ thăng bằng",
                        "GERALD HALE": "một tay chỉ về phía ADRIAN, tay kia nắm lại"})
V("05", [7, 8], "trung 50mm · ADRIAN NÉT phải đứng thẳng trên hai chân + GERALD HALE NÉT trái lùi lại · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("GERALD HALE", "GERALD HALE")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN, KHÔNG có xe lăn, KHÔNG có nạng. GERALD HALE rõ mặt. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN bước hai bước trên nền đá, GERALD HALE lùi lại một bước",
  [("ADRIAN", "even, counting", 7), ("GERALD HALE", "raised, grasping", 8)])

S("06", "trung 50mm, cao 1m20, cách MAYA 2m, máy hạ thấp, lấy ADRIAN đứng và MAYA quỳ dưới nền",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, đã tới sát chỗ MAYA quỳ, một tay chìa xuống. MAYA quỳ ở nửa PHẢI khung, "
  "ngẩng nhìn lên. " + KHACH,
  "ADRIAN một tay chìa xuống về phía MAYA, lòng bàn tay ngửa. MAYA hai tay còn chống xuống nền đá.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người đi hết một gian phòng chỉ để đưa tay xuống cho vợ mình: mặt bình, mắt sáng, hơi thở nặng. "
  "MAYA — chưa dám tin thứ mình đang nhìn: mắt mở to, môi run.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay MAYA chạm vào bàn tay anh",
  ["ADRIAN_VEST", "MAYA_TRANG"], "nền đá cẩm thạch cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung, tay chìa xuống", "MAYA": "quỳ nửa phải khung"},
  "sát nhau", {"ADRIAN": "một tay chìa xuống ngửa lòng bàn tay", "MAYA": "hai tay chống xuống nền đá"})
V("06", [9, 10], "trung 50mm hạ thấp · ADRIAN NÉT trái đứng thẳng chìa tay xuống + MAYA NÉT phải quỳ dưới nền",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt đang quỳ dưới nền. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN chìa một bàn tay xuống về phía MAYA, lòng bàn tay ngửa",
  [("ADRIAN", "quiet, steady", 9), ("MAYA", "small, disbelieving", 10)],
  ketclip="Cuối clip, MAYA nắm lấy bàn tay anh và được kéo đứng dậy, ADRIAN cởi áo vest khoác lên vai cô. "
          "Clip dừng đúng lúc vạt áo phủ lên chỗ tay áo rách.")

S("07", "cận-trung 85mm, cao 1m55, cách ADRIAN 1m6, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, đã cởi áo vest và đang khoác nó lên vai MAYA. MAYA đứng ở nửa PHẢI khung, "
  "vai trái có chỗ tay áo rách. Hậu cảnh là vòng khách vây quanh, mờ.",
  "ADRIAN hai tay kéo hai vạt áo vest phủ lên vai MAYA. MAYA một tay giữ lấy vạt áo trước ngực.",
  "Hai người nhìn thẳng vào mắt nhau, rất gần.",
  "ADRIAN — người trả lời câu hỏi lớn bằng ba câu ngắn: giọng nhỏ, hơi thở còn nặng, mắt dịu. "
  "MAYA — nghe từng chữ và chưa ghép được: mắt ướt, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi anh đã tập bao lâu",
  ["ADRIAN_VEST", "MAYA_TRANG"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "MAYA": "đứng nửa phải khung, vai trái có chỗ áo rách"},
  "rất gần nhau", {"ADRIAN": "hai tay kéo vạt áo vest phủ lên vai MAYA",
                   "MAYA": "một tay giữ vạt áo trước ngực"})
V("07", [11], "cận-trung 85mm · ADRIAN NÉT trái đứng thẳng khoác áo vest lên vai MAYA + MAYA NÉT phải",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt, vai trái có chỗ tay áo rách. "
  "Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN cởi áo vest và kéo hai vạt áo phủ lên vai MAYA",
  [("ADRIAN", "quiet, tender", 11)], [("MAYA", "silent, eyes filling")])

S("08", "cận 85mm, cao 1m55, cách MAYA 1m3, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, áo vest đen khoác trên vai. ADRIAN chỉ còn là vai và gáy ở rìa "
  "TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là vòng khách vây quanh mờ và ánh đèn pha lê.",
  "MAYA một tay giữ hai vạt áo vest trước ngực.",
  "MAYA nhìn thẳng vào mặt ADRIAN.",
  "MAYA — người hỏi hai chữ và đã bắt đầu hiểu ra quy mô của những gì mình chưa biết: mắt ướt, "
  "giọng rất nhỏ, mày chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN trả lời bằng các con số",
  ["MAYA_TRANG", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"MAYA": "đứng chính diện giữa khung, áo vest khoác trên vai", "ADRIAN": "vai và gáy tiền cảnh trái"},
  "rất gần nhau", {"MAYA": "một tay giữ hai vạt áo vest trước ngực",
                   "ADRIAN": "hai tay buông, ngoài vùng nét"})
V("08", [12, 13], "OTS cận 85mm · MAYA NÉT chính diện khoác áo vest · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_TRANG"), ("ADRIAN", "ADRIAN_VEST")],
  "MAYA rõ mặt chính diện, áo vest đen khoác trên vai. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA giữ hai vạt áo vest trước ngực và hỏi",
  [("MAYA", "very small, shaken", 12), ("ADRIAN", "quiet, factual", 13)])

S("09", "two-shot trung 50mm, cao 1m55, cách MAYA 2m, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "MAYA đứng ở nửa PHẢI khung, áo vest khoác trên vai. ADRIAN đứng thẳng ở nửa TRÁI khung. "
  "Hậu cảnh là chiếc xe lăn tay cũ còn đổ nghiêng trên nền đá và vòng khách mờ.",
  "MAYA một tay chỉ về phía chiếc xe lăn đổ. ADRIAN hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa hiểu ra rằng mọi cú ngã đều là cố ý: mắt mở to, giọng vỡ, mày chau. "
  "ADRIAN — thừa nhận không né một chữ nào: mặt bình, mắt thẳng, giọng đều.",
  "đúng khoảnh khắc ngay TRƯỚC khi có tiếng báo cáo vọng tới từ phía cửa lớn",
  ["MAYA_TRANG", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"MAYA": "đứng nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung"},
  "sát nhau", {"MAYA": "một tay chỉ về phía chiếc xe lăn đổ", "ADRIAN": "hai tay buông dọc thân"})
V("09", [14, 15], "two-shot trung 50mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT phải khoác áo vest · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "MAYA chỉ về phía chiếc xe lăn còn đổ nghiêng trên nền đá",
  [("MAYA", "cracking, realising", 14), ("ADRIAN", "even, admitting", 15)])

# ── HAI MƯƠI NGƯỜI Ở CỬA LỚN ──
S("10", "trung 50mm, cao 1m55, cách SECURITY CHIEF 2m2, đặt trong lòng nhà thờ nhìn về phía cửa lớn",
  "SECURITY CHIEF đứng ở nửa TRÁI khung, một tay đưa lên tai nghe xoắn dây. GERALD HALE đứng ở nửa PHẢI khung, "
  "đã quay hẳn về phía cửa lớn. Hậu cảnh xa là hai cánh cửa gỗ lớn cuối nhà thờ ĐANG MỞ RA.",
  "SECURITY CHIEF một tay đưa lên tai nghe, tay kia chỉ về phía cửa lớn. GERALD HALE hai tay buông dọc thân.",
  "Cả hai nhìn về phía hai cánh cửa lớn đang mở.",
  "SECURITY CHIEF — báo cáo một sự việc mình không kiểm soát được: mặt căng, giọng gọn. "
  "GERALD HALE — đếm số người đang bước vào: mắt mở to, giọng cao.",
  "đúng khoảnh khắc ngay TRƯỚC khi người đầu tiên bước qua ngưỡng cửa lớn",
  ["SECURITY CHIEF", "GERALD HALE"], "giữa lòng nhà thờ, nhìn về phía cửa lớn",
  {"SECURITY CHIEF": "đứng nửa trái khung", "GERALD HALE": "đứng nửa phải khung"},
  "sát cạnh nhau", {"SECURITY CHIEF": "một tay đưa lên tai nghe, tay kia chỉ về cửa lớn",
                    "GERALD HALE": "hai tay buông dọc thân"})
V("10", [16, 17], "trung 50mm · SECURITY CHIEF NÉT trái + GERALD HALE NÉT phải, cùng nhìn về cửa lớn đang mở",
  [("SECURITY CHIEF", "SECURITY CHIEF"), ("GERALD HALE", "GERALD HALE")],
  "SECURITY CHIEF và GERALD HALE, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "hai cánh cửa lớn cuối nhà thờ mở ra, SECURITY CHIEF đưa tay lên tai nghe",
  [("SECURITY CHIEF", "tight, reporting", 16), ("GERALD HALE", "raised, alarmed", 17)])

S("11", "trung 50mm, cao 1m55, cách SEBASTIAN 2m4, đặt trong lòng nhà thờ nhìn về phía cửa lớn",
  "SEBASTIAN đứng ở nửa TRÁI khung ngay trong cửa lớn, một tay giơ lên ra hiệu. GERALD HALE đứng ở nửa PHẢI "
  "khung, đã bước tới chắn đường. Hậu cảnh là hai cánh cửa gỗ mở toang và ánh sáng chiều ngoài bậc thềm.",
  "SEBASTIAN một tay giơ lên ngang vai ra hiệu về hai phía cửa, tay kia giữ bìa kẹp hồ sơ da nâu. "
  "GERALD HALE một tay chỉ vào ngực SEBASTIAN.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "SEBASTIAN — người ra lệnh trong nhà của người khác bằng giọng bình thản nhất: mặt hoàn toàn bình. "
  "GERALD HALE — vẫn còn tưởng đây là nhà mình: mặt đỏ, giọng vang.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN bước một bước vào trong lòng nhà thờ",
  ["SEBASTIAN", "GERALD HALE"], "trong cửa lớn cuối nhà thờ",
  {"SEBASTIAN": "đứng trong cửa lớn nửa trái khung", "GERALD HALE": "đứng chắn đường nửa phải khung"},
  "cách nhau hai bước", {"SEBASTIAN": "một tay giơ ngang vai ra hiệu, tay kia giữ bìa kẹp hồ sơ",
                         "GERALD HALE": "một tay chỉ vào ngực SEBASTIAN"})
V("11", [18, 19], "trung 50mm · SEBASTIAN NÉT trái trong cửa lớn + GERALD HALE NÉT phải chắn đường",
  [("SEBASTIAN", "SEBASTIAN"), ("GERALD HALE", "GERALD HALE")],
  "SEBASTIAN và GERALD HALE, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "SEBASTIAN giơ tay ra hiệu về hai phía cửa, GERALD HALE bước tới chắn đường",
  [("SEBASTIAN", "calm, commanding", 18), ("GERALD HALE", "loud, indignant", 19)])

S("12", "cận-trung 85mm, cao 1m55, cách SEBASTIAN 1m7, đặt cuối nhà thờ lấy SEBASTIAN nét và JULIAN cùng khung",
  "SEBASTIAN đứng ở nửa TRÁI khung. JULIAN đứng ở nửa PHẢI khung, đã bước tới, một tay đưa ra. "
  "Hậu cảnh là cửa lớn mở và ánh sáng chiều.",
  "SEBASTIAN hai tay giữ một chiếc ÁO KHOÁC DẠ ĐEN gấp trên cẳng tay. JULIAN một tay đưa ra phía SEBASTIAN.",
  "SEBASTIAN nhìn qua vai JULIAN về phía cuối lối đi ngoài khung. JULIAN nhìn SEBASTIAN.",
  "SEBASTIAN — người vừa nghe một lời mua chuộc và không buồn trả lời nó: mặt hoàn toàn bình, mắt không dừng "
  "lại ở JULIAN. JULIAN — vẫn đang mặc cả: mắt sáng, giọng nhanh.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN bước vòng qua JULIAN",
  ["SEBASTIAN", "JULIAN_TUX"], "cuối nhà thờ, giữa lối đi",
  {"SEBASTIAN": "đứng nửa trái khung", "JULIAN": "đứng nửa phải khung"},
  "cách nhau một bước", {"SEBASTIAN": "hai tay giữ chiếc áo khoác dạ đen gấp trên cẳng tay",
                         "JULIAN": "một tay đưa ra phía SEBASTIAN"})
V("12", [20, 21], "cận-trung 85mm · SEBASTIAN NÉT trái cầm áo khoác + JULIAN NÉT phải đưa tay ra",
  [("SEBASTIAN", "SEBASTIAN"), ("JULIAN", "JULIAN_TUX")],
  "SEBASTIAN và JULIAN, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "SEBASTIAN cầm chiếc áo khoác dạ đen gấp trên cẳng tay, JULIAN đưa tay ra chặn ông lại",
  [("SEBASTIAN", "calm, factual", 20), ("JULIAN", "quick, bargaining", 21)])

S("13", "trung 50mm, cao 1m55, cách ADRIAN 2m2, đặt trong lòng nhà thờ lấy cả ba người",
  "ADRIAN đứng thẳng ở nửa PHẢI khung. SEBASTIAN đứng ở giữa khung, đã bước tới và đang chìa chiếc ÁO KHOÁC DẠ "
  "ĐEN ra bằng cả hai tay. JULIAN đứng ở nửa TRÁI khung phía sau, quay hẳn lại nhìn.",
  "SEBASTIAN hai tay chìa chiếc áo khoác ra phía ADRIAN. ADRIAN một tay đưa ra nhận. "
  "JULIAN hai tay buông dọc thân.",
  "SEBASTIAN nhìn ADRIAN. ADRIAN nhìn SEBASTIAN. JULIAN nhìn cả hai.",
  "SEBASTIAN — gọi sếp mình bằng đúng chức danh trước mặt bốn trăm người: mặt bình, giọng rõ. "
  "ADRIAN — nhận áo: mặt bình. JULIAN — nghe cái chức danh đó: mặt trắng ra, miệng hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN cầm lấy chiếc áo khoác",
  ["ADRIAN_VEST", "SEBASTIAN", "JULIAN_TUX"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa phải khung", "SEBASTIAN": "đứng giữa khung chìa áo khoác",
   "JULIAN": "đứng nửa trái khung phía sau"},
  "ba người trong vòng hai mét",
  {"SEBASTIAN": "hai tay chìa chiếc áo khoác ra", "ADRIAN": "một tay đưa ra nhận",
   "JULIAN": "hai tay buông dọc thân"})
V("13", [22, 23], "trung 50mm · SEBASTIAN NÉT giữa chìa áo khoác + ADRIAN NÉT phải đứng thẳng + JULIAN NÉT trái phía sau",
  [("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_VEST"), ("JULIAN", "JULIAN_TUX")],
  "SEBASTIAN, ADRIAN và JULIAN, cả ba rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "SEBASTIAN chìa chiếc áo khoác dạ đen ra bằng cả hai tay về phía ADRIAN",
  [("SEBASTIAN", "formal, deferential", 22), ("JULIAN", "hoarse, disbelieving", 23)])

S("14", "trung 50mm, cao 1m55, cách CRANE 2m4, đặt trong lòng nhà thờ nhìn về phía lối đi giữa",
  "BOARD CHAIRMAN CRANE đang đi tới ở nửa TRÁI khung giữa lối đi, một tay khẽ gạt các cụm khách sang bên. "
  "GERALD HALE đứng ở nửa PHẢI khung, đã quay hẳn lại nhìn ông. " + KHACH,
  "BOARD CHAIRMAN CRANE một tay khẽ gạt sang bên xin đường, tay kia cầm chiếc áo khoác dạ gấp. "
  "GERALD HALE một tay đưa lên chỉ về phía CRANE.",
  "BOARD CHAIRMAN CRANE nhìn thẳng về phía cuối lối đi ngoài khung. GERALD HALE nhìn CRANE.",
  "BOARD CHAIRMAN CRANE — người sáu mươi bảy tuổi đi qua một đám cưới như đi qua một hành lang công ty: "
  "mặt trang trọng, mắt thẳng. GERALD HALE — nhận ra mặt ông ta: mắt mở to, giọng khàn.",
  "đúng khoảnh khắc ngay TRƯỚC khi BOARD CHAIRMAN CRANE dừng lại ở cuối lối đi",
  ["BOARD CHAIRMAN CRANE", "GERALD HALE"], "giữa lối đi cuối nhà thờ",
  {"BOARD CHAIRMAN CRANE": "đang đi tới ở nửa trái khung", "GERALD HALE": "đứng nửa phải khung"},
  "cách nhau ba bước", {"BOARD CHAIRMAN CRANE": "một tay khẽ gạt sang bên xin đường, tay kia cầm áo khoác gấp",
                        "GERALD HALE": "một tay chỉ về phía CRANE"})
V("14", [24, 25], "trung 50mm · BOARD CHAIRMAN CRANE NÉT trái đang đi tới + GERALD HALE NÉT phải · khách nền mờ",
  [("BOARD CHAIRMAN CRANE", "BOARD CHAIRMAN CRANE"), ("GERALD HALE", "GERALD HALE")],
  "BOARD CHAIRMAN CRANE và GERALD HALE, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "BOARD CHAIRMAN CRANE đi giữa lối đi, khẽ gạt các cụm khách sang bên",
  [("BOARD CHAIRMAN CRANE", "polite, formal", 24), ("GERALD HALE", "hoarse, recognising", 25)])

S("15", "cận-trung 85mm, cao 1m55, cách ADRIAN 1m7, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "BOARD CHAIRMAN CRANE đứng ở nửa TRÁI khung, đã cúi đầu một chút. ADRIAN đứng thẳng ở nửa PHẢI khung, "
  "áo khoác dạ đen đã khoác trên vai. Hậu cảnh là lối đi và các cụm khách mờ.",
  "BOARD CHAIRMAN CRANE hai tay giữ chiếc áo khoác gấp trước bụng. ADRIAN một tay chỉnh lại vạt áo khoác trên vai.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "BOARD CHAIRMAN CRANE — báo cáo với sếp mình giữa một đám cưới của người khác: mặt trang trọng, giọng rõ. "
  "ADRIAN — chào lại bằng đúng một cái tên: mặt bình, mắt tĩnh.",
  "đúng khoảnh khắc ngay TRƯỚC khi BOARD CHAIRMAN CRANE gọi chức danh đầy đủ của anh",
  ["BOARD CHAIRMAN CRANE", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"BOARD CHAIRMAN CRANE": "đứng nửa trái khung", "ADRIAN": "đứng thẳng nửa phải khung"},
  "cách nhau một bước", {"BOARD CHAIRMAN CRANE": "hai tay giữ chiếc áo khoác gấp trước bụng",
                         "ADRIAN": "một tay chỉnh lại vạt áo khoác trên vai"})
V("15", [26, 27, 28], "cận-trung 85mm · BOARD CHAIRMAN CRANE NÉT trái + ADRIAN NÉT phải đứng thẳng",
  [("BOARD CHAIRMAN CRANE", "BOARD CHAIRMAN CRANE"), ("ADRIAN", "ADRIAN_VEST")],
  "BOARD CHAIRMAN CRANE và ADRIAN, cả hai rõ mặt. ADRIAN ĐỨNG THẲNG TRÊN HAI CHÂN. "
  "Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "BOARD CHAIRMAN CRANE cúi đầu một chút và báo cáo",
  [("BOARD CHAIRMAN CRANE", "formal, deferential", 26), ("ADRIAN", "quiet, level", 27),
   ("BOARD CHAIRMAN CRANE", "formal, respectful", 28)])

S("16", "trung 50mm, cao 1m55, cách VANESSA 2m2, đặt trong lòng nhà thờ lấy cả hai người",
  "VANESSA đứng ở nửa PHẢI khung trong váy cưới, mặt trắng ra. GERALD HALE đứng ở nửa TRÁI khung cạnh cô. "
  + KHACH,
  "VANESSA một tay đưa lên nắm lấy cổ áo cưới của mình. GERALD HALE một tay chỉ về phía ADRIAN ngoài khung.",
  "Cả hai nhìn về phía ADRIAN ngoài khung.",
  "VANESSA — người vừa nghe đúng một chữ và hiểu ra toàn bộ: mặt trắng, môi hé, mắt mở to. "
  "GERALD HALE — vẫn đang bám vào những gì mình biết: giọng cao, lắc đầu.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN quay đầu về phía họ",
  ["VANESSA_CODAU", "GERALD HALE"], "giữa lòng nhà thờ, gần chỗ ADRIAN đứng",
  {"VANESSA": "đứng nửa phải khung", "GERALD HALE": "đứng nửa trái khung"},
  "sát cạnh nhau", {"VANESSA": "một tay nắm lấy cổ áo cưới của mình",
                    "GERALD HALE": "một tay chỉ về phía ADRIAN ngoài khung"})
V("16", [29, 30], "trung 50mm · GERALD HALE NÉT trái + VANESSA NÉT phải, cùng nhìn về phía ADRIAN · khách nền mờ",
  [("GERALD HALE", "GERALD HALE"), ("VANESSA", "VANESSA_CODAU")],
  "GERALD HALE và VANESSA, cả hai rõ mặt. Khách khác mờ ở hậu cảnh, không ai nhìn vào camera.",
  "VANESSA nắm lấy cổ áo cưới của mình, GERALD HALE lắc đầu và chỉ về phía ADRIAN",
  [("VANESSA", "hoarse, dawning", 29), ("GERALD HALE", "loud, denying", 30)])

S("17", "cận-trung 85mm, cao 1m55, cách ADRIAN 1m5, đặt trong lòng nhà thờ, lấy ADRIAN nét và MAYA cùng khung",
  "ADRIAN đứng thẳng ở nửa TRÁI khung, áo khoác dạ đen trên vai. MAYA đứng ở nửa PHẢI khung sát cạnh anh, "
  "áo vest khoác trên vai cô. Hậu cảnh là vòng khách vây quanh, mờ.",
  "ADRIAN một tay hơi mở ra ngang hông theo nhịp nói. MAYA một tay giữ vạt áo vest trước ngực.",
  "ADRIAN nhìn về phía cụm người đứng ngoài khung bên phải. MAYA nhìn ADRIAN.",
  "ADRIAN — người nói ra sự thật đơn giản nhất của cả sáu tháng: giọng đều, chậm, mắt tĩnh, KHÔNG đắc thắng. "
  "MAYA — nghe và bắt đầu hiểu ra mình đã sống cạnh ai: mắt mở to.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay hẳn người về phía anh",
  ["ADRIAN_VEST", "MAYA_TRANG"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng nửa trái khung", "MAYA": "đứng sát cạnh nửa phải khung"},
  "sát nhau", {"ADRIAN": "một tay hơi mở ra ngang hông", "MAYA": "một tay giữ vạt áo vest trước ngực"})
V("17", [31], "cận-trung 85mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT phải khoác áo vest · khách nền mờ",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "ADRIAN mở một bàn tay ra ngang hông và nói ra cả gian phòng",
  [("ADRIAN", "even, deliberate", 31)], [("MAYA", "silent, eyes widening")])

S("18", "two-shot cận-trung 85mm, cao 1m55, cách MAYA 1m6, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "MAYA đứng ở nửa PHẢI khung, đã quay hẳn về phía ADRIAN. ADRIAN đứng thẳng ở nửa TRÁI khung. "
  "Hậu cảnh là vòng khách vây quanh mờ và ánh đèn pha lê.",
  "MAYA một tay còn giữ vạt áo vest, tay kia đưa lên rồi hạ xuống. ADRIAN hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau, rất gần.",
  "MAYA — người hỏi chồng mình là ai và biết mình sắp nghe câu trả lời làm đổi cả bốn tuần vừa qua: "
  "giọng nhỏ, mắt ướt. ADRIAN — nói ra tất cả trong một câu: mặt bình, mắt không rời, giọng rất rõ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA lùi lại nửa bước",
  ["MAYA_TRANG", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"MAYA": "đứng nửa phải khung, đã quay hẳn lại", "ADRIAN": "đứng thẳng nửa trái khung"},
  "rất gần nhau", {"MAYA": "một tay giữ vạt áo vest, tay kia đưa lên rồi hạ xuống",
                   "ADRIAN": "hai tay buông dọc thân"})
V("18", [32, 33], "two-shot cận-trung 85mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT phải quay hẳn về phía anh",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "MAYA quay hẳn người về phía anh, một tay đưa lên rồi hạ xuống",
  [("MAYA", "small, shaken", 32), ("ADRIAN", "quiet, plain", 33)])

S("19", "cận 85mm, cao 1m55, cách MAYA 1m3, máy sau vai TRÁI của ADRIAN; vai và gáy anh chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, đã lùi lại nửa bước, áo vest còn trên vai. ADRIAN chỉ còn là "
  "vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là vòng khách vây quanh mờ.",
  "MAYA một tay buông vạt áo vest ra, tay kia đưa lên ngang ngực rồi dừng.",
  "MAYA nhìn thẳng vào mặt ADRIAN.",
  "MAYA — người đang ghép từng mảnh lại với nhau và mỗi mảnh làm cô lùi thêm nửa bước: mắt mở to, "
  "giọng phẳng dần, mặt trắng ra.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nói ra tên toà nhà cuối cùng",
  ["MAYA_TRANG", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"MAYA": "đứng chính diện giữa khung, đã lùi nửa bước", "ADRIAN": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"MAYA": "một tay buông vạt áo vest, tay kia đưa lên ngang ngực rồi dừng",
                         "ADRIAN": "hai tay buông, ngoài vùng nét"})
V("19", [34, 35, 36, 37], "OTS cận 85mm · MAYA NÉT chính diện · vai và gáy ADRIAN tiền cảnh trái out nét",
  [("MAYA", "MAYA_TRANG"), ("ADRIAN", "ADRIAN_VEST")],
  "MAYA rõ mặt chính diện. ADRIAN chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA lùi lại nửa bước, buông vạt áo vest ra và hỏi từng câu một",
  [("MAYA", "flat, listing", 34), ("ADRIAN", "quiet, confirming", 35),
   ("MAYA", "flat, listing", 36), ("ADRIAN", "quiet, confirming", 37)])

S("20", "two-shot trung 50mm, cao 1m55, cách MAYA 2m, đặt trong lòng nhà thờ lấy cả hai người đứng",
  "MAYA đứng ở nửa PHẢI khung, ADRIAN đứng thẳng ở nửa TRÁI khung, giữa hai người có một khoảng cách một bước "
  "mà lúc nãy không có. Hậu cảnh là chiếc xe lăn tay cũ còn đổ nghiêng trên nền đá.",
  "MAYA hai tay buông dọc thân, áo vest tuột khỏi một bên vai. ADRIAN hai tay buông dọc thân.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người vừa hiểu ra rằng mọi lần mình đẩy anh qua thành phố này đều là một cuộc thử: "
  "mắt ướt, giọng phẳng, mặt cứng lại. ADRIAN — nhận hết, không né: mặt bình, mắt không rời.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi một chữ",
  ["MAYA_TRANG", "ADRIAN_VEST"], "giữa nền đá cuối nhà thờ",
  {"MAYA": "đứng nửa phải khung", "ADRIAN": "đứng thẳng nửa trái khung"},
  "cách nhau một bước", {"MAYA": "hai tay buông dọc thân, áo vest tuột khỏi một bên vai",
                         "ADRIAN": "hai tay buông dọc thân"})
V("20", [38, 39, 40, 41, 42], "two-shot trung 50mm · ADRIAN NÉT trái đứng thẳng + MAYA NÉT phải, cách nhau một bước",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA rõ mặt. Khách vây quanh mờ, không ai nhìn vào camera.",
  "MAYA đứng nguyên, hai tay buông dọc thân, hỏi từng câu một",
  [("MAYA", "flat, listing", 38), ("ADRIAN", "quiet, confirming", 39),
   ("MAYA", "hardening, quiet", 40), ("ADRIAN", "plain, owning it", 41),
   ("MAYA", "flat, demanding", 42)])

S("21", "cận 85mm, cao 1m55, cách ADRIAN 1m3, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN đứng chính diện chiếm phần lớn khung, áo khoác dạ đen trên vai. MAYA chỉ còn là vai và gáy ở rìa "
  "PHẢI tiền cảnh, ngoài vùng nét. Hậu cảnh là lối đi trải thảm trắng và vòng khách vây quanh mờ.",
  "ADRIAN một tay đưa lên ngang ngực rồi hạ xuống rất chậm.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người nói ra lý do thật của cả sáu tháng và biết nó không phải một lời xin lỗi đủ: giọng chậm, "
  "rõ từng chữ, mắt ướt lần đầu tiên trong cả bộ phim, mặt vẫn bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi bàn tay ADRIAN hạ hẳn xuống bên hông",
  ["ADRIAN_VEST", "MAYA_TRANG"], "giữa nền đá cuối nhà thờ",
  {"ADRIAN": "đứng thẳng chính diện giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"ADRIAN": "một tay đưa lên ngang ngực rồi hạ xuống chậm",
                         "MAYA": "hai tay buông, ngoài vùng nét"})
V("21", [43], "OTS cận 85mm · ADRIAN NÉT chính diện đứng thẳng · vai và gáy MAYA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_VEST"), ("MAYA", "MAYA_TRANG")],
  "ADRIAN rõ mặt chính diện, ĐỨNG THẲNG TRÊN HAI CHÂN. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "ADRIAN đưa một tay lên ngang ngực rồi hạ xuống rất chậm trong lúc nói",
  [("ADRIAN", "slow, confessing", 43)], [("MAYA", "silent, listening")])
