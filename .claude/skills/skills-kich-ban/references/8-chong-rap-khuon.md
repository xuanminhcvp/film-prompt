# 8 — Chống rập khuôn

> **File này trả lời:** làm sao dùng được số đo từ kho tham chiếu mà không biến kịch bản mới thành bản sao của kho cũ.
> **Mở khi:** trước khi viết (bước 3, bước 4) và ở bước 5, ngay trước khi giao bài.
> **Không chứa:** bản thân các định mức (→ `../dang/`) · nguyên lý kể chuyện (→ `0-nguyen-ly-ke-chuyen.md`)
>
> **File này có quyền phủ quyết.** Khi một luật ở file khác đẩy bài viết về phía rập khuôn, luật ở đây thắng.

## 1. Ba loại ràng buộc — đọc mọi luật của skill này qua lăng kính đó

Mọi con số và mọi khuôn trong `dang/` thuộc đúng một trong ba loại. Nhầm loại là nguồn gốc của cả sáu lỗi ở §2.

| Loại | Tư cách | Vi phạm thì sao | Nhận ra bằng |
|---|---|---|---|
| **Ràng buộc sản xuất** | Yêu cầu có thật của kênh/khách. Cứng. | Bài không dùng được | Nhãn **[SẢN XUẤT]** |
| **Nhiệm vụ chức năng** | Việc đoạn văn phải làm được. Bắt buộc đạt, **tự do về cách** | Truyện hỏng ở tầng kể chuyện | Nhãn **[NHIỆM VỤ]** |
| **Mẫu hình quan sát** | Cách kho tham chiếu hay làm. **Không phải luật.** | Không sao cả | Nhãn **[QUAN SÁT]** |

**Luật vàng:** *[NHIỆM VỤ] nói cái gì phải xảy ra. [QUAN SÁT] chỉ kể cách người khác từng làm cho nó xảy ra.* Khi hai thứ mâu thuẫn, giữ nhiệm vụ, bỏ mẫu hình.

Một mẫu hình quan sát chỉ được nâng lên thành nhiệm vụ khi trả lời được: *bỏ nó đi thì truyện hỏng ở chỗ nào?* Không trả lời được → nó vẫn chỉ là mẫu hình.

## 2. Sáu lỗi

### 2.1 Prompt overfitting — khớp quá sát bộ mẫu
Số đo từ một kho hữu hạn bị dùng như quy luật của thể loại. Kho có 117 bài quanh 7.500 từ không có nghĩa 7.000 từ là sai — chỉ có nghĩa kho ấy làm thế.
**Chữa:** hỏi *"con số này đến từ đâu?"* Từ nhu cầu sản xuất → giữ. Từ việc đếm mẫu → đó là [QUAN SÁT], được phép lệch khi truyện đòi.

### 2.2 Over-specific template — khuôn quá chi li
Khuôn đánh số tới từng câu, từng phần trăm, khiến mọi bài ra cùng một hình. Người viết bận điền ô thay vì kể chuyện.
**Chữa:** khuôn mô tả **việc cần làm xong**, không mô tả **thứ tự câu**. Trình tự là mặc định để bắt đầu, không phải đường ray.

### 2.3 Over-constraining — trói tay
Quá nhiều "cấm" khiến chỉ còn đúng một cách viết. Ràng buộc chồng nhau đến mức mọi lựa chọn thú vị đều phạm luật.
**Chữa:** mỗi cấm phải kèm **lý do hỏng gì**. Không nêu được thì đó là sở thích, không phải luật — bỏ. Cấm bảo vệ *ý nghĩa*, không bảo vệ *hình thức*.

### 2.4 Trope lock-in — khoá vào mô-típ
Motif của kho tham chiếu (nghề nghiệp, sắc tộc, kiểu sỉ nhục, kiểu phần thưởng) bị coi là điều kiện của thể loại.
**Chữa:** motif đến từ **yêu cầu của user và logic câu chuyện**, không đến từ kho. Kho cho biết *cấu trúc cảm xúc nào hiệu quả*, không quy định *ai đóng vai gì*. Không lặp lại một motif chỉ vì nó phổ biến trong kho.

### 2.5 Template leakage — rò rỉ khuôn mẫu
Chữ của hướng dẫn lọt vào bài giao: tên khối, tên nước đi, nhãn dạng bài, hoặc **câu ví dụ chép nguyên văn**.
**Chữa:** mọi ví dụ trong `dang/` là **mẫu vật để nhận dạng, không phải chất liệu để dùng lại**. Cấm chép lại câu, cụm từ đặc trưng, tên nhân vật, tên tổ chức từ ví dụ. Bài giao không được chứa một chữ nào của bộ luật.

### 2.6 Low abstraction — dạy bề mặt
Luật mô tả *bài mẫu trông ra sao* thay vì *vì sao nó hiệu quả*. Người viết sao chép hình dạng mà không hiểu cơ chế, nên chệch một chút là hỏng.
**Chữa:** mỗi luật hình dạng phải truy được về một nguyên lý ở `0-nguyen-ly-ke-chuyen.md`. Không truy được thì nó là thói quen của kho, hạ xuống [QUAN SÁT].

## 3. Ba câu hỏi trước khi giao bài

1. *Nếu đặt bài này cạnh năm bài trong kho tham chiếu, có ai phân biệt được không — hay chúng chỉ khác tên riêng?*
2. *Có chi tiết nào ở đây vì câu chuyện cần, hay tất cả đều vì bộ luật bảo thế?*
3. *Chỗ nào tôi đã lệch khỏi mẫu hình quan sát — và lệch vì lý do gì?* Không lệch chỗ nào là dấu hiệu xấu, không phải dấu hiệu tốt.

## 4. Kiểm tra

- [ ] Mọi con số đã dùng đều xác định được thuộc loại nào trong §1.
- [ ] Không con số [QUAN SÁT] nào bị đối xử như [SẢN XUẤT].
- [ ] Mỗi cấm đã áp dụng đều nêu được **hỏng gì nếu vi phạm**.
- [ ] Bài giao không chứa tên khối, tên nước đi, tên dạng bài, hay bất kỳ chữ nào của bộ luật.
- [ ] Không câu nào, cụm từ đặc trưng nào, tên riêng nào bị chép lại từ ví dụ trong `dang/`.
- [ ] Motif (nghề, sắc tộc, bối cảnh, kiểu xung đột) đến từ yêu cầu user và logic truyện, không từ thói quen của kho.
- [ ] (Toàn bài) Trả lời được cả ba câu hỏi ở §3, gồm cả câu thứ ba — nêu được ít nhất một chỗ đã lệch khỏi mẫu hình và lý do.
