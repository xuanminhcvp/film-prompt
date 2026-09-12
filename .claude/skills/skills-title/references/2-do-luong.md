# 2 — Đo lường: mọi con số và mọi cấm kỵ

**NGUỒN:** đo trên 131 title mẫu (2026-09-09): dài **69–100** ký tự, **trung vị 97**, trung bình 95,5. 91% nằm trong dải 90–100.

## 1. Bảng định mức

| Mã | Nhãn | Giá trị |
|---|---|---|
| `TITLE.tran-tren` | **[BẮT BUỘC]** | **≤ 100 ký tự.** Chỗ nền tảng cắt chữ. Vượt một ký tự cũng là hỏng — phần bị cắt luôn là vế lật |
| `TITLE.san-duoi` | **[BẮT BUỘC]** | **≥ 90 ký tự.** Dưới 90 thì không đủ chỗ cho cả hai đầu sắc lẫn vế sau có quy mô. 12/131 mẫu dưới sàn — chúng đều mờ một đầu |
| `TITLE.dai-toi-uu` | [THAM KHẢO] | **95–99 ký tự.** Trung vị kho là 97. Viết sát 100 rủi ro, viết 91 là bỏ phí chỗ |
| `TITLE.dau-gach` | **[BẮT BUỘC]** | **Đúng một dấu `—`** (em dash U+2014), có khoảng trắng hai bên. Không dùng `-`, `–`, `:` thay nó. Hai dấu `—` = ba mệnh đề = hỏng |
| `TITLE.menh-de` | **[BẮT BUỘC]** | **Đúng hai mệnh đề**: tội `—` giá. Ba mệnh đề trở lên thì không mệnh đề nào kịp đứng |
| `TITLE.tu-bat-buoc` | **[BẮT BUỘC]** | **`Black` phải có mặt ở vế trước** — mặc định sản xuất của kênh: nhân vật chính luôn là người da đen. 83% kho có. Ngoại lệ duy nhất: user nói rõ phim này không phải dòng đó |
| `TITLE.chu-so` | [THAM KHẢO] | Viết bằng **chữ số**, không bằng chữ: `$2M`, `4-Star`, `300`, `9 Moves`. Ngược hẳn luật của kịch bản — title là chỗ chữ số được phép kêu. 39% kho có ít nhất một |
| `TITLE.caps` | [THAM KHẢO] | **Tối đa một từ VIẾT HOA TOÀN BỘ**, đặt ở chỗ muốn người đọc dừng mắt: `HER Job`, `FBI DIRECTOR`, `EVERYTHING`. 45% kho có. Hai từ CAPS trở lên là hét, người đọc lướt qua |
| `TITLE.ngoac-kep` | [THAM KHẢO] | Thoại trong ngoặc kép ở một trong hai vế: 26% kho. Mở đầu bằng thoại (`T4`): 7% |
| `TITLE.title-case` | **[BẮT BUỘC]** | Viết hoa đầu mỗi từ chính (Title Case). Giới từ ngắn, mạo từ, liên từ giữ chữ thường |
| `TITLE.dau-cau-cuoi` | **[BẮT BUỘC]** | Không có dấu chấm cuối. Không dấu chấm than trần trụi cuối câu |

## 2. Cấm kỵ — mỗi cấm kèm hậu quả

| Cấm | Vì sao |
|---|---|
| **Tính từ đánh giá**: *incredible · shocking · unbelievable · amazing · heartbreaking* | Nói hộ người đọc cảm xúc họ chưa có. Chi tiết tự gây được cảm xúc thì không cần dán nhãn |
| **Nêu thẳng cú lật cuối cùng** | Hết lý do bấm. Title được phép cho biết cú lật **to cỡ nào** và **chạm vào cái gì**, nhưng không nói **nó là gì** |
| **Hứa thứ nội dung không có** | Người xem thoát ở giây thứ ba mươi, và kênh trả giá bằng lượt đề xuất |
| **Vế sau chỉ nói cảm xúc**: *…And Everyone Cried* | Không có quy mô, không có chỗ đau. Cảm xúc là kết quả, không phải lời hứa |
| **`What Happened Next` đứng trơ một mình** | Hứa suông. Phải kèm danh từ có sức nặng (`1-cong-thuc.md` §3) |
| **Hai từ CAPS trở lên · dấu chấm than kép** | Hét. Người đọc trượt mắt qua thay vì dừng lại |
| **Tên riêng của nhân vật ở vế trước** | Tên riêng không nói địa vị. `Willa` không cho biết gì; `the Black Janitor` cho biết tất cả. Danh xưng nghề nghiệp luôn thắng tên riêng trong title |
| **Rút gọn tới mức mất một đầu** để lọt trần ký tự | Thà đổi hẳn góc vào còn hơn giao một title 98 ký tự có vế trước mờ. Cách cắt đúng ở `3-quy-trinh.md` §4 |

## 3. Chạy script — bắt buộc trước khi giao

```bash
python3 .claude/skills/skills-title/scripts/kiem-title.py <file.txt>
```

Hoặc dán thẳng qua stdin:

```bash
python3 .claude/skills/skills-title/scripts/kiem-title.py -
```

Script đếm ký tự thật, đếm dấu `—`, đếm từ CAPS, soát `Black`, soát dấu gạch sai loại, và cảnh báo mẫu mòn. **Không đếm ký tự bằng mắt** — dấu `—`, dấu nháy cong `'` và `…` là ba chỗ đếm nhẩm hay sai nhất.

Script in `OK` / `CẢNH BÁO` / `LỖI`. **LỖI thì không được giao**, kể cả kèm ghi chú.

## 4. Checklist đo lường

- [ ] Chạy `kiem-title.py`, không title nào còn dòng `LỖI`.
- [ ] Mọi title trong dải **90–100** ký tự, phần lớn rơi vào 95–99.
- [ ] Mỗi title có **đúng một** dấu `—` đúng loại em dash.
- [ ] Đúng hai mệnh đề.
- [ ] `Black` có mặt ở vế trước (trừ khi user miễn).
- [ ] Tối đa một từ CAPS mỗi title.
- [ ] Số viết bằng chữ số.
- [ ] Không tính từ đánh giá, không lộ cú lật, không hứa suông.
