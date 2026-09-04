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

### 1.1 Tái sử dụng SF (bắt buộc không sinh trùng lặp)
- Khi tạo shot mới, mặc định gán 1 mã SF tương ứng (`SF-S<scene>-<shot>`, VD: `SF-S1-07`).
- **Bắt buộc dùng lại SF cũ** khi shot lặp lại cùng nhân vật, cùng góc máy, cùng tư thế và cùng nón quan sát. Áp cho cả ba nhóm:
  - **(a)** Cặp OTS / cận đơn khi đảo góc A-B-A-B;
  - **(b)** Khung TWO-SHOT — mỗi lần mạch thoại quay lại thế trận chung của hai người;
  - **(c)** Khung MASTER / rộng — mỗi lần cần tái lập không gian (ít hơn 2 nhóm trên).
- *Cách ghi vào dữ liệu*: `2-du-lieu-sf-board.md` §5.2.

### 1.2 Định mức của scene / dự án
| Định mức | Ngưỡng |
|---|---|
| Tổng thời lượng Hook | **ĐÚNG 2 PHÚT (120 giây)** |
| Nhịp lặng (shot không thoại) | **0% (TUYỆT ĐỐI KHÔNG DÙNG NHỊP LẶNG)** |
| Tái sử dụng SF | ~20–25% tổng số shot (scene thoại đảo góc 2 người có thể đạt 30–40%) |
| Cân bằng thành phần trong số shot dùng lại | OTS + cận đơn ≤ 60% · two-shot + master ≥ 40% |
| Tỉ lệ cỡ cảnh | Cận/Trung (CU/MCU) ~40–50% · Góc đôi (Two-Shot/OTS) 20–30% · Toàn cảnh/Góc rộng 20–25% · Góc Đặc Tả (Insert/ECU) ~2% |
| Cụm có ≥3 main cast | ≥60% SF có đủ mặt cả nhóm · ≤20% SF chỉ có 2 người |

**Cách tự đếm** — làm trên BẢNG SHOT, trước khi sinh prompt:

1. Đếm tổng số shot của scene.
2. Đếm shot có ô `sf` trỏ về mã SF đã dùng trước đó → tỉ lệ tái sử dụng.
3. Trong số shot dùng lại, chia hai cột: (OTS + cận đơn) và (two-shot + master) → kiểm 60/40.
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

### 5.0 Tổng thời lượng Hook (Đúng 2 phút)
- **Tổng thời lượng toàn bộ bảng shot phải bằng ĐÚNG 2 PHÚT (120 giây).**
- Dù kịch bản gốc có dài hay chứa nhiều phân đoạn, bảng shot chỉ sản xuất dung lượng vừa tròn 120s (vd: 8 shot 15s hoặc kết hợp 10s/15s đạt tổng 120s).

### 5.1 Mốc `dur`
- Mặc định dùng mốc 15s (`dur: 15`) — chủ yếu nhất. Dạng 3 shot con, 2 hard cut.
- Số ít trường hợp rất hiếm dùng mốc 10s (`dur: 10`), không quá 10% tổng số shot toàn phim. Dạng 2 shot con, 1 hard cut.
- **Tuyệt đối không dùng mốc 6s** hoặc các con số lẻ khác.

### 5.2 Tốc độ và mật độ thoại
- Con số 3.0 từ/giây vừa là trần chống nhồi (trần cứng tối đa 42 từ cho clip 15s để chừa 1s biên an toàn 14s; tối đa 28 từ cho clip 10s), vừa là thước đo sàn chống loãng.
- **Mật độ thoại**: đa số shot phải lấp 13–14s thoại trong clip 15s (≈39–42 từ). Chỉ số ít shot thật sự cần đất diễn cảm xúc mới hạ xuống 8–10s (≈24–28 từ). Thoại mỏng hơn nữa thì clip rỗng, toàn quãng chết — phải gộp thêm thoại của shot kế vào, đừng để một câu 3–8 từ đứng riêng một clip 15s.
- Ba biên phải tự đếm: **sàn từng shot** (≥8s thoại cho clip 15s ≈ 24 từ) · **trần từng shot** (42 từ cho 15s, 28 từ cho 10s) · **mật độ toàn phim** (≥65% shot thoại lấp ≥13s ≈ 39 từ).
- *Bộ luật cũ từng có song song hai con số: **42 từ** và **45 từ** (bản ở phần prompt video). Đã thống nhất về **42**.*

### 5.3 Cắt theo phản ứng
Shot cắt sang mặt người nghe khi phản ứng của họ là nội dung chính.

### 5.4 Xử lý thoại O.S (điện thoại / loa / gọi vọng)
AI sinh video tự cấp giọng O.S rất tệ. Phải mồi một "bản sao" có người thật đứng nói để lấy chuẩn Voice.
- *Với gọi điện thoại*: lặp câu thoại của B 2 lần. Video 1: A nói, B nói off-screen (giữ O.S y như kịch bản gốc để tạo nhịp diễn/thời lượng). Video 2 ngay dưới (bản sao): SF chuẩn của B cầm điện thoại áp tai, riêng tả B đang nói lại chính xác câu đó.
- *Với loa phát / lộ đoạn ghi âm / gọi vọng*: Video 1: shot nhân vật ngơ ngác nghe ngóng. Video 2: SF chuẩn của nhân vật đó đặc tả chính họ đang thốt ra câu thoại đó (cầm micro, đứng gọi từ xa, hoặc cảnh rò rỉ trong quá khứ lúc họ bị lén ghi âm, chuẩn theo cảm xúc lúc đó).

### 5.5 Chuyển động
Cộng thêm 2–3s (hoặc hơn) vào thời lượng ước tính của shot nếu có di chuyển, đứng/ngồi, đi khỏi khung — làm cơ sở nâng mốc `dur` từ 10s lên 15s.

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
- [ ] Mọi shot có `dur` là **15** hoặc **10**; không 6s, không số lẻ.
- [ ] Shot `dur=10` chiếm **≤10%** tổng số shot toàn phim.
- [ ] Không shot nào vượt **42 từ** (clip 15s) / **28 từ** (clip 10s).
- [ ] Không shot thoại nào dưới **24 từ** (sàn 8s cho clip 15s) — dưới thì gộp thoại shot kế vào.
- [ ] **≥65%** shot thoại lấp ≥13s (≈39 từ) — tính trên toàn phim.
- [ ] Tái sử dụng SF **20–25%** tổng số shot (scene đảo góc 2 người có thể 30–40%).
- [ ] Trong số shot dùng lại: OTS + cận đơn **≤60%**, two-shot + master **≥40%**.
- [ ] Góc rộng **20–25%** · đặc tả **~2%** · cận/trung **40–50%** · góc đôi **20–30%**.
- [ ] Cụm có ≥3 main cast: **≥60%** SF đủ mặt cả nhóm · **≤20%** SF chỉ có 2 người.

**Phải đọc mới thấy:**
- [ ] Diff text với kịch bản gốc: mọi câu chữ giữ nguyên vẹn, không tự ý lược bỏ.
- [ ] Người đang nói xuất hiện trong khung (rõ mặt hoặc vai/gáy OTS).
- [ ] Bộ góc máy đảm bảo luật **30° / 2 bậc** giữa các shot liền nhau.
- [ ] Rà 4 trục continuity giữa mọi cặp shot liền nhau: xa/gần · đứng/ngồi · trước/sau · tay cầm gì.
- [ ] Mọi mối nhảy `zone` / `who` đã vá bằng cách phù hợp.
