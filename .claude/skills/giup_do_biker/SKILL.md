---
name: giup_do_biker
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~7.500–8.000 từ) cho kênh kể chuyện YouTube, thuộc dòng LÒNG TỐT ĐƯỢC TRẢ VỀ — "một người đang tự chìm mở cửa cho một nhóm người mà cả vùng vừa đóng cửa, rồi cộng đồng của nhóm đó quay lại và dựng lại cả cuộc đời họ". Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title dạng "ai đó giúp / cho trú / cứu một nhóm bị xa lánh — rồi hôm sau cái gì đó xuất hiện trước cửa nhà họ", hoặc yêu cầu viết bài mới / sửa mở màn / viết vĩ thanh cho dòng này. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Lòng tốt được trả về — cánh cửa thứ bảy

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không bước nào ở giữa cần user.**

Chạy theo `references/7-quy-trinh-viet.md`, bước 0 → 8, với hai cổng tự duyệt:

```
title → đọc title, dựng phần title không cho → nhân vật + sổ cài đặt → phác cảnh đền đáp
      → mở màn + hai dòng lời hứa  → ⛔ CỔNG 1
      → thân bài → sự đền đáp → dựng lại → vĩ thanh → vòng khép → ⛔ CỔNG 2
      → ghi file → báo cáo
```

**Không hỏi user** về độ dài, bối cảnh, tên, nhóm người, mùa. Title không nói thì tự quyết. **Giữ nguyên văn title.** Chỉ dừng hỏi khi chuỗi user dán không phải một title. User yêu cầu thêm điều gì thì áp dụng và vẫn chạy thẳng.

## 1. Hợp đồng đầu ra

File chỉ gồm: dòng đầu `title: <tiêu đề tiếng Anh>`, rồi **văn xuôi**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn một dòng, giữa hai đoạn đúng một dòng trống, mỗi lượt thoại một đoạn riêng** (`6-van-phong.md` mục 1). Ngoại lệ về thì chỉ ở hai dòng lời hứa cuối mở màn và ở các câu treo phóng tới tương lai.

**Chỉ tiếng Anh Mỹ trong file.** Không chữ nước ngoài, không phiên âm. Nếu một nhân vật nói bằng thứ tiếng khác, viết câu đó bằng tiếng Anh và gọi tên thứ tiếng trong câu dẫn (*she said in Spanish*) để đội làm video biết câu nào lồng tiếng. Chi tiết: `6-van-phong.md` mục 5.

Không tiêu đề mục, số cảnh, nhãn, ghi chú, gạch đầu dòng, thuật ngữ của skill.

Trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác. Quy mô mặc định khoảng 7.500–8.000 từ; user nói khác thì co giãn theo `3-cau-truc.md` mục 5.

## 2. Sáu động cơ

Lý do thể loại chạy. Chi tiết và "vì sao" ở `references/1-nguyen-ly-cot-loi.md`.

1. **Cánh cửa thứ bảy** — người cần giúp đã bị từ chối nhiều lần, **đếm được**, trước khi tới. Một tiếng "vào đi" chỉ nặng bằng đúng số tiếng "không" đứng sau lưng nó.
2. **Người cho đang tự chìm** — người mở cửa không dư dả; họ có một hạn chót đang đếm ngược sẽ xoá sổ họ. Cho đi lúc đó mới là cho.
3. **Định kiến được thừa nhận, không được miễn trừ** — người tốt cũng nhìn thấy đúng cái cả vùng nhìn thấy, và dừng lại một nhịp thật. Ai giúp mà không do dự thì không chọn gì cả.
4. **Cái nhãn che một sự thật bình thường** — người bị xa lánh hoá ra có nghề, có con, có mạng lưới. Điều đó phải **hé ra qua một nguồn trung lập**, không do người kể bênh vực.
5. **Sự đền đáp là một cộng đồng, không phải một tấm séc** — cái quay lại là số đông có tay nghề, và nó sửa đúng những thứ chưa ai được nghe kể.
6. **Món quà bị đẩy tiếp đi** — người nhận biến nó thành vĩnh viễn và hướng ra ngoài mình; bài đóng bằng chính hành động ban đầu lặp lại với một người lạ mới.

**Luật tuyệt đối**: đỉnh điểm là **một đám đông hiện ra ở ngay nơi của người cho và làm việc bằng tay** — nghe được, đếm được, nhìn thấy được. Không phải một cú điện thoại báo tin tốt, không phải một tấm séc, không phải một bản tin.

## 3. Bất biến và biến số — đọc trước mọi thứ

Skill này rút từ **một** Golden Project. Một điểm dữ liệu không phải quy luật.

- **Bất biến** là sáu động cơ ở trên và các chức năng trong `references/`. Chúng giữ nguyên ở mọi bài.
- **Biến số** là mọi cách hiện thực: nhóm người bị xa lánh là ai, cơn cớ đẩy họ vào đường cùng, nghề và nơi của người cho, thứ người cho sắp mất, khung thời gian, số cánh cửa đã đóng, hình thức đền đáp, quy mô, đạo cụ, câu chữ. Chúng **phải mọc từ title và bối cảnh của bài đang viết**.

Bảng tách hai loại này ở `references/12-pattern-golden.md` mục 1. Khi phân vân, hỏi: *nếu đổi chi tiết này, bài có mất lý do để hay không?* Không mất → nó là biến số, và phải chọn mới.

**Năm lỗi skill này được thiết kế để tránh — người viết cũng phải tránh:**

| Lỗi | Trông ra sao khi viết bài |
|---|---|
| **Overfitting vào Golden** | bài mới là Golden đổi tên: vẫn biker, vẫn mưa bão, vẫn tiệm sửa xe, vẫn bà vợ với cái tạp dề |
| **Khuôn quá cụ thể** | lấp đúng từng nhịp, từng câu của Golden theo thứ tự |
| **Ràng buộc quá chặt** | coi tỉ lệ %, số cánh cửa, số người quay lại, số tuần sửa chữa là chỉ tiêu phải đạt |
| **Khoá trope** | mọi bài đều bão, đều ông bà già, đều đứa cháu sắp vào đại học, đều một tấm biển đồng ở cuối |
| **Rò khuôn** | cụm câu, nhịp câu, hình ảnh nhận ra được là của Golden (`12-pattern-golden.md` mục 3) |

## 4. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Sáu động cơ và vì sao. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dựng nhân vật theo chức năng; sáu trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Tám chặng, hình dạng tổng thể, sổ cài đặt. |
| [4-hook-va-cta.md](references/4-hook-va-cta.md) | Đọc title; mở màn (sáu chức năng); hai dòng lời hứa; mốc lùi. |
| [5-vi-thanh.md](references/5-vi-thanh.md) | Sự đền đáp, dựng lại, món quà, vĩ thanh, vòng khép. |
| [6-van-phong.md](references/6-van-phong.md) | Nhịp câu mảnh, sổ con số, thoại vùng miền, cảm xúc qua bàn tay. |
| [7-quy-trinh-viet.md](references/7-quy-trinh-viet.md) | Quy trình tự động, bước 0 → 8. Mở ngay sau khi nhận title. |
| [8-vi-du-co-chu-thich.md](references/8-vi-du-co-chu-thich.md) | Kỹ thuật trong Golden, chỉ tới dòng cụ thể, kèm thứ không được mang đi. |
| [9-chu-de-nhay-cam.md](references/9-chu-de-nhay-cam.md) | Định kiến nhóm, chủng tộc, nhãn xã hội — viết mà không kích động. |
| [10-checklist.md](references/10-checklist.md) | Phần H = Cổng 1. Phần A–G = Cổng 2. |
| [11-cau-treo.md](references/11-cau-treo.md) | Câu treo phóng tới tương lai — công cụ đặc trưng của dòng này. |
| [12-pattern-golden.md](references/12-pattern-golden.md) | Golden đã làm gì; bảng tách nguyên lý / lựa chọn; danh sách chữ ký không được dùng lại. |

## 5. Golden Project

`GOLDEN-1.txt` là Golden Project duy nhất — **chỉ đọc, không bao giờ sửa**.

**Một chỗ Golden KHÔNG phải chuẩn** — luật của user thắng: Golden viết liền không dòng trống; chuẩn là một dòng trống giữa các đoạn.

- **Đọc L2–16 ngay trước khi viết mở màn**, và **đọc một mảng dài ở giữa bài một lần trước khi viết thân bài**. Nhịp câu mảnh và mật độ chi tiết của thể loại này không mô tả trọn được bằng luật — phải nghe.
- **Đọc để lấy nhịp, rồi đóng lại.** Không mở lại trong lúc viết, để khỏi chép.
- Golden minh hoạ **cách lấp các chức năng**, không phải kho cốt truyện, không phải kho câu.

## 6. Bảy lỗi khi vận dụng skill

- **Chép câu chữ hoặc vỏ câu** của Golden hay của các ví dụ trong `references/`.
- **Coi tám chặng là danh sách cảnh.** Chặng là chức năng; một chặng có thể là một cảnh hay nhiều cảnh.
- **Chọn biến số theo Golden thay vì theo title.**
- **Để lộ khung** trong file bàn giao.
- **Để người cho không do dự một nhịp nào** — mất động cơ 3, nhân vật thành thánh, không còn là lựa chọn.
- **Biến sự đền đáp thành tiền** — một tấm séc lớn giết cả đoạn cuối; cái phải quay lại là người và tay nghề.
- **Giảng bài** — người kể nói hộ ý nghĩa thay vì để một nhân vật nói bằng giọng của họ, hoặc để một hành động nói thay.
- **Tin vào cảm giác về nhịp câu thay vì đếm.** Đây là lỗi trượt thường xuyên nhất khi chạy thử: bài đúng cấu trúc, đúng sáu động cơ, mà câu dài hơn Golden 60%. Người viết không tự nghe ra được. **Phải chạy đoạn đo ở `6-van-phong.md` mục 3b** ở cả hai cổng.
- **Thuộc lòng luật thay vì hiểu lý do.** Mỗi luật trong `references/` kèm một câu vì sao. Gặp tình huống lạ, bám vào lý do mà suy ra.
