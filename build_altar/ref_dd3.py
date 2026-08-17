# -*- coding: utf-8 -*-
"""THẺ ĐỊA ĐIỂM — công sở, phòng chỉ huy, toà án, toà tháp Hale, phòng trọ, hầm xe."""
from lib import ref, luatchung

R = []
D = lambda rid, label, desc, prompt, vl, fp, tr, bg=None: R.append(
    ref(rid, label, desc, prompt, bg=bg, luat=luatchung(vl, fp, tr)))

VL_KINH = """VẬT LIỆU CHUNG CỦA CAO ỐC KÍNH (mọi phòng dùng chung, không đổi):
· Cao ốc văn phòng hạng A của Mỹ, mới, đắt, vô cảm: kính, thép, đá và gỗ veneer sẫm.
· Vách ngoài là KÍNH CƯỜNG LỰC suốt trần tới sàn, khung nhôm màu chì mảnh.
· Tường trong sơn TRẮNG XÁM; một mảng tường ốp GỖ VENEER ÓC CHÓ SẪM.
· Sàn trải THẢM TẤM MÀU XÁM THAN dệt mịn ở khu làm việc. Trần thả tấm phẳng có đèn LED âm trần dài.
· Kim loại đều là NHÔM XƯỚC và THÉP MỜ. Không có đồ trang trí cá nhân.
· KHÔNG có chữ hay logo đọc được ở bất kỳ đâu trong khung."""

D("REF_VANPHONG_NGAY", "Phòng tổng giám đốc, tầng 40 — BAN NGÀY",
  "THẺ BỐI CẢNH — phòng kính tầng 40 nơi Sebastian ép sa thải Ryan trong hai mươi phút. Dùng S12.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở góc phòng phía cửa, cách mép bàn làm việc 5m,\n"
  "nhìn chếch để thấy cả bàn lẫn vách kính nhìn ra thành phố.\n\n"
  "KHÔNG GIAN: phòng làm việc của tổng giám đốc trên tầng bốn mươi một cao ốc kính, BAN NGÀY, trời quang.\n"
  "Ánh sáng ban ngày trắng tràn qua vách kính chiếm trọn một mặt phòng, thấy rõ các nóc nhà và cao ốc khác phía dưới;\n"
  "đèn LED âm trần bật ở mức thấp. Toàn cảnh SÁNG, LẠNH, SẠCH. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một BÀN LÀM VIỆC LỚN mặt gỗ veneer óc chó sẫm chân thép mờ, trên có hai màn hình máy tính mỏng\n"
  "quay lưng ra cửa, một điện thoại bàn đen, một khay giấy kim loại và một ly cà phê giấy đã cạn.\n"
  "Sau bàn là GHẾ DA ĐEN lưng cao. Trước bàn là HAI GHẾ KHÁCH khung thép bọc da đen.\n"
  "Sát tường trái là một BÀN HỌP TRÒN nhỏ với bốn ghế và một tủ thấp gỗ veneer, trên nóc đặt một cây lan hồ điệp\n"
  "trắng trong chậu gốm xám.\n"
  "Bức tường trong cùng ốp gỗ veneer óc chó, treo một BỨC TRANH TRỪU TƯỢNG khổ lớn tông xám xanh không có hình\n"
  "nhận ra được. Vách ngăn với hành lang là KÍNH TRONG SUỐT từ sàn tới trần, có một CỬA KÍNH BẢN LỀ SÀN;\n"
  "qua vách kính thấy một đoạn hành lang trải thảm xám than và một ghế băng chờ.\n\n"
  "ĐÓNG BĂNG: phòng làm việc sáng và trống, đúng khoảnh khắc ngay TRƯỚC khi cửa kính mở và có người bước vào.",
  VL_KINH,
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG TỔNG GIÁM ĐỐC (đứng giữa phòng, quay mặt về bàn làm việc):
· ĐỐI DIỆN: bàn làm việc lớn mặt gỗ veneer óc chó, ghế da đen lưng cao, tường trong ốp gỗ treo tranh trừu tượng.
· BÊN PHẢI: VÁCH KÍNH suốt trần tới sàn nhìn ra thành phố từ tầng bốn mươi.
· BÊN TRÁI: bàn họp tròn nhỏ bốn ghế và tủ thấp gỗ veneer có chậu lan trắng.
· SAU LƯNG: VÁCH KÍNH TRONG SUỐT ngăn với hành lang và một CỬA KÍNH bản lề sàn; qua đó thấy hành lang trải thảm
  xám than và một ghế băng chờ.
· Phòng rộng khoảng 8m, sâu 7m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· BÀN LÀM VIỆC luôn ở phía SCREEN LEFT; CỬA KÍNH ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía người ngồi sau bàn thì hậu cảnh là tường gỗ veneer và tranh trừu tượng;
  quay về phía người đứng trước bàn thì hậu cảnh là vách kính hành lang và ghế băng chờ.
· Ánh sáng ban ngày mạnh luôn tới từ BÊN PHẢI MÀN HÌNH (phía vách kính ngoài trời), đổ bóng dài về bên trái.""")

D("REF_CHIHUY_DEM", "Phòng chỉ huy Kane Holdings — ĐÊM",
  "THẺ BỐI CẢNH — phòng điều hành mười tám màn hình, nơi Adrian ra lệnh và tập đứng dậy. Dùng S13.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở đầu phòng phía cửa, cách đầu bàn họp 6m,\n"
  "nhìn dọc bàn về phía bức tường màn hình.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY VẬT LIỆU của cao ốc kính — kính khung nhôm chì,\n"
  "gỗ veneer óc chó sẫm, thảm xám than, thép mờ. **ĐÂY LÀ MỘT CĂN PHÒNG KHÁC (PHÒNG ĐIỀU HÀNH)** — KHÔNG copy\n"
  "bàn làm việc, tranh hay bàn họp tròn của ảnh gốc.\n\n"
  "KHÔNG GIAN: phòng điều hành không cửa sổ ra ngoài trừ một vách kính ở đầu phòng, BAN ĐÊM. Nguồn sáng chính là\n"
  "BỨC TƯỜNG MÀN HÌNH đang phát, hắt ánh XANH LẠNH lên mặt bàn và trần; thêm hai dải đèn LED âm trần bật ở mức thấp\n"
  "cho ánh trắng ấm hơn. Đủ SÁNG RÕ mặt người, KHÔNG mảng đen đặc. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: cuối phòng là MỘT BỨC TƯỜNG GỒM MƯỜI TÁM MÀN HÌNH xếp thành ba hàng sáu cột, viền đen mảnh sát nhau;\n"
  "các màn hình đang hiển thị đồ thị đường, bản đồ thế giới và các ô hình chữ nhật màu — thấy rõ là dữ liệu\n"
  "nhưng KHÔNG đọc được chữ hay số nào.\n"
  "Giữa phòng là một BÀN HỌP DÀI mặt gỗ veneer óc chó sẫm bo tròn hai đầu, quanh bàn có MƯỜI GHẾ XOAY DA ĐEN\n"
  "lưng cao; trên bàn đặt các micro cần nhỏ, ba máy tính bảng úp màn hình và hai bình nước thuỷ tinh với ly.\n"
  "Ở đầu bàn phía màn hình có một KHOẢNG TRỐNG không kê ghế (chỗ cho xe lăn) và một BỤC PHÁT BIỂU thấp bằng thép mờ\n"
  "có TAY VỊN NGANG bằng thép — chi tiết tay vịn này BẮT BUỘC phải thấy rõ.\n"
  "Tường hai bên ốp gỗ veneer óc chó tối màu, có nẹp LED chạy dọc chân tường. Sàn trải thảm tấm xám than.\n\n"
  "ĐÓNG BĂNG: phòng chỉ huy sáng màn hình và trống, đúng khoảnh khắc ngay TRƯỚC khi cửa mở và người vào họp.",
  VL_KINH,
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG CHỈ HUY (đứng ở đầu bàn phía cửa, quay mặt về tường màn hình):
· ĐỐI DIỆN (cuối phòng): BỨC TƯỜNG MƯỜI TÁM MÀN HÌNH ba hàng sáu cột đang phát; trước nó là khoảng trống không
  kê ghế và một BỤC THÉP MỜ THẤP CÓ TAY VỊN NGANG.
· BÊN PHẢI: tường ốp gỗ veneer óc chó tối màu có nẹp LED chân tường; một tủ thấp đặt máy in và hai điện thoại hội nghị.
· BÊN TRÁI: VÁCH KÍNH mờ ngăn với hành lang, phía sau kính chỉ thấy bóng người mờ khi có ai đi qua.
· SAU LƯNG: CỬA GỖ VENEER hai cánh dẫn ra hành lang tầng điều hành.
· GIỮA PHÒNG: bàn họp dài mặt gỗ veneer với mười ghế xoay da đen.
· Phòng dài khoảng 12m, ngang 7m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· BỨC TƯỜNG MÀN HÌNH luôn ở phía SCREEN LEFT; CỬA ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía đầu bàn có bục thép thì hậu cảnh là tường mười tám màn hình sáng xanh;
  quay về phía cửa thì hậu cảnh là bàn họp, ghế xoay da đen và cửa gỗ veneer.
· Ánh xanh lạnh của màn hình luôn tới từ BÊN TRÁI MÀN HÌNH; đèn LED trần đổ đều từ trên xuống.""",
  bg="REF_VANPHONG_NGAY")

D("REF_TOAAN_NGAY", "Phòng xử án hạt — BAN NGÀY",
  "THẺ BỐI CẢNH — phiên toà giám hộ, nơi Maya đọc bệnh án và Julian thua đơn. Dùng S14.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở cuối phòng phía cửa, cách bục thẩm phán 12m,\n"
  "nhìn thẳng về bục.\n\n"
  "KHÔNG GIAN: phòng xử án của một toà án hạt Mỹ xây thập niên 1920, BAN NGÀY. Bốn cửa sổ vòm cao bên trái cho\n"
  "nắng ban ngày vào thành các cột sáng nghiêng thấy rõ bụi; đèn quả cầu thuỷ tinh trên trần bật.\n"
  "Toàn cảnh SÁNG, TRANG NGHIÊM, ấm màu gỗ. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: cuối phòng là BỤC THẨM PHÁN bằng gỗ sồi sẫm cao, mặt bàn rộng, phía trên có một chiếc ghế da lưng\n"
  "cao; trên bục có một BÚA GỖ đặt trên đế tròn, một micro cần cong và một chồng hồ sơ.\n"
  "Sau bục là mảng tường ốp gỗ và HAI LÁ CỜ ĐỨNG hai bên — CẢ HAI LÁ CỜ ĐỀU TRƠN MỘT MÀU (một xanh navy, một đỏ sẫm),\n"
  "KHÔNG có hoa văn, ngôi sao hay chữ.\n"
  "Bên trái bục là BỤC NHÂN CHỨNG nhỏ có ghế gỗ và micro; bên phải là BÀN THƯ KÝ TOÀ thấp có máy tốc ký.\n"
  "Giữa phòng có HAI BÀN LUẬT SƯ bằng gỗ sồi đặt song song cách nhau ba mét, mỗi bàn có ba ghế gỗ, trên bàn là\n"
  "các tập hồ sơ, ly nước thuỷ tinh và bình nước inox. Trước hai bàn có một KHOẢNG TRỐNG rộng.\n"
  "Ngăn cách khu xử với khu khán giả là một HÀNG RÀO GỖ THẤP có cửa lật. Khu khán giả là sáu HÀNG GHẾ BĂNG GỖ\n"
  "giống ghế nhà thờ. Sàn lát ĐÁ HOA VUÔNG be nâu, lối đi giữa trải một dải thảm xanh rêu đã mòn.\n\n"
  "ĐÓNG BĂNG: phòng xử sáng nắng và trống, đúng khoảnh khắc ngay TRƯỚC khi thư ký mở cửa cho mọi người vào.",
  """VẬT LIỆU CHUNG (toà án hạt):
· Công thự Mỹ thập niên 1920: trần cao 5m, bề thế, tất cả bằng GỖ SỒI SẪM đánh vec-ni đã lên nước bóng.
· Tường ốp gỗ sồi nửa dưới cao ngang ngực, nửa trên sơn màu KEM NGẢ VÀNG.
· Sàn ĐÁ HOA VUÔNG màu be nâu đã mòn; lối đi giữa trải thảm chạy màu xanh rêu đã bạc.
· Đèn là quả cầu thuỷ tinh trắng đục treo dây đồng. Kim loại là ĐỒNG THAU XỈN.
· MỌI LÁ CỜ trong khung đều TRƠN MỘT MÀU, KHÔNG hoa văn, KHÔNG ngôi sao. KHÔNG có chữ đọc được ở bất kỳ đâu.""",
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG XỬ ÁN (đứng giữa khu xử, quay mặt về bục thẩm phán):
· ĐỐI DIỆN: BỤC THẨM PHÁN gỗ sồi cao có búa gỗ và micro; sau bục là tường ốp gỗ và hai lá cờ trơn hai bên.
· BÊN TRÁI: bục nhân chứng nhỏ có ghế gỗ và micro; xa hơn là bốn CỬA SỔ VÒM CAO khung gỗ.
· BÊN PHẢI: bàn thư ký toà thấp có máy tốc ký; sát tường là dãy ghế bồi thẩm gỗ mười hai chỗ, hiện để trống.
· SAU LƯNG: hàng rào gỗ thấp có cửa lật, sau đó là sáu hàng ghế băng gỗ khu khán giả, cuối cùng là CỬA GỖ HAI CÁNH
  có ô kính mờ dẫn ra hành lang.
· GIỮA KHU XỬ: hai bàn luật sư gỗ sồi đặt song song cách nhau ba mét.
· Phòng dài khoảng 20m, ngang 12m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· BỤC THẨM PHÁN luôn ở phía SCREEN LEFT; CỬA ra hành lang và khu khán giả luôn ở phía SCREEN RIGHT.
· BÀN CỦA BÊN NGUYÊN (phía Julian) luôn là bàn gần SCREEN LEFT; BÀN CỦA BÊN KIA (phía Adrian và Maya) luôn ở
  gần SCREEN RIGHT. Không bao giờ đổi chỗ hai bàn.
· Nền theo nhân vật: quay về phía thẩm phán thì hậu cảnh là bục gỗ cao và hai lá cờ; quay về phía hai bàn luật sư
  thì hậu cảnh là hàng rào gỗ thấp và các hàng ghế khán giả.
· Nắng luôn tới từ BÊN TRÁI MÀN HÌNH qua bốn cửa sổ vòm, thành cột sáng nghiêng.""")

D("REF_BAIXETOA_CHIEU", "Bãi xe ngầm toà án — CHIỀU MƯA",
  "THẺ BỐI CẢNH — bãi đỗ xe lộ thiên cạnh toà án dưới mưa, ngay sau phiên xử. Dùng S15.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt dưới mái che lối ra, cách hàng xe gần nhất 7m,\n"
  "nhìn chếch qua bãi.\n\n"
  "KHÔNG GIAN: bãi đỗ xe lộ thiên cạnh toà án, BUỔI CHIỀU, TRỜI MƯA VỪA. Trời xám chì, mưa rơi thành các sợi\n"
  "nhìn rõ, mặt nhựa ướt bóng phản chiếu đèn và bóng xe; đèn cao áp trên cột đã bật sớm cho ánh trắng lạnh.\n"
  "Toàn cảnh vẫn SÁNG RÕ, KHÔNG tối đen.\n"
  "Khung hình TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: mặt sân NHỰA ĐEN ƯỚT có các vũng nước nông phản chiếu; vạch kẻ ô đỗ màu vàng đã mờ.\n"
  "Đỗ khoảng mười lăm xe con ướt nước, trong đó có ba xe đen bóng đỗ gần lối ra (biển số LÀM MỜ).\n"
  "Bên trái là MỘT MÁI CHE BẰNG TÔN nối từ cửa hông toà án ra tới mép bãi, cột thép sơn xanh rêu, mép mái\n"
  "đang nhỏ nước thành hàng giọt. Dưới mái che có một DỐC BÊ TÔNG thoải nối bậc cửa xuống mặt bãi và một\n"
  "TAY VỊN INOX chạy dọc dốc.\n"
  "Cuối bãi là hàng rào lưới thép cao và một hàng cây trụi lá ướt; xa hơn là mặt sau toà án bằng đá xám\n"
  "với các cửa sổ vòm sáng đèn.\n"
  "Cạnh dốc có một THÙNG RÁC KIM LOẠI có nắp và một biển báo đỗ xe hình chữ nhật màu trắng — CHỈ CÓ HÌNH MŨI TÊN,\n"
  "KHÔNG có chữ.\n\n"
  "ĐÓNG BĂNG: bãi xe mưa và vắng, đúng khoảnh khắc ngay TRƯỚC khi cửa hông toà án mở và người bước ra dưới mái che.",
  """VẬT LIỆU CHUNG (khu ngoài trời của toà án):
· Mặt sau toà án bằng ĐÁ XÁM khối lớn, cửa sổ vòm khung gỗ sẫm.
· Mặt bãi NHỰA ĐEN, khi mưa thì ƯỚT BÓNG và có vũng nước nông; vạch kẻ ô màu VÀNG đã mờ.
· Mái che bằng TÔN SÓNG màu ghi trên cột THÉP SƠN XANH RÊU đã tróc; tay vịn và gờ dốc bằng INOX XƯỚC.
· Hàng rào LƯỚI THÉP mạ kẽm. BIỂN SỐ mọi xe LÀM MỜ, KHÔNG có chữ đọc được ở bất kỳ đâu.""",
  """QUY HOẠCH KHÔNG GIAN 360° — BÃI XE TOÀ ÁN (đứng dưới mái che, quay mặt ra bãi):
· SAU LƯNG: cửa hông toà án bằng gỗ sẫm có bậc đá, dốc bê tông thoải và tay vịn inox chạy dọc dốc.
· ĐỐI DIỆN: ba hàng ô đỗ xe ướt nước, xa nhất là hàng rào lưới thép và hàng cây trụi lá.
· BÊN TRÁI: dãy cột thép xanh rêu đỡ mái tôn, mép mái nhỏ nước thành hàng giọt; một thùng rác kim loại có nắp.
· BÊN PHẢI: lối xe chạy ra đường công cộng, có một thanh chắn barie sơn sọc và một cabin bảo vệ nhỏ.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· CỬA HÔNG TOÀ ÁN và mái che luôn ở phía SCREEN LEFT; LỐI RA ĐƯỜNG luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía toà án thì hậu cảnh là mặt đá xám, cửa sổ vòm sáng đèn và cột mái che;
  quay về phía bãi thì hậu cảnh là hàng xe ướt, hàng rào lưới thép và cây trụi lá.
· Đèn cao áp trắng lạnh luôn tới từ TRÊN CAO BÊN PHẢI MÀN HÌNH; mưa rơi thẳng, hơi xiên về bên trái.""")

D("REF_SUITE_NGAY", "Phòng cô dâu, toà tháp Hale — BAN NGÀY",
  "THẺ BỐI CẢNH — phòng chờ cô dâu xa hoa nơi Vanessa thuê Maya làm điều dưỡng riêng ba nghìn đô một ngày. Dùng S17.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở phía cửa đôi, cách bàn trang điểm 6m, nhìn chéo\n"
  "qua phòng về phía vách kính.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY VẬT LIỆU của cao ốc kính — vách kính khung nhôm chì,\n"
  "độ mới và mức sang trọng. **ĐÂY LÀ MỘT CĂN PHÒNG KHÁC (PHÒNG CHỜ CÔ DÂU)** — KHÔNG copy bàn làm việc, ghế da\n"
  "hay tranh trừu tượng của ảnh gốc.\n\n"
  "KHÔNG GIAN: phòng chờ cô dâu trên tầng cao một toà tháp, BAN NGÀY, trời quang. Ánh sáng ban ngày trắng tràn\n"
  "qua vách kính suốt một mặt phòng, thấy nền trời và các nóc nhà phía dưới; thêm một dãy bóng đèn tròn viền quanh\n"
  "gương trang điểm đang bật. Toàn cảnh SÁNG, TRẮNG, ĐẮT TIỀN. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: sát tường phải là một BÀN TRANG ĐIỂM dài mặt đá trắng với GƯƠNG LỚN viền bóng đèn tròn;\n"
  "trên mặt bàn bày các hộp mỹ phẩm, ba lọ nước hoa thuỷ tinh, một khay bạc và một hộp nhung nhỏ ĐANG ĐÓNG NẮP.\n"
  "Trước bàn là một GHẾ ĐÔN bọc nhung màu ngà.\n"
  "Giữa phòng là một BỘ SOFA NHUNG MÀU NGÀ hình chữ L với bàn trà mặt đá tròn, trên bàn có một bình hoa mẫu đơn\n"
  "trắng lớn, hai ly champagne rỗng và một khay bánh nhỏ.\n"
  "Sát tường trong có một GIÁ TREO VÁY bằng đồng, trên đó treo MỘT CHIẾC TÚI VẢI TRẮNG DÀI đựng váy cưới,\n"
  "khoá kéo đóng kín — KHÔNG nhìn thấy chiếc váy bên trong.\n"
  "Sàn trải THẢM LÔNG NGẮN MÀU KEM dày. Trần có một đèn chùm pha lê nhỏ. Cạnh cửa đôi có một xe đẩy phục vụ\n"
  "bằng đồng với xô đá và chai champagne (nhãn chai LÀM MỜ, không đọc được chữ).\n\n"
  "ĐÓNG BĂNG: phòng cô dâu sáng và trống, đúng khoảnh khắc ngay TRƯỚC khi cửa đôi mở và có người được dẫn vào.",
  VL_KINH + """
· RIÊNG KHU NHÀ HALE: bảng màu TRẮNG NGÀ · KEM · ĐỒNG MẠ VÀNG; vải là NHUNG và LỤA; hoa tươi màu trắng.""",
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG CÔ DÂU (đứng giữa phòng, quay mặt về bàn trang điểm):
· ĐỐI DIỆN: bàn trang điểm dài mặt đá trắng với gương lớn viền bóng đèn tròn và ghế đôn nhung ngà.
· BÊN TRÁI: VÁCH KÍNH suốt trần tới sàn nhìn ra bầu trời và các nóc nhà; trước vách kính có một chậu cây lá cọ lớn.
· BÊN PHẢI: giá treo váy bằng đồng với túi vải trắng dài đựng váy cưới, và một cửa gỗ trắng dẫn vào phòng thay đồ.
· SAU LƯNG: CỬA ĐÔI GỖ SƠN TRẮNG có tay nắm đồng mạ vàng dẫn ra hành lang; cạnh cửa là xe đẩy phục vụ bằng đồng.
· GIỮA PHÒNG: bộ sofa nhung ngà hình chữ L và bàn trà mặt đá tròn trên thảm lông kem.
· Phòng rộng khoảng 9m, sâu 8m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· BÀN TRANG ĐIỂM và gương luôn ở phía SCREEN LEFT; CỬA ĐÔI ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía chủ nhà thì hậu cảnh là gương viền bóng đèn và bàn trang điểm; quay về phía
  người khách đứng gần cửa thì hậu cảnh là cửa đôi trắng, xe đẩy đồng và giá treo váy.
· Ánh sáng ban ngày mạnh luôn tới từ BÊN TRÁI MÀN HÌNH (phía vách kính), đổ bóng mềm về bên phải.""",
  bg="REF_VANPHONG_NGAY")

D("REF_PHONGTRO_DEM", "Phòng trọ phố Ridge — ĐÊM",
  "THẺ BỐI CẢNH — căn phòng bốn mươi mốt đô một tuần, giường kê dưới cửa sổ. Dùng S18.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở góc phòng phía cửa, cách giường 4m, nhìn chéo\n"
  "qua cả phòng.\n\n"
  "KHÔNG GIAN: một căn phòng trọ đơn ở tầng hai một khu nhà cũ, BAN ĐÊM. Ngoài cửa sổ là đêm và một mảng tường\n"
  "gạch của toà nhà đối diện, có ánh ĐÈN ĐƯỜNG MÀU CAM hắt vào thành một vệt nghiêng trên tường trong phòng.\n"
  "Trong phòng bật một ĐÈN BÀN chao vải kem và một bóng đèn trần đơn có chụp thiếc — ánh VÀNG ẤM, hơi yếu,\n"
  "vẫn ĐỦ SÁNG RÕ mặt người, KHÔNG mảng đen đặc. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: phòng hẹp, tường sơn màu BE NGẢ VÀNG đã ố, một vệt nứt chân chim chạy dọc góc tường.\n"
  "Sàn LINOLEUM màu nâu vân gỗ đã bong mép ở góc, trải một tấm thảm chùi chân nhỏ.\n"
  "KÊ SÁT DƯỚI CỬA SỔ là một GIƯỜNG ĐƠN khung sắt sơn trắng, ga trải xám phẳng, hai gối — chi tiết giường kê\n"
  "dưới cửa sổ BẮT BUỘC phải thấy rõ.\n"
  "Cạnh giường là một TỦ ĐẦU GIƯỜNG GỖ nhỏ có đèn bàn, một cốc nước và một vỉ thuốc.\n"
  "Sát tường phải là một BẾP ĐIỆN ĐÔI đặt trên tủ gỗ thấp, một BỒN RỬA INOX nhỏ có vòi, một tủ lạnh mini màu kem,\n"
  "và một giá gỗ hai tầng úp vài cái bát đĩa.\n"
  "Giữa phòng là một BÀN GỖ TRÒN nhỏ với hai ghế gỗ không cùng bộ. Góc phòng có bốn THÙNG CARTON chưa mở nắp\n"
  "xếp chồng và hai túi vải to. Trên tường treo một tấm gương chữ nhật nhỏ và một chiếc đồng hồ tròn vỏ nhựa trắng\n"
  "(mặt đồng hồ KHÔNG có chữ số đọc được).\n\n"
  "ĐÓNG BĂNG: căn phòng trọ sáng đèn vàng và trống, đúng khoảnh khắc ngay TRƯỚC khi có người mở cửa bước vào.",
  """VẬT LIỆU CHUNG (phòng trọ phố Ridge):
· Phòng thuê rẻ tiền trong khu nhà cũ: chật, cũ, nhưng SẠCH SẼ và NGĂN NẮP — đây là chỗ ở của một điều dưỡng
  chăm chút, KHÔNG phải nhà bừa bộn.
· Tường sơn BE NGẢ VÀNG đã ố, có vết nứt chân chim. Trần thấp 2m5, sơn trắng đã xám.
· Sàn LINOLEUM màu nâu vân gỗ bong mép. Cửa và khung cửa sổ bằng gỗ sơn trắng đã tróc.
· Đồ đạc là đồ cũ không cùng bộ: khung sắt sơn trắng, gỗ mộc, nhựa và inox rẻ tiền.
· KHÔNG có đồ điện tử đắt tiền, KHÔNG có tranh ảnh, KHÔNG có chữ đọc được.""",
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG TRỌ (đứng giữa phòng, quay lưng về cửa ra vào):
· ĐỐI DIỆN: CỬA SỔ CHỮ NHẬT khung gỗ trắng nhìn ra đêm và tường gạch toà nhà đối diện; ngay DƯỚI CỬA SỔ kê
  giường đơn khung sắt trắng, cạnh giường là tủ đầu giường gỗ có đèn bàn.
· BÊN PHẢI: góc bếp với bếp điện đôi trên tủ gỗ thấp, bồn rửa inox, tủ lạnh mini và giá úp bát đĩa.
· BÊN TRÁI: bốn thùng carton chưa mở xếp chồng, hai túi vải to, và một tấm gương chữ nhật nhỏ treo tường.
· SAU LƯNG: CỬA GỖ sơn trắng đã tróc có hai ổ khoá và một xích chặn cửa; cạnh cửa là mắc áo gỗ.
· GIỮA PHÒNG: bàn gỗ tròn nhỏ với hai ghế gỗ không cùng bộ.
· Phòng rộng khoảng 4m, sâu 5m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· GIƯỜNG và CỬA SỔ luôn ở phía SCREEN LEFT; CỬA RA VÀO luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía giường thì hậu cảnh là cửa sổ đêm và khung giường sắt trắng; quay về phía cửa
  thì hậu cảnh là cánh cửa gỗ trắng tróc sơn và chồng thùng carton.
· Ánh đèn bàn vàng ấm luôn tới từ BÊN TRÁI MÀN HÌNH; vệt đèn đường cam hắt vào cũng từ phía đó.""")

D("REF_HAMXE_DEM", "Hầm đỗ xe tầng B2 — ĐÊM",
  "THẺ BỐI CẢNH — hầm xe nơi ba người của Julian chặn Maya và Adrian, và bàn tay Maya bị đánh gãy. Dùng S19.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt giữa lối xe chạy, cách hàng cột gần nhất 10m,\n"
  "nhìn dọc theo hầm.\n\n"
  "KHÔNG GIAN: tầng hầm B2 của một bãi đỗ xe công cộng, BAN ĐÊM. Không có ánh sáng tự nhiên; đèn tuýp gắn trần\n"
  "bật cách quãng, một bóng NHẤP NHÁY, cho ánh trắng lạnh loang lổ — có vùng sáng rõ và vùng tối mờ,\n"
  "nhưng KHÔNG có mảng đen đặc, mọi gương mặt bước vào khung đều phải NHÌN RÕ. Hầm TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: sàn BÊ TÔNG MÀI XÁM có vạch kẻ ô đỗ màu vàng đã mờ và các vệt dầu loang sẫm.\n"
  "Hai hàng CỘT BÊ TÔNG VUÔNG lớn sơn xám, chân cột sơn một vành VÀNG ĐEN sọc chéo, đứng cách nhau chừng sáu mét,\n"
  "trên mỗi cột có một con số sơn stencil ĐÃ MỜ KHÔNG ĐỌC ĐƯỢC.\n"
  "Đỗ rải rác bảy tám xe con phủ bụi (biển số LÀM MỜ). Trần bê tông thấp có các ống thông gió tròn bằng tôn\n"
  "và ống nước chạy nổi, một vài chỗ rỉ nước để lại vệt ố dài trên cột.\n"
  "Bên trái, ở giữa hai cột, có một CỬA THANG MÁY hai cánh bằng inox xước với một bảng nút bấm nhỏ cạnh cửa —\n"
  "trên cửa thang máy DÁN MỘT TỜ GIẤY A4 trắng, chỉ thấy là có tờ giấy, KHÔNG đọc được chữ.\n"
  "Cạnh thang máy là CỬA THOÁT HIỂM bằng thép sơn xám có thanh đẩy ngang.\n"
  "Trên sàn giữa lối xe có một MIỆNG CỐNG THOÁT NƯỚC hình vuông bằng gang — chi tiết này BẮT BUỘC phải thấy rõ.\n"
  "Cuối hầm là DỐC XE dẫn lên tầng trên, có mũi tên sơn trắng trên sàn.\n\n"
  "ĐÓNG BĂNG: hầm xe vắng dưới ánh đèn tuýp loang lổ, đúng khoảnh khắc ngay TRƯỚC khi có người rẽ vào từ phía dốc.",
  """VẬT LIỆU CHUNG (hầm đỗ xe):
· Bãi đỗ xe ngầm công cộng, cũ và bẩn công nghiệp: BÊ TÔNG TRẦN ở mọi bề mặt, không hoàn thiện.
· Sàn BÊ TÔNG MÀI XÁM có vết dầu loang; vạch kẻ ô đỗ màu VÀNG đã mờ; chân cột sơn vành VÀNG ĐEN sọc chéo.
· Trần bê tông thấp 2m6 có ống thông gió TÔN TRÒN và ống nước chạy nổi, vài chỗ rỉ nước để lại vệt ố.
· Đèn là bóng TUÝP TRẦN gắn cách quãng, ánh trắng lạnh, có một bóng nhấp nháy.
· BIỂN SỐ mọi xe LÀM MỜ; các con số sơn trên cột đều MỜ KHÔNG ĐỌC ĐƯỢC; KHÔNG có chữ nào đọc được.""",
  """QUY HOẠCH KHÔNG GIAN 360° — HẦM B2 (đứng giữa lối xe chạy, quay mặt về phía dốc lên):
· ĐỐI DIỆN (cuối hầm): DỐC XE dẫn lên tầng trên, trên sàn có mũi tên sơn trắng chỉ hướng.
· BÊN TRÁI: hàng cột bê tông vuông, giữa hai cột là CỬA THANG MÁY inox xước có bảng nút bấm và một tờ giấy A4
  dán trên cánh cửa; kế đó là CỬA THOÁT HIỂM thép xám có thanh đẩy ngang.
· BÊN PHẢI: hàng cột thứ hai và các ô đỗ xe với bảy tám xe con phủ bụi.
· SAU LƯNG: lối xe chạy tiếp về phía cuối hầm tối hơn, có một vũng nước đọng dưới chỗ ống nước rỉ.
· GIỮA LỐI XE: MIỆNG CỐNG THOÁT NƯỚC vuông bằng gang trên sàn bê tông.
· Hầm rộng khoảng 16m, sâu 30m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· CỬA THANG MÁY và cửa thoát hiểm luôn ở phía SCREEN LEFT; DỐC XE lên tầng trên luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía thang máy thì hậu cảnh là cửa inox xước và cột bê tông có vành sọc vàng đen;
  quay về phía dốc thì hậu cảnh là hàng xe đỗ phủ bụi và miệng dốc sáng hơn.
· Đèn tuýp trần luôn đổ thẳng từ trên xuống thành các quầng sáng cách quãng dọc theo hầm.""")
