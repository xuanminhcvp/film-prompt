---
name: skills-kich-ban
description: Viết trọn một kịch bản kể chuyện (story) từ ý tưởng đến file — chọn dạng bài (random nếu user không chỉ định), title, hook, rồi toàn bộ phần sau hook, tự kiểm chất lượng ở mỗi bước và chạy thẳng không hỏi lại — xuất ra `KICH-BAN.md` và `MO-TA-YOUTUBE.md` trong `<TEN-DU-AN>.project/`. Hỗ trợ tám dạng bài (REVEAL · CHALLENGE · KINDNESS · FIGHT · WARNING · TEST · REUNION · INVESTIGATION) dùng chung khung chung trong `dang/`. Dùng skill này mỗi khi user nói "viết kịch bản mới", "nghĩ title", "viết hook cho phim này", "viết tiếp phần sau hook", "làm story về ...", kể cả khi user chỉ ném một ý tưởng một dòng. Cũng dùng khi user nói "viết mô tả YouTube", "viết description cho phim này". KHÔNG dùng cho khâu dựng hình (SF, prompt video, nhạc) — đó là skills-film / skills-hook.
---

# Viết kịch bản kể chuyện

> **Luật tuyệt đối: File này chỉ chứa quy trình + bảng chủ quyền**. Mọi luật chi tiết nằm ở `references/` và `dang/`.
> Giữ file dưới 5.000 token. Không tóm tắt luật của file khác vào đây — bản tóm tắt luôn là bản thứ hai đang chờ trôi khỏi bản gốc.

## Ba tầng luật — đọc trước khi làm bất cứ việc gì

| Tầng | Ở đâu | Chứa gì | Đổi dạng bài thì |
|---|---|---|---|
| **Lõi** | `references/` | Luật đúng với mọi kịch bản: nguyên lý, form, cấm kỵ | **Không đổi** |
| **Khung chung** | `dang/KHUNG-CHUNG.md` | 12 định mức · tám nhiệm vụ hook · bảy nhiệm vụ thân | **Không đổi** |
| **Dạng bài** | `dang/bai/<TÊN>.md` | *Cái gì khởi động* · *cú lật là gì* · trục biến thiên | Đổi 6 thứ |

**Hiện có tám dạng bài**, tất cả dùng chung khung `KHUNG-CHUNG`: `REVEAL` · `CHALLENGE` · `KINDNESS` · `FIGHT` · `WARNING` · `TEST` · `REUNION` · `INVESTIGATION`. Bảng đầy đủ ở [dang/KHUNG-CHUNG.md](dang/KHUNG-CHUNG.md) §8.

Lõi **khai báo tên tham số** (`HOOK.do-dai`, `THAN.khung-muc`, …) và nói "tra ở khung chung".
Khung chung **điền giá trị** cho đúng những tham số ấy. Dạng bài **chỉ ghi đè những gì `KHUNG-CHUNG.md` §8 liệt kê** và cấm chép lại phần còn lại.

Mỗi lượt làm việc chỉ nạp: **lõi cần cho bước đang làm + `dang/KHUNG-CHUNG.md` + đúng MỘT dạng bài.**
Hợp đồng 12 tham số và cách mở rộng: [1-chon-dang.md](references/1-chon-dang.md).

## Ba loại ràng buộc — đọc mọi con số của skill này qua lăng kính này

Skill này chứa nhiều số đo thật, lấy từ kho tham chiếu. **Số thật không tự động là luật.** Mỗi định mức trong `dang/` mang một nhãn:

| Nhãn | Tư cách | Được phép lệch? |
|---|---|---|
| **[BẮT BUỘC]** | Yêu cầu có thật của kênh/khách (độ dài video, CTA, trần title) | Không |
| **[MỤC TIÊU]** | Việc đoạn văn phải làm được (tạo tò mò · trả đúng nợ · chịu thiệt trước cú lật) | Không — nhưng **tự do hoàn toàn về cách làm** |
| **[THAM KHẢO]** | Kho tham chiếu hay làm thế (thứ tự các bước · tỉ lệ câu ngắn · motif · công thức title) | Có, và **nên lệch khi truyện đòi** |

Đối xử với một định mức [THAM KHẢO] như thể nó là [BẮT BUỘC] chính là cách biến mọi kịch bản mới thành bản sao thống kê của kho cũ.

## Ranh giới với hai skill kia

| Skill | Sở hữu việc gì |
|---|---|
| **skills-kich-ban** (file này) | Sinh ra chữ: title · hook · thân truyện → `KICH-BAN.md` |
| `skills-film` | Biến `KICH-BAN.md` đã có thành `sf-board.json` (SF, shot, prompt video, nhạc) |
| `skills-hook` | Như trên nhưng bó đúng 120 giây cho `HOOK-*.project` |

Kịch bản chưa xong thì không đụng vào `sf-board.json`. Bàn giao ở `7-file-va-ban-giao.md` §4.

## Quy trình — chạy thẳng, tự kiểm ở mỗi cửa

User bảo "viết kịch bản" là **chạy trọn từ đầu đến cuối, không hỏi lại**. Mỗi bước có một **cửa QC**: không qua thì sửa tại chỗ rồi kiểm lại, qua rồi mới đi tiếp. Chỉ dừng hỏi user khi gặp một trong ba việc ở §Khi nào mới được dừng.

| Bước | Làm gì | Mở thêm file | Cửa QC — qua rồi mới đi tiếp |
|---|---|---|---|
| **1** Chọn dạng bài | User có ý tưởng → chọn dạng khớp *khởi động* + *cú lật*. Không có ý tưởng → **random**, trừ dạng của hai bài gần nhất | [1-chon-dang](references/1-chon-dang.md) | Ghi ra `DẠNG BÀI` · `SỰ THẬT LÕI` · `HẬU QUẢ` . Báo cho user biết đã chọn dạng nào, rồi **đi tiếp luôn** |
| **2** Title | Dựng 5 phương án, tự chấm, **tự chọn 1** | [2-title](references/2-title.md) | `2-title.md` §5. Phương án được chọn phải qua sạch checklist — không qua thì viết lại, đừng hạ chuẩn để lấy cho đủ |
| **3** Hook | 115–175 từ, tám nhiệm vụ | [3-hook](references/3-hook.md) · [5-nhan-vat](references/5-nhan-vat-va-chi-tiet.md) · [6-giong-van](references/6-giong-van.md) | `3-hook.md` §6 + `KHUNG-CHUNG.md` §7 phần hook + checklist dạng bài. Đếm từ thật. Báo mức thoại đã chọn cùng lúc báo số từ. Tách riêng **câu lời hứa** để bước 7 đối chiếu |
| **4a** Thân — dựng người | Giai đoạn 1–3 | [4-than-truyen](references/4-than-truyen.md) · [5-nhan-vat](references/5-nhan-vat-va-chi-tiet.md) · [6-giong-van](references/6-giong-van.md) | Đủ việc của ba giai đoạn theo §3 dạng bài · **số từ khớp ngân sách đã chốt cho GĐ 1–3 (lệch >10% thì sửa ngay, đừng hẹn bù ở 4c)** · nhịp câu đạt · đã gài xong mọi thứ giai đoạn 6 sẽ dùng |
| **4b** Thân — sự việc | Giai đoạn 4–5 | như trên | Mất mát có thật và **đúng kiểu của dạng bài** · **số từ khớp ngân sách GĐ 4–5** · chưa lộ cú lật |
| **4c** Thân — lật và kết | Giai đoạn 6–7 | như trên | Cú lật kể từng bước, không tóm tắt · CTA cuối đủ ba phần · tổng bài trong 7.300–8.050 từ |
| **5** Mô tả | Viết mô tả YouTube từ kịch bản vừa xong | [9-mo-ta-youtube](references/9-mo-ta-youtube.md) | `9-mo-ta-youtube.md` §6. Mọi dữ kiện phải đối chiếu được với `KICH-BAN.md` — không bịa thêm con số nào cho kêu |
| **6** Giao | Ghi file, chốt sổ | [7-file-va-ban-giao](references/7-file-va-ban-giao.md) | File đúng chỗ, có Lịch sử sửa. Dừng — không tự sang khâu dựng board |

**Cửa QC là cửa thật.** Không qua thì sửa rồi kiểm lại, không đi tiếp và hẹn "sẽ chỉnh sau". Lỗi ở hook mà mang xuống thân là lỗi phải sửa 7.500 từ.

**Ghi file từ bước 3, không đợi bước 7.** Hook qua cửa là ghi ngay vào `KICH-BAN.md`; mỗi lượt 4a/4b/4c ghi nối tiếp. Bước 6 chỉ chốt sổ.

**Báo tiến độ, đừng hỏi xin phép.** Sau mỗi bước nói ngắn: đã làm gì, số từ, đang sang bước nào. User đọc và can thiệp nếu muốn — nhưng không phải đợi user gật mới chạy tiếp.

### Khi nào mới được dừng hỏi user

Đúng ba trường hợp. Ngoài ba cái này thì tự quyết:

1. **Không dạng bài nào khớp ý tưởng user đưa** — không ép vào dạng gần nhất (`1-chon-dang.md` §3).
2. **Ý tưởng thiếu một dữ kiện mà đoán bừa sẽ hỏng cả bài** — ví dụ user muốn có thật một nhân vật cụ thể nhưng không nói họ làm nghề gì.
3. **Một cửa QC không qua sau hai lần viết lại** — báo thẳng chỗ kẹt thay vì giao bài lỗi.

### Random dạng bài

Không có ý tưởng cụ thể thì bốc thật, đừng luôn chọn `REVEAL` vì nó phổ biến nhất.

```bash
grep -rh "^> \*\*DẠNG BÀI\*\*" *.project/KICH-BAN.md 2>/dev/null | tail -2
```

Hai dạng vừa dùng bị loại khỏi lượt bốc này. Tỉ trọng kho ở `KHUNG-CHUNG.md` §8 **không phải chỉ tiêu** — `INVESTIGATION` chiếm 2% kho nhưng là dạng khó lặp lại nhất, đừng né nó.

## Bảng chủ quyền — luật nào nằm ở file nào

**Mỗi khái niệm có đúng một file làm chủ. Mọi chỗ khác chỉ được trỏ tên, không được chép lại.**

| Khái niệm | File làm chủ |
|---|---|
| Vì sao người xem ở lại · khoảng trống thông tin · lời hứa & trả nợ · đảo định kiến · nhịp cảm xúc | `references/0-nguyen-ly-ke-chuyen.md` |
| Ba tầng luật · hợp đồng 12 tham số · quy trình bước 1 · **cách mở rộng** · sổ khung chung | `references/1-chon-dang.md` |
| Title là hợp đồng · vế sau phải lật · luật trình 5 phương án · cấm kỵ trong title | `references/2-title.md` |
| Hook làm gì · luật chung của chuỗi nước đi · luật chung của CTA · luật câu chốt | `references/3-hook.md` |
| Thân là hoá đơn · luật chung của khung khối · chỗ trả nợ · gieo & nở · kết vòng | `references/4-than-truyen.md` |
| Tên riêng · dữ kiện cứng · luật bịa · vật chứng | `references/5-nhan-vat-va-chi-tiet.md` |
| **Số viết bằng chữ** (và ngoại lệ mã hiệu) · cấm sáo ngữ · tiếng Anh/tiếng Việt ở đâu | `references/6-giong-van.md` |
| Tên folder dự án · khung `KICH-BAN.md` · Lịch sử sửa · bàn giao sang skills-film/hook | `references/7-file-va-ban-giao.md` |
| Mười một khối của mô tả YouTube · ba bài học · độ dài · từ khoá | `references/9-mo-ta-youtube.md` |
| **Mọi giá trị định mức** (độ dài, nhịp câu, CTA, trần title) · tám nhiệm vụ hook · bảy nhiệm vụ thân | `dang/KHUNG-CHUNG.md` |
| **Cái gì khởi động · cú lật là gì · công thức vế trước của title · cấm riêng** | `dang/bai/<DẠNG-BÀI>.md` |

**Luật phân tầng, dùng khi không biết viết luật mới vào đâu:**

> Đúng bất kể viết gì → `references/`.
> Đúng với cả tám dạng bài, đổi thì tám cái cùng đổi → `dang/KHUNG-CHUNG.md`.
> Chỉ đúng với một kiểu chuyện → `dang/bai/<DẠNG-BÀI>.md`.

## Luật cứng khi viết kịch bản mới

- **Không đọc project cũ.** Viết kịch bản mới thì không mở `KICH-BAN.md` của phim khác để "tham khảo". Luật viết nằm ở `references/` và `dang/`, không nằm ở phim cũ. Mở phim cũ là cách chắc chắn nhất để đẻ ra bản sao mờ của nó. *(Ngoại lệ duy nhất: user gửi mẫu để rút định mức cho một dạng mới — `1-chon-dang.md` §4.)*
- **`kho-tham-chieu/` là kho tham chiếu, không phải nguồn để viết, chỉ dùng khi user bảo cần research vào để fix skill.** 349 kịch bản KHUNG-CHUNG tải từ sheet gốc (~15MB, không track git), kèm `TITLES.md` liệt kê toàn bộ title và số từ. **Chỉ mở khi cần thông tin để sửa skill** (`1-chon-dang.md` §4). **Đang viết một kịch bản thì cấm mở** — kể cả để "xem người ta làm thế nào"; đó chính là cách kho nuốt bài mới. *(Ngoại lệ duy nhất: bước 2 TITLE **bắt buộc** mở `kho-tham-chieu/TITLES.md` để lấy lõi tình huống — `2-title.md` §0. Ngoại lệ chỉ cho file title, không cho `kich-ban/` và `short/`.)*
- **Kịch bản đã ghi ra file thì không tự sửa.** Chỉ sửa khi user yêu cầu đích danh, và phải ghi vào khối Lịch sử sửa.
- **Không tự chế dạng bài mới.** Không dạng nào khớp → dừng, hỏi user xin kịch bản mẫu. Đừng ép câu chuyện vào dạng gần nhất.
- **Không tự sửa skill khi user chê output.** User bảo sửa thì mới sửa.
- **Không chép chữ từ bộ luật vào bài giao.** Tên nhiệm vụ, tên dạng bài, và nhất là **các câu ví dụ trong `dang/`** — ví dụ ở đó là mẫu vật để nhận dạng, không phải chất liệu để dùng lại.
- **Ý tưởng title đến từ kho, phần còn lại thì không.** Title phải mọc từ một dòng có thật trong `kho-tham-chieu/TITLES.md` (`2-title.md` §0). Hook, thân truyện, nhân vật, chi tiết thì viết mới — không lấy từ kho.
- **Motif đến từ user, không từ kho.** Nghề nghiệp, bối cảnh, sắc tộc, kiểu xung đột của kho tham chiếu là *mô tả kho*, không phải điều kiện của thể loại.

## Ghi luật mới

Luật mới đến thì hỏi hai câu, theo thứ tự:

1. *"Luật này có phụ thuộc dạng không?"* → có thì vào `dang/`, không thì vào `references/`.
2. *"Khái niệm nào của tôi sở hữu nó?"* → không file nào nhận thì thiếu file; hai file cùng nhận thì ranh giới sai, sửa ranh giới, đừng nhét bừa một chỗ.

- **Luật đếm được** → ghi ngưỡng vào file sở hữu nó, **kèm nhãn**, **và thêm một dòng vào checklist cuối file đó**. Ngưỡng không nằm trong checklist thì không ai kiểm.
- **Luật mới mặc định là [THAM KHẢO].** Muốn nâng lên [MỤC TIÊU] phải trả lời được: *bỏ nó đi thì truyện hỏng ở chỗ nào?* Không trả lời được thì nó là thói quen, không phải luật.
- **Mỗi "cấm" phải kèm lý do hỏng gì.** Cấm không nêu được hậu quả là sở thích cá nhân đang đội lốt luật.
- **Thêm tham số mới** = sửa bảng §2 của `1-chon-dang.md` + sửa file lõi khai báo nó + điền vào **mọi** hồ sơ dạng đang có + sửa `dang/_MAU-KHUNG-CHUNG.md`. Không làm đủ bốn việc thì đừng thêm.
- **Một dạng đòi phá luật lõi** (chứ không chỉ đổi giá trị) là dấu hiệu lõi đang chứa thứ lẽ ra phải là tham số. Sửa lõi thành tham số, đừng nhét ngoại lệ vào hồ sơ dạng.
- **Không chép lại luật của file khác** — chỉ trỏ tên file + tên mục.

## Tự kiểm

**checklist cuối mỗi file luật** — làm xong bước nào thì mở lại file của bước đó và kiểm đã qua hết chưa.

| Bước vừa xong | Checklist ở |
|---|---|
| Bước 1 — chọn dạng bài | `references/1-chon-dang.md` §6 |
| Bước 2 — title | `references/2-title.md` §5 |
| Bước 3 — hook | `references/3-hook.md` §6 · `dang/KHUNG-CHUNG.md` §7 · checklist cuối dạng bài |
| Bước 4a–4c — thân | `references/4-than-truyen.md` §7 · `dang/KHUNG-CHUNG.md` §7 · checklist cuối dạng bài |
| Trong lúc viết — nhân vật & chi tiết | `references/5-nhan-vat-va-chi-tiet.md` §6 |
| Trong lúc viết — giọng văn | `references/6-giong-van.md` §6 |
| Bước 5 — mô tả YouTube | `references/9-mo-ta-youtube.md` §6 |
| Bước 6 — ghi file & bàn giao | `references/7-file-va-ban-giao.md` §6 |

Cả ba checklist **đều phải chạy**: lõi kiểm form, khung chung kiểm số, dạng bài kiểm cú lật.

**Hai tầm kiểm — đừng nhầm:**
- **Tầm đoạn**: đếm trong phạm vi một đoạn (câu dài quá không, số đã viết bằng chữ chưa, chi tiết có cụ thể không).
- **Tầm kịch bản**: chỉ lộ ra khi đọc cả bài (lời hứa ở hook có được trả không, chi tiết gieo ở đầu có nở ở cuối không, một chi tiết có bị lặp ba lần không, tổng số từ).

Viết xong hook mà chỉ kiểm tầm đoạn thì **chưa kiểm gì cả** ở tầm kịch bản. Các mục tầm kịch bản đã ghi rõ "toàn bài" trong từng checklist.

## Vận hành

- **Chốt sự thật lõi trước khi viết chữ nào.** Một câu, ≤ 25 từ, trả lời: *chuyện này thật ra nói về cái gì mà khán giả chưa biết?*
- **Ngôn ngữ**: kịch bản (title, hook, thân truyện, thoại) viết **tiếng Anh**; khung file, ghi chú, lịch sử sửa và toàn bộ đối thoại với user viết **tiếng Việt**. Bảng đầy đủ ở `6-giong-van.md` §5.
