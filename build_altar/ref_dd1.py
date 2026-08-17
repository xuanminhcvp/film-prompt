# -*- coding: utf-8 -*-
"""THẺ ĐỊA ĐIỂM — cụm NHÀ THỜ và cụm BỆNH VIỆN."""
from lib import ref, luatchung

R = []
D = lambda rid, label, desc, prompt, vl, fp, tr, bg=None: R.append(
    ref(rid, label, desc, prompt, bg=bg, luat=luatchung(vl, fp, tr)))

# ══════════════════════════ NHÀ THỜ ══════════════════════════
VL_NHATHO = """VẬT LIỆU CHUNG CỦA CẢ TOÀ NHÀ THỜ (mọi khung dùng chung, không đổi):
· Nhà thờ Công giáo Mỹ xây bằng ĐÁ SA THẠCH MÀU MẬT ONG, kiểu tân Gothic, khoảng một trăm hai mươi năm tuổi.
· Trong lòng nhà thờ: tường đá để trần mạch vữa rõ, hàng CỘT ĐÁ TRÒN chia hai bên, vòm trần nhọn cao mười hai mét
  có xương gân đá.
· Sàn lát ĐÁ PHIẾN XÁM lớn đã mòn bóng ở lối đi giữa. Ghế băng dài bằng GỖ SỒI SẪM đánh vec-ni.
· Hai bên tường cao là dãy CỬA SỔ KÍNH MÀU hình vòm nhọn, hoạ tiết hình học nhiều màu, KHÔNG có chữ.
· Kim loại trang trí là ĐỒNG THAU đã xỉn. Mọi thứ CŨ, SẠCH, ĐƯỢC LAU CHÙI KỸ — không bụi, không mạng nhện."""

FP_NHATHO = """QUY HOẠCH KHÔNG GIAN 360° — LÒNG NHÀ THỜ (đứng ở giữa lối đi chính, quay mặt về BÀN THỜ):
· ĐỐI DIỆN (cuối nhà thờ, phía trước): BỆ BÀN THỜ đá trắng ba bậc, phía sau là bức tường hậu có cửa sổ kính màu
  hình hoa hồng tròn lớn; bên trái bàn thờ là BỤC GIẢNG gỗ chạm, bên phải là một cây ĐÀN ORGAN nhỏ.
· BÊN TRÁI và BÊN PHẢI: hai dãy GHẾ BĂNG GỖ SỒI, mỗi bên mười hai hàng, cách nhau bởi LỐI ĐI CHÍNH rộng hai mét
  trải THẢM ĐỎ SẪM chạy suốt từ cửa lớn tới bậc bàn thờ; sát tường hai bên là hàng cột đá và các cửa sổ kính màu.
· SAU LƯNG (cuối phòng): CỬA GỖ HAI CÁNH LỚN dẫn ra tiền sảnh và bậc thềm ngoài trời; hai bên cửa là hai
  hàng ghế cuối cùng và một BÀN GỖ NHỎ đặt sách hát; góc phải cuối phòng có một CỬA HẸP dẫn ra hành lang phục vụ.
· Lòng nhà thờ dài khoảng 30m, ngang 14m."""

TR_NHATHO = """TRỤC (screen mapping — không bao giờ đảo):
· BÀN THỜ luôn ở phía SCREEN LEFT khi máy đặt ngang lối đi; CỬA LỚN ra ngoài luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía bàn thờ thì hậu cảnh là bệ đá trắng và cửa sổ kính hoa hồng; quay về phía cửa
  lớn thì hậu cảnh là hai cánh cửa gỗ và các hàng ghế cuối.
· Nguồn sáng cửa sổ kính màu luôn hắt từ BÊN TRÁI MÀN HÌNH sang, đổ bóng nghiêng về bên phải."""

D("REF_NHATHO_SANG", "Nhà thờ St. Michael — SÁNG, đám cưới của Maya",
  "THẺ BỐI CẢNH GỐC CỦA CẢ CỤM NHÀ THỜ. Buổi sáng đám cưới Maya bị bỏ rơi. Hai trăm khách, hoa trắng rẻ tiền.\n"
  "Dùng S1.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở cuối lối đi chính phía cửa lớn, cách bậc bàn thờ 22m,\n"
  "nhìn thẳng dọc lối đi về phía bàn thờ.\n\n"
  "KHÔNG GIAN: lòng nhà thờ tân Gothic bằng đá sa thạch màu mật ong, BAN NGÀY. Nắng sáng chếch qua dãy cửa sổ kính\n"
  "màu bên trái, đổ những vệt sáng màu lên thảm đỏ và lưng ghế; trong không khí thấy rõ bụi bay. Đèn chùm đồng thau\n"
  "trên cao bật ở mức thấp. Toàn cảnh SÁNG, ẤM, rõ từng chi tiết. Phòng TRỐNG NGƯỜI.\n\n"
  "TRANG TRÍ ĐÁM CƯỚI (rẻ tiền và ít, đây là đám cưới của một điều dưỡng): đầu mỗi hàng ghế buộc một BÓ HOA CÚC\n"
  "TRẮNG NHỎ bằng ruy băng trắng, vài bó đã hơi rũ. Hai bên bậc bàn thờ đặt hai BÌNH HOA LY TRẮNG cỡ vừa.\n"
  "Trên bàn gỗ nhỏ cuối phòng xếp một chồng SÁCH THÁNH CA bìa nâu sờn. Trên bệ bàn thờ có hai cây nến trắng cao\n"
  "đang cháy và một cuốn sách lễ mở sẵn.\n\n"
  "ĐÓNG BĂNG: lòng nhà thờ đã trang trí xong và còn trống, đúng khoảnh khắc ngay TRƯỚC khi khách bắt đầu vào chỗ.",
  VL_NHATHO, FP_NHATHO, TR_NHATHO)

D("REF_NHATHO_CHIEU", "Nhà thờ St. Michael — CHIỀU MUỘN, trống không",
  "THẺ BỐI CẢNH — chính nhà thờ đó sáu tiếng sau, khách đã về hết, hoa đã héo. Biến thể giờ của REF_NHATHO_SANG.\n"
  "Dùng S4.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở cuối lối đi chính phía cửa lớn, cách bậc bàn thờ 22m —\n"
  "ĐÚNG góc máy của ảnh tham chiếu.\n\n"
  "GIỮ NGUYÊN 100% kiến trúc, đồ đạc, vật liệu và bố cục của ảnh bối cảnh đính kèm.\n\n"
  "CHỈ ĐỔI THỜI ĐIỂM VÀ TRẠNG THÁI — CHIỀU MUỘN, SAU KHI MỌI NGƯỜI ĐÃ VỀ. Nắng chiều xiên rất thấp qua dãy cửa sổ\n"
  "kính màu bên trái, thành hai vệt sáng dài màu hổ phách nằm ngang trên thảm đỏ và trên lưng ghế; các góc phòng\n"
  "chìm trong bóng mờ nhưng vẫn ĐỦ SÁNG để nhìn rõ mặt người, KHÔNG mảng đen đặc. Đèn chùm đã TẮT.\n"
  "ĐỔI THÊM: hoa cúc trắng ở đầu các hàng ghế đã RŨ XUỐNG và rụng vài cánh trên thảm; hai cây nến trên bàn thờ\n"
  "đã tắt, còn khói mảnh; một vài cuốn sách thánh ca bị bỏ lại nằm lệch trên mặt ghế; dưới sàn lối đi rải rác\n"
  "vài cánh hoa và một tờ chương trình lễ rơi úp. Phòng TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: nhà thờ trống lúc chiều muộn, đúng khoảnh khắc ngay TRƯỚC khi có người đẩy cửa lớn bước vào.",
  VL_NHATHO, FP_NHATHO, TR_NHATHO, bg="REF_NHATHO_SANG")

D("REF_NHATHOTIEC_CHIEU", "Nhà thờ St. Michael — CHIỀU, đám cưới nhà Hale",
  "THẺ BỐI CẢNH — vẫn nhà thờ đó, bốn tuần sau, được nhà Hale trang hoàng cho đám cưới truyền hình trực tiếp.\n"
  "Biến thể của REF_NHATHO_SANG. Dùng S20 · S21 · S22 · S23.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở cuối lối đi chính phía cửa lớn, cách bậc bàn thờ 22m —\n"
  "ĐÚNG góc máy của ảnh tham chiếu.\n\n"
  "GIỮ NGUYÊN 100% kiến trúc, cột đá, vòm trần, cửa sổ kính màu, sàn đá và các hàng ghế gỗ của ảnh bối cảnh đính kèm.\n\n"
  "ĐỔI THỜI ĐIỂM — ĐẦU GIỜ CHIỀU: nắng chiều mạnh và vàng ấm đổ chéo qua dãy cửa sổ kính màu bên trái thành những\n"
  "mảng sáng lớn có màu trên sàn đá. Toàn cảnh SÁNG RÕ và sang trọng, KHÔNG mảng đen đặc.\n\n"
  "ĐỔI TOÀN BỘ TRANG TRÍ — ĐÂY LÀ ĐÁM CƯỚI CỦA GIỚI SIÊU GIÀU, ĐẮT GẤP TRĂM LẦN LẦN TRƯỚC:\n"
  "· Thảm lối đi giữa đổi thành THẢM TRẮNG dày, hai mép rắc cánh hoa hồng trắng.\n"
  "· Đầu mỗi hàng ghế gắn một KHỐI HOA HỒNG TRẮNG VÀ LAN TRẮNG lớn cắm dày, buộc ruy băng satin trắng.\n"
  "· Hai bên bậc bàn thờ dựng hai CỘT HOA CAO ba mét kết hoa trắng; phía sau bàn thờ treo một MÀN LỤA TRẮNG rủ.\n"
  "· Trên cao dọc hai hàng cột treo các CHÙM ĐÈN PHA LÊ nhỏ đang bật.\n"
  "· Hai bên lối đi có bốn CHÂN MÁY QUAY TRUYỀN HÌNH màu đen với đèn LED tròn gắn trên, và hai dàn ĐÈN SÂN KHẤU\n"
  "  đặt sát tường; dây cáp đen được dán gọn xuống sàn.\n"
  "· Cuối lối đi bên phải, sát cửa hẹp ra hành lang phục vụ, kê một BÀN DÀI phủ khăn trắng có khay ly champagne.\n"
  "Phòng TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: nhà thờ đã trang hoàng xong và còn trống, đúng khoảnh khắc ngay TRƯỚC khi khách đầu tiên bước vào.",
  VL_NHATHO,
  FP_NHATHO + """
· BỔ SUNG CHO ĐÁM CƯỚI NHÀ HALE: CỬA PHỤC VỤ hẹp ở góc cuối phòng bên PHẢI là chỗ đứng cố định của nhân viên
  y tế; ngay cạnh nó là BÀN DÀI phủ khăn trắng có khay ly. CỘT ĐÁ THỨ BA tính từ cửa lớn về phía bàn thờ,
  bên phải lối đi, là chỗ chiếc xe lăn đỗ suốt buổi lễ. Bốn chân máy quay truyền hình đứng dọc hai bên lối đi.""",
  TR_NHATHO, bg="REF_NHATHO_SANG")

D("REF_BAIDOXE_SANG", "Bãi đỗ xe nhà thờ St. Michael — SÁNG",
  "THẺ BỐI CẢNH — bãi đỗ xe sau nhà thờ, nơi Maya quỳ xin tiền mẹ Ryan ngay sau khi bị bỏ ở bàn thờ. Dùng S2.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở mép bãi phía tường nhà thờ, cách hàng xe gần nhất 8m,\n"
  "nhìn chếch qua bãi về phía lối ra đường.\n\n"
  "KHÔNG GIAN: bãi đỗ xe ngoài trời của một nhà thờ Mỹ, BAN NGÀY, trời quang, nắng sáng cao và gắt, bóng đổ ngắn\n"
  "và rõ trên mặt nhựa. Toàn cảnh SÁNG RÕ.\n\n"
  "TRONG KHUNG: mặt sân trải NHỰA ĐƯỜNG XÁM ĐÃ BẠC, vạch kẻ ô đỗ màu trắng đã mờ, vài vết nứt được vá bằng nhựa đen.\n"
  "Đỗ rải rác chừng mười chiếc xe con đủ màu, trong đó có vài xe sang màu đen bóng đỗ gần lối ra — biển số các xe\n"
  "đều LÀM MỜ, không đọc được. Sát tường đá nhà thờ bên trái là một hàng BỤI CÂY THẤP cắt vuông và hai THÙNG RÁC\n"
  "KIM LOẠI XANH có nắp. Cuối bãi là hàng rào lưới thép thấp, sau đó là một hàng cây phong và mái nhà dân.\n"
  "Trên mặt sân gần thùng rác có vài cánh hoa trắng rơi và một dải ruy băng trắng bị gió thổi dạt vào chân tường.\n"
  "Bãi xe TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: bãi xe nắng và vắng, đúng khoảnh khắc ngay TRƯỚC khi có người bước ra từ cửa hông nhà thờ.",
  """VẬT LIỆU CHUNG (khu ngoài trời của nhà thờ):
· Tường nhà thờ là ĐÁ SA THẠCH MÀU MẬT ONG cùng loại với bên trong, mạch vữa rõ, chân tường có vệt rêu khô.
· Mặt sân là NHỰA ĐƯỜNG XÁM BẠC có vạch kẻ trắng mờ và vết vá đen.
· Cây cối là phong Mỹ lá xanh sẫm. Kim loại ngoài trời (thùng rác, hàng rào) sơn XANH RÊU đã tróc.
· BIỂN SỐ MỌI XE trong khung đều LÀM MỜ.""",
  """QUY HOẠCH KHÔNG GIAN 360° — BÃI ĐỖ XE (đứng giữa bãi, quay lưng về tường nhà thờ):
· SAU LƯNG: tường đá hông nhà thờ với một CỬA HÔNG GỖ SẪM có ba bậc đá, và một cửa sổ kính màu hẹp trên cao.
· ĐỐI DIỆN: lối ra đường có hai trụ gạch thấp, sau đó là mặt đường và hàng cây phong.
· BÊN TRÁI: hàng bụi cây cắt vuông chạy dọc tường và hai thùng rác kim loại xanh.
· BÊN PHẢI: ba hàng ô đỗ xe song song, xe đỗ thưa; xa nhất là hàng rào lưới thép và mái nhà dân.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· CỬA HÔNG NHÀ THỜ luôn ở phía SCREEN LEFT; LỐI RA ĐƯỜNG luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía nhà thờ thì hậu cảnh là tường đá và cửa hông; quay về phía lối ra thì hậu cảnh
  là hàng xe đỗ và hàng cây.
· Nắng luôn chiếu từ TRÊN CAO CHẾCH PHẢI MÀN HÌNH, bóng đổ ngắn về phía trái.""")

D("REF_BACTHEM_CHAPTOI", "Bậc thềm trước nhà thờ St. Michael — CHẬP TỐI",
  "THẺ BỐI CẢNH — bậc thềm đá trước cửa lớn, ngay sau khi mọi thứ sụp đổ trong nhà thờ. Dùng S24.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt dưới lòng đường trước nhà thờ, cách chân bậc thềm 12m,\n"
  "nhìn chếch lên mặt tiền và dãy bậc.\n\n"
  "GIỮ NGUYÊN vật liệu đá sa thạch màu mật ong và kiểu kiến trúc tân Gothic của ảnh bối cảnh đính kèm.\n"
  "ĐÂY LÀ MẶT TIỀN NHÀ THỜ, KHÔNG copy đồ đạc của ảnh gốc.\n\n"
  "KHÔNG GIAN: CHẬP TỐI, trời đã chuyển xanh mực loang tím ở chân trời, đèn đường vàng cam hai bên đã bật.\n"
  "Có ĐÈN PHA TRUYỀN HÌNH màu trắng lạnh chiếu từ dưới lòng đường lên bậc thềm, tạo hai lớp sáng chồng nhau —\n"
  "đủ SÁNG RÕ mặt người, KHÔNG mảng đen đặc.\n\n"
  "TRONG KHUNG: một dãy MƯỜI BẬC ĐÁ rộng chạy suốt mặt tiền, hai bên có LAN CAN ĐÁ THẤP; trên cùng là hai\n"
  "CÁNH CỬA GỖ SẪM lớn có bản lề đồng, đang MỞ HÉ. Hai bên cửa gắn hai ĐÈN LỒNG ĐỒNG THAU đang sáng.\n"
  "Dưới chân bậc, sát vỉa hè, đỗ hai XE TIN TỨC màu trắng có cột ăng-ten dựng cao và hai XE CẢNH SÁT bật đèn\n"
  "hiệu xanh đỏ nhấp nháy — biển số LÀM MỜ, thân xe KHÔNG có chữ đọc được.\n"
  "Trên vài bậc thềm rơi rải rác cánh hoa hồng trắng bị giẫm nát và một chiếc ly champagne rỗng nằm nghiêng.\n"
  "Bậc thềm TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: bậc thềm sáng đèn và trống, đúng khoảnh khắc ngay TRƯỚC khi cánh cửa lớn bật mở và người tràn ra.",
  """VẬT LIỆU CHUNG (mặt tiền nhà thờ):
· ĐÁ SA THẠCH MÀU MẬT ONG cùng loại với bên trong, khối lớn, mạch vữa rõ, chân tường sẫm màu vì ẩm.
· Cửa lớn bằng GỖ SỒI SẪM có đinh tán và bản lề ĐỒNG THAU xỉn. Đèn lồng hai bên cửa cũng bằng đồng thau.
· Bậc thềm là đá xám đã mòn lõm ở giữa mỗi bậc. Vỉa hè bê tông xám, lòng đường nhựa đen ướt sương.
· BIỂN SỐ và LOGO trên mọi xe trong khung đều LÀM MỜ, không đọc được.""",
  """QUY HOẠCH KHÔNG GIAN 360° — BẬC THỀM (đứng giữa dãy bậc, quay lưng về cửa lớn):
· SAU LƯNG: hai cánh cửa gỗ sồi lớn mở hé, hai đèn lồng đồng thau hai bên, phía trên là cửa sổ hoa hồng tròn
  và tháp chuông nhọn.
· ĐỐI DIỆN VÀ PHÍA DƯỚI: mười bậc đá xuống vỉa hè, rồi tới lòng đường có xe tin tức và xe cảnh sát đèn nhấp nháy.
· BÊN TRÁI: lan can đá thấp, một cây phong lớn và một trụ đèn đường vàng cam.
· BÊN PHẢI: lan can đá thấp, lối dốc lát đá dẫn vòng ra bãi đỗ xe phía sau.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· CỬA LỚN NHÀ THỜ luôn ở phía SCREEN LEFT (phía trên bậc); LÒNG ĐƯỜNG và xe tin tức luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía nhà thờ thì hậu cảnh là cửa gỗ và đèn lồng đồng; quay về phía đường thì hậu cảnh
  là xe tin tức, đèn hiệu nhấp nháy và hàng cây tối.
· Đèn pha truyền hình luôn chiếu TỪ DƯỚI PHẢI MÀN HÌNH hắt lên; đèn đường vàng cam hắt từ trên trái.""",
  bg="REF_BAIDOXE_SANG")

# ══════════════════════════ BỆNH VIỆN ══════════════════════════
VL_BV = """VẬT LIỆU CHUNG CỦA CẢ BỆNH VIỆN ST. AGNES (mọi phòng dùng chung, không đổi):
· Bệnh viện công Mỹ đã cũ, sạch sẽ, ngân sách eo hẹp: mọi thứ được lau chùi kỹ nhưng không có gì mới.
· Tường sơn màu XANH BẠC HÀ NHẠT ở nửa dưới và TRẮNG NGÀ ở nửa trên, ngăn nhau bằng một NẸP GỖ SẪM ngang tầm hông.
· Sàn lát VINYL CUỘN màu xám nhạt vân đá, mối nối hàn nhiệt, đã mòn bóng theo lối đi.
· Trần thả tấm khoáng trắng có đèn huỳnh quang âm trần hình chữ nhật.
· Cửa phòng bằng gỗ công nghiệp phủ laminate màu gỗ nhạt, có ô kính vuông nhỏ ở trên và tay nắm inox.
· Kim loại đều là INOX XƯỚC. Không có đồ trang trí cá nhân ở hành lang."""

D("REF_VIENPHI_RANGSANG", "Quầy viện phí St. Agnes — RẠNG SÁNG",
  "THẺ BỐI CẢNH GỐC CỦA CẢ BỆNH VIỆN. Quầy thu viện phí lúc 5 giờ 47 sáng, nơi Maya biết hoá đơn đã bằng không.\n"
  "Dùng S5.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở giữa sảnh chờ, cách mặt quầy 6m, nhìn thẳng vào quầy.\n\n"
  "KHÔNG GIAN: phòng thu viện phí của một bệnh viện công Mỹ đã cũ, lúc RẠNG SÁNG. Ngoài dãy cửa sổ cao bên phải,\n"
  "trời còn xanh mực nhưng đã hửng một vệt cam nhạt ở chân trời; đèn huỳnh quang âm trần BẬT hết, cho ánh sáng\n"
  "trắng hơi lạnh, đều và hơi rát. Hai lớp sáng chồng nhau. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một QUẦY DÀI mặt laminate màu xám nhạt chạy ngang phòng, cao ngang ngực, phía trên có TẤM KÍNH\n"
  "chắn với ba ô cửa giao dịch hình chữ nhật khoét ở dưới. Sau quầy là ba chỗ ngồi có MÀN HÌNH MÁY TÍNH đời cũ\n"
  "vỏ kem, bàn phím, máy in hoá đơn nhỏ và các khay nhựa đựng giấy tờ; sát tường sau là dãy TỦ HỒ SƠ KIM LOẠI\n"
  "màu ghi và một chiếc máy photocopy.\n"
  "Trước quầy là bốn HÀNG GHẾ CHỜ khung thép mặt nhựa màu xanh dương gắn liền nhau, một cây nước uống bằng nhựa\n"
  "trắng có bình úp, và một thùng rác inox có nắp lật.\n"
  "Trên tường trái treo một BẢNG THÔNG BÁO nỉ xanh ghim nhiều tờ giấy trắng — thấy giấy nhưng KHÔNG đọc được chữ.\n"
  "Trên quầy có một hộp khăn giấy đã móp và một chậu cây nhựa nhỏ.\n\n"
  "ĐÓNG BĂNG: phòng viện phí sáng đèn và trống, đúng khoảnh khắc ngay TRƯỚC khi có người đẩy cửa bước vào.",
  VL_BV,
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG VIỆN PHÍ (đứng giữa sảnh chờ, quay mặt vào quầy):
· ĐỐI DIỆN: QUẦY DÀI có tấm kính chắn và ba ô cửa giao dịch; sau quầy là ba bàn máy tính, dãy tủ hồ sơ kim loại
  và máy photocopy sát tường.
· BÊN PHẢI: dãy CỬA SỔ CAO khung nhôm nhìn ra bãi cỏ và bãi đỗ xe bệnh viện.
· BÊN TRÁI: tường có bảng thông báo nỉ xanh, cây nước uống và thùng rác inox.
· SAU LƯNG: bốn hàng ghế chờ nhựa xanh, rồi tới CỬA KÍNH HAI CÁNH tự động dẫn ra hành lang chính.
· Phòng rộng khoảng 9m, sâu 7m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· QUẦY GIAO DỊCH luôn ở phía SCREEN LEFT; CỬA KÍNH ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía nhân viên quầy thì hậu cảnh là tủ hồ sơ và màn hình máy tính; quay về phía
  người đến nộp tiền thì hậu cảnh là hàng ghế chờ và cửa kính.
· Ánh sáng huỳnh quang đều từ trên xuống; ánh rạng sáng ngoài cửa sổ luôn hắt từ BÊN PHẢI MÀN HÌNH.""")

D("REF_ICU_DEM", "Khoa hồi sức ICU, buồng 4 — ĐÊM",
  "THẺ BỐI CẢNH — buồng bệnh giường 12 nơi mẹ Maya nằm, ca đêm. Dùng S9.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở cửa buồng bệnh, cách chân giường 5m, nhìn chếch\n"
  "dọc theo giường về phía cửa sổ.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY VẬT LIỆU — màu sơn tường xanh bạc hà và trắng ngà,\n"
  "nẹp gỗ ngang, sàn vinyl xám, trần tấm khoáng. **ĐÂY LÀ MỘT CĂN PHÒNG KHÁC (BUỒNG BỆNH HỒI SỨC)** —\n"
  "KHÔNG copy quầy, tủ hồ sơ hay ghế chờ của ảnh gốc.\n\n"
  "KHÔNG GIAN: buồng bệnh hồi sức một giường, BAN ĐÊM. Ngoài cửa sổ là đêm đen và vài đốm đèn thành phố ở xa.\n"
  "Đèn trần chính TẮT; chỉ bật một ĐÈN ĐỌC gắn tường ở đầu giường cho quầng sáng ấm, cộng ánh sáng xanh lạnh hắt ra\n"
  "từ màn hình theo dõi và một vệt sáng trắng từ hành lang lọt qua khe cửa. Đủ SÁNG RÕ mặt người, KHÔNG mảng đen đặc.\n"
  "Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một GIƯỜNG BỆNH ĐIỆN đặt giữa phòng hơi chếch, thành chắn kim loại hai bên đã hạ một bên,\n"
  "ga trải trắng và chăn dệt màu trắng ngà kéo phẳng, gối trắng lõm dấu đầu — GIƯỜNG TRỐNG, KHÔNG có người nằm.\n"
  "Đầu giường phía tường có một MÀN HÌNH THEO DÕI đang chạy các đường sóng xanh lá và số nhỏ (không đọc rõ số),\n"
  "một CỘT TRUYỀN DỊCH inox treo hai túi dịch trong, và một hộp ổ cắm khí y tế màu trắng gắn tường.\n"
  "Bên phải giường là một BÀN ĐẨY nhỏ có bánh xe, trên đặt một khay inox, một hộp găng tay và một chai dung dịch\n"
  "sát khuẩn. Cuối giường treo một BÌA KẸP BỆNH ÁN bằng nhựa. Góc phòng có một GHẾ TỰA khung gỗ bọc nhựa xanh.\n"
  "Ở chân giường gắn một TẤM BIỂN TÊN nhựa trắng ngà — thấy rõ là có biển nhưng KHÔNG đọc được chữ trên đó.\n\n"
  "ĐÓNG BĂNG: buồng bệnh yên lặng lúc đêm, đúng khoảnh khắc ngay TRƯỚC khi có người đẩy cửa bước vào.",
  VL_BV,
  """QUY HOẠCH KHÔNG GIAN 360° — BUỒNG ICU GIƯỜNG 12 (đứng ở chân giường, quay mặt về đầu giường):
· ĐỐI DIỆN (đầu giường): tường có màn hình theo dõi, đèn đọc gắn tường và hộp ổ cắm khí y tế màu trắng.
· BÊN PHẢI: CỬA SỔ CAO khung nhôm có rèm lá dọc màu ngà kéo hé, nhìn ra đêm thành phố; dưới cửa sổ là ghế tựa
  bọc nhựa xanh cho người nhà.
· BÊN TRÁI: bàn đẩy có bánh xe với khay inox và hộp găng tay; sau đó là một BỒN RỬA TAY inox nhỏ gắn tường
  có bình xà phòng và hộp khăn giấy.
· SAU LƯNG: CỬA TRƯỢT KÍNH MỜ dẫn ra hành lang khoa hồi sức, khe cửa hắt vào một vệt sáng trắng.
· GIỮA PHÒNG: giường bệnh điện có thành chắn kim loại và cột truyền dịch inox bên đầu giường.
· Phòng rộng khoảng 5m, sâu 6m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· ĐẦU GIƯỜNG và màn hình theo dõi luôn ở phía SCREEN LEFT; CỬA TRƯỢT ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía đầu giường thì hậu cảnh là màn hình theo dõi và đèn đọc; quay về phía cửa
  thì hậu cảnh là cửa trượt kính mờ và bồn rửa tay.
· Ánh sáng ấm của đèn đọc luôn tới từ PHÍA TRÁI MÀN HÌNH, ánh xanh của màn hình theo dõi cũng vậy.""",
  bg="REF_VIENPHI_RANGSANG")

D("REF_ICU_NGAY", "Khoa hồi sức ICU, buồng 4 — BAN NGÀY",
  "THẺ BỐI CẢNH — chính buồng bệnh đó vào ban ngày, cảnh cuối phim khi Helen tỉnh lại. Biến thể giờ của REF_ICU_DEM.\n"
  "Dùng S25.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở cửa buồng bệnh, cách chân giường 5m — ĐÚNG góc máy\n"
  "của ảnh tham chiếu.\n\n"
  "GIỮ NGUYÊN 100% kiến trúc, đồ đạc, vị trí giường, thiết bị và vật liệu của ảnh bối cảnh đính kèm.\n\n"
  "CHỈ ĐỔI THỜI ĐIỂM — GIỮA BUỔI SÁNG, TRỜI QUANG: ngoài cửa sổ là trời sáng và tán cây xanh; rèm lá dọc được kéo\n"
  "mở hẳn, nắng sớm tràn vào thành một mảng sáng lớn ấm nằm trên ga giường và sàn vinyl. Đèn đọc đầu giường ĐÃ TẮT,\n"
  "đèn trần bật ở mức thấp. Toàn phòng SÁNG, ẤM và sạch — tương phản hoàn toàn với chính nó lúc đêm.\n"
  "THÊM MỘT THỨ: trên bậu cửa sổ đặt một BÌNH THUỶ TINH nhỏ cắm mấy bông cúc trắng còn tươi. Phòng TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: buồng bệnh ngập nắng và trống, đúng khoảnh khắc ngay TRƯỚC khi có người chạy vào cửa.",
  VL_BV,
  """QUY HOẠCH KHÔNG GIAN 360° — BUỒNG ICU GIƯỜNG 12 (đứng ở chân giường, quay mặt về đầu giường):
· ĐỐI DIỆN (đầu giường): màn hình theo dõi, đèn đọc gắn tường (đã tắt), hộp ổ cắm khí y tế trắng.
· BÊN PHẢI: cửa sổ cao rèm lá dọc kéo mở, nắng tràn vào; dưới cửa sổ là ghế tựa bọc nhựa xanh; trên bậu cửa sổ
  có bình hoa cúc trắng.
· BÊN TRÁI: bàn đẩy có khay inox, bồn rửa tay inox gắn tường.
· SAU LƯNG: cửa trượt kính mờ ra hành lang khoa hồi sức.
· GIỮA PHÒNG: giường bệnh điện có thành chắn và cột truyền dịch inox.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· ĐẦU GIƯỜNG luôn ở phía SCREEN LEFT; CỬA TRƯỢT ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về đầu giường thì hậu cảnh là màn hình theo dõi; quay về phía cửa thì hậu cảnh là
  cửa trượt kính mờ và bồn rửa tay.
· Nắng luôn tới từ BÊN PHẢI MÀN HÌNH (phía cửa sổ), đổ bóng nghiêng về bên trái.""",
  bg="REF_ICU_DEM")

D("REF_HR_NGAY", "Phòng nhân sự bệnh viện St. Agnes — BAN NGÀY",
  "THẺ BỐI CẢNH — phòng làm việc của giám đốc nhân sự, nơi Maya bị đình chỉ. Dùng S18.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở góc phòng phía cửa ra vào, cách mép bàn làm việc 4m.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY VẬT LIỆU — màu sơn tường, nẹp gỗ ngang, sàn vinyl xám,\n"
  "trần tấm khoáng, cửa laminate. **ĐÂY LÀ MỘT CĂN PHÒNG KHÁC (PHÒNG LÀM VIỆC HÀNH CHÍNH)** — KHÔNG copy quầy kính,\n"
  "ghế chờ hay tủ hồ sơ xếp dãy của ảnh gốc.\n\n"
  "KHÔNG GIAN: phòng làm việc cá nhân nhỏ trong khối hành chính bệnh viện, BAN NGÀY. Cửa sổ chớp lật hé mở cho\n"
  "nắng ban ngày vào thành các dải sáng nằm ngang trên tường; đèn huỳnh quang âm trần bật. Phòng SÁNG ĐỀU,\n"
  "hơi ngột ngạt. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một BÀN LÀM VIỆC gỗ công nghiệp màu gỗ nhạt kê chắn ngang phòng, trên có màn hình máy tính đời cũ\n"
  "xoay nghiêng, một bàn phím, một điện thoại bàn màu ghi, một khay giấy hai tầng và một hộp khăn giấy.\n"
  "Sau bàn là GHẾ XOAY bọc vải xanh sẫm; trước bàn là HAI GHẾ TỰA khung thép mặt nhựa màu ghi đặt song song.\n"
  "Sát tường trái là một TỦ HỒ SƠ GỖ bốn ngăn, trên nóc đặt một chậu cây trầu bà và một khung ảnh nhỏ ÚP MẶT XUỐNG.\n"
  "Trên tường sau lưng ghế xoay treo ba KHUNG BẰNG KHEN cỡ A4 — thấy rõ là bằng khen nhưng KHÔNG đọc được chữ.\n\n"
  "ĐÓNG BĂNG: phòng nhân sự sáng đèn và trống, đúng khoảnh khắc ngay TRƯỚC khi hai người bước vào và khép cửa.",
  VL_BV,
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG NHÂN SỰ (đứng ở giữa phòng, quay mặt về bàn làm việc):
· ĐỐI DIỆN: bàn làm việc gỗ nhạt có màn hình máy tính, điện thoại bàn và khay giấy; sau bàn là ghế xoay bọc vải
  xanh sẫm và mảng tường treo ba khung bằng khen.
· BÊN PHẢI: dãy cửa sổ chớp lật hé mở nhìn ra sân trong bệnh viện.
· BÊN TRÁI: tủ hồ sơ gỗ bốn ngăn, trên nóc có chậu trầu bà và một khung ảnh úp mặt.
· SAU LƯNG: CỬA GỖ LAMINATE có ô kính vuông nhỏ, dẫn ra hành lang khối hành chính; cạnh cửa là một mắc áo đứng.
· GIỮA PHÒNG: hai ghế tựa khung thép mặt nhựa ghi đặt trước bàn.
· Phòng rộng khoảng 4m, sâu 5m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· BÀN LÀM VIỆC luôn ở phía SCREEN LEFT; CỬA ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía người ngồi sau bàn thì hậu cảnh là tường bằng khen; quay về phía người ngồi
  ghế khách thì hậu cảnh là cửa gỗ và tủ hồ sơ.
· Nắng luôn tới từ BÊN PHẢI MÀN HÌNH qua cửa sổ chớp lật, thành các dải sáng nằm ngang.""",
  bg="REF_VIENPHI_RANGSANG")

D("REF_HANHLANG_NGAY", "Hành lang bệnh viện St. Agnes — BAN NGÀY",
  "THẺ BỐI CẢNH — hành lang chính dẫn ra sảnh trước, nơi Maya bị áp giải ra và dặn Diane trở mẹ hai tiếng một lần.\n"
  "Dùng S18.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt giữa hành lang, cách ngã rẽ cuối hành lang 12m,\n"
  "nhìn dọc theo hành lang về phía sảnh trước.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY VẬT LIỆU — màu sơn tường, nẹp gỗ ngang, sàn vinyl,\n"
  "trần tấm khoáng, cửa laminate. **ĐÂY LÀ MỘT KHÔNG GIAN KHÁC (HÀNH LANG)** — KHÔNG copy quầy kính hay ghế chờ.\n\n"
  "KHÔNG GIAN: hành lang dài của bệnh viện công, BAN NGÀY. Đèn huỳnh quang âm trần bật hết cho ánh sáng trắng đều;\n"
  "cuối hành lang là mảng CỬA KÍNH lớn của sảnh trước, ngoài đó là ánh sáng ban ngày trắng chói khiến cuối hành lang\n"
  "sáng hơn hẳn. Toàn cảnh SÁNG RÕ. Hành lang TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: hành lang rộng ba mét, hai bên là tường sơn xanh bạc hà nửa dưới, có TAY VỊN INOX chạy suốt dọc\n"
  "hai bên tường. Dọc tường trái là ba CỬA PHÒNG laminate có ô kính vuông nhỏ; dọc tường phải là một dãy BĂNG GHẾ\n"
  "NHỰA XANH gắn tường, một cây nước uống, một xe đẩy dụng cụ y tế inox đỗ sát tường và một BỘ RỬA TAY KHÔ gắn tường.\n"
  "Trên trần treo hai BIỂN CHỈ DẪN nhựa trắng hình chữ nhật có mũi tên — thấy rõ mũi tên nhưng KHÔNG đọc được chữ.\n"
  "Cuối hành lang bên phải có một QUẦY TIẾP ĐÓN thấp và sau đó là cửa kính ra sảnh trước.\n\n"
  "ĐÓNG BĂNG: hành lang sáng đèn và vắng, đúng khoảnh khắc ngay TRƯỚC khi một nhóm người rẽ vào từ cuối hành lang.",
  VL_BV,
  """QUY HOẠCH KHÔNG GIAN 360° — HÀNH LANG CHÍNH (đứng giữa hành lang, quay mặt về sảnh trước):
· ĐỐI DIỆN (cuối hành lang): quầy tiếp đón thấp và mảng CỬA KÍNH lớn ra sảnh trước, ánh sáng ban ngày trắng chói
  hắt ngược vào hành lang.
· BÊN TRÁI: ba cửa phòng laminate có ô kính vuông, tay vịn inox chạy dọc tường.
· BÊN PHẢI: băng ghế nhựa xanh gắn tường, cây nước uống, xe đẩy dụng cụ inox và bộ rửa tay khô.
· SAU LƯNG: hành lang chạy tiếp về phía khối hành chính rồi rẽ trái tại một ngã rẽ có biển chỉ dẫn treo trần.
· Hành lang rộng 3m, dài khoảng 25m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· SẢNH TRƯỚC (cửa kính sáng) luôn ở phía SCREEN RIGHT; khối hành chính phía trong luôn ở phía SCREEN LEFT.
· Nền theo nhân vật: quay về phía người đi ra thì hậu cảnh là cửa kính sáng chói và quầy tiếp đón; quay về phía
  người đi vào thì hậu cảnh là dãy cửa phòng và hành lang hun hút.
· Ánh sáng ban ngày mạnh luôn tới từ BÊN PHẢI MÀN HÌNH (phía sảnh), đèn huỳnh quang đều từ trên xuống.""",
  bg="REF_VIENPHI_RANGSANG")
