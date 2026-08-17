# -*- coding: utf-8 -*-
"""SCENE 5 — QUẦY VIỆN PHÍ ST. AGNES, 5 GIỜ 47 SÁNG. Hoá đơn đã bằng không."""
import qc
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S5", "REF_VIENPHI_RANGSANG", qc=qc.S5)

# ── NHỊP MỞ CẢNH ──
S("B1", "trung-rộng 35mm, cao 1m60, cách MAYA 5m, đặt sau quầy nhìn ra sảnh chờ",
  "MAYA vừa bước qua cửa kính hai cánh vào phòng viện phí và đang đi tới quầy, tay ôm một chiếc cặp tài liệu giấy màu nâu. "
  "Bốn hàng ghế chờ nhựa xanh hai bên gần như trống. Sau quầy chưa có ai ngồi.",
  "MAYA hai tay ôm chiếc cặp tài liệu giấy màu nâu ép vào ngực.",
  "MAYA nhìn thẳng vào ô cửa giao dịch ở giữa quầy.",
  "MAYA — người thức trắng đêm và tới đây từ trước giờ mở cửa: mắt hơi sưng nhưng tỉnh, quai hàm giữ, bước chân nhanh.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt tay lên mặt quầy",
  ["MAYA_KHOAC"], "sảnh chờ phòng viện phí, đang đi tới quầy",
  {"MAYA": "đi một mình về phía quầy"}, "một mình trong khung",
  {"MAYA": "hai tay ôm cặp tài liệu giấy nâu trước ngực"})
B("B1", "Mở cảnh. 5 giờ 47 sáng. MAYA bước vào phòng viện phí còn vắng, ôm một chiếc cặp tài liệu giấy màu nâu.",
  "trung-rộng 35mm · MAYA NÉT đi một mình về phía quầy · không có ai khác trong khung",
  [("MAYA", "MAYA_KHOAC")],
  "CHỈ MỘT MÌNH MAYA trong khung, rõ mặt, đang đi tới quầy. Không có người nào khác trong phòng.",
  "một người thức trắng đêm đã tới đây trước cả giờ mở cửa, mang theo tất cả những gì mình còn, và biết rằng "
  "nó không đủ.",
  "MAYA đi nhanh qua các hàng ghế trống, ôm chặt chiếc cặp tài liệu; đèn huỳnh quang trên trần nhấp một cái rồi sáng đều; "
  "ngoài cửa sổ bên phải, trời rạng dần.",
  "Ambient tiếng ù của đèn huỳnh quang và tiếng máy lạnh, SFX tiếng giày trên sàn vinyl.",
  nhac("NGHỈ", "Cả đêm dồn nén vừa qua cần một khoảng thở trước khi tin tốt bất ngờ giáng xuống — và nhạc phải giữ trung tính để cú lật không bị báo trước.",
       "Ambient piano at 56 BPM; one upright piano placing single notes with long gaps, a female voice humming very "
       "softly far back in the mix, entering twice; no drums, no bass; the pull is a long silence before the final "
       "note; wordless and neutral, dry early-morning mix, female vocal, piano, ambient, still",
       "Ambient instrumental at 54 BPM; a warm pad breathing slowly under one felt-piano note repeating every four "
       "seconds, a faint fluorescent-like hum underneath, no percussion, no arc, fading out; "
       "extremely soft mix, piano, pad, minimal, sleepless"),
  dur=8)

# ── QUẦY VIỆN PHÍ ──
S("01", "two-shot trung 50mm, cao 1m50, cách MAYA 2m2, đặt chếch bên quầy lấy cả hai người qua ô cửa giao dịch",
  "MAYA đứng ở nửa PHẢI khung trước quầy, hai tay chống lên mặt quầy. BILLING CLERK ngồi ở nửa TRÁI khung sau quầy, "
  "sau tấm kính chắn có ô cửa khoét dưới, trước mặt là màn hình máy tính đời cũ.",
  "MAYA hai tay chống lên mặt quầy, chiếc cặp tài liệu giấy màu nâu đặt xuống cạnh tay. "
  "BILLING CLERK một tay đặt trên bàn phím, tay kia cầm chuột.",
  "MAYA nhìn thẳng vào mặt BILLING CLERK qua ô cửa. BILLING CLERK nhìn MAYA rồi quay sang màn hình.",
  "MAYA — người nói một mạch cho hết trước khi bị ngắt: giọng nhanh, rõ, mắt không chớp. "
  "BILLING CLERK — vừa vào ca và nhận ra người đứng trước mặt: mày nhướn, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi BILLING CLERK gõ phím đầu tiên",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng trước quầy nửa phải khung", "BILLING CLERK": "ngồi sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "hai tay chống lên mặt quầy",
                             "BILLING CLERK": "một tay trên bàn phím, tay kia cầm chuột"})
V("01", [0, 1], "two-shot trung 50mm · MAYA NÉT phải trước quầy + BILLING CLERK NÉT trái sau quầy",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA và BILLING CLERK, cả hai rõ mặt hai bên quầy. Không có ai khác trong phòng.",
  "MAYA chống hai tay lên mặt quầy và nói một mạch, BILLING CLERK quay sang màn hình gõ phím",
  [("MAYA", "urgent, clear", 0), ("BILLING CLERK", "brisk, kind", 1)])

S("02", "cận-trung 85mm, cao 1m50, cách MAYA 1m6, máy sau vai PHẢI của BILLING CLERK; vai và gáy bà chiếm rìa trái, out nét",
  "MAYA đứng chính diện chiếm phần lớn khung, chiếc cặp tài liệu giấy màu nâu đã mở nắp trong tay. BILLING CLERK chỉ còn "
  "là vai và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh sau lưng MAYA là các hàng ghế chờ nhựa xanh.",
  "MAYA hai tay rút từ cặp tài liệu ra một xấp giấy tờ và đặt lên mặt quầy, ngón cái vuốt cho mép giấy thẳng.",
  "MAYA nhìn thẳng vào mặt BILLING CLERK qua ô cửa.",
  "MAYA — người đã bán hết mọi thứ và đang xin đúng hai tuần: giọng nhanh, hơi vấp một lần, mắt đỏ, "
  "vẫn giữ được thẳng lưng.",
  "đúng khoảnh khắc ngay TRƯỚC khi BILLING CLERK cắt lời cô lần thứ nhất",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng chính diện giữa khung", "BILLING CLERK": "vai và gáy tiền cảnh trái"},
  "cách nhau một mặt quầy", {"MAYA": "hai tay đặt xấp giấy tờ lên quầy",
                             "BILLING CLERK": "hai tay trên bàn phím, ngoài vùng nét"})
V("02", [2, 3], "OTS cận-trung 85mm · MAYA NÉT chính diện · vai và gáy BILLING CLERK tiền cảnh trái out nét",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA rõ mặt chính diện. BILLING CLERK chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA rút xấp giấy tờ ra khỏi cặp tài liệu và đặt lên mặt quầy",
  [("MAYA", "fast, pleading", 2), ("BILLING CLERK", "gentle, interrupting", 3)])

S("03", "trung 50mm, cao 1m50, cách MAYA 2m2, đặt chếch bên quầy lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, hai tay còn đặt trên xấp giấy tờ. BILLING CLERK ngồi ở nửa TRÁI khung, đã bỏ tay khỏi "
  "bàn phím và đưa một tay lên ra hiệu dừng lại.",
  "MAYA hai tay đè lên xấp giấy tờ trên quầy. BILLING CLERK một tay giơ lên ngang ngực, lòng bàn tay hướng ra ngoài; "
  "tay kia xoay MÀN HÌNH MÁY TÍNH về phía ô cửa giao dịch.",
  "MAYA nhìn BILLING CLERK. BILLING CLERK nhìn MAYA rồi hất cằm về phía màn hình.",
  "MAYA — người vẫn đang bồi thêm mọi thứ mình có thể ký: giọng gấp. "
  "BILLING CLERK — muốn cắt ngang để đưa ra một tin mà chính bà cũng chưa tin: mày nhướn cao, giọng to hơn một chút.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhìn sang màn hình",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng trước quầy nửa phải khung", "BILLING CLERK": "ngồi sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "hai tay đè lên xấp giấy tờ",
                             "BILLING CLERK": "một tay giơ ngang ngực, tay kia xoay màn hình"})
V("03", [4, 5], "trung 50mm · MAYA NÉT phải trước quầy + BILLING CLERK NÉT trái sau quầy",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA và BILLING CLERK, cả hai rõ mặt hai bên quầy. Không có ai khác trong phòng.",
  "MAYA còn đang nói thì BILLING CLERK giơ tay ra hiệu dừng và xoay màn hình máy tính về phía cô",
  [("MAYA", "desperate, fast", 4), ("BILLING CLERK", "raised, urgent", 5)])

S("04", "cận 85mm, cao 1m50, cách MAYA 1m2, đặt chính diện, hậu cảnh là hàng ghế chờ xoá phông",
  "MAYA đứng chiếm phần lớn khung từ ngực trở lên, đầu hơi nghiêng về phía màn hình máy tính đặt ngoài rìa TRÁI khung. "
  "Ở rìa TRÁI khung thấy một mảng vai của BILLING CLERK, out nét.",
  "MAYA một tay đưa lên bám vào mép tấm kính chắn của quầy.",
  "MAYA nhìn chăm chăm vào màn hình máy tính ngoài rìa khung.",
  "MAYA — người đang đọc một dòng số và chưa dám hiểu nó: mày chau, mắt hơi nheo, môi hé.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay mặt lại phía BILLING CLERK",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng chính diện giữa khung", "BILLING CLERK": "một mảng vai rìa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "một tay bám mép tấm kính chắn",
                             "BILLING CLERK": "một tay trên chuột, ngoài vùng nét"})
V("04", [6, 7], "cận 85mm · MAYA NÉT chính diện nhìn màn hình · một mảng vai BILLING CLERK rìa trái out nét",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA rõ mặt. BILLING CLERK chỉ thấy MỘT MẢNG VAI ở rìa trái, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA bám tay vào mép tấm kính và nghiêng đầu đọc màn hình",
  [("MAYA", "confused, quiet", 6), ("BILLING CLERK", "plain, careful", 7)])

S("05", "two-shot trung 50mm, cao 1m50, cách MAYA 2m, đặt chếch bên quầy lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, người đã nghiêng hẳn về phía ô cửa giao dịch. BILLING CLERK ngồi ở nửa TRÁI khung, "
  "một tay đặt trên màn hình đã xoay, tay kia chỉ vào một dòng trên đó.",
  "MAYA một tay bám mép quầy, tay kia buông thõng. BILLING CLERK một tay giữ mép màn hình, ngón trỏ tay kia "
  "chỉ vào một dòng.",
  "Hai người nhìn thẳng vào mắt nhau qua ô cửa.",
  "MAYA — người đã quá quen với việc hệ thống báo sai và không cho phép mình mừng: giọng phẳng, mắt cảnh giác. "
  "BILLING CLERK — chắc chắn về thứ mình vừa đọc: lắc đầu một cái, giọng chậm lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi BILLING CLERK gõ tiếp để mở chi tiết giao dịch",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng nghiêng về ô cửa nửa phải khung", "BILLING CLERK": "ngồi sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "một tay bám mép quầy",
                             "BILLING CLERK": "một tay giữ mép màn hình, tay kia chỉ vào một dòng"})
V("05", [8, 9], "two-shot trung 50mm · MAYA NÉT phải trước quầy + BILLING CLERK NÉT trái chỉ vào màn hình",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA và BILLING CLERK, cả hai rõ mặt hai bên quầy. Không có ai khác trong phòng.",
  "BILLING CLERK chỉ ngón tay vào một dòng trên màn hình, MAYA nghiêng hẳn người về phía ô cửa",
  [("MAYA", "flat, disbelieving", 8), ("BILLING CLERK", "certain, slower", 9)])

S("06", "cận-trung 85mm, cao 1m50, cách BILLING CLERK 1m6, máy sau vai TRÁI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "BILLING CLERK ngồi sau quầy chiếm phần lớn khung, sau lưng bà là dãy tủ hồ sơ kim loại màu ghi. MAYA chỉ còn là "
  "vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét.",
  "BILLING CLERK hai tay đặt lên bàn phím, người hơi ngả về phía màn hình; giữa câu, một tay bà nhấc lên khỏi phím.",
  "BILLING CLERK nhìn màn hình rồi ngước lên nhìn thẳng vào mặt MAYA qua vai cô.",
  "BILLING CLERK — người làm ở cái quầy này mười một năm và chưa từng thấy chuyện như vậy: mắt mở to sau cặp kính, "
  "giọng hạ xuống gần thành thì thầm.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA hỏi tiếp về lệnh rút máy thở",
  ["BILLING CLERK", "MAYA_KHOAC"], "hai bên quầy viện phí",
  {"BILLING CLERK": "ngồi sau quầy giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một mặt quầy", {"BILLING CLERK": "hai tay trên bàn phím, một tay nhấc lên giữa câu",
                             "MAYA": "một tay bám mép quầy, ngoài vùng nét"})
V("06", [10, 11], "OTS cận-trung 85mm · BILLING CLERK NÉT sau quầy · vai và gáy MAYA tiền cảnh phải out nét",
  [("BILLING CLERK", "BILLING CLERK"), ("MAYA", "MAYA_KHOAC")],
  "BILLING CLERK rõ mặt sau quầy. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA hỏi, BILLING CLERK đọc từ màn hình rồi ngước lên hạ giọng xuống",
  [("MAYA", "quiet, pressing", 10), ("BILLING CLERK", "hushed, amazed", 11)])

S("07", "trung 50mm, cao 1m50, cách MAYA 2m2, đặt chếch bên quầy lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, một tay đã rời khỏi quầy. BILLING CLERK ngồi ở nửa TRÁI khung, đang cuộn chuột "
  "và đọc một dòng ghi chú trên màn hình.",
  "MAYA một tay đưa lên che miệng rồi hạ xuống ngang cổ. BILLING CLERK một tay cuộn chuột, tay kia lần theo dòng chữ "
  "trên màn hình.",
  "MAYA nhìn BILLING CLERK. BILLING CLERK nhìn màn hình.",
  "MAYA — người vừa nghe rằng cái hạn chót đã bị huỷ và chân bắt đầu mềm ra: mắt ướt, môi run một nhịp. "
  "BILLING CLERK — đọc lại ghi chú vì thấy nó lạ: mày chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đưa tay bám vào mép quầy cho khỏi ngã",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng trước quầy nửa phải khung", "BILLING CLERK": "ngồi sau quầy nửa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "một tay che miệng rồi hạ xuống ngang cổ",
                             "BILLING CLERK": "một tay cuộn chuột, tay kia lần theo dòng chữ"})
V("07", [12, 13], "trung 50mm · MAYA NÉT phải trước quầy + BILLING CLERK NÉT trái đọc màn hình",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA và BILLING CLERK, cả hai rõ mặt hai bên quầy. Không có ai khác trong phòng.",
  "MAYA đưa tay lên che miệng rồi hạ xuống, BILLING CLERK cuộn chuột đọc dòng ghi chú",
  [("MAYA", "small, unsteady", 12), ("BILLING CLERK", "puzzled, reading", 13)])

S("08", "cận 85mm, cao 1m50, cách MAYA 1m2, đặt chính diện, hậu cảnh là hàng ghế chờ và cửa kính xoá phông",
  "MAYA đứng chiếm phần lớn khung từ ngực trở lên, một tay bám chặt mép quầy. Ở rìa TRÁI khung thấy một mảng vai "
  "của BILLING CLERK, out nét.",
  "MAYA một tay bám chặt mép quầy, các khớp ngón trắng ra.",
  "MAYA nhìn thẳng vào mặt BILLING CLERK.",
  "MAYA — người vừa hiểu rằng có ai đó đã cố ý chặn mọi câu hỏi để cô khỏi lo, và không biết nên thấy thế nào: "
  "mắt mở to, môi hé, mặt trắng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA buông tay khỏi mép quầy",
  ["MAYA_KHOAC", "BILLING CLERK"], "hai bên quầy viện phí",
  {"MAYA": "đứng chính diện giữa khung", "BILLING CLERK": "một mảng vai rìa trái khung"},
  "cách nhau một mặt quầy", {"MAYA": "một tay bám chặt mép quầy",
                             "BILLING CLERK": "một tay trên chuột, ngoài vùng nét"})
V("08", [14, 15], "cận 85mm · MAYA NÉT chính diện · một mảng vai BILLING CLERK rìa trái out nét",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA rõ mặt. BILLING CLERK chỉ thấy MỘT MẢNG VAI ở rìa trái, out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA bám chặt mép quầy, các khớp ngón trắng ra",
  [("MAYA", "stunned, small", 14), ("BILLING CLERK", "gentle, concerned", 15)],
  ketclip="Cuối clip, MAYA buông tay khỏi mép quầy và lùi hai bước ra giữa sảnh chờ, đứng lại giữa hai hàng ghế. "
          "Clip dừng đúng lúc cô đứng lại.")

S("09", "trung 50mm, cao 1m50, cách MAYA 2m6, đặt phía quầy nhìn ra sảnh chờ",
  "MAYA đứng một mình giữa sảnh chờ ở nửa PHẢI khung, giữa hai hàng ghế nhựa xanh, xấp giấy tờ còn để lại trên quầy. "
  "BILLING CLERK ngồi ở nửa TRÁI khung phía sau quầy, đã nhổm người lên nhìn theo cô.",
  "MAYA hai tay buông thõng hai bên, các ngón mở. BILLING CLERK một tay chống lên mặt quầy để nhổm người.",
  "MAYA nhìn về phía cửa kính hai cánh cuối phòng. BILLING CLERK nhìn theo MAYA.",
  "MAYA — người vừa hiểu ra người đàn ông trong xe lăn đã nói thật, và cả cơ thể mới bắt đầu tin: mắt mở, "
  "hơi thở sâu, khoé môi động. BILLING CLERK — lo cho người đang đứng giữa phòng: mày chau.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước bước đầu tiên về phía cửa",
  ["MAYA_KHOAC", "BILLING CLERK"], "sảnh chờ và quầy viện phí",
  {"MAYA": "đứng một mình giữa sảnh chờ nửa phải khung", "BILLING CLERK": "nhổm người sau quầy nửa trái khung"},
  "cách nhau bốn mét", {"MAYA": "hai tay buông thõng hai bên", "BILLING CLERK": "một tay chống lên mặt quầy"})
V("09", [16], "trung 50mm · MAYA NÉT phải đứng giữa sảnh chờ + BILLING CLERK NÉT trái nhổm người sau quầy",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA và BILLING CLERK, cả hai rõ mặt. Không có ai khác trong phòng.",
  "MAYA đứng lại giữa hai hàng ghế, hai tay buông thõng, nói gần như với chính mình",
  [("MAYA", "quiet, dazed", 16)], [("BILLING CLERK", "silent, watching her")])

# ── NHỊP KHÉP CẢNH ──
S("B2", "toàn cảnh 24mm, cao 1m60, cách MAYA 8m, đặt ở góc sảnh chờ nhìn chếch qua cả phòng",
  "MAYA đứng một mình giữa sảnh chờ, giữa bốn hàng ghế nhựa xanh trống. Quầy viện phí ở phía sau bên trái khung, "
  "BILLING CLERK đã ngồi xuống lại sau quầy, nhỏ và xa trong khung. Ngoài dãy cửa sổ bên phải, trời đã hửng sáng.",
  "MAYA hai tay buông xuôi hai bên. BILLING CLERK hai tay đặt trên bàn phím.",
  "MAYA nhìn xuống sàn vinyl trước mặt mình. BILLING CLERK nhìn xuống màn hình.",
  "MAYA — người vừa được cứu mà chưa kịp mừng vì chưa hiểu tại sao: mặt trống, vai buông hẳn xuống lần đầu tiên "
  "sau nhiều ngày. BILLING CLERK — trở lại công việc: mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi vệt nắng sớm đầu tiên chạm tới chân MAYA",
  ["MAYA_KHOAC", "BILLING CLERK"], "sảnh chờ phòng viện phí",
  {"MAYA": "đứng một mình giữa sảnh chờ", "BILLING CLERK": "ngồi sau quầy, xa trong khung"},
  "cách nhau sáu mét", {"MAYA": "hai tay buông xuôi", "BILLING CLERK": "hai tay trên bàn phím"})
B("B2", "Khép cảnh. Hoá đơn đã bằng không. MAYA đứng một mình giữa sảnh chờ trong ánh rạng sáng đầu tiên.",
  "toàn cảnh 24mm · MAYA NÉT đứng một mình giữa sảnh chờ + BILLING CLERK NÉT nhỏ ở xa sau quầy",
  [("MAYA", "MAYA_KHOAC"), ("BILLING CLERK", "BILLING CLERK")],
  "MAYA rõ mặt đứng giữa sảnh chờ, BILLING CLERK rõ mặt nhưng nhỏ và xa phía sau quầy. Không có ai khác trong phòng.",
  "một người vừa được cứu bởi một người lạ và chưa hiểu vì sao; sự nhẹ nhõm này chưa có chỗ để đặt xuống.",
  "MAYA đứng yên rất lâu giữa hai hàng ghế trống; ngoài cửa sổ, trời hửng dần và một vệt nắng sớm bò vào sàn "
  "về phía chân cô; BILLING CLERK sau quầy quay lại với màn hình.",
  "Ambient tiếng ù đèn huỳnh quang và tiếng máy in xa, SFX một tiếng chuông thang máy rất khẽ ngoài hành lang.",
  nhac("NÂNG", "Mốc lật của chương một: cái chết đã bị đẩy lùi. Nhạc được phép dâng, nhưng phải rút về mộc vì cô vẫn chưa biết mình vừa mắc nợ ai.",
       "Cinematic soul at 78 BPM; Rhodes and upright bass entering first, a female alto singing low and close after "
       "six seconds, strings rising underneath and a soft kick joining at the midpoint, then everything dropping away "
       "to voice and Rhodes for the last phrase; lyrics about a debt disappearing overnight and being afraid to "
       "believe it, grateful and unsteady, never triumphant; warm analog mix, female vocal, soul, strings, hopeful",
       "Cinematic instrumental at 76 BPM; Rhodes playing a rising four-chord figure, cello entering underneath, "
       "a string section swelling once at the midpoint then pulling back, a single soft kick in the final bars, "
       "ending open and unresolved; warm analog mix, Rhodes, cello, strings, hopeful, unresolved"),
  dur=10)
