---
name: tai_nang_bi_lam_tro_cuoi_truoc_dam_dong
description: Dán một title vào là ra nguyên kịch bản. Viết truyện kể bằng văn xuôi tiếng Anh (~7.500–8.000 từ) cho kênh kể chuyện YouTube, thuộc dòng TÀI NĂNG BỊ LÀM TRÒ CƯỜI TRƯỚC ĐÁM ĐÔNG — "một người mang cái nhãn thấp (lao công, phục vụ, bảo vệ, người không bằng cấp…) bị kẻ gác cổng lôi ra giữa một căn phòng đông người để mua vui, bị ấn vào tay đúng bài toán mà người có chức danh đã thua — và giải nó ngay tại chỗ, trong vài phút, trước mặt tất cả. Kẻ gác cổng thua ở nghề nên trả đũa bằng quyền hành chính: dựng một cuộc thi công khai để loại cô, rồi khoá từng cánh cửa. Cuối cùng chính năng lực bị hắn chế nhạo là thứ đọc ra rằng nền móng sự nghiệp của hắn là đồ đi mượn." Phục vụ mọi loại tài năng — toán, y khoa, nấu ăn, âm nhạc, kỹ thuật, lập trình, ngôn ngữ ký hiệu, cờ, kiến trúc… Chạy tự động từ title tới file, tự duyệt qua hai cổng, không hỏi lại user. Dùng skill này khi user dán một title dạng "giáo sư / bếp trưởng / chủ tịch bắt X giải / làm thử để cho vui — X hoàn thành trong N phút", "X bị sỉ nhục giữa hội trường rồi khiến cả phòng câm lặng", hoặc yêu cầu viết bài mới / sửa mở màn / viết phần công bố và cái kết cho dòng này. Title tài năng NGÔN NGỮ (bị chế nhạo bằng thứ tiếng tưởng họ không hiểu) dùng tai_nang_ngon_ngu; title "im lặng ghi danh một đấu trường rồi quá khứ niêm phong được công bố" dùng tai_nang_bi_khinh_tren_dau_truong; title "nửa đêm bị người có quyền bắt gặp đang làm việc" dùng tai_nang_duoc_phat_hien_ban_dem. Đầu ra là văn xuôi liền mạch, KHÔNG phải kịch bản phân cảnh.
---

# Tài năng bị làm trò cười trước đám đông — sân khấu do kẻ khinh mình dựng lên

## 0. Chế độ chạy

**User dán một title. Skill trả về một file kịch bản hoàn chỉnh. Không bước nào ở giữa cần user.**

Chạy theo `references/7-quy-trinh-viet.md`, bước 0 → 8, với hai cổng tự duyệt:

```
title → đọc title, dựng phần title không cho → dựng BÀI TOÁN THẬT và LỜI GIẢI THẬT
      → nhân vật + sổ cài đặt → phác cảnh sỉ nhục và cảnh công bố cuối
      → mở màn + hook → ⛔ CỔNG 1
      → thế giới → sỉ nhục & chứng minh tại chỗ → cái giá của việc được nhìn thấy
      → bóp nghẹt → vết nứt → đáy & người bảo lãnh → đấu trường → công bố & sụp đổ
      → vĩ thanh → khối đóng bài → ⛔ CỔNG 2
      → ghi file → báo cáo
```

**Không hỏi user** về độ dài, bối cảnh, tên, nghề. Title không nói thì tự quyết. **Giữ nguyên văn title.** Chỉ dừng hỏi khi chuỗi user dán không phải một title. User yêu cầu thêm điều gì thì áp dụng và vẫn chạy thẳng.

**Phân tuyến** — bốn dòng tài năng dễ lẫn, phân bằng **cách tài năng lộ ra**:

| Tài năng lộ ra vì… | Skill |
|---|---|
| kẻ có quyền lôi họ ra làm trò cười và tự trao cho họ sân khấu | **skill này** |
| họ tự ghi danh một đấu trường và im lặng đi tới cùng | `tai_nang_bi_khinh_tren_dau_truong` |
| họ làm việc lúc không ai thấy và bị người có quyền bắt gặp | `tai_nang_duoc_phat_hien_ban_dem` |
| kẻ có quyền khinh họ bằng một thứ tiếng tưởng họ không hiểu | `tai_nang_ngon_ngu` |

## 1. Hợp đồng đầu ra

File chỉ gồm: dòng đầu `title: <tiêu đề tiếng Anh>`, rồi **văn xuôi**, ngôi thứ ba, thì quá khứ. **Mỗi đoạn một dòng, giữa hai đoạn đúng một dòng trống, mỗi lượt thoại một đoạn riêng** (`6-van-phong.md` mục 1). Ngoại lệ về ngôi và thì chỉ ở lời rủ tương tác đầu bài và khối đóng bài cuối bài.

**Chỉ tiếng Anh Mỹ trong file.** Nếu có nhân vật nói tiếng nước ngoài, câu đó viết bằng tiếng Anh và tự gọi tên thứ tiếng trong câu dẫn (*he said in Spanish*) — `6-van-phong.md` mục 5.1.

Không tiêu đề mục, số cảnh, nhãn, ghi chú, gạch đầu dòng, thuật ngữ của skill.

Trao đổi với user bằng **tiếng Việt**. Bài viết bằng **tiếng Anh Mỹ**, trừ khi user yêu cầu khác. Quy mô mặc định khoảng 7.500–8.000 từ; user nói khác thì co giãn theo `3-cau-truc.md` mục 5.

## 2. Bảy động cơ

Lý do thể loại chạy. Chi tiết và "vì sao" ở `references/1-nguyen-ly-cot-loi.md`.

1. **Cái nhãn nói dối, và một quá khứ bị cắt ngang** — thế giới đọc nhân vật chính bằng một cái nhãn nhìn thấy được. Nhưng tài năng của cô **đã từng được thế giới xác nhận một lần**, rồi bị một biến cố ngoài ý muốn lấy mất. Cô không phải người chưa ai biết; cô là người đã bị bỏ lại.
2. **Nghi thức giữ nghề trong bóng tối** — sau ca làm, không khán giả, không phần thưởng, cô vẫn hành nghề. Có một chỗ cất, một vật mang tài năng, một giờ cố định. Đây là bằng chứng sớm nhất và im lặng nhất rằng tài năng là thật.
3. **Sỉ nhục công khai tự mở cửa** — kẻ gác cổng lôi cô ra giữa đám đông để mua vui, và **chính hắn ấn công cụ vào tay cô**. Hắn trao sân khấu vì hắn chắc chắn cô sẽ thất bại. Món nợ và cơ hội sinh ra trong cùng một câu nói.
4. **Chứng minh tại chỗ, hai lần, dưới thước đo của nghề** — lần đầu bị gọi là ăn may hoặc chép; lần hai diễn ra dưới **điều kiện do chính kẻ gác cổng đặt ra**, và được **một người trong nghề không thuộc phe nào** xác nhận bằng từ ngữ khen nặng nhất của nghề đó. Cô không cãi một câu nào.
5. **Hắn thua ở nghề nên trả đũa bằng quyền hành chính** — lịch làm việc, quyền truy cập, chính sách, thư gửi cấp trên, tịch thu vật mang tài năng. Mỗi đòn để lại một dấu vết có chữ ký. Và hắn dựng **một đấu trường có luật và một vụ cược** để thanh toán cô một lần cho xong.
6. **Người đã thấy và đã im lặng** — một người có thẩm quyền (thường là thẩm quyền cũ) đã bắt gặp nghi thức trong bóng tối từ trước và **không nói gì**. Họ giúp bằng những việc không ký tên, rồi tới lúc phải ký tên — và phải trả giá cho chính sự im lặng của mình, công khai.
7. **Nền móng đi mượn** — thứ hạ kẻ gác cổng không phải lời tố cáo, mà là **một lỗi kiểm chứng được nằm trong chính công trình đã làm nên hắn**, do đúng cái năng lực hắn chế nhạo tìm ra. Hắn không bị vạch mặt; hắn bị **đọc**.

**Luật tuyệt đối**: tài năng thắng bằng **một thước đo công khai mà phía bên kia đã chấp nhận trước**, và lời buộc tội cuối cùng phải là **một sự kiện kiểm chứng được do chính nhân vật chính tìm ra bằng nghề của mình** — không phải một bí mật rơi từ trên xuống, không phải lời kể của ai đó.

**Luật về sự im lặng**: nhân vật chính nói rất ít, và số lần cô nói là đếm được. Câu đầu tiên cô nói thẳng với kẻ gác cổng phải **rơi đúng vào chỗ nó đổi thế trận** — và là một câu hỏi về điều kiện, không phải một lời tự vệ.

## 3. Bất biến và biến số — đọc trước mọi thứ

Skill này rút từ **một** Golden Project. Một điểm dữ liệu không phải quy luật.

- **Bất biến** là bảy động cơ ở trên và các chức năng trong `references/` — **kể cả việc màn chứng minh diễn ra công khai, ngay tại chỗ, do kẻ gác cổng ép mở, và diễn ra hai lần** — lần sau dưới điều kiện do chính hắn đặt. *Hình thức* của cả hai lần thì hoàn toàn là biến số.
- **Biến số** là mọi cách hiện thực: loại tài năng, nghề, bối cảnh, thân phận, cái đã cắt ngang đời cô, bài toán, loại phòng, cách sỉ nhục, vật mang tài năng, nghi thức, người xác nhận, hình thức đấu trường, cách hắn bóp nghẹt, loại lỗi trong nền móng của hắn, ai là người đã im lặng, cái kết. Chúng **phải mọc từ title và bối cảnh của bài đang viết**.

Bảng tách hai loại này ở `references/12-pattern-golden.md` mục 1. Khi phân vân, hỏi: *nếu đổi chi tiết này, bài có mất lý do để hay không?* Không mất → nó là biến số, và phải chọn mới.

**Sáu lỗi skill này được thiết kế để tránh — người viết cũng phải tránh:**

| Lỗi | Trông ra sao khi viết bài |
|---|---|
| **Overfitting vào Golden** | bài mới là Golden đổi nghề: vẫn phấn và bảng đen, vẫn ba phút, vẫn giáo sư, vẫn em gái, vẫn giấy giấu trong giày |
| **Khuôn quá cụ thể** | lấp đúng từng nhịp của Golden theo thứ tự — đúng ba đòn bóp nghẹt, đúng ba vòng thi, món quà thầm lặng rơi xuống đúng ngày thứ mười bốn |
| **Ràng buộc quá chặt** | coi tỉ lệ %, số vòng, số phút trong title là chỉ tiêu phải đạt |
| **Khoá trope** | mọi bài đều là học thuật, đều có video lan truyền, đều có người bảo trợ là tiền nhiệm về hưu, đều kết bằng học bổng |
| **Rò khuôn** | cụm câu, nhịp câu, hình ảnh nhận ra được là của Golden (`12-pattern-golden.md` mục 3) |
| **Mức trừu tượng thấp** | chép chi tiết bề mặt của Golden thay vì chức năng của chi tiết đó — lấy "cuốn sổ dưới chai tẩy" thay vì lấy "nghi thức có một chỗ cất bí mật" |

## 4. Mục lục

| File | Dùng khi |
|---|---|
| [1-nguyen-ly-cot-loi.md](references/1-nguyen-ly-cot-loi.md) | Luôn đọc đầu tiên. Bảy động cơ và vì sao. |
| [2-nhan-vat.md](references/2-nhan-vat.md) | Dựng nhân vật theo chức năng; chín trục đa dạng hoá. |
| [3-cau-truc.md](references/3-cau-truc.md) | Chín chặng, hình dạng tổng thể, sổ cài đặt. |
| [4-hook-va-cta.md](references/4-hook-va-cta.md) | Đọc title; mở màn (bảy chức năng); câu trớ trêu, lời rủ, câu đưa về đầu. |
| [5-vi-thanh.md](references/5-vi-thanh.md) | Chứng minh tại chỗ, bóp nghẹt, vết nứt, đấu trường, công bố, sụp đổ, vĩ thanh, khối đóng bài. |
| [6-van-phong.md](references/6-van-phong.md) | Nhịp câu, hình ảnh, cách viết một tài năng cho người ngoài nghề. |
| [7-quy-trinh-viet.md](references/7-quy-trinh-viet.md) | Quy trình tự động, bước 0 → 8. Mở ngay sau khi nhận title. |
| [8-vi-du-co-chu-thich.md](references/8-vi-du-co-chu-thich.md) | Kỹ thuật trong Golden, chỉ tới dòng cụ thể, kèm thứ không được mang đi. |
| [9-chu-de-nhay-cam.md](references/9-chu-de-nhay-cam.md) | Chủng tộc, giai cấp, bằng cấp — viết mà không kích động. |
| [10-checklist.md](references/10-checklist.md) | Phần H = Cổng 1. Phần A–G = Cổng 2. |
| [11-cau-treo.md](references/11-cau-treo.md) | Câu treo cuối chặng và câu đẩy cuối đoạn. |
| [12-pattern-golden.md](references/12-pattern-golden.md) | Golden đã làm gì; bảng tách nguyên lý / lựa chọn; danh sách chữ ký không được dùng lại. |
| [scripts/kiem-do-dai.py](scripts/kiem-do-dai.py) | **Chạy ở cả hai cổng.** Đếm từ mở màn, lời rủ, toàn bài; soát dòng trống và ký tự ngoài tiếng Anh. Không đếm bằng mắt. |

## 5. Golden Project

`GOLDEN-1.txt` là Golden Project duy nhất — **chỉ đọc, không bao giờ sửa**. Lao công dọn giảng đường bị trưởng khoa toán ấn phấn vào tay để mua vui, giải xong phương trình trong ba phút, rồi giải tiếp bài thứ hai do chính hắn ra. ~7.550 từ.

**Hai chỗ Golden KHÔNG phải chuẩn** — luật thắng Golden:
- Golden viết liền không dòng trống. Chuẩn: dòng trống giữa các đoạn.
- Golden có vài chỗ lệch thì (một câu hiện tại lọt giữa văn quá khứ). Chuẩn: thì quá khứ suốt bài, trừ hai khối nói thẳng với người xem.

- **Đọc L1–14 ngay trước khi viết mở màn**, và **đọc tới L116 một lần trước khi viết thân bài** — hết cảnh sỉ nhục và màn chứng minh tại chỗ. Nhịp câu và mật độ chi tiết của thể loại này không mô tả trọn được bằng luật — phải nghe.
- **Đọc để lấy nhịp, rồi đóng lại.** Không mở lại trong lúc viết, để khỏi chép.
- Golden minh hoạ **cách lấp các chức năng**, không phải kho cốt truyện, không phải kho câu.

## 6. Mười lỗi khi vận dụng skill

- **Chép câu chữ hoặc vỏ câu** của Golden hay của các ví dụ trong `references/`.
- **Cảnh sỉ nhục chỉ một nấc** — chửi một câu là hết. Người xem chưa kịp giận đủ thì màn chứng minh đã tới, và cả bài thiếu lực trả nợ (`3-cau-truc.md` chặng 2).
- **Chỉ chứng minh một lần.** Một lần thì còn cãi được là ăn may. Lần thứ hai, dưới điều kiện của chính hắn, mới đóng cửa lý lẽ đó lại.
- **Người kể tự khen tài năng** thay vì để một người trong nghề không thuộc phe nào xác nhận bằng thước đo.
- **Coi chín chặng là danh sách cảnh.** Chặng là chức năng; một chặng có thể là một cảnh hay nhiều cảnh, và hai chặng có thể nhập một.
- **Chọn biến số theo Golden thay vì theo title.**
- **Bài toán giả.** Bài toán được giải bằng một câu mơ hồ ("cô viết vài dòng và nó xong") hoặc bằng một cơ chế sai về chuyên môn. Người trong nghề xem kênh sẽ nghe ra ngay.
- **Vết nứt trong nền móng kẻ gác cổng rơi từ trên trời** — ai đó đưa cho cô, hoặc cô tình cờ thấy. Nó phải do **chính nghề của cô** tìm ra, và cô phải kiểm nó nhiều lần trước khi tin.
- **Để lộ khung** trong file bàn giao, hoặc **dựng không gian mơ hồ** — người nghe không biết ai đứng đâu (`6-van-phong.md` mục 5b).
- **Thuộc lòng luật thay vì hiểu lý do.** Mỗi luật trong `references/` kèm một câu vì sao. Gặp tình huống lạ, bám vào lý do mà suy ra.
