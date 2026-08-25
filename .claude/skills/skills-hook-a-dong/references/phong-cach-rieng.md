# Phong Cách A Đồng (A Dong Style Reference Guide)

> **LƯU Ý QUAN TRỌNG**: File này đóng vai trò bổ trợ DNA phong cách A Đồng cho bộ skill `skills-hook-a-dong`. Bộ skill này vẫn tuân thủ 100% **Quy trình 5 bước cốt lõi**, **Kiến trúc Master SF**, **Schema `sf-board.json`** và **Trình kiểm luật tự động (`kiem-luat.py`)**.

---

## I. NHỮNG ĐẶC TRƯNG CỐT LÕI CỦA PHONG CÁCH A ĐỒNG

### 1. Khung Tem Thể Loại & Chất Ảnh Tiêu Chuẩn (A Dong Aesthetic Header)
Trích nguyên văn tiêu chuẩn chất ảnh mở đầu prompt ảnh của A Đồng:
```text
Cinematic 16:9 ultra-photorealistic airline-humiliation keyframe, premium American emotional-drama photography, bright neutral white balance, cinematic HDR, sharp realistic faces, realistic luxury materials, realistic skin and fabric texture, no blur, no film grain, no CGI, no text overlay, no logo, no watermark.
```
*Lưu ý về Grain/Blur*: A Đồng dùng **`No film grain. No blur.`** ở 100% prompt (ảnh luôn razor-sharp).

### 2. Bộ Khối LOCK Cố Định (7 LOCK Blocks Nguyên Văn)
Khi cần khoá cố định bối cảnh hoặc nhân vật cho toàn bộ phim:
- **CHARACTER LOCK**: `EXACTLY the same woman as Reference Image 1. Never change her face, age, skin tone, hairstyle or body proportions. Only her wardrobe changes.`
- **PHYSICAL ACTION LOCK (Khống chế hành vi bạo lực)**:
  ```text
  Sandra may block Whitney's path.
  Sandra may snatch the boarding pass.
  Sandra may tear the boarding pass.
  Sandra never punches Whitney.
  Sandra never pushes Whitney.
  Sandra never grabs Whitney's body.
  Whitney never physically retaliates.
  Ticket-snatching and ticket-tearing should happen in silent action beats whenever possible.
  ```
- **BACKGROUND / LOCATION LOCK (Thương hiệu hư cấu & Cụ thể bối cảnh)**:
  ```text
  Use the complete FIXED CHARACTER REFERENCE GUIDE and WHITFIELD MEMORIAL HOSPITAL LOCATION LOCK.
  ```
  *(Các thương hiệu hư cấu chuẩn A Đồng: SkyVault Airlines · Meridian Club · Whitfield Memorial · Common Grounds · Stonebriar Landing)*.
- **GLOBAL VISUAL LOCK**:
  ```text
  Bright neutral white balance. Premium cinematic HDR.
  Sharp realistic faces. Natural skin texture.
  No exaggerated orange color cast.
  No blur. No film grain. No CGI look. No plastic skin.
  ```
- **GLOBAL KLING CONTINUITY LOCK**:
  ```text
  no duplicated people · no disappearing equipment · no sudden location changes · Background staff move naturally and subtly. Avoid frantic unnatural arm movements.
  ```
- **AUDIO LOCK (Khép prompt video 3 dòng)**:
  ```text
  No generated narration.
  No soundtrack music.
  No unrelated human dialogue.
  ```

---

## II. QUY TẮC AN TOÀN & BẢO VỆ PHẨM GIÁ NHÂN VẬT

### 1. Phủ Định Hành Vi Để Giữ Phẩm Giá (Dignity Enforcement)
Nhân vật chính bị hạ nhục tuyệt đối không hoảng loạn hay sụp đổ:
- `She does not cry, speak or collapse.`
- `He does not resist. He does not lower his eyes.`
- `Whitney never physically retaliates.`
- `Whitney maintains executive composure. Her gaze is steady, cold and unreadable.`

### 2. Khoá Người Ngoài Cuộc (Nobody Intervenes)
Thiết yếu cho thể loại Hook "kẻ bị coi thường lật ngược thế cờ":
- `Nobody intervenes.` (Đảm bảo màn hạ nhục diễn ra trọn vẹn mà không có ai nhảy vào can thiệp trước thời điểm twist).

### 3. Luật Vệ Sinh Nội Dung (Content Safety Rules)
```text
No graphic wounds. Patients may have bandages, oxygen masks, cervical collars and blankets, but no blood or exposed injuries.
All patients shown after the crisis are alive and visibly breathing.
No graphic injuries, no visible blood, no corpses and no disturbing medical gore.
```

---

## III. CHI TIẾT KỸ THUẬT & TỪ VỰNG A ĐỒNG

### 1. Số Đếm Hiện Vật Chính Xác (Exact Counts)
A Đồng luôn số hóa mọi vật thể trong kịch bản để AI render chính xác:
- `Approximately twenty hospital beds are already filled`
- `a dense, carefully organized line of fifty occupied gurneys`
- `EXACTLY two torn main ticket halves`

### 2. Cá Thể Hoá Phản Ứng Nhân Chứng (Individualized Witness Actions)
Không tả "đám đông phản ứng", tả từng người trong nhóm khoá:
- `Passenger one pauses with luggage halfway toward an overhead bin.`
- `Passenger two sits by the aisle with lips pressed tightly.`
- `Passenger three has turned fully toward Whitney.`
- `Passenger four lowers something from her hand.`
- `Passenger five watches silently from farther back.`

### 3. Định Vị Khung Hình & Chuyển Cảnh
- **Định vị**: Dùng `screen-left` / `screen-right` (vd: `Whitney stands screen-left... Sandra stands screen-right.`)
- **Dẫn hướng bằng bàn tay**: `one trembling nurse slowly raises a finger and points toward an unseen corner outside the camera frame.`
- **Hồi tưởng (Flashback)**: `Match cut from Hope's exhausted eyes at dawn to the same eyes twelve hours earlier. Elegant visual rewind transition. No spinning clocks, no fantasy particles and no readable time graphics.`

### 4. Bảng Danh Từ Đặt Tên Nhịp (Beat Naming Vocabulary)
Mỗi nhịp clip gắn đúng danh từ chức năng:
`hero reveal` · `mystery-reveal sequence` · `hidden-authority teaser` · `silent-power keyframe` · `suspenseful flashback transition` · `suspense montage` · `heroic transition` · `executive-decision keyframe` · `closing hook-backstory image`.

---

## IV. 3 ĐIỂM CỐ Ý KHÔNG THEO A ĐỒNG (DIVERGENCES WITH INTENTION)

Hệ thống prompt của bộ skill này **CỐ Ý KHÔNG THEO** 3 điểm sau đây của A Đồng để bảo vệ tính nhất quán của hệ thống Master SF & `sf-board.json`:

1. **Không tả lại ánh sáng ở SF lẻ**:
   - *Lý do*: SF lẻ đã đính `refs.bg` trỏ về Master SF (ảnh đính kèm đã khoá Look & Ánh sáng). Viết lại ánh sáng ở SF lẻ sẽ làm nhiễu AI sinh ảnh và đè mất Look gốc.
2. **Không thêm câu chốt ngụ ý văn học ở cuối prompt ảnh** (`The emotional center...` / `The image must communicate...`):
   - *Lý do*: Bộ skill tuân thủ nghiêm ngặt luật **CẤM ngụ ý văn học / CẤM ẩn dụ**. Chỉ tả trạng thái thể chất/vật lý có thể chụp được, tránh AI suy diễn ảo giác.
3. **Không lặp lại bộ 7 khối LOCK bằng chữ ở mọi SF lẻ**:
   - *Lý do*: A Đồng dùng máy sinh ảnh/video không đính được ảnh tham chiếu nên phải lặp 100% LOCK block ở từng prompt. Bộ skill này tận dụng cơ chế đính ảnh phân tầng `refs.chars` và `refs.bg` của `sf-board.json` nên chỉ nạp LOCK block ở cấp Master / Thẻ REF.
