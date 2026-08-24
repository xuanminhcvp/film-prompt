---
name: skills-hook
description: Viết/sửa prompt ảnh nhân vật, Start Frame (SF), prompt video Grok và prompt nhạc Suno trong sf-board.json cho các video Hook ngắn (khoảng 2 phút). Dùng skill này mỗi khi tạo REF nhân vật mới, tạo SF, chia shot, viết prompt video có chứa câu dẫn chuyện (narration) và thoại, hoặc sửa ngoại hình nhân vật trong board.
---

# Làm video Hook từ kịch bản

> **LUẬT TUYỆT ĐỐI**: File này chứa quy trình và chỉ mục. Chi tiết luật nằm ở các file `references/`. Giữ file dưới 5.000 token. Đừng thêm luật dài vào đây.

**LƯU Ý BẮT BUỘC:**  ưu tiên tuân thủ các quy tắc tại [phong-cach-rieng.md] nếu có (references/phong-cach-rieng.md) trong mọi bước.

## Mục lục
- [Quy trình 5 bước](#quy-trình-5-bước)
- [Phạm vi & Bản đã duyệt](#phạm-vi--bản-đã-duyệt)
- [Kiểm tra bằng Script](#kiểm-tra-bằng-script)
- [Luật viết nhanh](#luật-viết-nhanh)
- [Kịch bản & Ghi luật](#kịch-bản--ghi-luật)

---

## Quy trình 5 bước
**MỖI BƯỚC MỘT FILE, và là nguồn sự thật duy nhất cho bước đó**. Bắt buộc mở file của bước trước khi viết prompt.

| Bước | Việc | Đọc file |
|---|---|---|
| **0B** | **Tiêu chuẩn D.O.P**: Hệ thống quy tắc về Chất ảnh (Image Quality), Màu sắc (Color Palette) và Ánh sáng (Lighting). | [7-nghe-thuat-anh-sang.md](references/7-nghe-thuat-anh-sang.md) |
| **1** | **Chia shot**: Bảng shot (1 shot = 1 SF), chèn nhịp lặng, nối shot, khai báo `goc`. | [1-chia-shot.md](references/1-chia-shot.md) |
| **2** | **Tạo hình & Địa điểm (REF)**: Mẫu hoá khối lặp (85% nội dung bối cảnh, trang phục...), SF chỉ khai tham số. | [2-tao-hinh-va-dia-diem.md](references/2-tao-hinh-va-dia-diem.md) |
| **3** | **Prompt SF (Khung hình)** | [3-prompt-sf.md](references/3-prompt-sf.md) |
| **4** | **Prompt video** | [4-prompt-video.md](references/4-prompt-video.md) |
| **5** | **Prompt nhạc Suno** | [5-nhac-suno.md](references/5-nhac-suno.md) |

## Kiểm tra bằng Script
**MÁY KIỂM, ĐỪNG KIỂM TAY.** Mọi ngưỡng đếm được đã nằm trong script.
```bash
python3 sfboard/kiem-luat.py <PROJECT> [--scene S6]        # 21 luật cứng
python3 sfboard/kiem-noi-shot.py <PROJECT> [S6] --day-du   # Nối shot: zone, tư thế, tay
```
- **Lưu ý 2 tầm kiểm**: Phép kiểm chạy ở tầm hẹp (1 scene) không bao phủ tầm rộng (cấp phim). Các luật liên-scene (chuỗi tối liền, trang phục) **TỰ TẮT** khi chạy `--scene`. Hãy đọc phần dữ liệu chưa phủ trước khi tin là "SẠCH".
- **Checklist mắt**: Góc máy thực tế (nhìn cột GÓC, đừng chỉ nhìn "hướng thứ N"), trang sức/mức sống/độ tuổi, sự hợp lý của nhân vật ở địa điểm/thời điểm, tay kể chuyện, nhạc Suno cho nhịp lặng.

---

## Luật viết nhanh
1. **Chuẩn chỉ 2 phút đầu (Không bỏ text, Không nhảy text)**: Dù user gửi kịch bản dài để lấy ngữ cảnh, BẠN CHỈ LÀM ĐÚNG 2 PHÚT ĐẦU NỘI DUNG tính từ câu đầu tiên (tương đương ~120 giây / 10-15 shot) — 120 giây là ngân sách cho thoại + lời dẫn cộng lại. Trong 2 phút đầu này, BẮT BUỘC giữ nguyên 100% NGUYÊN VĂN TOÀN BỘ TEXT (cả thoại nhân vật VÀ lời dẫn narrator) theo đúng thứ tự thời gian từ trên xuống dưới. TUYỆT ĐỐI KHÔNG bỏ bớt bất kỳ câu text nào, KHÔNG nhảy text linh tinh, và KHÔNG tráo thứ tự. Đến mốc ~120s (hết 2 phút đầu) thì dừng lại, không chia tiếp kịch bản phía sau. Thứ tự text từ kịch bản phải đồng bộ 1-1 chính xác tuyệt đối giữa mảng `sfs` (SF) và mảng `shots` (Video).
2. **Làm bảng shot trước, sinh prompt sau**: Bảng shot quyết định danh sách SF. Kiểm máy trên bảng cho sạch RỒI mới sinh prompt.
3. **Mẫu hoá khối lặp ĐÚNG CHỖ**: 85% nội dung (bối cảnh, trang phục...) để ở prompt của thẻ địa điểm. Bố cục có 6 khung xương, SF chỉ khai tham số.
4. **MỘT SHOT = MỘT SF**: Số SF = số shot. Cùng góc nhưng khác beat/tay thì vẫn sinh SF mới.
5. **Gộp scene**: Gộp 5-6 scene làm một lượt để tiết kiệm token nạp luật.
6. **Chạy song song**: Có thể dùng subagent chạy song song nhiều scene, nhưng **phải chung thư viện dựng prompt**.
7. **Hai chế độ**: Làm theo lệnh user từng bước, hoặc "tạo hết" (chạy 5 bước, tự duyệt). Việc viết prompt có thể gộp.
8. Sửa gì trong file sf-board.json thì nhớ phải sửa cả những thứ liên quan bị ảnh hưởng theo nữa.
---

## Kịch bản & Ghi luật
- **File kịch bản**: Mỗi dự án có 1 `KICH-BAN.md` (bản người đọc). TUYỆT ĐỐI KHÔNG tự ý sửa kịch bản gốc. Chỉ cập nhật kịch bản khi user yêu cầu đích danh, và phải ghi lịch sử ở đầu file (ngày, scene, sửa gì, vì sao).
- **Thẻ Siêu dữ liệu Kịch bản (Metadata Tags)**: Kịch bản có thể chứa các thẻ ngữ cảnh (vd: `[SCENE CONTEXT]`, `[SCENE PURPOSE]`, `[INTENTION]`, `[BEAT]`, `[KNOWLEDGE]`, `[END STATE]`). BẮT BUỘC coi đây là lời diễn giải tâm lý/đạo diễn để sinh biểu cảm và nhịp phim chính xác. **TUYỆT ĐỐI KHÔNG** coi các thẻ này là lời thoại, không cho nhân vật đọc lên, và không render chúng ra như chữ viết trên màn hình.
- **Ghi luật mới**: 
  - Luật đếm được -> ghi vào `kiem-luat.py`, không ghi văn bản.
  - Ghi rõ luật áp cho loại việc nào.
  - ⛔ **Tìm luật cũ trước khi viết mới**. Ưu tiên sửa luật cũ cho sắc hơn, tránh thêm mục mới gây loãng.
  - ⛔ **Không tự sửa skill khi user chê output**.
