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
⛔ **Short không dùng lại ảnh SF, dù chỉ một lần.** Mỗi shot video có đúng một SF của riêng nó; số SF của scene luôn **bằng** số shot.

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
| Mốc dur | **10s cho MỌI shot** |
| Số shot | **ceil(tổng số từ Short ÷ 26)** |
| Nhịp lặng (shot không thoại) | **0% (TUYỆT ĐỐI KHÔNG DÙNG NHỊP LẶNG)** |
| Tái sử dụng ảnh SF | **0% — cấm tuyệt đối, số SF = số shot** |
| Tỉ lệ cỡ cảnh (khung dọc 9:16) | Cận/Trung (CU/MCU/MS) **50–60%** · Góc đôi xếp lớp (Stacked Two-Shot/OTS) **20–30%** · Toàn cảnh dọc (Vertical Wide) **10–20%** · Góc Đặc Tả (Insert/ECU) **~2%** |
| Sàn của Toàn cảnh dọc | **= đúng số cụm không gian** (mỗi cụm 1 Master SF, không hơn) |
| Trần của Góc Đặc Tả | **tối đa 1 shot cho cả phim** (Short 8–12 clip, 2% làm tròn xuống là 0–1) |
| SF một nhân vật (Solo Frame) | **25–40%** tổng số shot · **≤3 shot liên tiếp** — là nhóm con của Cận/Trung, không cộng thêm vào tổng |
| Cụm có ≥3 main cast | ≥60% SF có đủ mặt cả nhóm · ≤20% SF chỉ có 2 người |

**Cách tự đếm** — làm trên BẢNG SHOT, trước khi sinh prompt:

1. Đếm tổng số shot của scene.
2. Đếm số mã `sf` khác nhau → phải BẰNG tổng số shot. Có hai shot trùng mã là sai.
3. Với mỗi cặp SF cùng cụm và cùng chủ thể, đối chiếu ba trục ở §1.1 → phải khác nhau ở ít nhất hai trục.
4. Đếm shot theo cỡ cảnh ghi ở cột GÓC → 4 nhóm tỉ lệ; đối chiếu luôn số góc rộng với số cụm không gian.
5. Với cụm có ≥3 main cast: đếm SF đủ mặt cả nhóm, và SF chỉ có 2 người.
6. Đếm SF chỉ có **một** tên trong `pose.who` → đó là Solo Frame; rà luôn xem có chỗ nào 4 solo liên tiếp không (§3.3).

⚠️ *Định mức đủ cast tính theo **cụm không gian**, không theo scene — một scene nhiều cụm thì đếm riêng từng cụm. Bản cũ từng ghi ngưỡng **50%**; đã thống nhất về **60%**. Trong khung dọc, "đủ mặt cả nhóm" được thoả bằng cách **xếp so le theo chiều sâu** (§3.0), không phải bằng cách lùi máy cho rộng ra.*

⚠️ **Solo Frame ăn vào định mức đủ cast, không cộng thêm vào tổng cỡ cảnh.** Solo là nhóm con của Cận/Trung nên không làm tổng tỉ lệ vượt 100. Nhưng ở cụm có ≥3 main cast, luật "≥60% SF đủ mặt cả nhóm" siết Solo xuống — cả Solo lẫn SF 2 người cộng lại chỉ còn ≤40%. Đó là chủ ý: nhóm càng đông thì càng phải giữ khán giả khỏi mất dấu người. Cụm 2 nhân vật thì Solo thoải mái chạy hết 25–40%.

⚠️ **Đụng độ giữa sàn Toàn cảnh dọc và trần 20%** — thứ tự ưu tiên rõ ràng: mỗi cụm bắt buộc có 1 Master SF góc rộng (`6-cum-va-master-sf.md` §2.2), nên **sàn luôn thắng trần**. Tuyệt đối không bỏ Master của một cụm để chạy cho đủ tỉ lệ, và cũng không thêm góc rộng nào ngoài các Master.

Vượt trần 20% (VD: 3 cụm trong 10 shot) không phải lỗi tỉ lệ mà là **cảnh báo thế trận bị chẻ vụn** — quay lại `6-cum-va-master-sf.md` §1 rà xem hai cụm nào thực ra chung một trục sâu và gộp được. Gộp được thì gộp; xét kỹ mà đúng là ba nơi khác nhau thì giữ ba Master, ghi nhận vượt trần và đi tiếp.

## 2. Quy tắc viết dòng `goc`

Dòng `goc` trả lời câu hỏi *"Khung này quay bằng góc gì, có ai, nét hay mờ?"*. Bắt buộc có cho mọi SF. Viết cùng lúc sinh SF ban đầu.

> **Lưu ý**: dòng `goc` sinh ra cùng SF, nhưng nó được dùng làm tiêu chuẩn khung hình cho Video Shot trên timeline.

1. **Nêu đích danh**, không đếm số lượng (VD: *"Everett trái + Warren phải, CẢ HAI RÕ MẶT"*).
2. **OTS phải nêu rõ vai của ai** làm tiền cảnh.
3. **Đúng tên nhân vật** như trong kịch bản.
4. **Khai cả người không phải chủ thể** (đang ngồi im/ngủ trong `pose.who` cũng phải khai, kể cả MAIN CAST đang diễn ở cụm khác mà lọt vào lớp sau của khung gối đầu, dù họ ở rất xa và out nét).
5. **Phải dùng đúng thuật ngữ cỡ cảnh/góc máy bản KHUNG DỌC** (Vertical Wide, CU, Stacked Two-Shot, OTS, Low Angle...) được quy định ở §3.1–§3.2. Không tả lồng bối cảnh, đạo cụ hay thông số kỹ thuật máy quay (tiêu cự 35mm, f/1.8) vào dòng này. Thuật ngữ của phim ngang (`Medium Two-Shot`, `Two-Shot ngang`, `3-4 Shot`) đã bị thay — dùng lại là sai chuẩn.
6. **Tuyệt đối cấm khai báo nhân vật nền** (nền, quần chúng, khách nền, người đi đường). Dòng này chỉ dành cho MAIN CAST.

## 3. Góc máy (Coverage)

- **Góc rộng**: dùng làm Master Shot mở cảnh, khép/chuyển cảnh, hoặc khung bao quát khi các nhân vật đối thoại nhóm/di chuyển trong bối cảnh khi thấy hợp lý.
- **Góc Đặc Tả (Insert/ECU)**: rất hạn chế — với một Short 8–12 clip, ~2% nghĩa là **tối đa 1 shot cho cả phim**. Dùng để đặc tả đồ vật quan trọng, chi tiết tay, mắt... nhằm chuyển nhịp hoặc che giấu raccord.
- **Góc cực đoan (High/Low/POV)**: rất hạn chế, chỉ dùng có chủ đích (nhấn mạnh tâm lý, quyền lực, hoặc nhập vai).
- Luật cỡ cảnh của Master SF: `6-cum-va-master-sf.md` §2.2.

### 3.0 Khung dọc 9:16 đổi luật cỡ cảnh thế nào

> Mọi thuật ngữ ở §3.1 và §3.2 bên dưới đã được viết lại theo luật này. Đọc §3.0 trước, đừng bê thẳng bộ góc của phim ngang vào.

**Định luật: khung dọc không có chỗ theo chiều NGANG, chỉ có chỗ theo chiều SÂU.** Ở cùng một chiều cao chủ thể, khung 9:16 chỉ rộng bằng khoảng một phần ba khung 16:9. Mọi thế trận mà phim ngang giải quyết bằng cách **dàn hàng ngang**, khung dọc bắt buộc giải quyết bằng cách **xếp so le theo chiều sâu** — người gần máy nằm ở dải dưới khung, người lùi sâu hơn nổi cao dần lên trong khung.

**Hệ quả 1 — không lùi máy để nhét thêm người.** Muốn giữ đúng chừng ấy người trong khung, máy dọc phải lùi xa hơn máy ngang một bậc, và mặt sẽ nhỏ đi theo. Luật đảo lại: **giữ nguyên khoảng cách máy, chấp nhận ít người trong khung hơn**. **Sàn cỡ mặt:** ở mọi shot có thoại, mặt người đang nói phải cao **≥1/8 chiều cao khung** — kể cả ở Vertical Wide. Thấp hơn ngưỡng đó là mất biểu cảm khi xem trên điện thoại, và cả clip thành công cốc. (Cận/trung thì vượt xa ngưỡng này; ngưỡng chỉ để chặn thói quen lùi máy cho "đủ người".)

**Hệ quả 2 — trần người rõ mặt theo cỡ cảnh (luật cứng, đếm được):**

| Cỡ cảnh dọc | Số người ĐƯỢC rõ mặt | Người còn lại trong khung |
|---|---|---|
| ECU / CU | **1** | không ai khác lọt khung |
| MCU · Dirty Single | **1** | 1 vai/gáy tiền cảnh ở đáy khung, out nét |
| Stacked Two-Shot · OTS | **2** | tối đa 1 người lùi sâu, out nét |
| Medium Wide dọc | **3** | — |
| Vertical Wide (Master SF) | **4** (trần tuyệt đối, khớp trần 4 nhân vật ở `2-du-lieu-sf-board.md` §7) | — |

**Hệ quả 3 — cấm dàn hàng ngang.** Tuyệt đối không viết ba, bốn người đứng thành một hàng ngang trên cùng một mặt phẳng chiều sâu trong khung dọc. Kết quả luôn là một trong hai lỗi: máy phải lùi rất xa khiến mặt ai cũng bé, hoặc AI cắt cụt người ở hai mép khung. Thế trận so le theo chiều sâu **phải được chốt ngay từ Master SF** (`6-cum-va-master-sf.md` §1.1) — tự bịa ra lúc cắt cận là vi phạm `8-prompt-sf.md` §2.2 (cấm đẩy người ngang hàng thành "lớp sau").

**Hệ quả 4 — chiều cao là tài nguyên, bắt buộc tiêu.** Khung dọc thừa chỗ trên và dưới. Mỗi khung phải khai rõ đỉnh khung có gì và đáy khung có gì: trần/mái/vòm/bầu trời ở đỉnh · mặt sàn/mặt bàn/bậc thềm ở đáy · hoặc một lớp tiền cảnh chắn thấp (lưng ghế, mép bàn, vai người). Bỏ trống cả hai đầu thì khung đọc ra như một ảnh ngang bị kéo dãn. *(Cách viết vị trí theo dải dọc và vùng an toàn UI: `8-prompt-sf.md` §1.1.)*

**Hệ quả 5 — đổi góc thì đổi theo chiều sâu, không đổi theo bề ngang.** Luật "khác ≥2 trục" ở §1.1 vẫn giữ nguyên, nhưng trục **cỡ cảnh** trong khung dọc chủ yếu được tạo ra bằng cách **đổi khoảng cách máy tới người gần nhất**, chứ không phải bằng cách quét ngang sang một nhóm khác trong cùng bối cảnh.

### 3.1 Phân rã đối thoại 2 người (bộ góc tiêu chuẩn — bản khung dọc)
Bắt buộc dùng đúng bộ thuật ngữ sau khi viết dòng `goc` và prompt SF. Cột "vì sao" ghi lại chỗ khác với phim ngang.

**Khung cơ bản (Basic Frames)**
- **Vertical Wide Two-Shot** *(thay cho Master / Wide Two-Shot)*: toàn cảnh 2 người và không gian, hai người đứng **so le chiều sâu** — một người gần máy hơn rõ rệt. Dùng làm Master SF.
- **Stacked Two-Shot** *(thay cho Medium Two-Shot — đây là khung đôi MẶC ĐỊNH của 9:16)*: người gần máy chiếm dải dưới khung (lấy từ ngực trở lên), người kia lùi sâu hơn một đến hai bước chân, nổi ở dải giữa khung, cao hơn trong khung. Cả hai rõ mặt.
- **Tight Stacked Two-Shot** *(thay cho Tight Two-Shot)*: như trên nhưng cắt sát hơn, người dưới lấy từ vai trở lên. Dùng khi cần cảm xúc của cả hai cùng lúc.
- **Profile Two-Shot dọc**: hai người đối diện nhau quay ngang 90°, máy đứng ở giữa trục. Chỉ dùng khi hai người **cách nhau dưới một bước chân** — xa hơn là hai cái đầu bị đẩy ra hai mép khung và vỡ khung dọc.
- **3/4 Stacked Two-Shot**: máy đặt chéo, một người gần một người xa, thấy mặt/phản ứng của cả hai.
- ⛔ **Two-Shot ngang (hai người dàn hàng cạnh nhau, cùng mặt phẳng chiều sâu)**: **CẤM** trong khung dọc — §3.0 Hệ quả 3. Hai người ngồi cạnh nhau ngoài đời thì máy phải xê dịch về một bên để biến thế ngồi đó thành so le chiều sâu.

**Góc hội thoại (Dialogue Coverage)**
- **Clean Stacked Two-Shot**: cả hai cùng rõ mặt, vẫn phải so le chiều sâu.
- **OTS A → B / OTS B → A (Qua vai)**: vai/gáy người tiền cảnh chiếm **góc dưới khung** (không phải mép trái/phải như phim ngang), người kia ở dải giữa. Đây là góc ăn nhất của 9:16 sau Clean Single.
- **Dirty Single**: cận 1 người, một mảnh vai hoặc đỉnh đầu người kia lọt vào **đáy khung**, out nét.
- **Clean Single**: cận 1 người rõ mặt, không vướng vai/đầu người kia ở tiền cảnh — nhưng người kia **vẫn có thể** ở lớp sau, out nét. Khung dọc "ăn" góc này nhất.
- **Solo Frame (SF một nhân vật)**: trong khung **không có ai khác thuộc main cast**, kể cả vai/gáy tiền cảnh lẫn bóng người out nét ở lớp sau. Đây là góc riêng, không phải biến thể của OTS — luật đầy đủ ở §3.3.
- **Shared Reaction Stacked Two-Shot**: giữ cả hai trong khung để bắt phản ứng cùng lúc, theo bố cục Stacked.

**Góc cao, thấp & góc nhìn**
- **Eye-Level**: máy ngang tầm mắt, cảm giác tự nhiên (mặc định).
- **High-Angle**: nhìn xuống, nhân vật nhỏ bé/yếu thế. Vẫn phải nghiêng nhẹ — khung dọc nghiêng mạnh là méo hình thang thấy rõ và mặt bị bóp.
- ⛔ **Low-Angle chếch ngược lên mặt: CẤM.** Thể hiện quyền lực bằng **máy ngang tầm mắt, hạ thấp hơn tầm mắt nhân vật một chút, không tilt lên**, cỡ Medium 3/4. Luật đầy đủ + câu chặn bắt buộc chèn vào prompt: `0-tu-duy-dien-anh.md` §II.3b.
- **Overhead / Top Shot**: nhìn gần như từ đỉnh xuống để thấy vị trí. Khung dọc dùng góc này tốt hơn phim ngang (một hàng người trải theo chiều sâu đọc ra rất rõ), nhưng vẫn tính vào nhóm góc cực đoan, dùng hạn chế.
- **Rear Stacked Two-Shot** *(thay cho Rear Two-Shot / Back-to-Back)*: người quay lưng chiếm đáy khung, người kia lùi sâu quay mặt đi hướng khác — nhấn chia rẽ/lạnh nhạt. Không đặt hai người quay lưng nhau cạnh nhau theo bề ngang.

### 3.2 Phân rã đối thoại >2 người & nhóm (bản khung dọc)
Nhóm 3–4 người là chỗ khung dọc dễ vỡ nhất. Dùng đúng các chuẩn khung sau, tất cả đều giả định thế trận **so le chiều sâu** đã chốt ở Master SF:

- **Vertical Wide / Long Shot dọc (Toàn cảnh)**: thấy toàn bộ cơ thể và không gian, nhóm trải theo **chiều sâu** (người gần nhất ở đáy khung, người xa nhất khoảng 1/3 trên khung). Dùng làm Master SF, chốt vị trí và khoảng cách. Trần 4 người rõ mặt.
- **Full Shot dọc (Toàn thân)**: thấy trọn người từ đầu đến chân — cỡ cảnh mà khung dọc thoải mái nhất, vì chiều đứng chính là chiều dư. Dùng cho đối thoại di chuyển và hành động nhóm. Trần 3 người rõ mặt (người thứ 4 lùi sâu, out nét).
- **Medium Wide dọc / 3-Shot** *(thay cho "3-4 Shot")*: cắt từ đùi hoặc gối trở lên. **Trần 3 người**, không phải 4 — nhét người thứ tư vào là hai người ngoài cùng bị cắt cụt ở mép khung.
- **Medium Shot / Waist Shot**: cắt ngang eo. Trần **2 người rõ mặt** + 1 người lùi sâu out nét. Đây là ngưỡng mà phim ngang còn giữ được 3 người, khung dọc thì không.

**Nguyên tắc xử lý shot nhóm:**
- **Shot định vị**: bắt buộc có ít nhất 1 góc rộng dọc (Vertical Wide / Full Shot dọc) ở đầu phân đoạn để sinh Master SF. Khung dọc càng cần shot này hơn phim ngang: các khung cận sau đó chỉ chứa 1–2 người, nên nếu khán giả không được xem bản đồ vị trí một lần cho tử tế, họ sẽ mất dấu người thứ ba ngay từ cú cắt đầu tiên.
- **Chia để trị (Sub-grouping)**: không chẻ bằng cách xoá người. Khán giả không được mất dấu ai giữa một cuộc đối chất. Tuyệt đối không nhồi 3-4 người cùng nét, cùng cỡ mặt vào một khung cận (CU/MCU). Để giữ đủ mặt nhóm 3-4 người trong khung dọc, có 2 cách:
  - *(Cách 1)* Dùng góc Toàn dọc hoặc Medium Wide dọc, **và** xếp nhóm so le theo chiều sâu chứ không thành hàng ngang (§3.0 Hệ quả 3).
  - *(Cách 2)* Nếu dùng góc Cận/Hẹp, phải chẻ bằng độ nét theo **ba tầng dọc**: người gần máy làm vai/gáy tiền cảnh out nét ở **đáy khung** · chủ thể chính nét ở **dải giữa** · người thứ ba đứng lùi mờ ở **dải trên**. ⚠️ Chỉ được gán "lớp sau" cho người vốn dĩ đang đứng phía sau theo chiều sâu vật lý ở Master SF — luật đầy đủ và cách xử lý đúng: `8-prompt-sf.md` §Cấm đẩy người ngang hàng thành "lớp sau".
- **Khi trần người bị vượt**: không lùi máy để nhét cho đủ (§3.0 Hệ quả 1). Cách đúng là tách thành hai shot liên tiếp, mỗi shot một nhóm nhỏ, và giữ liên tục bằng hướng mắt — người ở shot A phải đang nhìn về đúng phía mà shot B đặt người kia.

### 3.3 SF một nhân vật (Solo Frame) — góc riêng, KHÔNG phải OTS

**Định nghĩa cứng:** trong khung chỉ có **đúng một** main cast. Không vai/gáy tiền cảnh của người khác. Không bóng người main cast đứng mờ ở lớp sau. Dòng `goc` và `pose.who` chỉ mang đúng một tên.

⚠️ **Ba góc dễ bị nhầm là solo mà không phải:**

| Góc | Có phải Solo Frame? | Vì sao |
|---|---|---|
| **OTS / Dirty Single** | ❌ **Không** | có mảnh vai/đỉnh đầu người kia ở đáy khung |
| **Clean Single** | ❌ Không nhất thiết | người kia vẫn được phép đứng mờ ở lớp sau |
| **Solo Frame** | ✅ | tuyệt đối không main cast nào khác lọt khung |

**Quần chúng nền KHÔNG bị cấm trong Solo Frame.** "Solo" nói về main cast, không nói về người nền. Nơi công cộng vẫn phải giữ mật độ sinh tồn và người nền vẫn phải đã dừng việc, quay hẳn nhìn về tiền cảnh (`9-quan-chung-nen.md`). Khung solo trống trơn người là một lỗi khác, nặng hơn.

**Khi nào dùng — bốn chỗ:**
1. Câu thoại là tuyên bố cá nhân, lời tự nói, hoặc narration của riêng nhân vật đó.
2. Beat "nhân vật cô độc" (`0-tu-duy-dien-anh.md` §III Beat 5) — cô lập bằng khung, không phải bằng cách xoá người nền.
3. Cỡ cảnh CU/ECU: trần người rõ mặt vốn là 1 (§3.0 Hệ quả 2), nên khung này gần như luôn là solo.
4. Trong kịch bản nhân vật đang ở một mình thật.

**Bốn luật khi viết Solo Frame:**
1. **Hướng mắt phải khoá đúng chỗ người kia đứng ở Master SF.** Nhân vật nhìn ra ngoài khung, về đúng phía đối phương, cùng một bên trục 180°. Đây là chỗ vỡ nhiều nhất — mất người kia khỏi khung thì **chỉ còn hướng mắt** giữ được thế trận.
2. **Cấm dùng Solo Frame để né trần người rõ mặt.** Khung đông quá thì tách shot theo §3.2, không phải xoá bớt người cho vừa khung.
3. **Hậu cảnh phải gánh phần việc của người thứ hai.** Khung solo mất một mốc không gian, nên bắt buộc khai rõ hơn mốc bối cảnh phía sau (mảng tường / quầy / cửa / dãy ghế nào) để khán giả biết nhân vật đang đứng ở đâu trong cụm.
4. **Không quá 3 Solo Frame liên tiếp** mà không chèn một khung có ≥2 người. Chuỗi solo dài biến Short thành talking-head và khán giả mất dấu thế trận.

**Ràng buộc dữ liệu:** `refs.chars` chỉ đính thẻ của đúng nhân vật đó (+ Master SF của cụm). `refs.bg` vẫn trỏ Master SF như mọi SF con.

**Prompt video:** clip sinh từ Solo Frame bắt buộc có câu chặn một-nhân-vật — `11-prompt-video.md` §4.1.

## 4. Tư duy chuyển góc khi lập bảng
- **Tư duy theo Beat tâm lý:** lập danh sách shot dựa trên diễn biến câu chuyện thay vì liệt kê cơ học.
- Nguyên lý *"chỉ chuyển góc khi nhận thức / quyền lực / thông tin / cảm xúc thay đổi"* và Công thức nhịp điệu (Drama Flow): `0-tu-duy-dien-anh.md` §II, §IV.
- Cách suy ra ai lọt vào khung từ điểm đặt camera: `8-prompt-sf.md` §Xác định CAST.

## 5. Chia thoại và thời lượng

### 5.0 Tổng thời lượng Short
- **Tổng thời lượng = số shot × 10s**, là hệ quả của số chữ, không phải mục tiêu.

### 5.1 Mốc `dur`
- **Mặc định dùng mốc 10s (`dur: 10`)** là mốc duy nhất của Short (Dạng 2 shot con, 1 hard cut). Bỏ hẳn mốc 15s.
- **Tuyệt đối không dùng mốc 6s** hoặc các con số lẻ khác.

### 5.2 Tốc độ và mật độ thoại
- **Quy đổi 3.0 từ/giây**: định nghĩa lại ba biên theo tỉ lệ lấp đầy thay cho giây tuyệt đối:
  - **Sàn**: mỗi shot lấp ≥80% dur → clip 10s cần ≥24 từ.
  - **Trần**: chừa 0,7s biên → 28 từ.
  - **Cửa sổ chuẩn**: 24–28 từ/clip. Ra ngoài cửa sổ thì gộp/tách thoại, KHÔNG đổi dur.

### 5.3 Cắt theo phản ứng
Shot cắt sang mặt người nghe khi phản ứng của họ là nội dung chính.

### 5.4 Xử lý thoại O.S (điện thoại / loa / gọi vọng)
AI sinh video tự cấp giọng O.S rất tệ. Phải mồi một "bản sao" có người thật đứng nói để lấy chuẩn Voice.
- *Với gọi điện thoại*: lặp câu thoại của B 2 lần. Video 1: A nói, B nói off-screen (giữ O.S y như kịch bản gốc để tạo nhịp diễn/thời lượng). Video 2 ngay dưới (bản sao): SF chuẩn của B cầm điện thoại áp tai, riêng tả B đang nói lại chính xác câu đó.
- *Với loa phát / lộ đoạn ghi âm / gọi vọng*: Video 1: shot nhân vật ngơ ngác nghe ngóng. Video 2: SF chuẩn của nhân vật đó đặc tả chính họ đang thốt ra câu thoại đó (cầm micro, đứng gọi từ xa, hoặc cảnh rò rỉ trong quá khứ lúc họ bị lén ghi âm, chuẩn theo cảm xúc lúc đó).



## 6. Continuity (không gian liên tục)

SF là khung đầu clip, nên phải lấy trạng thái kết thúc của clip liền trước.

- **Rà 4 trục liên tục**: Xa/gần · Trên/dưới (đứng/ngồi) · Trước/sau · tay cầm gì (đặc biệt các món có vai trò kịch bản).
- **Quy tắc trạng thái chờ (Pending State)**: nếu trong shot có hành động thay đổi trạng thái tĩnh (mở cửa, đứng lên, ngồi xuống, đưa đồ), khung đầu clip (SF) phải ở trạng thái chưa thực hiện. Luật đầy đủ khi viết prompt: `8-prompt-sf.md` §Trạng thái chờ.
- **Shot trước di chuyển**: trong prompt phải có đoạn kết clip (→ `11-prompt-video.md`), và SF của shot đó phải thấy rõ mặt người sắp di chuyển (không để họ quay lưng tiền cảnh).
- **Mối nối nhảy `zone` / `who`**: vá bằng một trong hai cách (Short không dùng nhịp lặng):
  1. Cho nhân vật vừa đi vừa nói (nếu nhịp phim cho phép), hoặc
  2. Tả bước di chuyển ngắn ở cuối prompt shot trước.

## 7. Kiểm tra cuối bước

**Đếm được — đếm trên bảng shot, ghi số ra rồi đối chiếu:**
- [ ] Mọi shot có `dur` là **10**.
- [ ] Không shot nào vượt **28 từ**.
- [ ] Không shot nào có giây thoại < 80% dur (dưới 24 từ).
- [ ] Cột "giây thoại" (từ ÷ 3.0) đã ghi ra cho từng shot.
- [ ] Số mã `sf` khác nhau **bằng đúng** tổng số shot — không shot nào dùng lại ảnh SF của shot khác (§1.1).
- [ ] Toàn cảnh dọc **10–20%** (và **đúng bằng số cụm**) · đặc tả **tối đa 1 shot** · cận/trung **50–60%** · góc đôi xếp lớp **20–30%**.
- [ ] Không khung nào vượt trần người rõ mặt của cỡ cảnh đó (§3.0 Hệ quả 2): CU 1 · MCU 1 · Stacked/OTS 2 · Medium Wide dọc 3 · Vertical Wide 4.
- [ ] Không dòng `goc` nào còn dùng thuật ngữ phim ngang (`Medium Two-Shot`, `Two-Shot ngang`, `3-4 Shot`) — §2.5.
- [ ] Solo Frame **25–40%** tổng số shot, **không quá 3 shot liên tiếp** (§3.3).
- [ ] Cụm có ≥3 main cast: **≥60%** SF đủ mặt cả nhóm · **≤20%** SF chỉ có 2 người.
- [ ] Mọi cặp SF cùng cụm & cùng chủ thể khác nhau ở **≥2 trục** (cỡ cảnh · trục máy ≥30° · hướng mắt/tư thế) — §1.1.

**Phải đọc mới thấy:**
- [ ] Diff text với kịch bản gốc: mọi câu chữ giữ nguyên vẹn, không tự ý lược bỏ.
- [ ] Người đang nói xuất hiện trong khung (rõ mặt hoặc vai/gáy OTS).
- [ ] Bộ góc máy đảm bảo luật **30° / 2 bậc** giữa các shot liền nhau.
- [ ] Không khung nào dàn người thành hàng ngang cùng mặt phẳng chiều sâu (§3.0 Hệ quả 3); thế so le đã có sẵn ở Master SF, không phải bịa lúc cắt cận.
- [ ] Mặt người đang nói cao **≥1/8 chiều cao khung** ở mọi shot có thoại, kể cả Vertical Wide (§3.0 Hệ quả 1).
- [ ] Mọi khung đã khai rõ đỉnh khung có gì và đáy khung có gì (§3.0 Hệ quả 4) — không khung nào bỏ trống cả hai đầu.
- [ ] Mọi Solo Frame: `pose.who` đúng một tên, không vai/gáy người khác, không main cast mờ ở lớp sau; hướng mắt khoá đúng phía đối phương đứng ở Master SF (§3.3).
- [ ] Không khung nào dùng low-angle chếch ngược lên mặt; khung có ý đồ áp đảo đã chèn câu chặn của `0-tu-duy-dien-anh.md` §II.3b.
- [ ] Rà 4 trục continuity giữa mọi cặp shot liền nhau: xa/gần · đứng/ngồi · trước/sau · tay cầm gì.
- [ ] Mọi mối nhảy `zone` / `who` đã vá bằng cách phù hợp.
