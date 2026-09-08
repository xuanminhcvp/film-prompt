# MẪU HỒ SƠ DẠNG — chép file này, đừng sửa file này

> **Cách dùng:** `cp _MAU-DANG.md <TÊN-DẠNG>.md` rồi điền. Quy trình đầy đủ ở
> `../references/1-chon-dang.md` §4.
>
> **Ba luật khi điền:**
> 1. **Chỉ điền giá trị.** Không chép lại nguyên lý của lõi. Một câu chép là một bản sao đang chờ trôi khỏi bản gốc.
> 2. **Đủ 12 ô.** Ô nào mẫu kịch bản không nói rõ thì hỏi user — không bịa, không để trống, không ghi "tuỳ".
> 3. **Số phải là số.** "Hook ngắn thôi" không phải giá trị. "280–400 từ" mới là giá trị.
> 4. **Mỗi ô phải mang một nhãn** — `[SẢN XUẤT]` (yêu cầu có thật của kênh, cứng) · `[NHIỆM VỤ]` (việc phải làm được, tự do về cách) · `[QUAN SÁT]` (kho hay làm thế, không phải luật). Đọc `../references/8-chong-rap-khuon.md` §1 trước khi gắn. Số đo được từ một bộ mẫu hữu hạn mặc định là `[QUAN SÁT]`; muốn nâng lên `[NHIỆM VỤ]` thì phải trả lời được *bỏ nó đi thì truyện hỏng ở chỗ nào*.
> 5. **Mỗi "cấm" kèm lý do hỏng gì.** Không nêu được thì đừng viết.

---

# Dạng `<TÊN-DẠNG>`

**DÙNG KHI:** <một câu, mô tả loại chuyện nào rơi vào dạng này — đây là dòng bộ định tuyến đọc để chọn dạng>

**NGUỒN:** <rút từ mẫu nào, ngày nào. Nếu định mức còn là ước lượng thì ghi rõ "tạm, chờ mẫu">

## 1. Định mức (12 ô tham số)

| Mã | Nhãn | Giá trị |
|---|---|---|
| `TITLE.cong-thuc` | | |
| `TITLE.tran` | | |
| `HOOK.do-dai` | | |
| `HOOK.chuoi-nuoc-di` | | |
| `HOOK.cta` | | |
| `HOOK.cau-chot` | | |
| `THAN.khung-muc` | | |
| `THAN.do-dai` | | |
| `THAN.cta-cuoi` | | |
| `VAN.ngoi-ke` | | |
| `VAN.nhip-cau` | | |
| `CHI-TIET.mat-do` | | |

## 2. Khuôn hook — chuỗi nước đi

Liệt kê từng nước đi theo thứ tự, mỗi nước một dòng: *tên nước đi · nó làm gì · dài bao nhiêu*.
Đây là chỗ triển khai giá trị của `HOOK.chuoi-nuoc-di` ở §1.

## 3. Khuôn thân truyện

Liệt kê các khối theo thứ tự, mỗi khối: *tên khối · nhiệm vụ · dài bao nhiêu*.
Đây là chỗ triển khai giá trị của `THAN.khung-muc` ở §1.

## 4. Dấu nhận dạng của dạng này · [QUAN SÁT]

3–6 gạch đầu dòng: đọc lên là biết ngay đang ở dạng này chứ không phải dạng khác.
Viết bằng thứ **quan sát được**, không bằng tính từ. Đây là mô tả để nhận ra dạng, **không phải danh sách phải làm đủ**.

## 5. Cấm riêng của dạng này — kèm lý do

| Cấm | Hỏng gì nếu vi phạm |
|---|---|
| <việc dạng khác làm được mà dạng này không> | <không điền được thì bỏ dòng này> |

## 6. Kiểm tra riêng của dạng

- [ ] <mỗi định mức đếm được ở §1 phải có một dòng kiểm ở đây — ngưỡng không nằm trong checklist thì không ai kiểm>
