# -*- coding: utf-8 -*-
"""Quần chúng nền — CHỮ ĐI VÀO TỪNG SF, không bao giờ đi vào thẻ địa điểm.

Thẻ địa điểm (`refs.bg`) luôn là bối cảnh TRỐNG NGƯỜI. Mọi người nền chỉ tồn tại
dưới dạng câu chữ trong khối `AI VÀ ĐANG LÀM GÌ` của từng SF, và trong khối
`Trong khung` của từng prompt video.

Mỗi chỗ giữ vài biến thể để đám đông đổi tư thế theo shot mà không bốc hơi:
biến thể (1) cho khung rộng, (2) cho khung trung, (3) cho khung cận/OTS.
Nơi riêng tư — nhà cổng (S7 · S11 · S16 trong nhà), phòng nhân sự, phòng trọ,
hầm xe đêm, nhà thờ đã trống (S4) — KHÔNG có mục ở đây, đúng luật.
"""

# ══════════════════════════ S2 · bãi đỗ xe nhà thờ ══════════════════════════
# Lễ vừa vỡ, khách đã ra gần hết. Mọi khung cận đều 85mm xoá phông vào tường đá
# hoặc hàng xe nên nón quan sát không còn ai.
S2 = {"B1": "Ở mép xa của bãi, hai khách dự cưới đang đi về phía xe mình, một người đã mở cửa xe.",
      "01": "", "02": "", "03": "", "04": "", "05": "", "06": "",
      "B2": "Ở mép xa của bãi còn một khách dự cưới đang cúi vào cốp xe.",
      "07": "", "08": "", "09": "", "10": "", "11": "", "12": "", "B3": ""}

# ══════════════════ S3 · tiệm cầm đồ → sảnh ngân hàng, giờ hành chính ══════════════════
# Tiệm nhỏ nên đúng một khách là đủ, và ông ta đứng nguyên chỗ suốt đoạn cầm đồ.
# Ngân hàng có hàng chờ, nhưng chỉ những góc nhìn về phía dãy quầy mới thấy.
# Người khách ở tiệm cầm đồ giữ nguyên tư thế ĐỨNG, nhưng đổi việc đang làm qua
# từng khung — khoá cứng một động tác qua bốn khung liền thì thành hình nộm.
S3 = {"B1": "Ở cuối quầy kính bên trái có một khách đàn ông đứng tuổi đang cúi xem tủ đồng hồ cũ.",
      "01": "Ở cuối quầy kính phía sau, một khách đàn ông đứng tuổi đang đứng cúi xem tủ đồng hồ cũ.",
      "02": "",
      "03": "Ở cuối quầy kính phía sau, người khách đàn ông đã đứng thẳng lên, một chiếc đồng hồ đeo tay trong tay.",
      "04": "Ở cuối quầy kính phía sau, người khách đàn ông đã chuyển sang đứng xem giá tường treo nhạc cụ.",
      "05": "",
      "B2": "Phía sau là hàng chờ sáu người đứng cách đều nhau trước vạch vàng, và hai giao dịch "
            "viên ngồi sau dãy quầy kính.",
      "06": "Ngoài rìa khung phía sau là dãy quầy giao dịch có hai giao dịch viên ngồi làm việc.",
      "07": "",
      "08": "Ngoài rìa khung phía sau, một giao dịch viên ngồi đếm tiền, người kia ngồi quay sang màn hình.",
      "09": "Ở dãy quầy giao dịch đó có hai giao dịch viên ngồi làm việc và hai khách đứng chờ.",
      "10": "Ngoài rìa khung phía sau, hai giao dịch viên vẫn ngồi sau quầy, một người vừa dập một con dấu.",
      "B3": "Ở dãy quầy giao dịch bên trái còn hai khách đứng chờ tới lượt."}

# ══════════════════════ S5 · quầy viện phí lúc 5 giờ 47 sáng ══════════════════════
# Đúng luật mật độ theo giờ: sảnh gần như trống, chỉ còn một người ngủ lại qua đêm.
NGU = "Ở hàng ghế chờ phía sau có một người đàn ông ngồi gục đầu ngủ."
S5 = {"B1": "Ở hàng ghế chờ cuối phòng có một người đàn ông ngồi gục đầu ngủ, áo khoác phủ ngang ngực.",
      "01": "", "02": NGU, "03": "", "04": "", "05": "", "06": "", "07": "", "08": NGU,
      "09": "Ở hàng ghế chờ giữa sảnh có một người đàn ông ngồi gục đầu ngủ.",
      "B2": "Ở hàng ghế chờ giữa sảnh, người đàn ông vẫn ngồi gục đầu ngủ."}

# ═══════════════════ S6 · phòng hộ tịch toà thị chính, giờ hành chính ═══════════════════
# Hai cặp chờ NGỒI nguyên trên băng ghế cạnh cửa suốt scene; chỉ những góc lấy
# được cửa gỗ hai cánh mới thấy họ.
CHO6 = "Trên băng ghế chờ cạnh cửa phía sau có hai cặp ngồi đợi tới lượt."
S6 = {"B1": "Trên băng ghế chờ cạnh cửa gỗ có hai cặp ngồi đợi tới lượt, một cặp đang cúi điền giấy tờ.",
      "01": CHO6, "02": "", "03": CHO6,
      "04": "Trên băng ghế chờ cạnh cánh cửa đó có hai cặp ngồi đợi tới lượt.",
      "05": "", "06": "",
      "07": "Trên băng ghế chờ đó có hai cặp ngồi đợi tới lượt, một cặp đang cúi điền giấy tờ.",
      "08": "", "09": "",
      "10": "Trên băng ghế chờ cạnh cánh cửa đó có hai cặp ngồi đợi tới lượt.",
      "B2": "Trên băng ghế chờ cạnh cửa vẫn còn một cặp ngồi đợi tới lượt."}

# ════════════════════ S8 · phòng ăn dinh thự Kane, bữa tối gia tộc ════════════════════
# Mười mấy người nhà Kane NGỒI dọc bàn dài từ đầu tới cuối scene. Góc nào lấy
# được thân bàn thì thấy họ; góc quay vào lò sưởi hoặc cửa vòm thì không.
# Gia tộc giữ tư thế NGỒI cả bữa, nhưng mỗi khung một việc nhỏ khác nhau.
S8 = {"B1": "Dọc hai bên bàn ăn dài là mười mấy khách nhà Kane ngồi tại chỗ, dao dĩa dừng trên đĩa.",
      "01": "Dọc bàn dài phía sau, các thành viên gia tộc vẫn ngồi nguyên chỗ, mờ ngoài vùng nét.",
      "02": "Dọc bàn dài phía sau, một người đang ngồi rót nước từ bình thuỷ tinh, số còn lại ngồi yên.",
      "03": "Dọc bàn dài phía sau, hai người ngồi tựa hẳn vào lưng ghế, mờ ngoài vùng nét.",
      "04": "Dọc bàn dài phía sau, một người vừa ngồi gấp khăn ăn đặt lên mặt bàn, mờ ngoài vùng nét.",
      "05": "Dọc bàn dài phía sau, một người đang ngồi cắt thức ăn trên đĩa, số còn lại ngồi yên.",
      "06": "",
      "07": "Dọc bàn dài phía sau, một người đang ngồi nâng ly nước lên, mờ ngoài vùng nét.",
      # ── BIẾN CỐ: MAYA kéo ghế đưa ADRIAN lên đầu bàn. Cả bàn ngừng ăn.
      "08": "Dọc bàn dài phía sau, các thành viên gia tộc đã bỏ dao dĩa xuống và ngồi quay về phía đầu bàn.",
      "09": "", "10": "Dọc bàn dài phía sau, không ai còn động vào đĩa, tất cả ngồi quay về phía hai người.",
      "11": "", "12": "", "13": "",
      "14": "Dọc bàn dài phía sau, các thành viên gia tộc ngồi im, không ai còn động vào đĩa của mình.",
      "15": "Dọc bàn dài phía sau, tất cả vẫn ngồi quay về phía đầu bàn, dao dĩa để yên trên đĩa.",
      "B2": "Dọc hai bên bàn dài, các thành viên gia tộc ngồi im, không ai còn động vào đĩa của mình."}

# ═════════════════════════ S9 · ICU buồng 4, ban đêm ═════════════════════════
# Buồng bệnh là buồng riêng nên trong buồng không có ai ngoài cast. Quầy trực
# đêm ngoài hành lang chỉ lọt khung ở những góc đặt máy ngoài hành lang.
S9 = {"B1": "", "01": "", "02": "",
      "03": "Dọc hành lang phía sau có quầy trực sáng đèn với một điều dưỡng đêm ngồi ghi hồ sơ.",
      "04": "Ở cuối hành lang phía sau, quầy trực sáng đèn có một điều dưỡng đêm ngồi ghi hồ sơ.",
      "05": "Ở cuối hành lang phía sau, điều dưỡng đêm vẫn ngồi ở quầy trực, đã xoay ghế sang phía màn hình.",
      "06": "", "07": "",
      "08": "Ở cuối hành lang phía sau, điều dưỡng đêm vẫn ngồi ở quầy trực, một tay cầm ống nghe điện thoại bàn.",
      "09": "", "10": "", "11": "", "B2": ""}

# ═════════════════════ S10 · vỉa hè trước quán cà phê, ban ngày ═════════════════════
# Nơi công cộng giữa ban ngày: khách quán NGỒI nguyên bàn suốt scene, người đi
# đường thì cứ đi việc của họ. Máy hạ rất thấp thì chỉ còn thấy chân bàn ghế.
# Ba khách quán giữ tư thế NGỒI suốt scene, nhưng mỗi khung một việc nhỏ khác;
# người đi bộ thì cứ đi việc của họ, mỗi lần một người khác.
KINH10 = "Sau mặt tiền kính đó có hai khách ngồi trong quán."
S10 = {"B1": "",
       "01": "Trên vỉa hè phía sau có hai người đi bộ đang bước ngang qua.",
       "02": "Dưới mái hiên quán phía sau, ba khách vẫn ngồi ở bàn tròn, một người đang nâng cốc lên.",
       "03": "",
       "04": "Dưới mái hiên quán phía sau, ba khách vẫn ngồi ở bàn tròn, một người đang cúi nhìn điện thoại.",
       "05": KINH10,
       "06": "Dưới mái hiên quán phía sau, ba khách vẫn ngồi ở bàn tròn, hai người ngồi tựa hẳn vào lưng ghế.",
       "07": "",
       # ── BIẾN CỐ: chiếc xe lăn bị hất đổ. Từ đây quần chúng chuyển hẳn từ
       #    "sinh hoạt tự nhiên" sang "bị thu hút" — vẫn NGỒI, nhưng bỏ việc đang làm.
       "08": "Ở rìa khung phía sau, chân bàn ghế quán và chân hai khách ngồi đã xoay hẳn về phía vỉa hè.",
       "09": "Ở rìa khung phía sau, hai đôi chân khách ngồi bất động, không ai còn nhấc chân lên.",
       "10": "Dưới mái hiên quán phía sau, ba khách đã bỏ cốc xuống, ngồi nguyên trên ghế và quay hẳn sang nhìn.",
       "11": "Sau mặt tiền kính đó, hai khách ngồi trong quán đã quay hẳn ra phía vỉa hè.",
       "12": "Dưới mái hiên quán phía sau, ba khách vẫn ngồi nhưng không ai còn động vào cốc của mình.",
       "13": "Trên vỉa hè phía sau, hai người đi bộ đã dừng hẳn lại và quay sang nhìn.",
       "14": "Ở rìa khung phía sau, chân bàn ghế quán và chân hai khách ngồi bất động, một chiếc túi dựng dưới ghế.",
       "15": "Dưới mái hiên quán phía sau, ba khách ngồi bất động trên ghế, mặt quay hẳn về phía vỉa hè.",
       "16": "Ở rìa khung phía sau, chân bàn ghế quán và hai đôi chân khách ngồi đã xoay hẳn về phía này.",
       "16b": "Ở rìa khung phía sau, chân bàn ghế quán và chân hai khách ngồi bất động.",
       "17": "Trên vỉa hè phía sau, một người đi bộ đã dừng lại đứng nhìn, tay còn xách túi giấy.",
       "B2": "Dưới mái hiên quán, ba khách vẫn ngồi quay nhìn theo; trên vỉa hè hai người đi bộ đã đi tiếp."}

# ══════════════════════ S12 · phòng kính tầng 40, ban ngày ══════════════════════
# Phòng làm việc riêng nên trong phòng không thả người nền. Chỉ những góc lấy
# được vách kính HÀNH LANG mới thấy sàn làm việc chung phía ngoài.
S12 = {"B1": "", "01": "",
       "02": "Qua vách kính hành lang phía sau thấy sàn làm việc chung với ba nhân viên ngồi trước màn hình.",
       "03": "", "04": "", "05": "", "06": "",
       "07": "Qua vách kính hành lang phía sau, một nhân viên đã ngồi ngẩng lên nhìn về phía phòng kính, hai người kia vẫn trước màn hình.",
       "08": "", "09": "", "10": "", "11": "",
       "12": "Qua vách kính hành lang phía sau, ba nhân viên ở sàn làm việc đã ngồi quay hẳn về phía phòng kính.",
       "B2": "Qua vách kính hành lang phía sau, sàn làm việc chung còn hai nhân viên ngồi trước màn hình."}

# ═══════════════════ S13 · phòng chỉ huy Kane Holdings, ban đêm ═══════════════════
# Phòng họp kín ban đêm, ghế xoay dọc bàn đều trống — không gian riêng tư triệt
# tiêu nhân vật nền. Hai thành viên hội đồng là cast, không phải quần chúng.
S13 = {k: "" for k in ("B1", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                       "11", "12", "B2")}

# ════════════════════ S14 · phòng xử án hạt, phiên đang xử ════════════════════
# Đúng ví dụ trong luật: máy hướng XUỐNG khu xử thì thấy hàng ghế khán giả, máy
# hướng LÊN bục thẩm phán thì chỉ còn tường ốp gỗ và cờ. Khán giả ngồi suốt phiên.
# Khán giả NGỒI suốt phiên, chỉ đổi việc nhỏ giữa các khung.
S14 = {"B1": "Sau hàng rào gỗ thấp, các hàng ghế khán giả có chừng mười lăm người ngồi rải rác.",
       "01": "",
       "02": "Trên các hàng ghế khán giả đó có chừng mười lăm người ngồi rải rác, mặt hướng về khu xử.",
       "03": "Trên các hàng ghế khán giả đó, một người đang ngồi ghi vào cuốn sổ nhỏ trên đùi.",
       "04": "",
       "05": "Trên các hàng ghế khán giả đó, một người ngồi tựa hẳn vào lưng ghế, hai tay khoanh trước ngực.",
       "06": "Trên các hàng ghế khán giả đó, chừng mười lăm người vẫn ngồi rải rác sau hàng rào gỗ.",
       "07": "",
       "08": "Trên các hàng ghế khán giả đó, hai người ngồi cạnh nhau ở hàng đầu, một người vừa đổi tư thế ngồi.",
       "09": "",
       "10": "Trên các hàng ghế khán giả đó, một người đang ngồi đặt tập giấy xuống chỗ ghế bên cạnh.",
       "11": "",
       "12": "Trên các hàng ghế khán giả đó, chừng mười lăm người vẫn ngồi rải rác, mờ ngoài vùng nét.",
       "13": "",
       "14": "Trên các hàng ghế khán giả đó, một người ngồi ngả người sang bên để nhìn qua vai người trước.",
       # ── BIẾN CỐ: MAYA phản công rồi JULIAN bật dậy. Khán giả bỏ hết việc riêng.
       "15": "Trên các hàng ghế khán giả đó, chừng mười lăm người đã ngồi thẳng lên, không ai còn cựa quậy.",
       "16": "",
       "17": "Trên các hàng ghế khán giả đó, chừng mười lăm người ngồi im, tất cả hướng về khu xử.",
       "18": "Trên các hàng ghế khán giả đó, không ai còn cựa quậy, tất cả ngồi hướng về phía MAYA.",
       "19": "",
       "20": "Trên các hàng ghế khán giả đó chỉ còn năm sáu người ngồi lại, số kia đã đứng lên ra về.",
       "21": "",
       "B2": "Các hàng ghế khán giả đã vãn, còn vài người đang đi ra dọc lối đi giữa."}

# ═════════════════════ S15 · bãi xe toà án, chiều mưa ═════════════════════
# Mưa và mái che cắt gần hết tầm nhìn; chỉ khung rộng mới còn thấy người, và họ
# đang lo đi cho nhanh chứ không liên quan gì tới hai người dưới mái che.
S15 = {"B1": "Ngoài mái che, hai người che ô đang đi nhanh giữa các hàng xe về phía cửa toà.",
       "01": "", "02": "Xa hơn ngoài mái che, một người che ô đang đi nhanh giữa hai hàng xe.",
       "03": "", "04": "", "05": "", "06": "", "07": "",
       "08": "Xa hơn ngoài mái che, một người che ô đang mở cửa xe rồi cúi vào trong.",
       "09": "", "10": ""}

# ════════════════════ S16 · nhà cổng, buổi sáng bị trục xuất ════════════════════
# Sân nhà riêng nhưng đang có đội trục xuất làm việc: hai người khuân đồ và một
# an ninh gác cổng. Họ làm việc của họ, không đứng nhìn.
KHUAN16 = "Cạnh chiếc xe tải đó, hai người khuân đồ mặc áo bảo hộ xám đang bê thùng carton lên thùng xe."
GAC16 = "Ở cổng sắt phía sau có một nhân viên an ninh mặc đồng phục sẫm đứng gác."
S16 = {"B1": KHUAN16, "01": "", "02": "", "03": GAC16,
       "04": "Trong khung cửa nhà kho đó có một người khuân đồ đang bê thùng carton đi ra.",
       "05": "", "06": "", "07": "",
       # ── BIẾN CỐ: JULIAN thu chiếc xe lăn điện. Đội trục xuất dừng tay quay nhìn.
       "08": "Ở cổng sắt phía sau, nhân viên an ninh đã quay đầu nhìn về phía hai người.",
       "09": "",
       "10": "Cạnh chiếc xe tải đó, hai người khuân đồ đã dừng tay, quay nhìn về phía sân.",
       "11": "", "12": "", "13": "", "14": "", "14b": "", "14c": ""}

# ═══════════════ S17 · phòng cô dâu toà tháp Hale, giữa buổi thử váy ═══════════════
# Thợ làm tóc đứng ở bàn trang điểm, trợ lý cưới đứng cạnh xe đẩy champagne —
# cả hai làm việc của mình suốt scene, chỗ đứng không đổi.
# Thợ làm tóc và trợ lý cưới giữ tư thế ĐỨNG tại chỗ của mình, đổi việc từng khung.
S17 = {"B1": "Ở bàn trang điểm phía trong, một thợ làm tóc đang sắp lược và kẹp lên mặt bàn.",
       "01": "", "02": "Bên bàn trang điểm đó, một thợ làm tóc đang đứng sắp lược và kẹp lên mặt bàn.",
       "03": "Bên bàn trang điểm đó, thợ làm tóc đang đứng cắm phích một chiếc máy uốn tóc.",
       "04": "Cạnh xe đẩy phục vụ đó, một trợ lý cưới đang đứng xếp lại các ly champagne.",
       "05": "", "06": "", "07": "",
       "08": "Bên bàn trang điểm đó, một thợ làm tóc đang sắp lược, mờ ngoài vùng nét.",
       "09": "", "10": "",
       "11": "Cạnh xe đẩy phục vụ đó, trợ lý cưới đứng gấp lại một chiếc khăn ăn.",
       "12": "Bên bàn trang điểm đó, thợ làm tóc đứng lau gương bằng một chiếc khăn nhỏ.",
       "13": "",
       "B2": "Bên bàn trang điểm, thợ làm tóc đã lùi ra một bước và đứng chờ."}

# ══════ S18 · phòng nhân sự → hành lang bệnh viện → phòng trọ ══════
# Phòng nhân sự là văn phòng riêng và phòng trọ là nhà riêng — cả hai triệt tiêu
# người nền. Chỉ đoạn hành lang bệnh viện giữa ban ngày mới có người qua lại.
S18 = {"B1": "", "01": "", "02": "", "03": "", "04": "", "05": "", "06": "", "07": "",
       "08": "", "09": "",
       "B2": "Dọc hành lang phía sau có một điều dưỡng đang đẩy giường đẩy rỗng và hai người "
             "nhà bệnh nhân đi ngược lại.",
       "10": "Dọc hành lang phía sau có một điều dưỡng đang đẩy giường đẩy rỗng đi ngang.",
       "11": "Ở cuối hành lang, hai dáng người đang đi về phía cửa kính sáng, mờ.",
       "12": "Ở cuối hành lang có một dáng người đang đi xa dần, mờ.",
       "B3": "", "13": "", "14": ""}


# ════════════ S20–S23 · nhà thờ St. Michael, tiệc cưới nhà Hale, buổi chiều ════════════
# Bốn trăm khách dự tiệc ĐỨNG thành cụm cầm ly suốt bốn scene — tư thế cốt lõi
# không đổi, chỉ hướng chú ý dồn dần về chỗ đang xảy ra chuyện. Chuỗi rỗng ở đây
# nghĩa là khối AI VÀ ĐANG LÀM GÌ của khung đó ĐÃ tự khai khách rồi, hoặc máy áp
# sát xoá phông vào cột đá.
# Khách giữ tư thế ĐỨNG suốt bốn scene. S20–S21 tiệc còn đang chạy nên họ vẫn
# sinh hoạt bình thường; từ S22 (ADRIAN đứng dậy) trở đi cả phòng chết lặng nên
# trạng thái tĩnh là do kịch bản chứ không phải do khoá cứng một động tác.
T = ["Xung quanh là các cụm khách dự tiệc mặc tuxedo và váy dạ hội đứng cầm ly, mờ ngoài vùng nét.",
     "Xung quanh là các cụm khách dự tiệc đứng thành vòng, một người vừa hạ ly xuống ngang hông, mờ.",
     "Xung quanh là các cụm khách dự tiệc đứng cầm ly, hai người ở cụm xa đã quay sang hướng khác, mờ.",
     "Xung quanh là các cụm khách dự tiệc đứng cầm ly, một bồi bàn bưng khay đi len giữa các cụm, mờ.",
     "Xung quanh là các cụm khách dự tiệc đứng cầm ly, một người đang đặt ly rỗng lên khay bồi bàn, mờ.",
     "Xung quanh là các cụm khách dự tiệc đứng cầm ly, một người vừa đổi chân trụ, mờ ngoài vùng nét."]
TL = ["Xung quanh là các cụm khách dự tiệc đứng im, ly còn trong tay không ai nâng lên, mờ ngoài vùng nét.",
      "Xung quanh là các cụm khách dự tiệc đứng im nhìn về phía nền đá, mờ ngoài vùng nét.",
      "Xung quanh là các cụm khách dự tiệc đứng im, một người đã hạ ly xuống ngang hông, mờ ngoài vùng nét.",
      "Xung quanh là các cụm khách dự tiệc đứng im, không một ai nhúc nhích, mờ ngoài vùng nét.",
      "Xung quanh là các cụm khách dự tiệc đứng im, vài người đã khép vòng lại gần hơn, mờ ngoài vùng nét.",
      "Xung quanh là các cụm khách dự tiệc đứng im, một người đứng sau đã nhích sang bên để nhìn cho rõ, mờ.",
      "Xung quanh là các cụm khách dự tiệc đứng im, hai ly champagne bỏ quên trên chiếc bàn cạnh họ, mờ.",
      "Xung quanh là các cụm khách dự tiệc đứng im, không ai còn nói với ai, mờ ngoài vùng nét."]
TB = ["Quanh chiếc bàn dài phủ khăn trắng đó có ba khách dự tiệc đứng cầm ly, mờ ngoài vùng nét.",
      "Quanh chiếc bàn dài phủ khăn trắng đó, một khách đang đặt ly rỗng xuống khay, hai người kia đứng cạnh, mờ.",
      "Quanh chiếc bàn dài phủ khăn trắng đó có ba khách đứng, một người vừa cầm lên một ly mới, mờ.",
      "Quanh chiếc bàn dài phủ khăn trắng đó, ba khách đã bỏ ly xuống bàn và quay hẳn sang nhìn, mờ.",
      "Quanh chiếc bàn dài phủ khăn trắng đó, ba khách đứng im, ly còn nguyên trong tay, mờ."]
TC = ["Vòng quanh phía sau chỉ còn thấy chân và gấu váy dạ hội của các khách đứng vây quanh, mờ.",
      "Vòng quanh phía sau chỉ thấy chân người đứng vây quanh, một đôi giày vừa xê dịch nửa bước, mờ.",
      "Vòng quanh phía sau chỉ thấy chân và gấu váy dạ hội, hai người đã lùi ra nửa bước, mờ.",
      "Vòng quanh phía sau chỉ thấy chân người đứng vây quanh, không một bàn chân nào nhúc nhích, mờ."]

S20 = {"B1": "Khắp lòng nhà thờ là khách dự tiệc mặc tuxedo và váy dạ hội đứng thành từng cụm cầm ly.",
       "01": T[0], "02": TB[0], "03": T[1], "04": "", "05": "",
       "06": "Xa hơn phía sau là các cụm khách dự tiệc đứng cầm ly, một người vừa quay sang cụm bên, mờ.",
       "07": T[2], "08": "", "09": TB[1], "10": T[3], "11": "", "B2": T[4]}

# Cả S21 nằm SAU biến cố (VANESSA hô mất vòng cổ ngay câu thoại đầu), nên khách
# ở trạng thái BỊ THU HÚT từ khung đầu tiên chứ không còn sinh hoạt tự nhiên.
S21 = {"01": TL[0], "02": "", "03": TL[1], "04": TL[2], "05": TB[3], "06": TL[3], "07": TL[4],
       "08": TB[4], "09": TL[5], "10": TB[3], "11": TL[6], "12": TL[7], "12b": TL[0],
       "13": TL[2], "14": TC[0], "15": TC[1], "16": TL[4], "17": TL[6],
       "18": TC[2], "19": TC[3], "20": ""}

S22 = {"02": TC[1], "04": TC[3], "05": TL[0], "06": TC[0], "10": TL[1], "11": TL[2],
       "12": TL[3], "13": TL[0], "16": TL[1], "20": TL[2],
       **{k: "" for k in ("B1", "01", "03", "07", "08", "09", "14", "15", "17", "18", "19",
                          "21", "B2")}}

S23 = {"01": TL[4],
       "02": "Xung quanh hai người là các khách dự tiệc khác đứng im, ly còn trong tay, mờ ngoài vùng nét.",
       "03": TL[5], "04": TL[1], "05": TL[6], "06": TL[2], "08": TL[7],
       "10": TL[3], "11": TC[3], "12": TC[0], "12b": TC[1], "13": TL[4], "14": TL[5],
       "16": TL[0],
       "19": "Xung quanh là các cụm khách dự tiệc đứng im, vài người đã lùi ra mở rộng vòng, mờ.",
       "20": TL[7], "20b": "",
       **{k: "" for k in ("B1", "07", "09", "15", "17", "18", "B2")}}

# ═══════════════════ S24 · bậc thềm nhà thờ lúc chập tối ═══════════════════
# Phóng viên đứng chen dưới chân bậc và hai cảnh sát chắn ở mép lòng đường —
# họ đứng nguyên chỗ suốt scene. Góc nào quay vào cánh cửa gỗ thì không thấy họ.
# Đám phóng viên đứng chen ở chân bậc suốt scene, nhưng mỗi khung một người khác
# đang làm một việc khác — cả đám cùng giơ máy suốt bảy khung thì thành hình nộm.
S24 = {"B1": "Dưới chân bậc là một đám phóng viên đứng chen nhau giơ máy ảnh và micro; hai cảnh sát "
             "đứng chắn ở mép lòng đường.",
       "01": "Dưới chân bậc là một đám phóng viên đứng chen nhau giơ máy ảnh và micro lên.",
       "02": "Dưới chân bậc, đám phóng viên vẫn đứng chen nhau, một người đang cúi đổi ống kính.",
       "03": "Dưới chân bậc, đám phóng viên đứng chen nhau, hai người đã hạ máy ảnh xuống ngang ngực.",
       "04": "",
       "05": "Dưới chân bậc, đám phóng viên đứng chen nhau, một người đang giơ điện thoại lên quay.",
       "06": "", "07": "",
       "08": "Dưới chân bậc, đám phóng viên đứng chen nhau; hai cảnh sát vẫn đứng chắn ở mép lòng đường.",
       "08b": "Dưới chân bậc, đám phóng viên đứng chen nhau, một người đang nói vào micro cầm tay.",
       "09": "",
       "10": "Dưới chân bậc, đám phóng viên đứng chen nhau, một người vừa lùi ra sau lấy thêm khoảng cách.",
       "11": "", "12": "",
       "13": "Dưới chân bậc, đám phóng viên đứng chen nhau; một cảnh sát đã quay người về phía lòng đường.",
       "14": "",
       "15": "Dưới chân bậc, đám phóng viên đứng chen nhau, vài người đang hạ máy ảnh xuống."}

# ═════════════════════ S25 · ICU giường 12, ban ngày ═════════════════════
# Buồng riêng nên trong buồng không có ai ngoài cast. Chỉ hai khung nhìn ra cửa
# trượt mới thấy hành lang bên ngoài.
S25 = {"B1": "",
       "01": "Qua cửa trượt phía sau thấy hành lang sáng, có một điều dưỡng đang đi ngang.",
       "02": "", "03": "", "04": "",
       "05": "Qua cửa trượt mở hé phía sau thấy một mảng hành lang sáng và một người đi ngang.",
       **{k: "" for k in ("06", "07", "08", "09", "09b", "10", "11", "11b", "12", "13", "13b",
                          "14", "15", "16", "17", "17b", "18", "19", "20", "21", "22", "23",
                          "B2")}}


# ── Ghi đè lẻ cho prompt video: những khung mà khối AI VÀ ĐANG LÀM GÌ đã tự khai
#    người nền (nên qc rỗng) — clip vẫn phải khai lại, không thì Grok xoá họ đi.
S8V = {"06": "Ở một phần bàn ăn phía sau còn thấy vài khách nhà Kane ngồi tại chỗ, mờ.",
       "11": "Dọc mép bàn dài phía sau, các thành viên gia tộc vẫn ngồi nguyên chỗ, mờ."}
S23V = {"07": "Khách dự tiệc vây quanh phía sau đứng nguyên tại chỗ, mờ, không ai nhìn vào camera.",
        "17": "Khách dự tiệc vây quanh phía sau đứng nguyên tại chỗ, mờ, không ai nhìn vào camera."}

S22V = {"08": "Khách dự tiệc vây quanh phía sau đứng nguyên tại chỗ, mờ, không ai nhìn vào camera.",
        "19": "Khách dự tiệc vây quanh phía sau đứng nguyên tại chỗ, mờ, không ai nhìn vào camera.",
        "21": "Khách dự tiệc vây quanh phía sau đứng nguyên tại chỗ, mờ, không ai nhìn vào camera."}
