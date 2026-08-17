---
name: skills-film
description: Viết/sửa prompt ảnh nhân vật, Start Frame (SF), prompt video Grok và prompt nhạc Suno trong sf-board.json của các dự án PIPELINE-*.project. Dùng skill này mỗi khi tạo REF nhân vật mới, tạo SF cho một scene, chia shot, viết hoặc sửa prompt video, viết nhạc cho nhịp không thoại, hoặc sửa ngoại hình/trang phục nhân vật trong board — kể cả khi user chỉ nói "tạo SF cho scene X", "viết prompt video S8", "prompt S8 chuẩn chưa" mà không nhắc rõ kỹ thuật.
---

# Làm phim từ kịch bản

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
| **1** | **Chia shot**: Bảng shot (1 shot = 1 SF), chèn nhịp lặng, nối shot, khai báo `goc`. | [1-chia-shot.md](references/1-chia-shot.md) |
| **2** | **Tạo hình & Địa điểm (REF)**: Ảnh portrait, full-body từng trang phục, Thẻ địa điểm (mọi biến thể Sáng/Tối của địa điểm đó xuất hiện trong kịch bản). | [2-tao-hinh-va-dia-diem.md](references/2-tao-hinh-va-dia-diem.md) |
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
1. **Làm bảng shot trước, sinh prompt sau**: Bảng shot quyết định danh sách SF. Kiểm máy trên bảng cho sạch RỒI mới sinh prompt.
2. **Mẫu hoá khối lặp ĐÚNG CHỖ**: 85% nội dung (bối cảnh, trang phục, trục...) để ở `luatchung` của thẻ địa điểm. Bố cục có 6 khung xương, SF chỉ khai tham số.
3. **MỘT SHOT = MỘT SF**: Số SF = số shot. Cùng góc nhưng khác beat/tay thì vẫn sinh SF mới.
4. **Gộp scene**: Gộp 5-6 scene làm một lượt để tiết kiệm token nạp luật.
5. **Chạy song song**: Có thể dùng subagent chạy song song nhiều scene, nhưng **phải chung thư viện dựng prompt**.
6. **Hai chế độ**: Làm theo lệnh user từng bước, hoặc "tạo hết" (chạy 5 bước, tự duyệt). Việc viết prompt có thể gộp, nhưng chạy ảnh luôn tuần tự (ảnh sau đính ảnh trước làm background).

---

## Kịch bản & Ghi luật
- **File kịch bản**: Mỗi dự án có 1 `KICH-BAN.md` (bản người đọc). TUYỆT ĐỐI KHÔNG tự ý sửa kịch bản gốc. Chỉ cập nhật kịch bản khi user yêu cầu đích danh, và phải ghi lịch sử ở đầu file (ngày, scene, sửa gì, vì sao).
- **Ghi luật mới**: 
  - Luật đếm được -> ghi vào `kiem-luat.py`, không ghi văn bản.
  - Ghi rõ luật áp cho loại việc nào.
  - ⛔ **Tìm luật cũ trước khi viết mới**. Ưu tiên sửa luật cũ cho sắc hơn, tránh thêm mục mới gây loãng.
  - ⛔ **Không tự sửa skill khi user chê output**.
