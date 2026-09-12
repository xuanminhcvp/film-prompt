---
name: skills-title
description: Sinh, soát và PHÂN DẠNG title tiếng Anh cho video kể chuyện. Ràng buộc cứng 90–100 ký tự, đúng một dấu `—`, hai mệnh đề. Mỗi title được gán dạng truyện theo tám dạng của kênh — phân biệt chủng tộc & cái kết (REVEAL) · tài năng (CHALLENGE / FIGHT) · giúp đỡ (KINDNESS) · đoàn tụ (REUNION) · chứng cứ (INVESTIGATION) · phép thử (TEST) · cảnh báo (WARNING) — kèm địa chỉ bàn giao sang skill viết kịch bản. Dùng skill này khi user nói "nghĩ title", "cho tôi 20 title", "title dạng giúp đỡ", "title này thuộc dạng nào", "title này ổn chưa", "sửa title cho dưới 100 ký tự", "phân loại list title này", hoặc dán một list title vào. KHÔNG dùng để viết kịch bản (skills-kich-ban / tai_nang_ngon_ngu / phan_biet_chung_toc_va_cai_ket) hay dựng board (skills-film / skills-hook).
---

# Viết title

> File này chỉ chứa **quy trình + bảng chủ quyền**. Mọi luật chi tiết nằm ở `references/`.
> Giữ dưới 3.000 token. Không tóm tắt luật của file khác vào đây.

## Việc của skill này

Sinh ra **title đứng một mình bán được** — người đọc thấy title là muốn bấm, chưa cần biết kịch bản.
Title ở đây là **một lời hứa hai vế**: vế trước là **tội**, vế sau là **giá phải trả**, ngăn nhau bằng đúng một dấu `—`.

Mỗi title mang **bốn mã**: `D#` dạng truyện (`4-dang-bai.md`) × `T#` kiểu vế trước × `V#` kiểu vế sau × `L#` trục lật (`1-cong-thuc.md`). Không ghi được đủ bốn mã nghĩa là title chưa rõ hình dạng.

Không viết hook, không viết kịch bản, không đụng `sf-board.json`.

## Ranh giới với ba skill kia

| Skill | Sở hữu việc gì |
|---|---|
| **skills-title** (file này) | Sinh title hàng loạt · soát title · phân loại list title user dán vào |
| `phan_biet_chung_toc_va_cai_ket` | Nhận một title `D1` REVEAL, trả về kịch bản văn xuôi |
| `tai_nang_ngon_ngu` (chỉ tài năng ngôn ngữ) | Nhận một title `D2` CHALLENGE hoặc `D4` FIGHT, trả về kịch bản văn xuôi |
| `skills-kich-ban` | Viết trọn kịch bản cho năm dạng còn lại. Bước 2 của nó cũng ra title — **nó dùng luật của nó**, đừng ép nó sang đây |
| `skills-film` / `skills-hook` | Dựng hình từ kịch bản đã có |

Bảng bàn giao đầy đủ ở [4-dang-bai](references/4-dang-bai.md) §3. **Skill này không tự gọi skill viết kịch bản** — ghi mã, báo user, dừng.

Khi user đang viết kịch bản mà cần title → chạy `skills-kich-ban`.
Khi user chỉ cần **title thôi** (list, brainstorm, soát, sửa độ dài) → chạy skill này.

## Quy trình

| Bước | Làm gì | Mở thêm file |
|---|---|---|
| **0a** Chốt dòng kho gốc | Mở kho title, chọn dòng làm gốc cho từng phương án. **Không có dòng gốc thì không được viết title.** Giữ lõi tình huống của dòng đó, đổi ít là đủ. Chức vụ + bối cảnh tra [TU-DIEN-KHO](kho/TU-DIEN-KHO.md). Vòng mẫu: [GOLDEN-1](golden_project/GOLDEN-1.md) | [3-quy-trinh](references/3-quy-trinh.md) §0 |
| **0b** Chốt dạng bài | User nói rõ dạng ("cho tôi title dạng giúp đỡ") → dùng dạng đó cho cả mẻ. Không nói → mẻ phải trải ít nhất bốn dạng | [4-dang-bai](references/4-dang-bai.md) |
| **1** Chốt hạt giống | Ghi ra ba thứ trước khi viết chữ nào: **KẺ RA ĐÒN** (nêu đích danh quyền lực) · **NGƯỜI CHỊU ĐÒN** (nêu đích danh địa vị thấp) · **THỨ HỌ GIẤU** (danh tính / năng lực / hậu thuẫn). Thiếu một trong ba thì title sẽ mờ, không cứu được ở khâu chữ nghĩa | [1-cong-thuc](references/1-cong-thuc.md) §1 |
| **2** Chọn cặp công thức | Chọn **kiểu vế trước** (T1–T9) × **kiểu vế sau** (V1–V6). Hai trục độc lập | [1-cong-thuc](references/1-cong-thuc.md) |
| **3** Dựng | User xin `n` title → dựng `n + 40%` phương án, **đổi kiểu vế trước chứ đừng đổi cách nói**. Năm phương án cùng T1 là một phương án viết năm lần | [1-cong-thuc](references/1-cong-thuc.md) §4 |
| **4** Đo | Chạy `scripts/kiem-title.py`. Mọi title lỗi phải sửa hoặc bỏ, **không giao kèm ghi chú "hơi dài"** | [2-do-luong](references/2-do-luong.md) |
| **5** Lọc | Bỏ phương án trùng dạng và trùng trục lật với phương án mạnh hơn trong cùng mẻ. Giao đúng `n` cái qua sạch checklist, mỗi cái kèm mã `D#` để user biết giao sang skill nào | [3-quy-trinh](references/3-quy-trinh.md) · [4-dang-bai](references/4-dang-bai.md) §3 |

**Cửa QC là cửa thật.** Title 101 ký tự không phải "gần đạt" — nền tảng cắt chữ, và phần bị cắt luôn là vế lật.

### Khi user dán một list title vào

Đó là yêu cầu **phân loại**, không phải yêu cầu viết mới. Gán mỗi title đủ bốn mã `D# · T# × V# × L#`, báo phân bố **theo dạng bài trước**, rồi mới tới hình dạng câu, và chỉ ra cái nào lệch chuẩn đo lường. Mẫu đã phân loại sẵn: [kho/PHAN-LOAI-131.md](kho/PHAN-LOAI-131.md).

## Bảng chủ quyền

| Khái niệm | File làm chủ |
|---|---|
| Chín kiểu vế trước · sáu kiểu vế sau · sáu trục lật · luật ghép hai vế | `references/1-cong-thuc.md` |
| **Tám dạng truyện · cách phân biệt dạng dễ nhầm · bàn giao sang skill nào · luật đa dạng dạng bài** | `references/4-dang-bai.md` |
| **Mọi con số**: trần ký tự, dấu gạch, mệnh đề, CAPS, chữ số, từ bắt buộc · mọi cấm kỵ | `references/2-do-luong.md` |
| Dựng bao nhiêu · lọc thế nào · cách cắt khi quá dài · checklist giao bài | `references/3-quy-trinh.md` |
| **Vòng làm title mẫu (Golden Project)** | `golden_project/GOLDEN-1.md` |
| **Hàng rào chức vụ · bối cảnh** | `kho/TU-DIEN-KHO.md` |
| **Kho ý tưởng — nguồn gốc bắt buộc của mọi title** (643 title) | `kho/KHO-BO-SUNG-2026-09-12.md` (437) · `../skills-kich-ban/kho-tham-chieu/TITLES.md` (206) · `kho/PHAN-LOAI-131.md` (131, đã gán mã) |

**Luật phân tầng:** đếm được → `2-do-luong.md`. Là hình dạng câu → `1-cong-thuc.md`. Là kiểu truyện → `4-dang-bai.md`. Là thao tác → `3-quy-trinh.md`.

**Tám dạng bài do `skills-kich-ban/dang/bai/` làm chủ.** File `4-dang-bai.md` chỉ trỏ sang, không định nghĩa lại — dạng bài đổi thì đổi ở đó, không đổi ở đây.

## Luật cứng

- **Ý tưởng title chỉ được lấy từ kho — cấm tự nghĩ lõi mới.** Mọi title giao ra phải bắt nguồn từ một dòng có thật trong kho, và phải ghi kèm dòng gốc đó. Luật đầy đủ ở [3-quy-trinh](references/3-quy-trinh.md) §0.
- **Chức vụ và bối cảnh cũng chỉ lấy từ kho.** Tra [kho/TU-DIEN-KHO.md](kho/TU-DIEN-KHO.md) — 98 chức vụ, 52 bối cảnh. Nghề lạ hay nơi lạ là lỗi, kể cả khi nghe hay hơn. Con số, mốc thời gian, tuổi và chữ nghĩa vế sau thì tự do.
- **Không mở `KICH-BAN.md` hay project cũ để lấy cảm hứng title.** Kho title là nguồn ý tưởng; kịch bản cũ thì không. Mở phim cũ là cách chắc chắn nhất để đẻ ra bản sao mờ của nó.
- **Không sửa `golden_project/`.** Đó là bản mẫu user đã duyệt; chỉ user được sửa thủ công.
- **Không tự sửa skill khi user chê output.** User bảo sửa thì mới sửa.
- **Chạy script, đừng đếm bằng mắt.** Đếm ký tự bằng mắt sai nhiều hơn bạn tưởng, nhất là với dấu `—` và dấu nháy cong.
- **Ngôn ngữ**: title viết **tiếng Anh**; mọi trao đổi với user viết **tiếng Việt**.
