# 7 — Bảng shot: scene này có shot nào, dài bao nhiêu, nối vào nhau ra sao

> **File này trả lời:** danh sách shot của scene, cỡ cảnh của từng shot, thoại dài bao nhiêu, và hai shot liền nhau nối được không.
> **Mở khi:** sau khi đã chốt cụm không gian, trước khi sinh bất kỳ prompt ảnh nào.
> **Không chứa:** cụm không gian & Master SF (→ `6-cum-va-master-sf.md`) ·
>   shot không thoại (→ `10-nhip-lang.md`) · cú pháp mã ID (→ `2-du-lieu-sf-board.md`) ·
>   nội dung prompt ảnh (→ `8-prompt-sf.md`) · quần chúng nền (→ `9-quan-chung-nen.md`)

> **Luật cốt lõi: Lập bảng shot trước, sinh prompt sau.** Bảng shot quyết định danh sách SF. Kiểm máy trên bảng cho sạch rồi mới sinh prompt ảnh.

## 1. Lập bảng shot chi tiết

Sau khi đã chốt danh sách các Cụm Không Gian và số lượng Master SF (`6-cum-va-master-sf.md`), mới bắt đầu điền các góc cận/trung cho từng câu thoại.

Cột của bảng: Mã shot | Thoại | Số từ | Giây | Góc | Có kết clip.

### 1.1 KHÔNG tái sử dụng ảnh SF — mỗi clip một ảnh riêng
⛔ **Hook không dùng lại ảnh SF, dù chỉ một lần.** Mỗi shot video có đúng một SF của riêng nó; số SF của scene luôn **bằng** số shot.

- Khi tạo shot mới, luôn gán một mã SF mới (`SF-S<scene>-<shot>`, VD: `SF-S1-07`). Không ô `sf` nào được trỏ về mã SF mà một shot khác đã dùng.
- **Mạch thoại quay lại thế trận cũ thì vẫn phải có ảnh mới** — không bê tấm cũ về. Tạo một góc phủ (coverage) khác cho cùng cụm không gian, khác bản cũ ở **ít nhất hai** trong ba trục:
  - **cỡ cảnh** (MCU → CU, tight two-shot → medium two-shot),
  - **trục máy** (nhích ≥30°, luôn giữ cùng một bên trục hành động để không vỡ 180°),
  - **hướng mắt / tư thế** của chủ thể (mắt đang nhìn xuống vật → mắt đã ngước lên khoá vào đối phương).
- Ảnh mới vẫn trỏ `refs.bg` về đúng Master SF của cụm mình — đổi góc phủ, không đổi cụm.
- *Cách ghi vào dữ liệu*: `2-du-lieu-sf-board.md` §5.2.

**Vì sao**: Start Frame là khung đầu clip. Hai clip dùng chung một tấm thì mắt người xem đọc ra là video bị lặp hình, đứng hình giả tạo — kể cả khi mỗi clip có Shot 2 crop/push-in khác nhau. Một cụm đối thoại phải có nhiều góc phủ (Master + OTS + cận + two-shot), chứ không phải một tấm dùng lại nhiều lần.

### 1.2 Định mức của scene / dự án
| Định mức | Ngưỡng |
|---|---|
| Mốc dur | **10s cho mọi shot** · riêng cặp clip tách từ chuỗi thoại dồn: **6s mỗi clip** (§5.2b) |
| Số shot | **ceil(tổng số từ hook ÷ 26)**, rồi **+1 cho mỗi lần tách** chuỗi thoại dồn (§5.2b) |
| Nhịp lặng (shot không thoại) | **0% (TUYỆT ĐỐI KHÔNG DÙNG NHỊP LẶNG)** |
| Tái sử dụng ảnh SF | **0% — cấm tuyệt đối, số SF = số shot** |
| Tỉ lệ cỡ cảnh | Cận/Trung (CU/MCU) ~40–50% · Góc đôi (Two-Shot/OTS) 20–30% · Toàn cảnh/Góc rộng 20–25% · Góc Đặc Tả (Insert/ECU) ~2% |
| Cụm có ≥3 main cast | ≥60% SF có đủ mặt cả nhóm · ≤20% SF chỉ có 2 người |

**Cách tự đếm** — làm trên BẢNG SHOT, trước khi sinh prompt:

1. Đếm tổng số shot của scene.
2. Đếm số mã `sf` khác nhau → phải BẰNG tổng số shot. Có hai shot trùng mã là sai.
3. Với mỗi cặp SF cùng cụm và cùng chủ thể, đối chiếu ba trục ở §1.1 → phải khác nhau ở ít nhất hai trục.
4. Đếm shot theo cỡ cảnh ghi ở cột GÓC → 4 nhóm tỉ lệ.
5. Với cụm có ≥3 main cast: đếm SF đủ mặt cả nhóm, và SF chỉ có 2 người.

⚠️ *Định mức đủ cast tính theo **cụm không gian**, không theo scene — một scene nhiều cụm thì đếm riêng từng cụm. Bản cũ từng ghi ngưỡng **50%**; đã thống nhất về **60%**.*

## 2. Quy tắc viết dòng `goc`

Dòng `goc` trả lời câu hỏi *"Khung này quay bằng góc gì, có ai, nét hay mờ?"*. Bắt buộc có cho mọi SF. Viết cùng lúc sinh SF ban đầu.

> **Lưu ý**: dòng `goc` sinh ra cùng SF, nhưng nó được dùng làm tiêu chuẩn khung hình cho Video Shot trên timeline.

1. **Nêu đích danh**, không đếm số lượng (VD: *"Everett trái + Warren phải, CẢ HAI RÕ MẶT"*).
2. **OTS phải nêu rõ vai của ai** làm tiền cảnh.
3. **Đúng tên nhân vật** như trong kịch bản.
4. **Khai cả người không phải chủ thể** (đang ngồi im/ngủ trong `pose.who` cũng phải khai, kể cả MAIN CAST đang diễn ở cụm khác mà lọt vào lớp sau của khung gối đầu, dù họ ở rất xa và out nét).
5. **Phải dùng đúng thuật ngữ cỡ cảnh/góc máy** (Wide, CU, Two-Shot, Low Angle...) được quy định ở §3. Không tả lồng bối cảnh, đạo cụ hay thông số kỹ thuật máy quay (tiêu cự 35mm, f/1.8) vào dòng này.
6. **Tuyệt đối cấm khai báo nhân vật nền** (nền, quần chúng, khách nền, người đi đường). Dòng này chỉ dành cho MAIN CAST.

## 3. Góc máy (Coverage)

- **Góc rộng**: dùng làm Master Shot mở cảnh, khép/chuyển cảnh, hoặc khung bao quát khi các nhân vật đối thoại nhóm/di chuyển trong bối cảnh khi thấy hợp lý.
- **Góc Đặc Tả (Insert/ECU)**: rất hạn chế (giữ mức ~2% tổng số shot toàn kịch bản). Dùng để đặc tả đồ vật quan trọng, chi tiết tay, mắt... nhằm chuyển nhịp hoặc che giấu raccord.
- **Góc cực đoan (High/Low/POV)**: rất hạn chế, chỉ dùng có chủ đích (nhấn mạnh tâm lý, quyền lực, hoặc nhập vai).
- Luật cỡ cảnh của Master SF: `6-cum-va-master-sf.md` §2.2.

### 3.1 Phân rã đối thoại 2 người (bộ góc tiêu chuẩn)
Ưu tiên dùng bộ thuật ngữ sau khi viết dòng `goc` và prompt SF:

**Khung cơ bản (Basic Frames)**
- **Master / Wide Two-Shot**: toàn cảnh 2 người và không gian xung quanh. Dùng để thiết lập không gian và làm Master SF.
- **Medium Two-Shot**: khung trung, thấy rõ cả hai khi trò chuyện.
- **Tight Two-Shot**: khung gần, nhấn mạnh cảm xúc của 2 người.
- **Two-Shot ngang**: hai người ngồi hoặc đứng cạnh nhau, cùng nhìn về trước.
- **Profile Two-Shot**: hai người đối diện nhau, quay ngang 90°.
- **3/4 Two-Shot**: máy đặt góc chéo để thấy mặt/phản ứng của cả hai.

**Góc hội thoại (Dialogue Coverage)**
- **Clean Two-Shot**: cả hai cùng rõ mặt trong một khung hội thoại.
- **OTS A → B / OTS B → A (Qua vai)**: qua vai người này để nhìn người kia đang nói/phản ứng.
- **Dirty Single**: cận 1 người, có một phần vai hoặc đầu của người kia lọt vào tiền cảnh.
- **Clean Single**: cận 1 người hoàn toàn, không vướng vai/đầu người kia.
- **Shared Reaction Two-Shot**: giữ cả hai trong khung để bắt phản ứng cùng lúc.

**Góc cao, thấp & góc nhìn**
- **Eye-Level**: máy ngang tầm mắt, cảm giác tự nhiên (mặc định).
- **High-Angle / Low-Angle**: nhìn xuống (nhân vật nhỏ bé/yếu thế) hoặc nhìn lên (tăng cảm giác quyền lực/căng thẳng).
- **Overhead / Top Shot**: nhìn gần như từ trên đỉnh xuống để thấy vị trí.
- **Rear Two-Shot / Back-to-Back**: nhìn từ sau lưng cả hai / hai người quay lưng nhau (nhấn mạnh sự chia rẽ/lạnh nhạt).

### 3.2 Phân rã đối thoại >2 người & nhóm
Để thiết lập không gian ban đầu cho nhóm 3-4 người, dùng các chuẩn khung sau trước khi cắt cận:

- **Wide Shot / Long Shot (Toàn cảnh)**: thấy toàn bộ cơ thể và không gian xung quanh. Dùng để thiết lập bối cảnh (làm Master SF), vị trí, khoảng cách giữa các nhân vật.
- **Full Shot / Medium Long Shot (Toàn thân)**: thấy rõ toàn bộ cơ thể từ đầu đến chân. Dùng cho cảnh đối thoại di chuyển, hành động nhóm.
- **Medium Wide / 3-4 Shot**: cắt ngang từ đùi hoặc gối trở lên. Giữ được ngôn ngữ cơ thể và biểu cảm tương tác.
- **Medium Shot / Waist Shot**: cắt ngang eo. Dùng nhiều trong hội thoại nhóm, tranh luận, tập trung vào tương tác và phản ứng.

**Nguyên tắc xử lý shot nhóm:**
- **Shot định vị**: bắt buộc có ít nhất 1 góc rộng (Wide/Full/Medium Wide) ở đầu phân đoạn để sinh Master SF, giúp khán giả nhận diện không gian và vị trí tương đối của nhóm.
- **Chia để trị (Sub-grouping)**: không chẻ bằng cách xoá người. Khán giả không được mất dấu ai giữa một cuộc đối chất. Tuyệt đối không nhồi 3-4 người cùng nét, cùng cỡ mặt vào một khung cận (CU/MCU). Để giữ đủ mặt nhóm 3-4 người, có 2 cách:
  - *(Cách 1)* Dùng góc Toàn hoặc góc Trung (Wide/Medium) để tất cả đều rõ mặt trong khung.
  - *(Cách 2)* Nếu dùng góc Cận/Hẹp, phải chẻ bằng độ nét (phân lớp chiều sâu): chủ thể chính nét ở giữa, người thứ hai làm vai/gáy tiền cảnh out nét, người thứ ba đứng lùi mờ ở lớp sau. ⚠️ Chỉ được gán "lớp sau" cho người vốn dĩ đang đứng phía sau theo chiều sâu vật lý ở Master SF — luật đầy đủ và cách xử lý đúng: `8-prompt-sf.md` §Cấm đẩy người ngang hàng thành "lớp sau".

## 4. Tư duy chuyển góc khi lập bảng
- **Tư duy theo Beat tâm lý:** lập danh sách shot dựa trên diễn biến câu chuyện thay vì liệt kê cơ học.
- Nguyên lý *"chỉ chuyển góc khi nhận thức / quyền lực / thông tin / cảm xúc thay đổi"* và Công thức nhịp điệu (Drama Flow): `0-tu-duy-dien-anh.md` §II, §IV.
- Cách suy ra ai lọt vào khung từ điểm đặt camera: `8-prompt-sf.md` §Xác định CAST.

## 5. Chia thoại và thời lượng

### 5.0 Tổng thời lượng Hook
- **Tổng thời lượng = tổng `dur` thực tế** (10s × clip thường + 6s × clip tách từ chuỗi thoại dồn — §5.2b), là hệ quả của số chữ, không phải mục tiêu. Mỗi lần tách: +1 shot, +2s.

### 5.1 Mốc `dur`
- **Mốc chuẩn 10s (`dur: 10`)** cho mọi clip của Hook (2 shot con, 1 hard cut). Bỏ hẳn mốc 15s.
- **Mốc 6s (`dur: 6`)** CHỈ dùng cho cặp clip tách ra từ một chuỗi thoại dồn (§5.2b). Mỗi clip 6s vẫn là 2 shot con, 1 hard cut.
- Ngoài trường hợp đó, tuyệt đối không dùng 6s hay bất kỳ con số lẻ nào khác.

### 5.2 Tốc độ và mật độ thoại
- **Quy đổi 3.0 từ/giây**: định nghĩa lại ba biên theo tỉ lệ lấp đầy thay cho giây tuyệt đối:
  - **Sàn**: mỗi shot lấp ≥80% dur → clip 10s cần ≥24 từ.
  - **Trần**: chừa 0,7s biên → 28 từ.
  - **Cửa sổ chuẩn**: 24–28 từ/clip. Ra ngoài cửa sổ thì gộp/tách thoại, KHÔNG đổi dur.
  - **Clip 6s** (chỉ ở §5.2b): trần **16 từ**; không áp sàn 80% — khoảng lặng giữa các lượt cắt lời là nhịp diễn, không phải chỗ trống.

### 5.2b Chuỗi thoại dồn → tách 2 clip 6s
- **Nhận diện**: khi chia câu vào clip 10s mà một clip rơi vào **≥4 lượt thoại liên tiếp đổi người nói, lượt nào cũng ngắn (≤6 từ)** — kiểu cắt lời qua lại ("Your Honor—" / "Sit down." / "Your Honor—" / "I said sit down.") — thì KHÔNG nhồi vào một clip.
- **Tách**: cắt thành **2 clip liền nhau, mỗi clip `dur: 6`**, cắt đúng ranh giới một lượt thoại, mỗi clip **≤3 lượt**. Câu văn kể dính kèm đi theo lượt thoại liền trước nó, giữ nguyên thứ tự gốc (`1-kich-ban.md` §2.2).
- Mỗi clip 6s vẫn có **SF riêng** (§1.1) và vẫn áp luật người nói rõ mặt (§5.3). Nên đổi góc giữa hai clip (VD: clip đầu OTS lên người đang áp đảo, clip sau góc thấy mặt người bị cắt lời) để cú qua lại có nhịp cắt thật.
- **Hành động của người bị cắt lời** phải là phản ứng với tình huống (bước lên chắn cho thân chủ rồi phải lùi về…), không phải cử chỉ nghi thức rỗng (giơ bàn tay xin phát biểu rồi hạ xuống) — `11-prompt-video.md` §4.5b.
- Báo user số shot và tổng thời lượng sau khi tách (§5.0).
- **Vì sao**: 5 lượt ngắn trong một clip 10s thì diễn viên AI không kịp thở, cú cắt lời thành máy móc; lỗi có thật ở một Hook có loạt thẩm phán ↔ luật sư cắt lời nhau. Tách ra thì mỗi clip chỉ còn một cú đẩy qua lại, và 6s giữ nhịp dồn dập thay vì kéo dài lặng.

### 5.3 Người nói phải rõ mặt · cắt theo phản ứng
- **Trong shot con có câu thoại của ai, người đó phải RÕ MẶT trong khung** (chính diện, 3/4, tối đa nghiêng ngang, đủ lớn để thấy miệng). Cấm để người nói chính phát thoại từ sau lưng, từ vai/gáy OTS hay từ một dáng mờ nhỏ ở mép khung — nhất là phản diện đang nhục mạ: nhìn gáy thì mất sạch sự khinh miệt trên mặt, và lip sync không còn gì để bám.
- **Cắt theo phản ứng** (shot cắt sang mặt người nghe khi phản ứng của họ là nội dung chính) vẫn đúng, nhưng phản ứng phải nằm ở **shot con khác, sau khi câu thoại đã xong**, hoặc dùng góc hai lớp thấy mặt cả người nói lẫn người nghe. Không mượn góc sau lưng người nói để lấy mặt người nghe trong lúc người nói đang nói. Lỗi có thật: một clip quay sau lưng thẩm phán suốt 5 giây ông hạch hỏi người mẹ.
- **Ngoại lệ duy nhất**: câu chen ngang ngắn **≤5 từ, hoặc bị cắt lời giữa chừng**, của một người phụ, trong clip mà người nói chính vẫn rõ mặt — câu đó được nói từ vai/gáy OTS.

### 5.4 Xử lý thoại O.S (điện thoại / loa / gọi vọng)
AI sinh video tự cấp giọng O.S rất tệ. Phải mồi một "bản sao" có người thật đứng nói để lấy chuẩn Voice.
- *Với gọi điện thoại*: lặp câu thoại của B 2 lần. Video 1: A nói, B nói off-screen (giữ O.S y như kịch bản gốc để tạo nhịp diễn/thời lượng). Video 2 ngay dưới (bản sao): SF chuẩn của B cầm điện thoại áp tai, riêng tả B đang nói lại chính xác câu đó.
- *Với loa phát / lộ đoạn ghi âm / gọi vọng*: Video 1: shot nhân vật ngơ ngác nghe ngóng. Video 2: SF chuẩn của nhân vật đó đặc tả chính họ đang thốt ra câu thoại đó (cầm micro, đứng gọi từ xa, hoặc cảnh rò rỉ trong quá khứ lúc họ bị lén ghi âm, chuẩn theo cảm xúc lúc đó).



## 6. Continuity (không gian liên tục)

SF là khung đầu clip, nên phải lấy trạng thái kết thúc của clip liền trước.

- **Rà 4 trục liên tục**: Xa/gần · Trên/dưới (đứng/ngồi) · Trước/sau · tay cầm gì (đặc biệt các món có vai trò kịch bản).
- **Quy tắc trạng thái chờ (Pending State)**: nếu trong shot có hành động thay đổi trạng thái tĩnh (mở cửa, đứng lên, ngồi xuống, đưa đồ), khung đầu clip (SF) phải ở trạng thái chưa thực hiện. Luật đầy đủ khi viết prompt: `8-prompt-sf.md` §Trạng thái chờ.
- **Shot trước di chuyển**: trong prompt phải có đoạn kết clip (→ `11-prompt-video.md`), và SF của shot đó phải thấy rõ mặt người sắp di chuyển (không để họ quay lưng tiền cảnh).
- **Mối nối nhảy `zone` / `who`**: vá bằng một trong hai cách (Hook không dùng nhịp lặng):
  1. Cho nhân vật vừa đi vừa nói (nếu nhịp phim cho phép), hoặc
  2. Tả bước di chuyển ngắn ở cuối prompt shot trước.

## 7. Kiểm tra cuối bước

**Đếm được — đếm trên bảng shot, ghi số ra rồi đối chiếu:**
- [ ] Mọi shot có `dur` là **10**; chỉ cặp clip tách từ chuỗi thoại dồn là **6** (§5.2b).
- [ ] Không clip 10s nào vượt **28 từ**; không clip 6s nào vượt **16 từ**.
- [ ] Không clip 10s nào có giây thoại < 80% dur (dưới 24 từ) — clip 6s được miễn.
- [ ] Không clip nào chứa **≥4 lượt thoại ngắn (≤6 từ) liên tiếp đổi người nói** — có thì đã tách 2 clip 6s, mỗi clip **≤3 lượt** (§5.2b).
- [ ] Cột "giây thoại" (từ ÷ 3.0) đã ghi ra cho từng shot.
- [ ] Số mã `sf` khác nhau **bằng đúng** tổng số shot — không shot nào dùng lại ảnh SF của shot khác (§1.1).
- [ ] Góc rộng **20–25%** · đặc tả **~2%** · cận/trung **40–50%** · góc đôi **20–30%**.
- [ ] Cụm có ≥3 main cast: **≥60%** SF đủ mặt cả nhóm · **≤20%** SF chỉ có 2 người.
- [ ] Mọi cặp SF cùng cụm & cùng chủ thể khác nhau ở **≥2 trục** (cỡ cảnh · trục máy ≥30° · hướng mắt/tư thế) — §1.1.

**Phải đọc mới thấy:**
- [ ] Diff text với kịch bản gốc: mọi câu chữ giữ nguyên vẹn, không tự ý lược bỏ.
- [ ] Người nói trong mỗi shot con **RÕ MẶT** (chính diện/3/4/nghiêng ngang, đủ lớn thấy miệng); chỉ câu chen ngang **≤5 từ** hoặc bị cắt lời của người phụ mới được nói từ vai/gáy OTS (§5.3).
- [ ] Bộ góc máy đảm bảo luật **30° / 2 bậc** giữa các shot liền nhau.
- [ ] Rà 4 trục continuity giữa mọi cặp shot liền nhau: xa/gần · đứng/ngồi · trước/sau · tay cầm gì.
- [ ] Mọi mối nhảy `zone` / `who` đã vá bằng cách phù hợp.
