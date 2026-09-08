# 1 — Chọn dạng bài (bộ định tuyến)

> **File này trả lời:** kịch bản này thuộc dạng bài nào, nạp file nào, và mở rộng skill thế nào.
> **Mở khi:** bước 1, ngay sau khi nhận yêu cầu. Mở lại mỗi khi user gửi một kịch bản mẫu mới.
> **Không chứa:** giá trị định mức (→ `../dang/MUSE.md` §1) · luật riêng của từng dạng bài (→ `../dang/muse/`) ·
>   nguyên lý kể chuyện (→ `0-nguyen-ly-ke-chuyen.md`)

## 1. Ba tầng luật — hiểu sai tầng là hỏng cả skill

| Tầng | Ở đâu | Chứa gì | Đổi dạng bài thì |
|---|---|---|---|
| **Lõi** | `references/` | Luật đúng với mọi kịch bản | **Không đổi** |
| **Khung chung** | `dang/MUSE.md` | 12 định mức · tám nhiệm vụ hook · bảy nhiệm vụ thân | **Không đổi** |
| **Dạng bài** | `dang/muse/<TÊN>.md` | *Cái gì khởi động* và *cú lật là gì* | Đổi 4 thứ |

Hiện có **một khung chung (`MUSE`) và tám dạng bài**. Mọi bài đều nạp: lõi + `MUSE.md` + **đúng một** dạng bài.

Ranh giới để biết một luật mới thuộc tầng nào:

> Đúng bất kể viết gì → **lõi**.
> Đúng với cả tám dạng bài, đổi thì tám cái cùng đổi → **khung chung**.
> Chỉ đúng với một kiểu chuyện → **dạng bài**.

Vì sao tách khung chung ra khỏi tám dạng bài: tám kiểu chuyện này dùng **chung** độ dài, nhịp câu, CTA và khung nhiệm vụ. Viết chúng thành tám file trọn vẹn sẽ đẻ ra tám bản trùng nhau 80%, và tám bản ấy sẽ trôi khỏi nhau ngay lần sửa đầu tiên.

## 2. Hợp đồng tham số

`MUSE.md` §1 điền đủ 12 ô dưới đây, **mỗi ô kèm nhãn** `[SẢN XUẤT]` / `[NHIỆM VỤ]` / `[QUAN SÁT]` theo `8-chong-rap-khuon.md` §1. Số đo từ một bộ mẫu hữu hạn mặc định là `[QUAN SÁT]`.

| Mã tham số | Nghĩa | Lõi khai báo ở |
|---|---|---|
| `TITLE.cong-thuc` | Công thức title | `2-title.md` §2 |
| `TITLE.tran` | Trần ký tự · số từ · số dấu gạch | `2-title.md` §3 |
| `HOOK.do-dai` | Số từ và số giây đọc | `3-hook.md` §2 |
| `HOOK.chuoi-nuoc-di` | Các nhiệm vụ hook | `3-hook.md` §3 |
| `HOOK.cta` | CTA giữa hook | `3-hook.md` §4 |
| `HOOK.cau-chot` | Câu đóng hook phải làm gì | `3-hook.md` §5 |
| `THAN.khung-muc` | Thân chia thế nào | `4-than-truyen.md` §2 |
| `THAN.do-dai` | Số từ toàn bài | `4-than-truyen.md` §2 |
| `THAN.cta-cuoi` | CTA cuối bài | `4-than-truyen.md` §6 |
| `VAN.ngoi-ke` | Ngôi kể · mức thoại | `6-giong-van.md` §2 |
| `VAN.nhip-cau` | Độ dài câu · tỉ lệ câu ngắn · trần câu · độ dài đoạn | `6-giong-van.md` §2 |
| `CHI-TIET.mat-do` | Mật độ dữ kiện cứng | `5-nhan-vat-va-chi-tiet.md` §3 |

Thêm tham số mới = sửa bảng này + sửa file lõi khai báo nó + điền vào `MUSE.md` + sửa `dang/_MAU-DANG.md`.

## 3. Quy trình bước 1

1. Đọc ý tưởng user gửi — nếu có.
2. Mở bảng tám dạng bài (`../dang/MUSE.md` §8):
   - **Có ý tưởng** → chọn dạng khớp theo cột **Khởi động** và **Cú lật**, không chọn theo chủ đề. Một ý tưởng về bệnh viện có thể là `REVEAL`, `CHALLENGE`, `WARNING` hay `INVESTIGATION` — chủ đề không quyết định dạng.
   - **Không có ý tưởng** → **bốc ngẫu nhiên thật**, loại hai dạng của hai bài gần nhất:
     ```bash
     grep -rh "^> \*\*DẠNG BÀI\*\*" *.project/KICH-BAN.md 2>/dev/null | tail -2
     ```
     Đừng mặc định `REVEAL` vì nó chiếm 35% kho. Tỉ trọng mô tả kho cũ, không phải chỉ tiêu cho bài mới.
3. Ghi ra ba dòng; chưa có thì chưa được sang bước 2:

```
DẠNG BÀI: <tên file trong dang/muse/, không đuôi>
SỰ THẬT LÕI: <một câu, ≤ 25 từ, thứ khán giả chưa biết mà kịch bản này dạy họ>
LỆCH CÓ CHỦ Ý: <một chỗ định làm khác kho tham chiếu, và vì sao>
```

Dòng thứ ba là bắt buộc. Bám sát mọi mẫu hình của kho là cách chắc chắn để ra một bài không có gì của riêng nó (`8-chong-rap-khuon.md` §3).

4. **Nạp: lõi + `dang/MUSE.md` + đúng một file trong `dang/muse/`.** Nạp hai dạng bài là cách chắc chắn nhất để lẫn cú lật.
5. Báo cho user biết đã chọn dạng nào và vì sao — **một câu** — rồi đi tiếp luôn, không đợi gật.
6. User có ý tưởng nhưng **không dạng nào khớp** → đây là một trong ba trường hợp được dừng hỏi (`../SKILL.md` §Khi nào mới được dừng). Không ép vào dạng gần nhất, không tự chế dạng mới từ suy đoán.

## 4. Mở rộng khi user gửi mẫu mới

Đọc mẫu và **đếm** trước đã: tổng số từ, số từ của hook, có CTA cuối không, nhịp câu. Rồi rẽ một trong hai nhánh:

**Nhánh A — định mức trùng khớp `MUSE.md`, chỉ khác khởi động và cú lật** → đây là **dạng bài mới**:
1. Chép `dang/muse/_MAU-DANG-BAI.md` thành `dang/muse/<TÊN>.md`. Tên viết HOA, không dấu.
2. Điền 5 mục; mỗi "cấm" kèm cột *hỏng gì nếu vi phạm*.
3. Thêm một dòng vào bảng ở `../dang/MUSE.md` §8.

**Nhánh B — định mức khác hẳn** (độ dài, nhịp câu, hoặc không có CTA cuối) → đây là **khung chung mới**:
1. Chép `dang/_MAU-DANG.md` thành `dang/<TÊN>.md`, điền đủ 12 ô kèm nhãn.
2. Nếu khung mới cũng có nhiều kiểu chuyện, tạo `dang/<tên>/` và làm như nhánh A.
3. Thêm một dòng vào §5 dưới đây.

Đừng dựng khung chung thứ hai gần trùng `MUSE` chỉ vì một bài mẫu hơi khác. Hỏi: *bỏ nó vào một dạng bài của MUSE thì hỏng chỗ nào?*

## 5. Sổ khung chung

| Khung | Dùng khi | Nguồn định mức |
|---|---|---|
| [`MUSE`](../dang/MUSE.md) | Người bị coi thường nắm một thứ người đối diện không biết. Tám dạng bài ở `dang/muse/` | **Đo thật** trên 242 title + 117 kịch bản của kho *MUSE Stories* |

## 6. Kiểm tra

- [ ] Đã ghi đủ ba dòng `DẠNG BÀI:`, `SỰ THẬT LÕI:`, `LỆCH CÓ CHỦ Ý:` trước khi sang bước 2.
- [ ] `SỰ THẬT LÕI` ≤ 25 từ, nói điều khán giả **chưa biết**, không phải tóm tắt cốt truyện.
- [ ] Dạng bài đã chọn có file trong `dang/muse/`.
- [ ] (Khi bốc ngẫu nhiên) Đã loại hai dạng của hai bài gần nhất, và không mặc định chọn dạng phổ biến nhất.
- [ ] Chỉ nạp **một** dạng bài, kèm `MUSE.md`.
- [ ] Mọi ô trong khung chung đều có nhãn, và không ô [QUAN SÁT] nào bị viết như mệnh lệnh.
- [ ] (Khi vừa mở rộng) Đã rẽ đúng nhánh A hay B ở §4, và đã thêm dòng vào bảng tương ứng.
