# THƯ VIỆN DỰNG CHUNG — AISLE SEVEN (bước 1 + bước 2)

Mọi agent làm phim này PHẢI dùng đúng tên/mã dưới đây. Không tự đặt mã mới.
Dự án: `/Users/may1/Desktop/grokpipe/PIPELINE-AISLE-SEVEN.project/` · kịch bản gốc: `KICH-BAN.md` (KHÔNG sửa).
Skill: `/Users/may1/Desktop/grokpipe/.claude/skills/skills-film/` (SKILL.md + references/). Đọc file được chỉ định trước khi viết.
Chỉ dùng python: `./.venv/bin/python3` (chạy từ `/Users/may1/Desktop/grokpipe`).

## 0. Bối cảnh phim
Drama Mỹ hiện đại. Keisha Dawson (nhân viên sàn siêu thị Grayway) mở một chai nước cam 3$19 cho ông lão Walter đang tụt đường huyết trên sàn aisle seven → bị Pike sa thải với chữ "theft" → mất bảo hiểm, đi lau nhà 11$/giờ → Walter hoá ra là Walter Gray, người sáng lập chuỗi → Keisha thi vào Fellowship, làm dự án Reach and Rest, phát hiện Pike sửa số, tự công bố số đúng → một năm sau là giám đốc vận hành vùng, viết chính sách Assist First.
Thoại phim: tiếng Anh giọng Mỹ, GIỮ NGUYÊN 100% từng chữ trong KICH-BAN.md. Mọi văn bản khác (label, goc, pose, prompt, desc) viết tiếng Việt.

## 1. NHÂN VẬT — tên thoại → mã REF
Tên trong `text`/`goc`/`pose.who` phải ĐÚNG như tên đứng đầu dòng thoại trong kịch bản (viết HOA).

| Tên thoại | Portrait | Mô tả cố định (dùng cho mọi prompt) |
|---|---|---|
| KEISHA | REF_KEISHA_PORTRAIT ✅ đã có ảnh | nữ Mỹ gốc Phi 31 tuổi, da nâu ấm, tóc đen xoăn tít búi cao gọn trên đỉnh đầu, KHUYÊN TAI NGỌC TRAI NHỎ (dấu riêng, mọi bộ đồ đều thấy) |
| WALTER | REF_WALTER_PORTRAIT ✅ | nam da trắng 78 tuổi, tóc bạc trắng dày hất ngược, mắt xanh xám, mặt nhiều nếp nhăn sâu, cạo râu sạch |
| PIKE | REF_PIKE_PORTRAIT ✅ | nam da trắng 42 tuổi, tóc nâu sẫm vuốt hất, râu quai nón nâu rậm tỉa gọn, mắt xanh xám |
| ELAINE | REF_ELAINE_PORTRAIT ✅ | nữ da trắng 52 tuổi, tóc nâu sẫm thẳng ngang vai rẽ ngôi lệch, khuyên đinh vàng nhỏ, con gái Walter |
| LORETTA | REF_LORETTA_PORTRAIT | nữ Mỹ gốc Phi 60 tuổi, mẹ Keisha; tóc ngắn xoăn tự nhiên điểm bạc; kính lão gọng nâu; mặt sắc, ấm, mệt nhưng kiêu hãnh; tiểu đường + tim |
| DENISE | REF_DENISE_PORTRAIT | nữ gốc Latin 33 tuổi, thu ngân quầy 4, mẹ đơn thân; tóc đen thẳng cột đuôi ngựa thấp; mặt tròn, hay lo |
| RANDALL | REF_RANDALL_PORTRAIT | nam da trắng 56 tuổi, thanh tra vùng; gầy, tóc muối tiêu cắt ngắn, kính không gọng, cầm bìa kẹp giấy |
| SHOPPER ONE | REF_SHOPPERONE_PORTRAIT | nữ da trắng 48 tuổi, khách; tóc vàng nhuộm buộc thấp, mặt cau, áo khoác gió |
| SHOPPER TWO | REF_SHOPPERTWO_PORTRAIT | nữ da trắng 20 tuổi (NGƯỜI LỚN, con gái Shopper One); tóc nâu dài, tay cầm điện thoại |
| PHARMACIST | REF_PHARMACIST_PORTRAIT | nam gốc Nam Á 45 tuổi, dược sĩ; tóc đen ngắn, kính gọng đen, áo blouse trắng |
| RECRUITER | REF_RECRUITER_PORTRAIT | nữ da trắng 47 tuổi, nhân viên tuyển dụng; tóc nâu đỏ ngắn, cardigan, giọng mệt nhưng tử tế |
| PROCTOR | REF_PROCTOR_PORTRAIT | nam Mỹ gốc Phi 60 tuổi, giám thị; tóc bạc cắt sát, sơ mi cà vạt, nghiêm |
| CANDIDATE ONE | REF_CANDIDATEONE_PORTRAIT | nam da trắng 28 tuổi, thí sinh; tóc nâu vuốt gel, tự tin, sơ mi xanh nhạt |
| CANDIDATE TWO | REF_CANDIDATETWO_PORTRAIT | nữ gốc Á 30 tuổi, thí sinh; tóc đen thẳng ngang vai, blazer xám |
| COLIN | REF_COLIN_PORTRAIT | nam da trắng 36 tuổi, quy hoạch vùng 8 năm; tóc vàng cát cắt gọn, KÍNH GỌNG MỎNG kim loại, cạo râu sạch, gầy (phải KHÁC HẲN Pike: không râu, tóc sáng) |
| BOARD MEMBER | REF_BOARDMEMBER_PORTRAIT | nam Mỹ gốc Phi 66 tuổi, thành viên HĐQT; tóc bạc, vest xám đậm |
| MANAGER | REF_MANAGER_PORTRAIT | nam gốc Latin 40 tuổi, quản lý cửa hàng (S25); tóc đen ngắn, ria mép mỏng, sơ mi cộc tay xanh Grayway + cà vạt |
| JONAS | REF_JONAS_PORTRAIT | nam Mỹ gốc Phi 20 tuổi, nhân viên sàn mới 7 tuần; tóc đen cắt fade, mặt non, áo polo Grayway |

Quần chúng nền (khách siêu thị, thí sinh khác, học viên, thành viên HĐQT khác, khách căng-tin, nhân viên y tế…) KHÔNG có REF, KHÔNG được khai trong `goc`/`pose.who`; chỉ tả bằng chữ trong prompt SF (bước 3).

## 2. TRANG PHỤC — mã REF FULL và scene dùng
Mỗi thẻ FULL: 9:16, `refs.chars = [REF_<TÊN>_PORTRAIT]`, prompt KHÔNG tả lại mặt ("Gương mặt giống ẢNH portrait tham chiếu"), `desc` kết bằng dòng riêng `Dùng: S1 · S2`.

| Mã FULL | Ai | Bộ đồ | Dùng |
|---|---|---|---|
| REF_KEISHA_UNIFORM_FULL | KEISHA | đồng phục Grayway: áo polo xanh lá rừng (forest green) đã bạc nhẹ vì giặt nhiều nhưng SẠCH, thẻ tên "KEISHA" gài ngực trái, quần đen công sở, giày sneaker đen mòn gót; khuyên ngọc trai | S1 · S2 · S3 · S4 · S5 |
| REF_KEISHA_THUONG_FULL | KEISHA | đồ ở nhà nghèo-sạch: áo thun cổ tròn xám than sờn cổ, cardigan len mỏng màu be cũ, quần jean bạc, tất, KHÔNG giày; khuyên ngọc trai + dây chuyền mảnh mặt chữ thập nhỏ (áo cổ tròn nên thấy) | S6 · S8 · S10 · S11 · S16 |
| REF_KEISHA_TUTE_FULL | KEISHA | bộ tử tế đi phỏng vấn/đi thi: sơ mi trắng cài kín (hơi cũ, ủi phẳng), quần tây đen, giày bệt đen; khuyên ngọc trai, đồng hồ dây da nâu cổ tay TRÁI | S7 · S12 · S13 |
| REF_KEISHA_CONGSO1_FULL | KEISHA | công sở mới (Fellowship): áo blouse lụa xanh navy, quần tây xám, giày bệt đen; khuyên ngọc trai + đồng hồ da nâu tay TRÁI; thẻ nhân viên Gray Foods đeo dây cổ | S14 · S15 · S17 · S18 |
| REF_KEISHA_CONGSO2_FULL | KEISHA | áo len cổ lọ mỏng màu rượu vang, quần tây đen, giày bệt; khuyên ngọc trai + đồng hồ; thẻ Gray Foods | S19 · S20 · S21 |
| REF_KEISHA_BLAZER_FULL | KEISHA | blazer đen ôm + áo trong trắng, quần tây đen, giày gót thấp; khuyên ngọc trai + đồng hồ | S22 · S23 |
| REF_KEISHA_GIAMDOC_FULL | KEISHA | một năm sau, giám đốc: áo blazer màu kem sang, áo trong đen, quần tây đen, thẻ Gray Foods; khuyên ngọc trai + đồng hồ da nâu | S24 · S25 |
| REF_WALTER_AOVUON_FULL | WALTER | "gardening coat": áo khoác vải bạt màu ô-liu cũ sờn, dính vết đất khô ở gấu và khuỷu, dưới là áo sơ mi flannel kẻ ca-rô nâu, quần kaki bạc, giày da nâu cũ; sắc mặt XÁM (đang tụt đường) | S1 · S2 |
| REF_WALTER_BENHVIEN_FULL | WALTER | áo bệnh nhân xanh nhạt hoa văn nhỏ, chăn trắng, băng dán kim truyền mu bàn tay TRÁI, tóc bạc rối; sắc mặt hồng lại | S9 |
| REF_WALTER_KHACH_FULL | WALTER | old-money giản dị: áo khoác tweed nâu xám, áo len cổ tròn xanh navy, sơ mi trắng bên trong, quần vải xám, giày da nâu đánh bóng, gậy chống gỗ | S10 · S11 · S24 |
| REF_WALTER_VANPHONG_FULL | WALTER | cardigan len xám đậm cài cúc, sơ mi trắng cổ mở, quần tây than, giày da | S12 |
| REF_PIKE_QUANLY_FULL | PIKE | quản lý cửa hàng: sơ mi trắng dài tay, cà vạt xanh lá rừng Grayway, thẻ tên "D. PIKE — STORE MANAGER" ngực trái, quần tây đen, thắt lưng đen, bộ đàm gài hông | S2 · S3 |
| REF_PIKE_VUNG_FULL | PIKE | quản lý vùng: blazer xanh navy, sơ mi xanh nhạt, không cà vạt, thẻ Gray Foods đeo dây, quần tây | S18 · S21 |
| REF_ELAINE_BENHVIEN_FULL | ELAINE | áo khoác trench be, áo len xám, quần tây đen, túi xách da nâu | S9 |
| REF_ELAINE_CONGSO1_FULL | ELAINE | vest nữ xám than, áo lụa trắng, quần tây, giày gót vừa; khuyên đinh vàng | S14 · S15 · S17 |
| REF_ELAINE_CONGSO2_FULL | ELAINE | váy công sở xanh navy dài gối + blazer cùng màu, khuyên đinh vàng | S19 · S22 |
| REF_LORETTA_NHA1_FULL | LORETTA | váy nhà (housedress) hoa nhí xanh nhạt đã bạc, cardigan len nâu, dép nhà; kính lão treo dây trước ngực | S5 · S8 |
| REF_LORETTA_NHA2_FULL | LORETTA | áo len cổ tim màu tím than cũ, quần vải đen, khăn quàng mỏng; kính lão | S10 · S11 · S16 |
| REF_DENISE_UNIFORM_FULL | DENISE | đồng phục Grayway (polo xanh lá rừng + thẻ tên "DENISE"), quần đen, giày sneaker trắng | S1 · S3 · S4 (S2 không lên hình) |
| REF_RANDALL_SUIT_FULL | RANDALL | vest xám nhạt, cà vạt sọc, bìa kẹp giấy đen trên tay | S2 |
| REF_SHOPPERONE_FULL | SHOPPER ONE | áo khoác gió tím, quần jean, túi vải đeo vai | S1 |
| REF_SHOPPERTWO_FULL | SHOPPER TWO | hoodie xám, quần jean, điện thoại trên tay | S1 |
| REF_PHARMACIST_FULL | PHARMACIST | blouse trắng, thẻ tên, sơ mi xanh bên trong | S6 |
| REF_RECRUITER_FULL | RECRUITER | cardigan xanh rêu, áo trong trắng, kính đọc trên đầu | S7 |
| REF_PROCTOR_FULL | PROCTOR | sơ mi trắng, cà vạt đen, quần tây | S13 |
| REF_CANDIDATEONE_FULL | CANDIDATE ONE | sơ mi xanh nhạt xắn tay, quần kaki | S13 |
| REF_CANDIDATETWO_FULL | CANDIDATE TWO | blazer xám, áo trong đen | S13 |
| REF_COLIN_CONGSO1_FULL | COLIN | sơ mi trắng, gi-lê len xám, quần tây navy, thẻ Gray Foods, kính | S14 · S15 · S17 |
| REF_COLIN_CONGSO2_FULL | COLIN | sơ mi xanh nhạt xắn tay, cà vạt nới, quần tây, kính | S19 · S20 · S23 |
| REF_BOARDMEMBER_FULL | BOARD MEMBER | vest xám đậm, cà vạt đỏ đô | S22 |
| REF_MANAGER_FULL | MANAGER | sơ mi cộc tay xanh Grayway + cà vạt, thẻ "STORE MANAGER" | S25 |
| REF_JONAS_FULL | JONAS | polo xanh lá rừng Grayway mới tinh, thẻ tên "JONAS", quần đen | S25 |

## 3. ĐẠO CỤ CHỦ CHỐT
| Mã | Mô tả |
|---|---|
| REF_PROP_NUOCCAM_KIN | chai nước cam Grayway 16oz nhựa trong, nắp XANH LÁ, nhãn trắng chữ xanh lá "GRAYWAY 100% ORANGE JUICE", tem giá "$3.19"; đặt trên mặt bàn gỗ trơn, 1:1, góc 3/4, KHÔNG người/tay |
| REF_PROP_NUOCCAM_MO | y hệt chai trên nhưng ĐÃ MỞ NẮP, nắp đặt cạnh, mực nước vơi 1/4 |
(S25 chai nước lọc của Jonas: KHÔNG tạo REF, tả trong SF.)

## 4. ĐỊA ĐIỂM — mã thẻ, giờ, scene, sơ đồ & trục
Thẻ địa điểm nằm ở scene `REF`, id `REF_<NƠI>_<GIỜ>` (hậu tố giờ BẮT BUỘC thuộc: NGAY/SANG/TRUA/CHIEU = sáng · DEM/CHAPTOI/KHUYA/RANGSANG = tối). Thẻ mang `luatchung`; `refs.chars = []`; SF con trỏ `refs.bg` về thẻ. Thẻ là BỐI CẢNH TRỐNG KHÔNG NGƯỜI.
Ký hiệu trục: "SL" = screen left (nửa trái khung), "SR" = screen right. Trục KHÔNG BAO GIỜ đảo trong một scene.

| Mã thẻ | Scene | Gốc/biến thể | Sơ đồ 360° (Trái/Phải/Đối diện/Sau lưng tính từ MÁY QUAY CHUẨN) · zone · trục |
|---|---|---|---|
| REF_AISLE7_NGAY | S1 · S2 | GỐC cụm Grayway | Aisle seven, ban ngày, đèn huỳnh quang trắng. Máy chuẩn đứng ở ĐẦU aisle (phía quầy thu ngân) nhìn dọc vào trong. TRÁI: kệ NƯỚC ÉP/ĐỒ UỐNG (chai nước cam Grayway ở tầng ngang thắt lưng, biển "AISLE 7 · JUICE · BAKING · TEA" treo trên). PHẢI: kệ hàng khô (bột mì, trà, hộp bánh — bột & trà ở TẦNG TRÊN CÙNG ~1m8). ĐỐI DIỆN (cuối aisle): tủ mát cửa kính đựng TRỨNG/SỮA, sàn trước tủ có VŨNG NƯỚC LOANG (không cone). SAU LƯNG: lối đi chính + quầy thu ngân mờ. Sàn gạch vinyl trắng ngà vân xám. Zone: `đầu aisle` · `giữa aisle (chỗ Walter ngồi)` · `cuối aisle (tủ trứng)`. TRỤC: WALTER ngồi bệt lưng tựa kệ TRÁI, chân duỗi, giỏ nhựa đỏ có hộp trứng cạnh hông = SL. KEISHA quỳ/ngồi xổm đối diện ông, lưng về kệ PHẢI = SR. DENISE/PIKE/RANDALL tới từ đầu aisle (phía máy) đứng SR phía sau Keisha. |
| REF_AISLE7MOI_CHIEU | S24 | biến thể của REF_AISLE7_NGAY (bg→AISLE7_NGAY, khoá kiến trúc) | Một năm sau, chiều: THÊM ghế băng gỗ khung sắt sơn xanh lá đặt sát kệ PHẢI đúng chỗ Walter từng ngồi đối diện; bột mì & trà đã hạ xuống TẦNG NGANG KHUỶU TAY; sàn cuối aisle KHÔ, có thảm cao su xám trước tủ trứng. Zone như thẻ gốc + `ghế băng`. TRỤC: WALTER ngồi ghế băng SL, KEISHA ngồi cạnh/đứng SR. |
| REF_PHONGNGHI_NGAY | S3 · S25 | cùng toà Grayway (bg→AISLE7_NGAY, ĐỒNG BỘ PHONG CÁCH — phòng khác) | Phòng nghỉ nhân viên không cửa sổ: bàn formica xám 4 ghế nhựa giữa phòng; TRÁI: dãy tủ locker xám; ĐỐI DIỆN: bảng thông báo có poster Grayway + máy chấm công; PHẢI: tủ lạnh nhỏ, lò vi sóng, bình nước; SAU LƯNG: cửa ra sàn bán hàng (kính nhỏ). Zone: `bàn` · `cửa` · `tủ lạnh`. TRỤC S3: PIKE ngồi ghế SL (giấy trên bàn), KEISHA đứng/ngồi SR, DENISE ở cửa (nền, sau lưng máy → khi quay về cửa Denise SR xa). TRỤC S25: MANAGER ngồi SL, JONAS đứng SR, KEISHA vào từ cửa và đứng SR cạnh Jonas. |
| REF_TRAMXE_CHIEU | S4 | ngoại cảnh Grayway (bg→AISLE7_NGAY, CHỈ lấy màu thương hiệu xanh lá) | Trạm xe buýt trên vỉa hè trước bãi đỗ xe Grayway, chiều nắng xiên. Máy chuẩn đứng dưới lòng đường nhìn vào: TRÁI: mái che trạm bằng kính + ghế băng kim loại; ĐỐI DIỆN: bãi đỗ xe thưa và mặt tiền siêu thị xa với biển "GRAYWAY MARKET" chữ xanh lá; PHẢI: cột biển báo xe buýt + thùng rác; SAU LƯNG: lòng đường (xe buýt sẽ tới từ SR). Zone: `ghế trạm` · `vỉa hè`. TRỤC: KEISHA ngồi đầu ghế SL, DENISE chạy tới đứng rồi ngồi SR. |
| REF_BEPDAWSON_CHIEU | S11 | GỐC cụm nhà Dawson | Bếp căn hộ tầng 4 cũ, nhỏ, nghèo-sạch, chiều nắng vào. Máy chuẩn đứng ở CỬA BẾP nhìn vào: TRÁI: cửa sổ khung nhôm cũ rèm ren, dưới cửa sổ là BÀN ĂN gỗ vuông nhỏ (khăn trải nhựa hoa) kê sát tường + 3 ghế gỗ lệch bộ; ĐỐI DIỆN: bếp gas 4 lò cũ, nồi cơm, quầy formica; PHẢI: tủ lạnh trắng đầy nam châm + hoá đơn, giá thuốc nhỏ trên quầy (hộp thuốc Loretta); SAU LƯNG: cửa bếp mở ra hành lang căn hộ. Zone: `bàn ăn` · `bếp lò` · `cửa bếp`. TRỤC: LORETTA ghế đầu bàn phía bếp lò = SR; KEISHA ghế đối diện phía cửa sổ = SL; ghế khách (WALTER S11) cạnh bàn phía máy, giữa. |
| REF_BEPDAWSON_CHAPTOI | S5 | biến thể (bg→BEPDAWSON_CHIEU) | Chập tối, ĐÈN TẮT, chỉ ánh xanh xám cuối ngày qua cửa sổ + đèn hút mùi vàng nhỏ trên bếp. Cùng zone/trục. |
| REF_BEPDAWSON_DEM | S8 · S16 | biến thể (bg→BEPDAWSON_CHIEU) | Đêm, cửa sổ đen, một đèn trần huỳnh quang vàng + đèn bàn nhỏ trên quầy. Cùng zone/trục. |
| REF_CUADAWSON_CHIEU | S10 | cùng toà (bg→BEPDAWSON_CHIEU, ĐỒNG BỘ PHONG CÁCH — không copy đồ đạc) | Hành lang tầng 4 trước cửa căn hộ 4B, chiều. Máy chuẩn đứng trong hành lang: TRÁI: đầu cầu thang xuống (lan can sắt sơn nâu); ĐỐI DIỆN: cửa gỗ sơn xanh xám số "4B", chuông cửa; PHẢI: tường vôi vàng ố + cửa căn hộ khác; SAU LƯNG: hành lang kéo dài, cửa sổ nhỏ. Zone: `thềm cửa` · `đầu cầu thang`. TRỤC: WALTER đứng ngoài, phía cầu thang = SL (tay cầm túi giấy có chai nước cam); KEISHA đứng trong ngưỡng cửa = SR; LORETTA xuất hiện sau lưng Keisha trong nhà (SR sâu). |
| REF_HIEUTHUOC_NGAY | S6 | độc lập | Quầy dược của hiệu thuốc chuỗi Mỹ, ban ngày đèn trắng. Máy chuẩn đứng phía khách: TRÁI: đầu quầy có màn hình + máy tính tiền; ĐỐI DIỆN: quầy cao ngang ngực, phía sau là kệ trắng đầy túi thuốc trắng có ghim; PHẢI: kệ hàng OTC + biển "PICK UP"; SAU LƯNG: hàng khách xếp (nền). Zone: `quầy`. TRỤC: PHARMACIST sau quầy = SL, KEISHA trước quầy = SR. |
| REF_TUYENDUNG_NGAY | S7 | độc lập | Văn phòng nhỏ Eastside Staffing Agency, ban ngày. Máy chuẩn ở cửa: TRÁI: cửa kính mờ chữ "EASTSIDE STAFFING"; ĐỐI DIỆN: bàn làm việc gỗ ép + màn hình, tủ hồ sơ; PHẢI: cửa sổ rèm lá dọc, cây giả; SAU LƯNG: hành lang chờ. Zone: `bàn`. TRỤC: RECRUITER sau bàn = SL, KEISHA ghế khách = SR. |
| REF_PHONGBENH_NGAY | S9 | độc lập | Phòng bệnh 412 Mercy General, ban ngày. Máy chuẩn ở chân giường: TRÁI: cửa sổ rèm lá sáng; ĐỐI DIỆN: đầu giường bệnh, màn hình theo dõi, giá truyền; PHẢI: ghế khách bọc vinyl xanh, tủ đầu giường; SAU LƯNG: cửa phòng + hành lang. Zone: `giường` · `ghế khách`. TRỤC: WALTER nằm/nửa ngồi trên giường = SL, ELAINE ghế/đứng cạnh giường = SR. |
| REF_VPWALTER_NGAY | S12 | GỐC cụm Gray Foods Corporate | Văn phòng góc của Walter, ban ngày. Máy chuẩn ở cửa: TRÁI: tường kính nhìn ra thành phố; ĐỐI DIỆN: bàn gỗ óc chó lớn, ghế da; PHẢI: kệ sách gỗ, cửa; SAU LƯNG: cửa vào + hành lang kính. Vật liệu chung cả toà: sàn thảm xám xanh, tường trắng kem, gỗ óc chó, logo "GRAY FOODS" xanh lá thẫm. Zone: `bàn làm việc` · `ghế khách`. TRỤC: WALTER sau bàn = SL, KEISHA ghế khách = SR. |
| REF_PHONGTHI_NGAY | S13 | cùng toà (bg→VPWALTER_NGAY, ĐỒNG BỘ PHONG CÁCH) | Phòng thi: 5 hàng × 6 bàn học nhỏ, ban ngày. Máy chuẩn ở CUỐI phòng nhìn lên: ĐỐI DIỆN: bàn giám thị + bảng trắng + đồng hồ treo tường; TRÁI: cửa sổ rèm; PHẢI: cửa ra vào; SAU LƯNG: tường trống. Zone: `bàn giám thị` · `hàng giữa (chỗ Keisha)` · `cửa`. TRỤC: PROCTOR phía trước = SL; KEISHA bàn hàng 3 giữa; CANDIDATE ONE bàn hàng 3 bên PHẢI Keisha = SR; CANDIDATE TWO hàng 2 bên trái = SL. |
| REF_PHONGDINHHUONG_NGAY | S14 | cùng toà (bg→VPWALTER_NGAY) | Phòng định hướng lớn: bàn xếp chữ U, màn chiếu chữ "STORE OPERATIONS FELLOWSHIP", ban ngày. Máy chuẩn ở đáy chữ U: ĐỐI DIỆN: bục + màn chiếu; TRÁI/PHẢI: hai cánh bàn với học viên; SAU LƯNG: cửa đôi. Zone: `bục` · `bàn cánh phải (Keisha & Colin)`. TRỤC: ELAINE ở bục = SL; KEISHA ngồi cánh phải, COLIN ngồi ghế kề bên trái Keisha → trong cặp hai người: COLIN = SL, KEISHA = SR. |
| REF_PHONGHOP_NGAY | S17 · S19 | cùng toà (bg→VPWALTER_NGAY) | Phòng họp kính: bàn dài 10 ghế, màn hình đầu bàn, ban ngày. Máy chuẩn ở cửa (cuối bàn): ĐỐI DIỆN: màn hình + ghế đầu bàn; TRÁI: tường kính ra hành lang; PHẢI: tường trắng, bảng. Zone: `đầu bàn (màn hình)` · `giữa bàn`. TRỤC: ELAINE ghế đầu bàn dưới màn hình = giữa/xa; KEISHA đứng (S17) / ngồi (S19) bên PHẢI bàn = SR; COLIN ngồi bên TRÁI bàn đối diện = SL. |
| REF_PHONGHOIDONG_NGAY | S22 | cùng toà (bg→VPWALTER_NGAY) | Phòng HĐQT: bàn gỗ óc chó bầu dục 14 ghế da, tường ốp gỗ, cửa sổ lớn, ban ngày. Máy chuẩn ở cửa: ĐỐI DIỆN: đầu bàn + màn hình; TRÁI: cửa sổ; PHẢI: tường gỗ. Zone: `đầu bàn` · `dọc bàn`. TRỤC: KEISHA đứng đầu bàn = SR; BOARD MEMBER ngồi ghế đầu bên trái = SL; ELAINE ngồi cạnh Board Member phía xa = SL sâu. |
| REF_PHONGDULIEU_DEM | S20 | cùng toà (bg→VPWALTER_NGAY) | Phòng dữ liệu nhỏ, đêm: 2 bàn máy tính, 3 màn hình, máy in, chồng giấy, rèm hạ, đèn bàn. Máy chuẩn ở cửa: ĐỐI DIỆN: bàn máy tính sát tường; TRÁI: máy in + kệ hồ sơ; PHẢI: cửa sổ rèm hạ. Zone: `bàn máy tính` · `cửa`. TRỤC: KEISHA ngồi trước màn hình = SR; COLIN vào từ cửa (SL) rồi đứng cạnh, cúi xem = SL. |
| REF_HAMXE_DEM | S21 | cùng toà (bg→VPWALTER_NGAY, chỉ lấy tông màu) | Hầm xe bê tông, đêm, đèn tuýp trắng lạnh, vài xe. Máy chuẩn giữa lối: TRÁI: cột bê tông sơn số "P2"; ĐỐI DIỆN: dãy xe đỗ + xe sedan đen của Pike; PHẢI: cửa thang máy inox; SAU LƯNG: lối ra dốc. Zone: `cạnh xe Pike` · `cửa thang máy`. TRỤC: PIKE đứng cạnh xe = SL; KEISHA = SR. |
| REF_CANGTIN_NGAY | S23 | cùng toà (bg→VPWALTER_NGAY) | Căng-tin công ty 1 giờ 30 chiều, thưa người, cửa sổ lớn nắng. Máy chuẩn ở lối vào: ĐỐI DIỆN: cửa kính lớn; TRÁI: quầy tự phục vụ; PHẢI: dãy bàn 4 ghế. Zone: `bàn cạnh cửa sổ`. TRỤC: KEISHA ngồi bàn cạnh cửa sổ = SR (khay bánh mì gà chưa ăn); COLIN tới ngồi đối diện = SL. |
| REF_STORE12_NGAY | S15 | chi nhánh khác cùng chuỗi (bg→AISLE7_NGAY, ĐỒNG BỘ PHONG CÁCH — cửa hàng CŨ hơn, đèn vàng hơn, kệ thấp cũ) | Sàn bán hàng Grayway số 12: cửa hàng già 91 năm khu phố. Máy chuẩn ở lối vào chính: ĐỐI DIỆN: tủ mát sữa cuối lối đi với MẢNG SÀN MÒN bạc trắng 1m trước tủ (ẩm); TRÁI: aisle 4 (biển "AISLE 4 · TEA · FLOUR · DETERGENT") hàng chất TẦNG TRÊN CÙNG; PHẢI: quầy thu ngân + hành lang WC có GHẾ BĂNG GÃY một chân. Zone: `tủ sữa` · `aisle 4` · `ghế gãy`. TRỤC: ELAINE giữa; COLIN = SL; KEISHA = SR (Keisha di chuyển giữa các zone → shot đó khai `chuyen`). |
| REF_HANHLANG12_NGAY | S18 | cùng toà store 12 (bg→STORE12_NGAY, ĐỒNG BỘ PHONG CÁCH — hành lang sau) | Hành lang sau cửa hàng 12: tường gạch block sơn trắng ố, ban ngày đèn tuýp. Máy chuẩn giữa hành lang: TRÁI: cửa kho hai cánh + xe đẩy pallet; ĐỐI DIỆN: cửa văn phòng quản lý kính nhỏ; PHẢI: máy chấm công + bảng lịch; SAU LƯNG: cửa ra sàn. Zone: `hành lang`. TRỤC: PIKE = SL (tựa cửa văn phòng), KEISHA = SR (cầm bìa hồ sơ). |

## 5. QUY ƯỚC DỮ LIỆU BẢNG SHOT (bước 1)
Mỗi scene = 1 file patch JSON: `{ "name": ..., "script": ..., "sfs": [...], "shots": [...] }`.
- `name`: `"S<n> — <tên địa điểm tiếng Việt ngắn>"`.
- `script`: nguyên văn thoại của scene (copy đúng từ KICH-BAN.md, mỗi dòng `TÊN: câu`).
- **1 shot = 1 SF**. Shot `V-S<n>-<NN>` ↔ SF `SF-S<n>-<NN>` (NN hai chữ số 01, 02…). Nhịp lặng: `V-S<n>-B<k>` ↔ `SF-S<n>-B<k>`.
- SHOT: `{"id","sf","dur","text","goc","prompt":"","notes":"","vstatus":""}`. `dur` là SỐ NGUYÊN 10 hoặc 6 (Grok chỉ có 6s/10s). 10s chứa 21–31 từ tiếng Anh; 6s chứa ≤19 từ. Không được để 1 shot >31 từ (máy đo từ ÷ 3 ≤ dur + 0,5). Câu thoại quá dài (>31 từ) thì TÁCH tại ranh giới câu sang shot kế (cùng người nói, giữ nguyên chữ). ~90% shot là 10s với 2–4 lượt thoại. Shot có đứng lên/ngồi xuống/đi lại thì bớt số từ (dành 2–3s cho chuyển động).
- `text`: các dòng thoại nguyên văn `TÊN: câu\nTÊN: câu`. Nhịp lặng: `"[NHỊP] mô tả hành động ngắn tiếng Việt"`.
- `goc` (ghi trên SHOT và chép y hệt sang SF): 1 dòng "cỡ cảnh · ai NÉT · ai vai-gáy/mờ · ai quay lưng", NÊU ĐÍCH DANH TÊN THOẠI, khai CẢ người trong khung không nói. OTS phải ghi "OTS qua vai <TÊN>". KHÔNG tả cảnh/đạo cụ/thông số máy. KHÔNG khai quần chúng. Ví dụ: `"MCU · OTS qua vai KEISHA tiền cảnh phải · WALTER NÉT ngồi bệt tựa kệ trái"`.
- SF: `{"id","label","goc","pose","prompt":"","refs":{"chars":[...],"bg":"<mã thẻ địa điểm>"},"status":"proposed","notes":""}`.
  - `label`: ngắn tiếng Việt, VD `"S1-07 · KEISHA nắm tay WALTER đang run"`; nhịp lặng thêm tag `[NHỊP]`.
  - `refs.chars`: portrait + đúng bộ FULL của MỖI người trong khung (kể cả vai/gáy tiền cảnh); tối đa 4 người (8 mã). Đính thêm `REF_PROP_NUOCCAM_KIN`/`_MO` khi chai nước cam trong khung.
  - `pose` là DICT: `{"zone": "<zone theo mục 4>", "who": {"KEISHA": "quỳ một gối đối diện Walter", "WALTER": "ngồi bệt lưng tựa kệ trái, chân duỗi"}, "dist": "gần, cách 0,5 m", "hands": {"KEISHA": "chai nước cam mở nắp tay phải", "WALTER": "tay run trên đùi"}}`. Key của `who` = tên thoại của MỌI người có mặt trong khung (kể cả nền mờ có REF). Shot mang di chuyển đổi zone: thêm `"chuyen": true` vào dict pose của SF ĐÍCH (SF của shot đó). Hồi tưởng: `"hoituong": true`.
- Nhịp lặng (`[NHỊP]`): MỖI SCENE mở bằng `-B1` (khung rộng giới thiệu địa điểm, CÓ NGƯỜI trong khung — nhân vật chính đang ở đó, khai `goc` bình thường), thêm 0–2 nhịp giữa cảnh ở đỉnh cảm xúc / nhảy thời gian. Nhịp lặng dur 10 (hoặc 6). Đích toàn phim ~12% shot là nhịp.
- Góc máy: 75–80% CU/MCU; góc rộng chỉ cho `-B1`/khép cảnh, KHÔNG gán thoại vào khung rộng. Cụm thoại ≥3 shot BẮT BUỘC có cặp OTS/reverse. Hai shot liền nhau phải khác góc ≥30° hoặc khác cỡ cảnh 2 bậc. Khung thoại trực tiếp phải có ≥2 người trong `pose.who` (trừ độc thoại/điện thoại).
- Continuity: SF là KHUNG ĐẦU clip → lấy trạng thái KẾT của shot trước. Thoại có mệnh lệnh đổi trạng thái ("Sit down", "Give me the pen") → SF ở trạng thái CHƯA làm. Rà 5 trục: xa/gần · đứng/ngồi · trước/sau · trái/phải (trục SL/SR mục 4) · TAY CẦM GÌ (chai nước cam, tờ giấy sa thải, bút, tiền 20$, thuốc, form, chồng báo cáo, khay bánh mì…). Tối đa 3 mối đổi zone/scene.
- Người nói phải có mặt trong `goc` của shot đó (rõ mặt hoặc vai/gáy). Không có thoại off-screen trừ khi thật sự cần; nếu cần thì ghi `TÊN (off-screen, ...)`.
- KHÔNG viết `prompt` (bước 3/4 làm sau). KHÔNG sửa một chữ thoại.
- Kiểm bằng máy sau khi ghi: `./.venv/bin/python3 sfboard/kiem-luat.py PIPELINE-AISLE-SEVEN.project --scene S<n>` và `./.venv/bin/python3 sfboard/kiem-noi-shot.py PIPELINE-AISLE-SEVEN.project S<n> --day-du`.

## 6. GHI VÀO BOARD
KHÔNG mở/sửa `sf-board.json` bằng tay. Ghi patch nhỏ rồi chạy:
`./.venv/bin/python3 sfboard/sua-board.py patch PIPELINE-AISLE-SEVEN.project <SCENE_ID> <patch.json>`
(scene chưa có thì tool tự tạo; các key lạ bị lọc — nên `chuyen`/`hoituong` phải nằm trong `pose` của SF, không nằm trên shot).
Thẻ REF (nhân vật/đạo cụ/địa điểm) patch vào scene `REF`.
