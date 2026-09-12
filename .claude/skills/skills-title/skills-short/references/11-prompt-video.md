# 11 — Prompt Video (Grok): biến ảnh tĩnh thành clip

> **File này trả lời:** viết prompt video cho một clip thế nào — cấu trúc shot con, camera, lip sync, kết clip.
> **Mở khi:** sinh prompt video cho bất kỳ shot nào.
> **Không chứa:** prompt video của nhịp không thoại (→ `10-nhip-lang.md`) ·
>   prompt nhạc (→ `12-nhac-suno.md`) · thời lượng & số từ thoại (→ `7-bang-shot.md`) ·
>   triết lý chuyển góc (→ `0-tu-duy-dien-anh.md`)

## 1. Cấu trúc video multi-shot theo `dur`
- **Mặc định chuẩn 10 giây (`dur: 10`) — duy nhất cho Short:** mọi video mặc định sinh ở mốc 10s, gồm 2 shot con nối bằng 1 cú HARD CUT dứt khoát (`10-SECOND VIDEO. EXACTLY TWO SHOTS. EXACTLY ONE HARD CUT.`).
- **Prompt không nén:** prompt video mặc định viết bằng tiếng Anh, đầy đủ, không nén. Bỏ tư duy rút gọn để ép vừa ký tự cũ. Trần ký tự của prompt video phim/short: 2.000 – 2.800 ký tự.
- **Khung dọc 9:16:** mọi prompt video bắt buộc mở đầu bằng dòng `VERTICAL 9:16 VIDEO...` ngay trước dòng `<n>-SECOND VIDEO...`, vì SF neo là ảnh dọc 9:16 (`2-du-lieu-sf-board.md` §8) — thiếu dòng này Grok hay tự cắt về khung ngang.
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

### 3.1 Form Video 10 giây (2 Shot, 1 Hard Cut)
```text
Use the uploaded reference image as the visual anchor for character appearance, wardrobe, layout, lighting, props, and spatial relationships.

VERTICAL 9:16 VIDEO. Keep the full vertical frame of the reference image. Do not crop, letterbox, pillarbox, or reframe to widescreen.

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

### 3.2 Form Video 15 giây (3 Shot, 2 Hard Cut) (KHÔNG DÙNG CHO SHORT)
```text
Use the uploaded reference image as the visual anchor for character appearance, wardrobe, interior layout, lighting, props, and spatial relationships.

VERTICAL 9:16 VIDEO. Keep the full vertical frame of the reference image. Do not crop, letterbox, pillarbox, or reframe to widescreen.

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

### 3.3 Biến thể "Không lồng giọng narrator" — chừa khoảng lặng cho hậu kỳ ghép giọng đọc
Dùng khi user muốn **văn kể (narration) không được AI video đọc lên**, mà chừa sẵn khoảng lặng âm thanh đúng độ dài để hậu kỳ tự ghép giọng đọc thật vào sau. Đây không phải mặc định — chỉ áp dụng khi user yêu cầu; mặc định vẫn theo form §3.1 (đọc thẳng lời thoại, không cần khối `TIMING`).

**Khác biệt duy nhất so với form §3.1**: chèn thêm khối `TIMING` ngay sau `SCENE`, mọi tiêu đề `SHOT N` ghi kèm mốc giây `(0:00–0:0X)`, và khối `AUDIO`/`LIP SYNC` phải nói rõ không có narrator được sinh ra.

```text
SCENE:
<Mô tả mục đích và tâm lý tự nhiên>.

TIMING (không sinh giọng narrator — chừa khoảng lặng sạch để hậu kỳ ghép giọng đọc):
0:00–0:0X <Shot nào lấp khoảng này, có thoại hay im lặng dành cho câu văn kể nào — trích nguyên văn câu đó>.
0:0X–0:10 <tương tự cho phần còn lại>.

DIALOGUE ORDER:
<TÊN A> (hoặc "None. No character speaks in this clip." nếu toàn bộ clip là văn kể)

SHOT 1 (0:00–0:0X) — <cỡ cảnh> — <camera>
...(nếu là khoảng lặng): Hold the full <X> seconds silent.
...(nếu có thoại): <TÊN A> — <emotion>: "<thoại nguyên văn>"

HARD CUT.

SHOT 2 (0:0X–0:10) — <cỡ cảnh> — <camera>
...

AUDIO:
<Đoạn có thoại>: dialogue clear American English. <Đoạn im lặng>: no dialogue, ambient only — leave clean for narrator dub. No narrator generated.

EDITING:
CUT 1: At 0:0X, <mô tả đúng khoảnh khắc chuyển, khớp nội dung Shot 2 hiện tại — xem §5.1.2>.
```

- **Tính mốc giây bằng đúng tốc độ 3.0 từ/giây** (cùng chuẩn với `7-bang-shot.md` §5.2), rồi chia lại ranh giới Shot 1/Shot 2 cho khớp — không mặc định chia đôi 5s/5s nếu số từ hai vế lệch nhau nhiều.
- Câu văn kể trích trong `TIMING` phải đúng nguyên văn và đúng thứ tự như kịch bản gốc (→ `1-kich-ban.md` §2.2).
- Nếu một clip có CẢ thoại lẫn khoảng lặng dành cho văn kể xen kẽ trong cùng 1 shot con, ghi rõ mốc giây con bên trong phần mô tả diễn biến của shot đó (VD: `0:00–0:02: im lặng... 0:02–0:06: <TÊN A> nói...`).
- Field `text` của shot (→ `2-du-lieu-sf-board.md` §2.5) vẫn ghi đủ cả câu thoại lẫn câu văn kể theo đúng thứ tự gốc, bất kể văn kể có được AI đọc lên hay không.

## 4. Các khối bắt buộc

### 4.1 Khối `CHARACTERS` tối giản
- Chỉ dùng để phân biệt người này với người kia trong khung hình. Bỏ hẳn loại áo/kiểu dáng, chỉ ghi màu áo (vd: `wearing an ash-gray T-shirt`, `wearing soft blush-pink pajamas`).
- Nhân vật mờ ở tiền cảnh / out focus: ghi rõ `, blurred in foreground, completely still like a statue`.
- Cấm tả trang phục vùng dưới (quần, giày, vớ), thắt lưng, phụ kiện (đồng hồ, nhẫn, túi).
- *(Việc mỗi nhân vật cùng scene có một màu áo khác nhau đã được chốt từ thẻ REF — `3-ref-nhan-vat.md` §4.)*

**Clip sinh từ Solo Frame (SF một nhân vật — `7-bang-shot.md` §3.3):** khối `CHARACTERS` chỉ khai đúng một người, và bắt buộc thêm câu chặn ngay dưới nó:

```text
Only ONE character appears in this entire video.
Do not add, invent, or reveal any second person — not a face, not a shoulder, not a hand, not a reflection, not a silhouette.
No one enters or leaves the frame.
```

Không có câu này, AI đọc một clip nghe như đối thoại rồi tự dựng thêm người thứ hai ở mép khung. Người nền vẫn được giữ bình thường — câu chặn nói về nhân vật, không nói về quần chúng (`9-quan-chung-nen.md`).

### 4.2 Khóa Lip Sync & phép đối thoại
- Bắt buộc có câu: `Only the currently speaking character moves their lips. No overlapping dialogue.`
- Gắn trực tiếp câu listening cho từng nhân vật: `When A speaks, B listens silently with their mouth closed.`
- Với nhịp không thoại: `No character speaks. No character moves their lips as if talking.`
- **Solo Frame**: bỏ hẳn các câu `When A speaks, B listens...`, chỉ giữ `Only the currently speaking character moves their lips. No overlapping dialogue.` — khai tên người thứ hai ở đây là mời AI vẽ họ ra.

### 4.3 Khoảng lặng diễn xuất cảm xúc (Emotional Dramatic Pauses)
- Con số 3.0 từ/giây chỉ là trần tối đa chống nhồi thoại. Trần cứng theo `7-bang-shot.md` §5.2 (28 từ cho clip 10s).
- Với các phân cảnh lắng đọng, uất ức, xúc động hoặc kìm nén, số từ thoại có thể ít nhiều tuỳ trường hợp. Tốc độ thoại hoàn toàn linh hoạt tùy tình huống diễn biến trong video.
- Viết rõ khoảng lặng cảm xúc trong từng shot con hoặc giữa các lượt thoại, ví dụ:
  `Brief dramatic pause. <TÊN A> hesitates, eyes glinting with suppressed emotion, before speaking in a low voice.`
  hoặc
  `<TÊN B> lingers in heavy silence, taking a slow breath before answering.`
- Trong khối `LIP SYNC:` luôn đảm bảo: `During silent pauses, mouths remain closed with lips still.`

### 4.4 Cấm tả "mắt đỏ" khi nhân vật khóc
Không viết *"eyes red"*, *"red-rimmed eyes"* trong bất kỳ khối nào (SCENE, PERFORMANCE, mô tả shot con...) — AI đọc "red" đứng cạnh "eyes" thành hiệu ứng mắt phát sáng đỏ kèm vệt máu chảy gò má, không thành mắt người khóc (lỗi có thật đã xảy ra). Dùng *"eyes brimming with tears"*, *"tear-swollen eyes"* và chèn câu chặn trong khối `PERFORMANCE`: *"Natural human eyes only: no glowing eyes, no colored light on the face, no streaks or marks down the cheeks. Tears and wet skin only."* Song song, prompt ảnh SF neo của clip đó cũng phải mang guard tương ứng (`8-prompt-sf.md` §6).

### 4.5 Tầng diễn xuất — viết HÀNH VI, không viết tính từ

Áp cho mọi clip, nhưng **bắt buộc rà kỹ nhất ở clip toàn văn kể** (biến thể §3.3, không có lượt
thoại nào): nhân vật không có gì để làm nên rất dễ ra khung tượng sáp — đơ, chết mặt.

**Nguyên tắc gốc**: AI video không diễn được tính từ. `cold`, `contemptuous`, `unhurried`,
`satisfied`, `composed`, `đắc thắng lạnh lùng` chỉ cho ra một khuôn mặt nghiêm nghiêm trung tính.
Mỗi tính từ cảm xúc phải quy đổi thành **một hành vi cơ thể quan sát được, quay được**.

#### (a) Phản diện — cái ác phải được KHOE cho người trong phòng xem
*(Nguyên lý vì sao: `0-tu-duy-dien-anh.md` §VII.1.)* Mỗi clip có phản diện **RÕ NÉT trong khung**
phải mang **ít nhất một** hành vi thuộc các nhóm sau. Clip mà phản diện chỉ là vai/gáy mờ tiền cảnh
thì miễn — gánh nặng cảm xúc lúc đó dồn hết sang mục (b).
- **Diễn cho khán giả tại chỗ, không diễn cho nạn nhân** — `glances at her guests to check they are
  watching` · `turns her head a few degrees toward her guests and back, sharing it with them` ·
  `throws the last of the line half toward her friends, not at the victim`.
- **Xử lý nạn nhân như đồ vật** — `tugs the tag to seat it, the way you straighten a price ticket` ·
  `turns her chin a few degrees toward the light the way a buyer turns a head` · `wipes her
  fingertips on her own gown afterwards` · `her eyes go over the uniform first, the face second`.
- **Lệch pha giọng và nội dung** — nói câu tàn bạo bằng giọng **nhẹ, dễ chịu, kiểu bà chủ tiệc**:
  `light, almost pleasant, as if adjusting a seating plan` · `warm, generous, as if handing over a
  gift`. Lệch pha gây phẫn nộ mạnh hơn gào; chỉ cho gào khi kịch bản ghi rõ có tiếng quát.
- Cú đắc nhất cho khung cuối phân đoạn: cho phản diện **thôi không nhìn nạn nhân nữa**, quay sang
  chia sẻ chiến thắng với đám bạn.

#### (b) Chính diện kìm nén — phải THẤY ĐƯỢC CÁI GIÁ, không phải mặt trơ
⛔ **Cấm gán cho chính diện** các cụm: `expression does not change`, `gives away nothing`,
`perfectly still`, `absolutely still`, `mặt tĩnh hoàn toàn`, `không một nét cảm xúc`. Lặp mấy cụm
này qua vài clip chính là ra lệnh cho AI làm tượng sáp.

Áp cho mỗi clip có chính diện **RÕ NÉT trong khung** (clip mà họ chỉ là vai/gáy mờ tiền cảnh thì miễn).
Thay bằng dấu hiệu thể chất của việc **đang phải giữ** — mỗi clip chọn hai đến ba cái:
hàm siết thấy cơ gồ ở khớp · cánh mũi phập phồng vì nén hơi · một cái nuốt khan · mạch đập bên cổ ·
mi mắt nhắm đúng một nhịp rồi mở lại · nắm tay lại rồi **CHỦ ĐỘNG mở ra** · môi mím một nhịp · mắt
quét một lượt vật/con số rồi trả về mặt đối phương · hít vào bằng mũi rồi giữ hơi.

⛔ **Mỗi cử chỉ dùng TỐI ĐA MỘT LẦN trong cả Hook — đếm cả prompt ảnh SF, không chỉ prompt video.**
Không đủ khi chỉ tránh lặp ở hai clip liền nhau: rải cùng một cử chỉ ở vài clip cách quãng thì người
xem vẫn đọc ra ngay là "đang diễn", và cử chỉ đó thôi làm điểm nhấn. Thủ phạm số một là **nắm tay
siết bên hông** — nó là cử chỉ dễ nghĩ ra nhất nên hay bị rải khắp Master SF, SF cận và hai ba clip
cùng lúc. Chốt trước nó nằm ở ĐÚNG một chỗ (thường là khung cuối, nơi có thể cho các ngón chủ động
mở ra thành một beat thật), rồi mọi SF còn lại ghi tay buông tự nhiên kèm câu chặn *"các ngón hơi
cong theo dáng nghỉ, không nắm chặt"*.

⛔ **Chọn hành vi theo DANH TÍNH nhân vật trước, mới lấy từ danh sách trên.** Danh sách này là kho
chung, không phải mặc định. Hỏi trước: *nhân vật này làm nghề gì / giỏi cái gì, và người như thế
phản xạ ra sao ở đúng khoảnh khắc này?* Phản xạ nghề nghiệp vừa tự nhiên hơn vừa cài sẵn thông tin
cho cú lật phía sau. VD kỳ thủ bị giật mất quân cờ: **mắt rơi xuống đúng ô vừa trống** (anh ta đang
tính lại thế) — đắt hơn hẳn nắm đấm, vì nó hé lộ anh ta là ai. Rồi để một từ trong câu thoại kéo
mắt anh ta ngẩng lên: *"his eyes come back up on the word 'mother'"*.

Chốt ý đồ ở `PERFORMANCE`, ví dụ: *"Restraint, not blankness: the audience must see how much it
costs her to look calm. The face must never go slack or empty."*

> **Ngoại lệ hợp lệ**: cụm `blurred in foreground, completely still like a statue` vẫn đúng và vẫn
> bắt buộc — nó dành cho vai/gáy MỜ ở tiền cảnh (§4.1), không phải cho mặt chủ thể đang nét.

#### (c) Đặt hành vi ở đâu, lấy chỗ ở đâu
- **Hành vi nằm ở khối `SHOT`** (nơi model đọc diễn biến). Khối `PERFORMANCE` chỉ **2–3 câu** chốt ý
  đồ, tuyệt đối không chép lại hành vi đã viết ở `SHOT` — trần 2.800 ký tự rất chật.
- Thiếu chỗ thì **nén boilerplate trước** (`AUDIO`, `LIP SYNC`, `EDITING`, `CAMERA SUMMARY`, câu dẫn
  của khối `TIMING`). Tuyệt đối không cắt hành vi để lấy chỗ cho câu mô tả máy quay.
- Prompt ảnh SF neo của clip phải mang đúng biểu cảm ấy, nếu không khung đầu đã chết mặt sẵn và cả
  clip chết theo: `8-prompt-sf.md` §5.

## 5. Khối kết clip — `< 7%` số shot của phim

**Cảnh báo lạm dụng**: chỉ `< 7%` số shot của phim thật sự cần khối kết clip.

### 5.1 Định luật Bảo toàn Image-to-Video & chọn lại SF (tối quan trọng)
Video sinh ra từ một bức ảnh tĩnh duy nhất (được trỏ bởi ô `"sf"` trong mảng `shots`) — **CẢ HAI shot con** (trước và sau HARD CUT) đều phải bắt nguồn từ đúng một ảnh đó, không phải chỉ Shot 1.
- **Mỗi clip một ảnh SF riêng, không dùng lại ảnh của clip khác** (`7-bang-shot.md` §1.1). Khi mạch thoại đảo góc quay lại cùng nhân vật, vẫn sinh SF mới với góc phủ khác — ô `"sf"` luôn trỏ về một ID chưa clip nào dùng.
- **Cách viết prompt**: video shot này đọc đúng bức ảnh SF được trỏ tới làm Start Frame gốc. Chỉ viết prompt diễn biến/thoại/hành động dựa trên vốn liếng bối cảnh, vị trí và nhân vật đã có sẵn ở SF đó, không bịa ra thứ mà SF đó không có.
- **Tuyệt đối cấm**: lấy trạng thái của shot kế tiếp kéo về bắt shot hiện tại phải vẽ thêm trong khi SF được trỏ tới không có (VD: bắt "A bước vào" trong khi SF hiện tại không hề có hình bóng A trong khung).

#### 5.1.1 Tự kiểm Shot 2 trước khi viết — 3 lỗi hay gặp nhất
Trước khi viết Shot 2, đọc lại đúng dòng `goc`/`pose` của SF neo và tự hỏi: *"Điều Shot 2 sắp mô tả có ĐÃ RÕ trong ảnh này không?"* Ba lỗi cụ thể đã xảy ra trong thực tế, phải rà đúng 3 câu hỏi sau:
1. **Đạo cụ mọc từ hư không**: Shot 2 cho nhân vật "rút/lấy ra" một món đồ (điện thoại, giấy tờ...) mà SF không hề vẽ nó ở đâu trên người họ (túi, tay). *Sửa đúng*: nếu vật đó phải xuất hiện đúng lúc này, sửa lại chính ảnh SF neo cho vật đã cầm sẵn (ở tư thế chưa dùng tới), rồi Shot 2 chỉ "nâng/xoay" vật đã có sẵn.
2. **Mặt rõ mọc từ vùng mờ/quay lưng**: SF là OTS hoặc góc chỉ thấy vai/gáy mờ của một nhân vật (không thấy mặt) — Shot 2 tuyệt đối không được "cắt sang khuôn mặt rõ nét" của đúng người đó. Nếu người đó cần thoại, để họ nói với mặt vẫn quay đi (giọng phát ra, không cần thấy miệng mấp máy) — không đổi hẳn sang góc mặt rõ chỉ vì họ có lời thoại ở Shot 2.
3. **Đám đông/hậu cảnh mờ hoá thành chủ thể rõ nét**: SF tả quần chúng/hậu cảnh là "ngoài nét" — Shot 2 tuyệt đối không được biến họ thành chủ thể rõ nét, có cảm xúc cụ thể (VD: "mắt mở to, nín thở"). Muốn nhấn cảm xúc đó, giữ nguyên độ mờ và để phần lời (narration/VO) gánh thông tin thay vì hình ảnh.
4. **Đạo cụ thuộc môi trường (không phải trên người) mọc từ hư không**: nhân vật phải "đi lấy" một đạo cụ đặt RIÊNG trong bối cảnh (vd: xô nước ở ngưỡng cửa, chìa khoá trên bàn) mà SF neo hiện tại không hề vẽ nó ở đâu trong khung. AI không thấy đạo cụ trong ảnh gốc sẽ tự bịa ra một phiên bản khác (sai hình dạng, sai chất liệu, sai màu) khi sinh video — lỗi có thật đã xảy ra với một chiếc mop bucket. *Sửa đúng — tách SF làm hai bước*:
   - (a) thêm đạo cụ đó vào TẤT CẢ SF trước đó trong cùng cụm không gian (đặt sẵn ở hậu cảnh, "chưa ai chạm tới") để giữ tính nhất quán môi trường xuyên suốt cụm.
   - (b) tạo một SF mới ngay trước shot hành động lấy đồ, trong đó đạo cụ được đưa lên rõ ràng trong khung (tiền cảnh hoặc cận hậu cảnh), nhân vật CHƯA chạm vào nó — đây là "trạng thái chờ" đúng nghĩa.
   - (c) trỏ `"sf"` của shot hành động sang SF mới này, không dùng lại SF cũ (không có đạo cụ) hay SF sau (đã cầm đạo cụ).

   **Khi tách SF làm đôi một hành động liên tục → chia lại câu văn kể (`text`) cho khớp hình**: nếu câu văn kể gốc mô tả 2 nửa hành động liên tiếp (VD: "quay vào cửa" + "quay ra với cái xô") mà nay rơi vào 2 SF/clip khác nhau, PHẢI chia câu văn kể theo đúng ranh giới hình ảnh của từng clip: nửa nào tả đúng cái đang THẤY trên màn hình của clip đó thì thuộc `text` (và khối `TIMING`) của clip đó — không dồn cả câu vào một clip rồi để clip kia trống, và không cắt sai chỗ khiến nửa câu narrate một hành động mà clip đó chưa/không còn hiển thị. Đồng bộ lại khối `TIMING` của CẢ HAI prompt video sau khi chia.

#### 5.1.2 Đồng bộ dòng `CUT 1` mỗi khi sửa lại Shot 2
Dòng `CUT 1:` trong khối `EDITING` mô tả đúng khoảnh khắc chuyển giữa Shot 1 → Shot 2. **Mỗi lần sửa nội dung Shot 2** (đổi hành động, đổi góc, đổi SF neo), bắt buộc đọc lại và sửa luôn dòng `CUT 1` cho khớp — dòng này rất dễ bị bỏ sót, sinh ra một câu mô tả hành động không còn tồn tại trong Shot 2 đã sửa.

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

**Đếm được:**
- [ ] Prompt video **trong khoảng 2.000 – 2.800 ký tự** (§1).
- [ ] Prompt mở đầu có dòng `VERTICAL 9:16 VIDEO...` đứng ngay trước dòng `<n>-SECOND VIDEO...` (§1).
- [ ] Mọi clip sinh từ Solo Frame có đủ khối chặn `Only ONE character appears...` và không khai tên nhân vật thứ hai ở bất kỳ khối nào (§4.1, §4.2).
- [ ] Khối kết clip dưới **7%** số shot của phim.
- [ ] Khối `PERFORMANCE` **2–3 câu**, không chép lại hành vi đã viết ở khối `SHOT` (§4.5c).

**Phải đọc mới thấy:**
- [ ] Không có khối nào thừa ngoài form chuẩn. Không tả lại tuổi/quần áo/nhân dạng.
- [ ] Không cảm xúc nào chỉ được tả bằng tính từ suông; mỗi cảm xúc có ít nhất một hành vi cơ thể quay được (§4.5).
- [ ] Chính diện KHÔNG bị gán `expression does not change` / `gives away nothing` / `mặt tĩnh hoàn toàn`; mọi clip có chính diện RÕ NÉT đều có 2–3 dấu hiệu kìm nén (§4.5b).
- [ ] **Không cử chỉ kìm nén nào dùng quá 1 lần trong cả Hook** — liệt kê ra từng cử chỉ đã dùng và đối chiếu qua CẢ prompt ảnh SF lẫn prompt video; riêng `nắm tay siết` đếm kỹ, các SF còn lại phải có câu chặn "không nắm chặt" (§4.5b).
- [ ] Hành vi kìm nén của chính diện đã chọn theo nghề nghiệp/danh tính nhân vật, không lấy mặc định từ danh sách (§4.5b).
- [ ] Phản diện chưa bị lộ: mọi clip có phản diện RÕ NÉT đều mang ít nhất một hành vi khoe cái ác cho người trong phòng (§4.5a).
- [ ] Khối kết clip đặt đúng chỗ, dư thời gian diễn.
- [ ] Người thoại luôn có mặt (ngoại trừ qua điện thoại/loa — `7-bang-shot.md` §5.4).
- [ ] Không có chuyển động camera Mức C.
- [ ] Mọi nhịp không thoại có vai trò rõ ràng, kèm đủ 2 prompt Suno (`12-nhac-suno.md`).
- [ ] Shot 2 không vẽ điều gì mà SF neo không có/không rõ — đã tự kiểm đủ 4 câu hỏi ở §5.1.1 (kể cả đạo cụ thuộc môi trường, không chỉ đạo cụ trên người).
- [ ] Dòng `CUT 1` khớp đúng nội dung Shot 2 hiện tại (đã đồng bộ lại sau lần sửa gần nhất — §5.1.2).
- [ ] Nếu dùng biến thể "không narrator" (§3.3): mọi clip đều có khối `TIMING`, mốc giây tính đúng từ số từ thực tế, và `shot.text` vẫn ghi đủ nguyên văn theo đúng thứ tự kịch bản.
- [ ] Nếu một hành động bị tách làm 2 SF/clip: câu văn kể đã chia đúng ranh giới hình ảnh của từng clip (§5.1.1 mục 4), không có nửa câu narrate một cảnh mà clip đó không hiển thị.
- [ ] Không viết "eyes red" / "red-rimmed eyes" ở bất kỳ đâu; nếu nhân vật khóc đã có guard clause đúng chuẩn (§4.4).
