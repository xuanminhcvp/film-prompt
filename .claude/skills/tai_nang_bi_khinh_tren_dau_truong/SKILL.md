---
name: tai_nang_bi_khinh_tren_dau_truong
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~7.500–8.500 từ) cho kênh kể chuyện YouTube, thuộc dòng "một người bị khinh vì vẻ ngoài / giới / màu da bước vào một đấu trường có thước đo công khai; họ im lặng và thắng bằng năng lực, kẻ có quyền liên tục nâng rào để loại họ — rồi một người có thẩm quyền cao hơn công bố cái quá khứ bị niêm phong mà không ai ở đó biết". Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title dạng "người có quyền không biết người kia thực ra là …" gắn với một cuộc thi / kỳ sát hạch / ca trực / phiên chấm, hoặc yêu cầu viết bài mới, sửa mở màn, viết phần công bố và cái kết cho dòng này. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Truyện kể: tài năng bị khinh trên đấu trường, và hồ sơ được mở

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không có bước nào ở giữa cần user.**

Chạy thẳng theo `references/7-quy-trinh-viet.md`, bước 0 → bước 9, với hai cổng tự duyệt:

```
title → đọc title → dàn nhân vật + đấu trường + quá khứ niêm phong → phác chuỗi vòng thi
      → phác cảnh công bố → viết mở màn + câu bắc cầu
                                        ↓
                              ⛔ CỔNG 1 (phần H)
                                        ↓
     quá khứ → lý do quay lại → các vòng leo thang → công bố → hệ quả → coda
                                        ↓
                              ⛔ CỔNG 2 (phần A–G)
                                        ↓
                             ghi file → báo cáo
```

**Không hỏi user**: không xin duyệt outline, không xin duyệt mở màn, không hỏi độ dài, bối cảnh hay tên nhân vật. Title không nói gì thì tự quyết theo `7-quy-trinh-viet.md` bước 1.

**Giữ nguyên văn title của user.** Không viết lại, không rút gọn, không "cải thiện" — kể cả khi title có chữ nghe lạ.

Ngoại lệ duy nhất được dừng lại hỏi: chuỗi user dán vào không phải một title.

User yêu cầu thêm (độ dài khác, bối cảnh cụ thể, ngôn ngữ khác) thì áp dụng và vẫn chạy thẳng.

## 1. Hợp đồng đầu ra

Sản phẩm cuối cùng chỉ gồm **đúng hai thành phần**:

1. Dòng đầu tiên: `title: <tiêu đề tiếng Anh>`
2. Phần còn lại là **văn xuôi liền mạch**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn nằm trên một dòng, và giữa hai đoạn có đúng một dòng trống.**

> ⚠️ **Đây là chỗ duy nhất skill cố ý lệch khỏi golden.** Golden project viết liền, không dòng trống. User đã chốt là muốn cách dòng cho dễ đọc. Luật này **thắng golden** — không được "sửa lại cho khớp golden" ở bất kỳ vòng duyệt nào.

Trong file **không được có**: tiêu đề mục, số cảnh, `SCENE`, `Act`, tên nhịp, ghi chú đạo diễn, gạch đầu dòng, chú thích của người viết, hay bất kỳ thuật ngữ nào của skill này. Outline (nếu cần) nằm trong tin nhắn, không nằm trong file.

**Không có CTA.** Dòng này không mời like, không mời subscribe, không hỏi khán giả câu nào, không có người kể nói trực tiếp với người xem ở bất cứ đâu — kể cả câu cuối. Bài kết bằng một hình ảnh yên tĩnh. (Nếu user đòi CTA thì thêm; mặc định là không.)

**Ngôn ngữ**: trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác.

**Quy mô mặc định**: khoảng 7.500–8.500 từ (golden: ~7.600). User muốn ngắn/dài hơn thì co giãn theo tỉ lệ ở `3-cau-truc.md`, giữ nguyên trật tự.

## 2. Năm động cơ của thể loại

Chi tiết và lý do ở `references/1-nguyen-ly-cot-loi.md`. Tóm tắt:

1. **Có một thước đo công khai, và nhân vật chính thắng nó trước mặt mọi người.** Đây không phải chuyện chờ được minh oan. Họ chứng minh, bằng con số, nhiều lần, trước khi bất cứ ai bênh họ.
2. **Kẻ có quyền không chấp nhận bằng chứng — họ nâng rào.** Mỗi lần bằng chứng đến, họ đổi luật cho khó hơn. Chính chuỗi nâng rào ấy, chứ không phải một câu nhục mạ, là thứ kéo sập họ ở cuối.
3. **Nhân vật chính mang một quá khứ không trưng ra được.** Thành tích của họ bị niêm phong, bị giấu, hoặc đứng tên người khác — nên im lặng là lựa chọn duy nhất có thật, không phải sự nhẫn nhịn màu mè.
4. **Họ bước vào đấu trường vì một nhu cầu đời thường có hạn chót.** Không vì danh dự, không để dạy ai bài học. Khán giả biết cái giá cụ thể của việc thua.
5. **Sự thật được một người có thẩm quyền cao hơn công bố, rất muộn — sau khi nhân vật chính đã tự thắng.** Chiến thắng đến trước, sự công nhận đến sau. Hệ quả gọn, rồi bài về một không gian nhỏ và yên.

## 3. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Năm động cơ và lý do chúng chạy. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dựng dàn nhân vật theo **chức năng**; bốn trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Trục khối, tỉ lệ độ dài, chuỗi vòng leo thang, sổ cài–trả. |
| [4-mo-man.md](references/4-mo-man.md) | Đọc title, viết mở màn, câu treo, câu bắc cầu về quá khứ. |
| [5-cong-bo-va-ket.md](references/5-cong-bo-va-ket.md) | Cảnh công bố, hệ quả, và coda yên tĩnh. |
| [6-van-phong.md](references/6-van-phong.md) | Định dạng, nhịp câu, giọng người kể, câu treo cuối khối, cách viết số liệu. |
| [7-quy-trinh-viet.md](references/7-quy-trinh-viet.md) | **Quy trình tự động bước 0 → 9.** Mở ngay sau khi nhận title. |
| [8-vi-du-co-chu-thich.md](references/8-vi-du-co-chu-thich.md) | Xem một kỹ thuật trông ra sao trên trang giấy. |
| [9-chu-de-nhay-cam.md](references/9-chu-de-nhay-cam.md) | Viết về định kiến mà không thành nội dung kích động. |
| [10-checklist.md](references/10-checklist.md) | Phần H = Cổng 1 (mở màn). Phần A–G = Cổng 2 (toàn bài). |
| `golden_project/golden_project_1/KICH-BAN.md` | Bài chuẩn. **Chỉ mở khi có câu hỏi cụ thể, đọc một đoạn.** Xem mục 4. |

## 4. Golden Project

```
golden_project/
└── golden_project_1/KICH-BAN.md   ← ~7.600 từ, đúng định dạng đầu ra
```

Đây là **chuẩn mực sống**: khi `references/` mô tả một luật bằng lời, golden cho thấy luật đó trông ra sao khi đã nằm trên trang giấy. Nếu một luật trong `references/` mâu thuẫn với golden, golden đúng — báo lại cho user trong tin nhắn.

**Một ngoại lệ duy nhất**: luật cách dòng ở mục 1. Golden viết liền; skill viết cách dòng, theo yêu cầu của user. Đừng "sửa" nó.

**Hiện chỉ có một bài chuẩn.** Vì vậy mọi con số đo trong skill (số từ mở màn, tỉ lệ khối, vị trí cảnh công bố) là **điểm neo lấy từ một mẫu**, không phải ngưỡng. Lệch vừa phải mà bài vẫn chạy thì không sao; lệch nhiều thì phải có lý do nằm trong chính câu chuyện.

**Luật cứng — HỌC CÁCH LÀM, KHÔNG LẤY CHẤT LIỆU.**

| Được lấy | Không được lấy |
|---|---|
| Hình dạng: sỉ nhục ở ngay đầu → lùi về quá khứ → nhu cầu có hạn chót → nhiều vòng thi leo thang → thắng → công bố muộn → coda yên | Chính các tình tiết lấp vào hình dạng đó |
| Cách kẻ có quyền đổi luật ngay sau mỗi lần thua, và lời biện minh "sân của tôi, luật của tôi" | Cấu hình "đô đốc hải quân chủ giải bắn tỉa" |
| Cách một câu của người đã mất trở thành điệp khúc, quay lại đúng phát cuối | Nguyên câu thoại đó, nguyên hình ảnh người quan sát chết vì mìn |
| Cách một người đồng nghiệp tự nguyện đứng về phía nhân vật chính mà không hỏi lý do | Cấu hình "lính thuỷ quân lục chiến xin làm người quan sát" |
| Cách người có thẩm quyền đọc to hồ sơ và trích lại đúng câu nhục mạ ở mở màn | Bài phát biểu của vị tướng, các huân chương, cú bắn 1400 yard |
| Cách bài kết bằng một âm thanh đời thường trong một căn nhà nhỏ | Hiên nhà, trà đá, tiếng ve, luống cà chua |

**Bộ cấu hình golden đã tiêu** — không dựng lại nguyên cụm này, kể cả khi đổi tên:
một giải bắn tỉa quân đội · nhân vật chính là nữ quân nhân da đen giải ngũ · kẻ phán xét là sĩ quan cao cấp chủ nhà của giải · hồ sơ chiến đấu bị niêm phong bởi một vị tướng · mẹ ung thư cần tiền phẫu thuật · giải thưởng tiền mặt đúng bằng số tiền cần · người quan sát đã chết vì mìn · một cú bắn huyền thoại phá vây cứu người · quân cảnh áp giải kẻ phán xét ra khỏi sân.

Một hai yếu tố trùng là bình thường nếu title đòi hỏi. Trùng từ **ba yếu tố trở lên** thì đổi những yếu tố title không ép.

Cấm tái sử dụng: tên người, tên đơn vị, địa danh, con số, biệt danh, câu thoại.

**Danh sách câu đã tiêu.** Ngoài chất liệu, golden còn có khoảng mười lăm **hình dạng câu** đặc trưng — mở màn đóng bằng một trạng từ tuyệt đối, câu bắc cầu "N năm trước buổi sáng đó…", nhịp bốn mệnh đề sở hữu ở cảnh công bố, câu cuối coda. Chúng nằm ở `references/8-vi-du-co-chu-thich.md` mục 10 và **đã được dùng**. Viết lại chúng bằng cách đổi danh từ vẫn là chép. Quét bản nháp theo danh sách đó trước khi qua Cổng 2.

**Đọc lúc nào, đọc bao nhiêu.**

- ⛔ Không nạp cả file theo phản xạ. Mặc định **không đọc** — `8-vi-du-co-chu-thich.md` đã trích sẵn các đoạn tiêu biểu kèm luật rút ra.
- Chỉ mở golden khi có **câu hỏi cụ thể** không tra được trong `references/`, và khi đó **đọc đúng một đoạn** (~40–60 dòng) của phần liên quan.
- Rớt cùng một mục ở Cổng 1 hoặc Cổng 2 hai vòng liền → mở đúng phần tương ứng xem bài chuẩn giải quyết ra sao.
- Đọc xong thì **diễn đạt lại thành nguyên tắc** rồi mới viết. Câu nào trong bản nháp tra ngược được về golden bằng tìm chuỗi ký tự thì viết lại.

**Không được sửa golden project**, kể cả khi thấy lỗi. Chỉ user sửa thủ công. Phát hiện chỗ khả nghi thì báo trong tin nhắn.

## 5. Sáu cách hỏng khi vận dụng skill này

Thể loại có đặc trưng rất rõ, nên rủi ro lớn nhất là mọi bài ra cùng một khuôn.

- **Chép bề mặt golden.** Golden là một hiện thân. Súng, quân đội, huân chương chỉ là *một* cách lấp vào năm động cơ. Hỏi: *nếu đổi hết bối cảnh, bài có còn đủ năm động cơ không?*
- **Nhân bản trình tự.** Nguy hiểm hơn chép chất liệu, vì nó không lộ ra khi đọc. Một bài thử chạy skill này đã cho ra mở màn khớp golden **11 trên 11 khe theo đúng thứ tự**, với tên và nghề hoàn toàn khác — và đọc lên vẫn thấy "ổn". Bảo hiểm duy nhất là **đối chiếu đoạn với đoạn** ở Cổng 1 và đếm chuỗi trùng ở Cổng 2.
- **Coi trục khối là bảng kiểm tuần tự.** `3-cau-truc.md` ghi rõ khối nào bắt buộc, khối nào tuỳ chọn, và số vòng thi co giãn được. Tuỳ chọn là tuỳ chọn thật.
- **Khoá vào một mô-típ.** Người thân bệnh nặng, giải thưởng tiền mặt, người thầy đã chết, clip lan truyền, cuộc điều tra nội bộ — mỗi thứ là một lựa chọn trong nhiều lựa chọn. `5-cong-bo-va-ket.md` và `2-nhan-vat.md` liệt kê các dạng thay thế.
- **Mặc định đấu trường là một cuộc thi.** Đấu trường chỉ cần ba thứ: luật công khai, thước đo ai cũng đọc được, và người xem. Ca trực, kỳ sát hạch, phiên đấu thầu, buổi hội chẩn, cuộc diễn tập, phiên chấm đều đủ điều kiện.
- **Để lộ khung.** Nhãn, số khối, thuật ngữ skill lọt vào file. Xem mục 1.
- **Thuộc luật mà không hiểu lý do.** Mỗi quy tắc trong `references/` đều kèm "vì sao nó chạy". Gặp tình huống lạ thì suy từ lý do, đừng ép tình huống vừa khuôn.
