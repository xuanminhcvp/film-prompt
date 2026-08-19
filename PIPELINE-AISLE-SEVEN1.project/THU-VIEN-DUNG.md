# THƯ VIỆN DỰNG CHUNG — AISLE SEVEN (bước 1 + bước 2)

> Dựng lại từ đầu 2026-08-18 sau khi user chốt chân dung KEISHA (tóc bob thẳng,
> khuyên vàng thả giọt) và WALTER. Bản cũ nằm ở
> `.snapshots/2026-08-18-1500/`.

Mọi agent làm phim này PHẢI dùng đúng tên/mã dưới đây. Không tự đặt mã mới.
Dự án: `/Users/may1/Desktop/film-prompts/PIPELINE-AISLE-SEVEN1.project/` · kịch bản gốc: `KICH-BAN.md` (KHÔNG sửa).
Skill: `/Users/may1/Desktop/film-prompts/.claude/skills/skills-film/` (SKILL.md + references/). Đọc file được chỉ định trước khi viết.

## 0. Bối cảnh phim

Drama Mỹ hiện đại. Keisha Dawson (nhân viên sàn siêu thị Grayway) mở một chai nước
cam 3$19 cho ông lão Walter đang tụt đường huyết trên sàn aisle seven → bị Pike sa
thải với chữ "theft" → mất bảo hiểm, đi lau nhà 11$/giờ → Walter hoá ra là Walter
Gray, người sáng lập chuỗi → Keisha thi vào Fellowship, làm dự án Reach and Rest,
phát hiện Pike sửa số, tự công bố số đúng → một năm sau là giám đốc vận hành vùng,
viết chính sách Assist First.

Thoại phim: tiếng Anh giọng Mỹ, GIỮ NGUYÊN 100% từng chữ trong `KICH-BAN.md`.
Mọi văn bản khác (label, goc, pose, prompt, desc) viết tiếng Việt.

## 1. NHÂN VẬT — tên thoại → mã REF chân dung

Tên trong `text` / `goc` / `pose.who` phải ĐÚNG như tên đứng đầu dòng thoại trong
kịch bản (viết HOA, có dấu cách: `SHOPPER ONE`, `BOARD MEMBER`).

| Tên thoại | Portrait | Mô tả cố định (dùng cho mọi prompt) | Số scene |
|---|---|---|---|
| KEISHA | REF_KEISHA_PORTRAIT ⛔ user dán | nữ Mỹ gốc Phi 31 tuổi, da nâu ấm, **TÓC ĐEN THẲNG BÓNG CẮT BOB NGANG HÀM, rẽ ngôi giữa lệch nhẹ, một bên vén sau tai**, **KHUYÊN TAI VÀNG THẢ GIỌT NHỎ** (dấu riêng, mọi bộ đồ đều thấy) | 24 |
| WALTER | REF_WALTER_PORTRAIT ⛔ user dán | nam da trắng 78 tuổi, tóc bạc trắng dày gợn sóng buông phủ tai, mắt xanh xám nhạt, nếp nhăn sâu, đốm đồi mồi, cạo râu sạch | 7 |
| PIKE | REF_PIKE_PORTRAIT | nam da trắng 42 tuổi, tóc nâu sẫm vuốt hất, râu quai nón nâu tỉa gọn, mắt xanh xám, quai hàm vuông | 4 |
| ELAINE | REF_ELAINE_PORTRAIT | nữ da trắng 52 tuổi, con gái Walter; tóc nâu sẫm thẳng ngang vai rẽ ngôi lệch, khuyên đinh vàng nhỏ, mắt xanh xám giống cha | 6 |
| LORETTA | REF_LORETTA_PORTRAIT | nữ Mỹ gốc Phi 60 tuổi, mẹ Keisha; tóc ngắn xoăn tự nhiên điểm bạc; kính lão gọng nhựa nâu; tiểu đường + tim | 5 |
| COLIN | REF_COLIN_PORTRAIT | nam da trắng 36 tuổi, quy hoạch vùng 8 năm; tóc vàng cát cắt gọn, KÍNH GỌNG MỎNG kim loại, cạo râu sạch, gầy (phải KHÁC HẲN Pike: không râu, tóc sáng) | 6 |
| DENISE | REF_DENISE_PORTRAIT | nữ gốc Latin 33 tuổi, thu ngân quầy 4, mẹ đơn thân; tóc đen thẳng cột đuôi ngựa thấp; mặt tròn | 3 |
| RANDALL | REF_RANDALL_PORTRAIT | nam da trắng 56 tuổi, thanh tra vùng; gầy, tóc muối tiêu cắt ngắn, kính không gọng | 1 |
| SHOPPER ONE | REF_SHOPPERONE_PORTRAIT | nữ da trắng 48 tuổi, khách; tóc vàng nhuộm buộc thấp, mặt cau | 1 |
| SHOPPER TWO | REF_SHOPPERTWO_PORTRAIT | nữ da trắng 20 tuổi (NGƯỜI LỚN, con gái Shopper One); tóc nâu dài | 1 |
| PHARMACIST | REF_PHARMACIST_PORTRAIT | nam gốc Nam Á 45 tuổi, dược sĩ; tóc đen ngắn, kính gọng đen | 1 |
| RECRUITER | REF_RECRUITER_PORTRAIT | nữ da trắng 47 tuổi, tuyển dụng; tóc nâu đỏ ngắn, khuyên đinh nhỏ | 1 |
| PROCTOR | REF_PROCTOR_PORTRAIT | nam Mỹ gốc Phi 60 tuổi, giám thị; tóc bạc cắt sát, nghiêm | 1 |
| CANDIDATE ONE | REF_CANDIDATEONE_PORTRAIT | nam da trắng 28 tuổi, thí sinh; tóc nâu vuốt gel, tự tin | 1 |
| CANDIDATE TWO | REF_CANDIDATETWO_PORTRAIT | nữ gốc Á 30 tuổi, thí sinh; tóc đen thẳng ngang vai | 1 |
| BOARD MEMBER | REF_BOARDMEMBER_PORTRAIT | nam Mỹ gốc Phi 66 tuổi, thành viên HĐQT; tóc bạc cắt sát, kính gọng sừng | 1 |
| MANAGER | REF_MANAGER_PORTRAIT | nam gốc Latin 40 tuổi, quản lý cửa hàng (S25); tóc đen ngắn, ria mép mỏng | 1 |
| JONAS | REF_JONAS_PORTRAIT | nam Mỹ gốc Phi 20 tuổi, nhân viên sàn mới 7 tuần; tóc đen cắt fade, mặt non | 1 |

**Quần chúng nền** (khách siêu thị, thí sinh khác, học viên khác, thành viên HĐQT
khác, khách căng-tin, nhân viên y tế…) KHÔNG có REF, KHÔNG được khai trong `goc`
hay `pose.who`; chỉ tả bằng chữ, có định lượng, trong prompt SF ở bước 3.

## 2. TRANG PHỤC — mã REF FULL và scene dùng

Mỗi thẻ FULL: 9:16, `refs.chars = [REF_<TÊN>_PORTRAIT]`, prompt KHÔNG tả lại mặt
("Gương mặt giống ẢNH portrait tham chiếu"), `desc` kết bằng dòng riêng
`Dùng: S1 · S2` để `kiem-luat.py` đối chiếu được.

### KEISHA — 11 bộ (24 scene, luật đòi ≥10)

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_KEISHA_UNIFORM_FULL | đồng phục Grayway: polo xanh lá rừng đã bạc nhẹ vì giặt nhiều nhưng SẠCH, thẻ tên "KEISHA", quần đen, sneaker đen mòn gót | S1 · S2 · S3 · S5 |
| REF_KEISHA_UNIFORMKHOAC_FULL | vẫn bộ đồng phục trên, khoác thêm áo jean bạc màu và đeo túi vải — bộ ra khỏi cửa hàng | S4 |
| REF_KEISHA_THUONG_FULL | đồ ra ngoài ngày thường: áo len mỏng cổ tròn xám than sờn cổ, quần jean bạc, sneaker | S6 |
| REF_KEISHA_TUTE_FULL | bộ tử tế (phỏng vấn · gặp Walter · đi thi): sơ mi trắng cài kín hơi cũ nhưng ủi phẳng, quần tây đen, giày bệt đen | S7 · S12 · S13 |
| REF_KEISHA_ONHA_FULL | đồ ở nhà buổi tối: áo thun dài tay xám sờn, quần jogger đen, tất, KHÔNG giày | S8 · S16 |
| REF_KEISHA_NHA2_FULL | đồ ở nhà ban ngày khi có khách: áo len be cũ, quần jean sẫm, dép trong nhà | S10 · S11 |
| REF_KEISHA_CONGSO1_FULL | công sở mới (ngày đầu Fellowship): blouse lụa xanh navy, quần tây xám, giày bệt, thẻ Gray Foods đeo dây cổ | S14 · S15 |
| REF_KEISHA_CONGSO2_FULL | áo len cổ lọ mỏng màu rượu vang, quần tây đen, thẻ Gray Foods | S17 · S18 |
| REF_KEISHA_CONGSO3_FULL | sơ mi xám nhạt xắn tay + gi-lê len đen, quần tây đen, thẻ Gray Foods | S19 · S20 · S21 |
| REF_KEISHA_BLAZER_FULL | blazer đen ôm + áo trong trắng, quần tây đen, giày gót thấp — ngày ra hội đồng | S22 · S23 |
| REF_KEISHA_GIAMDOC_FULL | một năm sau: blazer màu kem cắt may đẹp, áo trong đen, quần tây đen, thẻ Gray Foods | S24 · S25 |

Dấu riêng xuyên suốt: **khuyên tai vàng thả giọt nhỏ**. Áo cổ tròn/cổ tim → thêm
dây chuyền mảnh mặt chữ thập nhỏ. Áo cổ lọ/sơ mi cài kín → giấu dây chuyền, chỉ
thấy khuyên + **đồng hồ dây da nâu cổ tay TRÁI** (từ S14 trở đi). Trần số món:
nghèo 1 · thường ngày 3 · công sở 2.

### WALTER — 5 bộ (7 scene)

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_WALTER_AOVUON_FULL | "gardening coat": khoác vải bạt ô-liu cũ sờn, vệt đất khô ở gấu và khuỷu, trong là sơ mi flannel ca-rô nâu, kaki bạc, giày da nâu cũ; SẮC MẶT XÁM (đang tụt đường) | S1 · S2 |
| REF_WALTER_BENHVIEN_FULL | áo bệnh nhân xanh nhạt hoa văn nhỏ, băng dán kim truyền mu bàn tay TRÁI, tóc bạc rối; sắc mặt đã hồng lại | S9 |
| REF_WALTER_KHACH_FULL | old-money giản dị: khoác tweed nâu xám, áo len cổ tròn navy, sơ mi trắng, quần vải xám, giày da nâu đánh bóng, gậy chống gỗ | S10 · S11 |
| REF_WALTER_VANPHONG_FULL | cardigan len xám đậm cài cúc, sơ mi trắng cổ mở, quần tây than, giày da | S12 |
| REF_WALTER_MOTNAM_FULL | một năm sau: áo khoác dạ xanh navy, áo len xám nhạt, quần vải nâu, gậy chống gỗ | S24 |

### PIKE — 3 bộ (4 scene; S2 và S3 là CÙNG MỘT NGÀY nên dùng chung một bộ)

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_PIKE_QUANLY_FULL | quản lý cửa hàng: sơ mi trắng dài tay, cà vạt xanh lá rừng Grayway, thẻ "D. PIKE — STORE MANAGER", quần tây đen, bộ đàm gài hông | S2 · S3 |
| REF_PIKE_VUNG1_FULL | quản lý vùng: blazer xanh navy, sơ mi xanh nhạt không cà vạt, thẻ Gray Foods đeo dây | S18 |
| REF_PIKE_VUNG2_FULL | áo khoác ngoài xám chì, sơ mi trắng hở cổ, quần tây than | S21 |

### ELAINE — 4 bộ (6 scene)

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_ELAINE_BENHVIEN_FULL | khoác trench be, áo len xám, quần tây đen, túi da nâu | S9 |
| REF_ELAINE_CONGSO1_FULL | vest nữ xám than, áo lụa trắng, quần tây, giày gót vừa | S14 · S15 |
| REF_ELAINE_CONGSO2_FULL | áo len cashmere xanh rêu, chân váy bút chì đen dài gối | S17 · S19 |
| REF_ELAINE_CONGSO3_FULL | vest nữ xanh navy sẫm, áo lụa xanh nhạt, ghim cài áo nhỏ | S22 |

### COLIN — 4 bộ (6 scene)

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_COLIN_CONGSO1_FULL | sơ mi xanh nhạt cài kín, cà vạt xám mảnh, quần tây xám | S14 · S15 |
| REF_COLIN_CONGSO2_FULL | sơ mi trắng, áo len cổ chữ V xanh navy, quần tây than | S17 · S19 |
| REF_COLIN_CONGSO3_FULL | sơ mi kẻ sọc mảnh xắn tay tới khuỷu, không cà vạt, quần tây xám (khuya ở phòng dữ liệu) | S20 |
| REF_COLIN_CONGSO4_FULL | sơ mi xám nhạt nhàu nhẹ, không áo khoác, thẻ Gray Foods lệch dây | S23 |

### LORETTA — 4 bộ (5 scene)

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_LORETTA_NHA1_FULL | váy nhà hoa nhí xanh nhạt đã bạc, cardigan len nâu, dép nhà; kính lão treo dây trước ngực | S5 |
| REF_LORETTA_DEM_FULL | áo ngủ cotton dài tay màu kem, áo choàng mỏng xanh than, dép | S8 |
| REF_LORETTA_NHA2_FULL | áo len cổ tim tím than cũ, quần vải đen, khăn quàng mỏng — bộ tiếp khách | S10 · S11 |
| REF_LORETTA_KHUYA_FULL | áo choàng ngủ kẻ sọc, khăn lụa trùm tóc, dép; kính lão đeo lên mắt | S16 |

### Vai một cảnh — 1 bộ mỗi người

| Mã FULL | Bộ đồ | Dùng |
|---|---|---|
| REF_DENISE_UNIFORM_FULL | polo Grayway xanh lá rừng, thẻ "DENISE", quần đen, tạp dề ngắn quầy thu ngân | S1 · S3 · S4 |
| REF_RANDALL_SUIT_FULL | vest xám than, sơ mi trắng, cà vạt xám, bìa kẹp giấy kim loại | S2 |
| REF_SHOPPERONE_FULL | áo khoác gió tím than, quần legging đen, giày thể thao | S1 |
| REF_SHOPPERTWO_FULL | áo hoodie xám, quần jean ống rộng | S1 |
| REF_PHARMACIST_FULL | blouse trắng ngắn tay, sơ mi xanh nhạt, thẻ hiệu thuốc | S6 |
| REF_RECRUITER_FULL | cardigan len xám dài, áo trong đen, quần tây | S7 |
| REF_PROCTOR_FULL | sơ mi trắng, cà vạt xanh sẫm, quần tây, đồng hồ bấm giờ đeo dây cổ | S13 |
| REF_CANDIDATEONE_FULL | sơ mi xanh nhạt cài kín, quần tây xanh navy | S13 |
| REF_CANDIDATETWO_FULL | blazer xám, áo trong trắng, quần tây đen | S13 |
| REF_BOARDMEMBER_FULL | vest xám đậm ba mảnh, sơ mi trắng, cà vạt đỏ boóc-đô | S22 |
| REF_MANAGER_FULL | sơ mi cộc tay xanh Grayway, cà vạt xanh lá rừng, thẻ quản lý | S25 |
| REF_JONAS_FULL | polo Grayway xanh lá rừng còn mới, thẻ "JONAS", quần đen, sneaker trắng | S25 |

## 3. ĐẠO CỤ CHỦ CHỐT

Chai nước cam là vật gieo–trả của cả phim (S1 mở → S3 bị gọi là "theft" → S10
Walter mang lên trả → S25 Jonas nhại lại bằng chai nước): đủ cả bốn điều kiện của
luật đạo cụ nên BẮT BUỘC có REF riêng, hai trạng thái.

| Mã | Trạng thái | Dùng |
|---|---|---|
| REF_PROP_NUOCCAM_KIN | chai nhựa 450ml nước cam, nhãn Grayway xanh lá rừng, nắp trắng CÒN NGUYÊN, tem giá `$3.19` | S1 (trước khi mở) · S10 |
| REF_PROP_NUOCCAM_MO | cùng chai đó, NẮP ĐÃ MỞ nằm cạnh, mực nước vơi 1/3 | S1 · S2 · S3 |

Giấy sa thải (S3) và giấy write-up (S25) chỉ ở 2 cảnh nên KHÔNG tạo REF — tả
thẳng trong SF.

## 4. ĐỊA ĐIỂM — thẻ neo, biến thể giờ và quan hệ tham chiếu

22 thẻ. Ba "bối cảnh gốc" (in đậm) phải được sinh ảnh và user chốt TRƯỚC, các thẻ
còn lại đính ảnh gốc vào `refs.bg` để khoá kiến trúc hoặc khoá art direction.

### Chuỗi Grayway Market (cửa hàng số 1)

| Mã | Nơi | Quan hệ | Dùng |
|---|---|---|---|
| **REF_AISLE7_NGAY** | lối đi số bảy, ban ngày — **BỐI CẢNH GỐC của cả chuỗi siêu thị** | — | S1 · S2 |
| REF_AISLE7MOI_NGAY | vẫn aisle seven, một năm sau: có ghế băng, hàng nặng hạ xuống tầm hông | khoá kiến trúc từ AISLE7_NGAY | S24 |
| REF_PHONGNGHI_NGAY | phòng nghỉ nhân viên | đồng bộ art direction từ AISLE7_NGAY, KHÁC PHÒNG | S3 · S25 |
| REF_TRAMXE_CHIEU | trạm xe buýt ngoài vỉa hè trước cửa hàng, chiều muộn | đồng bộ art direction, ngoài trời | S4 |

### Chuỗi Grayway Market số 12

| Mã | Nơi | Quan hệ | Dùng |
|---|---|---|---|
| REF_STORE12_NGAY | sàn bán hàng cửa hàng 12, cũ hơn cửa hàng 1 | đồng bộ art direction từ AISLE7_NGAY, KHÁC CỬA HÀNG | S15 |
| REF_HANHLANG12_NGAY | hành lang sau kho cửa hàng 12 | đồng bộ từ STORE12_NGAY, KHÁC PHÒNG | S18 |

### Chuỗi căn hộ Dawson

| Mã | Nơi | Quan hệ | Dùng |
|---|---|---|---|
| **REF_BEPDAWSON_CHIEU** | bếp căn hộ, nắng chiều — **BỐI CẢNH GỐC của căn hộ** | — | S11 |
| REF_BEPDAWSON_CHAPTOI | cùng bếp, chập tối, chỉ còn đèn hắt từ hành lang | khoá kiến trúc từ BEPDAWSON_CHIEU | S5 |
| REF_BEPDAWSON_DEM | cùng bếp, đêm, một bóng đèn trần | khoá kiến trúc | S8 |
| REF_BEPDAWSON_KHUYA | cùng bếp, 2 giờ sáng, đèn bàn kéo lại gần | khoá kiến trúc | S16 |
| REF_CUADAWSON_CHIEU | cửa căn hộ nhìn từ chiếu nghỉ tầng bốn | đồng bộ art direction, KHÁC KHÔNG GIAN | S10 |

### Chuỗi trụ sở Gray Foods Corporate

| Mã | Nơi | Quan hệ | Dùng |
|---|---|---|---|
| **REF_PHONGHOP_NGAY** | phòng họp kính — **BỐI CẢNH GỐC của cả trụ sở** | — | S17 · S19 |
| REF_VPWALTER_NGAY | văn phòng riêng Walter, gỗ óc chó, khác hẳn phần còn lại | đồng bộ vật liệu, KHÁC PHÒNG | S12 |
| REF_PHONGTHI_NGAY | phòng thi, bàn đơn kê hàng | đồng bộ, KHÁC PHÒNG | S13 |
| REF_PHONGDINHHUONG_NGAY | phòng định hướng, ghế xếp hình chữ U | đồng bộ, KHÁC PHÒNG | S14 |
| REF_PHONGDULIEU_KHUYA | phòng dữ liệu, khuya, màn hình là nguồn sáng chính | đồng bộ, KHÁC PHÒNG | S20 |
| REF_HAMXE_DEM | hầm để xe tầng B2, đêm | đồng bộ, KHÁC KHÔNG GIAN | S21 |
| REF_PHONGHOIDONG_NGAY | phòng hội đồng, bàn dài gỗ sẫm | đồng bộ, KHÁC PHÒNG | S22 |
| REF_CANGTIN_NGAY | căng-tin nhân viên, 1 giờ 30 chiều | đồng bộ, KHÁC PHÒNG | S23 |

### Ngoài ba chuỗi trên

| Mã | Nơi | Dùng |
|---|---|---|
| REF_HIEUTHUOC_NGAY | quầy thuốc trong hiệu thuốc chuỗi | S6 |
| REF_TUYENDUNG_NGAY | phòng tư vấn Eastside Staffing Agency | S7 |
| REF_PHONGBENH_NGAY | phòng bệnh 412, Mercy General | S9 |

**Kiểm chuỗi scene tối** (trần 2 liền): S5 chập tối → S6 ngày. S8 đêm → S9 ngày.
S16 khuya → S17 ngày. S20 khuya → S21 đêm → S22 ngày. Dài nhất là 2. ĐẠT.

## 5. QUY ƯỚC MÃ

- Shot thoại: `V-S<scene>-<2 chữ số>` · SF tương ứng `SF-S<scene>-<2 chữ số>`.
- Nhịp không thoại: `V-S<scene>-B<số>` · `SF-S<scene>-B<số>`, nhãn mở đầu bằng `[NHỊP]`.
- 1 shot = 1 SF, không SF nào gánh hai shot.
- `goc` nằm ở SF; chỉ khai MAIN CAST, cấm khai quần chúng nền.
- `pose` là dict bốn trục: `zone` · `who` (dict theo tên) · `dist` · `hands` (dict theo tên).

## 6. TRẠNG THÁI ẢNH (2026-08-18)

- `assets/REF_WALTER_PORTRAIT.png` — ĐÃ CÓ, giữ nguyên từ bản cũ (đúng khuôn mặt user chốt).
- `assets/REF_KEISHA_PORTRAIT.jpg` — ĐÃ CÓ, user dán 2026-08-18. Ảnh 502x463 (gần vuông, KHÔNG phải 2:3),
  nền phố mờ, mắt nhìn chếch xuống, môi hé. Mọi thẻ FULL đã được siết câu "CHỈ LẤY KHUÔN MẶT VÀ KIỂU TÓC,
  KHÔNG lấy nền / hướng nhìn / biểu cảm của ảnh đó". Đừng gỡ câu này.
- 83 thẻ REF còn lại — **chưa sinh ảnh**. Sinh 3 bối cảnh gốc trước, rồi 19 thẻ neo vào chúng.

## 7. BẢNG SHOT (bước 1 — chốt 2026-08-18)

351 shot · 351 SF (đúng luật 1 shot = 1 SF) · 46 nhịp không thoại (15%) · 50 phút 06.
Thoại đã diff từng chữ với `KICH-BAN.md`: TRÙNG KHỚP 100% cả 25 scene.

| Scene | Shot | Nhịp | Thời lượng | Thẻ địa điểm |
|---|---|---|---|---|
| S1 | 15 | 3 | 2:14 | REF_AISLE7_NGAY |
| S2 | 13 | 2 | 1:54 | REF_AISLE7_NGAY |
| S3 | 16 | 2 | 2:00 | REF_PHONGNGHI_NGAY |
| S4 | 10 | 2 | 1:28 | REF_TRAMXE_CHIEU |
| S5 | 17 | 2 | 2:18 | REF_BEPDAWSON_CHAPTOI |
| S6 | 11 | 2 | 1:34 | REF_HIEUTHUOC_NGAY |
| S7 | 12 | 2 | 1:48 | REF_TUYENDUNG_NGAY |
| S8 | 14 | 2 | 1:56 | REF_BEPDAWSON_DEM |
| S9 | 13 | 1 | 1:50 | REF_PHONGBENH_NGAY |
| S10 | 10 | 2 | 1:32 | REF_CUADAWSON_CHIEU |
| S11 | 14 | 1 | 2:00 | REF_BEPDAWSON_CHIEU |
| S12 | 16 | 1 | 2:20 | REF_VPWALTER_NGAY |
| S13 | 14 | 3 | 2:00 | REF_PHONGTHI_NGAY |
| S14 | 15 | 2 | 2:10 | REF_PHONGDINHHUONG_NGAY |
| S15 | 16 | 3 | 2:16 | REF_STORE12_NGAY |
| S16 | 13 | 2 | 1:50 | REF_BEPDAWSON_KHUYA |
| S17 | 14 | 1 | 2:04 | REF_PHONGHOP_NGAY |
| S18 | 12 | 2 | 1:52 | REF_HANHLANG12_NGAY |
| S19 | 13 | 1 | 1:54 | REF_PHONGHOP_NGAY |
| S20 | 14 | 2 | 2:00 | REF_PHONGDULIEU_KHUYA |
| S21 | 16 | 2 | 2:20 | REF_HAMXE_DEM |
| S22 | 14 | 1 | 2:00 | REF_PHONGHOIDONG_NGAY |
| S23 | 17 | 1 | 2:06 | REF_CANGTIN_NGAY |
| S24 | 16 | 2 | 2:24 | REF_AISLE7MOI_NGAY |
| S25 | 16 | 2 | 2:16 | REF_PHONGNGHI_NGAY |

**55 shot mang chuyển động** đã khai `pose.chuyen = true` (nhân vật đi · đứng lên ·
ngồi xuống · đổi chỗ NGAY TRONG clip đó). Đó là cờ của `kiem-noi-shot.py`; đừng gỡ,
gỡ là 131 mối nối giả hiện lại. Sang bước 4, đúng những shot này phải có khối
KẾT CLIP tả đường đi.

`pose.who` chỉ ghi TƯ THẾ và VỊ TRÍ, KHÔNG ghi hướng đầu hay hướng người — thứ đó
nằm ở `goc` và ở khối HƯỚNG NHÌN của prompt SF. Viết hai cách khác nhau cho cùng
một tư thế là sinh mối nối giả.

Chỉ dùng hai mức thời lượng: **6s** và **10s**. Câu thoại dài quá 31 từ phải tách
sang shot kế tiếp theo ranh giới CÂU, tuyệt đối không sửa chữ.

## 8. TRẠNG THÁI BOARD (chốt 2026-08-18)

Cả năm bước đã viết xong, `kiem-luat.py` và `kiem-noi-shot.py` đều **✓ SẠCH**.

| Bước | Nội dung | Số lượng |
|---|---|---|
| 1 | bảng shot · `goc` · `pose` 4 trục | 351 shot / 351 SF (1:1) · 46 nhịp (15%) · 50:14 |
| 2 | thẻ REF | 85 (18 chân dung · 43 trang phục · 2 đạo cụ · 22 địa điểm) |
| 3 | prompt SF | 351 · đủ 7 khối · cận 35% · trung 56% · trung-rộng 7% · rộng 2% |
| 4 | prompt video | 351 · form chuẩn · 15 khối KẾT CLIP (4,3% — trần 7%) |
| 5 | nhạc Suno | 46 nhịp × 2 phương án (A có lời + B không lời) · ĐẨY 3 · NÂNG 9 · KÌM 15 · NGHỈ 19 |

**Vai ĐẨY chỉ có 3, đúng trần**: `V-S1-B1` mở phim · `V-S16-B2` hai mẹ con chia đôi chồng biên bản ·
`V-S25-B2` kết phim. Không thêm nhịp ĐẨY nào nữa.

**12 cảnh báo `thoại có lệnh thay đổi trạng thái`** đã rà tay: mọi SF liên quan đều vẽ đúng trạng thái
CHƯA LÀM (Keisha còn ở ghế cửa sổ khi Loretta bảo ngồi xuống bàn; Walter chưa bước qua ngưỡng khi
Loretta bảo ngồi; Keisha đứng chưa ngồi khi Walter mời). Ba cảnh báo còn lại là thành ngữ
("Do not sit there and tell me"), không phải mệnh lệnh.

⛔ **Chưa có ảnh nào ngoài hai chân dung.** Prompt SF bám theo Floor Plan trong `luatchung` của thẻ
địa điểm. Nếu sinh ảnh rồi đổi bố cục phòng (đổi bên đặt quầy bếp, đổi phía cửa sổ), phải rà lại
prompt SF của phòng đó — trục màn hình đã khoá cứng theo Floor Plan hiện tại.
