---
name: tai_nang_bi_khinh_va_loi_thach_cuoc_cong_khai
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~7.500–8.500 từ) cho kênh kể chuyện YouTube, thuộc dòng TÀI NĂNG BỊ KHINH VÀ LỜI THÁCH CƯỢC CÔNG KHAI — "một người mang cái nhãn thấp nhất trong sân (người vô gia cư, người làm thuê, người lạ không giấy tờ) lên tiếng về một thứ đang hỏng mà người có quyền đang rao bán; kẻ có quyền lôi họ ra làm trò trước đám đông, ném đi thứ duy nhất họ có, rồi buột miệng thách một lời cược lớn có nhân chứng — họ xin nói lại lời cược đó cho rõ vào máy ghi, bước vào, và thắng bằng phương pháp chứ không bằng sức. Cuối cùng một người có thẩm quyền tới với hồ sơ, và cái quá khứ bị bôi đen của họ, lẫn quyền sở hữu thật đối với chính thứ đang được rao bán, được đọc to trước tất cả." Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title dạng "người giàu / chủ / kẻ có quyền thách người ở đáy: làm được thì thưởng X — sai lầm lớn nhất đời họ", hoặc yêu cầu viết bài mới / sửa mở màn / viết phần công bố và cái kết cho dòng này. Title "bị lôi ra giải bài toán của nghề giữa hội trường" dùng tai_nang_bi_lam_tro_cuoi_truoc_dam_dong; "tự ghi danh một kỳ thi rồi đi tới cùng" dùng tai_nang_bi_khinh_tren_dau_truong; "nửa đêm bị người có quyền bắt gặp đang làm việc" dùng tai_nang_duoc_phat_hien_ban_dem; "bị chế nhạo bằng thứ tiếng tưởng họ không hiểu" dùng tai_nang_ngon_ngu. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Tài năng bị khinh và lời thách cược công khai — cái bẫy do chính kẻ có quyền dựng lên

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không bước nào ở giữa cần user.**

Chạy theo `references/8-quy-trinh-viet.md`, bước 0 → 9, với hai cổng tự duyệt:

```
title → đọc title → dựng CÁI ĐANG HỎNG và LỜI GIẢI THẬT → dàn nhân vật + sổ cài đặt
      → phác cảnh thách cược, cảnh trình diễn, cảnh hồ sơ
      → mở màn + lời rủ tương tác → ⛔ CỔNG 1
      → thế giới → sỉ nhục leo thang → ném đi vật duy nhất → lời cược được ghi lại
      → trình diễn → xác nhận bằng người trong nghề → hồ sơ & hai lần lật
      → phản ứng từng người → hệ quả có định chế → đảo ngôi → kết → khối đóng bài → ⛔ CỔNG 2
      → ghi file → báo cáo
```

**Không hỏi user** về độ dài, bối cảnh, tên, nghề, loại tài năng. Title không nói thì tự quyết theo `8-quy-trinh-viet.md` bước 1. **Giữ nguyên văn title** — không viết lại, không rút gọn, không "cải thiện", kể cả khi title có chữ nghe lạ hoặc sai ngữ pháp. Chỉ dừng lại hỏi khi chuỗi user dán vào không phải một title. User yêu cầu thêm (độ dài khác, bối cảnh cụ thể) thì áp dụng và vẫn chạy thẳng.

**Phân tuyến** — năm dòng tài năng dễ lẫn, phân bằng **cách tài năng bị đẩy ra ánh sáng**:

| Tài năng lộ ra vì… | Skill |
|---|---|
| kẻ có quyền thách một lời cược có phần thưởng và có nhân chứng, rồi bị chính lời mình trói | **skill này** |
| kẻ có quyền lôi họ ra giữa phòng và ấn bài toán của nghề vào tay họ | `tai_nang_bi_lam_tro_cuoi_truoc_dam_dong` |
| họ tự ghi danh một kỳ thi có thước đo và im lặng đi tới cùng | `tai_nang_bi_khinh_tren_dau_truong` |
| họ làm việc lúc không ai thấy và bị người có quyền bắt gặp | `tai_nang_duoc_phat_hien_ban_dem` |
| kẻ có quyền khinh họ bằng một thứ tiếng tưởng họ không hiểu | `tai_nang_ngon_ngu` |

Ranh giới thật của skill này: **có một lời hứa/lời cược được nói ra trước nhân chứng, và nó trở thành ràng buộc.** Không có nhịp đó thì bài thuộc dòng khác.

## 1. Hợp đồng đầu ra

File chỉ gồm: dòng đầu `title: <tiêu đề tiếng Anh>`, rồi **văn xuôi**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn một dòng, giữa hai đoạn đúng một dòng trống, mỗi lượt thoại một đoạn riêng** (`7-van-phong.md` mục 1).

Ngoại lệ về ngôi và thì chỉ ở **lời rủ tương tác** cuối mở màn và **khối đóng bài** cuối bài — hai chỗ này nói thẳng với người xem (`4-mo-man-va-cta.md` mục 4). Đây là dòng có CTA; không được bỏ.

**Chỉ tiếng Anh Mỹ trong file.** Nhân vật nói tiếng nước ngoài thì câu đó viết bằng tiếng Anh và tự gọi tên thứ tiếng trong câu dẫn (*she said in Portuguese*).

Không tiêu đề mục, số cảnh, nhãn, ghi chú của người viết, gạch đầu dòng, hay bất kỳ thuật ngữ nào của skill này. Outline nếu cần thì nằm trong tin nhắn, không nằm trong file.

Trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác. Quy mô mặc định khoảng 7.500–8.500 từ (Golden ~8.000); user nói khác thì co giãn theo `3-cau-truc.md` mục 5, giữ nguyên trật tự khối.

## 2. Bảy động cơ

Lý do thể loại này chạy. Chi tiết và "vì sao" ở `references/1-nguyen-ly-cot-loi.md`.

1. **Nhân vật chính mở miệng vì người khác, không vì mình.** Câu đầu tiên họ nói ra không phải lời tự vệ mà là một **nhận xét nghề về cái đang hỏng** — con vật đang đau, cái máy sắp gãy, người bệnh đang bị đọc sai. Đó là thứ kéo hoả lực về phía họ. Người xem thích họ trước khi biết họ là ai.

2. **Cái đang hỏng là thứ kẻ có quyền đang kiếm tiền.** Nhận xét kia không xúc phạm hiểu biết của hắn; nó xúc phạm **cái giá**. Vì vậy hắn không thể bỏ qua, và phản ứng của hắn phải quá tay so với một câu nói vu vơ.

3. **Sỉ nhục leo thang tới chỗ không rút lại được.** Nhiều nấc, nấc sau nặng hơn nấc trước, và ít nhất một nấc là **hành động chứ không phải lời** — thứ duy nhất nhân vật chính sở hữu bị giằng lấy, bị ném đi, bị phá. Từ nhịp đó trở đi, một lời xin lỗi không còn đủ để đóng truyện.

4. **Lời cược do chính kẻ có quyền buột ra, và nhân vật chính xin nói lại cho rõ.** Đây là nhịp ký tên của dòng này. Họ không đòi tiền; họ đòi **sự rõ ràng** — nói lại số tiền, ai trả, trả cho ai, trước ngần này máy ghi hình. Kẻ có quyền nghe ra đó là lời cầu xin được sỉ nhục thêm lần nữa, nên nói to hơn và đẹp hơn cả lần đầu. Cái bẫy do hắn tự bước vào, giữa lúc hắn đang thắng.

5. **Thắng bằng phương pháp, và việc đầu tiên làm là không làm gì.** Đám đông chờ một cuộc vật lộn. Cái họ nhận được là **kỹ thuật của một người đã làm nghề này mười nghìn lần** — chậm, không phô, và đọc được bởi đúng một người trong đám đông có nghề. Người đó dịch lại cho cả sân nghe, nên khán giả hiểu mình đang xem cái gì.

6. **Quá khứ bị bôi đen, và quyền sở hữu bị giấu.** Nhân vật chính không im lặng vì cao thượng; họ im lặng vì **không có gì trưng ra được** — tên bị treo, giấy phép bị rút, một hồ sơ vu cho họ tội mà chính người đang sỉ nhục họ đã dựng. Người có thẩm quyền tới vì một việc hành chính khác hẳn, và **lật hai lần**: lần một là họ từng là ai; lần hai là **thứ đang được rao bán vốn thuộc về họ**.

7. **Lời hứa bị chối, rồi bị chính đám đông thi hành.** Kẻ có quyền gọi luật sư, gọi lời cược là đùa. Bằng chứng đánh sập nó không đến từ định chế mà **đến từ chính những cái điện thoại được giơ lên để cười nhạo nhân vật chính**. Đám đông trở thành sổ ghi biên bản.

**Luật tuyệt đối 1**: chiến thắng phải **diễn ra trên sân, trước mặt mọi người, trước khi ai biết nhân vật chính là ai**. Hồ sơ đến sau và chỉ giải thích cái đám đông vừa thấy — nó không bao giờ là thứ tạo ra chiến thắng.

**Luật tuyệt đối 2**: nhân vật chính **không tự khai mình là ai**, không một lần, ở bất cứ đâu trong bài. Ai cũng có quyền nói hộ họ, trừ chính họ.

## 3. Bất biến và biến số — đọc trước mọi thứ

Skill này rút từ **một** Golden Project. Một điểm dữ liệu không phải quy luật.

- **Bất biến**: bảy động cơ ở trên, hai luật tuyệt đối, và các **chức năng** trong `references/`.
- **Biến số**: mọi cách hiện thực. Loại tài năng, nghề, thời đại, quốc gia, cái nhãn thấp, cái đang hỏng, loại đấu trường, hình thức phần thưởng, vật mang tài năng, người có thẩm quyền, loại hồ sơ, câu chữ. Chúng **phải mọc ra từ title đang viết**, không mọc từ Golden.

Bảng tách hai loại ở `references/12-pattern-golden.md`. Khi phân vân, hỏi: *nếu đổi chi tiết này, bài có mất lý do để hay không?* Không mất → nó là biến số, và phải chọn mới.

**Sáu lỗi skill này được thiết kế để tránh — người viết cũng phải tránh:**

- **Bắt chước bề mặt Golden** (*prompt overfitting*). Golden là **một** hiện thân: ngựa, trang trại, tiền mặt chỉ là một cách lấp vào bảy động cơ. Hỏi: *đổi sạch bối cảnh, bài còn đủ bảy động cơ không?*
- **Nhân bản trình tự** (*over-specific template*). Nguy hơn chép chất liệu vì không lộ ra khi đọc. Một bản nháp có thể khớp Golden 13/13 khe theo đúng thứ tự mà tên và nghề khác hoàn toàn, và đọc vẫn thấy "ổn". Bảo hiểm là **đối chiếu đoạn với đoạn** ở Cổng 1 và đếm chuỗi trùng ở Cổng 2.
- **Buộc quá chặt** (*over-constraining*). Con số trong skill là **điểm neo lấy từ một mẫu**, không phải ngưỡng. Lệch vừa phải mà bài vẫn chạy thì không sao; lệch nhiều thì phải có lý do nằm trong chính câu chuyện.
- **Khoá vào một mô-típ** (*trope lock-in*). Con vật bất kham, phần thưởng tiền mặt, vị chủ tịch hiệp hội, tấm séc — mỗi thứ là **một** lựa chọn trong nhiều. Danh sách thay thế ở `2-nhan-vat.md` và `6-cong-bo-va-ket.md`; phải thực sự dùng chúng.
- **Lọt khung ra file** (*template leakage*). Nhãn, số khối, thuật ngữ skill xuất hiện trong bài. Xem mục 1.
- **Thuộc luật mà không hiểu lý do** (*low abstraction*). Mỗi quy tắc trong `references/` đều kèm "vì sao nó chạy". Gặp tình huống lạ thì suy từ lý do, đừng ép tình huống vừa khuôn.

## 4. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Bảy động cơ và lý do chúng chạy. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dàn nhân vật theo **chức năng**; các trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Trục khối, tỉ lệ độ dài, sổ cài–trả. |
| [4-mo-man-va-cta.md](references/4-mo-man-va-cta.md) | **Mở màn, câu treo, lời rủ tương tác, khối đóng bài.** Phần user quan tâm nhất. |
| [5-trinh-dien.md](references/5-trinh-dien.md) | Cảnh chứng minh trên sân: phương pháp, người dịch nghề, đám đông đổi chiều. |
| [6-cong-bo-va-ket.md](references/6-cong-bo-va-ket.md) | Hồ sơ, hai lần lật, thi hành lời hứa, hệ quả, đảo ngôi, kết. |
| [7-van-phong.md](references/7-van-phong.md) | Định dạng, nhịp câu, giọng người kể, cách viết số liệu và thoại. |
| [8-quy-trinh-viet.md](references/8-quy-trinh-viet.md) | **Quy trình tự động bước 0 → 9.** Mở ngay sau khi nhận title. |
| [9-vi-du-co-chu-thich.md](references/9-vi-du-co-chu-thich.md) | Xem một kỹ thuật trông ra sao trên trang giấy + **danh sách câu đã tiêu**. |
| [10-chu-de-nhay-cam.md](references/10-chu-de-nhay-cam.md) | Viết về định kiến mà không thành nội dung kích động. |
| [11-checklist.md](references/11-checklist.md) | Phần H = Cổng 1 (mở màn). Phần A–G = Cổng 2 (toàn bài). |
| [12-pattern-golden.md](references/12-pattern-golden.md) | Bảng bất biến/biến số và **bộ chất liệu Golden đã tiêu**. |

## 5. Golden Project

```
golden_project/
└── golden_project_1/KICH-BAN.md   ← ~8.000 từ, đúng hình dạng của dòng này
```

Đây là **chuẩn mực sống**: khi `references/` mô tả một luật bằng lời, Golden cho thấy luật đó trông ra sao khi đã nằm trên trang giấy. `references/` mâu thuẫn với Golden thì Golden đúng — báo lại cho user trong tin nhắn.

**Một ngoại lệ**: luật dòng trống ở mục 1. Golden viết liền không dòng trống; skill viết cách dòng theo yêu cầu của user. Đừng "sửa" nó ở bất kỳ vòng duyệt nào.

**Luật cứng — HỌC CÁCH LÀM, KHÔNG LẤY CHẤT LIỆU.** Bảng đối chiếu đầy đủ ở `12-pattern-golden.md`; bản rút gọn:

| Được lấy | Không được lấy |
|---|---|
| Hình dạng: lên tiếng vì cái đang hỏng → bị sỉ nhục leo thang → mất vật duy nhất → lời cược được ghi lại → thắng bằng phương pháp → hồ sơ lật hai lần → hệ quả → đảo ngôi → đi ra | Chính các tình tiết lấp vào hình dạng đó |
| Cách nhân vật chính xin nói lại lời cược cho rõ trước máy ghi | Con số hai triệu, tấm séc bìa đỏ, câu "loser crawls back to his ditch" |
| Cách một người trong nghề ở đám đông dịch lại kỹ thuật cho cả sân hiểu | Cấu hình "ông bán yên cương sáu mươi tuổi nhận ra nút thắt" |
| Cách một người có chuyên môn bị dập im rồi trả giá để nói ra sự thật | Cấu hình "bác sĩ thú y hợp đồng bị đuổi việc tại chỗ" |
| Cách hồ sơ lật hai lần: họ từng là ai, rồi thứ đang bán vốn là của họ | Giấy đăng ký ngựa giống, hiệp hội, lệnh truy tố trộm cắp |
| Cách bài kết bằng việc nhân vật chính đi ra, không nhìn kẻ kia, mang theo đúng thứ họ tới vì nó | Đường hạt, đôi ủng cầm trên tay, con ngựa đen |

**Đọc lúc nào, đọc bao nhiêu.**

- ⛔ Không nạp cả file theo phản xạ. Mặc định **không đọc** — `9-vi-du-co-chu-thich.md` đã trích sẵn các đoạn tiêu biểu kèm luật rút ra.
- **Ngoại lệ bắt buộc**: trước khi viết mở màn, đọc **một lần** phần mở màn của Golden (từ dòng đầu tới câu rủ tương tác, ~15 dòng) để nghe nhịp, rồi đóng lại và viết bằng chất liệu của mình.
- Ngoài ra chỉ mở Golden khi có **câu hỏi cụ thể** không tra được trong `references/`, và khi đó đọc đúng một đoạn (~40–60 dòng) của phần liên quan.
- Rớt cùng một mục ở Cổng 1 hoặc Cổng 2 hai vòng liền → mở đúng phần tương ứng xem bài chuẩn giải quyết ra sao.
- Đọc xong thì **diễn đạt lại thành nguyên tắc** rồi mới viết. Câu nào trong bản nháp tra ngược được về Golden bằng tìm chuỗi ký tự thì viết lại.

**Không được sửa Golden Project**, kể cả khi thấy lỗi. Chỉ user sửa thủ công. Phát hiện chỗ khả nghi thì báo trong tin nhắn.
