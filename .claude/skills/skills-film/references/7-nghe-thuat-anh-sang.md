# Nghệ Thuật Ánh Sáng Điện Ảnh (Cinematography)

> Khác biệt lớn nhất giữa một đoạn phim tài liệu và một bộ phim điện ảnh nằm ở **Ánh sáng có chủ đích**. File này đóng vai trò như một Giám đốc Hình ảnh (D.O.P), trang bị cho AI hệ thống từ vựng để đánh sáng, đổ bóng và tô màu (Color Grading) cho các Thẻ địa điểm và khung hình.

## ⚠️ PHẠM VI ÁP DỤNG (SCOPE) - BẮT BUỘC ĐỌC
1. **CHỈ DÙNG CHO BỐI CẢNH (Thẻ Địa Điểm):** Mọi kỹ thuật ánh sáng, tương phản và bảng màu trong file này CHỈ được phép áp dụng khi tạo Prompt cho **Thẻ Địa Điểm (`REF_BG`)**.
2. **CẤM DÙNG CHO NHÂN VẬT:** Tuyệt đối KHÔNG áp dụng đánh sáng điện ảnh (đổ bóng gắt, tối, tương phản cao) vào Thẻ Nhân Vật (Portrait / Full-body). Ảnh REF nhân vật bắt buộc phải dùng ánh sáng studio dịu nhẹ, đều, phẳng để lấy nét rõ khuôn mặt.
3. **CẤM VIẾT LẠI VÀO SHOT LẺ (SF):** Khi tạo các khung hình SF lẻ (S1, S2...), KHÔNG được nhét lại từ khóa ánh sáng vào prompt. SF lẻ sẽ tự động kế thừa (inherit) ánh sáng từ Thẻ Địa Điểm. Tả lại sẽ làm đè (override) Look gốc.
## 1. Nguyên lý Đánh sáng Điện ảnh (Cinematic Lighting)
CẤM sử dụng "Ánh sáng trần/phẳng" (Flat lighting) làm triệt tiêu hình khối. Một bức ảnh điện ảnh chuẩn luôn cần sự kết hợp của 3 nguồn sáng cơ bản:
- **Key Light (Sáng chính):** Nguồn sáng mạnh nhất, quyết định hình khối của chủ thể. Đặt lệch góc để tạo bóng đổ (ví dụ: *light coming from the large window on the left*).
- **Fill Light (Sáng phụ):** Ánh sáng làm mềm phần bóng râm (shadows) do Key Light tạo ra. Không bao giờ được mạnh bằng Key Light.
- **Rim Light / Backlight (Sáng ven):** Ánh sáng đánh từ phía sau chủ thể để tạo đường viền sáng quanh tóc/vai, giúp tách chủ thể ra khỏi phông nền (Đặc biệt quan trọng cho AI để tránh bị bẹp ảnh).

**Từ khóa khuyên dùng:** *Cinematic lighting, volumetric light (ánh sáng khối/God rays), soft shadows, dramatic lighting.*

## 2. Tỷ lệ Tương phản (Contrast Ratios)
Mỗi thể loại phim cần một độ tương phản khác nhau (Tone & Mood):
- **High-key Lighting:** Rất sáng, bóng đổ mờ nhạt, tương phản thấp. Tạo cảm giác an toàn, vui vẻ, tươi sáng.
  - *Thể loại:* Hài (Comedy), Tình cảm (Romance), TV Commercial.
  - *Từ khóa:* *High-key lighting, bright and airy, soft diffused light, low contrast.*
- **Low-key Lighting (Chiaroscuro):** Rất tối, bóng đổ đậm đặc, tương phản cực gắt. Tạo cảm giác kịch tính, nguy hiểm, bí ẩn.
  - *Thể loại:* Drama, Kinh dị (Horror), Phim rạp (Thriller/Noir).
  - *Từ khóa:* *Low-key lighting, chiaroscuro, harsh shadows, moody atmosphere, high contrast.*

## 3. Bảng màu Điện ảnh (Color Palettes & Grading)
Việc ép AI dùng một bảng màu cụ thể sẽ ngay lập tức biến bức ảnh thành cảnh phim Hollywood:
- **Teal & Orange (Xanh dương & Cam):** Bảng màu phổ biến nhất của bom tấn Hollywood. Da người (cam) nổi bật hoàn hảo trên nền tối (xanh dương).
  - *Từ khóa:* *Teal and orange cinematic color grading, block-buster look.*
- **Muted / Desaturated (Trầm / Nhạt màu):** Bảng màu bị rút bớt sắc độ rực rỡ, thiên về u ám, lạnh lẽo.
  - *Thể loại:* Hậu tận thế (Post-apocalyptic), Bi kịch.
  - *Từ khóa:* *Desaturated colors, muted color palette, bleak atmosphere.*
- **Neon / Cyberpunk:** Đánh sáng gắt bằng các tông màu nhân tạo rực rỡ (Hồng neon, Xanh lơ, Tím).
  - *Từ khóa:* *Neon noir, vibrant magenta and cyan lighting.*
- **Warm / Golden Hour (Giờ vàng):** Ánh sáng ấm áp, rực rỡ của hoàng hôn/bình minh.
  - *Từ khóa:* *Golden hour lighting, warm amber glow, nostalgic.*

## 4. Ứng dụng thực tế
### A. Dùng ở cấp độ Toàn Phim (Global)
Nếu một bộ phim cần duy trì xuyên suốt một màu sắc (VD: Cả phim đều mang màu u ám của Gotham), hãy ghi lệnh Color Grading (như *Low-key, Desaturated*) vào file `phong-cach-rieng.md`. Mọi prompt ảnh sau này sẽ bị ép phải tuân theo phong cách này.

### B. Dùng ở cấp độ Cảnh (Local)
Nếu chỉ cần đổi ánh sáng cho một căn phòng vào ban đêm: Trong thẻ Địa điểm biến thể (Thẻ Bếp đêm), chỉ cần đính kèm ảnh Bếp ngày vào `refs.bg` và viết prompt:
> *"Giữ nguyên 100% không gian kiến trúc của ảnh tham chiếu. Chỉ thay đổi ánh sáng: Low-key lighting, cinematic moonlight streaming through the window, moody blue color grading, deep shadows."*

## 5. Danh sách CẤM (Anti-Cinematic Words)
Tuyệt đối KHÔNG dùng các cụm từ sau khi tả bối cảnh hoặc ánh sáng (trừ phi đang cố tình làm phim tài liệu cấp thấp/kinh dị):
- ❌ *Ánh sáng đều (Even lighting)*
- ❌ *Ánh sáng phẳng (Flat lighting)*
- ❌ *Trắng lạnh không bóng đổ (Cold white light without shadows)*
- ❌ Dùng số năm để tả độ cũ (VD: *nhà 30 năm tuổi* -> ⚠️ Dễ bị AI bóp méo thành hoang tàn rùng rợn. Khuyên dùng: *Nostalgic, retro, well-maintained*).
