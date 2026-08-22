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

## Quy trình cốt lõi
**MỖI BƯỚC MỘT FILE, và là nguồn sự thật duy nhất cho bước đó**. Bắt buộc mở file của bước trước khi viết prompt.

| Bước | Việc | Đọc file |
|---|---|---|
| **00** | **Khởi tạo Dự án**: Cấu trúc thư mục, khởi tạo `sf-board.json` chuẩn Schema. | [00-khoi-tao-du-an.md](references/00-khoi-tao-du-an.md) |
| **0A** | **Tư duy đạo diễn**: Nền tảng triết lý chuyển góc máy, nhịp điệu kể chuyện và kiểm soát cảm xúc khán giả. | [6-tu-duy-dien-anh.md](references/6-tu-duy-dien-anh.md) |
| **0B** | **Tiêu chuẩn D.O.P**: Hệ thống quy tắc về Chất ảnh (Image Quality), Màu sắc (Color Palette) và Ánh sáng (Lighting). | [7-nghe-thuat-anh-sang.md](references/7-nghe-thuat-anh-sang.md) |
| **1** | **Phân rã Blocking & Chia shot**: Bảng shot & tái sử dụng SF, chèn nhịp lặng, nối shot, khai báo `goc`. | [1-chia-shot.md](references/1-chia-shot.md) |
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
- **Checklist mắt**: Góc máy thực tế (nhìn cột GÓC, đừng chỉ nhìn "hướng thứ N"), trang sức/mức sống/độ tuổi, sự hợp lý của nhân vật VÀ CỦA CHÍNH ĐỊA ĐIỂM ở thời điểm đó (xe cộ di chuyển trên đường, hàng quán mở/đóng, đèn bật/tắt, rác thải bối cảnh...), tay kể chuyện, nhạc Suno cho nhịp lặng.

---

## Luật viết nhanh
1. **Làm bảng shot trước, sinh prompt sau**: Bảng shot quyết định danh sách SF. Kiểm máy trên bảng cho sạch RỒI mới sinh prompt.
2. **Mẫu hoá khối lặp ĐÚNG CHỖ**: 85% nội dung (bối cảnh, trang phục...) để ở phần Prompt của Thẻ Địa Điểm. Prompt SF viết thành các đoạn văn điện ảnh (Cinematic) mạch lạc thay vì điền form cứng nhắc.
3. **TẠO VÀ TÁI SỬ DỤNG SF**: Mỗi shot mới mặc định có mã SF tương ứng, nhưng **BẮT BUỘC tái sử dụng SF cũ** khi đối thoại đảo góc máy A-B-A-B (cùng nhân vật, góc máy, tư thế và nón quan sát).
4. **Gộp scene**: Gộp 5-6 scene làm một lượt để tiết kiệm token nạp luật.
5. **Chạy song song**: Có thể dùng subagent chạy song song nhiều scene, nhưng **phải chung thư viện dựng prompt**.
6. **Hai chế độ**: Làm theo lệnh user từng bước, hoặc "tạo hết" (chạy 5 bước, tự duyệt). Việc viết prompt có thể gộp.
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
