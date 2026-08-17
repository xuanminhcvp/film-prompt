# -*- coding: utf-8 -*-
"""THẺ ĐỊA ĐIỂM — phố xá, nhà cổng Kane, dinh thự, công sở, toà án, hầm xe."""
from lib import ref, luatchung

R = []
D = lambda rid, label, desc, prompt, vl, fp, tr, bg=None: R.append(
    ref(rid, label, desc, prompt, bg=bg, luat=luatchung(vl, fp, tr)))

D("REF_CAMDO_NGAY", "Tiệm cầm đồ — BAN NGÀY",
  "THẺ BỐI CẢNH — tiệm cầm đồ nơi Maya bán chiếc nhẫn cưới của mẹ. Dùng S3.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở phía cửa ra vào, cách mặt quầy 5m, nhìn thẳng vào quầy.\n\n"
  "KHÔNG GIAN: một tiệm cầm đồ nhỏ ở phố Mỹ, BAN NGÀY. Nắng ban ngày lọt qua ô kính mặt tiền có dán decal mờ,\n"
  "thành một mảng sáng trắng đổ chéo lên sàn; trong tiệm bật hai bóng đèn tuýp trắng và một dãy ĐÈN LED trong tủ kính.\n"
  "Ánh sáng ĐỦ RÕ, hơi bụi bặm. Tiệm TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một QUẦY KÍNH DÀI chạy ngang phòng, cao ngang thắt lưng, mặt kính dày, bên trong bày trên nhung\n"
  "đen các món kim hoàn nhỏ, đồng hồ cũ và vài chiếc nhẫn — nhìn thấy lấp lánh nhưng KHÔNG rõ từng món.\n"
  "Trên mặt quầy có một CÂN TIỂU LY điện tử nhỏ, một ĐÈN SOI có kính lúp cần gập, một tấm ĐỆM NHUNG XÁM để đặt đồ,\n"
  "một cuốn sổ ghi chép bìa cứng và một máy tính bỏ túi.\n"
  "Sau quầy là GIÁ TƯỜNG bằng gỗ ép treo chi chít đàn ghi ta điện, kèn saxophone, máy khoan, loa thùng và vài\n"
  "chiếc va li da cũ xếp chồng. Tường bên trái treo một tấm LƯỚI THÉP gắn dụng cụ. Góc phải có CAMERA AN NINH\n"
  "hình hộp gắn cao và một két sắt cũ màu xám.\n"
  "Sàn lát GẠCH VINYL VUÔNG màu be đã ố và tróc mép. Trần thấp có ống điện chạy nổi.\n\n"
  "ĐÓNG BĂNG: tiệm cầm đồ sáng đèn và trống, đúng khoảnh khắc ngay TRƯỚC khi chuông cửa kêu và có người bước vào.",
  """VẬT LIỆU CHUNG (tiệm cầm đồ):
· Cửa hàng nhỏ, cũ, chật, mọi thứ đều là đồ đã qua tay: gỗ ép sẫm, kim loại xước, kính dày có vết xước mờ.
· Tường sơn màu BE NGẢ VÀNG đã ố, chân tường ốp gỗ sẫm thấp.
· Sàn gạch vinyl vuông màu be, mối ghép hở, đã tróc mép ở lối đi.
· Kim loại là THÉP MẠ ĐÃ XƯỚC và NHÔM CŨ. Không có gì mới trong tiệm.""",
  """QUY HOẠCH KHÔNG GIAN 360° — TIỆM CẦM ĐỒ (đứng trước quầy, quay mặt vào trong):
· ĐỐI DIỆN: QUẦY KÍNH DÀI với cân tiểu ly, đèn soi kính lúp và đệm nhung xám; sau quầy là giá tường treo nhạc cụ,
  dụng cụ và va li cũ.
· BÊN PHẢI: góc có camera an ninh hình hộp gắn cao và một két sắt xám cũ đặt dưới đất.
· BÊN TRÁI: tấm lưới thép gắn tường treo dụng cụ, dưới chân là ba thùng nhựa đựng dây cáp.
· SAU LƯNG: MẶT TIỀN KÍNH có decal mờ và CỬA KÍNH có chuông cửa nhỏ, ngoài kia là vỉa hè và phố.
· Tiệm rộng khoảng 6m, sâu 8m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· QUẦY và người chủ tiệm luôn ở phía SCREEN LEFT; CỬA RA PHỐ luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía chủ tiệm thì hậu cảnh là giá tường treo nhạc cụ; quay về phía khách thì hậu cảnh
  là mặt tiền kính sáng và cửa ra phố.
· Nắng ngoài phố luôn hắt vào từ BÊN PHẢI MÀN HÌNH thành một mảng sáng chéo trên sàn.""")

D("REF_NGANHANG_NGAY", "Sảnh ngân hàng — BAN NGÀY",
  "THẺ BỐI CẢNH — sảnh giao dịch nơi hồ sơ vay lần thứ ba của Maya bị từ chối. Dùng S3.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở giữa sảnh, cách bàn tín dụng 6m, nhìn chếch về\n"
  "dãy bàn tư vấn.\n\n"
  "KHÔNG GIAN: sảnh giao dịch một chi nhánh ngân hàng Mỹ hạng trung, BAN NGÀY. Mặt tiền kính lớn cho nắng ban ngày\n"
  "tràn vào; đèn âm trần trắng trung tính bật đều. Toàn cảnh SÁNG, SẠCH, LẠNH. Sảnh TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: sàn lát ĐÁ MÀI XÁM SÁNG bóng. Bên trái là DÃY QUẦY GIAO DỊCH bằng gỗ veneer sẫm mặt đá nhân tạo\n"
  "trắng, có bốn ô làm việc, phía trên treo bốn màn hình nhỏ tối. Giữa sảnh có HAI CỘT DÂY CĂNG bằng inox chia luồng\n"
  "xếp hàng, dây màu xanh navy. Bên phải là KHU TƯ VẤN: hai BÀN LÀM VIỆC gỗ sẫm, mỗi bàn có màn hình máy tính,\n"
  "một khay giấy, một hộp danh thiếp nhỏ và hai GHẾ KHÁCH bọc nỉ xám đặt trước bàn.\n"
  "Sát tường sau là một BẢNG TỶ GIÁ điện tử tối màu — thấy khung bảng nhưng KHÔNG đọc được chữ hay số.\n"
  "Cạnh cửa có một KỆ TỜ RƠI bằng mica trong đựng các tờ gấp nhiều màu (không đọc được chữ) và một chậu cây\n"
  "lá lớn trong chậu gốm trắng.\n\n"
  "ĐÓNG BĂNG: sảnh ngân hàng sáng và vắng, đúng khoảnh khắc ngay TRƯỚC khi cửa tự động mở và có người bước vào.",
  """VẬT LIỆU CHUNG (chi nhánh ngân hàng):
· Kiến trúc thương mại Mỹ hạng trung, mới chừng mười năm: sạch, lạnh, không có gì cá nhân.
· Tường sơn TRẮNG NGÀ, một mảng tường sau quầy ốp gỗ veneer màu ÓC CHÓ SẪM.
· Sàn ĐÁ MÀI XÁM SÁNG đánh bóng. Trần thạch cao phẳng có đèn âm trần tròn.
· Mặt bàn và mặt quầy là ĐÁ NHÂN TẠO TRẮNG. Kim loại đều là INOX SÁNG.
· KHÔNG có logo hay tên ngân hàng nào đọc được ở bất kỳ đâu trong khung.""",
  """QUY HOẠCH KHÔNG GIAN 360° — SẢNH NGÂN HÀNG (đứng giữa sảnh, quay mặt về quầy giao dịch):
· ĐỐI DIỆN: dãy quầy giao dịch bốn ô bằng gỗ veneer mặt đá trắng, phía trên có bốn màn hình nhỏ tối,
  sau quầy là mảng tường ốp gỗ óc chó và bảng tỷ giá điện tử.
· BÊN PHẢI: khu tư vấn với hai bàn làm việc gỗ sẫm và các ghế khách bọc nỉ xám.
· BÊN TRÁI: hai cột dây căng inox chia luồng xếp hàng, một máy ATM âm tường và một kệ tờ rơi mica.
· SAU LƯNG: MẶT TIỀN KÍNH cao suốt trần và CỬA TỰ ĐỘNG hai cánh ra vỉa hè, cạnh cửa có chậu cây lá lớn.
· Sảnh rộng khoảng 12m, sâu 10m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· KHU TƯ VẤN và người của ngân hàng luôn ở phía SCREEN LEFT; CỬA KÍNH ra phố luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía nhân viên ngân hàng thì hậu cảnh là quầy giao dịch và tường gỗ óc chó;
  quay về phía khách thì hậu cảnh là mặt tiền kính sáng và kệ tờ rơi.
· Nắng ban ngày luôn tới từ BÊN PHẢI MÀN HÌNH qua mặt tiền kính.""")

D("REF_UBND_NGAY", "Phòng hộ tịch toà thị chính — BAN NGÀY",
  "THẺ BỐI CẢNH — phòng đăng ký kết hôn, nơi Maya và Adrian ký giấy trong bốn phút. Dùng S6.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở phía cửa ra vào, cách bàn hộ tịch 5m, nhìn thẳng\n"
  "vào bàn.\n\n"
  "KHÔNG GIAN: một phòng hộ tịch nhỏ trong toà thị chính Mỹ xây thập niên 1930, BAN NGÀY. Hai cửa sổ cao khung gỗ\n"
  "cho nắng ban ngày vào thành hai cột sáng nghiêng có bụi bay; đèn quả cầu thuỷ tinh trên trần bật. Phòng SÁNG,\n"
  "trang nghiêm mà tẻ nhạt. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một BÀN GỖ SẪM lớn kê ngang phòng, trên có một cuốn SỔ ĐĂNG KÝ bìa da to đang mở, một con dấu gỗ\n"
  "cán tròn với hộp mực, một khay bút, một máy tính đời cũ vỏ kem và một lá cờ nhỏ cắm ống — LÁ CỜ TRƠN MÀU XANH\n"
  "NAVY, KHÔNG có hoa văn hay chữ.\n"
  "Sau bàn là hai GHẾ XOAY bọc nỉ nâu và một dãy TỦ HỒ SƠ GỖ cao tới ngực. Trước bàn kê HAI GHẾ GỖ TỰA LƯNG NAN\n"
  "và một KHOẢNG TRỐNG rộng bên phải (đủ chỗ cho một chiếc xe lăn đỗ).\n"
  "Tường ốp gỗ sẫm nửa dưới, sơn kem nửa trên; treo hai KHUNG GIẤY CHỨNG NHẬN cỡ lớn và một ĐỒNG HỒ TRÒN\n"
  "vỏ gỗ — mặt đồng hồ chỉ giờ nhưng KHÔNG có chữ số đọc được.\n"
  "Sàn lát ĐÁ HOA VUÔNG đen trắng đã mòn. Góc phòng có một cây cảnh giả trong chậu đồng.\n\n"
  "ĐÓNG BĂNG: phòng hộ tịch sáng nắng và trống, đúng khoảnh khắc ngay TRƯỚC khi cửa mở và có người bước vào.",
  """VẬT LIỆU CHUNG (toà thị chính):
· Công thự Mỹ thập niên 1930: bề thế, mòn, đã sửa chữa nhiều lần bằng vật liệu rẻ hơn.
· Tường ốp GỖ SỒI SẪM nửa dưới cao ngang ngực, nửa trên sơn màu KEM ĐÃ Ố.
· Sàn ĐÁ HOA VUÔNG ĐEN TRẮNG đã mòn lõm ở lối đi. Trần cao ba mét rưỡi có phào chỉ thạch cao đơn giản.
· Cửa và khung cửa sổ bằng GỖ SỒI SẪM đánh vec-ni đã bong. Kim loại là ĐỒNG THAU XỈN.
· KHÔNG có chữ đọc được trên bất kỳ giấy tờ, bảng hay con dấu nào.""",
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG HỘ TỊCH (đứng trước bàn, quay mặt vào bàn):
· ĐỐI DIỆN: bàn gỗ sẫm lớn có sổ đăng ký, con dấu và máy tính cũ; sau bàn là hai ghế xoay và dãy tủ hồ sơ gỗ.
· BÊN TRÁI: hai CỬA SỔ CAO khung gỗ nhìn ra phố, bậu cửa sổ dày có một chậu cây nhỏ.
· BÊN PHẢI: mảng tường ốp gỗ treo hai khung giấy chứng nhận và đồng hồ tròn vỏ gỗ; dưới chân là khoảng trống rộng.
· SAU LƯNG: CỬA GỖ HAI CÁNH có ô kính mờ ở nửa trên dẫn ra hành lang; cạnh cửa có một băng ghế gỗ dài chờ.
· Phòng rộng khoảng 7m, sâu 6m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· BÀN HỘ TỊCH luôn ở phía SCREEN LEFT; CỬA ra hành lang luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía cán bộ hộ tịch thì hậu cảnh là tủ hồ sơ gỗ và giấy chứng nhận treo tường;
  quay về phía cặp đôi thì hậu cảnh là cửa gỗ hai cánh và băng ghế chờ.
· Nắng luôn tới từ BÊN TRÁI MÀN HÌNH qua hai cửa sổ cao, thành cột sáng nghiêng.""")

D("REF_CONGNHA_CHIEU", "Nhà cổng cũ, dinh thự Kane — CHIỀU",
  "THẺ BỐI CẢNH GỐC CỦA CẢ KHU DINH THỰ KANE. Cổng sắt lớn, đường phục vụ và căn nhà cổng mái vá bạt nơi Adrian\n"
  "bị đẩy ra ở. Dùng S7.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt trên đường phục vụ, cách bậc thềm nhà cổng 10m,\n"
  "nhìn chếch để thấy cả căn nhà cổng bên phải lẫn cổng sắt và toà nhà chính trên đồi phía sau.\n\n"
  "KHÔNG GIAN: khu cổng của một dinh thự Mỹ rất giàu, BUỔI CHIỀU. Nắng chiều thấp màu vàng mật đổ chéo từ bên trái,\n"
  "bóng cây dài trên mặt cỏ; trời trong. Toàn cảnh SÁNG RÕ và ấm. Khung hình TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: chính giữa phía sau là một CỔNG SẮT UỐN HAI CÁNH cao bốn mét sơn đen, hoa văn xoắn, gắn giữa hai\n"
  "TRỤ GẠCH ĐÁ lớn có chóp đá; cổng đang ĐÓNG. Sau cổng là đường xe rải sỏi trắng chạy vòng lên đồi, hai bên là\n"
  "bãi cỏ cắt phẳng và hàng cây phong cao. Trên đỉnh đồi phía xa là TOÀ NHÀ CHÍNH bằng đá sáng màu, ba tầng,\n"
  "mái dốc, nhiều ống khói — nhìn thấy rõ nhưng ở xa và hơi mờ sương.\n"
  "Bên PHẢI khung, sát đường phục vụ, là CĂN NHÀ CỔNG: nhà gạch đỏ một tầng nhỏ, cũ, tường loang rêu ở chân,\n"
  "MÁI NGÓI CÓ MỘT MẢNG VÁ BẰNG BẠT NHỰA MÀU XANH chằng dây; hai cửa sổ khung gỗ sơn trắng đã tróc;\n"
  "CỬA RA VÀO bằng gỗ nâu có BA BẬC ĐÁ dẫn lên, KHÔNG CÓ DỐC XE LĂN — đây là chi tiết bắt buộc phải thấy rõ.\n"
  "Cạnh nhà là một NHÀ KHO GỖ nhỏ cửa hé, bên trong lấp ló tấm ván ép và dụng cụ. Trước nhà có một ghế băng gỗ\n"
  "đã bạc và một chậu đất nung trồng cây khô.\n\n"
  "ĐÓNG BĂNG: khu cổng nắng chiều và vắng, đúng khoảnh khắc ngay TRƯỚC khi một chiếc xe đỗ lại trên đường phục vụ.",
  """VẬT LIỆU CHUNG CỦA CẢ KHU DINH THỰ KANE (mọi khung dùng chung, không đổi):
· Dinh thự Mỹ tân cổ điển của một gia tộc rất giàu: bề thế, lạnh, được chăm sóc cực kỳ kỹ ở khu chính.
· Toà nhà chính và các trụ cổng bằng ĐÁ SÁNG MÀU KEM XÁM; cổng và hàng rào bằng SẮT UỐN SƠN ĐEN.
· Đường xe rải SỎI TRẮNG, bãi cỏ cắt phẳng đều, hàng cây phong cao.
· SỰ TƯƠNG PHẢN LÀ TRỌNG TÂM THỊ GIÁC: khu chính hoàn hảo và đắt tiền — căn nhà cổng thì gạch đỏ cũ, tường loang
  rêu, mái vá bạt xanh, ba bậc đá không có dốc.
· KHÔNG có chữ đọc được ở bất kỳ đâu: không biển tên, không số nhà, không logo.""",
  """QUY HOẠCH KHÔNG GIAN 360° — KHU CỔNG (đứng trên đường phục vụ, quay mặt về cổng sắt):
· ĐỐI DIỆN: CỔNG SẮT UỐN HAI CÁNH cao bốn mét giữa hai trụ đá; sau cổng là đường sỏi trắng vòng lên đồi và
  TOÀ NHÀ CHÍNH ba tầng bằng đá sáng màu ở xa trên đỉnh đồi.
· BÊN PHẢI: CĂN NHÀ CỔNG gạch đỏ một tầng, mái vá bạt xanh, ba bậc đá lên cửa gỗ nâu, hai cửa sổ khung gỗ trắng
  tróc sơn; kế đó là nhà kho gỗ nhỏ.
· BÊN TRÁI: bãi cỏ rộng, hàng cây phong cao và một đoạn hàng rào sắt đen chạy dọc ranh đất.
· SAU LƯNG: đường phục vụ trải nhựa cũ chạy ra đường công cộng, hai bên có bụi cây thấp.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· CĂN NHÀ CỔNG luôn ở phía SCREEN RIGHT; CỔNG SẮT và toà nhà chính trên đồi luôn ở phía SCREEN LEFT.
· Nền theo nhân vật: quay về phía người đứng ở bậc thềm thì hậu cảnh là tường gạch đỏ và cửa sổ tróc sơn;
  quay về phía người đứng ngoài đường thì hậu cảnh là cổng sắt đen và toà nhà chính trên đồi.
· Nắng chiều luôn tới từ BÊN TRÁI MÀN HÌNH và thấp, đổ bóng dài về bên phải.""")

D("REF_CONGNHA_SANG", "Nhà cổng cũ, dinh thự Kane — SÁNG (ngày trục xuất)",
  "THẺ BỐI CẢNH — chính khu cổng đó vào buổi sáng bị đuổi khỏi nhà. Biến thể giờ của REF_CONGNHA_CHIEU. Dùng S16.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt trên đường phục vụ, cách bậc thềm nhà cổng 10m —\n"
  "ĐÚNG góc máy của ảnh tham chiếu.\n\n"
  "GIỮ NGUYÊN 100% kiến trúc, vật liệu, vị trí cổng sắt, căn nhà cổng, nhà kho và toà nhà chính trên đồi của ảnh\n"
  "bối cảnh đính kèm.\n\n"
  "CHỈ ĐỔI THỜI ĐIỂM VÀ THÊM ĐỒ — GIỮA BUỔI SÁNG, TRỜI XÁM ÍT MÂY: ánh sáng ban ngày trắng, khuếch tán đều,\n"
  "bóng đổ nhạt và ngắn, cỏ còn ướt sương. Toàn cảnh SÁNG RÕ nhưng lạnh màu hơn ảnh gốc.\n"
  "THÊM VÀO: trước ba bậc đá của nhà cổng, trên nền đất, xếp BỐN THÙNG CARTON đã gấp nắp và HAI TÚI VẢI to\n"
  "đựng đồ — đồ đạc vừa được dọn ra. Cạnh đó dựng một TẤM VÁN ÉP dài đặt tạm làm dốc lên bậc thềm.\n"
  "Trên đường phục vụ, đỗ một XE TẢI NHỎ MÀU TRẮNG mở thùng sau (biển số LÀM MỜ, thân xe KHÔNG có chữ).\n"
  "Cửa nhà kho gỗ mở toang. Khung hình TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: khu cổng buổi sáng với đồ đạc đã dọn ra sân, đúng khoảnh khắc ngay TRƯỚC khi có người bước ra khỏi cửa.",
  """VẬT LIỆU CHUNG CỦA CẢ KHU DINH THỰ KANE (giữ nguyên như thẻ gốc):
· Toà nhà chính và trụ cổng bằng ĐÁ SÁNG MÀU KEM XÁM; cổng và hàng rào SẮT UỐN SƠN ĐEN; đường xe rải SỎI TRẮNG.
· Căn nhà cổng bằng GẠCH ĐỎ CŨ, tường loang rêu ở chân, mái ngói có mảng VÁ BẠT NHỰA XANH, cửa sổ khung gỗ trắng
  đã tróc sơn, ba bậc đá không có dốc xe lăn.
· BIỂN SỐ mọi xe trong khung đều LÀM MỜ. KHÔNG có chữ đọc được ở bất kỳ đâu.""",
  """QUY HOẠCH KHÔNG GIAN 360° — KHU CỔNG (đứng trên đường phục vụ, quay mặt về cổng sắt):
· ĐỐI DIỆN: cổng sắt uốn hai cánh giữa hai trụ đá, đường sỏi trắng lên đồi, toà nhà chính ba tầng ở xa.
· BÊN PHẢI: căn nhà cổng gạch đỏ với ba bậc đá và tấm ván ép đặt tạm làm dốc; trước bậc là bốn thùng carton
  và hai túi vải đựng đồ; kế đó là nhà kho gỗ cửa mở toang.
· BÊN TRÁI: bãi cỏ ướt sương, hàng cây phong và hàng rào sắt đen.
· SAU LƯNG: đường phục vụ có một xe tải nhỏ màu trắng đỗ, thùng sau mở.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· CĂN NHÀ CỔNG luôn ở phía SCREEN RIGHT; CỔNG SẮT và toà nhà chính luôn ở phía SCREEN LEFT.
· Nền theo nhân vật: quay về phía bậc thềm thì hậu cảnh là tường gạch đỏ và đống thùng carton; quay về phía
  đường thì hậu cảnh là cổng sắt đen, xe tải trắng và toà nhà chính trên đồi.
· Ánh sáng ban ngày trắng khuếch tán đều từ trên xuống, KHÔNG có nguồn sáng hướng mạnh.""",
  bg="REF_CONGNHA_CHIEU")

D("REF_NHACONG_CHIEU", "Trong nhà cổng — CHIỀU",
  "THẺ BỐI CẢNH — một gian phòng duy nhất bên trong nhà cổng, buổi chiều đầu tiên Maya bước vào. Dùng S7.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở góc phòng phía cửa ra vào, cách giường 5m,\n"
  "nhìn chéo qua cả gian phòng.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY VẬT LIỆU của căn nhà cổng — gạch đỏ cũ, khung cửa sổ\n"
  "gỗ sơn trắng đã tróc, mức độ cũ kỹ. **ĐÂY LÀ BÊN TRONG CĂN NHÀ ĐÓ** — KHÔNG copy cổng sắt, bãi cỏ hay toà nhà\n"
  "chính của ảnh gốc.\n\n"
  "KHÔNG GIAN: một gian phòng chữ nhật duy nhất, trần thấp, BUỔI CHIỀU. Nắng chiều vàng mật xiên thấp qua hai\n"
  "cửa sổ bên trái thành hai vệt sáng dài trên sàn gỗ; trong phòng chưa bật đèn nhưng vẫn ĐỦ SÁNG RÕ, KHÔNG mảng\n"
  "đen đặc. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: tường trát vữa sơn màu XANH XÁM NHẠT đã ố và bong vài mảng nhỏ; một vệt ố nước loang ở góc trần.\n"
  "Sàn VÁN GỖ SẪM cũ, khe ván hở, trải một tấm thảm dệt hình chữ nhật màu nâu đất đã bạc.\n"
  "Kê sát tường trong là một GIƯỜNG ĐƠN khung sắt sơn trắng, ga trải xám phẳng, hai gối. Cạnh giường là một\n"
  "TỦ ĐẦU GIƯỜNG GỖ hai ngăn kéo, trên đặt một đèn bàn chao vải kem, một cốc nước và một vỉ thuốc.\n"
  "Giữa phòng là một BÀN GỖ VUÔNG nhỏ với hai ghế gỗ không cùng bộ. Góc bếp nhỏ ở tường phải: tủ bếp gỗ sơn trắng\n"
  "đã ố, bồn rửa inox nhỏ, một bếp điện đôi và một tủ lạnh mini màu kem.\n"
  "Cạnh cửa ra vào có một mắc áo gỗ và một đôi găng tay len đặt trên bậu. Trên tường treo một tấm gương chữ nhật\n"
  "viền gỗ mộc. KHÔNG có tranh ảnh cá nhân nào.\n\n"
  "ĐÓNG BĂNG: gian phòng nắng chiều và trống, đúng khoảnh khắc ngay TRƯỚC khi cửa mở và có người vào.",
  """VẬT LIỆU CHUNG CỦA CĂN NHÀ CỔNG (trong và ngoài dùng chung):
· Nhà gạch đỏ một tầng xây từ lâu, được sửa chữa tối thiểu: mọi thứ cũ nhưng SẠCH và NGĂN NẮP, KHÔNG bẩn thỉu.
· Trong nhà: tường trát vữa sơn XANH XÁM NHẠT đã ố, sàn VÁN GỖ SẪM khe hở, trần thấp 2m6 có dầm gỗ lộ.
· Cửa và khung cửa sổ bằng GỖ SƠN TRẮNG đã tróc từng mảng, lộ lớp sơn cũ bên dưới.
· Đồ đạc là đồ cũ không cùng bộ: khung sắt sơn trắng, gỗ mộc, vải bông màu trung tính.
· KHÔNG có đồ điện tử đắt tiền, KHÔNG có vật trang trí cá nhân, KHÔNG có chữ đọc được.""",
  """QUY HOẠCH KHÔNG GIAN 360° — TRONG NHÀ CỔNG (đứng giữa phòng, quay lưng về cửa ra vào):
· ĐỐI DIỆN (tường trong): GIƯỜNG ĐƠN khung sắt trắng kê sát tường, tủ đầu giường gỗ có đèn bàn chao vải kem;
  cạnh giường là một CỬA GỖ TRẮNG HẸP dẫn vào phòng tắm, thường đóng.
· BÊN TRÁI: hai CỬA SỔ khung gỗ trắng tróc sơn nhìn ra bãi cỏ và cổng sắt, rèm vải mỏng màu ngà vén hai bên.
· BÊN PHẢI: góc bếp nhỏ với tủ bếp gỗ sơn trắng, bồn rửa inox, bếp điện đôi và tủ lạnh mini màu kem.
· SAU LƯNG: CỬA RA VÀO bằng gỗ nâu mở thẳng ra ba bậc đá; cạnh cửa là mắc áo gỗ và một tấm gương viền gỗ mộc.
· GIỮA PHÒNG: bàn gỗ vuông nhỏ với hai ghế gỗ không cùng bộ, trên thảm dệt nâu đất.
· Phòng dài khoảng 7m, ngang 5m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· GIƯỜNG và cửa phòng tắm luôn ở phía SCREEN LEFT; CỬA RA VÀO luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía giường thì hậu cảnh là khung giường sắt trắng và tủ đầu giường; quay về phía
  cửa ra vào thì hậu cảnh là cánh cửa gỗ nâu, mắc áo và tấm gương.
· Nguồn sáng ngoài trời luôn tới từ PHÍA SAU MÁY QUAY BÊN TRÁI qua hai cửa sổ, đổ vệt sáng chéo trên sàn gỗ.""",
  bg="REF_CONGNHA_CHIEU")

D("REF_NHACONG_DEM", "Trong nhà cổng — ĐÊM",
  "THẺ BỐI CẢNH — chính gian phòng đó về đêm, khi Maya thay băng cho Adrian và tìm thấy hồ sơ giám định.\n"
  "Biến thể giờ của REF_NHACONG_CHIEU. Dùng S11.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở góc phòng phía cửa ra vào, cách giường 5m —\n"
  "ĐÚNG góc máy của ảnh tham chiếu.\n\n"
  "GIỮ NGUYÊN 100% kiến trúc, đồ đạc, vị trí giường, bàn, góc bếp và vật liệu của ảnh bối cảnh đính kèm.\n\n"
  "CHỈ ĐỔI THỜI ĐIỂM — BAN ĐÊM: ngoài hai cửa sổ là đêm đen, chỉ thấy một đốm đèn vàng rất xa trên đồi.\n"
  "Trong phòng bật ĐÈN BÀN chao vải kem ở tủ đầu giường và một ĐÈN TRẦN bóng đơn có chụp thiếc trắng giữa phòng,\n"
  "cho ánh sáng VÀNG ẤM và hơi yếu, quầng sáng gọn quanh giường và bàn, các góc phòng tối mờ nhưng vẫn ĐỦ SÁNG\n"
  "để nhìn rõ mặt người. KHÔNG mảng đen đặc.\n"
  "THÊM MỘT THỨ: trên mặt bàn gỗ vuông đặt một CHẬU NƯỚC INOX nhỏ, một chồng khăn bông trắng gấp và một cuộn băng\n"
  "gạc — đồ thay băng đã bày sẵn. Phòng TRỐNG NGƯỜI.\n\n"
  "ĐÓNG BĂNG: gian phòng sáng đèn vàng và trống, đúng khoảnh khắc ngay TRƯỚC khi có người từ phòng tắm đi ra.",
  """VẬT LIỆU CHUNG CỦA CĂN NHÀ CỔNG (giữ nguyên như thẻ gốc):
· Tường trát vữa sơn XANH XÁM NHẠT đã ố và bong mảng nhỏ, vệt ố nước ở góc trần.
· Sàn VÁN GỖ SẪM khe hở, thảm dệt nâu đất đã bạc. Trần thấp 2m6 có dầm gỗ lộ.
· Cửa và khung cửa sổ GỖ SƠN TRẮNG đã tróc. Đồ đạc cũ, không cùng bộ, sạch và ngăn nắp.
· KHÔNG có vật trang trí cá nhân, KHÔNG có chữ đọc được.""",
  """QUY HOẠCH KHÔNG GIAN 360° — TRONG NHÀ CỔNG (đứng giữa phòng, quay lưng về cửa ra vào):
· ĐỐI DIỆN: giường đơn khung sắt trắng, tủ đầu giường gỗ có đèn bàn đang bật, và cửa gỗ trắng hẹp vào phòng tắm.
· BÊN TRÁI: hai cửa sổ khung gỗ trắng, ngoài là đêm đen; rèm vải mỏng màu ngà vén hai bên.
· BÊN PHẢI: góc bếp nhỏ với tủ bếp gỗ sơn trắng, bồn rửa inox, bếp điện đôi, tủ lạnh mini màu kem.
· SAU LƯNG: cửa ra vào bằng gỗ nâu, mắc áo gỗ và tấm gương viền gỗ mộc.
· GIỮA PHÒNG: bàn gỗ vuông nhỏ hai ghế, trên bàn có chậu nước inox, khăn bông trắng gấp và cuộn băng gạc.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· GIƯỜNG và cửa phòng tắm luôn ở phía SCREEN LEFT; CỬA RA VÀO luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía giường thì hậu cảnh là khung giường sắt trắng và đèn bàn đang bật; quay về phía
  cửa ra vào thì hậu cảnh là cánh cửa gỗ nâu và tấm gương.
· Ánh đèn bàn vàng ấm luôn tới từ PHÍA TRÁI MÀN HÌNH; đèn trần đổ từ trên xuống chính giữa phòng.""",
  bg="REF_NHACONG_CHIEU")

D("REF_PHONGAN_DEM", "Phòng ăn dinh thự Kane — ĐÊM",
  "THẺ BỐI CẢNH — phòng ăn lớn của toà nhà chính, bữa tối mười chín người của gia tộc Kane. Dùng S8.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở đầu phòng phía cửa vòm, cách đầu bàn ăn 6m,\n"
  "nhìn dọc theo chiều dài bàn.\n\n"
  "ĐỒNG BỘ PHONG CÁCH: dùng ảnh bối cảnh đính kèm CHỈ ĐỂ LẤY MỨC ĐỘ GIÀU CÓ và vật liệu đá sáng màu kem xám của\n"
  "toà nhà chính nhà Kane. **ĐÂY LÀ MỘT KHÔNG GIAN KHÁC (PHÒNG ĂN TRONG NHÀ)** — KHÔNG copy cổng sắt, bãi cỏ hay\n"
  "căn nhà cổng gạch đỏ của ảnh gốc.\n\n"
  "KHÔNG GIAN: phòng ăn lớn của một dinh thự tân cổ điển, BAN ĐÊM. Ngoài ba cửa sổ cao là đêm đen, rèm nhung nặng\n"
  "màu rượu vang buông hai bên. Một ĐÈN CHÙM PHA LÊ lớn treo trên bàn đang bật ở mức ấm, cộng hai đèn tường mạ đồng —\n"
  "ánh sáng VÀNG ẤM, sang trọng, ĐỦ SÁNG RÕ mọi gương mặt, KHÔNG mảng đen đặc. Phòng TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: một BÀN ĂN GỖ ÓC CHÓ SẪM rất dài đánh bóng gương, phủ khăn trải bàn trắng ở giữa, kê chính giữa\n"
  "phòng, quanh bàn là HAI MƯƠI GHẾ TỰA LƯNG CAO bọc nhung xanh rêu. Trên bàn bày sẵn đĩa sứ trắng viền vàng,\n"
  "dao dĩa bạc, ly rượu pha lê, ba lọ hoa hồng trắng thấp và hai chân nến bạc — bày biện đối xứng, hoàn hảo, lạnh.\n"
  "SÁT TƯỜNG PHẢI, CẠNH CỬA BẾP, KÊ RIÊNG MỘT BÀN VUÔNG NHỎ với một ghế đơn và một bộ dao dĩa — chi tiết này\n"
  "BẮT BUỘC phải thấy rõ, đặt tách hẳn khỏi bàn lớn.\n"
  "Tường sơn trắng kem có phào chỉ thạch cao trắng; treo hai bức TRANH SƠN DẦU KHỔ LỚN chân dung người xưa\n"
  "trong khung mạ vàng. Sát tường trái là một TỦ BÀY BÁT ĐĨA bằng gỗ óc chó có mặt đá trắng.\n"
  "Sàn lát ĐÁ CẨM THẠCH TRẮNG VÂN XÁM, trải một tấm thảm Ba Tư lớn dưới bàn ăn.\n\n"
  "ĐÓNG BĂNG: phòng ăn bày sẵn và trống, đúng khoảnh khắc ngay TRƯỚC khi khách bắt đầu vào ngồi.",
  """VẬT LIỆU CHUNG CỦA TOÀ NHÀ CHÍNH NHÀ KANE:
· Dinh thự tân cổ điển Mỹ của một gia tộc rất giàu: bề thế, đối xứng, lạnh, sạch đến vô hồn.
· Tường sơn TRẮNG KEM, phào chỉ thạch cao trắng sát trần, nẹp chân tường trắng bản rộng. Trần cao 3m5.
· ĐÁ CẨM THẠCH TRẮNG VÂN XÁM cho sàn khu chính; GỖ ÓC CHÓ SẪM cho cửa, đồ nội thất và tay vịn.
· Kim loại trang trí đều là ĐỒNG MẠ VÀNG đã xỉn nhẹ. Vải bọc là NHUNG XANH RÊU và NHUNG RƯỢU VANG.
· Mọi thứ đắt, được lau bóng, bày đối xứng — KHÔNG bụi, KHÔNG bừa bộn, KHÔNG đồ cá nhân bày ra ngoài.
· KHÔNG có chữ đọc được ở bất kỳ đâu trong khung.""",
  """QUY HOẠCH KHÔNG GIAN 360° — PHÒNG ĂN (đứng ở đầu bàn phía cửa vòm, quay mặt về cuối bàn):
· ĐỐI DIỆN (cuối phòng): đầu bàn phía trong với chiếc GHẾ CHỦ TOẠ lưng cao nhất; sau nó là lò sưởi đá trắng
  có mặt gương lớn phía trên.
· BÊN PHẢI: CỬA GỖ ÓC CHÓ dẫn vào bếp phục vụ, và ngay cạnh nó là BÀN VUÔNG NHỎ MỘT GHẾ kê riêng sát tường.
· BÊN TRÁI: ba CỬA SỔ CAO có rèm nhung rượu vang, và một TỦ BÀY BÁT ĐĨA gỗ óc chó mặt đá trắng.
· SAU LƯNG: CỬA VÒM lớn không cánh dẫn ra đại sảnh và cầu thang chính.
· GIỮA PHÒNG: bàn ăn gỗ óc chó rất dài với hai mươi ghế nhung xanh rêu, trên thảm Ba Tư.
· Phòng dài khoảng 12m, ngang 7m.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· ĐẦU BÀN CHỦ TOẠ và lò sưởi luôn ở phía SCREEN LEFT; CỬA VÒM ra đại sảnh luôn ở phía SCREEN RIGHT.
· BÀN NHỎ CẠNH CỬA BẾP luôn nằm ở nửa khung phía SCREEN RIGHT, sát mép khung.
· Nền theo nhân vật: quay về phía đầu bàn chủ toạ thì hậu cảnh là lò sưởi đá trắng và tranh sơn dầu khung vàng;
  quay về phía cửa vòm thì hậu cảnh là cửa vòm, tủ bày bát đĩa và cửa bếp.
· Ánh đèn chùm luôn đổ từ TRÊN CAO CHÍNH GIỮA xuống; đèn tường mạ đồng hắt từ hai bên.""",
  bg="REF_CONGNHA_CHIEU")

D("REF_VIAHE_NGAY", "Quán cà phê vỉa hè — BAN NGÀY",
  "THẺ BỐI CẢNH — đoạn vỉa hè trước một quán cà phê, nơi Vanessa hất đổ xe lăn của Adrian. Dùng S10.",
  "MÁY QUAY: toàn cảnh, ống kính 24mm, ống kính cao 1m60, đặt ở mép lòng đường, cách mặt tiền quán 8m, nhìn dọc\n"
  "theo vỉa hè.\n\n"
  "KHÔNG GIAN: một đoạn phố thương mại Mỹ, BAN NGÀY, trời quang. Nắng cao đổ bóng ngắn và rõ; mặt tiền kính quán\n"
  "phản chiếu hàng cây đối diện. Toàn cảnh SÁNG RÕ. Khung hình TRỐNG NGƯỜI.\n\n"
  "TRONG KHUNG: vỉa hè lát BÊ TÔNG XÁM chia ô vuông, có vài vết nứt và một nắp cống gang tròn.\n"
  "Bên PHẢI là MẶT TIỀN QUÁN CÀ PHÊ: cửa kính lớn khung thép đen, MÁI HIÊN VẢI BẠT MÀU XANH RÊU căng ra vỉa hè,\n"
  "dưới hiên kê bốn BÀN TRÒN NHỎ mặt kim loại đen với tám ghế sắt uốn, trên mỗi bàn có một lọ hoa nhỏ và một\n"
  "hộp giấy ăn kim loại. Cạnh cửa quán có một BẢNG ĐEN ĐỨNG hình chữ A — mặt bảng chỉ có các nét phấn nguệch ngoạc,\n"
  "KHÔNG đọc được chữ nào.\n"
  "Ngay trước cửa quán có một DỐC XE LĂN BẰNG BÊ TÔNG hẹp nối vỉa hè xuống mặt đường, hai bên có gờ thấp —\n"
  "chi tiết này BẮT BUỘC phải thấy rõ.\n"
  "Bên TRÁI, dọc mép vỉa hè, có một CỘT ĐÈN GIAO THÔNG, hai CÂY PHONG trồng trong ô đất vuông, một thùng rác công\n"
  "cộng bằng kim loại đen và một hàng xe đỗ dọc bên đường (biển số LÀM MỜ). Phía sau là dãy nhà phố hai tầng bằng\n"
  "gạch nâu với các mặt tiền cửa hàng khác — không đọc được biển hiệu nào.\n\n"
  "ĐÓNG BĂNG: vỉa hè nắng và vắng, đúng khoảnh khắc ngay TRƯỚC khi có người rẽ vào từ đầu phố.",
  """VẬT LIỆU CHUNG (phố thương mại):
· Dãy nhà phố GẠCH NÂU hai tầng kiểu Mỹ cũ, tầng trệt là cửa hàng có mặt tiền kính khung thép đen.
· Vỉa hè BÊ TÔNG XÁM chia ô vuông, có vết nứt và nắp cống gang. Lòng đường nhựa đen có vạch kẻ trắng đã mờ.
· Mái hiên là VẢI BẠT MÀU XANH RÊU. Bàn ghế ngoài trời bằng KIM LOẠI SƠN ĐEN.
· BIỂN SỐ mọi xe LÀM MỜ; KHÔNG có biển hiệu hay logo nào đọc được.""",
  """QUY HOẠCH KHÔNG GIAN 360° — VỈA HÈ TRƯỚC QUÁN (đứng giữa vỉa hè, quay lưng về lòng đường):
· ĐỐI DIỆN: mặt tiền quán cà phê với cửa kính khung thép đen, mái hiên bạt xanh rêu, bốn bàn tròn kim loại
  và bảng đen chữ A cạnh cửa.
· BÊN PHẢI: dốc xe lăn bê tông nối vỉa hè xuống mặt đường, sau đó là mặt tiền cửa hàng kế bên.
· BÊN TRÁI: hai cây phong trong ô đất vuông, một thùng rác kim loại đen và cột đèn giao thông.
· SAU LƯNG: mép vỉa hè, hàng xe đỗ dọc đường, lòng đường và dãy nhà phố gạch nâu bên kia đường.""",
  """TRỤC (screen mapping — không bao giờ đảo):
· MẶT TIỀN QUÁN CÀ PHÊ luôn ở phía SCREEN LEFT; LÒNG ĐƯỜNG và hàng xe đỗ luôn ở phía SCREEN RIGHT.
· Nền theo nhân vật: quay về phía quán thì hậu cảnh là cửa kính, mái hiên bạt xanh và các bàn tròn; quay về phía
  đường thì hậu cảnh là hàng xe đỗ, cây phong và dãy nhà phố bên kia đường.
· Nắng luôn tới từ TRÊN CAO CHẾCH TRÁI MÀN HÌNH, bóng đổ ngắn về bên phải.""")
