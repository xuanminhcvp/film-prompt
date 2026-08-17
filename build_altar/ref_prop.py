# -*- coding: utf-8 -*-
"""REF đạo cụ chủ chốt."""
from lib import ref, PROP_HEAD

R = []
D = lambda rid, label, desc, body: R.append(ref(rid, label, desc, PROP_HEAD + body))

D("REF_PROP_TIEN", "Xấp tiền mười một nghìn đô",
  "ĐẠO CỤ LƯU ĐỘNG — số tiền Vanessa ném vào mặt Maya giữa nhà thờ (S1), và cũng chính xấp tiền đó Maya trả lại "
  "cho Ryan trên bậc thềm bốn tuần sau (S24). Vật gieo-trả của cả phim.\nDùng: S1 · S24",
  "MỘT XẤP TIỀN MẶT gồm mười một cọc tiền giấy một trăm đô la Mỹ, mỗi cọc bó bằng một dải giấy trắng trơn\n"
  "quấn ngang giữa (dải giấy KHÔNG có chữ, KHÔNG có số). Các cọc xếp chồng thành hai hàng thấp, hơi xô lệch,\n"
  "vài tờ ở cọc trên cùng bị gập mép.\n"
  "Tiền là giấy bạc đã qua lưu thông: hơi mềm, có nếp gấp mờ, màu xanh xám ngả vàng nhẹ, KHÔNG mới cứng.\n"
  "Hoa văn trên tờ tiền vẽ ở mức nhìn xa: thấy rõ đó là tiền đô la Mỹ nhưng KHÔNG đọc được chữ hay số sê-ri nào.\n"
  "Cạnh xấp tiền đặt một chiếc PHONG BÌ GIẤY TRẮNG dày đã bóc nắp, nằm sấp.")

D("REF_PROP_HOPDONG", "Bản hợp đồng mười hai tháng",
  "ĐẠO CỤ LƯU ĐỘNG — bản hợp đồng Adrian đưa cho Maya ở hàng ghế cuối nhà thờ và cô ký lên lưng cuốn thánh ca.\n"
  "Dùng: S4",
  "MỘT TẬP GIẤY A4 gồm ba tờ rời đặt chồng hơi lệch nhau trên mặt bàn, giấy trắng dày, mép cắt sắc.\n"
  "Tờ trên cùng in chữ đen mật độ vừa phải, chia thành các đoạn đánh số 1, 2, 3, 4 nhìn thấy rõ hình khối chữ\n"
  "nhưng CHỮ NHỎ KHÔNG ĐỌC ĐƯỢC NỘI DUNG — trừ đúng MỘT DÒNG TIÊU ĐỀ in đậm ở đầu trang, chữ in hoa serif đen,\n"
  "ghi chính xác `TWELVE MONTH AGREEMENT`, in rõ ràng và sắc nét, KHÔNG nhoè, KHÔNG sai chính tả.\n"
  "Cuối tờ trên cùng có hai dòng kẻ chân chữ ký còn TRỐNG, chưa ai ký.\n"
  "Bên cạnh tập giấy đặt một cây BÚT MÁY màu đen thân trơn, nắp đã mở, đầu bút hướng về phía tập giấy.")

D("REF_PROP_HOPDONGRACH", "Tờ hợp đồng đã xé đôi",
  "ĐẠO CỤ — chính bản hợp đồng đó, đã bị xé làm đôi, Adrian đặt xuống trước mặt Maya và mẹ cô ở phòng bệnh.\n"
  "Dùng: S25",
  "CHÍNH TẬP GIẤY A4 ba tờ đó nhưng ĐÃ BỊ XÉ LÀM ĐÔI theo chiều dọc: hai nửa đặt cạnh nhau trên mặt bàn,\n"
  "mép xé lởm chởm và xù sợi giấy, hai nửa lệch nhau chừng hai đốt ngón tay nên đường xé nhìn rất rõ.\n"
  "Nửa bên trái còn thấy phần đầu của dòng tiêu đề in hoa serif đen `TWELVE`, nửa bên phải thấy phần còn lại\n"
  "`MONTH AGREEMENT` — ghép lại đọc đúng thành `TWELVE MONTH AGREEMENT`, in rõ nét, KHÔNG nhoè.\n"
  "Phần chữ nhỏ còn lại chỉ thấy hình khối, KHÔNG đọc được.\n"
  "Ở chân nửa bên phải có một CHỮ KÝ VIẾT TAY bằng mực đen, nét chảy, KHÔNG đọc ra tên.")

D("REF_PROP_NHAN", "Nhẫn cưới vàng mỏng của Helen",
  "ĐẠO CỤ — chiếc nhẫn cưới bốn mươi năm của mẹ Maya, thứ cô mang đi cầm để mua thêm thời gian.\nDùng: S3",
  "MỘT CHIẾC NHẪN VÀNG TRƠN dành cho nữ, bản rất mảnh (chừng hai milimét), vàng vàng ấm đã xỉn màu,\n"
  "bề mặt CHI CHÍT VẾT XƯỚC LI TI và mòn dẹt ở mặt dưới vì đeo bốn mươi năm không tháo.\n"
  "Nhẫn đặt nằm nghiêng dựa vào một mép gờ nhỏ trên mặt bàn gỗ để thấy được cả vành ngoài lẫn lòng trong.\n"
  "KHÔNG đá quý, KHÔNG hoa văn, KHÔNG chữ khắc đọc được.\n"
  "Cạnh chiếc nhẫn đặt một chiếc TÚI NHUNG NHỎ MÀU ĐỎ SẪM đã sờn, miệng túi mở, dây rút buông ra.")

D("REF_PROP_HOSO", "Phong bì phim X-quang giám định",
  "ĐẠO CỤ LƯU ĐỘNG — hồ sơ giám định phương tiện Maya tìm thấy trong ngăn kéo, bằng chứng dây phanh bị cắt.\n"
  "Dùng: S11",
  "MỘT PHONG BÌ GIẤY KRAFT khổ lớn màu nâu vàng, dày, đã cũ và quăn góc, nắp phong bì mở, miệng phong bì\n"
  "hơi banh ra để lộ mép của một tấm ảnh bên trong.\n"
  "Trên mặt phong bì có một Ô CHỮ NHẬT IN SẴN màu đen, bên trong ghi đúng một dòng chữ in hoa sans-serif đen\n"
  "`FORENSIC VEHICLE INSPECTION`, in rõ ràng sắc nét, KHÔNG nhoè, KHÔNG sai chính tả. KHÔNG có dòng chữ nào khác.\n"
  "Rút ra một phần khỏi phong bì và đặt chồng lên nó là MỘT TẤM ẢNH CHỤP CẬN cỡ 20x25cm: ảnh một ĐOẠN ỐNG DẦU\n"
  "PHANH bằng kim loại bện màu tối trên nền vải trắng, ống bị CẮT ĐỨT với MẶT CẮT PHẲNG, THẲNG VÀ SẮC như\n"
  "cắt bằng kìm — tuyệt đối KHÔNG tưa, KHÔNG rách sợi. Vết cắt là thứ sắc nét nhất trong khung.")

D("REF_PROP_VONGCO", "Vòng cổ kim cương nhà Hale",
  "ĐẠO CỤ LƯU ĐỘNG — viên kim cương hai triệu đô Vanessa tự gài vào túi Maya để vu trộm, và cũng là vật trên\n"
  "màn hình an ninh khi sự thật bật lên.\nDùng: S21 · S23",
  "MỘT DÂY CHUYỀN KIM CƯƠNG cao cấp đặt xoè trên mặt bàn: dây là một hàng đá tấm nhỏ gắn liền nhau trên nền\n"
  "bạch kim sáng, ở giữa buông xuống MỘT VIÊN KIM CƯƠNG CHÍNH cắt giọt nước rất lớn (cỡ bằng đầu ngón tay út),\n"
  "trong vắt, bắt sáng thành nhiều tia nhỏ.\n"
  "Dây được thả thành hình bầu dục hơi lộn xộn, khoá móc nhỏ nằm ở mép ngoài.\n"
  "Cạnh đó đặt một HỘP NHUNG MÀU XANH ĐÊM đã mở nắp, lòng hộp lót nhung cùng màu có rãnh đặt dây CÒN TRỐNG.\n"
  "KHÔNG có chữ, KHÔNG có logo trên hộp.")

D("REF_PROP_THONGBAO", "Lệnh trục xuất bốn tiếng",
  "ĐẠO CỤ — tờ lệnh phó cảnh sát trưởng tống đạt ở cửa nhà cổng.\nDùng: S16",
  "MỘT TỜ GIẤY A4 MÀU VÀNG CANARY dày, đặt ngửa trên mặt bàn, mép dưới hơi cong lên.\n"
  "Trên đầu tờ giấy có một khối chữ in hoa serif đen ghi đúng một dòng `NOTICE TO VACATE`, in rõ ràng và sắc nét,\n"
  "KHÔNG nhoè, KHÔNG sai chính tả. Phía dưới là các dòng chữ nhỏ và vài ô kẻ khung để điền — thấy hình khối chữ\n"
  "nhưng KHÔNG đọc được nội dung.\n"
  "Góc dưới bên phải có một DẤU MỰC TRÒN màu xanh đóng hơi lệch và một chữ ký tay bằng mực xanh, KHÔNG đọc ra tên.\n"
  "Giấy còn mới, có một nếp gấp ngang chính giữa.")

D("REF_PROP_BIENTEN", "Biển tên đầu giường bệnh",
  "ĐẠO CỤ — tấm biển cũ ở chân giường số 12, thứ Adrian đưa ra ở cảnh cuối để Maya hiểu anh là ai.\nDùng: S25",
  "MỘT TẤM BIỂN TÊN BỆNH NHÂN kiểu cũ: khung nhựa màu trắng ngà đã ố vàng, hình chữ nhật nằm ngang cỡ bằng\n"
  "bàn tay rưỡi, bốn góc bo tròn, có hai lỗ bắt vít ở hai đầu và vết xước dài ở mặt nhựa.\n"
  "Trong khung là một TẤM THẺ GIẤY CỨNG đã ngả vàng, in sẵn hai dòng chữ in hoa sans-serif màu đen,\n"
  "in rõ ràng và sắc nét, KHÔNG nhoè, KHÔNG sai chính tả:\n"
  "dòng trên ghi `UNIDENTIFIED`; dòng dưới cỡ nhỏ hơn ghi `BED 12`.\n"
  "KHÔNG có thêm bất kỳ dòng chữ, số hay ký hiệu nào khác. Mép thẻ giấy có một vết ố tròn màu nâu nhạt.")
