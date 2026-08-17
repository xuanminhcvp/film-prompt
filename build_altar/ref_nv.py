# -*- coding: utf-8 -*-
"""REF nhân vật — chân dung + toàn thân theo trạng thái trang phục."""
from lib import ref, P_HEAD, F_HEAD, F_HEAD_NGOI

R = []
P = lambda rid, label, desc, body, status="proposed": R.append(
    ref(rid, label, desc, P_HEAD + body, status=status))
F = lambda rid, label, desc, body, port, head=F_HEAD: R.append(
    ref(rid, label, desc, head + body, chars=[port]))

XELAN_DIEN = ("CHIẾC XE LĂN: xe lăn ĐIỆN cao cấp màu đen nhám, khung nhôm liền khối, hai bánh sau đặc bản rộng, "
              "tựa lưng cao có đệm, cần điều khiển nhỏ ở tay vịn PHẢI, để chân bằng thép gập. Xe sạch, còn mới.")
XELAN_TAY = ("CHIẾC XE LĂN: xe lăn TAY kiểu bệnh viện đời cũ, khung thép sơn xám đã tróc và gỉ lấm tấm, "
             "đệm ngồi vải đen sờn, VÀNH BÁNH TRÁI CONG NHẸ nên xe hơi nghiêng, tay vịn bọc nhựa nứt. Cũ và nặng.")

# ══════════════════ 4 CHÂN DUNG USER ĐÃ CHỐT ══════════════════
P("REF_MAYA_PORTRAIT", "★ MAYA BENNETT (đã chốt — ảnh user dán)",
  "NỮ CHÍNH · 27 tuổi, Mỹ gốc Phi, điều dưỡng hồi sức tích cực ở St. Agnes. Bị bỏ ở bàn thờ Chúa, "
  "ký hợp đồng làm vợ 12 tháng để cứu mẹ. Dùng: toàn phim. "
  "Mặt phải đọc ra: bình tĩnh, tử tế, có gan — KHÔNG khốn khổ, KHÔNG cam chịu.\n"
  "⛔ ẢNH NÀY USER TỰ DÁN VÀO, LÀ BẢN CHUẨN TUYỆT ĐỐI. Không render lại, không nâng cấp.",
  "Người phụ nữ Mỹ gốc Phi 27 tuổi. Da nâu vừa, mịn, ấm. Gương mặt trái xoan nhỏ nhắn, gò má cao, cằm thon.\n"
  "Mắt to hình hạnh nhân màu nâu sẫm, hàng mi dày, chân mày nâu được tỉa gọn dáng cong mềm.\n"
  "Mũi nhỏ, sống mũi thẳng. Môi đầy, tô son hồng nhạt. Trang điểm rất nhẹ, da còn thấy kết cấu thật.\n"
  "Tóc đen xoăn xoăn tự nhiên, búi cao lộn xộn trên đỉnh đầu, vài lọn xoăn buông xuống thái dương.\n"
  "Đeo một đôi khuyên tai nhỏ đính đá lấp lánh sát dái tai. Vai trần để lộ đường cổ dài.\n"
  "Ánh nhìn ĐIỀM TĨNH VÀ ẤM, hơi ngước nhẹ, không phòng thủ.\n"
  "TUYỆT ĐỐI KHÔNG làm hốc hác, không quầng thâm.", status="approved")

P("REF_ADRIAN_PORTRAIT", "★ ADRIAN KANE (đã chốt — ảnh user dán)",
  "NAM CHÍNH · 34 tuổi, Mỹ gốc Phi, chủ sở hữu Kane Holdings. Bị cắt dây phanh, gãy cột sống, "
  "ngồi xe lăn sáu tháng và để cả họ tin mình đã hỏng. Dùng: toàn phim trừ S3 · S5 · S12 · S17 · S18. "
  "Mặt phải đọc ra: điềm tĩnh tuyệt đối, đo người khác bằng mắt — KHÔNG hằn học, KHÔNG bi luỵ.\n"
  "⛔ ẢNH NÀY USER TỰ DÁN VÀO, LÀ BẢN CHUẨN TUYỆT ĐỐI. Không render lại, không nâng cấp.",
  "Người đàn ông Mỹ gốc Phi 34 tuổi. Da nâu sẫm, khoẻ, có kết cấu thật.\n"
  "Gương mặt vuông vức, xương gò má cao và rõ, quai hàm bạnh chắc, cằm vuông.\n"
  "Tóc đen cắt cực ngắn ôm sát đầu kiểu fade, đường chân tóc trước trán được tỉa thẳng sắc nét.\n"
  "Râu quai nón đen tỉa gọn ôm quai hàm nối liền ria mép, độ dài đều.\n"
  "Mắt nâu sẫm, mí trên hơi nặng, chân mày rậm thẳng. Mũi bản rộng vừa. Môi đầy, khép tự nhiên.\n"
  "Vai rộng, cổ dày. Mặc áo thun cotton đen cổ tròn.\n"
  "Ánh nhìn TĨNH VÀ ĐO ĐẠC — người đang nghe nhiều hơn nói. KHÔNG gườm, KHÔNG đe doạ, KHÔNG cười.",
  status="approved")

P("REF_VANESSA_PORTRAIT", "★ VANESSA HALE (đã chốt — ảnh user dán)",
  "PHẢN DIỆN NỮ · 28 tuổi, da trắng, con gái Gerald Hale của Hale Group. Cướp chú rể, ném tiền vào mặt Maya, "
  "gài vòng cổ vu trộm. Dùng: S1 · S10 · S21 · S22 · S23 · S24. "
  "Mặt phải đọc ra: đẹp, lạnh, quen được phục vụ — KHÔNG dữ tướng, cái ác nằm ở lời thoại.\n"
  "⛔ ẢNH NÀY USER TỰ DÁN VÀO, LÀ BẢN CHUẨN TUYỆT ĐỐI. Không render lại, không nâng cấp.",
  "Người phụ nữ da trắng 28 tuổi. Da sáng mịn, hơi ửng hồng ở gò má.\n"
  "Gương mặt trái xoan cân đối, gò má cao, quai hàm thon rõ nét, cằm nhọn vừa.\n"
  "Mắt to màu XANH XÁM, mi mắt được kẻ eyeliner mảnh và mi giả mỏng, chân mày nâu tỉa gọn hơi cong.\n"
  "Mũi thẳng nhỏ, môi đầy tô son hồng nude bóng. Trang điểm hoàn hảo kiểu tiệm chuyên nghiệp.\n"
  "Tóc vàng bạch kim DÀI THẲNG mượt, rẽ ngôi giữa, buông qua vai xuống quá ngực.\n"
  "Đeo một đôi khuyên tai kim cương tấm nhỏ sát dái tai. Cổ cao, vai trần.\n"
  "Ánh nhìn TỰ TIN VÀ HƠI BỀ TRÊN, khoé môi giữ nét cười xã giao rất nhạt.", status="approved")

P("REF_RYAN_PORTRAIT", "★ RYAN PRESCOTT (đã chốt — ảnh user dán)",
  "PHẢN DIỆN NAM · 31 tuổi, da trắng, giám đốc kinh doanh. Bỏ Maya ngay tại bàn thờ Chúa để cưới con gái tài phiệt. "
  "Dùng: S1 · S12 · S20 · S21 · S22 · S23 · S24. "
  "Mặt phải đọc ra: đẹp trai kiểu bán hàng, tự tin rỗng — KHÔNG hung dữ.\n"
  "⛔ ẢNH NÀY USER TỰ DÁN VÀO, LÀ BẢN CHUẨN TUYỆT ĐỐI. Không render lại, không nâng cấp.",
  "Người đàn ông da trắng 31 tuổi. Da sáng, hơi rám nắng nhẹ, có kết cấu thật.\n"
  "Gương mặt dài cân đối, gò má rõ, quai hàm thẳng và sắc, cằm vuông vừa.\n"
  "Tóc NÂU SẪM dày, hơi gợn sóng, chải hất ngược ra sau và sang một bên gọn gàng kiểu tiệm.\n"
  "Mắt màu NÂU HẠT DẺ, chân mày nâu rậm thẳng. Mũi cao thẳng. Môi mỏng vừa, khép tự nhiên.\n"
  "Cằm và quai hàm có lún phún râu mới cạo rất ngắn. Cổ và vai chắc.\n"
  "Mặc áo sơ mi trắng cài kín cúc trên cùng.\n"
  "Ánh nhìn THẲNG VÀ TỰ TIN, hơi phẳng lặng — người quen được nhìn. KHÔNG cười, KHÔNG gườm.",
  status="approved")

# ══════════════════ CHÂN DUNG NHÂN VẬT PHỤ ══════════════════
P("REF_HELEN_PORTRAIT", "HELEN BENNETT — mẹ Maya",
  "MẸ NỮ CHÍNH · 56 tuổi, Mỹ gốc Phi, hôn mê ở giường 12 khoa hồi sức suốt phim, tỉnh lại ở S25. "
  "Dùng: S9 · S25. Mặt phải đọc ra: từng là người phụ nữ mạnh mẽ, nay yếu vì bệnh dài ngày.",
  "Người phụ nữ Mỹ gốc Phi 56 tuổi, ốm nặng dài ngày. Da nâu vừa, cùng tông với con gái, nhợt đi vì thiếu nắng.\n"
  "Gương mặt trái xoan gầy, gò má cao nổi rõ, hai má hóp nhẹ. Nếp nhăn thật ở khoé mắt và hai bên miệng.\n"
  "Mắt nâu sẫm, mí trên hơi sụp, ánh nhìn mệt và hiền. Môi khô nhạt màu.\n"
  "Tóc xoăn tự nhiên đã bạc quá nửa, cắt ngắn sát đầu, gọn.\n"
  "Không trang điểm, không trang sức. Mặc áo bệnh nhân màu xanh nhạt cài sau gáy.\n"
  "TUYỆT ĐỐI KHÔNG vẽ ống thở hay thiết bị y tế trong ảnh chân dung này.")

P("REF_SEBASTIAN_PORTRAIT", "SEBASTIAN — trợ lý của Adrian",
  "TRỢ LÝ · 52 tuổi, Mỹ gốc Phi, luật sư riêng kiêm người tin cẩn duy nhất của Adrian. "
  "Dùng: S1 · S6 · S12 · S13 · S22 · S23. Mặt phải đọc ra: kín, chuyên nghiệp, tuyệt đối trung thành.",
  "Người đàn ông Mỹ gốc Phi 52 tuổi. Da nâu sẫm, cạo nhẵn, có kết cấu thật.\n"
  "Gương mặt dài, gò má cao, quai hàm rõ. Nếp nhăn ngang trán và rãnh hai bên miệng.\n"
  "Đầu cạo trọc bóng, râu cằm bạc muối tiêu tỉa cực gọn thành một vệt mỏng quanh miệng.\n"
  "Mắt nâu sẫm, sắc và tỉnh, chân mày muối tiêu. Mũi thẳng. Môi mỏng khép.\n"
  "Đeo kính gọng kim loại mảnh màu bạc, tròng chữ nhật.\n"
  "Mặc sơ mi trắng cổ cứng, cà vạt xám than thắt chuẩn, vest đen.\n"
  "Ánh nhìn ĐIỀM ĐẠM VÀ CHÚ Ý, không biểu lộ.")

P("REF_JULIAN_PORTRAIT", "JULIAN KANE — anh họ Adrian",
  "PHẢN DIỆN CHÍNH · 41 tuổi, Mỹ gốc Phi, quyền chủ tịch gia tộc Kane, người thuê cắt dây phanh. "
  "Dùng: S8 · S14 · S16 · S20 · S21 · S22 · S23. Mặt phải đọc ra: lịch thiệp, mượt mà, cái ác được đánh bóng.",
  "Người đàn ông Mỹ gốc Phi 41 tuổi. Da nâu sẫm, được chăm kỹ, có kết cấu thật.\n"
  "Gương mặt vuông, gò má cao, quai hàm rõ — có nét họ hàng với Adrian nhưng KHÔNG giống hệt:\n"
  "mặt gầy hơn, cằm nhọn hơn, mũi hẹp hơn.\n"
  "Tóc đen cắt ngắn chải chuốt bóng, thái dương hớt cao, có vài sợi bạc ở mai.\n"
  "Ria mép đen tỉa mỏng sắc nét, cằm cạo nhẵn.\n"
  "Mắt nâu sẫm, hơi hẹp, chân mày rậm. Môi mỏng, khoé môi hơi nhếch lên thành nét cười xã giao thường trực.\n"
  "Mặc sơ mi xanh navy cổ cứng cài kín.\n"
  "Ánh nhìn LỊCH SỰ VÀ LẠNH, kiểu người luôn đang tính giá của mọi thứ.")

P("REF_PRIEST_PORTRAIT", "PRIEST — linh mục nhà thờ St. Michael",
  "VAI PHỤ · 64 tuổi, da trắng, chủ hôn ở cả hai đám cưới trong nhà thờ. "
  "Dùng: S1. Mặt phải đọc ra: hiền, mệt, bối rối trước chuyện đang xảy ra trong nhà Chúa.",
  "Người đàn ông da trắng 64 tuổi. Da sáng, nhiều nếp nhăn thật ở trán và khoé mắt, má hơi chảy.\n"
  "Gương mặt tròn phúc hậu, mũi to bản, môi dày.\n"
  "Tóc bạc trắng thưa, chải ngược, hói nhẹ ở đỉnh. Không râu.\n"
  "Mắt xanh xám nhạt sau cặp kính gọng vàng nhỏ hình bầu dục.\n"
  "Mặc áo chùng linh mục màu đen cổ cồn trắng, ngoài khoác dây stola màu trắng thêu chỉ vàng.\n"
  "Ánh nhìn HIỀN VÀ LO, không phán xét.")

P("REF_PRESCOTT_PORTRAIT", "MRS. PRESCOTT — mẹ Ryan",
  "VAI PHỤ · 59 tuổi, da trắng, mẹ Ryan, từ chối cho Maya vay tiền ở bãi xe. "
  "Dùng: S2. Mặt phải đọc ra: sang trọng, khinh người một cách rất lịch sự.",
  "Người phụ nữ da trắng 59 tuổi. Da sáng được chăm kỹ, nếp nhăn thật ở khoé mắt và cổ.\n"
  "Gương mặt gầy, gò má cao, quai hàm thon, môi mỏng tô son đỏ trầm.\n"
  "Tóc vàng tro nhuộm, cắt bob ngang cằm, sấy phồng chuẩn tiệm, không một sợi lệch.\n"
  "Mắt xanh nhạt, mí trên hơi sụp, chân mày kẻ mảnh. Mũi thẳng hẹp.\n"
  "Đeo khuyên tai ngọc trai tròn và một chuỗi ngọc trai một vòng ở cổ.\n"
  "Mặc áo khoác vải tweed màu kem cài cúc vàng.\n"
  "Ánh nhìn LẠNH VÀ TỪ TRÊN XUỐNG, mặt không động.")

P("REF_CLERKBILL_PORTRAIT", "BILLING CLERK — nhân viên thu ngân viện phí",
  "VAI PHỤ · 46 tuổi, da trắng, người gọi báo cắt máy thở và sau đó báo hoá đơn bằng không. "
  "Dùng: S2 (chỉ giọng qua điện thoại) · S5. Mặt phải đọc ra: mệt, thương người nhưng bất lực trước con số.",
  "Người phụ nữ da trắng 46 tuổi, hơi đầy đặn. Da sáng, có tàn nhang mờ ở gò má, quầng mắt nhẹ vì ca sớm.\n"
  "Gương mặt tròn, má đầy, cằm mềm. Mũi nhỏ hếch. Môi vừa, son dưỡng nhạt.\n"
  "Tóc nâu sẫm buộc đuôi ngựa thấp, vài sợi loà xoà ở thái dương.\n"
  "Mắt nâu, hiền, có nếp nhăn cười ở đuôi mắt. Đeo kính gọng nhựa đen bản to.\n"
  "Mặc áo blouse polyester màu xanh nhạt của nhân viên hành chính bệnh viện, cài kín.\n"
  "Ánh nhìn MỆT VÀ ÁI NGẠI.")

P("REF_PAWN_PORTRAIT", "PAWN BROKER — chủ tiệm cầm đồ",
  "VAI PHỤ · 57 tuổi, da trắng, người định giá chiếc nhẫn cưới của mẹ Maya. "
  "Dùng: S3. Mặt phải đọc ra: chai sạn nghề nghiệp, không ác, chỉ là đã thấy quá nhiều.",
  "Người đàn ông da trắng 57 tuổi, thấp đậm. Da sạm, lỗ chân lông rõ, nếp nhăn sâu ở trán.\n"
  "Gương mặt vuông thô, mũi to bè, môi dày, cằm có ngấn.\n"
  "Tóc xám thưa cắt ngắn, hói cao hai bên trán. Râu cằm xám lởm chởm hai ngày chưa cạo.\n"
  "Mắt nâu nhỏ, mí dày, ánh nhìn phẳng và thực dụng.\n"
  "Đeo kính lúp thợ kim hoàn đẩy lên trán. Mặc áo sơ mi kẻ ca rô xám xanh xắn tay tới khuỷu.\n"
  "Ánh nhìn BÌNH THẢN, không thương hại cũng không khinh.")

P("REF_LOAN_PORTRAIT", "LOAN OFFICER — nhân viên tín dụng ngân hàng",
  "VAI PHỤ · 38 tuổi, da trắng, người từ chối hồ sơ vay lần thứ ba của Maya. "
  "Dùng: S3. Mặt phải đọc ra: lịch sự, quy trình, không mảy may lay động.",
  "Người đàn ông da trắng 38 tuổi. Da sáng sạch, mặt gầy dài, gò má phẳng, cằm hẹp.\n"
  "Tóc nâu nhạt cắt ngắn rẽ ngôi lệch, vuốt gel gọn.\n"
  "Mắt xám xanh, chân mày nhạt, mũi thẳng dài, môi mỏng.\n"
  "Đeo kính gọng nhựa trong suốt, tròng vuông.\n"
  "Mặc sơ mi trắng cài kín, cà vạt xanh navy trơn thắt chặt.\n"
  "Ánh nhìn LỊCH SỰ VÀ TRỐNG, kiểu người đọc màn hình nhiều hơn đọc mặt người.")

P("REF_CLERK_PORTRAIT", "CLERK — cán bộ hộ tịch toà thị chính",
  "VAI PHỤ · 51 tuổi, da đen, người làm thủ tục đăng ký kết hôn cho Maya và Adrian. "
  "Dùng: S6. Mặt phải đọc ra: nhanh, gọn, đã làm việc này mười nghìn lần.",
  "Người phụ nữ Mỹ gốc Phi 51 tuổi. Da nâu sẫm, mặt tròn đầy, gò má cao, cằm mềm.\n"
  "Tóc đen tết cornrow sát da đầu rồi búi gọn sau gáy, chân tóc có vài sợi bạc.\n"
  "Mắt nâu sẫm, ánh nhìn nhanh và thực tế. Chân mày tỉa gọn. Môi đầy tô son nâu đất.\n"
  "Đeo kính đọc gọng đỏ mảnh trễ xuống sống mũi và một đôi khuyên tai vàng tròn nhỏ.\n"
  "Mặc áo blazer xanh navy ngoài sơ mi trắng, bên ngực trái có kẹp thẻ nhân viên úp mặt (không đọc được chữ).\n"
  "Ánh nhìn NHANH NHẸN VÀ TRUNG TÍNH.")

P("REF_MARGARET_PORTRAIT", "AUNT MARGARET — bà cô họ Kane",
  "VAI PHỤ · 66 tuổi, Mỹ gốc Phi, bà cô trong bữa tối gia tộc, người duy nhất lên tiếng nhẹ. "
  "Dùng: S8. Mặt phải đọc ra: quý phái, biết chuyện sai nhưng không dám cãi Julian.",
  "Người phụ nữ Mỹ gốc Phi 66 tuổi. Da nâu vừa, được chăm kỹ, nếp nhăn thật ở khoé mắt và cổ.\n"
  "Gương mặt tròn, gò má cao, cằm mềm, môi đầy tô son đỏ trầm.\n"
  "Tóc bạc xám uốn phồng ngắn ôm đầu kiểu quý bà, chải rất gọn.\n"
  "Mắt nâu sẫm, mí trên hơi chùng, ánh nhìn lo lắng và mềm.\n"
  "Đeo khuyên tai ngọc trai giọt nước và một chuỗi ngọc trai ở cổ.\n"
  "Mặc áo lụa màu tím nhạt cổ tròn, ngoài khoác một chiếc áo len mỏng màu kem.\n"
  "Ánh nhìn ÁI NGẠI VÀ NHÚN NHƯỜNG.")

P("REF_PETER_PORTRAIT", "UNCLE PETER — ông chú họ Kane",
  "VAI PHỤ · 63 tuổi, Mỹ gốc Phi, người hỏi thẳng Maya được trả bao nhiêu. "
  "Dùng: S8. Mặt phải đọc ra: hợm hĩnh, thích trò đùa ác trên bàn ăn.",
  "Người đàn ông Mỹ gốc Phi 63 tuổi, bụng đầy. Da nâu sẫm, mặt vuông to bản, má chảy.\n"
  "Tóc đen bạc muối tiêu cắt ngắn, chân tóc lùi cao. Ria mép rậm muối tiêu.\n"
  "Mắt nâu sẫm nhỏ, mí dày, ánh nhìn giễu cợt. Mũi to bè. Môi dày, khoé môi kéo ngang.\n"
  "Mặc sơ mi hồng nhạt cài kín, cà vạt lụa vân màu rượu vang, ngoài là vest xám than.\n"
  "Ánh nhìn CHẾ GIỄU MỘT CÁCH DỄ CHỊU, không hung dữ.")

P("REF_DIANE_PORTRAIT", "NURSE DIANE — bạn cùng ca của Maya",
  "VAI PHỤ · 44 tuổi, da trắng, điều dưỡng ICU, người duy nhất ở bệnh viện đứng về phía Maya. "
  "Dùng: S9 · S18 · S25. Mặt phải đọc ra: ấm, thẳng thắn, mệt vì ca đêm.",
  "Người phụ nữ da trắng 44 tuổi. Da sáng có tàn nhang, quầng mắt nhẹ, không trang điểm.\n"
  "Gương mặt bầu, gò má đầy, mũi nhỏ, môi vừa nứt nhẹ vì thiếu nước.\n"
  "Tóc đỏ nâu buộc búi thấp gọn, vài sợi loà xoà.\n"
  "Mắt xanh lá xám, ánh nhìn thẳng và ấm, có nếp nhăn cười ở đuôi mắt.\n"
  "Mặc áo scrub y tá màu xanh mòng két, cổ chữ V, túi ngực có một cây bút bi.\n"
  "Ánh nhìn TỬ TẾ VÀ MỆT.")

P("REF_PAULA_PORTRAIT", "NURSE PAULA — điều dưỡng nói xấu sau lưng",
  "VAI PHỤ · 33 tuổi, da trắng, người bàn tán chuyện Maya bán mình lấy hai trăm nghìn. "
  "Dùng: S9. Mặt phải đọc ra: tò mò, hớt hải, không tự thấy mình đang ác.",
  "Người phụ nữ da trắng 33 tuổi. Da sáng, trang điểm nhẹ, má hồng.\n"
  "Gương mặt trái xoan, cằm nhọn, mũi nhỏ hếch, môi mỏng tô son hồng.\n"
  "Tóc nâu vàng nhuộm highlight, buộc đuôi ngựa cao bóng mượt.\n"
  "Mắt nâu sáng, mi được chuốt kỹ, chân mày kẻ đậm.\n"
  "Mặc áo scrub y tá màu tím hoa cà, cổ chữ V.\n"
  "Ánh nhìn TÒ MÒ VÀ HÁO HỨC, hơi nghiêng đầu.")

P("REF_HALLORAN_PORTRAIT", "MR. HALLORAN — tổng giám đốc sàn 40",
  "VAI PHỤ · 56 tuổi, da trắng, sếp của Ryan, người bị Sebastian ép sa thải Ryan trong hai mươi phút. "
  "Dùng: S12. Mặt phải đọc ra: quyền lực vừa đủ, đang sợ một thứ lớn hơn mình.",
  "Người đàn ông da trắng 56 tuổi, đậm người. Da sáng ửng đỏ ở gò má và cổ, có mồ hôi rịn ở thái dương.\n"
  "Gương mặt vuông to, cằm có ngấn, mũi to bản có mạch máu li ti.\n"
  "Tóc bạc muối tiêu chải ngược gọn, hói nhẹ hai bên trán.\n"
  "Mắt xanh xám, mí dưới hơi húp, ánh nhìn căng thẳng.\n"
  "Mặc sơ mi trắng cổ cứng, cà vạt lụa xanh navy nới lỏng một nấc, tay áo cài khuy măng sét.\n"
  "Ánh nhìn LO LẮNG VÀ GẮNG GIỮ VẺ ĐIỀM TĨNH.")

P("REF_BOARD1_PORTRAIT", "BOARD MEMBER ONE — thành viên hội đồng",
  "VAI PHỤ · 49 tuổi, da trắng, người báo cáo mười tám màn hình đã trực tuyến. "
  "Dùng: S13. Mặt phải đọc ra: kỷ luật, chờ lệnh.",
  "Người đàn ông da trắng 49 tuổi. Da sáng, mặt gầy góc cạnh, gò má cao, cằm vuông.\n"
  "Tóc nâu sẫm cắt ngắn gọn, hai bên tỉa cao, có sợi bạc ở mai.\n"
  "Mắt nâu, chân mày thẳng, mũi cao, môi mỏng.\n"
  "Mặc sơ mi trắng, cà vạt xám bạc, vest xanh than.\n"
  "Ánh nhìn TẬP TRUNG VÀ TRUNG THÀNH.")

P("REF_BOARD2_PORTRAIT", "BOARD MEMBER TWO — thành viên hội đồng",
  "VAI PHỤ · 45 tuổi, da đen, người đọc số dư hạn mức bốn trăm triệu của Hale Group. "
  "Dùng: S13. Mặt phải đọc ra: sắc sảo, thuộc số liệu.",
  "Người phụ nữ Mỹ gốc Phi 45 tuổi. Da nâu sẫm mịn, gương mặt trái xoan, gò má cao, cằm thon.\n"
  "Tóc đen duỗi thẳng cắt bob ngang cằm, rẽ ngôi lệch, rất gọn.\n"
  "Mắt nâu sẫm sắc, chân mày tỉa gọn, môi tô son nâu trầm.\n"
  "Đeo một đôi khuyên tai vàng bản dẹt nhỏ.\n"
  "Mặc áo blazer đen ngoài sơ mi lụa trắng cài kín.\n"
  "Ánh nhìn SẮC VÀ ĐIỀM TĨNH.")

P("REF_WHITMORE_PORTRAIT", "JUDGE WHITMORE — thẩm phán",
  "VAI PHỤ · 61 tuổi, da đen, thẩm phán bác đơn giám hộ của Julian. "
  "Dùng: S14. Mặt phải đọc ra: uy nghiêm, công bằng, nghe kỹ.",
  "Người phụ nữ Mỹ gốc Phi 61 tuổi. Da nâu sẫm, gương mặt vuông đầy đặn, gò má cao, quai hàm rõ.\n"
  "Tóc xoăn bạc xám cắt ngắn ôm đầu, gọn gàng.\n"
  "Mắt nâu sẫm, ánh nhìn thẳng và bình tĩnh, mí trên hơi nặng.\n"
  "Đeo kính đọc gọng kim loại mảnh trễ xuống sống mũi. Khuyên tai vàng tròn nhỏ.\n"
  "Mặc áo choàng thẩm phán màu ĐEN, cổ áo sơ mi trắng lộ ra ở trong.\n"
  "Ánh nhìn UY NGHIÊM VÀ ĐIỀM ĐẠM.")

P("REF_LAWYER_PORTRAIT", "JULIAN'S LAWYER — luật sư của Julian",
  "VAI PHỤ · 50 tuổi, da trắng, luật sư trình bày đơn xin giám hộ. "
  "Dùng: S14. Mặt phải đọc ra: trơn tru, nhà nghề, không tin điều mình đang nói.",
  "Người đàn ông da trắng 50 tuổi. Da sáng, mặt dài, gò má phẳng, cằm hẹp, môi mỏng.\n"
  "Tóc đen nhuộm chải bóng ngược ra sau, thái dương bạc.\n"
  "Mắt nâu nhỏ sau kính gọng đồi mồi tròn nhỏ. Mũi dài thẳng.\n"
  "Mặc sơ mi trắng, cà vạt lụa xanh rêu, vest xám sọc mảnh, khăn túi ngực trắng.\n"
  "Ánh nhìn TRƠN TRU VÀ NGHỀ NGHIỆP.")

P("REF_DEPUTY_PORTRAIT", "SHERIFF'S DEPUTY — phó cảnh sát trưởng",
  "VAI PHỤ · 36 tuổi, da trắng, người tống đạt lệnh trục xuất bốn tiếng. "
  "Dùng: S16. Mặt phải đọc ra: chỉ đang làm việc, hơi ngại.",
  "Người đàn ông da trắng 36 tuổi, vai rộng. Da sáng rám nắng, mặt vuông, quai hàm bạnh, cằm chẻ nhẹ.\n"
  "Tóc vàng sẫm cắt cua ngắn. Cạo nhẵn.\n"
  "Mắt xanh xám, chân mày nhạt, ánh nhìn ngại ngùng.\n"
  "Mặc đồng phục cảnh sát hạt màu XANH RÊU SẪM, cổ áo có phù hiệu kim loại nhỏ (không đọc được chữ),\n"
  "dây đeo vai bằng da đen, bảng tên úp mặt.\n"
  "Ánh nhìn NGHIÊM TÚC NHƯNG KHÔNG ĐE DOẠ.")

P("REF_HR_PORTRAIT", "HR DIRECTOR — giám đốc nhân sự bệnh viện",
  "VAI PHỤ · 53 tuổi, da đen, người buộc phải đình chỉ Maya sau khi Gerald Hale tài trợ bệnh viện. "
  "Dùng: S18. Mặt phải đọc ra: xấu hổ, biết mình đang làm điều sai.",
  "Người phụ nữ Mỹ gốc Phi 53 tuổi. Da nâu vừa, gương mặt tròn, gò má đầy, cằm mềm.\n"
  "Tóc đen duỗi thẳng búi thấp sau gáy, chân tóc có sợi bạc.\n"
  "Mắt nâu sẫm, mí trên hơi chùng, ánh nhìn né tránh. Môi đầy tô son nâu nhạt.\n"
  "Đeo kính gọng vàng mảnh và một sợi dây chuyền vàng bản nhỏ.\n"
  "Mặc áo blazer xám ngoài sơ mi trắng cài kín.\n"
  "Ánh nhìn ÁY NÁY VÀ NÉ TRÁNH.")

P("REF_THUG1_PORTRAIT", "THUG ONE — kẻ đánh thuê thứ nhất",
  "VAI PHỤ · 38 tuổi, da trắng, kẻ cầm đầu ba người chặn Maya và Adrian ở hầm xe. "
  "Dùng: S19. Mặt phải đọc ra: lạnh, làm thuê, không giận dữ.",
  "Người đàn ông da trắng 38 tuổi, vai rộng, cổ dày. Da sạm, có sẹo mờ ở chân mày trái.\n"
  "Gương mặt vuông thô, mũi từng gãy hơi lệch, quai hàm bạnh.\n"
  "Tóc đen cắt cực ngắn. Râu cằm đen lởm chởm ba ngày.\n"
  "Mắt nâu sẫm, mí nặng, ánh nhìn phẳng và trống.\n"
  "Mặc áo khoác bomber vải dù màu đen kéo khoá tới ngực, bên trong là áo thun xám.\n"
  "Ánh nhìn TRỐNG VÀ NGHỀ NGHIỆP, không hằn học.")

P("REF_THUG2_PORTRAIT", "THUG TWO — kẻ đánh thuê thứ hai",
  "VAI PHỤ · 32 tuổi, da trắng, kẻ nhắn lại lời của gia đình. "
  "Dùng: S19. Mặt phải đọc ra: hờ hững, coi việc này là công việc.",
  "Người đàn ông da trắng 32 tuổi, cao gầy rắn. Da sáng tái, gò má cao nhô, má hóp.\n"
  "Tóc nâu nhạt buộc túm nhỏ sau gáy, hai bên cạo sát.\n"
  "Mắt xanh nhạt, chân mày nhạt, ánh nhìn hờ hững. Mũi hẹp dài. Môi mỏng.\n"
  "Mặc áo hoodie xám than kéo khoá kín, mũ trùm hạ xuống vai.\n"
  "Ánh nhìn HỜ HỮNG VÀ XA CÁCH.")

P("REF_PLANNER_PORTRAIT", "WEDDING PLANNER — người điều phối đám cưới",
  "VAI PHỤ · 35 tuổi, da trắng, người xếp Maya đứng ở cửa phục vụ, ngoài tầm máy quay. "
  "Dùng: S20. Mặt phải đọc ra: gấp gáp, coi người như một dòng trong bảng phân công.",
  "Người phụ nữ da trắng 35 tuổi. Da sáng, trang điểm nhẹ chuyên nghiệp, gương mặt góc cạnh.\n"
  "Tóc nâu sẫm cắt bob ngắn ép thẳng, rẽ ngôi giữa.\n"
  "Mắt nâu sắc, chân mày kẻ đậm gọn, môi tô son đỏ gạch.\n"
  "Đeo tai nghe headset mảnh có micro nhỏ trước miệng.\n"
  "Mặc bộ vest đen ôm, sơ mi đen bên trong, trên tay cầm bìa kẹp hồ sơ (không đọc được chữ).\n"
  "Ánh nhìn GẤP GÁP VÀ HIỆU QUẢ.")

P("REF_GRANDMA_PORTRAIT", "GRANDMOTHER HALE — bà nội Vanessa",
  "VAI PHỤ · 89 tuổi, da trắng, suy tim, người duy nhất bên nhà Hale nói đỡ cho Maya. "
  "Dùng: S20 · S21. Mặt phải đọc ra: yếu về thân thể nhưng đầu óc sắc, còn biết xấu hổ.",
  "Người phụ nữ da trắng 89 tuổi. Da rất mỏng, trắng, nhiều đồi mồi và nếp nhăn sâu, gò má nhô.\n"
  "Gương mặt gầy, cằm nhỏ, môi mỏng nhạt màu.\n"
  "Tóc bạc trắng mỏng, uốn phồng nhẹ ôm đầu, chải gọn.\n"
  "Mắt xanh nhạt, mí trên sụp nhiều, ánh nhìn vẫn tỉnh và sắc.\n"
  "Đeo khuyên tai ngọc trai nhỏ và một chuỗi ngọc trai ngắn.\n"
  "Mặc áo lụa màu xanh phấn cổ tròn cài kín, ngoài khoác áo len mỏng màu ngà.\n"
  "Ánh nhìn TỈNH TÁO VÀ NGHIÊM.")

P("REF_GERALD_PORTRAIT", "GERALD HALE — bố Vanessa",
  "PHẢN DIỆN · 62 tuổi, da trắng, chủ Hale Group, người đá đổ xe lăn của Adrian giữa nhà thờ. "
  "Dùng: S20 · S21 · S22 · S23 · S24. Mặt phải đọc ra: quyền lực cũ, quen ra lệnh, không quen bị từ chối.",
  "Người đàn ông da trắng 62 tuổi, cao lớn, bụng vừa. Da sáng rám nắng sân golf, nếp nhăn sâu ở trán.\n"
  "Gương mặt to bản, quai hàm nặng, cằm vuông, mũi to thẳng.\n"
  "Tóc bạc trắng dày chải ngược ra sau. Cạo nhẵn.\n"
  "Mắt xanh xám, chân mày bạc rậm, ánh nhìn nặng và áp đảo.\n"
  "Mặc sơ mi trắng cổ cứng và nơ đen thắt sẵn.\n"
  "Ánh nhìn UY QUYỀN VÀ KHÔNG KIÊN NHẪN.")

P("REF_SECURITY_PORTRAIT", "SECURITY CHIEF — trưởng an ninh tiệc cưới",
  "VAI PHỤ · 47 tuổi, da đen, người khám túi Maya và tìm thấy vòng cổ. "
  "Dùng: S21 · S22. Mặt phải đọc ra: kỷ luật, làm đúng quy trình, không thù ghét.",
  "Người đàn ông Mỹ gốc Phi 47 tuổi, vai rất rộng. Da nâu sẫm, đầu cạo trọc, quai hàm vuông.\n"
  "Mắt nâu sẫm, chân mày rậm, ánh nhìn tỉnh và quét ngang.\n"
  "Râu cằm đen tỉa cực ngắn. Có tai nghe xoắn dây trong suốt gài ở tai phải.\n"
  "Mặc vest đen bó, sơ mi trắng, cà vạt đen bản nhỏ.\n"
  "Ánh nhìn KỶ LUẬT VÀ TRUNG TÍNH.")

P("REF_OFFICER_PORTRAIT", "POLICE OFFICER — cảnh sát bắt Vanessa",
  "VAI PHỤ · 31 tuổi, da đen, người còng tay Vanessa giữa tiệc cưới. "
  "Dùng: S23. Mặt phải đọc ra: điềm tĩnh, đúng quy trình.",
  "Người phụ nữ Mỹ gốc Phi 31 tuổi. Da nâu sẫm, gương mặt trái xoan, gò má cao, quai hàm gọn.\n"
  "Tóc đen tết sát da đầu rồi búi chặt sau gáy.\n"
  "Mắt nâu sẫm, ánh nhìn thẳng, không biểu lộ. Môi khép.\n"
  "Mặc đồng phục cảnh sát màu XANH ĐEN, cổ áo có phù hiệu kim loại nhỏ (không đọc được chữ),\n"
  "áo gilê chống đạn mỏng bên ngoài, bộ đàm gài vai trái.\n"
  "Ánh nhìn ĐIỀM TĨNH VÀ NGHIỆP VỤ.")

P("REF_MOORE_PORTRAIT", "DETECTIVE MOORE — điều tra viên",
  "VAI PHỤ · 54 tuổi, da trắng, người đọc lệnh bắt Julian tội mưu sát. "
  "Dùng: S23. Mặt phải đọc ra: dày dạn, chậm rãi, chắc chắn.",
  "Người đàn ông da trắng 54 tuổi, đậm người. Da sạm, nếp nhăn sâu ở trán và hai bên miệng.\n"
  "Gương mặt vuông, mũi to bản, cằm nặng. Râu ria muối tiêu lún phún.\n"
  "Tóc xám cắt ngắn, hói nhẹ đỉnh đầu.\n"
  "Mắt nâu sẫm, mí nặng, ánh nhìn chậm và chắc.\n"
  "Mặc áo khoác măng tô len màu xám than ngoài sơ mi xanh nhạt, cà vạt nâu thắt lỏng.\n"
  "Ánh nhìn ĐIỀM TĨNH VÀ MỆT MỎI NGHỀ NGHIỆP.")

P("REF_CRANE_PORTRAIT", "BOARD CHAIRMAN CRANE — chủ tịch hội đồng Kane Holdings",
  "VAI PHỤ · 67 tuổi, da trắng, người bước vào nhà thờ và gọi Adrian là Chairman Kane. "
  "Dùng: S22 · S23. Mặt phải đọc ra: quyền lực thật sự, cúi đầu trước một người trẻ hơn.",
  "Người đàn ông da trắng 67 tuổi, cao gầy. Da sáng mỏng, nếp nhăn sâu, gò má cao.\n"
  "Tóc bạc trắng thưa chải sát, râu cạo nhẵn.\n"
  "Mắt xanh xám nhạt sau kính gọng vàng mảnh. Mũi khoằm nhẹ. Môi mỏng.\n"
  "Mặc smoking đen cổ satin, sơ mi trắng cổ cánh, nơ đen.\n"
  "Ánh nhìn TRANG TRỌNG VÀ KÍNH CẨN.")

P("REF_REPORTER_PORTRAIT", "REPORTER — phóng viên trước cửa nhà thờ",
  "VAI PHỤ · 29 tuổi, da trắng, người chĩa micro vào Vanessa lúc bị còng tay. "
  "Dùng: S24. Mặt phải đọc ra: hăng, đang săn tin lớn nhất đời mình.",
  "Người phụ nữ da trắng 29 tuổi. Da sáng, trang điểm đậm chuẩn lên hình, má hồng.\n"
  "Gương mặt trái xoan, cằm nhọn, mũi nhỏ thẳng, môi tô son đỏ tươi.\n"
  "Tóc nâu sẫm dài ép thẳng, rẽ ngôi lệch, buông qua vai.\n"
  "Mắt nâu sáng, mi chuốt kỹ, chân mày kẻ sắc.\n"
  "Mặc áo khoác dạ màu đỏ tươi cổ bẻ, bên trong là áo thun đen.\n"
  "Ánh nhìn HĂNG HÁI VÀ TẬP TRUNG.")

P("REF_GUEST1_PORTRAIT", "GUEST ONE — khách dự cưới (nam)",
  "QUẦN CHÚNG CÓ THOẠI · 57 tuổi, da trắng, người thốt lên khi Ryan làm nhục Maya và khi băng hình bật lên. "
  "Dùng: S1 · S21 · S22 · S23. Mặt phải đọc ra: khá giả, bàng hoàng, không dám can.",
  "Người đàn ông da trắng 57 tuổi. Da sáng, mặt dài, gò má rõ, cằm vuông vừa.\n"
  "Tóc bạc muối tiêu chải gọn rẽ ngôi lệch.\n"
  "Mắt xanh xám, chân mày bạc, mũi thẳng, môi mỏng.\n"
  "Đeo kính gọng kim loại mảnh hình bầu dục.\n"
  "Mặc sơ mi trắng và cà vạt lụa xám bạc.\n"
  "Ánh nhìn BÀNG HOÀNG VÀ NGẦN NGẠI.")

P("REF_GUEST2_PORTRAIT", "GUEST TWO — khách dự cưới (nữ)",
  "QUẦN CHÚNG CÓ THOẠI · 51 tuổi, da đen, người bảo Maya ngồi xuống và kêu lên khi tiền bị ném. "
  "Dùng: S1 · S21 · S22 · S23. Mặt phải đọc ra: thương người, thẳng tính.",
  "Người phụ nữ Mỹ gốc Phi 51 tuổi. Da nâu vừa, gương mặt tròn đầy, gò má cao, cằm mềm.\n"
  "Tóc đen xoăn cắt ngắn phồng ôm đầu, có vài sợi bạc.\n"
  "Mắt nâu sẫm ấm, chân mày tỉa gọn, môi đầy tô son đỏ đất.\n"
  "Đeo khuyên tai vàng bản tròn to vừa.\n"
  "Mặc áo lụa màu xanh cổ vịt cổ tròn cài kín.\n"
  "Ánh nhìn THƯƠNG CẢM VÀ BỨC XÚC.")

# ══════════════════ TOÀN THÂN — MAYA ══════════════════
F("REF_MAYA_CUOI_FULL", "MAYA — VÁY CƯỚI ĐI MƯỢN",
  "Bộ váy cưới đi mượn của cảnh bị bỏ rơi ở bàn thờ Chúa và cả ngày chạy tiền sau đó.\nDùng: S1 · S2 · S3 · S4",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Váy cưới ĐI MƯỢN: váy dài chấm đất bằng satin màu TRẮNG NGÀ đã hơi ngả,\n"
  "dáng chữ A đơn giản, tay lỡ bằng ren mỏng, cổ tròn kín, thân váy trơn KHÔNG đính đá, KHÔNG voan trùm đầu.\n"
  "Váy hơi RỘNG ở eo và được ghim tạm hai chiếc kim băng nhỏ ở sườn trái — dấu hiệu đồ mượn không vừa người.\n"
  "Gấu váy có một vệt bụi mờ. Chân đi giày cao gót bít mũi màu kem đã cũ, gót bọc da mòn một bên.\n"
  "Bộ đồ SẠCH SẼ và được là phẳng — cũ ở chất vải, KHÔNG rách, KHÔNG bẩn.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung. KHÔNG vòng cổ, KHÔNG nhẫn.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_THUONG_FULL", "MAYA — ĐỒ THƯỜNG NGÀY",
  "Bộ đồ lao động — mặc khi phải khuân vác, dọn nhà.\nDùng: S7 · S16",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Áo len mỏng cổ tròn màu XÁM THAN đã BẠC MÀU nhẹ, cổ áo hơi giãn,\n"
  "tay áo xắn tới giữa cẳng tay. Quần jean xanh sẫm ống đứng đã sờn nhạt ở đầu gối, gấu quần gập một lần.\n"
  "Chân đi giày thể thao vải trắng ngà đã ố xám ở mũi, đế mòn không đều.\n"
  "Bộ đồ SẠCH SẼ, được giặt cẩn thận và là phẳng — nghèo thể hiện ở độ hao mòn của vải, KHÔNG dơ bẩn, KHÔNG rách.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_TUTE_FULL", "MAYA — BỘ TỬ TẾ ĐI VIỆC QUAN TRỌNG",
  "Bộ tươm tất nhất — để dành cho đăng ký kết hôn và phiên toà giám hộ.\n"
  "Dùng: S6 · S14 · S15",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Váy liền thân dáng suông màu XANH NAVY bằng vải crepe, tay lỡ, cổ tròn kín,\n"
  "dài quá gối, được là phẳng phiu và vừa vặn. Ngoài khoác một áo blazer mỏng cùng tông xanh navy, cài một cúc.\n"
  "Chân đi giày bít mũi gót thấp màu đen, da đã mềm và xước nhẹ ở mũi.\n"
  "Bộ đồ RẺ TIỀN NHƯNG CHỈN CHU: đường may đơn giản, vải không bóng, không hàng hiệu.\n"
  "TRANG SỨC — đúng hai món: đôi khuyên tai nhỏ đính đá của ảnh chân dung và một chiếc đồng hồ mặt tròn\n"
  "dây da nâu ở cổ tay TRÁI.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_SCRUB_FULL", "MAYA — ĐỒ SCRUB ĐIỀU DƯỠNG",
  "Đồng phục điều dưỡng ICU ở St. Agnes.\nDùng: S9 · S18 (phòng nhân sự + hành lang) · S25",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Bộ scrub y tá màu XANH MÒNG KÉT: áo cổ chữ V tay ngắn có hai túi dưới,\n"
  "quần cùng màu ống suông có dây rút. Vải cotton pha đã giặt nhiều nên hơi bạc và mềm rũ.\n"
  "Túi ngực trái cài một cây bút bi và một chiếc kéo cắt băng nhỏ. Trên hông trái kẹp một thẻ nhân viên\n"
  "ÚP MẶT XUỐNG, không đọc được chữ.\n"
  "Chân đi giày y tế bít mũi màu trắng ngà đã ố, đế cao su bằng.\n"
  "Tóc búi cao gọn hơn ảnh chân dung, không lọn nào buông xuống mặt.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung. KHÔNG vòng tay, KHÔNG nhẫn (luật vô trùng).",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_TRANG_FULL", "MAYA — ĐỒNG PHỤC TRẮNG + NẸP NGÓN TAY",
  "Bộ đồng phục trắng Vanessa bắt mặc để đứng góc phòng ở đám cưới, và chiếc nẹp ngón tay bị đánh gãy ở hầm xe.\n"
  "Dùng: S20 · S21 · S22 · S23 · S24",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Bộ đồng phục điều dưỡng màu TRẮNG kiểu cũ: áo dài tay cổ bẻ nhỏ cài hàng cúc\n"
  "trắng giữa ngực, dài quá hông, bên trong là quần trắng ống suông. Vải dày, hồ cứng, phẳng phiu.\n"
  "Chân đi giày y tế bít mũi màu trắng, đế cao su bằng.\n"
  "BÀN TAY PHẢI: ngón trỏ và ngón giữa được nẹp bằng một THANH NẸP NHÔM MỎNG quấn băng vải trắng,\n"
  "cố định thẳng, thấy rõ. Bàn tay trái để trần bình thường.\n"
  "TAY ÁO TRÁI ở vai bị RÁCH một đường ngắn chừng một gang, mép vải sờn ra — vết rách mới, phần còn lại của bộ đồ vẫn sạch.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_KHOAC_FULL", "MAYA — ÁO KHOÁC Ô LIU ĐI SỚM VỀ KHUYA",
  "Bộ khoác vội khi ra khỏi nhà lúc trời còn tối hoặc đã khuya: rạng sáng ở quầy viện phí và đêm ở hầm đỗ xe.\n"
  "Dùng: S5 · S19",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Áo khoác dạ NGẮN ngang hông màu Ô LIU đã bạc thành xám xanh, cổ bẻ,\n"
  "khoá kéo kim loại kéo lên hai phần ba, hai túi khoét chéo, khuỷu tay sờn bóng. Bên trong là áo phông\n"
  "cổ tròn màu TRẮNG NGÀ. Quần jean ĐEN ống đứng đã phai thành xám ở đùi. Chân đi giày thể thao vải\n"
  "trắng ngà đã ố xám ở mũi — đúng đôi giày của bộ thường ngày.\n"
  "Bộ đồ SẠCH SẼ, giặt cẩn thận — nghèo thể hiện ở độ bạc màu của vải, KHÔNG dơ bẩn, KHÔNG rách.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_CARO_FULL", "MAYA — SƠ MI FLANNEL CARO ĐI DẠO",
  "Bộ mặc lúc đẩy xe cho chồng ra ngoài đường giữa ban ngày.\nDùng: S10",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Sơ mi FLANNEL KẺ CARO NÂU ĐỎ và than, tay dài xắn tới khuỷu, mặc mở phanh\n"
  "để hở áo phông cổ tròn màu XÁM TRO bên trong, vạt áo buông ngoài quần. Vải flannel đã giặt nhiều nên xù nhẹ.\n"
  "Quần jean XANH SẪM ống đứng đã sờn nhạt ở đầu gối, gấu quần gập một lần.\n"
  "Chân đi giày thể thao vải trắng ngà đã ố xám ở mũi.\n"
  "Bộ đồ SẠCH SẼ và là phẳng — cũ ở chất vải, KHÔNG rách, KHÔNG bẩn.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_ONHA_FULL", "MAYA — ĐỒ TRONG NHÀ, TÓC XOÃ",
  "Bộ mặc trong nhà cổng lúc đêm khi thay băng cho chồng — bộ duy nhất cô để tóc xoã.\nDùng: S11",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Áo NỈ MỎNG dài tay cổ tròn màu BE ẤM, thân rộng, cổ tay áo đã giãn,\n"
  "tay áo xắn lên tới khuỷu để làm việc. Quần JOGGER màu XÁM TRO có dây rút ở cạp, gấu bo ống.\n"
  "Chân đi TẤT LEN màu kem, KHÔNG đi giày.\n"
  "TÓC: đây là bộ DUY NHẤT mái tóc xoăn được THẢ XOÃ NGANG VAI, không búi — mềm, tự nhiên, vài lọn\n"
  "buông trước mặt. Đây là chi tiết BẮT BUỘC của thẻ này.\n"
  "Bộ đồ SẠCH SẼ và mềm vì giặt nhiều — KHÔNG rách, KHÔNG bẩn.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_DEN_FULL", "MAYA — VÁY ĐEN MUA LẠI ĐI ĂN TỐI NHÀ CHỒNG",
  "Chiếc váy đen mua lại ở cửa hàng đồ cũ để đi bữa tối mười chín người nhà Kane.\nDùng: S8",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Váy liền thân màu ĐEN TRƠN bằng vải jersey dày, dáng suông, tay dài,\n"
  "cổ tròn kín, dài quá gối. Váy VỪA VẶN và được là phẳng nhưng vải KHÔNG bóng, không có chi tiết trang trí,\n"
  "đường may đơn giản — rõ ràng là đồ rẻ tiền mua lại. Ngoài quàng một khăn choàng mỏng màu XÁM NHẠT\n"
  "vắt qua một vai. Chân đi giày bít mũi gót thấp màu đen, da đã mềm và xước nhẹ ở mũi.\n"
  "TRANG SỨC — đúng hai món: đôi khuyên tai nhỏ đính đá của ảnh chân dung và một chiếc đồng hồ mặt tròn\n"
  "dây da nâu ở cổ tay TRÁI.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_CARDIGAN_FULL", "MAYA — CARDIGAN NGÀ ĐI TOÀ THÁP HALE",
  "Bộ thứ hai tươm tất, mặc khi lên phòng cô dâu ở toà tháp Hale.\nDùng: S17",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Cardigan len mỏng màu NGÀ, dài quá hông, cài hai cúc trên, tay dài,\n"
  "len đã hơi xù ở cổ tay. Bên trong là váy chữ A màu XÁM NHẠT bằng vải cotton dày, dài quá gối, là phẳng.\n"
  "Chân đi giày bít mũi gót thấp màu đen, da đã mềm và xước nhẹ ở mũi.\n"
  "Bộ đồ RẺ TIỀN NHƯNG CHỈN CHU và VỪA VẶN: không hàng hiệu, không chi tiết trang trí.\n"
  "TRANG SỨC — đúng hai món: đôi khuyên tai nhỏ đính đá của ảnh chân dung và một chiếc đồng hồ mặt tròn\n"
  "dây da nâu ở cổ tay TRÁI.",
  "REF_MAYA_PORTRAIT")

F("REF_MAYA_SCRUBKHOAC_FULL", "MAYA — SCRUB KHOÁC CARDIGAN VỀ PHÒNG TRỌ",
  "Bộ scrub của ca trực cuối cùng, khoác thêm cardigan để đi bộ về phòng trọ trong đêm bị đuổi việc.\nDùng: S18",
  "Người phụ nữ ở ẢNH 1, 27 tuổi. Bộ scrub y tá màu XANH MÒNG KÉT: áo cổ chữ V tay ngắn có hai túi dưới,\n"
  "quần cùng màu ống suông có dây rút, vải đã bạc và mềm rũ.\n"
  "Ngoài khoác một CARDIGAN LEN màu XÁM TRO dài quá hông, không cài cúc, len xù nhẹ, hai tay áo dài phủ tới\n"
  "nửa bàn tay. Túi ngực trái áo scrub cài một cây bút bi.\n"
  "TRÊN NGỰC TRÁI KHÔNG CÒN THẺ NHÂN VIÊN — chỉ còn một vệt vải sẫm hình chữ nhật ở chỗ thẻ từng kẹp.\n"
  "Chân đi giày y tế bít mũi màu trắng ngà đã ố, đế cao su bằng. Tóc búi cao gọn.\n"
  "TRANG SỨC — đúng một món: đôi khuyên tai nhỏ đính đá của ảnh chân dung.",
  "REF_MAYA_PORTRAIT")

# ══════════════════ TOÀN THÂN — ADRIAN ══════════════════
F("REF_ADRIAN_NHATHO_FULL", "ADRIAN — ÁO KHOÁC TỐI, XE LĂN ĐIỆN",
  "Bộ mặc khi ngồi hàng ghế cuối nhà thờ ngày Maya bị bỏ rơi.\nDùng: S1 · S4",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Áo khoác dạ mỏng màu XÁM THAN cài kín tới ngực,\n"
  "bên trong là sơ mi đen cài kín cổ. Quần âu đen ống đứng, gấu quần phủ mu bàn chân.\n"
  "Chân đi giày da đen buộc dây, mũi giày còn nguyên vẹn KHÔNG mòn — dấu hiệu của người không đi lại.\n"
  "Hai chân đặt gọn trên bàn để chân của xe. Trên đùi phủ một tấm chăn len mỏng màu xám đá gấp gọn.\n"
  + XELAN_DIEN + "\n"
  "Quần áo đắt tiền, cắt may vừa vặn, nhưng KHÔNG phô trương, KHÔNG logo.\n"
  "TRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_TUTE_FULL", "ADRIAN — SƠ MI + CARDIGAN, XE LĂN ĐIỆN",
  "Bộ mặc đi đăng ký kết hôn, về nhà cổng, bữa tối gia tộc và phiên toà.\nDùng: S6 · S7 · S8 · S14 · S15",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Sơ mi cotton màu XANH XÁM NHẠT cài kín tới cổ,\n"
  "tay áo dài buông. Ngoài khoác một áo len cardigan mỏng màu XÁM ĐÁ cài hai cúc giữa.\n"
  "Quần âu xám sẫm ống đứng. Chân đi giày da nâu sẫm buộc dây, đế còn nguyên KHÔNG mòn.\n"
  "Hai chân đặt gọn trên bàn để chân của xe.\n"
  + XELAN_DIEN + "\n"
  "Quần áo tốt, giản dị, vừa vặn, KHÔNG logo.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_NHA_FULL", "ADRIAN — ÁO THUN Ở NHÀ, XE LĂN ĐIỆN",
  "Bộ mặc ở nhà cổng và lúc ra quán cà phê vỉa hè.\nDùng: S10 · S11",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Áo thun cotton dài tay màu XÁM TRO cổ tròn,\n"
  "vải dày mềm, tay áo xắn tới khuỷu để lộ cẳng tay. Quần vải mềm màu đen ống suông, gấu quần ngắn trên mắt cá.\n"
  "Chân đi giày lười vải xám, đế phẳng KHÔNG mòn. Hai chân đặt trên bàn để chân của xe.\n"
  "Trên đùi phủ một tấm chăn len mỏng màu xám đá.\n"
  + XELAN_DIEN + "\n"
  "Quần áo đơn giản, sạch, KHÔNG logo.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_VESTNGOI_FULL", "ADRIAN — VEST ĐEN, XE LĂN ĐIỆN (phòng chỉ huy)",
  "Bộ vest chủ tịch, chỉ mặc trong phòng chỉ huy Kane Holdings.\nDùng: S13",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Bộ vest hai mảnh màu ĐEN cắt may đo, ve áo bản vừa,\n"
  "cài một cúc; bên trong là sơ mi trắng cổ cứng cài kín và cà vạt lụa màu XÁM BẠC thắt chuẩn.\n"
  "Quần âu đen ly thẳng. Giày da đen bóng buộc dây, đế còn nguyên KHÔNG mòn.\n"
  "Hai chân đặt gọn trên bàn để chân của xe.\n"
  + XELAN_DIEN + "\n"
  "Quần áo rất đắt tiền, đường may sắc, KHÔNG logo.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_XANHREU_FULL", "ADRIAN — ÁO LEN XANH RÊU, XE LĂN ĐIỆN",
  "Cùng bộ áo len xanh rêu của ngày bị trục xuất, nhưng còn chiếc xe lăn điện — dùng cho các khung TRƯỚC khi "
  "Julian cho người tịch thu xe.\nDùng: S16",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Áo len mỏng cổ tròn màu XANH RÊU SẪM, tay dài buông, "
  "gấu áo hơi giãn. Quần vải mềm màu xám than. Chân đi giày lười da nâu, đế KHÔNG mòn.\n"
  "Hai chân đặt gọn trên bàn để chân của xe.\n"
  + XELAN_DIEN + "\n"
  "Quần áo sạch sẽ và phẳng phiu.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_XELANTAY_FULL", "ADRIAN — ÁO LEN, XE LĂN TAY CŨ VÀNH CONG",
  "Sau khi Julian tịch thu xe lăn điện, chỉ còn chiếc xe tay cũ trong nhà kho.\nDùng: S16 · S18 · S19",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Áo len mỏng cổ tròn màu XANH RÊU SẪM, tay dài buông,\n"
  "gấu áo hơi giãn. Quần vải mềm màu xám than. Chân đi giày lười da nâu, đế KHÔNG mòn.\n"
  "Hai chân đặt trên bàn để chân bằng thép đã tróc sơn.\n"
  + XELAN_TAY + "\n"
  "Quần áo sạch sẽ và phẳng phiu.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_TIEC_FULL", "ADRIAN — VEST ĐEN, XE LĂN TAY CŨ (đám cưới Hale)",
  "Bộ vest đen đi dự đám cưới Vanessa, vẫn ngồi chiếc xe tay cũ vành cong.\nDùng: S20 · S21 · S22",
  "Người đàn ông ở ẢNH 1, 34 tuổi, NGỒI TRONG XE LĂN. Bộ vest hai mảnh màu ĐEN cắt may đo, cài một cúc;\n"
  "bên trong sơ mi trắng cổ cứng và cà vạt lụa đen bản vừa thắt chuẩn.\n"
  "Quần âu đen ly thẳng, giày da đen bóng, đế còn nguyên KHÔNG mòn. Hai chân đặt trên bàn để chân bằng thép tróc sơn.\n"
  + XELAN_TAY + "\n"
  "SỰ TƯƠNG PHẢN LÀ TRỌNG TÂM: bộ vest đắt tiền, phẳng phiu, sắc nét trên một chiếc xe lăn bệnh viện gỉ sét.\n"
  "TRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT", F_HEAD_NGOI)

F("REF_ADRIAN_VEST_FULL", "ADRIAN — VEST ĐEN, ĐỨNG THẲNG",
  "Từ lúc anh đứng dậy giữa nhà thờ trở đi — KHÔNG có xe lăn trong ảnh này.\nDùng: S22 · S23 · S24 · S25",
  "Người đàn ông ở ẢNH 1, 34 tuổi, ĐỨNG THẲNG TRÊN HAI CHÂN, KHÔNG có xe lăn, KHÔNG có nạng, KHÔNG có gậy.\n"
  "Bộ vest hai mảnh màu ĐEN cắt may đo, cài một cúc; sơ mi trắng cổ cứng, cà vạt lụa đen bản vừa.\n"
  "Quần âu đen ly thẳng, giày da đen bóng buộc dây.\n"
  "Tư thế: lưng thẳng, hai vai cân, hai chân đứng hơi rộng bằng vai để giữ thăng bằng, đầu gối khoá cứng —\n"
  "dáng của người vừa tập đi lại được, VỮNG nhưng phải cố. KHÔNG loạng choạng, KHÔNG khom lưng.\n"
  "Quần áo rất đắt tiền, hơi nhàu nhẹ ở gấu áo vest.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_ADRIAN_PORTRAIT")

# ══════════════════ TOÀN THÂN — RYAN & VANESSA ══════════════════
F("REF_RYAN_CUOI_FULL", "RYAN — VEST CHÚ RỂ",
  "Bộ chú rể của đám cưới hụt với Maya.\nDùng: S1",
  "Người đàn ông ở ẢNH 1, 31 tuổi. Bộ vest ba mảnh màu XANH NAVY SẪM cắt may vừa vặn: áo vest cài hai cúc,\n"
  "gi-lê cùng màu bên trong, sơ mi trắng cổ cứng, cà vạt lụa màu bạc thắt bản vừa.\n"
  "Ve áo trái cài MỘT BÔNG HOA HỒNG TRẮNG NHỎ.\n"
  "Quần âu cùng bộ ly thẳng, giày da nâu sẫm bóng buộc dây.\n"
  "Quần áo mới, phẳng phiu, đắt vừa phải — người đi thuê bộ đẹp nhất mình mua được.\n"
  "TRANG SỨC: một chiếc đồng hồ kim loại mặt tròn ở cổ tay TRÁI.",
  "REF_RYAN_PORTRAIT")

F("REF_RYAN_COMLE_FULL", "RYAN — COMPLE ĐI LÀM",
  "Bộ đi làm và đi ngoài phố sau khi bỏ Maya.\nDùng: S12",
  "Người đàn ông ở ẢNH 1, 31 tuổi. Bộ vest hai mảnh màu XÁM THAN cắt may vừa vặn, cài một cúc;\n"
  "sơ mi trắng cổ cứng mở một cúc trên cùng, KHÔNG cà vạt.\n"
  "Quần âu cùng bộ ly thẳng, giày da đen bóng có khoá kim loại nhỏ ở mu bàn chân.\n"
  "Quần áo mới, đắt hơn hẳn bộ chú rể — dấu hiệu của người vừa đổi đời.\n"
  "TRANG SỨC: một chiếc đồng hồ kim loại mặt tròn to bản ở cổ tay TRÁI.",
  "REF_RYAN_PORTRAIT")

F("REF_RYAN_TUXEDO_FULL", "RYAN — TUXEDO CHÚ RỂ NHÀ HALE",
  "Bộ chú rể ở đám cưới với Vanessa — trạng thái NGUYÊN VẸN.\nDùng: S20 · S21",
  "Người đàn ông ở ẢNH 1, 31 tuổi. Bộ TUXEDO màu ĐEN cắt may đo, ve áo satin bản vừa, cài một cúc;\n"
  "sơ mi trắng cổ cánh có nếp gấp dọc ngực, NƠ ĐEN thắt sẵn, khuy măng sét bạc.\n"
  "Quần âu đen có dải satin dọc ống, giày da đen bóng lộn.\n"
  "Ve áo trái cài MỘT BÔNG HOA HỒNG TRẮNG NHỎ.\n"
  "Quần áo rất đắt tiền, mới tinh, phẳng phiu tuyệt đối.\n"
  "TRANG SỨC: đồng hồ kim loại mặt tròn to bản ở cổ tay TRÁI và nhẫn cưới vàng trơn ở ngón áp út tay TRÁI.",
  "REF_RYAN_PORTRAIT")

F("REF_RYAN_ADO_FULL", "RYAN — BOMBER DA LỘN ĐI PHỐ",
  "Bộ mặc khi đi cà phê ngoài phố với Vanessa.\nDùng: S10",
  "Người đàn ông ở ẢNH 1, 31 tuổi. Áo BOMBER DA LỘN màu NÂU HẠT DẺ, khoá kéo mở, cổ bo và gấu bo dệt kim\n"
  "màu nâu sẫm, da mềm mới nguyên. Bên trong là áo phông cổ tròn màu ĐEN trơn.\n"
  "Quần chinos màu BE ống côn, gấu quần gập một lần lộ mắt cá. Chân đi giày sneaker da trắng đế thấp,\n"
  "sạch không một vết. Quần áo mới, đắt tiền, đúng mốt — người vừa đổi đời và muốn ai cũng thấy.\n"
  "TRANG SỨC: một chiếc đồng hồ kim loại mặt tròn to bản ở cổ tay TRÁI, KHÔNG nhẫn.",
  "REF_RYAN_PORTRAIT")

F("REF_RYAN_SOMI_FULL", "RYAN — SƠ MI TRẮNG XẮN TAY",
  "Bộ mặc khi lên phòng cô dâu ở toà tháp Hale sau giờ làm.\nDùng: S17",
  "Người đàn ông ở ẢNH 1, 31 tuổi. Sơ mi TRẮNG cổ cứng, mở HAI cúc trên cùng, KHÔNG cà vạt,\n"
  "hai tay áo XẮN LÊN QUA KHUỶU gọn gàng, vạt áo sơ vin. Thắt lưng da nâu bản hẹp khoá kim loại bạc.\n"
  "Quần âu màu XANH NAVY ly thẳng, giày da nâu sẫm bóng buộc dây.\n"
  "Quần áo mới, cắt may vừa vặn, phẳng phiu.\n"
  "TRANG SỨC: một chiếc đồng hồ kim loại mặt tròn to bản ở cổ tay TRÁI.",
  "REF_RYAN_PORTRAIT")

F("REF_RYAN_TUXEDOROI_FULL", "RYAN — TUXEDO SAU KHI SỤP ĐỔ",
  "Vẫn bộ tuxedo của đám cưới, nhưng sau khi mọi thứ vỡ và anh ta quỳ trên bậc đá.\nDùng: S24",
  "Người đàn ông ở ẢNH 1, 31 tuổi. Vẫn bộ TUXEDO ĐEN của đám cưới, nhưng ĐÃ RÃ RỜI:\n"
  "NƠ ĐEN đã tháo, treo lủng lẳng hai đầu hai bên cổ áo; sơ mi trắng bung HAI cúc trên cùng, cổ áo vẹo;\n"
  "vạt áo tuxedo tuột khỏi cúc, mở phanh; một bên khuy măng sét đã mất nên cổ tay áo phải xổ ra.\n"
  "VE ÁO TRÁI CHỈ CÒN CHIẾC GHIM RỖNG — bông hoa hồng trắng đã rơi mất.\n"
  "HAI ĐẦU GỐI QUẦN có hai mảng BỤI ĐÁ XÁM rõ rệt vì vừa quỳ trên bậc thềm.\n"
  "Tóc nâu chải ngược đã XỔ RỐI, vài lọn rơi xuống trán. Giày da đen còn bóng.\n"
  "Bộ đồ vẫn đắt tiền và KHÔNG rách, KHÔNG bẩn ngoài hai vệt bụi ở gối — hỏng ở dáng, không ở vải.\n"
  "TRANG SỨC: đồng hồ kim loại mặt tròn to bản ở cổ tay TRÁI. NGÓN ÁP ÚT TAY TRÁI ĐỂ TRẦN — nhẫn cưới đã tháo.",
  "REF_RYAN_PORTRAIT")

F("REF_VANESSA_DO_FULL", "VANESSA — VÁY ĐỎ Ở NHÀ THỜ",
  "Bộ váy cô mặc khi bước vào phá đám cưới của Maya.\nDùng: S1",
  "Người phụ nữ ở ẢNH 1, 28 tuổi. Váy liền thân hàng hiệu màu ĐỎ RƯỢU VANG bằng lụa dày, dáng ôm,\n"
  "tay lỡ, cổ thuyền kín đáo, dài quá gối, đường may sắc nét, vải bắt sáng bóng mềm.\n"
  "Chân đi giày cao gót nhọn màu đen bóng, gót cao mảnh.\n"
  "Trên tay cầm một chiếc CLUTCH DA ĐEN nhỏ hình chữ nhật có khoá kim loại vàng.\n"
  "Quần áo MỚI, ĐẮT TIỀN và vừa như in — tương phản tuyệt đối với váy cưới đi mượn của nhân vật khác.\n"
  "TRANG SỨC — đúng ba món: khuyên tai kim cương tấm của ảnh chân dung, một chiếc vòng tay vàng bản to\n"
  "ở cổ tay PHẢI, và một chiếc đồng hồ vàng mặt nhỏ ở cổ tay TRÁI.",
  "REF_VANESSA_PORTRAIT")

F("REF_VANESSA_NGAY_FULL", "VANESSA — ĐỒ BAN NGÀY",
  "Bộ đi phố ban ngày.\nDùng: S10",
  "Người phụ nữ ở ẢNH 1, 28 tuổi. Áo khoác dạ mỏng dáng dài màu KEM SỮA mặc mở, bên trong là áo lụa\n"
  "màu trắng ngà cài kín và quần âu ống rộng màu kem cùng tông.\n"
  "Chân đi giày cao gót mũi nhọn màu nude bóng.\n"
  "Trên vai đeo một chiếc TÚI DA MÀU NÂU HẠT DẺ quai xích kim loại vàng.\n"
  "Quần áo mới, đắt tiền, phẳng phiu tuyệt đối, tông sáng đồng bộ.\n"
  "TRANG SỨC — đúng ba món: khuyên tai kim cương tấm của ảnh chân dung, vòng tay vàng bản to ở cổ tay PHẢI,\n"
  "và một chiếc nhẫn đính hôn kim cương to ở ngón áp út tay TRÁI.",
  "REF_VANESSA_PORTRAIT")

F("REF_VANESSA_CODAU_FULL", "VANESSA — VÁY CƯỚI CÔ DÂU",
  "Váy cưới ở đám cưới của chính cô — trạng thái NGUYÊN VẸN.\nDùng: S21 · S22",
  "Người phụ nữ ở ẢNH 1, 28 tuổi. Váy cưới cao cấp màu TRẮNG TINH: thân trên bằng ren dày đính hạt pha lê\n"
  "li ti, tay lỡ bằng ren mỏng, cổ tim kín đáo; chân váy xoè lớn bằng nhiều lớp tuyn, đuôi váy dài kéo lê\n"
  "phía sau chừng một mét rưỡi.\n"
  "Tóc búi cao cài một chiếc TRÂM KIM CƯƠNG nhỏ, KHÔNG voan trùm mặt.\n"
  "Chân đi giày cao gót satin trắng mũi nhọn.\n"
  "Quần áo mới tinh, đắt đến mức phô trương, phẳng phiu tuyệt đối.\n"
  "TRANG SỨC — đúng ba món: khuyên tai kim cương tấm của ảnh chân dung, nhẫn cưới kim cương ở ngón áp út\n"
  "tay TRÁI, và một chiếc vòng tay kim cương mảnh ở cổ tay PHẢI. CỔ ĐỂ TRẦN, KHÔNG đeo vòng cổ.",
  "REF_VANESSA_PORTRAIT")

F("REF_VANESSA_LUA_FULL", "VANESSA — ÁO CHOÀNG LỤA PHÒNG THỬ VÁY",
  "Bộ cô mặc khi tiếp Maya trong phòng cô dâu ở toà tháp Hale, giữa buổi thử váy.\nDùng: S17",
  "Người phụ nữ ở ẢNH 1, 28 tuổi. Áo choàng LỤA dài quá gối màu CHAMPAGNE ÁNH VÀNG, buông mở,\n"
  "thắt lưng lụa cùng màu buộc lơi ở eo, tay dài rộng, mặt lụa bắt sáng bóng mềm.\n"
  "Bên trong là bộ camisole lụa và quần lụa ống rộng cùng tông màu KEM SỮA.\n"
  "Chân đi dép lê satin gót nhọn màu champagne.\n"
  "Quần áo mới tinh, cực đắt, phẳng phiu tuyệt đối — người tiếp khách trong đồ ngủ vì không cần cố gắng.\n"
  "Tóc vàng bạch kim để DÀI THẲNG buông xuống ngực, chưa làm tóc cưới.\n"
  "TRANG SỨC — đúng ba món: khuyên tai kim cương tấm của ảnh chân dung, nhẫn đính hôn kim cương to ở ngón\n"
  "áp út tay TRÁI, và một chiếc vòng tay vàng bản to ở cổ tay PHẢI.",
  "REF_VANESSA_PORTRAIT")

F("REF_VANESSA_CODAUXO_FULL", "VANESSA — VÁY CƯỚI ĐÃ XỔ",
  "Vẫn chiếc váy cưới đó, sau khi đoạn băng được chiếu lên và cả gian phòng quay lại nhìn cô.\nDùng: S23",
  "Người phụ nữ ở ẢNH 1, 28 tuổi. Vẫn chiếc VÁY CƯỚI TRẮNG TINH của đám cưới: thân trên ren dày đính hạt\n"
  "pha lê li ti, tay lỡ ren mỏng, cổ tim kín, chân váy xoè lớn nhiều lớp tuyn, đuôi váy dài kéo lê phía sau.\n"
  "NHƯNG ĐÃ BẮT ĐẦU HỎNG DÁNG: búi tóc cao đã XỔ RA BA BỐN LỌN rơi xuống hai bên thái dương và gáy;\n"
  "chiếc TRÂM KIM CƯƠNG bị lệch hẳn sang một bên; một mảng ren ở vai TRÁI bị kéo giãn nhăn lại;\n"
  "gấu đuôi váy có MỘT VỆT GIÀY XÁM MỜ do bị người khác giẫm phải.\n"
  "Váy KHÔNG rách, KHÔNG bẩn ngoài vệt giày ở gấu — hỏng ở sự chỉn chu, không ở vải.\n"
  "Chân đi giày cao gót satin trắng mũi nhọn.\n"
  "TRANG SỨC — đúng ba món: khuyên tai kim cương tấm của ảnh chân dung, nhẫn cưới kim cương ở ngón áp út\n"
  "tay TRÁI, và vòng tay kim cương mảnh ở cổ tay PHẢI. CỔ ĐỂ TRẦN, KHÔNG đeo vòng cổ.",
  "REF_VANESSA_PORTRAIT")

F("REF_VANESSA_CODAUBAN_FULL", "VANESSA — VÁY CƯỚI, HAI TAY CÒNG SAU LƯNG",
  "Chiếc váy cưới ở bậc thềm nhà thờ lúc chập tối, khi cô bị dẫn xuống trước ống kính truyền hình.\nDùng: S24",
  "Người phụ nữ ở ẢNH 1, 28 tuổi. Vẫn chiếc VÁY CƯỚI TRẮNG của đám cưới, nay ĐÃ TAN:\n"
  "búi tóc SỤP HẲN, tóc vàng bạch kim XOÃ RỐI xuống hai vai và che một phần má; chiếc trâm kim cương\n"
  "ĐÃ RƠI MẤT, chỉ còn vài chiếc ghim tóc lỏng lẻo.\n"
  "HAI TAY BỊ CÒNG RA SAU LƯNG bằng một chiếc còng thép sáng — hai vai vì thế bị kéo ngửa ra sau,\n"
  "hai cánh tay duỗi thẳng sau lưng. Đây là chi tiết BẮT BUỘC của thẻ này.\n"
  "Gấu chân váy và đuôi váy LẤM MỘT VỆT BỤI XÁM chạy dài; một mảng ren ở vai TRÁI nhăn hẳn;\n"
  "một dải tuyn ở sườn phải bị tuột khỏi đường may, buông lơi.\n"
  "Váy KHÔNG rách toạc, KHÔNG bê bết — chỉ lấm bụi và mất dáng.\n"
  "Chân đi giày cao gót satin trắng mũi nhọn, một bên gót đã dính bụi đá.\n"
  "TRANG SỨC — đúng hai món: khuyên tai kim cương tấm của ảnh chân dung và nhẫn cưới kim cương ở ngón áp út\n"
  "tay TRÁI. VÒNG TAY KIM CƯƠNG ĐÃ THÁO, cổ tay phải để trần dưới vòng còng. CỔ ĐỂ TRẦN.",
  "REF_VANESSA_PORTRAIT")

# ══════════════════ TOÀN THÂN — CÒN LẠI ══════════════════
F("REF_HELEN_ICU_FULL", "HELEN — ÁO BỆNH NHÂN, NẰM GIƯỜNG ICU",
  "Trạng thái duy nhất của bà trong phim: nằm trên giường hồi sức.\nDùng: S9 · S25",
  "Người phụ nữ ở ẢNH 1, 56 tuổi, NẰM NGỬA trên một chiếc giường bệnh viện có thành chắn kim loại,\n"
  "đầu giường nâng khoảng ba mươi độ, chăn dệt màu trắng ngà kéo tới ngang ngực.\n"
  "Mặc áo bệnh nhân màu XANH PHẤN NHẠT có hoa văn chấm nhỏ, cài dây sau gáy, tay áo ngắn.\n"
  "Có một ống thở mũi (canun) hai nhánh nhỏ gác qua vành tai và một dây truyền dịch dán băng ở mu bàn tay TRÁI.\n"
  "Hai tay đặt xuôi trên chăn. Mắt NHẮM. Tóc bạc ngắn được chải gọn.\n"
  "KHÔNG có máy móc nào khác trong khung — chỉ người và giường.\n"
  "TRANG SỨC: KHÔNG đeo gì cả (nhẫn cưới đã bị tháo ra).",
  "REF_HELEN_PORTRAIT")

for _rid, _lb, _ds, _bd, _pt in [
 ("REF_SEBASTIAN_VEST_FULL", "SEBASTIAN — VEST ĐEN",
  "Trạng thái duy nhất: bộ vest công vụ.\nDùng: S1 · S6 · S12 · S13 · S22 · S23",
  "Người đàn ông ở ẢNH 1, 52 tuổi. Bộ vest hai mảnh màu ĐEN cắt may đo, cài hai cúc; sơ mi trắng cổ cứng,\n"
  "cà vạt lụa màu xám than thắt chặt. Quần âu đen ly thẳng, giày da đen bóng buộc dây.\n"
  "Trên tay cầm một BÌA KẸP HỒ SƠ BẰNG DA MÀU NÂU SẪM đóng kín (không đọc được chữ).\n"
  "Quần áo đắt tiền, phẳng phiu tuyệt đối, KHÔNG logo.\nTRANG SỨC: đồng hồ da đen mặt tròn ở cổ tay TRÁI.",
  "REF_SEBASTIAN_PORTRAIT"),
 ("REF_JULIAN_VEST_FULL", "JULIAN — VEST XANH NAVY",
  "Bộ mặc ở bữa tối gia tộc, phiên toà và buổi trục xuất.\nDùng: S8 · S14 · S16",
  "Người đàn ông ở ẢNH 1, 41 tuổi. Bộ vest ba mảnh màu XANH NAVY SẪM cắt may đo, ve áo bản hẹp, cài hai cúc;\n"
  "gi-lê cùng màu, sơ mi trắng cổ cứng, cà vạt lụa vân chìm màu xanh cổ vịt, khăn túi ngực lụa trắng gấp nhọn.\n"
  "Quần âu cùng bộ, giày da nâu đỏ bóng lộn buộc dây.\n"
  "Quần áo cực đắt và được chăm chút quá mức — người muốn ai cũng thấy mình đắt.\n"
  "TRANG SỨC: đồng hồ vàng mặt to ở cổ tay TRÁI và nhẫn vàng mặt vuông ở ngón út tay PHẢI.",
  "REF_JULIAN_PORTRAIT"),
 ("REF_JULIAN_TUXEDO_FULL", "JULIAN — TUXEDO DỰ TIỆC",
  "Bộ mặc ở đám cưới nhà Hale.\nDùng: S20 · S21 · S22 · S23",
  "Người đàn ông ở ẢNH 1, 41 tuổi. Bộ TUXEDO màu ĐEN ve satin, cài một cúc; sơ mi trắng cổ cánh,\n"
  "nơ đen thắt sẵn, khăn túi ngực lụa trắng. Quần âu đen có dải satin dọc ống, giày da đen bóng lộn.\n"
  "Quần áo cực đắt, mới tinh.\n"
  "TRANG SỨC: đồng hồ vàng mặt to ở cổ tay TRÁI và nhẫn vàng mặt vuông ở ngón út tay PHẢI.",
  "REF_JULIAN_PORTRAIT"),
 ("REF_PRIEST_AO_FULL", "PRIEST — LỄ PHỤC",
  "Trạng thái duy nhất.\nDùng: S1",
  "Người đàn ông ở ẢNH 1, 64 tuổi. Áo lễ dài chấm mắt cá màu TRẮNG NGÀ (áo alba) thắt dây lưng vải cùng màu,\n"
  "bên ngoài khoác dải STOLA màu TRẮNG thêu chỉ vàng vắt hai vai buông xuống trước ngực.\n"
  "Cổ áo cồn trắng cứng lộ ra ở trong. Chân đi giày da đen bệt đã cũ.\n"
  "Lễ phục sạch sẽ, là phẳng, có nếp gấp mềm của vải dùng lâu năm.\nTRANG SỨC: một cây thánh giá bạc nhỏ đeo dây da ở cổ.",
  "REF_PRIEST_PORTRAIT"),
 ("REF_PRESCOTT_FULL", "MRS. PRESCOTT — ÁO TWEED DỰ CƯỚI",
  "Trạng thái duy nhất.\nDùng: S2",
  "Người phụ nữ ở ẢNH 1, 59 tuổi. Bộ vest nữ vải TWEED màu KEM có sợi vàng dệt xen, áo khoác cài bốn cúc vàng,\n"
  "chân váy bút chì cùng bộ dài quá gối. Bên trong là áo lụa trắng ngà cài kín.\n"
  "Chân đi giày cao gót bít mũi màu kem, gót vuông thấp.\n"
  "Trên tay khoác một chiếc TÚI DA MÀU KEM quai ngắn có khoá kim loại vàng.\n"
  "Quần áo cực đắt, phẳng phiu tuyệt đối, không một sợi chỉ thừa.\n"
  "TRANG SỨC — đúng hai món: chuỗi ngọc trai một vòng ở cổ và khuyên tai ngọc trai tròn.",
  "REF_PRESCOTT_PORTRAIT"),
 ("REF_CLERKBILL_FULL", "BILLING CLERK — ÁO BLOUSE HÀNH CHÍNH",
  "Trạng thái duy nhất.\nDùng: S5",
  "Người phụ nữ ở ẢNH 1, 46 tuổi. Áo blouse polyester màu XANH NHẠT của khối hành chính bệnh viện,\n"
  "cổ bẻ, cài kín tới ngực, tay ngắn; bên dưới là quần âu đen ống suông đã bạc.\n"
  "Chân đi giày bệt màu đen mũi tròn, đế cao su, gót mòn vẹt.\n"
  "Trên cổ đeo một DÂY ĐEO THẺ NHÂN VIÊN màu xanh, tấm thẻ ÚP MẶT XUỐNG (không đọc được chữ).\n"
  "Quần áo sạch, đã giặt nhiều nên bạc màu.\nTRANG SỨC — đúng một món: nhẫn cưới vàng trơn mảnh ở ngón áp út tay TRÁI.",
  "REF_CLERKBILL_PORTRAIT"),
 ("REF_PAWN_FULL", "PAWN BROKER — ÁO CA RÔ XẮN TAY",
  "Trạng thái duy nhất.\nDùng: S3",
  "Người đàn ông ở ẢNH 1, 57 tuổi. Áo sơ mi flannel kẻ ca rô XÁM XANH xắn tay tới khuỷu, cổ áo đã sờn,\n"
  "hai cúc trên để mở, bên trong lộ áo lót cotton trắng ngà.\n"
  "Quần jean xanh bạc thắt dây lưng da nâu bản to có khoá đồng. Chân đi bốt da nâu đã nứt nẻ ở mũi.\n"
  "Quần áo cũ, sạch, hơi nhàu.\nTRANG SỨC: một chiếc nhẫn vàng bản dày ở ngón út tay PHẢI và đồng hồ kim loại cũ ở cổ tay TRÁI.",
  "REF_PAWN_PORTRAIT"),
 ("REF_LOAN_FULL", "LOAN OFFICER — SƠ MI CÀ VẠT NGÂN HÀNG",
  "Trạng thái duy nhất.\nDùng: S3",
  "Người đàn ông ở ẢNH 1, 38 tuổi. Sơ mi trắng cài kín cổ, cà vạt xanh navy trơn thắt chặt, tay áo dài cài khuy.\n"
  "Quần âu xám ly thẳng, thắt lưng da đen bản mảnh. Chân đi giày da đen bóng buộc dây.\n"
  "Trên ngực trái kẹp một thẻ nhân viên ÚP MẶT XUỐNG (không đọc được chữ).\n"
  "Quần áo rẻ tiền nhưng phẳng phiu tuyệt đối.\nTRANG SỨC: đồng hồ dây da đen mặt vuông ở cổ tay TRÁI.",
  "REF_LOAN_PORTRAIT"),
 ("REF_CLERK_FULL", "CLERK — BLAZER HỘ TỊCH",
  "Trạng thái duy nhất.\nDùng: S6",
  "Người phụ nữ ở ẢNH 1, 51 tuổi. Áo blazer XANH NAVY cài một cúc, bên trong sơ mi trắng cài kín;\n"
  "chân váy bút chì đen dài quá gối. Chân đi giày bệt bít mũi màu đen.\n"
  "Trên ngực trái kẹp một thẻ nhân viên ÚP MẶT XUỐNG (không đọc được chữ).\n"
  "Quần áo công chức, phẳng phiu, hơi cũ.\nTRANG SỨC — đúng hai món: khuyên tai vàng tròn nhỏ và đồng hồ dây kim loại ở cổ tay TRÁI.",
  "REF_CLERK_PORTRAIT"),
 ("REF_MARGARET_FULL", "AUNT MARGARET — ÁO LỤA DỰ TIỆC GIA TỘC",
  "Trạng thái duy nhất.\nDùng: S8",
  "Người phụ nữ ở ẢNH 1, 66 tuổi. Áo lụa màu TÍM NHẠT cổ tròn cài kín, tay dài buông; ngoài khoác áo len\n"
  "mỏng màu kem để hờ. Chân váy lụa cùng tông tím nhạt dài chấm bắp chân.\n"
  "Chân đi giày bít mũi gót thấp màu tím than.\n"
  "Quần áo cực đắt, cổ điển, phẳng phiu.\nTRANG SỨC — đúng hai món: chuỗi ngọc trai ở cổ và khuyên tai ngọc trai giọt nước.",
  "REF_MARGARET_PORTRAIT"),
 ("REF_PETER_FULL", "UNCLE PETER — VEST XÁM THAN",
  "Trạng thái duy nhất.\nDùng: S8",
  "Người đàn ông ở ẢNH 1, 63 tuổi, bụng đầy. Bộ vest hai mảnh màu XÁM THAN cắt rộng, cài một cúc căng nhẹ ở bụng;\n"
  "sơ mi HỒNG NHẠT cổ cứng, cà vạt lụa vân màu RƯỢU VANG thắt bản to.\n"
  "Quần âu cùng bộ, giày da nâu bóng buộc dây.\n"
  "Quần áo đắt tiền nhưng hơi chật.\nTRANG SỨC: đồng hồ vàng mặt to ở cổ tay TRÁI và nhẫn vàng mặt đá đỏ ở ngón út tay PHẢI.",
  "REF_PETER_PORTRAIT"),
 ("REF_DIANE_FULL", "NURSE DIANE — SCRUB XANH MÒNG KÉT",
  "Trạng thái duy nhất.\nDùng: S9 · S18 · S25",
  "Người phụ nữ ở ẢNH 1, 44 tuổi. Bộ scrub y tá màu XANH MÒNG KÉT: áo cổ chữ V tay ngắn hai túi dưới,\n"
  "quần cùng màu ống suông dây rút. Vải đã giặt nhiều nên bạc và mềm.\n"
  "Ngoài khoác một áo khoác fleece mỏng màu xám mở khoá.\n"
  "Túi ngực cài bút bi. Chân đi giày y tế bít mũi màu trắng đã ố.\n"
  "TRANG SỨC — đúng hai món: nhẫn cưới vàng trơn ở ngón áp út tay TRÁI và một chiếc đồng hồ y tá mặt tròn\n"
  "kẹp ở túi ngực trái.",
  "REF_DIANE_PORTRAIT"),
 ("REF_PAULA_FULL", "NURSE PAULA — SCRUB TÍM HOA CÀ",
  "Trạng thái duy nhất.\nDùng: S9",
  "Người phụ nữ ở ẢNH 1, 33 tuổi. Bộ scrub y tá màu TÍM HOA CÀ: áo cổ chữ V tay ngắn, quần cùng màu ống suông.\n"
  "Vải còn mới, phẳng. Chân đi giày y tế bít mũi màu trắng còn mới tinh.\n"
  "Trên cổ đeo dây thẻ nhân viên màu tím, thẻ ÚP MẶT XUỐNG (không đọc được chữ).\n"
  "TRANG SỨC — đúng ba món: khuyên tai vàng nhỏ, một chiếc vòng tay hạt nhỏ ở cổ tay PHẢI, và đồng hồ dây\n"
  "silicon hồng ở cổ tay TRÁI.",
  "REF_PAULA_PORTRAIT"),
 ("REF_HALLORAN_FULL", "MR. HALLORAN — SƠ MI TỔNG GIÁM ĐỐC",
  "Trạng thái duy nhất.\nDùng: S12",
  "Người đàn ông ở ẢNH 1, 56 tuổi, đậm người. Sơ mi trắng cổ cứng cài kín, cà vạt lụa XANH NAVY nới lỏng\n"
  "một nấc, cổ áo hơi bung. Quần âu xám than ly thẳng, thắt lưng da đen khoá bạc.\n"
  "Áo vest cùng bộ VẮT TRÊN CÁNH TAY TRÁI chứ không mặc. Chân đi giày da đen bóng buộc dây.\n"
  "Quần áo đắt tiền nhưng đã nhàu ở lưng và nách — người ngồi bàn giấy cả ngày.\n"
  "TRANG SỨC: đồng hồ kim loại mặt to ở cổ tay TRÁI và nhẫn cưới vàng ở ngón áp út tay TRÁI.",
  "REF_HALLORAN_PORTRAIT"),
 ("REF_BOARD1_FULL", "BOARD MEMBER ONE — VEST XANH THAN",
  "Trạng thái duy nhất.\nDùng: S13",
  "Người đàn ông ở ẢNH 1, 49 tuổi. Bộ vest hai mảnh màu XANH THAN cài một cúc, sơ mi trắng, cà vạt lụa xám bạc.\n"
  "Quần âu cùng bộ, giày da đen bóng. Trên tay cầm một chiếc MÁY TÍNH BẢNG màn hình tối (không đọc được chữ).\n"
  "Quần áo đắt, phẳng phiu.\nTRANG SỨC: đồng hồ dây da nâu ở cổ tay TRÁI.",
  "REF_BOARD1_PORTRAIT"),
 ("REF_BOARD2_FULL", "BOARD MEMBER TWO — BLAZER ĐEN",
  "Trạng thái duy nhất.\nDùng: S13",
  "Người phụ nữ ở ẢNH 1, 45 tuổi. Áo blazer ĐEN cắt sắc cài một cúc, bên trong sơ mi lụa trắng cài kín,\n"
  "quần âu đen ống đứng. Chân đi giày cao gót bít mũi màu đen gót vuông.\n"
  "Trên tay cầm một TẬP TÀI LIỆU BÌA CỨNG MÀU XÁM đóng kín (không đọc được chữ).\n"
  "Quần áo đắt, sắc sảo.\nTRANG SỨC — đúng hai món: khuyên tai vàng bản dẹt và đồng hồ vàng mảnh ở cổ tay TRÁI.",
  "REF_BOARD2_PORTRAIT"),
 ("REF_WHITMORE_FULL", "JUDGE WHITMORE — ÁO CHOÀNG THẨM PHÁN",
  "Trạng thái duy nhất.\nDùng: S14",
  "Người phụ nữ ở ẢNH 1, 61 tuổi. Áo choàng thẩm phán màu ĐEN rộng tay dài chấm bắp chân, cài kín trước ngực,\n"
  "cổ áo sơ mi trắng lộ ra ở trong. Chân đi giày bít mũi gót thấp màu đen.\n"
  "Áo choàng bằng vải dày rủ, phẳng phiu, có nếp gấp mềm.\n"
  "TRANG SỨC — đúng hai món: khuyên tai vàng tròn nhỏ và một chiếc nhẫn cưới vàng trơn ở tay TRÁI.",
  "REF_WHITMORE_PORTRAIT"),
 ("REF_LAWYER_FULL", "JULIAN'S LAWYER — VEST SỌC MẢNH",
  "Trạng thái duy nhất.\nDùng: S14",
  "Người đàn ông ở ẢNH 1, 50 tuổi. Bộ vest ba mảnh màu XÁM có SỌC DỌC MẢNH, cài hai cúc, gi-lê cùng bộ;\n"
  "sơ mi trắng cổ cứng, cà vạt lụa XANH RÊU, khăn túi ngực trắng gấp nhọn.\n"
  "Quần âu cùng bộ, giày da đen bóng buộc dây. Trên tay cầm một CẶP DA ĐEN dáng vuông.\n"
  "Quần áo đắt, kiểu cổ điển.\nTRANG SỨC: đồng hồ vàng dây da nâu ở cổ tay TRÁI.",
  "REF_LAWYER_PORTRAIT"),
 ("REF_DEPUTY_FULL", "SHERIFF'S DEPUTY — ĐỒNG PHỤC CẢNH SÁT HẠT",
  "Trạng thái duy nhất.\nDùng: S16",
  "Người đàn ông ở ẢNH 1, 36 tuổi, vai rộng. Đồng phục cảnh sát hạt màu XANH RÊU SẪM: áo sơ mi đồng phục\n"
  "tay ngắn cài kín có cầu vai, quần cùng màu có sọc đen dọc ống.\n"
  "Thắt lưng công vụ bằng da đen bản to có các ngăn đựng, KHÔNG có súng lộ ra.\n"
  "Trên ngực có phù hiệu kim loại hình khiên và bảng tên ÚP MẶT (không đọc được chữ).\n"
  "Chân đi bốt da đen cao cổ đánh bóng. Đội mũ lưỡi trai đồng phục cùng màu.\n"
  "TRANG SỨC: KHÔNG đeo gì cả.",
  "REF_DEPUTY_PORTRAIT"),
 ("REF_HR_FULL", "HR DIRECTOR — BLAZER XÁM",
  "Trạng thái duy nhất.\nDùng: S18",
  "Người phụ nữ ở ẢNH 1, 53 tuổi. Áo blazer XÁM cài một cúc, bên trong sơ mi trắng cài kín, chân váy bút chì\n"
  "màu xám than dài quá gối. Chân đi giày bít mũi gót thấp màu đen.\n"
  "Trên ngực trái kẹp thẻ nhân viên ÚP MẶT XUỐNG (không đọc được chữ).\n"
  "Quần áo tươm tất, hơi cũ.\nTRANG SỨC — đúng hai món: dây chuyền vàng bản nhỏ và khuyên tai vàng tròn.",
  "REF_HR_PORTRAIT"),
 ("REF_THUG1_FULL", "THUG ONE — ÁO BOMBER ĐEN",
  "Trạng thái duy nhất.\nDùng: S19",
  "Người đàn ông ở ẢNH 1, 38 tuổi, vai rộng. Áo khoác bomber vải dù màu ĐEN kéo khoá tới giữa ngực,\n"
  "bên trong là áo thun xám tro. Quần jean đen ống đứng, thắt lưng da đen.\n"
  "Chân đi giày thể thao da đen đế dày. Hai bàn tay đeo GĂNG TAY DA ĐEN ôm sát.\n"
  "Quần áo tối màu, không nhãn hiệu, không gì để nhận dạng.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_THUG1_PORTRAIT"),
 ("REF_THUG2_FULL", "THUG TWO — ÁO HOODIE XÁM THAN",
  "Trạng thái duy nhất.\nDùng: S19",
  "Người đàn ông ở ẢNH 1, 32 tuổi, cao gầy. Áo hoodie nỉ màu XÁM THAN kéo khoá kín, mũ trùm hạ xuống vai,\n"
  "tay áo dài. Quần jogger đen bó ống, chân đi giày thể thao đen.\n"
  "Hai bàn tay đeo GĂNG TAY DA ĐEN ôm sát.\n"
  "Quần áo tối màu, không nhãn hiệu.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_THUG2_PORTRAIT"),
 ("REF_PLANNER_FULL", "WEDDING PLANNER — VEST ĐEN ĐIỀU PHỐI",
  "Trạng thái duy nhất.\nDùng: S20",
  "Người phụ nữ ở ẢNH 1, 35 tuổi. Bộ vest đen ôm dáng: blazer cài một cúc, quần âu đen ống đứng,\n"
  "bên trong là áo thun đen cổ tròn. Chân đi giày bệt bít mũi màu đen.\n"
  "Đeo TAI NGHE HEADSET mảnh có micro nhỏ trước miệng, dây chạy xuống hộp điều khiển kẹp ở thắt lưng.\n"
  "Trên tay ôm một BÌA KẸP HỒ SƠ MÀU ĐEN (không đọc được chữ).\n"
  "Quần áo gọn gàng, tối màu, kiểu người hậu trường.\nTRANG SỨC: đồng hồ dây silicon đen ở cổ tay TRÁI.",
  "REF_PLANNER_PORTRAIT"),
 ("REF_GRANDMA_FULL", "GRANDMOTHER HALE — ÁO LỤA + XE LĂN NHẸ",
  "Trạng thái duy nhất: bà ngồi xe lăn nhẹ suốt tiệc cưới.\nDùng: S20 · S21",
  "Người phụ nữ ở ẢNH 1, 89 tuổi, NGỒI TRONG MỘT CHIẾC XE LĂN NHẸ khung nhôm bạc bọc đệm xám,\n"
  "bánh nhỏ, tay vịn bọc da — xe sạch và mới, KHÁC HẲN chiếc xe lăn bệnh viện gỉ sét của nhân vật khác.\n"
  "Mặc bộ váy lụa dài màu XANH PHẤN cổ tròn cài kín, tay dài; ngoài khoác áo len mỏng màu ngà.\n"
  "Trên đùi phủ một tấm khăn len mỏng màu ngà. Chân đi giày bệt da mềm màu kem.\n"
  "TRANG SỨC — đúng hai món: chuỗi ngọc trai ngắn ở cổ và khuyên tai ngọc trai nhỏ.",
  "REF_GRANDMA_PORTRAIT"),
 ("REF_GERALD_TUXEDO_FULL", "GERALD HALE — TUXEDO NHÀ TRAI",
  "Trạng thái duy nhất.\nDùng: S20 · S21 · S22 · S23 · S24",
  "Người đàn ông ở ẢNH 1, 62 tuổi, cao lớn. Bộ TUXEDO màu ĐEN ve satin cài một cúc, sơ mi trắng cổ cánh,\n"
  "NƠ ĐEN thắt sẵn, khăn túi ngực lụa trắng. Quần âu đen có dải satin dọc ống, giày da đen bóng lộn.\n"
  "Quần áo may đo cực đắt, phẳng phiu tuyệt đối.\n"
  "TRANG SỨC: đồng hồ vàng mặt to ở cổ tay TRÁI, nhẫn cưới vàng bản dày ở ngón áp út tay TRÁI,\n"
  "khuy măng sét vàng.",
  "REF_GERALD_PORTRAIT"),
 ("REF_SECURITY_FULL", "SECURITY CHIEF — VEST AN NINH",
  "Trạng thái duy nhất.\nDùng: S21 · S22",
  "Người đàn ông ở ẢNH 1, 47 tuổi, vai rất rộng. Bộ vest đen bó sát cài một cúc, sơ mi trắng cổ cứng,\n"
  "cà vạt đen bản nhỏ. Quần âu đen, giày da đen đế bằng.\n"
  "Tai phải có TAI NGHE XOẮN DÂY TRONG SUỐT chạy xuống cổ áo. Trên ve áo trái có huy hiệu tròn kim loại nhỏ.\n"
  "Quần áo tối màu, gọn, kiểu đồng phục an ninh sự kiện.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_SECURITY_PORTRAIT"),
 ("REF_OFFICER_FULL", "POLICE OFFICER — ĐỒNG PHỤC CẢNH SÁT",
  "Trạng thái duy nhất.\nDùng: S23",
  "Người phụ nữ ở ẢNH 1, 31 tuổi. Đồng phục cảnh sát thành phố màu XANH ĐEN: áo sơ mi đồng phục tay ngắn\n"
  "cài kín có cầu vai, quần cùng màu. Bên ngoài mặc ÁO GILÊ CHỐNG ĐẠN MỎNG màu đen.\n"
  "Thắt lưng công vụ da đen bản to có bao đựng còng tay, KHÔNG có súng lộ ra.\n"
  "Bộ đàm nhỏ gài ở cầu vai TRÁI. Phù hiệu kim loại hình khiên trên ngực trái (không đọc được chữ).\n"
  "Chân đi bốt da đen cao cổ.\nTRANG SỨC: KHÔNG đeo gì cả.",
  "REF_OFFICER_PORTRAIT"),
 ("REF_MOORE_FULL", "DETECTIVE MOORE — MĂNG TÔ XÁM",
  "Trạng thái duy nhất.\nDùng: S23",
  "Người đàn ông ở ẢNH 1, 54 tuổi, đậm người. Áo măng tô len màu XÁM THAN dài quá gối mặc mở,\n"
  "bên trong là sơ mi xanh nhạt và cà vạt nâu thắt lỏng, quần âu nâu sẫm.\n"
  "Chân đi giày da nâu đế dày đã mòn. Trên tay cầm một CUỐN SỔ TAY BÌA CỨNG MÀU ĐEN gập lại.\n"
  "Quần áo cũ, nhàu tự nhiên, không hàng hiệu.\nTRANG SỨC: nhẫn cưới vàng đã mòn ở ngón áp út tay TRÁI.",
  "REF_MOORE_PORTRAIT"),
 ("REF_CRANE_FULL", "BOARD CHAIRMAN CRANE — SMOKING",
  "Trạng thái duy nhất.\nDùng: S22 · S23",
  "Người đàn ông ở ẢNH 1, 67 tuổi, cao gầy. Bộ SMOKING màu ĐEN cổ satin cài một cúc, sơ mi trắng cổ cánh,\n"
  "nơ đen thắt tay. Quần âu đen dải satin, giày da đen bóng lộn.\n"
  "Trên tay cầm một chiếc ÁO KHOÁC DẠ MÀU ĐEN gấp vắt qua cẳng tay.\n"
  "Quần áo may đo cực đắt, cổ điển.\nTRANG SỨC: khuy măng sét vàng và đồng hồ vàng mỏng ở cổ tay TRÁI.",
  "REF_CRANE_PORTRAIT"),
 ("REF_REPORTER_FULL", "REPORTER — ÁO KHOÁC ĐỎ",
  "Trạng thái duy nhất.\nDùng: S24",
  "Người phụ nữ ở ẢNH 1, 29 tuổi. Áo khoác dạ màu ĐỎ TƯƠI cổ bẻ dài quá hông cài một cúc, bên trong áo thun đen,\n"
  "quần âu đen ống đứng. Chân đi bốt da đen cao cổ gót vuông.\n"
  "Trên tay cầm một chiếc MICRO CẦM TAY hình trụ màu đen có khối vuông ở đầu (KHÔNG có chữ trên khối vuông).\n"
  "Quần áo mới, nổi bật, kiểu lên hình.\nTRANG SỨC — đúng hai món: khuyên tai vàng nhỏ và đồng hồ dây kim loại ở cổ tay TRÁI.",
  "REF_REPORTER_PORTRAIT"),
 ("REF_GUEST1_COMLE_FULL", "GUEST ONE — COMPLE DỰ CƯỚI SÁNG",
  "Bộ dự đám cưới buổi sáng của Maya.\nDùng: S1",
  "Người đàn ông ở ẢNH 1, 57 tuổi. Bộ vest hai mảnh màu XÁM BẠC cài hai cúc, sơ mi trắng, cà vạt lụa xám bạc.\n"
  "Quần âu cùng bộ, giày da đen bóng buộc dây.\n"
  "Quần áo tươm tất kiểu trung lưu, không quá đắt.\nTRANG SỨC: đồng hồ dây da nâu ở cổ tay TRÁI.",
  "REF_GUEST1_PORTRAIT"),
 ("REF_GUEST1_TUXEDO_FULL", "GUEST ONE — TUXEDO DỰ TIỆC",
  "Bộ dự đám cưới nhà Hale.\nDùng: S21 · S22 · S23",
  "Người đàn ông ở ẢNH 1, 57 tuổi. Bộ TUXEDO màu ĐEN ve satin cài một cúc, sơ mi trắng cổ cánh, nơ đen.\n"
  "Quần âu đen dải satin dọc ống, giày da đen bóng lộn.\n"
  "Quần áo đắt tiền, mới.\nTRANG SỨC: đồng hồ dây da nâu ở cổ tay TRÁI.",
  "REF_GUEST1_PORTRAIT"),
 ("REF_GUEST2_AOLUA_FULL", "GUEST TWO — ÁO LỤA DỰ CƯỚI SÁNG",
  "Bộ dự đám cưới buổi sáng của Maya.\nDùng: S1",
  "Người phụ nữ ở ẢNH 1, 51 tuổi. Áo lụa màu XANH CỔ VỊT cổ tròn cài kín tay lỡ, chân váy xoè nhẹ cùng tông\n"
  "dài quá gối. Chân đi giày bít mũi gót thấp màu đen.\n"
  "Trên tay cầm một chiếc TÚI VẢI NHỎ màu đen quai ngắn.\n"
  "Quần áo tươm tất kiểu trung lưu.\nTRANG SỨC — đúng hai món: khuyên tai vàng bản tròn và một chiếc vòng tay\n"
  "vàng mảnh ở cổ tay PHẢI.",
  "REF_GUEST2_PORTRAIT"),
 ("REF_GUEST2_DAHOI_FULL", "GUEST TWO — VÁY DẠ HỘI",
  "Bộ dự đám cưới nhà Hale.\nDùng: S21 · S22 · S23",
  "Người phụ nữ ở ẢNH 1, 51 tuổi. Váy dạ hội dài chấm đất bằng nhung màu XANH ĐÊM, tay lỡ, cổ tròn kín,\n"
  "dáng suông rủ. Chân đi giày cao gót bít mũi màu đen.\n"
  "Trên tay cầm một chiếc CLUTCH NHUNG ĐEN nhỏ.\n"
  "Quần áo đắt tiền, trang trọng.\nTRANG SỨC — đúng hai món: khuyên tai vàng bản tròn to và vòng tay vàng ở cổ tay PHẢI.",
  "REF_GUEST2_PORTRAIT"),
]:
    F(_rid, _lb, _ds, _bd, _pt)
