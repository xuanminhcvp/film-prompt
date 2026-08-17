# -*- coding: utf-8 -*-
"""SCENE 7 — NHÀ CỔNG CŨ, DINH THỰ KANE (chiều). Ba bậc đá không có dốc."""
from lib import mk, nhac

SFS, SHOTS, S, V, VX, B = mk("S7", "REF_CONGNHA_CHIEU")
TRONG = "REF_NHACONG_CHIEU"

# ── NHỊP MỞ CẢNH ──
S("B1", "toàn cảnh 24mm, cao 1m60, cách MAYA 9m, đặt trên đường phục vụ nhìn về phía cổng sắt và căn nhà cổng",
  "MAYA đứng ở giữa đường phục vụ, vừa xuống xe, mặt ngẩng nhìn cổng sắt lớn và toà nhà chính trên đồi phía sau. "
  "ADRIAN ngồi trong xe lăn ngay bên phải cô. SEBASTIAN đứng lùi sau hai người một bước, cạnh một chiếc va li.",
  "MAYA một tay che ngang trán chắn nắng chiều. ADRIAN hai tay đặt trên vành tay vịn. "
  "SEBASTIAN một tay cầm quai chiếc va li vải đặt dưới đất.",
  "MAYA nhìn lên toà nhà chính ở xa trên đồi. ADRIAN nhìn thẳng về phía căn nhà cổng bên phải. "
  "SEBASTIAN nhìn MAYA.",
  "MAYA — người lần đầu nhìn thấy quy mô của thứ mình vừa lấy chồng vào: mắt mở to, môi hé. "
  "ADRIAN — không nhìn lên đồi một lần nào: mặt bình. SEBASTIAN — chờ phản ứng của cô: mày hơi nhướn.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay sang hỏi SEBASTIAN",
  ["MAYA_THUONG", "ADRIAN_TUTE", "SEBASTIAN"], "giữa đường phục vụ trước cổng sắt",
  {"MAYA": "đứng giữa đường phục vụ", "ADRIAN": "ngồi xe lăn bên phải MAYA",
   "SEBASTIAN": "đứng lùi sau một bước cạnh chiếc va li"},
  "ba người trong vòng hai mét",
  {"MAYA": "một tay che trán chắn nắng", "ADRIAN": "hai tay trên vành tay vịn",
   "SEBASTIAN": "một tay cầm quai va li"})
B("B1", "Mở cảnh. Xe vừa dừng trên đường phục vụ. MAYA lần đầu nhìn thấy cổng sắt và toà dinh thự trên đồi.",
  "toàn cảnh 24mm · MAYA NÉT giữa đường + ADRIAN NÉT ngồi xe lăn bên phải + SEBASTIAN NÉT lùi sau một bước",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_TUTE"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA, ADRIAN và SEBASTIAN rõ mặt. Không có ai khác trong khung.",
  "một người vừa nhìn thấy quy mô thật của gia đình mà mình vừa lấy vào, và cách nó đối xử với người trong nhà "
  "thì cô sắp thấy trong ba mươi giây nữa.",
  "MAYA ngẩng nhìn cổng sắt rồi đưa mắt lên đồi; nắng chiều thấp làm cô phải che trán; ADRIAN không nhìn theo, "
  "anh nhìn thẳng về phía căn nhà cổng mái vá bạt bên phải.",
  "Ambient tiếng gió qua hàng cây phong và tiếng chim chiều, SFX tiếng sỏi lạo xạo dưới chân.",
  nhac("NÂNG", "Mốc sang chương: nhân vật bước vào thế giới của nhà Kane. Nhạc tạo đà nhưng phải gợn lạnh, vì nơi này không phải chỗ tốt lành.",
       "Cinematic folk at 80 BPM; acoustic guitar picking a rising figure, a low cello entering underneath after "
       "four seconds, a female alto singing two short lines low and close; strings swell once then pull back; "
       "no drums; lyrics about standing at a gate that was never built for you; warm analog mix, female vocal, "
       "guitar, cello, cinematic, uneasy",
       "Cinematic instrumental at 78 BPM; acoustic guitar arpeggio over a sustained cello note, a French horn "
       "entering once far back, one string swell at the midpoint pulling straight back to guitar, no percussion, "
       "ending open; warm analog mix, guitar, cello, horn, cinematic, uneasy"),
  dur=8)

# ── NGOÀI SÂN ──
S("01", "trung 50mm, cao 1m40, cách MAYA 2m4, đặt trên đường phục vụ, hạ thấp để lấy cả người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã quay người về phía SEBASTIAN. SEBASTIAN đứng ở nửa TRÁI khung. "
  "Hậu cảnh sau lưng hai người là cổng sắt uốn đen và đường sỏi trắng vòng lên đồi.",
  "MAYA một tay còn chỉ về phía toà nhà chính trên đồi. SEBASTIAN hai tay chắp lại phía trước, tay phải giữ cổ tay trái.",
  "MAYA nhìn SEBASTIAN. SEBASTIAN nhìn lại MAYA.",
  "MAYA — người vừa đoán nhầm nơi mình sẽ ở: mày nhướn, giọng thật thà. "
  "SEBASTIAN — trả lời chính xác và không thêm gì: giọng đều, mắt hơi dời đi một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN quay người chỉ về phía căn nhà cổng",
  ["MAYA_THUONG", "SEBASTIAN"], "giữa đường phục vụ trước cổng sắt",
  {"MAYA": "đứng nửa phải khung", "SEBASTIAN": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "một tay chỉ về toà nhà chính trên đồi",
                         "SEBASTIAN": "hai tay chắp phía trước"})
V("01", [0, 1], "trung 50mm hạ thấp · MAYA NÉT phải + SEBASTIAN NÉT trái · cổng sắt và toà nhà chính ở hậu cảnh",
  [("MAYA", "MAYA_THUONG"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA và SEBASTIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA chỉ tay lên toà nhà chính trên đồi và hỏi, SEBASTIAN trả lời gọn",
  [("MAYA", "amazed, plain", 0), ("SEBASTIAN", "even, factual", 1)])

S("02", "trung 50mm, cao 1m40, cách MAYA 2m6, đặt chếch để thấy cả hai người và mặt tiền căn nhà cổng bên phải khung",
  "MAYA đứng ở nửa TRÁI khung, đã quay hẳn về phía căn nhà cổng. SEBASTIAN đứng ở nửa PHẢI khung, một tay chỉ về "
  "phía căn nhà gạch đỏ mái vá bạt xanh phía sau lưng ông.",
  "SEBASTIAN một tay chỉ về phía căn nhà cổng. MAYA hai tay buông xuống hai bên.",
  "MAYA nhìn theo hướng tay chỉ, quét từ mái bạt xuống tới ba bậc đá. SEBASTIAN nhìn MAYA.",
  "MAYA — người vừa hiểu ra chỗ mình sẽ ở là căn nhà nhỏ mái vá bạt chứ không phải toà nhà trên đồi: "
  "mắt mở, môi mím, KHÔNG chê bai. SEBASTIAN — nói ngắn vì biết câu này khó nghe: mặt bình.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bước lại gần ba bậc đá",
  ["MAYA_THUONG", "SEBASTIAN"], "giữa đường phục vụ, quay về phía căn nhà cổng",
  {"MAYA": "đứng nửa trái khung", "SEBASTIAN": "đứng nửa phải khung"},
  "cách nhau hai bước", {"SEBASTIAN": "một tay chỉ về phía căn nhà cổng", "MAYA": "hai tay buông xuống hai bên"})
V("02", [2, 3, 4], "trung 50mm · MAYA NÉT trái + SEBASTIAN NÉT phải chỉ về căn nhà cổng",
  [("MAYA", "MAYA_THUONG"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA và SEBASTIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "SEBASTIAN chỉ tay về phía căn nhà gạch đỏ mái vá bạt, MAYA quay theo và nhìn kỹ",
  [("MAYA", "plain, checking", 2), ("SEBASTIAN", "even, brief", 3), ("MAYA", "flat, observing", 4)])

S("03", "cận-trung 85mm, cao 1m40, cách MAYA 1m8, đặt cạnh ba bậc đá lấy MAYA nét và SEBASTIAN trong khung",
  "MAYA đứng ở nửa PHẢI khung, ngay dưới chân BA BẬC ĐÁ dẫn lên cửa gỗ nâu của căn nhà cổng. SEBASTIAN đứng ở "
  "nửa TRÁI khung, lùi lại một bước. Ba bậc đá và cửa gỗ chiếm rìa phải khung, KHÔNG có dốc xe lăn nào.",
  "MAYA một tay chỉ xuống ba bậc đá, tay kia chống hông. SEBASTIAN hai tay chắp phía trước.",
  "MAYA nhìn xuống ba bậc đá rồi ngước lên nhìn SEBASTIAN. SEBASTIAN nhìn MAYA.",
  "MAYA — người vừa nhìn thấy một điều vô lý đến mức phải hỏi lại cho chắc: mày chau sâu, giọng chậm lại. "
  "SEBASTIAN — trả lời bằng câu ngắn nhất có thể: mắt nhìn xuống một nhịp.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay lại nhìn chiếc xe lăn phía sau",
  ["MAYA_THUONG", "SEBASTIAN"], "chân ba bậc đá trước cửa nhà cổng",
  {"MAYA": "đứng nửa phải khung dưới chân bậc đá", "SEBASTIAN": "đứng nửa trái khung, lùi một bước"},
  "cách nhau hai bước", {"MAYA": "một tay chỉ xuống ba bậc đá, tay kia chống hông",
                         "SEBASTIAN": "hai tay chắp phía trước"})
V("03", [5, 6, 7], "cận-trung 85mm · MAYA NÉT phải dưới chân bậc đá + SEBASTIAN NÉT trái",
  [("MAYA", "MAYA_THUONG"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA và SEBASTIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA chỉ xuống ba bậc đá không có dốc và hỏi, SEBASTIAN trả lời bằng câu ngắn nhất",
  [("SEBASTIAN", "even, quiet", 5), ("MAYA", "slow, incredulous", 6), ("SEBASTIAN", "flat, plain", 7)])

S("04", "trung 50mm, cao 1m40, cách MAYA 2m2, đặt cạnh căn nhà cổng lấy cả hai người",
  "MAYA đứng ở nửa PHẢI khung, hai tay đã buông xuống. SEBASTIAN đứng ở nửa TRÁI khung. Phía sau hai người là "
  "tường gạch đỏ loang rêu của căn nhà cổng và một cửa sổ khung gỗ trắng đã tróc sơn.",
  "MAYA hai tay buông xuống hai bên, một tay nắm lại. SEBASTIAN một tay đưa lên chỉnh gọng kính rồi hạ xuống.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đang lắp các mốc thời gian lại với nhau và bắt đầu hiểu: mắt hơi nheo, quai hàm siết. "
  "SEBASTIAN — kể một chuyện mà ông đã nuốt xuống sáu tháng nay: giọng chậm, mắt cứng lại ở chữ cuối.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhắc lại hai chữ cuối cùng của ông",
  ["MAYA_THUONG", "SEBASTIAN"], "cạnh tường gạch căn nhà cổng",
  {"MAYA": "đứng nửa phải khung", "SEBASTIAN": "đứng nửa trái khung"},
  "cách nhau hai bước", {"MAYA": "hai tay buông, một tay nắm lại",
                         "SEBASTIAN": "một tay chỉnh gọng kính rồi hạ xuống"})
V("04", [8, 9], "trung 50mm · MAYA NÉT phải + SEBASTIAN NÉT trái · tường gạch nhà cổng ở hậu cảnh",
  [("MAYA", "MAYA_THUONG"), ("SEBASTIAN", "SEBASTIAN")],
  "MAYA và SEBASTIAN, cả hai rõ mặt. Không có ai khác trong khung.",
  "MAYA hỏi, SEBASTIAN chỉnh lại gọng kính rồi kể chậm",
  [("MAYA", "quiet, direct", 8), ("SEBASTIAN", "slow, restrained", 9)])

S("05", "trung 50mm, cao 1m40, cách ADRIAN 2m4, đặt chếch lấy cả ba người, ADRIAN gần máy nhất",
  "ADRIAN ngồi trong xe lăn ở nửa PHẢI khung tiền cảnh, đã quay đầu về phía hai người. MAYA đứng ở giữa khung "
  "phía sau anh, SEBASTIAN đứng ở nửa TRÁI khung. Hậu cảnh là đường phục vụ và cổng sắt.",
  "ADRIAN một tay hơi nhấc lên khỏi vành tay vịn ra hiệu dừng. MAYA hai tay buông. SEBASTIAN hai tay chắp phía trước.",
  "ADRIAN nhìn SEBASTIAN. MAYA nhìn ADRIAN. SEBASTIAN nhìn xuống ADRIAN.",
  "ADRIAN — người cắt ngang không phải vì giận mà vì không muốn nghe lại chuyện đó: giọng nhỏ, mặt bình. "
  "MAYA — nghe hai chữ đó và nhắc lại như để chắc mình nghe đúng: môi hé. SEBASTIAN — im ngay: cúi đầu một chút.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA quay hẳn về phía ADRIAN",
  ["ADRIAN_TUTE", "MAYA_THUONG", "SEBASTIAN"], "đường phục vụ trước căn nhà cổng",
  {"ADRIAN": "ngồi xe lăn nửa phải khung tiền cảnh", "MAYA": "đứng giữa khung phía sau ADRIAN",
   "SEBASTIAN": "đứng nửa trái khung"},
  "ba người trong vòng hai mét",
  {"ADRIAN": "một tay nhấc lên ra hiệu dừng", "MAYA": "hai tay buông", "SEBASTIAN": "hai tay chắp phía trước"})
V("05", [10, 11, 12], "trung 50mm · ADRIAN NÉT phải tiền cảnh ngồi xe lăn + MAYA NÉT giữa + SEBASTIAN NÉT trái",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_THUONG"), ("SEBASTIAN", "SEBASTIAN")],
  "ADRIAN, MAYA và SEBASTIAN, cả ba rõ mặt. Không có ai khác trong khung.",
  "MAYA nhắc lại hai chữ vừa nghe, SEBASTIAN đáp, ADRIAN nhấc tay ra hiệu dừng",
  [("MAYA", "quiet, testing", 10), ("SEBASTIAN", "flat, careful", 11), ("ADRIAN", "low, closing", 12)])

S("06", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m6, máy sau vai PHẢI của MAYA; vai và gáy cô chiếm rìa phải, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung. MAYA chỉ còn là vai và gáy ở rìa PHẢI tiền cảnh, ngoài vùng nét. "
  "Hậu cảnh sau lưng ADRIAN là bãi cỏ, cổng sắt đen và toà nhà chính trên đồi ở xa.",
  "ADRIAN hai tay đặt lại trên vành tay vịn, các ngón khép.",
  "ADRIAN nhìn thẳng vào mặt MAYA, không liếc lên đồi một lần nào.",
  "ADRIAN — người từ chối nhìn về phía ngôi nhà của chính gia đình mình: mặt hoàn toàn bình, mắt tĩnh, "
  "giọng rất nhỏ.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA chuyển sang hỏi chuyện khác",
  ["ADRIAN_TUTE", "MAYA_THUONG"], "đường phục vụ trước căn nhà cổng",
  {"ADRIAN": "ngồi xe lăn giữa khung", "MAYA": "vai và gáy tiền cảnh phải"},
  "cách nhau một bước", {"ADRIAN": "hai tay trên vành tay vịn", "MAYA": "hai tay buông, ngoài vùng nét"})
V("06", [13, 14], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn · vai và gáy MAYA tiền cảnh phải out nét",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_THUONG")],
  "ADRIAN rõ mặt ngồi trong xe lăn. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh phải, out nét — "
  "TUYỆT ĐỐI KHÔNG quay mặt về camera.",
  "MAYA hỏi về ngôi nhà trên đồi, ADRIAN không quay đầu nhìn lên đó",
  [("MAYA", "careful, curious", 13), ("ADRIAN", "flat, closing", 14)])

S("07", "trung 50mm, cao 1m40, cách MAYA 2m4, đặt cạnh nhà kho lấy cả ba người",
  "MAYA đứng ở giữa khung, đã quay sang phía nhà kho gỗ bên trái, một tay chỉ về phía đó. SEBASTIAN đứng ở nửa "
  "TRÁI khung cạnh cửa nhà kho đang hé. ADRIAN ngồi trong xe lăn ở nửa PHẢI khung, thấy rõ mặt.",
  "MAYA một tay chỉ về phía nhà kho, tay kia chống hông. SEBASTIAN một tay đẩy hé thêm cánh cửa nhà kho. "
  "ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn SEBASTIAN. SEBASTIAN nhìn vào trong nhà kho rồi nhìn MAYA. ADRIAN nhìn MAYA.",
  "MAYA — người vừa chuyển từ tức giận sang giải quyết vấn đề trong đúng một câu: giọng nhanh, dứt khoát. "
  "SEBASTIAN — bất ngờ vì được hỏi một câu thực tế: mày nhướn. ADRIAN — nhìn cô làm việc: mắt hơi nheo lại.",
  "đúng khoảnh khắc ngay TRƯỚC khi SEBASTIAN kéo tấm ván ép ra khỏi nhà kho",
  ["MAYA_THUONG", "SEBASTIAN", "ADRIAN_TUTE"], "trước cửa nhà kho gỗ cạnh căn nhà cổng",
  {"MAYA": "đứng giữa khung", "SEBASTIAN": "đứng nửa trái khung cạnh cửa nhà kho",
   "ADRIAN": "ngồi xe lăn nửa phải khung"},
  "ba người trong vòng ba mét",
  {"MAYA": "một tay chỉ về nhà kho, tay kia chống hông", "SEBASTIAN": "một tay đẩy hé cánh cửa nhà kho",
   "ADRIAN": "hai tay trên vành tay vịn"})
V("07", [15, 16], "trung 50mm · MAYA NÉT giữa + SEBASTIAN NÉT trái cạnh nhà kho + ADRIAN NÉT phải ngồi xe lăn",
  [("MAYA", "MAYA_THUONG"), ("SEBASTIAN", "SEBASTIAN"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA, SEBASTIAN và ADRIAN, cả ba rõ mặt. Không có ai khác trong khung.",
  "MAYA chỉ về phía nhà kho và hỏi một câu thực tế, SEBASTIAN đẩy hé cánh cửa nhìn vào trong",
  [("MAYA", "brisk, decisive", 15), ("SEBASTIAN", "surprised, helpful", 16)],
  ketclip="Cuối clip, SEBASTIAN kéo một tấm ván ép lớn ra khỏi nhà kho và đặt nghiêng lên ba bậc đá làm dốc tạm, "
          "MAYA đẩy chiếc xe lăn tới chân dốc. Clip dừng đúng lúc bánh xe chạm mép tấm ván.")

# ── NHỊP CHUYỂN VÀO TRONG NHÀ ──
S("B2", "trung-rộng 35mm, cao 1m40, cách MAYA 5m, đặt trong nhà nhìn ra cửa ra vào đang mở",
  "Nhìn từ bên trong gian phòng ra: cánh cửa gỗ nâu đã mở toang, MAYA đang đẩy chiếc xe lăn có ADRIAN ngồi lên "
  "tấm ván ép đặt nghiêng qua ngưỡng cửa. Ánh nắng chiều ngoài sân hắt vào thành một vệt sáng dài trên sàn ván gỗ.",
  "MAYA hai tay ghì chặt tay đẩy xe lăn, người đổ về phía trước. ADRIAN hai tay bám vành tay vịn.",
  "MAYA nhìn xuống bánh xe trước. ADRIAN nhìn thẳng vào trong phòng.",
  "MAYA — người đang dồn toàn bộ sức vào một cú đẩy và không định để ai giúp: quai hàm siết, hơi thở gấp. "
  "ADRIAN — lần đầu tiên được đưa vào nhà bằng đường chính chứ không phải bị bế: mặt bình, mắt hơi động.",
  "đúng khoảnh khắc ngay TRƯỚC khi bánh xe sau vượt qua ngưỡng cửa",
  ["MAYA_THUONG", "ADRIAN_TUTE"], "ngưỡng cửa ra vào căn nhà cổng, nhìn từ trong ra",
  {"MAYA": "đứng ngoài đẩy xe lăn lên tấm ván", "ADRIAN": "ngồi trong xe lăn trên tấm ván"},
  "MAYA sát sau ADRIAN", {"MAYA": "hai tay ghì tay đẩy xe lăn", "ADRIAN": "hai tay bám vành tay vịn"},
  bg=TRONG)
B("B2", "Nhịp chuyển vào trong nhà. MAYA đẩy chiếc xe lăn lên tấm ván ép đặt tạm qua ba bậc đá, vào gian phòng.",
  "trung-rộng 35mm · MAYA NÉT đẩy xe lăn ngoài ngưỡng cửa + ADRIAN NÉT ngồi trong xe lăn · không có ai khác",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN rõ mặt ở ngưỡng cửa. Không có người nào khác trong khung.",
  "sáu tháng nay chưa ai buồn làm cho người đàn ông này một cái dốc, và người vừa làm được điều đó bằng một tấm "
  "ván ép trong hai phút là người mới quen anh bốn ngày.",
  "MAYA ghì cả người vào cú đẩy cuối, bánh xe vượt ngưỡng cửa và lăn vào sàn ván gỗ; tấm ván ép rung một cái "
  "rồi đứng yên; vệt nắng chiều ngoài sân trải dài vào tận giữa phòng.",
  "SFX tiếng bánh xe lăn nghiến trên tấm ván ép và tiếng gỗ cọ vào bậc đá, Ambient tiếng gió ngoài sân.",
  nhac("NGHỈ", "Nhịp trước là vai NÂNG với guitar và dây; nhịp này phải đổi hẳn nhạc cụ dẫn và hạ xuống vai NGHỈ để cú đẩy nhỏ này không bị thổi phồng.",
       "Minimal soul at 66 BPM; Rhodes piano playing three chords very quietly, a female alto entering once with "
       "a single line half-spoken; no drums, no bass until the last bar; the pull is a full bar of silence at the "
       "midpoint; lyrics about a plank of wood and two minutes of somebody's attention; dry intimate mix, "
       "female vocal, Rhodes, minimal, warm",
       "Instrumental at 64 BPM; Rhodes piano alone playing three chords with long gaps, an upright bass entering "
       "on the last pass, no drums, no build, fading before it resolves; warm analog mix, Rhodes, upright bass, "
       "minimal, warm"),
  dur=8)

# ── TRONG NHÀ ──
S("08", "trung 50mm, cao 1m30, cách MAYA 2m2, đặt trong phòng, hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung cạnh chiếc bàn gỗ vuông giữa phòng, tay còn giữ tay đẩy xe lăn. ADRIAN ngồi trong "
  "xe lăn ở nửa TRÁI khung. Hậu cảnh là giường đơn khung sắt trắng và tủ đầu giường có đèn bàn.",
  "MAYA một tay rời tay đẩy và chống lên mép bàn gỗ. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống ADRIAN. ADRIAN ngước lên nhìn MAYA.",
  "MAYA — người vừa chuyển sang chế độ điều dưỡng và hỏi bằng giọng nghiệp vụ: mắt quét nhanh, giọng gọn. "
  "ADRIAN — không biết câu hỏi đó nghĩa là gì: mày nhướn, đầu hơi nghiêng.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA đặt túi đồ nghề xuống mặt bàn",
  ["MAYA_THUONG", "ADRIAN_TUTE"], "giữa gian phòng nhà cổng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng nửa phải khung cạnh bàn gỗ", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay chống mép bàn gỗ, tay kia trên tay đẩy xe lăn",
                         "ADRIAN": "hai tay trên vành tay vịn"}, bg=TRONG)
V("08", [17, 18], "trung 50mm hạ thấp · MAYA NÉT phải đứng cạnh bàn + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt trong gian phòng. Không có ai khác trong khung.",
  "MAYA rời tay khỏi tay đẩy, chống lên mép bàn và hỏi bằng giọng nghiệp vụ",
  [("MAYA", "brisk, clinical", 17), ("ADRIAN", "puzzled, plain", 18)])

S("09", "cận-trung 85mm, cao 1m30, cách ADRIAN 1m6, máy sau vai TRÁI của MAYA; vai và gáy cô chiếm rìa trái, out nét",
  "ADRIAN ngồi trong xe lăn chiếm phần lớn khung, ÁO CARDIGAN VÀ SƠ MI CÒN CÀI KÍN NGUYÊN. MAYA chỉ còn là vai "
  "và gáy ở rìa TRÁI tiền cảnh, ngoài vùng nét. Hậu cảnh là cửa sổ khung gỗ trắng có nắng chiều.",
  "ADRIAN một tay bám lấy vành tay vịn chặt hơn. MAYA một tay đưa ra phía trước, lòng bàn tay ngửa, chờ.",
  "ADRIAN nhìn thẳng vào mặt MAYA.",
  "ADRIAN — người vừa bị ra lệnh cởi áo bởi một người quen bốn ngày và mất đúng một nhịp để hiểu: mày nhướn cao, "
  "môi hé, KHÔNG khó chịu, chỉ bất ngờ.",
  "đúng khoảnh khắc ngay TRƯỚC khi ADRIAN đưa tay lên cúc áo cardigan",
  ["ADRIAN_TUTE", "MAYA_THUONG"], "giữa gian phòng nhà cổng",
  {"ADRIAN": "ngồi xe lăn giữa khung, áo còn cài kín", "MAYA": "vai và gáy tiền cảnh trái"},
  "cách nhau một bước", {"ADRIAN": "một tay bám chặt vành tay vịn",
                         "MAYA": "một tay đưa ra phía trước ngửa lên, ngoài vùng nét"}, bg=TRONG)
V("09", [19, 20], "OTS cận-trung 85mm · ADRIAN NÉT ngồi xe lăn, áo còn cài kín · vai và gáy MAYA tiền cảnh trái out nét",
  [("ADRIAN", "ADRIAN_TUTE"), ("MAYA", "MAYA_THUONG")],
  "ADRIAN rõ mặt ngồi trong xe lăn, ÁO VẪN CÀI KÍN NGUYÊN suốt clip. MAYA chỉ thấy VAI VÀ GÁY ở tiền cảnh trái, "
  "out nét — TUYỆT ĐỐI KHÔNG quay mặt về camera. Không ai cởi bỏ quần áo trong clip này.",
  "MAYA chìa tay ra chờ, ADRIAN mất đúng một nhịp mới hiểu ra",
  [("MAYA", "matter-of-fact, brisk", 19), ("ADRIAN", "taken aback, quiet", 20)])

S("10", "trung 50mm, cao 1m30, cách MAYA 2m, đặt trong phòng, hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, đã xắn tay áo len lên tới khuỷu. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, "
  "ÁO CÒN CÀI KÍN NGUYÊN. Trên mặt bàn gỗ cạnh hai người là một chậu nước inox và một chồng khăn bông trắng.",
  "MAYA một tay xắn nốt tay áo bên kia, tay kia chỉ vào lưng ghế xe lăn. ADRIAN hai tay đặt trên vành tay vịn.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "MAYA — người đang nói bằng đúng giọng mình dùng ở khoa hồi sức, không xin phép và cũng không thương hại: "
  "mắt thẳng, giọng đều, dứt khoát. ADRIAN — bị đối xử như một bệnh nhân bình thường lần đầu sau sáu tháng: "
  "mặt bình nhưng mắt động.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA nhúng chiếc khăn bông vào chậu nước",
  ["MAYA_THUONG", "ADRIAN_TUTE"], "giữa gian phòng nhà cổng, cạnh bàn gỗ vuông",
  {"MAYA": "đứng nửa phải khung, đã xắn tay áo", "ADRIAN": "ngồi xe lăn nửa trái khung, áo còn cài kín"},
  "cách nhau một bước", {"MAYA": "một tay xắn tay áo, tay kia chỉ vào lưng ghế xe lăn",
                         "ADRIAN": "hai tay trên vành tay vịn"}, bg=TRONG)
V("10", [21], "trung 50mm hạ thấp · MAYA NÉT phải xắn tay áo + ADRIAN NÉT trái ngồi xe lăn, áo còn cài kín",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt. ADRIAN VẪN MẶC NGUYÊN ÁO CÀI KÍN suốt clip, không ai cởi bỏ quần áo. "
  "Không có ai khác trong khung.",
  "MAYA xắn nốt tay áo bên kia và nói bằng đúng giọng cô dùng ở khoa hồi sức",
  [("MAYA", "firm, professional", 21)], [("ADRIAN", "silent, watching her work")])

S("11", "two-shot cận-trung 85mm, cao 1m30, cách MAYA 1m8, máy hạ thấp ngang tầm người ngồi xe lăn",
  "MAYA đứng ở nửa PHẢI khung, một tay cầm chiếc khăn bông trắng đã vắt. ADRIAN ngồi trong xe lăn ở nửa TRÁI khung, "
  "áo còn cài kín. Hậu cảnh là góc bếp nhỏ và cửa sổ có nắng chiều rất thấp.",
  "MAYA một tay cầm chiếc khăn bông, tay kia đặt lên lưng ghế xe lăn. ADRIAN một tay đặt trên vành tay vịn, "
  "tay kia buông.",
  "Hai người nhìn thẳng vào mắt nhau.",
  "ADRIAN — người đang chờ nghe một lời than phiền về căn nhà mà anh biết là tồi tàn: mắt hơi nheo, giọng thấp. "
  "MAYA — trả lời bằng thứ duy nhất cô quan tâm hôm nay: mặt bình, khoé môi động một nhịp, mắt ướt rất nhẹ.",
  "đúng khoảnh khắc ngay TRƯỚC khi vệt nắng chiều cuối cùng rời khỏi mặt sàn",
  ["MAYA_THUONG", "ADRIAN_TUTE"], "giữa gian phòng nhà cổng",
  {"MAYA": "đứng nửa phải khung cầm khăn bông", "ADRIAN": "ngồi xe lăn nửa trái khung"},
  "cách nhau một bước", {"MAYA": "một tay cầm khăn bông, tay kia trên lưng ghế xe lăn",
                         "ADRIAN": "một tay trên vành tay vịn, tay kia buông"}, bg=TRONG)
V("11", [22, 23], "two-shot cận-trung 85mm hạ thấp · MAYA NÉT phải cầm khăn + ADRIAN NÉT trái ngồi xe lăn",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN, cả hai rõ mặt, ADRIAN vẫn mặc nguyên áo cài kín. Không có ai khác trong khung.",
  "ADRIAN hỏi trước, MAYA dừng tay cầm khăn lại và trả lời",
  [("ADRIAN", "low, guarded", 22), ("MAYA", "plain, steady", 23)])

# ── NHỊP KHÉP CẢNH ──
S("B3", "toàn cảnh 24mm, cao 1m60, cách MAYA 6m, đặt ở góc phòng phía cửa ra vào nhìn chéo qua cả gian phòng",
  "Gian phòng nhỏ nhìn từ góc cửa: MAYA đứng cạnh bàn gỗ vuông giữa phòng, đang gấp lại chồng khăn bông trắng. "
  "ADRIAN ngồi trong xe lăn cạnh cửa sổ, quay mặt ra ngoài. Chiếc va li vải còn để nguyên cạnh cửa, chưa mở.",
  "MAYA hai tay gấp một chiếc khăn bông. ADRIAN hai tay đặt trên vành tay vịn.",
  "MAYA nhìn xuống chiếc khăn trong tay. ADRIAN nhìn ra ngoài cửa sổ về phía toà nhà chính trên đồi.",
  "MAYA — người vừa dọn vào một căn nhà mái vá bạt và đã bắt tay vào việc: mặt bình, vai buông tự nhiên. "
  "ADRIAN — nhìn về phía ngôi nhà đã đẩy mình ra ngoài: mặt bình, mắt tĩnh, hơi thở chậm.",
  "đúng khoảnh khắc ngay TRƯỚC khi MAYA bật ngọn đèn bàn ở tủ đầu giường",
  ["MAYA_THUONG", "ADRIAN_TUTE"], "gian phòng nhà cổng, nhìn từ góc cửa",
  {"MAYA": "đứng cạnh bàn gỗ giữa phòng gấp khăn", "ADRIAN": "ngồi xe lăn cạnh cửa sổ"},
  "cách nhau ba mét", {"MAYA": "hai tay gấp một chiếc khăn bông", "ADRIAN": "hai tay trên vành tay vịn"},
  bg=TRONG)
B("B3", "Khép cảnh. Trong gian phòng nhỏ: MAYA gấp khăn bên bàn, ADRIAN ngồi cạnh cửa sổ nhìn lên toà nhà trên đồi.",
  "toàn cảnh 24mm · MAYA NÉT đứng cạnh bàn gỗ + ADRIAN NÉT ngồi xe lăn cạnh cửa sổ · không có ai khác",
  [("MAYA", "MAYA_THUONG"), ("ADRIAN", "ADRIAN_TUTE")],
  "MAYA và ADRIAN rõ mặt trong gian phòng. Không có người nào khác trong khung.",
  "ngày đầu tiên của một cuộc hôn nhân trên giấy: hai người trong một gian phòng, không ai nói gì thêm, "
  "và cả hai đều đang làm việc của mình.",
  "MAYA gấp xong chiếc khăn và đặt lên chồng khăn, nhìn quanh gian phòng một lượt; ADRIAN vẫn nhìn ra ngoài "
  "cửa sổ; nắng chiều rút hẳn khỏi mặt sàn và căn phòng tối đi một bậc.",
  "Ambient tiếng gió ngoài cửa sổ và tiếng gỗ nhà cũ kêu khẽ, SFX tiếng vải khăn gấp lại.",
  nhac("KÌM", "Không ai trong hai người được phép để lộ ra rằng ngày hôm nay khó tới mức nào — nhạc phải kìm y như họ.",
       "Soul ballad at 62 BPM with a female alto very close to the mic, dry and almost spoken; Rhodes and upright "
       "bass only, brushed drums entering just once near the end; one held note at the midpoint then back down to "
       "voice; lyrics about folding towels in a stranger's house and calling it home for now, never self-pitying; "
       "dry intimate mix, female vocal, soul, restrained, sparse",
       "Chamber instrumental at 58 BPM; a cello holding one long low note under a felt-piano figure repeating and "
       "getting quieter each pass, a viola answering once, no percussion, no build, fading unresolved; "
       "very quiet, close-miked, cello, viola, piano, minimal"),
  dur=10)
