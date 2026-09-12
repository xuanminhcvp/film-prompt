---
name: kiem-chu-quyen
description: Rà toàn bộ MỘT skill để tìm chỗ phá vỡ nguyên tắc một-nguồn-sự-thật — luật bị chép ở hai nơi, hai con số đá nhau, dòng trỏ tới file đã xoá, file trong references/ không ai trỏ tới, khái niệm không file nào làm chủ hoặc hai file cùng nhận — rồi lập hoặc sửa bảng chủ quyền cho skill đó. Dùng khi user nói "rà lại skill", "skill này loạn rồi", "kiểm chủ quyền", "có luật nào trùng không", "dọn skill", "skill phình quá", hoặc sau một đợt sửa nhiều luật. KHÔNG dùng để vá một lỗi output cụ thể — đó là rule-surgeon. KHÔNG dùng để đồng bộ skill này sang skill kia — đó là align-hook-to-film. KHÔNG chứa chuẩn kỹ thuật viết skill (cấu trúc thư mục, frontmatter, ngân sách token) — hiện không skill nào trên máy làm chủ phần đó.
argument-hint: [đường dẫn thư mục skill cần rà]
---

# Kiểm chủ quyền

## Phạm vi

**Làm chủ:** sức khoẻ kiến trúc của **một** skill — khái niệm nào thuộc file nào, và mọi dấu hiệu cho thấy sự thật đã bị nhân bản ra nhiều chỗ.

**Không chứa** (chỉ trỏ, không chép):

| Cần gì | Đọc ở đâu |
|---|---|
| Ba dạng **không phải bản chép** ở file không làm chủ (dòng trỏ · ngoại lệ có phạm vi riêng · ngưỡng nằm trong checker) | `rule-surgeon`, mục *Nguyên tắc bất biến* |
| Bê luật từ skill này sang skill khác | `align-hook-to-film` |

⚠️ **Chuẩn kỹ thuật viết skill** — cấu trúc thư mục, frontmatter, cách viết `description`, ngân sách token — hiện **không skill nào trên máy làm chủ**. Đợt rà không tự lấp chỗ đó. Gặp câu hỏi thuộc loại này thì nêu ra ở phần bàn giao, đừng tự phán.

Skill này chạy được cho **bất kỳ** skill nào, kể cả skill **chưa có** bảng chủ quyền — đó là ca `rule-surgeon` phải dừng lại, và là lý do skill này tồn tại.

## Nguyên tắc bất biến

- **Mỗi khái niệm đúng một file làm chủ.** Bảng chủ quyền là bản đồ của quyền đó. Bảng nói sai thì mọi lần sửa sau đều sửa nhầm chỗ — cho nên bảng là thứ phải đúng trước tiên, trước cả luật.
- **Rà toàn bộ, sửa từng chỗ một.** Đợt rà quét cả skill, nhưng mỗi vi phạm là một quyết định riêng của user, không gộp thành một cú "dọn dẹp".
- **Vi phạm ≠ lỗi.** Một luật nằm ở chỗ trông lạ có thể là ngoại lệ có chủ ý. Hỏi *"gỡ cái này đi thì hành vi nào mất?"* trước khi đề xuất gỡ; không trả lời được thì phân loại là **chưa rõ**, không phải **thừa**.
- **Đợt rà không được đẻ ra luật mới.** Đây là việc dọn nhà, không phải việc viết luật. Phát hiện chỗ thiếu luật thì ghi vào phần bàn giao để user mở một đợt khác.

## Sáu loại vi phạm

| # | Loại | Dấu hiệu | Can thiệp mặc định |
|---|---|---|---|
| 1 | **Không ai làm chủ** | Luật đang sống trong `references/` nhưng không hàng nào của bảng chủ quyền nhận nó | Thêm hàng vào bảng, trỏ về file đang thật sự chứa luật. Không di chuyển luật. |
| 2 | **Hai file cùng nhận** | Cùng một khái niệm xuất hiện ở hai hàng, hoặc hai file cùng viết luật cho nó | Ranh giới sai. Trình user hai cách cắt ranh giới, chờ chọn — **đừng** tự nhét cả hai vào một file |
| 3 | **Bản chép thật** | Luật viết lại (nguyên văn hoặc diễn đạt khác) ở file không làm chủ | Thay đoạn chép bằng **một dòng trỏ** tên file + tên mục. Bản ở file chủ giữ nguyên |
| 4 | **Số đá nhau** | Cùng một ngưỡng, hai con số khác nhau ở hai chỗ | File chủ quyết. Chỗ còn lại đổi theo, hoặc rút xuống thành dòng trỏ |
| 5 | **Dòng trỏ chết** | Trỏ tới file hoặc tên mục không còn tồn tại | Theo `rule-surgeon`, *Nguyên tắc bất biến* — dạng thứ nhất, đủ ba nhánh giữ / đổi đích / xoá |
| 6 | **File mồ côi** | File trong `references/` mà `SKILL.md` không trỏ tới | Dựng lại dòng trỏ, ghi rõ **file đó chứa gì · khi nào mở** — thiếu hai vế ấy thì file vẫn coi như không tồn tại. File thật sự chết thì trình user, đừng tự xoá |

Loại 3 và 4 là thứ giết skill: hai bản cùng đúng ở ngày hôm nay, rồi một bản được sửa, bản kia im lặng ở lại và bắt đầu cãi nhau. Loại 1 và 2 là thứ khiến **lần sửa sau** vá nhầm file.

## Quy trình

### 1. Chốt phạm vi rà

Một skill mỗi đợt. Đọc trọn `SKILL.md`, rồi liệt kê mọi file trong `references/` và các thư mục con khác (`dang/`, `scripts/`…). Chưa có bảng chủ quyền thì đợt này chính là đợt **lập** bảng — nói rõ điều đó với user ngay từ đầu, vì việc và cách bàn giao khác hẳn.

### 2. Chạy các phép rà đếm được

Chạy từ thư mục skill. Đây là phần máy làm chắc hơn mắt — làm trước để không mất công đọc thủ công.

```bash
grep -roE '(references|dang|scripts)/[A-Za-z0-9._/-]+\.(md|py|sh)' . | sort -u -t: -k2 | while IFS=: read -r src p; do [ -e "$p" ] || echo "TRỎ CHẾT  $src → $p"; done
```

```bash
for f in references/*.md dang/*.md; do [ -e "$f" ] || continue; grep -q "$(basename "$f")" SKILL.md || echo "MỒ CÔI  $f"; done
```

```bash
grep -rnE '(trần|tối đa|không quá|dưới|ít nhất|≤|≥)[^.]{0,40}[0-9]' references/ SKILL.md | sort -t: -k3
```

Lệnh cuối chỉ **gom** mọi ngưỡng về một chỗ để mắt so; nó không tự biết hai con số nào đang nói về cùng một thứ.

### 3. Đọc chéo tìm loại 1–4

Phần đếm được đã xong; phần còn lại là phán đoán, không có lệnh nào thay được.

Tách mỗi file thành **rule nguyên tử** (định nghĩa ở `align-hook-to-film`, mục *Project bindings*), rồi với mỗi rule hỏi đúng hai câu:

1. *Khái niệm nào sở hữu nó, và bảng chủ quyền có nói vậy không?*
2. *Điều này còn được nói ở file nào khác không, kể cả bằng chữ khác?*

Câu 2 phải tìm theo **ý**, không theo chuỗi ký tự: hai bản chép nhau thường đã bị viết lại nên `grep` không bắt được. Đọc cả các file nghe như không liên quan — bản chép hay trốn ở đó nhất.

Không sửa gì ở bước này.

### 4. Trình danh sách, chờ duyệt, rồi mới sửa

Mỗi mục trình đủ: **vi phạm loại mấy · nằm ở file/dòng nào · file nào đang làm chủ · sửa gì · gỡ đi thì mất hành vi nào**.

Xếp theo mức chắc chắn giảm dần: trỏ chết và mồ côi (đếm được, chắc) → số đá nhau → bản chép → ranh giới chủ quyền (cần user quyết nhất).

Chờ user chọn từng mục. Duyệt xong mới sửa, và chỉ sửa đúng những mục đã duyệt.

## Cổng chặn

- ⛔ **Không sửa trước khi user duyệt danh sách.** Đợt rà là ca duy nhất được đụng nhiều file trong một lượt, vì vi phạm chủ quyền vốn nằm rải ở nhiều chỗ. Cái giá của quyền đó là cổng duyệt này. Sửa trước rồi báo sau thì đây chỉ là viết lại file.
- ⛔ **Không tự xoá luật vì "không thấy ai dùng".** Im lặng không phải bằng chứng chết — có thể nó đang lặng lẽ làm đúng, và chính vì đúng nên không sinh ra lỗi nào để lại dấu vết. Liệt kê cho user quyết.
- ⛔ **Không nhân tiện sửa nội dung luật.** Đợt này chỉ đổi **chỗ ở** của luật và **cách trỏ** tới nó. Luật sai nội dung là việc của `rule-surgeon`.
- ⛔ **Ba thứ cấm động trong đợt rà**, vì hậu quả của chúng nằm ngoài phạm vi rà: đổi **tên thư mục skill** (tên thư mục chính là lệnh `/`) · rút gọn **`description`** (skill còn trên đĩa nhưng không bao giờ tự nạp nữa) · xoá **dòng trỏ** tới `references/` (đó là cách đẻ ra vi phạm loại 6).

## Bàn giao

1. **Đã rà:** những file đã đọc, phép rà nào đã chạy, kết quả thật.
2. **Bảng chủ quyền sau đợt:** hàng thêm, hàng sửa đích, hàng gỡ — kèm lý do từng hàng.
3. **Đã sửa:** từng vi phạm đã duyệt và bản vá tương ứng.
4. **Chưa xử lý:** mục user chưa duyệt, hoặc cần quyết định ranh giới.
5. **Chỗ thiếu luật phát hiện được:** ghi ra để mở đợt khác, không tự viết trong đợt này.

Chỉ tuyên bố *"đã rà xong skill X"*. Không tuyên bố skill đã sạch — bản chép viết khéo vẫn có thể lọt.
