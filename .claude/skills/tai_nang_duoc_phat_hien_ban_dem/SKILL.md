---
name: tai_nang_duoc_phat_hien_ban_dem
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~7.500–8.000 từ) cho kênh kể chuyện YouTube, thuộc dòng TÀI NĂNG ĐƯỢC PHÁT HIỆN BAN ĐÊM — "một người ở đáy mang cái nhãn thấp (thực tập sinh, bảo vệ, lao công, người không bằng cấp…) bị kẻ gác cổng dập trước đám đông, rồi lúc nửa đêm, khi không ai giao việc, tự tay giải bài toán mà cả đội có chức danh bó tay — và một người có quyền cao hơn bắt gặp đúng lúc đó". Phục vụ mọi loại tài năng — sửa máy, điện, IT, y khoa, nấu ăn, âm nhạc, toán, xây dựng… Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title dạng "Tỉ phú / CEO / chủ … lúc 2AM–4AM bắt gặp X đang sửa / cứu / làm điều N chuyên gia không làm được", hoặc "X bị cười nhạo — nửa đêm ông chủ thấy X …", hoặc yêu cầu viết bài mới / sửa mở màn / viết vĩ thanh cho dòng này. Title tài năng NGÔN NGỮ (bị chế nhạo bằng thứ tiếng tưởng họ không hiểu) thì dùng tai_nang_ngon_ngu. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Tài năng được phát hiện ban đêm — cái nhãn nói dối, bài toán không ai giải được, và người thức cùng giờ

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không bước nào ở giữa cần user.**

Chạy theo `references/7-quy-trinh-viet.md`, bước 0 → 8, với hai cổng tự duyệt:

```
title → đọc title, dựng phần title không cho → dựng LỜI GIẢI THẬT của bài toán
      → nhân vật + sổ cài đặt → phác cảnh bắt gặp và cảnh công nhận
      → mở màn + hook → ⛔ CỔNG 1
      → thân bài → trình diễn → bắt gặp → công nhận & sụp đổ → vĩ thanh → khối đóng bài → ⛔ CỔNG 2
      → ghi file → báo cáo
```

**Không hỏi user** về độ dài, bối cảnh, tên, nghề. Title không nói thì tự quyết. **Giữ nguyên văn title.** Chỉ dừng hỏi khi chuỗi user dán không phải một title. User yêu cầu thêm điều gì thì áp dụng và vẫn chạy thẳng.

**Phân tuyến**: title tài năng ngôn ngữ — kẻ có quyền khinh người ở đáy bằng một thứ tiếng hắn tưởng họ không hiểu — thì chuyển sang skill `tai_nang_ngon_ngu`. Mọi tài năng khác ở đây.

## 1. Hợp đồng đầu ra

File chỉ gồm: dòng đầu `title: <tiêu đề tiếng Anh>`, rồi **văn xuôi**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn một dòng, giữa hai đoạn đúng một dòng trống, mỗi lượt thoại một đoạn riêng** (`6-van-phong.md` mục 1). Ngoại lệ về ngôi và thì chỉ ở lời rủ tương tác đầu bài và khối đóng bài cuối bài.

**Chỉ tiếng Anh Mỹ trong file.** Nếu có nhân vật nói tiếng nước ngoài, câu đó viết bằng tiếng Anh và tự gọi tên thứ tiếng trong câu dẫn (*he said in Spanish*) — `6-van-phong.md` mục 5.1.

Không tiêu đề mục, số cảnh, nhãn, ghi chú, gạch đầu dòng, thuật ngữ của skill.

Trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác. Quy mô mặc định khoảng 7.500–8.000 từ; user nói khác thì co giãn theo `3-cau-truc.md` mục 5.

## 2. Bảy động cơ

Lý do thể loại chạy. Chi tiết và "vì sao" ở `references/1-nguyen-ly-cot-loi.md`.

1. **Cái nhãn nói dối** — thế giới đọc nhân vật chính bằng một cái nhãn (thẻ, đồng phục, thiếu bằng cấp). Người xem được thấy thứ cái nhãn che đi, từ rất sớm.
2. **Bài toán mà chức danh bó tay** — một vấn đề cụ thể, đo được, có đồng hồ tiền/giờ đang chạy, mà cả đội có chức danh đã thua — vì họ nhìn sai chỗ, không vì họ dốt.
3. **Tài năng có gốc và có phương pháp riêng** — học từ đáy, từ một người trao nghề, từ lâu trước truyện; nó là **một cách nhìn khác** với cách nhìn chính thức, không chỉ là "giỏi hơn". Có một rào cản chính thức chặn nó.
4. **Lộ sớm, bị dập trước đám đông — leo nhiều nấc** — tài năng lộ ra và được sự thật xác nhận; chính điều đó biến kẻ gác cổng thành kẻ thù. Trong cảnh bị dập, hắn hạ cô **ít nhất ba nấc liền, nấc sau nặng hơn nấc trước** — chế giễu, cắt lời bằng cái nhãn và giao việc hèn trước mặt mọi người, làm nhục **vật mang tài năng** — và căn phòng đổi từ cười sang im lặng.
5. **Đêm: việc thật làm khi không ai thấy, rồi bị bắt gặp** — giữa đêm, lúc người có chức danh đã về, không ai giao và không ai cấm, cô tự tay giải bài toán, có rủi ro. Một người có quyền cao hơn — cũng đang thức vì cùng bài toán — bắt gặp đúng lúc đó và tự kiểm. Sáng hôm sau, cô tự giải thích trước đám đông.
6. **Quyết định của hắn là bằng chứng** — thứ hạ kẻ gác cổng là chính chẩn đoán sai, chữ ký, lời dập của hắn. Nhân vật chính không tố ai; **người từng im lặng tự đứng lên nói ra sự thật, trong phòng**, không để người phán quyết kể hộ.
7. **Người trao nghề** — người đã đưa tài năng vào tay nhân vật chính. Người xem cảm được họ suốt bài qua một phương pháp, một câu nói, một nghi thức; và lời cuối của truyện trao cho họ.

**Luật tuyệt đối**: tài năng thắng bằng **một việc thật chạy được** — cái máy chạy, bệnh nhân thở, món ăn được nếm — rồi được **chính nhân vật chính giải thích trước đám đông**. Không ai nói hộ; không lời khen suông thay cho kết quả.

## 3. Bất biến và biến số — đọc trước mọi thứ

Skill này rút từ **một** Golden Project. Một điểm dữ liệu không phải quy luật.

- **Bất biến** là bảy động cơ ở trên và các chức năng trong `references/` — **kể cả việc thật diễn ra trong đêm và cuộc bắt gặp diễn ra trong đêm**. Chúng giữ nguyên ở mọi bài.
- **Biến số** là mọi cách hiện thực: loại tài năng, nghề, bối cảnh, thân phận, bài toán, cách bị dập, vật mang tài năng, người trao nghề và nghi thức của họ, **loại đêm** (ca trực vắng, đêm trước hạn chót, đêm bão, đêm mất điện, đêm sau buổi tiệc), giờ cụ thể, ai bắt gặp và vì sao họ thức lúc đó, hình thức công nhận, câu chữ. Chúng **phải mọc từ title và bối cảnh của bài đang viết**.

Bảng tách hai loại này ở `references/12-pattern-golden.md` mục 1. Khi phân vân, hỏi: *nếu đổi chi tiết này, bài có mất lý do để hay không?* Không mất → nó là biến số, và phải chọn mới.

**Năm lỗi skill này được thiết kế để tránh — người viết cũng phải tránh:**

| Lỗi | Trông ra sao khi viết bài |
|---|---|
| **Overfitting vào Golden** | bài mới là Golden đổi nghề: vẫn cuốn sổ bị ném, vẫn ông chủ đi tuần theo thói quen lúc bốn giờ, vẫn học bổng |
| **Khuôn quá cụ thể** | lấp đúng từng nhịp của Golden theo thứ tự — ba "task", một hồi tưởng giữa lúc sửa, một cuộc gọi cho ông ở bãi xe, **cảnh đối chất đúng trình tự Golden** (giá → cãi quy trình → kể lại → "đúng không?" → cãi tư cách → điều tra) |
| **Ràng buộc quá chặt** | coi tỉ lệ %, số bước, số lần nhắc vật là chỉ tiêu phải đạt |
| **Khoá trope** | mọi bài đều là máy móc, đều cùng một loại đêm (nhà máy vắng tanh), đều người thầy là ông bà, đều họp toàn công ty |
| **Rò khuôn** | cụm câu, nhịp câu, hình ảnh nhận ra được là của Golden (`12-pattern-golden.md` mục 3) |

## 4. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Bảy động cơ và vì sao. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dựng nhân vật theo chức năng; tám trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Tám chặng, hình dạng tổng thể, sổ cài đặt. |
| [4-hook-va-cta.md](references/4-hook-va-cta.md) | Đọc title; mở màn (sáu chức năng); câu trớ trêu, lời rủ, câu đưa về đầu. |
| [5-vi-thanh.md](references/5-vi-thanh.md) | Trình diễn, bắt gặp, công nhận, sụp đổ, vĩ thanh, khối đóng bài. |
| [6-van-phong.md](references/6-van-phong.md) | Nhịp câu, hình ảnh, cách viết một tài năng cho người ngoài nghề. |
| [7-quy-trinh-viet.md](references/7-quy-trinh-viet.md) | Quy trình tự động, bước 0 → 8. Mở ngay sau khi nhận title. |
| [8-vi-du-co-chu-thich.md](references/8-vi-du-co-chu-thich.md) | Kỹ thuật trong Golden, chỉ tới dòng cụ thể, kèm thứ không được mang đi. |
| [9-chu-de-nhay-cam.md](references/9-chu-de-nhay-cam.md) | Chủng tộc, giai cấp, bằng cấp — viết mà không kích động. |
| [10-checklist.md](references/10-checklist.md) | Phần H = Cổng 1. Phần A–G = Cổng 2. |
| [11-cau-treo.md](references/11-cau-treo.md) | Câu treo cuối chặng và câu đẩy cuối đoạn. |
| [12-pattern-golden.md](references/12-pattern-golden.md) | Golden đã làm gì; bảng tách nguyên lý / lựa chọn; danh sách chữ ký không được dùng lại. |
| [scripts/kiem-do-dai.py](scripts/kiem-do-dai.py) | **Chạy ở cả hai cổng.** Đếm từ mở màn, lời rủ, toàn bài; soát dòng trống và ký tự ngoài tiếng Anh. Không đếm bằng mắt. |

## 5. Golden Project

`GOLDEN-1.txt` là Golden Project duy nhất — **chỉ đọc, không bao giờ sửa**. Thực tập sinh da đen 19 tuổi sửa cỗ máy CNC hai triệu đô mà mười hai kỹ sư tuyên bố đã chết. ~7.800 từ.

**Hai chỗ Golden KHÔNG phải chuẩn** — luật thắng Golden:
- Golden viết liền không dòng trống. Chuẩn: dòng trống giữa các đoạn.
- Mở màn của Golden lệch nhẹ với cảnh ở thân bài (mở màn: Avery còn đang sửa khi ông chủ tới; thân bài: máy đã chạy, Avery ngồi chờ). Chuẩn: mở màn **khớp** cảnh thật ở thân bài.

- **Đọc L1–14 ngay trước khi viết mở màn**, và **đọc tới L72 một lần trước khi viết thân bài**. Nhịp câu và mật độ chi tiết của thể loại này không mô tả trọn được bằng luật — phải nghe.
- **Đọc để lấy nhịp, rồi đóng lại.** Không mở lại trong lúc viết, để khỏi chép.
- Golden minh hoạ **cách lấp các chức năng**, không phải kho cốt truyện, không phải kho câu.

## 6. Mười lỗi khi vận dụng skill

- **Chép câu chữ hoặc vỏ câu** của Golden hay của các ví dụ trong `references/`.
- **Cảnh bị dập chỉ một hai nấc** — cười rồi phá vật là hết. Người xem chưa kịp giận đủ thì cú dập đã xong, và cả nửa sau thiếu lực trả nợ (`3-cau-truc.md` chặng 2).
- **Người im lặng được kể hộ** — người phán quyết thuật lại lời họ thay vì để họ tự đứng lên. Món nợ của căn phòng khi đó được trả gián tiếp, và cảnh đối chất trượt về trình tự Golden (`5-vi-thanh.md` mục 4).
- **Coi tám chặng là danh sách cảnh.** Chặng là chức năng; một chặng có thể là một cảnh hay nhiều cảnh.
- **Chọn biến số theo Golden thay vì theo title.**
- **Lời giải giả.** Bài toán được giải bằng một câu mơ hồ ("cô chỉnh vài thứ và nó chạy") hoặc bằng một cơ chế sai về chuyên môn. Người trong nghề xem kênh sẽ nghe ra ngay, và phần trình diễn — chỗ dài nhất bài — sụp.
- **Để lộ khung** trong file bàn giao.
- **Viết thành hồ sơ** — tài năng kể bằng thuật ngữ thay vì bằng tay, tai, mắt; con số hồ sơ thay con số chạm được.
- **Dựng không gian mơ hồ hoặc chật** — người nghe không biết ai đứng đâu (`6-van-phong.md` mục 5b).
- **Thuộc lòng luật thay vì hiểu lý do.** Mỗi luật trong `references/` kèm một câu vì sao. Gặp tình huống lạ, bám vào lý do mà suy ra.
