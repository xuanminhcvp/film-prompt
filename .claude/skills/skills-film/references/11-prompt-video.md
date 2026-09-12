# 11 — Prompt Video (Grok): biến ảnh tĩnh thành clip

> **File này trả lời:** viết prompt video cho một clip thế nào — cấu trúc shot con, camera, lip sync, kết clip.
> **Mở khi:** sinh prompt video cho bất kỳ shot nào.
> **Không chứa:** prompt video của nhịp không thoại (→ `10-nhip-lang.md`) ·
>   prompt nhạc (→ `12-nhac-suno.md`) · thời lượng & số từ thoại (→ `7-bang-shot.md`) ·
>   triết lý chuyển góc (→ `0-tu-duy-dien-anh.md`)

## 1. Cấu trúc video multi-shot theo `dur`
- **Mặc định chuẩn 15 giây (`dur: 15`) — chủ yếu nhất: mọi video mặc định sinh ở mốc 15s, gồm 3 shot con nối bằng 2 cú HARD CUT** dứt khoát (`15-SECOND VIDEO. EXACTLY THREE SHOTS. EXACTLY TWO HARD CUTS.`).
- **Rất ít dùng 10 giây (`dur: 10`):** chỉ ở số ít nhịp đặc biệt cực kỳ ngắn (2 shot con, 1 hard cut: `10-SECOND VIDEO. EXACTLY TWO SHOTS. EXACTLY ONE HARD CUT.`).
- **Prompt không nén:** prompt video mặc định viết bằng tiếng Anh, đầy đủ, không nén. Bỏ tư duy rút gọn để ép vừa ký tự cũ. Trần ký tự của prompt video phim/hook: 2.600 – 3.400 ký tự.
- Mốc `dur` và trần số từ thoại do `7-bang-shot.md` §5 quyết định.

## 2. Thang an toàn Camera AI

**Định luật:** không cho camera khám phá không gian mới. Chỉ cho camera thay đổi cách nhìn vào những gì đã tồn tại trong start frame. (Vì sao: `0-tu-duy-dien-anh.md` §VI.)

| Mức | Chuyển động | Dùng thế nào |
|---|---|---|
| A — rất an toàn, khuyên dùng | `Static` · `Slow Push-in` / `Dolly in` (vua của AI, tiến lại gần lấy cảm xúc) · `Rack focus` | Dùng thoải mái |
| B — an toàn vừa | `Pan nhẹ` · `Tilt nhẹ` · `Subtle handheld` · `Lateral drift` (trôi ngang cực nhẹ) | Dùng có kiểm soát |
| C — rủi ro cao, tránh/cấm | `Dolly out` / `Pull back` · `Orbit lớn` · `Crane` (bay lên) · `Tracking dài ra ngoài frame` · mọi từ khoá `"revealing..."` | AI sẽ vẽ bậy bối cảnh hoặc biến dạng nhân vật |

**Khóa camera trong prompt:**
- Khóa mạnh ngay đầu prompt: `STATIC LOCKED-OFF CAMERA ON A FIXED TRIPOD`, hoặc setup camera movement mượt mà (`SLOW PUSH-IN` / `SUBTLE LATERAL DOLLY`). Cấm rung lắc gắt, cấm tự động pan/zoom ngoài setup.
- Tùy chọn camera movement phù hợp cho từng shot con để tạo cảm xúc và nhịp phim tự nhiên (VD: `SHOT 1 = wide shot, slow push-in`, `SHOT 2 = medium shot, subtle lateral dolly`, `SHOT 3 = medium close-up, very slow push-in`). Nếu shot cần camera đứng yên thì mới dùng `STATIC LOCKED-OFF CAMERA ON A FIXED TRIPOD`.
- Tự động lặp lại summary camera ở khối `CAMERA SUMMARY` cuối prompt.

## 3. Form Prompt Video Chuẩn

### 3.1 Form Video 15 giây (3 Shot, 2 Hard Cut)
```text
Use the uploaded reference image as the visual anchor for character appearance, wardrobe, interior layout, lighting, props, and spatial relationships.

15-SECOND VIDEO. EXACTLY THREE SHOTS. EXACTLY TWO HARD CUTS.

CHARACTERS:
<TÊN A> — <age>-year-old <ethnicity> <gender>, wearing <outfit color/desc>, <position/state>.
<TÊN B> — <age>-year-old <ethnicity> <gender>, wearing <outfit color/desc>, <position/state>.

Keep exactly these characters throughout the video.
Do not add, remove, replace, duplicate, or transform any character.

SCENE:
<Mô tả tâm lý, mục đích, cảm xúc và bối cảnh hành động chung>.

DIALOGUE ORDER:
<TÊN A> → <TÊN B> → <TÊN A>

SHOT 1 — WIDE TWO-SHOT — SLOW PUSH-IN
Camera: Very slow, smooth push-in toward both characters. Controlled movement. No handheld shake.
<Mô tả diễn biến Shot 1>.
<TÊN A> — <emotion>: "<thoại tiếng Anh nguyên văn>"

HARD CUT.

SHOT 2 — MEDIUM CLOSE-UP ON <TÊN B> — SUBTLE LATERAL DOLLY
Camera: Very slow lateral dolly movement. Keep face as primary focus.
<Mô tả diễn biến Shot 2>.
<TÊN B> — <emotion>: "<thoại tiếng Anh nguyên văn>"

HARD CUT.

SHOT 3 — MEDIUM CLOSE-UP ON <TÊN A> — VERY SLOW PUSH-IN
Camera: Very slow, subtle push-in toward face. Smooth and restrained.
<Mô tả diễn biến Shot 3>.
<TÊN A> — <emotion>: "<thoại tiếng Anh nguyên văn>"

PERFORMANCE:
<Chi tiết biểu cảm, giữ sự tự nhiên, tinh tế>.

LIP SYNC:
Only the currently speaking character moves their lips. No overlapping dialogue.
When <TÊN A> speaks, <TÊN B> listens silently with their mouth closed.
When <TÊN B> speaks, <TÊN A> listens silently with their mouth closed.
(Nếu shot KHÔNG THOẠI: "No character speaks. No character moves their lips as if talking.")

AUDIO:
Character dialogue ONLY.
Clear natural American English voices.
No background ambience.
No music.
No narrator.
No sound effects.
No subtitles.
No captions.
No on-screen text.

EDITING:
Exactly THREE shots total.
Exactly TWO hard cuts.

CUT 1: Immediately after <TÊN A> finishes: "<thoại 1>"
CUT 2: Immediately after <TÊN B> finishes: "<thoại 2>"

CAMERA SUMMARY:
SHOT 1 = wide two-shot, slow push-in.
SHOT 2 = medium close-up <TÊN B>, subtle lateral dolly.
SHOT 3 = medium close-up <TÊN A>, very slow push-in.
```

### 3.2 Form Video 10 giây (2 Shot, 1 Hard Cut)
```text
Use the uploaded reference image as the visual anchor for character appearance, wardrobe, layout, lighting, props, and spatial relationships.

10-SECOND VIDEO. EXACTLY TWO SHOTS. EXACTLY ONE HARD CUT.

CHARACTERS:
<TÊN A> — <age>-year-old <ethnicity> <gender>, wearing <outfit color/desc>, <position/state>.
<TÊN B> — <age>-year-old <ethnicity> <gender>, wearing <outfit color/desc>, <position/state>.

Keep exactly these characters throughout the video.
Do not add, remove, replace, duplicate, or transform any character.

SCENE:
<Mô tả mục đích và tâm lý tự nhiên>.

DIALOGUE ORDER:
<TÊN A> → <TÊN B>

SHOT 1 — MEDIUM TWO-SHOT — SLOW PUSH-IN
Camera: Very slow, smooth push-in. Controlled movement.
<Mô tả diễn biến Shot 1>.
<TÊN A> — <emotion>: "<thoại tiếng Anh nguyên văn>"

HARD CUT.

SHOT 2 — CLOSE-UP ON <TÊN B> — SUBTLE PAN / TILT
Camera: Very slow, restrained movement focusing on <TÊN B>.
<Mô tả diễn biến Shot 2>.
<TÊN B> — <emotion>: "<thoại tiếng Anh nguyên văn>"

PERFORMANCE:
<Mô tả nét tự nhiên>.

LIP SYNC:
Only the currently speaking character moves their lips. No overlapping dialogue.
When <TÊN A> speaks, <TÊN B> listens silently with their mouth closed.
When <TÊN B> speaks, <TÊN A> listens silently with their mouth closed.
(Nếu shot KHÔNG THOẠI: "No character speaks. No character moves their lips as if talking.")

AUDIO:
Character dialogue ONLY. Clear natural American English voices. No background ambience. No music. No narrator. No sound effects. No subtitles.

EDITING:
Exactly TWO shots total.
Exactly ONE hard cut.

CUT 1: Immediately after <TÊN A> finishes: "<thoại 1>"

CAMERA SUMMARY:
SHOT 1 = medium two-shot, slow push-in.
SHOT 2 = close-up <TÊN B>, subtle camera movement.
```

## 4. Các khối bắt buộc

### 4.1 Khối `CHARACTERS` tối giản
- Chỉ dùng để phân biệt người này với người kia trong khung hình. Bỏ hẳn loại áo/kiểu dáng, chỉ ghi màu áo (vd: `wearing an ash-gray T-shirt`, `wearing soft blush-pink pajamas`).
- Nhân vật mờ ở tiền cảnh / out focus: ghi rõ `, blurred in foreground, completely still like a statue`.
- Cấm tả trang phục vùng dưới (quần, giày, vớ), thắt lưng, phụ kiện (đồng hồ, nhẫn, túi).
- *(Việc mỗi nhân vật cùng scene có một màu áo khác nhau đã được chốt từ thẻ REF — `3-ref-nhan-vat.md` §4.)*

### 4.2 Khóa Lip Sync & phép đối thoại
- Bắt buộc có câu: `Only the currently speaking character moves their lips. No overlapping dialogue.`
- Gắn trực tiếp câu listening cho từng nhân vật: `When A speaks, B listens silently with their mouth closed.`
- Với nhịp không thoại: `No character speaks. No character moves their lips as if talking.`

### 4.3 Khoảng lặng diễn xuất cảm xúc (Emotional Dramatic Pauses)
- 3,0 từ/giây là hằng số quy đổi, không phải trần (`7-bang-shot.md` §5.2). Số từ đã chốt ở bảng shot quyết định độ dài phần có tiếng; prompt video KHÔNG được làm thay đổi con số đó.
- Phân cảnh lắng đọng, uất ức hay kìm nén thì kéo dãn bằng **khoảng lặng viết rõ trong từng shot con**, KHÔNG bằng cách cắt bớt số từ. Cắt bớt từ là tạo quãng chết ở cuối clip, không phải tạo nhịp diễn.
- Viết rõ khoảng lặng cảm xúc trong từng shot con hoặc giữa các lượt thoại, ví dụ:
  `Brief dramatic pause. <TÊN A> hesitates, eyes glinting with suppressed emotion, before speaking in a low voice.`
  hoặc
  `<TÊN B> lingers in heavy silence, taking a slow breath before answering.`
- Trong khối `LIP SYNC:` luôn đảm bảo: `During silent pauses, mouths remain closed with lips still.`

## 5. Khối kết clip — `< 7%` số shot của phim

**Cảnh báo lạm dụng**: chỉ `< 7%` số shot của phim thật sự cần khối kết clip.

### 5.1 Định luật Bảo toàn Image-to-Video & chọn lại SF (tối quan trọng)
Video sinh ra từ một bức ảnh tĩnh duy nhất (được trỏ bởi ô `"sf"` trong mảng `shots`).
- **Chọn lại SF khi lặp góc máy**: khi shot video đảo góc quay lại cùng nhân vật và tư thế cũ, ô `"sf"` trỏ trực tiếp về ID của SF đã sinh trước đó (VD: `"sf": "SF-S1-01"`). Bảng `sfs` tuyệt đối không sinh prompt SF trùng lặp.
- **Cách viết prompt khi chọn lại SF cũ**: video shot này đọc đúng bức ảnh SF được trỏ tới làm Start Frame gốc. Chỉ viết prompt diễn biến/thoại/hành động dựa trên vốn liếng bối cảnh, vị trí và nhân vật đã có sẵn ở SF đó, không bịa ra thứ mà SF đó không có.
- **Tuyệt đối cấm**: lấy trạng thái của shot kế tiếp kéo về bắt shot hiện tại phải vẽ thêm trong khi SF được trỏ tới không có (VD: bắt "A bước vào" trong khi SF hiện tại không hề có hình bóng A trong khung).

### 5.2 Các dạng hành động hợp lệ trong khối kết clip (White-list)
Cấm tự phát minh hành động. Chỉ được phép dùng các dạng sau:
- **Dạng 1 (Đổi tư thế)**: chủ thể trong ảnh tự thay đổi (từ ngồi thành đứng dậy, quỳ thành đứng).
- **Dạng 2 (Đạo cụ tại chỗ)**: đưa tay lấy/ném/thả một vật *đã hiện diện sẵn* trong khung ảnh.
- **Dạng 3 (Bước đi / Rời khỏi khung — Exit Frame)**: một chủ thể quay lưng đi hoặc bước ra khỏi màn hình.

> ⚠️ **Cần user chốt:** bản cũ của file này ghi tiêu đề *"Bốn (04) Dạng ... Chỉ được phép dùng 4 dạng sau"* nhưng chỉ liệt kê 3 dạng — dạng thứ 4 chưa từng được viết ra. Hiện white-list là 3 dạng. Nếu có dạng 4, bổ sung vào đây.

### 5.3 Khi nào tuyệt đối không viết kết clip (sẽ làm rác prompt)
- **Đổi góc máy**: không có nhu cầu nối raccord.
- **Quy mô quá tham lam**: hễ có từ 2 thao tác nối nhau trở lên (VD: lấy ván → bắc ván → đẩy xe), bắt buộc tạo thành khối nhịp không thoại riêng (`10-nhip-lang.md`). Kết clip chỉ dùng cho một thao tác đơn giản.
- **Phản bội lời thoại**: hành động trong kết clip mâu thuẫn với ý câu thoại (VD: thoại vừa nói "Tôi sẽ ngồi im đây" thì tuyệt đối không viết kết clip bảo họ đứng dậy bỏ đi).

## 6. Kiểm tra cuối bước
- [ ] Không có khối nào thừa ngoài form chuẩn. Không tả lại tuổi/quần áo/nhân dạng.
- [ ] Khối kết clip đặt đúng chỗ, dư thời gian diễn, và dưới 7% số shot.
- [ ] Người thoại luôn có mặt (ngoại trừ qua điện thoại/loa — `7-bang-shot.md` §5.4).
- [ ] Không có chuyển động camera Mức C.
- [ ] Mọi nhịp không thoại có vai trò rõ ràng, kèm đủ 2 prompt Suno (`12-nhac-suno.md`).
