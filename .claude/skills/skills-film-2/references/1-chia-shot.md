# Bước 1 — Bảng shot và sinh SF

> **Nguồn sự thật duy nhất** cho việc nối shot, đếm thời lượng và logic không gian. Lập BẢNG SHOT trước khi sinh prompt.

## Mục lục
- [Luật Cốt Lõi: Tạo và Tái sử dụng SF](#luật-cốt-lõi-tạo-và-tái-sử-dụng-sf)
- [Quy tắc viết `goc`](#quy-tắc-viết-goc)
- [Góc Máy (Coverage)](#góc-máy-coverage)
- [Chia Thoại và Thời Lượng](#chia-thoại-và-thời-lượng)
- [Continuity (Không gian liên tục)](#continuity-không-gian-liên-tục)
- [Nhịp Không Thoại (Chuyển Cảnh)](#nhịp-không-thoại-chuyển-cảnh)
- [Tinh Chỉnh Thoại & Xử Lý Kịch Bản](#tinh-chỉnh-thoại--xử-lý-kịch-bản)
- [Kiểm tra cuối bước](#kiểm-tra-cuối-bước)

---

## Quy trình 2 Giai đoạn bắt buộc

Thay vì lao ngay vào chia shot cơ học, Bước 1 được chia làm 2 giai đoạn để chống vỡ raccord vị trí (Blocking).

### GIAI ĐOẠN 1: PHÂN RÃ THẾ TRẬN (BLOCKING SHIFTS)
Trước khi chia shot, BẮT BUỘC đọc kịch bản để tìm các **"Điểm Khựng" (Blocking Shifts)** làm thay đổi cấu trúc không gian:
- Nhân vật mới bước vào/bỏ đi làm vỡ cấu trúc nhóm.
- Các nhân vật dắt nhau di chuyển sang một khu vực khác (VD: Từ Bàn thờ xuống Lối đi).
- Sự thay đổi từ trạng thái tĩnh sang động (VD: Đang ngồi thì đứng phắt dậy cãi nhau).

- ⚠️ **Cảnh báo dây chuyền từ Khung Gối Đầu**: Khung gối đầu nhìn sang cụm khác có thể kéo thêm Main Cast của cụm đó lọt vào nón quan sát, làm tăng số lượng nhân vật trong khung của scene. BẮT BUỘC chốt danh sách các khung gối đầu ngay ở giai đoạn này để:
  1. Rà soát tỷ lệ khung hình (định mức ≥60% SF có đủ cast và trần ≤20% khung 2 người).
  2. Kịp thời bổ sung ID của Scene hiện tại vào dòng `Dùng: S1 · S2...` trong trường `desc` của thẻ `REF_<TÊN>_FULL` của nhân vật lọt ở hậu cảnh (tránh bị script `kiem-luat.py` báo lỗi thiếu đính thẻ).

**Mỗi một Cụm Không Gian (Blocking Shift) BẮT BUỘC phải có một Master SF riêng để chốt vị trí.**
> **Ví dụ điển hình (Cảnh Đám Cưới ALTAR)**:
> - *Cụm 1 (Chờ đợi)*: Clara và Linh mục tại bàn thờ. -> **Cần Master 1**.
> - *Cụm 2 (Đối đầu)*: Ryan dắt Vanessa lên bàn thờ cãi nhau. Vị trí xáo trộn 180 độ. -> **Cần Master 2**.
> - *Cụm 3 (Đụng độ)*: Ryan và Vanessa quay lưng bỏ đi, đụng độ Adrian ngồi xe lăn ở lối đi giữa. Thế trận dịch chuyển 10 mét. -> **Cần Master 3**.

- ⚠️ **Cụm không gian KHÔNG trùng với scene**: Một cụm có thể vắt qua nhiều scene, và một scene có thể mở đầu bằng khung thuộc cụm của scene trước. Xác định cụm bằng câu hỏi *"máy đứng ở đâu, chĩa về đâu"* — TUYỆT ĐỐI KHÔNG xác định bằng *"shot này nằm ở scene nào"*.

### GIAI ĐOẠN 2: LẬP BẢNG SHOT CHI TIẾT (SHOT LIST)
Sau khi đã chốt danh sách các Cụm Không Gian và số lượng Master SF, mới bắt đầu điền các góc cận/trung cho từng câu thoại.
- **Thứ tự sắp xếp (Chronological Order)**: Toàn bộ các SF (dù là SF Nhịp (SF-B), Master SF, hay SF thường) BẮT BUỘC phải được sắp xếp trong scene theo **đúng thứ tự thời gian xuất hiện (thứ tự render video)** từ trên xuống dưới. Tuyệt đối không gom các Master SF lên trên đầu bảng.
- **Quy định Tái sử dụng SF (SF Reuse - BẮT BUỘC KHÔNG SINH TRÙNG LẶP)**:
  - Khi tạo shot mới, mặc định gán 1 mã SF tương ứng (`SF-S<scene>-<shot>`, VD: `SF-S1-07`).
  - **BẮT BUỘC DÙNG LẠI SF CŨ**: Áp cho cả ba nhóm:
    - (a) Cặp OTS / cận đơn khi đảo góc A-B-A-B;
    - (b) Khung TWO-SHOT — mỗi lần mạch thoại quay lại thế trận chung của hai người;
    - (c) Khung MASTER / rộng — mỗi lần cần tái lập không gian (ít hơn 2 nhóm trên).
  - **Mục tiêu tỷ lệ & Cân bằng THÀNH PHẦN**: Tái sử dụng SF đạt ~20–25% tổng số shot trong scene/dự án (ở các scene thoại đảo góc 2 người có thể đạt 30–40%). Ngoài tổng lượng, **PHẢI CÂN CẢ THÀNH PHẦN**: trong tổng số shot dùng lại, nhóm OTS + cận đơn **không quá 60%**, nhóm two-shot + master **ít nhất 40%**.
- Các shot cận (CU, OTS) của cụm nào BẮT BUỘC phải trỏ `refs.bg` về đúng **Master SF** của cụm đó.
- **Đánh dấu Khung Gối Đầu Hai Cụm (Ngay từ Giai đoạn 1–2)**: Khi phân rã thế trận, BẮT BUỘC phải phát hiện và đánh dấu các khung hình nhìn từ cụm này sang cụm kia trong không gian thông nhau. Mỗi khung này sẽ cần 2 tham chiếu bối cảnh (`refs.bg` trỏ Master SF chính của cụm chủ thể, `refs.chars` đính Master SF/Thẻ bối cảnh cụm xa làm neo thứ hai), do đó phải chừa sẵn slot REF bối cảnh phụ khi phân bổ thẻ tham chiếu nhân vật.
- Lập bảng shot trước (Mã shot | Thoại | Số từ | Giây | Góc | Có kết clip). Kiểm tra sạch bằng script RỒI mới sinh prompt ảnh.

## Quy tắc viết `goc`
Dòng `goc` trả lời câu hỏi "Khung này quay bằng góc gì, có ai, nét hay mờ?". Bắt buộc có cho mọi SF. Viết cùng lúc sinh SF ban đầu.
> **Lưu ý**: Dòng `goc` này sinh ra cùng SF, nhưng nó sẽ được dùng làm **tiêu chuẩn khung hình** cho Video Shot trên timeline.
1. **Nêu đích danh**, không đếm số lượng (VD: *"Everett trái + Warren phải, CẢ HAI RÕ MẶT"*).
2. **OTS phải nêu rõ VAI CỦA AI** làm tiền cảnh.
3. **Đúng tên nhân vật** như trong kịch bản.
4. **Khai cả người KHÔNG phải chủ thể** (đang ngồi im/ngủ trong `pose.who` cũng phải khai, kể cả MAIN CAST đang diễn ở CỤM KHÁC mà lọt vào lớp sau của khung gối đầu, dù họ ở rất xa và out nét).
5. **Phải sử dụng đúng thuật ngữ cỡ cảnh/góc máy** (như Wide, CU, Two-Shot, Low Angle...) được quy định ở mục dưới. **KHÔNG** tả lồng bối cảnh, đạo cụ hay thông số kỹ thuật máy quay (tiêu cự 35mm, f/1.8) vào dòng này.
6. **TUYỆT ĐỐI CẤM khai báo nhân vật nền** (nền, quần chúng, khách nền, người đi đường). Dòng này **CHỈ** dành cho MAIN CAST. 

## Góc Máy (Coverage)
- **Shot định vị (MASTER SF)**: Cứ mỗi cụm không gian (Blocking Shift), BẮT BUỘC phải có một **MASTER SHOT**. Khung này sẽ được sinh ra làm **MASTER SF**, đóng vai trò thiết lập toàn bộ không gian, ánh sáng, vị trí nhân vật chính và CHỐT MẬT ĐỘ quần chúng nền ban đầu của cụm đó. MASTER SF sẽ làm mốc tham chiếu (`refs.bg`) cho toàn bộ các SF con trong cụm. (Lưu ý: Quần chúng nền của Master SF **PHẢI tuân Nguyên lý 1 (Mật độ Sinh tồn)** — không gian công cộng KHÔNG được viết trống người chỉ vì lý do cảm xúc/đạo diễn).
  - **Quy định Cỡ Cảnh CỨNG (Shot Size)**: Ảnh SF dùng làm Master BẮT BUỘC phải là góc **Wide Shot** hoặc **Cinematic Wide Shot** (Góc Rộng / Toàn cảnh) để bao quát 70-100% không gian bối cảnh gốc. **TUYỆT ĐỐI CẤM** dùng các góc hẹp như Medium Shot, Medium Two-Shot, OTS, hay Close-up làm Master SF vì không đủ rộng để thiết lập không gian, khiến các SF con phía sau tham chiếu vào bị mất bối cảnh gốc.
  - **Lưu ý tối quan trọng về Master SF**: **TUYỆT ĐỐI KHÔNG DÙNG SF Nhịp (SF-B) LÀM MASTER**. Master SF phải là ảnh ĐẦU TIÊN chuẩn vị trí và tư thế của nhân vật trong CỤM ĐÓ. Ví dụ, nếu có 2 nhân vật đang đối thoại, Master SF phải là khung hình rộng đầu tiên lúc 2 người **đã ổn định vị trí ngồi/đứng nói chuyện**, chứ không phải là nhịp bước vào hay nhịp chờ.

- **Tỷ lệ phân bổ (Cinematic Ratio)**: Khuyên dùng: ~40-50% Cận/Trung (CU/MCU) để bắt biểu cảm, 20-30% Góc đôi (Two-Shot/OTS) để giữ liên kết không gian, **20–25%** cho Toàn cảnh/Góc rộng (Wide/Cinematic Wide), và **rất hạn chế ~2%** cho Góc Đặc Tả (Insert/ECU).
- **Góc rộng**: Dùng làm Master Shot mở cảnh, khép/chuyển cảnh, hoặc khung hình bao quát khi các nhân vật đối thoại nhóm/di chuyển trong bối cảnh khi thấy hợp lý.
- **Góc Đặc Tả (Insert/ECU)**: Rất hạn chế góc máy này (chỉ giữ mức **~2%** tổng số shot toàn kịch bản). Dùng để đặc tả đồ vật quan trọng, chi tiết tay, mắt... nhằm chuyển nhịp hoặc che giấu raccord. **Đặc tả/Insert đạo cụ BẮT BUỘC phải là một shot độc lập (có mã SF riêng), tuyệt đối không được dùng hard-cut (khối hai đoạn) để cắt sang đặc tả.**
- **Góc cực đoan (High/Low/POV)**: Rất hạn chế, chỉ dùng có chủ đích (nhấn mạnh tâm lý, quyền lực, hoặc nhập vai).

### Phân rã đối thoại 2 người (Bộ góc tiêu chuẩn)
Để mô tả chính xác và đa dạng hơn trong dòng `goc` (cũng như prompt SF), ưu tiên sử dụng bộ thuật ngữ tiêu chuẩn sau:

**1. Khung Cơ Bản (Basic Frames)**
- **Master / Wide Two-Shot**: Toàn cảnh 2 người và không gian xung quanh. Dùng để thiết lập không gian và làm Master SF.
- **Medium Two-Shot**: Khung trung, thấy rõ cả hai khi trò chuyện.
- **Tight Two-Shot**: Khung gần, nhấn mạnh cảm xúc của 2 người.
- **Two-Shot ngang**: Hai người ngồi hoặc đứng cạnh nhau, cùng nhìn về trước.
- **Profile Two-Shot**: Hai người đối diện nhau, quay ngang 90°.
- **3/4 Two-Shot**: Máy đặt góc chéo để thấy mặt/phản ứng của cả hai.

**2. Góc Hội Thoại (Dialogue Coverage)**
- **Clean Two-Shot**: Cả hai cùng rõ mặt trong một khung hội thoại.
- **OTS A → B / OTS B → A (Qua vai)**: Qua vai người này để nhìn người kia đang nói/phản ứng. 
- **Dirty Single**: Cận 1 người, có một phần vai hoặc đầu của người kia lọt vào tiền cảnh.
- **Clean Single**: Cận 1 người hoàn toàn, không vướng vai/đầu người kia.
- **Shared Reaction Two-Shot**: Giữ cả hai trong khung để bắt phản ứng cùng lúc.

**3. Góc Cao, Thấp & Góc Nhìn**
- **Eye-Level**: Máy ngang tầm mắt, cảm giác tự nhiên (Mặc định).
- **High-Angle / Low-Angle**: Nhìn xuống (nhân vật nhỏ bé/yếu thế) hoặc Nhìn lên (tăng cảm giác quyền lực/căng thẳng).
- **Overhead / Top Shot**: Nhìn gần như từ trên đỉnh xuống để thấy vị trí.
- **Rear Two-Shot / Back-to-Back**: Nhìn từ sau lưng cả hai / Hai người quay lưng nhau (nhấn mạnh sự chia rẽ/lạnh nhạt).

### Phân rã đối thoại >2 người & Đám đông
Để thiết lập không gian ban đầu cho nhóm 3-4 người, sử dụng các chuẩn khung hình sau trước khi cắt cận:

**1. Khung cơ bản cho 3-4 người:**
- **Wide Shot / Long Shot (Toàn cảnh)**: Thấy toàn bộ cơ thể và không gian xung quanh. Dùng để thiết lập bối cảnh (Làm Master SF), vị trí, khoảng cách giữa các nhân vật.
- **Full Shot / Medium Long Shot (Toàn thân)**: Thấy rõ toàn bộ cơ thể từ đầu đến chân. Dùng cho cảnh đối thoại di chuyển, hành động nhóm.
- **Medium Wide / 3-4 Shot (Nhìn gần)**: Cắt ngang từ đùi hoặc gối trở lên. Giữ được ngôn ngữ cơ thể và biểu cảm tương tác giữa các nhân vật.
- **Medium Shot / Waist Shot (Cắt ngang eo)**: Cắt ngang eo. Dùng nhiều trong hội thoại nhóm, tranh luận, tập trung vào tương tác và phản ứng.

**2. Nguyên tắc xử lý shot nhóm:**
- **Shot định vị**: BẮT BUỘC có ít nhất 1 góc rộng (Wide/Full/Medium Wide) ở đầu phân đoạn để sinh Master SF, giúp khán giả nhận diện không gian và vị trí tương đối của nhóm.
- **Chia để trị (Sub-grouping)**: KHÔNG chẻ bằng cách xoá người. Khán giả không được mất dấu ai giữa một cuộc đối chất. TUYỆT ĐỐI KHÔNG nhồi 3-4 người cùng nét, cùng cỡ mặt vào một khung CẬN (CU/MCU). Để giữ đủ mặt nhóm 3-4 người, có 2 cách:
  - *(Cách 1)* Dùng góc Toàn hoặc góc Trung (Wide/Medium) để tất cả đều rõ mặt trong khung.
  - *(Cách 2)* Nếu dùng góc Cận/Hẹp, phải chẻ bằng ĐỘ NÉT (phân lớp chiều sâu): chủ thể chính NÉT ở giữa, người thứ hai làm vai/gáy tiền cảnh out nét, người thứ ba đứng lùi mờ ở lớp sau (LƯU Ý: CHỈ áp dụng *"lớp sau"* nếu nhân vật thứ 3 vốn dĩ ĐANG ĐỨNG PHÍA SAU theo chiều sâu vật lý ở Master SF; tuyệt đối KHÔNG gán *"lớp sau"* cho nhân vật đứng ngang hàng làm vỡ raccord vị trí).
  - **Định mức cho scene có ≥3 main cast**: 50% số SF phải có ĐỦ mặt cả nhóm hoặc lớn hơn 3 người; số còn lại cho phép có 2 người hoặc 1 người.
  - **Lọc Tham Chiếu (Cut-out)**: Chỉ gạt khỏi `refs.chars` những nhân vật KHÔNG CÓ MẶT VẬT LÝ trong không gian đó, hoặc đứng sau lưng máy quay. Người đang ở trong phòng mà nằm trong nón quan sát thì PHẢI có ref — kể cả khi họ chỉ là vai/gáy tiền cảnh hay một dáng mờ ở lớp sau. Gạt một người đang đứng ngay đó là bắt model dựng lại căn phòng thiếu họ.
- **Đám đông**: Không khai báo quần chúng/người đi đường vào dòng cấu trúc góc máy của main cast. Khung cảnh đông người được xử lý và khóa cứng ở góc rộng toàn cảnh ban đầu (Master SF).

## Tư duy chuyển góc máy (Sequence Logic)
- **Nguyên lý cốt lõi:** Không chuyển góc máy khi cảnh thay đổi vật lý. CHỈ chuyển góc khi nhận thức, quyền lực, thông tin hoặc cảm xúc thay đổi. Đừng nghĩ "Góc nào đẹp?", hãy nghĩ "Khán giả cần nhìn ai lúc này?".
- Mọi điểm đặt camera PHẢI tuân theo vị trí không gian đã chốt ở Master SF. Bắt buộc tư duy theo trình tự: **Đặt máy quay ở đâu? -> Hướng máy chĩa về đâu? -> Từ đó suy ra nón quan sát quét trúng ai và Background phía sau họ là gì.** Nếu không chốt được điểm đặt máy, AI sẽ làm nhân vật và bối cảnh nhảy vị trí lung tung.
- **Tư duy theo Beat tâm lý:** Lập danh sách shot dựa trên diễn biến câu chuyện thay vì liệt kê cơ học.
- **Công thức nhịp điệu (Drama Flow):** 
  - `Wide` (Thiết lập) → `Two-Shot` (Quan hệ) → `OTS` (Xung đột) → `Low Angle` (Người áp đảo) → `Close-up` (Tổn thương/Twist) → `Wide` (Thực tại mới).
- **Tham khảo trọn vẹn triết lý:** [6-tu-duy-dien-anh.md](6-tu-duy-dien-anh.md)

## Chia Thoại và Thời Lượng
- **Cắt theo phản ứng**: Shot cắt sang mặt người nghe khi phản ứng của họ là nội dung chính.
- **Lấp kín thời lượng**: ~90% shot dài 10s (chứa 2-4 lượt thoại qua lại). 10s cần 21-30 từ. 6s (12-18 từ) dùng cho câu ngắn/nhịp chuyển. Chừa dư tối đa 3s.
- **Xử lý Thoại O.S (Điện thoại / Loa / Gọi vọng)**: AI sinh video tự cấp giọng O.S rất tệ. Ta phải mồi một "bản sao" có người thật đứng nói để lấy chuẩn Voice.
  - *Với Gọi Điện Thoại*: Ví dụ lặp câu thoại của B 2 lần. Video 1: A nói, B nói off-screen (Giữ O.S y như kịch bản gốc để tạo nhịp diễn/thời lượng). Video 2 ngay dưới (Bản sao): SF ( SF chuẩn của B cầm điện thoại áp tai) riêng tả B đang NÓI LẠI CHÍNH XÁC CÂU ĐÓ.
  - *Với Loa phát / Lộ đoạn ghi âm / Gọi vọng*: Video 1: Nhịp không thoại kịch câm (Đám đông/ nhân vật ngơ ngác nghe ngóng/ cảm xúc lúc đó, KHÔNG ai nói O.S). Video 2: SF ( SF của chuẩn nhân vật đó nói) đặc tả chính nhân vật đang thốt ra câu thoại đó (Có thể là cảnh họ cầm micro, đứng gọi từ xa, hoặc cảnh rò rỉ trong quá khứ lúc họ bị lén ghi âm, chuẩn theo cảm xúc nói đúng lúc đó).
- **Chuyển động**: Cộng thêm 2-3s (hoặc hơn) vào thời lượng shot nếu có di chuyển, đứng/ngồi, đi khỏi khung.

## Continuity (Không gian liên tục)
SF là KHUNG ĐẦU clip, nên phải lấy TRẠNG THÁI KẾT THÚC của clip liền trước.
- **Quy tắc TRẠNG THÁI CHỜ (Pending State)**: Nếu trong shot có hành động thay đổi trạng thái tĩnh (mở cửa, đứng lên, ngồi xuống, đưa đồ), KHUNG ĐẦU clip (SF) phải ở trạng thái CHƯA THỰC HIỆN.
- **Rà 4 trục liên tục**: Xa/gần, Trên/dưới (đứng/ngồi), Trước/sau, **TAY CẦM GÌ** (đặc biệt các món có vai trò kịch bản).
- **Shot TRƯỚC di chuyển**: Trong prompt phải có đoạn KẾT CLIP, và SF của shot đó phải THẤY RÕ MẶT người sắp di chuyển (không để họ quay lưng tiền cảnh).
- **Mối nối nhảy `zone` / `who`**: Bắt buộc phải vá bằng MỘT TRONG BA CÁCH SAU (tùy ngữ cảnh): (1) Dùng một Shot CHUYỂN (Nhịp lặng), hoặc (2) Cho nhân vật vừa đi vừa nói (nếu nhịp phim cho phép), hoặc (3) Tả bước di chuyển ngắn ở CUỐI prompt shot trước.

## Nhịp Không Thoại (Nhịp Lặng & Chuyển Cảnh)
Nhịp không thoại CŨNG LÀ MỘT SHOT (SF). BẮT BUỘC phải sinh ra một dòng SF độc lập trong Bảng Shot cho mỗi nhịp lặng.
- **Tên Nhãn (Label)**: Phải gắn tag `[NHỊP]` hoặc `🎬 NHỊP LẶNG` vào tên nhãn.
- **Mã Shot (ID)**: BẮT BUỘC phải kết thúc bằng hậu tố `-B<số>` cho CẢ mã Shot Video và mã SF (Ví dụ: `V-S1-B1` và `SF-S1-B1`). Tuyệt đối không dùng số thứ tự thường (như `05`, `06`) cho nhịp lặng.
Rà mối nối giữa 2 scene VÀ các điểm rơi cảm xúc ở giữa cảnh.
1. **GIỮA CẢNH (Nhịp thở & Cao trào cảm xúc)**: Bắt buộc chèn vào giữa các chuỗi thoại dài để kéo dãn nhịp độ HOẶC làm nổi bật các điểm cảm xúc cao trào.
2. **MỞ CẢNH / TOÀN CẢNH**: Đầu scene sau (giới thiệu chỗ mới) hoặc Cuối scene trước. KHÁC địa điểm -> bắt buộc có nhịp lặng.
3. **CẦU NỐI**: Cuối cảnh trước/Đầu cảnh sau (nhảy thời gian/địa điểm).
- **Nhịp chuyển trỏ REF theo CỤM NÓ ĐỨNG, không theo scene chứa nó**: Nhịp bắc cầu A→B đứng ở đầu nào thì neo master đầu ấy: quay cảnh ở cụm cũ thì neo master cụm cũ (kể cả master ấy nằm ở scene trước), quay cảnh ở cụm mới thì neo master cụm mới (kể cả master ấy xuất hiện sau nó trong mạch shot).
- **Định mức**: Nhịp lặng chiếm khoảng **12%** tổng số shot của toàn phim. **Cho phép** xếp 2 cảnh không thoại liên tiếp nhau, thậm chí 3 cảnh liên tiếp ở 1-2 phân đoạn đặc biệt trong kịch bản để đẩy cảm xúc lên cao trào ( user sẽ ghép nhạc cho đoạn đó). Không bắt buộc phải luôn xen kẽ thoại.

## Xử Lý Kịch Bản
- **Tôn trọng kịch bản gốc**: TUYỆT ĐỐI KHÔNG tự ý sửa đổi, thêm bớt, hay cắt gọt thoại của nhân vật. Mọi câu chữ phải được giữ nguyên vẹn 100% như kịch bản cung cấp.
- **Kịch bản viết sẵn hard-cut trong 1 clip**: (Ví dụ: `0-5s: cảnh A, 5-10s: cắt cảnh B`). BẮT BUỘC phải tách thành 2 shot, 2 SF riêng biệt. Tuyệt đối không dựng hard-cut bên trong 1 clip video duy nhất. Báo lại user về việc tách.
- **Thẻ Siêu dữ liệu Kịch bản (Metadata Tags)**: Bỏ qua và **TUYỆT ĐỐI KHÔNG** coi các thẻ ngữ cảnh có định dạng ngoặc vuông (như `[SCENE CONTEXT]`, `[INTENTION]`, `[BEAT]`, `[KNOWLEDGE]`) là lời thoại của nhân vật. Thay vào đó, dùng chúng làm kim chỉ nam để:
  - Chọn góc máy (Ví dụ: `[INTENTION: warning]` -> cần góc quay uy quyền/thấp).
  - Viết phần "BIỂU CẢM" trong SF (Ví dụ: `[KNOWLEDGE: the child sees through her]` -> biểu cảm của bé tinh ý, mẹ chột dạ).
  - Chia tách `[BEAT]` thành các shot con hoặc nhịp lặng (Nhịp Không Thoại) để tạo độ giãn cho mạch cảm xúc.

## Kiểm tra cuối bước
- [ ] Chạy lệnh máy đếm: `kiem-luat.py` và `kiem-noi-shot.py` (pose continuity).
- [ ] Diff text với kịch bản gốc: Mọi câu chữ phải được giữ nguyên vẹn, không được tự ý lược bỏ.
- [ ] Người đang nói phải xuất hiện trong khung (rõ mặt hoặc vai/gáy OTS).
- [ ] Bộ góc máy đảm bảo luật 30° / 2 bậc giữa các shot liền nhau.
