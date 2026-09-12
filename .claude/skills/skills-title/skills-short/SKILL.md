---
name: skills-short
description: Viết/sửa prompt ảnh nhân vật, Start Frame (SF) và prompt video Grok trong sf-board.json của các dự án Short (SHORT-*.project). Toàn bộ ảnh REF, Master SF, SF và video đều là KHUNG DỌC 9:16. Mọi clip ở mốc 10 giây, thoại lấp ≥80% mỗi clip; tổng thời lượng suy ra từ số chữ của Short, tuyệt đối không dùng nhịp lặng, dù user có gửi cả kịch bản dài (chỉ dùng kịch bản để lấy ngữ cảnh và nhân vật chuẩn).
---

# Làm phim Short từ kịch bản

> **Luật tuyệt đối: File này chỉ chứa quy trình + bảng chủ quyền**. Mọi luật chi tiết nằm ở `references/`.
> Giữ file dưới 5.000 token. Không tóm tắt luật của file khác vào đây — bản tóm tắt luôn là bản thứ hai đang chờ trôi khỏi bản gốc.

## Quy trình

**Mỗi bước mở đúng file mình cần.** Một bước có thể mở nhiều file — đó là bình thường.

| Bước | Việc | Mở file | Xong khi |
|---|---|---|---|
| 0 | Đọc kịch bản (lấy ngữ cảnh/nhân vật chuẩn, chốt đoạn Short) | [0-tu-duy-dien-anh.md](references/0-tu-duy-dien-anh.md) · [1-kich-ban.md](references/1-kich-ban.md) | Trích xuất ngữ cảnh/nhân vật & tính số shot từ số chữ của Short |
| 1 | Dựng dự án + khung `sf-board.json` | [2-du-lieu-sf-board.md](references/2-du-lieu-sf-board.md) | JSON đủ scene theo mọi heading `##` thuộc đoạn Short |
| 2 | Tạo thẻ REF: người · vật · nơi chốn | [3-ref-nhan-vat.md](references/3-ref-nhan-vat.md) · [4-ref-dao-cu.md](references/4-ref-dao-cu.md) · [5-the-dia-diem.md](references/5-the-dia-diem.md) | User duyệt 100% thẻ địa điểm |
| 3 | Phân rã thế trận → chốt cụm không gian | [6-cum-va-master-sf.md](references/6-cum-va-master-sf.md) | Mỗi cụm có đúng 1 Master SF |
| 4 | Lập bảng shot chi tiết (tính theo số từ) | [7-bang-shot.md](references/7-bang-shot.md) | Bảng shot qua hết §7 Kiểm tra (mọi shot 10s, 0 nhịp lặng) |
| 6 | Sinh Master SF | [6-cum-va-master-sf.md](references/6-cum-va-master-sf.md) | Mọi Master trỏ `refs.bg` về Thẻ Địa Điểm |
| 7 | Sinh SF thường | [8-prompt-sf.md](references/8-prompt-sf.md) · [9-quan-chung-nen.md](references/9-quan-chung-nen.md) | Mọi SF trỏ đúng Master của cụm mình |
| 8 | Viết prompt video | [11-prompt-video.md](references/11-prompt-video.md) | Prompt video qua hết §6 Kiểm tra cuối bước |
| ⚠️ | Bất cứ lúc nào khung có trẻ em | [KHI-CO-TRE-EM.md](references/KHI-CO-TRE-EM.md) | — |

## Bảng chủ quyền — luật nào nằm ở file nào

**Mỗi khái niệm có đúng một file làm chủ. Mọi chỗ khác chỉ được trỏ tên, không được chép lại.**

| Khái niệm | File làm chủ |
|---|---|
| Triết lý chuyển góc · Drama Flow · vì sao camera AI khác camera thật · nhịp cảm xúc phản diện · đối đầu trực diện từ khung đầu · **cấm low-angle chếch ngược lên mặt (+ câu chặn gốc)** | `0-tu-duy-dien-anh.md` |
| Kịch bản gốc · giới hạn Short đếm theo chữ (kịch bản dài chỉ lấy ngữ cảnh/nhân vật) · thẻ metadata `[BEAT]` · cấm sửa thoại · thứ tự Thoại/Narration · tách câu dài quá trần · xử lý khi nối thêm Short vượt trần 120s | `1-kich-ban.md` |
| Schema JSON (gồm mảng `shots[]` video) · mã ID · chuỗi neo `refs` · trần 4 nhân vật · trần ký tự · **khung dọc 9:16 toàn dự án** · dòng `KHUNG DỌC 9:16` | `2-du-lieu-sf-board.md` |
| Portrait · full-body · trang phục · mức sống · y phục chức vụ · trang sức | `3-ref-nhan-vat.md` |
| `REF_PROP_*` — khi nào tạo, chụp thế nào | `4-ref-dao-cu.md` |
| Thẻ địa điểm · quy hoạch 360° · biến thể giờ · chất ảnh · màu · ánh sáng | `5-the-dia-diem.md` |
| Cụm không gian · Master SF · khung gối đầu hai cụm · **thế trận so le theo chiều sâu (cấm dàn hàng ngang)** | `6-cum-va-master-sf.md` |
| Danh sách shot · mọi shot 10s · **bộ góc khung dọc 9:16** · định mức tỉ lệ cỡ cảnh · **trần người rõ mặt theo cỡ cảnh** · **SF một nhân vật (Solo Frame)** · dòng `goc` · thời lượng & mật độ thoại · continuity · **cấm tái sử dụng ảnh SF (số SF = số shot)** | `7-bang-shot.md` |
| Prompt SF thường · bố cục **ba dải dọc & vùng an toàn UI** · chữ trong khung · hậu cảnh · trạng thái chờ · biểu cảm kìm nén trên khung tĩnh | `8-prompt-sf.md` |
| Quần chúng nền · xe cộ đang chạy · mật độ sinh tồn | `9-quan-chung-nen.md` |
| Form prompt video · thang an toàn camera · lip sync · kết clip · khối TIMING/không lồng narrator · đồng bộ dòng `CUT 1` · **tầng diễn xuất (hành vi thay tính từ, chống nhân vật bị "đơ")** | `11-prompt-video.md` |
| An toàn trẻ em · cấm hở hang | `KHI-CO-TRE-EM.md` |
| Mọi con số đếm được (trần từ, tỉ lệ, định mức) | file luật sở hữu khái niệm đó — **và phải có mặt trong checklist cuối file ấy** |

## Ghi luật mới

Luật mới đến thì hỏi: *"khái niệm nào của tôi sở hữu nó?"* Không file nào nhận → thiếu file. Hai file cùng nhận → ranh giới sai, sửa ranh giới, đừng nhét bừa một chỗ.

- **Luật đếm được** → ghi ngưỡng vào file luật sở hữu nó, **và thêm một dòng vào checklist cuối file đó**. Ngưỡng không nằm trong checklist thì không ai kiểm.
- **Ghi rõ luật áp cho loại việc nào** (khối phạm VI áp dụng ở đầu mỗi file, gồm cả dòng *không chứa*).
- **Tìm luật cũ trước khi viết mới.** Ưu tiên sửa luật cũ cho sắc hơn, tránh thêm mục mới gây loãng, nếu chưa có luật nào liên quan thì mới viết mới.
- **Không tự sửa skill khi user chê output.** → User bảo sửa thì mới sửa nhé.
- **Không chép lại luật của file khác** — chỉ trỏ tên file + tên mục. Chép một câu cũng đủ để hai bản trôi khỏi nhau.

## Tự kiểm

**checklist cuối mỗi file luật** — làm xong bước nào thì mở lại file của bước đó và kiểm tra đã qua hết checklist chưa.

| Bước vừa xong | Checklist ở |
|---|---|
| Kịch bản | `1-kich-ban.md` §5 |
| Dữ liệu / mã ID | `2-du-lieu-sf-board.md` §10 |
| Thẻ nhân vật | `3-ref-nhan-vat.md` §8 |
| Thẻ đạo cụ | `4-ref-dao-cu.md` §4 |
| Thẻ địa điểm | `5-the-dia-diem.md` §5 |
| Cụm & Master SF | `6-cum-va-master-sf.md` §4 |
| Bảng shot | `7-bang-shot.md` §7 |
| Prompt SF | `8-prompt-sf.md` §7 |
| Quần chúng nền | `9-quan-chung-nen.md` §6 |
| Prompt video | `11-prompt-video.md` §6 |
| Khung có trẻ em | `KHI-CO-TRE-EM.md` §3 |

**Hai tầm kiểm — đừng nhầm:**
- **Tầm scene**: đếm trong phạm vi một scene/cụm (tỉ lệ khung, đủ cast, continuity giữa shot liền nhau).
- **Tầm phim**: chỉ lộ ra khi nhìn cả kịch bản (tỉ lệ tái sử dụng SF · mật độ thoại · tỉ lệ nhịp lặng · tỉ lệ cỡ cảnh · chuỗi scene tối liền · trang phục qua nhiều scene).

Làm xong 5–6 scene mà chỉ kiểm tầm scene thì **chưa kiểm gì cả** ở tầm phim. Các mục tầm phim đã ghi rõ "toàn phim" trong từng checklist.

## Vận hành

- **Gộp scene**: gộp 5–6 scene làm một lượt để tiết kiệm token nạp luật.
- **Chạy song song**: có thể dùng subagent chạy song song nhiều scene, nhưng phải chung thư viện dựng prompt.
- **Hai chế độ**: làm theo lệnh user từng bước, hoặc "tạo hết" (chạy trọn quy trình, tự duyệt). Việc viết prompt có thể gộp.
- **Sửa dây chuyền**: sửa gì trong `sf-board.json` thì rà cả những thứ liên quan bị ảnh hưởng theo (`2-du-lieu-sf-board.md` §6).
