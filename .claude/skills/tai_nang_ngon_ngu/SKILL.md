---
name: tai_nang_ngon_ngu
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~7.500–8.000 từ) cho kênh kể chuyện YouTube, thuộc dòng TÀI NĂNG NGÔN NGỮ — "một người ở đáy bị kẻ có quyền khinh miệt bằng một thứ tiếng hắn tưởng họ không hiểu, rồi họ mở miệng và lật ván bằng chính lời hắn". Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title thuộc dòng này (người phục vụ/lao công/tài xế... nói nhiều thứ tiếng, bị chế nhạo bằng tiếng nước ngoài), hoặc yêu cầu viết bài mới / sửa mở màn / viết vĩ thanh cho dòng này. Chỉ phục vụ tài năng ngôn ngữ. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Tài năng ngôn ngữ — căn phòng kín bị mở khoá

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không bước nào ở giữa cần user.**

Chạy theo `references/7-quy-trinh-viet.md`, bước 0 → 8, với hai cổng tự duyệt:

```
title → đọc title, dựng phần title không cho → nhân vật + sổ cài đặt → phác cao trào
      → mở màn + hook  → ⛔ CỔNG 1
      → thân bài → trình diễn → vĩ thanh → khối đóng bài → ⛔ CỔNG 2
      → ghi file → báo cáo
```

**Không hỏi user** về độ dài, bối cảnh, tên, thứ tiếng. Title không nói thì tự quyết. **Giữ nguyên văn title.** Chỉ dừng hỏi khi chuỗi user dán không phải một title. User yêu cầu thêm điều gì thì áp dụng và vẫn chạy thẳng.

## 1. Hợp đồng đầu ra

File chỉ gồm: dòng đầu `title: <tiêu đề tiếng Anh>`, rồi **văn xuôi**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn một dòng, giữa hai đoạn đúng một dòng trống, mỗi lượt thoại một đoạn riêng** (`6-van-phong.md` mục 1). Ngoại lệ về ngôi và thì chỉ ở phần hook đầu bài và khối đóng bài cuối bài.

**Chỉ tiếng Anh Mỹ trong file.** Không câu tiếng gốc, không phiên âm, không kính ngữ nước ngoài — kể cả ở cao trào. Câu nhân vật nói bằng tiếng nước ngoài viết bằng tiếng Anh, và **mỗi câu tự gọi tên thứ tiếng trong câu dẫn** (*he said in Japanese*) để đội làm video biết câu nào lồng tiếng. Chi tiết: `6-van-phong.md` mục 5.1.

Không tiêu đề mục, số cảnh, nhãn, ghi chú, gạch đầu dòng, thuật ngữ của skill.

Trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác. Quy mô mặc định khoảng 7.500–8.000 từ; user nói khác thì co giãn theo `3-cau-truc.md` mục 5.

## 2. Sáu động cơ

Lý do thể loại chạy. Chi tiết và "vì sao" ở `references/1-nguyen-ly-cot-loi.md`.

1. **Căn phòng kín** — kẻ có quyền có một thứ tiếng hắn tin là không ai trong tầm nghe hiểu, và nói thật ở đó. Người xem biết điều hắn không biết.
2. **Tài năng học bằng tai, từ đáy** — có thật, tự học, có từ lâu, bị một rào cản chính thức chặn lại.
3. **Lộ sớm, giữ vũ khí** — tài năng được người ngoài xác nhận từ sớm; đúng thứ tiếng sẽ lật ván được giữ tới cao trào.
4. **Con tin thuộc về người khác** — lời bí mật hại một người ngoài nhân vật chính; mạnh nhất khi đó là người đã im lặng lúc cô bị khinh.
5. **Lời của hắn là bằng chứng** — thứ hạ phản diện là chính những gì hắn đã nói.
6. **Người đã trả giá** — có người hy sinh để tài năng tồn tại; người xem cảm được họ suốt bài, và cảnh cuối trao cho họ.

**Luật tuyệt đối**: đỉnh điểm là **một con người lên tiếng trước đám đông**, không phải một người đọc văn bản hay bật ghi âm.

## 3. Bất biến và biến số — đọc trước mọi thứ

Skill này rút từ **một** Golden Project. Một điểm dữ liệu không phải quy luật.

- **Bất biến** là sáu động cơ ở trên và các chức năng trong `references/`. Chúng giữ nguyên ở mọi bài.
- **Biến số** là mọi cách hiện thực: thứ tiếng, bối cảnh, thân phận, khung thời gian, loại hại, người bị hại, đường dây của người đã trả giá, số nấc leo thang, cách phản diện cố thoát, hình thức công nhận, đạo cụ, câu chữ. Chúng **phải mọc từ title và bối cảnh của bài đang viết**.

Bảng tách hai loại này ở `references/12-pattern-golden.md` mục 1. Khi phân vân, hỏi: *nếu đổi chi tiết này, bài có mất lý do để hay không?* Không mất → nó là biến số, và phải chọn mới.

**Năm lỗi skill này được thiết kế để tránh — người viết cũng phải tránh:**

| Lỗi | Trông ra sao khi viết bài |
|---|---|
| **Overfitting vào Golden** | bài mới là Golden đổi tên: vẫn nhà hàng, vẫn hợp đồng, vẫn vật của mẹ trong túi |
| **Khuôn quá cụ thể** | lấp đúng từng nhịp, từng câu của Golden theo thứ tự |
| **Ràng buộc quá chặt** | coi tỉ lệ %, số thứ tiếng, số lần nhắc là chỉ tiêu phải đạt |
| **Khoá trope** | mọi bài đều một buổi tối, đều chạy trốn qua ba thứ tiếng, đều vỗ tay, đều đóng khung một vật |
| **Rò khuôn** | cụm câu, nhịp câu, hình ảnh nhận ra được là của Golden (`12-pattern-golden.md` mục 3) |

## 4. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Sáu động cơ và vì sao. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dựng nhân vật theo chức năng; sáu trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Tám chặng, hình dạng tổng thể, sổ cài đặt. |
| [4-hook-va-cta.md](references/4-hook-va-cta.md) | Đọc title; mở màn (sáu chức năng); câu hook, lời rủ, mốc lùi. |
| [5-vi-thanh.md](references/5-vi-thanh.md) | Trình diễn, sụp đổ, được nhìn thấy, vĩ thanh, khối đóng bài. |
| [6-van-phong.md](references/6-van-phong.md) | Nhịp câu, hình ảnh, cách viết tài năng ngôn ngữ cho người không biết thứ tiếng đó. |
| [7-quy-trinh-viet.md](references/7-quy-trinh-viet.md) | Quy trình tự động, bước 0 → 8. Mở ngay sau khi nhận title. |
| [8-vi-du-co-chu-thich.md](references/8-vi-du-co-chu-thich.md) | Kỹ thuật trong Golden, chỉ tới dòng cụ thể, kèm thứ không được mang đi. |
| [9-chu-de-nhay-cam.md](references/9-chu-de-nhay-cam.md) | Chủng tộc, quốc tịch, thân phận — viết mà không kích động. |
| [10-checklist.md](references/10-checklist.md) | Phần H = Cổng 1. Phần A–G = Cổng 2. |
| [11-cau-treo.md](references/11-cau-treo.md) | Câu treo cuối chặng và câu đẩy cuối đoạn. |
| [12-pattern-golden.md](references/12-pattern-golden.md) | Golden đã làm gì; bảng tách nguyên lý / lựa chọn; danh sách chữ ký không được dùng lại. |

## 5. Golden Project

`GOLDEN-1.txt` là Golden Project duy nhất — **chỉ đọc, không bao giờ sửa**.

**Hai chỗ Golden KHÔNG phải chuẩn** — luật của user thắng: Golden viết liền không dòng trống (chuẩn: dòng trống giữa các đoạn), và Golden viết câu tiếng gốc ở cao trào (chuẩn: chỉ tiếng Anh, có nhãn thứ tiếng).

- **Đọc L1–16 ngay trước khi viết mở màn**, và **đọc nửa đầu bài một lần trước khi viết thân bài**. Nhịp câu và mật độ hình ảnh của thể loại này không mô tả trọn được bằng luật — phải nghe.
- **Đọc để lấy nhịp, rồi đóng lại.** Không mở lại trong lúc viết, để khỏi chép.
- Golden minh hoạ **cách lấp các chức năng**, không phải kho cốt truyện, không phải kho câu.

## 6. Bảy lỗi khi vận dụng skill

- **Chép câu chữ hoặc vỏ câu** của Golden hay của các ví dụ trong `references/`.
- **Coi tám chặng là danh sách cảnh.** Chặng là chức năng; một chặng có thể là một cảnh hay nhiều cảnh.
- **Chọn biến số theo Golden thay vì theo title.**
- **Để lộ khung** trong file bàn giao.
- **Viết thành hồ sơ** — âm mưu của phản diện kể bằng điều khoản thay vì bằng giọng hắn; con số hồ sơ thay con số chạm được.
- **Để chữ nước ngoài lọt vào file**, hoặc để một câu nói tiếng nước ngoài không mang nhãn thứ tiếng.
- **Dựng không gian mơ hồ hoặc chật** — người nghe không biết ai ngồi đâu (`6-van-phong.md` mục 5b).
- **Thuộc lòng luật thay vì hiểu lý do.** Mỗi luật trong `references/` kèm một câu vì sao. Gặp tình huống lạ, bám vào lý do mà suy ra.
