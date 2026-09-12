# GOLDEN-1 — một vòng làm title đúng chuẩn

> **Golden Project của `skills-title`.** Đây là bản mẫu user đã duyệt ngày 2026-09-12.
> Mở file này khi cần nhớ **cách làm một title**, không phải khi cần ý tưởng — ý tưởng lấy ở kho
> (`../references/3-quy-trinh.md` §0).
>
> ⛔ **Không sửa file này.** Chỉ user được sửa thủ công.

---

## Bước 1 — Lấy dòng gốc từ kho

Mở `../../skills-kich-ban/kho-tham-chieu/TITLES.md`, chọn một dòng có thật:

> **TITLES #52** — `Airport Clerk Laughed at Black Woman's English — Went Pale Learning She Controls $950M Travel Group`
> *(99 ký tự · [OK])*

---

## Bước 2 — Đọc dòng gốc ra lõi tình huống

Đây là phần **bắt buộc giữ**. Viết ra bảng này trước khi viết chữ nào:

| Thành phần | Dòng gốc #52 |
|---|---|
| **Kẻ ra đòn** | Nhân viên gác cổng của một dịch vụ (`Airport Clerk`) |
| **Đòn** | Cười cách người kia **nói** — chê tiếng / chê giọng |
| **Người chịu đòn** | Phụ nữ da đen, bị coi là khách hạng thấp |
| **Trục lật** | Cô **sở hữu / kiểm soát chính cái tập đoàn** hắn đang đứng làm việc cho |
| **Mã** | `T1` Đòn × `V5` Phản ứng cơ thể × `L1` Danh tính quyền lực |

---

## Bước 3 — Title giao ra

> **`Hotel Clerk Mocked a Black Maid's Accent — Went Pale Learning She Owns the $680M Chain He Works For`**
>
> 99 ký tự · `T1 × V5 × L1` · dạng `D1` REVEAL → giao cho `phan_biet_chung_toc_va_cai_ket`
> **(gốc: TITLES #52)**

---

## Bước 4 — Đổi đúng những gì

Lõi giữ nguyên. Năm chỗ đổi, đều là **chi tiết**, không phải lõi:

| | Gốc #52 | Title mới | Vì sao đổi |
|---|---|---|---|
| Bối cảnh | sân bay | khách sạn | đủ để không phải bản sao chữ |
| Đòn | `Laughed at … English` | `Mocked … Accent` | cùng loại đòn, khác chữ |
| Người chịu đòn | `Black Woman` (trống) | `Black Maid's` | **có nghề** → hai đầu thang xã hội sắc hơn gốc (`1-cong-thuc.md` §1) |
| Quy mô | `$950M Travel Group` | `$680M Chain` | con số mới, vẫn giữ sức nặng |
| Vế sau | `She Controls` | `She Owns … He Works For` | buộc cú lật đập thẳng vào chính kẻ ra đòn |

**Đây là đúng mức phải đổi.** Không viết mới hoàn toàn, cũng không bê nguyên văn.

---

## Bước 5 — Đo bằng script, không đếm mắt

```bash
echo "Hotel Clerk Mocked a Black Maid's Accent — Went Pale Learning She Owns the \$680M Chain He Works For" \
  | python3 .claude/skills/skills-title/scripts/kiem-title.py -
```

→ `[OK]  99`

---

## Ba thứ file này làm mẫu

1. **Luôn có dòng gốc, và ghi kèm nó.** Không ghi được `(gốc: TITLES #N)` nghĩa là title đó tự nghĩ — bỏ.
2. **Giữ lõi, đổi chi tiết.** Bốn ô đầu bảng ở Bước 2 là lõi; bối cảnh / chữ nghĩa / con số là chi tiết.
3. **Được phép làm dòng gốc tốt lên.** Ở đây `Black Woman` → `Black Maid's` là title mới **sắc hơn** gốc. Kho là điểm xuất phát, không phải trần.

## Cạm bẫy khi làm cả mẻ

`L1` chiếm 45% kho — làm mười cái theo đúng vòng này thì cả mẻ sẽ dồn về `L1`.
Luật `../references/3-quy-trinh.md` §3 chặn: không quá hai title cùng `L#` trong một mẻ.
Nên khi làm mẻ lớn, **rút dòng gốc từ các vùng `L2` / `L6` thưa hơn**, đừng rút mười dòng cùng một góc.
