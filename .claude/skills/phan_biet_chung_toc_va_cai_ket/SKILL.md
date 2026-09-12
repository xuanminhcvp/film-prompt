---
name: phan_biet_chung_toc_va_cai_ket
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~8.000 từ) cho kênh kể chuyện YouTube, thuộc dòng "một người bị sỉ nhục công khai vì định kiến, trong khi chính kẻ sỉ nhục đang sống nhờ vào người đó — rồi sự thật được người khác nói ra, và hậu quả kéo sập cả thế giới của kẻ kia". Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title thuộc dòng này, hoặc yêu cầu viết bài mới / sửa cold open / viết vĩ thanh. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Truyện kể: định kiến, cú lật danh tính, và cái kết

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không có bước nào ở giữa cần user.**

Chạy thẳng theo `references/7-quy-trinh-viet.md`, bước 0 → bước 8, với hai cổng tự duyệt:

```
title → đọc title → dàn nhân vật + đòn bẩy → phác đỉnh sỉ nhục + cú lật → cold open + CTA
                                                                               ↓
                                                                     ⛔ CỔNG 1 (phần H)
                                                                               ↓
                                              thân bài → hệ quả → ⛔ CỔNG 2 (phần A–G)
                                                                               ↓
                                                                    ghi file → báo cáo
```

**Không hỏi user**: không xin duyệt outline, không xin duyệt hook, không hỏi độ dài, bối cảnh hay tên nhân vật. Title không nói gì thì tự quyết theo `7-quy-trinh-viet.md` bước 1.

**Giữ nguyên văn title của user.** Không viết lại, không rút gọn, không "cải thiện" — kể cả khi title có chữ nghe lạ.

Ngoại lệ duy nhất được dừng lại hỏi: chuỗi user dán vào không phải một title.

User yêu cầu thêm (độ dài khác, bối cảnh cụ thể, ngôn ngữ khác) thì áp dụng và vẫn chạy thẳng.

## 1. Hợp đồng đầu ra

Sản phẩm cuối cùng chỉ gồm **đúng hai thành phần**:

1. Dòng đầu tiên: `title: <tiêu đề tiếng Anh>`
2. Phần còn lại là **văn xuôi liền mạch**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn nằm trên một dòng, giữa các đoạn không có dòng trống** — đúng như golden project.

Trong file **không được có**: tiêu đề mục, số cảnh, `SCENE`, `Act`, tên nhịp, ghi chú đạo diễn, gạch đầu dòng, chú thích của người viết, hay bất kỳ thuật ngữ nào của skill này. Outline (nếu cần) nằm trong tin nhắn, không nằm trong file.

**Ngôn ngữ**: trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác.

**Quy mô mặc định**: khoảng 7.500–8.500 từ (golden: ~7.900). User muốn ngắn/dài hơn thì co giãn theo tỉ lệ ở `3-cau-truc.md`, giữ nguyên trật tự.

## 2. Năm động cơ của thể loại

Chi tiết và lý do ở `references/1-nguyen-ly-cot-loi.md`. Tóm tắt:

1. **Sự thật nằm trong tầm tay mà không ai chịu với tới.** Một thao tác kiểm chứng rẻ tiền tồn tại suốt truyện, và bị bỏ qua vì kẻ phán xét đã tin vào mắt mình.
2. **Kẻ phán xét đang tự phá thứ mình sống nhờ.** Sự thật về nhân vật chính có sức nặng trực tiếp lên thế giới của chính kẻ đang sỉ nhục họ.
3. **Sự kiềm chế của nhân vật chính là cốt truyện.** Họ không chứng minh mình, không chống cự, nói ít — và bị đẩy xuống sâu hơn vì điều đó.
4. **Nhân vật chính không tự lật bài.** Người khác nói to sự thật lên, còn khán giả thì đã biết từ trước và chờ khoảnh khắc đó.
5. **Đám đông im lặng, và gần một nửa bài nằm sau cú lật.** Sự im lặng của người đứng nhìn bị đòi lại trong hệ quả; hệ quả không phải phần thu dọn — nó là phần khán giả ở lại để xem.

## 3. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Năm động cơ và lý do chúng chạy. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dựng dàn nhân vật theo **chức năng**; bốn trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Trục khối, tỉ lệ độ dài, cái gì bắt buộc / tuỳ chọn, sổ cài–trả. |
| [4-hook-va-cta.md](references/4-hook-va-cta.md) | Đọc title, viết cold open, câu nhử, CTA mở bài. |
| [5-vi-thanh.md](references/5-vi-thanh.md) | Toàn bộ phần sau cú lật, bài học, câu hỏi và CTA đóng bài. |
| [6-van-phong.md](references/6-van-phong.md) | Định dạng, nhịp câu, giọng người kể, cách nhúng thoại. |
| [7-quy-trinh-viet.md](references/7-quy-trinh-viet.md) | **Quy trình tự động bước 0 → 8.** Mở ngay sau khi nhận title. |
| [8-vi-du-co-chu-thich.md](references/8-vi-du-co-chu-thich.md) | Xem một kỹ thuật trông ra sao trên trang giấy. |
| [9-chu-de-nhay-cam.md](references/9-chu-de-nhay-cam.md) | Viết về định kiến mà không thành nội dung kích động. |
| [10-checklist.md](references/10-checklist.md) | Phần H = Cổng 1 (hook). Phần A–G = Cổng 2 (toàn bài). |
| `golden_project/golden_project_1/KICH-BAN.md` | Bài chuẩn. **Chỉ mở khi có câu hỏi cụ thể, đọc một đoạn.** Xem mục 4. |

## 4. Golden Project

```
golden_project/
└── golden_project_1/KICH-BAN.md   ← ~7.900 từ, đúng định dạng đầu ra
```

Đây là **chuẩn mực sống**: khi `references/` mô tả một luật bằng lời, golden cho thấy luật đó trông ra sao khi đã nằm trên trang giấy. Nếu một luật trong `references/` mâu thuẫn với golden, golden đúng — báo lại cho user trong tin nhắn.

**Hiện chỉ có một bài chuẩn.** Vì vậy mọi con số đo trong skill (số từ cold open, tỉ lệ khối, vị trí cú lật) là **điểm neo lấy từ một mẫu**, không phải ngưỡng. Lệch vừa phải mà bài vẫn chạy thì không sao; lệch nhiều thì phải có lý do nằm trong chính câu chuyện.

**Luật cứng — HỌC CÁCH LÀM, KHÔNG LẤY CHẤT LIỆU.**

| Được lấy | Không được lấy |
|---|---|
| Hình dạng: đỉnh sỉ nhục ở đầu, lùi về gốc, hai vòng leo thang, lật, hệ quả dây chuyền | Chính các tình tiết lấp vào hình dạng đó |
| Cách một người có quyền được giao việc rồi dùng quyền đó sai | Cấu hình "vợ chủ nhà được chồng giao tiếp khách" |
| Cách lời thoại đỉnh điểm xuất hiện ở cold open rồi trở lại nguyên văn ở thân bài | Nguyên câu thoại, nguyên câu tiếng Anh |
| Cách hậu quả nối nhau thành domino, mỗi nấc có mốc giờ và con số | Chuỗi hậu quả cụ thể (cổ phiếu, ngân hàng, phá sản…) |
| Cách nhân vật chính trở về gốc ở cuối bài | Nhân vật người mẹ, cái quỹ mang tên người thân |

**Bộ cấu hình golden đã tiêu** — không dựng lại nguyên cụm này, kể cả khi đổi tên:
một buổi tiệc/hội nghị sang trọng · kẻ sỉ nhục là vợ của người đang cần thương vụ · nhân vật chính là đối tác/nhà đầu tư chưa ai gặp mặt · đổ đồ uống lên người · bảo vệ khách sạn áp giải · một chính khách đến muộn nhận ra · ngân hàng ra tối hậu thư · kiện dân sự ra toà · quỹ mang tên người mẹ.

Một hai yếu tố trùng là bình thường nếu title đòi hỏi. Trùng từ **ba yếu tố trở lên** thì đổi những yếu tố title không ép.

Cấm tái sử dụng: tên người, tên công ty, địa danh, con số, thương hiệu, câu thoại.

**Đọc lúc nào, đọc bao nhiêu.**

- ⛔ Không nạp cả file theo phản xạ. Mặc định **không đọc** — `8-vi-du-co-chu-thich.md` đã trích sẵn các đoạn tiêu biểu kèm luật rút ra.
- Chỉ mở golden khi có **câu hỏi cụ thể** không tra được trong `references/`, và khi đó **đọc đúng một đoạn** (~40–60 dòng) của phần liên quan.
- Rớt cùng một mục ở Cổng 1 hoặc Cổng 2 hai vòng liền → mở đúng phần tương ứng xem bài chuẩn giải quyết ra sao.
- Đọc xong thì **diễn đạt lại thành nguyên tắc** rồi mới viết. Câu nào trong bản nháp tra ngược được về golden bằng tìm chuỗi ký tự thì viết lại.

**Không được sửa golden project**, kể cả khi thấy lỗi. Chỉ user sửa thủ công. Phát hiện chỗ khả nghi thì báo trong tin nhắn.

## 5. Sáu cách hỏng khi vận dụng skill này

Thể loại có đặc trưng rất rõ, nên rủi ro lớn nhất là mọi bài ra cùng một khuôn.

- **Chép bề mặt golden.** Golden là một hiện thân. Tiệc sang, rượu vang, thương vụ tỷ đô chỉ là *một* cách lấp vào năm động cơ. Hỏi: *nếu đổi hết bối cảnh, bài có còn đủ năm động cơ không?*
- **Coi trục khối là bảng kiểm tuần tự.** `3-cau-truc.md` ghi rõ khối nào bắt buộc, khối nào tuỳ chọn. Tuỳ chọn là tuỳ chọn thật.
- **Khoá vào một mô-típ.** Người mẹ tần tảo, vụ kiện ra toà, video lan truyền, cổ phiếu sập, quỹ từ thiện — mỗi thứ là một lựa chọn trong nhiều lựa chọn. `5-vi-thanh.md` liệt kê các dạng thay thế.
- **Mặc định nguồn quyền lực.** Nhân vật chính không phải lúc nào cũng giàu. Đòn bẩy có thể là quyền ký, chuyên môn, lời chứng, một lá phiếu, một vai trò nghi lễ — xem `2-nhan-vat.md`.
- **Để lộ khung.** Nhãn, số khối, thuật ngữ skill lọt vào file. Xem mục 1.
- **Thuộc luật mà không hiểu lý do.** Mỗi quy tắc trong `references/` đều kèm "vì sao nó chạy". Gặp tình huống lạ thì suy từ lý do, đừng ép tình huống vừa khuôn.
