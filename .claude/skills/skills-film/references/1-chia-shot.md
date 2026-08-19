# Bước 1 — Bảng shot và sinh SF 1:1

> **Nguồn sự thật duy nhất** cho việc nối shot, đếm thời lượng và logic không gian. Lập BẢNG SHOT trước khi sinh prompt.

## Mục lục
- [Luật Cốt Lõi: 1 Shot = 1 SF](#luật-cốt-lõi-1-shot--1-sf)
- [Quy tắc viết `goc`](#quy-tắc-viết-goc)
- [Góc Máy (Coverage)](#góc-máy-coverage)
- [Chia Thoại và Thời Lượng](#chia-thoại-và-thời-lượng)
- [Continuity (Không gian liên tục)](#continuity-không-gian-liên-tục)
- [Nhịp Không Thoại (Chuyển Cảnh)](#nhịp-không-thoại-chuyển-cảnh)
- [Tinh Chỉnh Thoại & Xử Lý Kịch Bản](#tinh-chỉnh-thoại--xử-lý-kịch-bản)
- [Kiểm tra cuối bước](#kiểm-tra-cuối-bước)

---

## Luật Cốt Lõi: 1 Shot = 1 SF
- **BẮT BUỘC**: Số SF = số shot. Tên SF = mã shot (VD: `SF-S1-07`).
- Shot cùng góc máy vẫn sinh hai SF khác nhau về biểu cảm/tay/câu đóng băng theo beat.
- Lập bảng shot trước (Mã shot | Thoại | Số từ | Giây | Góc | Có kết clip). Kiểm tra sạch bằng script RỒI mới sinh prompt ảnh.

## Quy tắc viết `goc`
Dòng `goc` trả lời câu hỏi "Khung này quay bằng góc gì, có ai, nét hay mờ?". Bắt buộc có cho mọi SF. Viết cùng lúc sinh SF ban đầu.
> **Lưu ý**: Dòng `goc` này sinh ra cùng SF, nhưng nó sẽ được dùng làm **tiêu chuẩn khung hình** cho Video Shot trên timeline.
1. **Nêu đích danh**, không đếm số lượng (VD: *"Everett trái + Warren phải, CẢ HAI RÕ MẶT"*).
2. **OTS phải nêu rõ VAI CỦA AI** làm tiền cảnh.
3. **Đúng tên nhân vật** như trong kịch bản.
4. **Khai cả người KHÔNG phải chủ thể** (đang ngồi im/ngủ trong `pose.who` cũng phải khai).
5. **Phải sử dụng đúng thuật ngữ cỡ cảnh/góc máy** (như Wide, CU, Two-Shot, Low Angle...) được quy định ở mục dưới. **KHÔNG** tả lồng bối cảnh, đạo cụ hay thông số kỹ thuật máy quay (tiêu cự 35mm, f/1.8) vào dòng này.
6. **TUYỆT ĐỐI CẤM khai báo nhân vật nền** (nền, quần chúng, khách nền, người đi đường). Dòng này **CHỈ** dành cho MAIN CAST. 

## Góc Máy (Coverage)
- **Tỷ lệ phân bổ (Cinematic Ratio)**: Khuyên dùng: ~50-60% Cận/Trung (CU/MCU) để bắt biểu cảm, 20-30% Góc đôi (Two-Shot/OTS) để giữ liên kết không gian, và 10 -15% cho Toàn cảnh (Wide) & Đặc tả (Insert), khung Single 1 người có thể có nhưng hạn chế (3-5%) để điều phối nhịp độ.
- **Góc rộng**: Chỉ dùng mở/khép/chuyển cảnh (1-2 góc/scene). KHÔNG gán thoại vào khung rộng.
- **Góc Đặc Tả (Insert/ECU)**: Rất hạn chế góc máy này. Dùng để đặc tả đồ vật, tay, mắt... nhằm chuyển nhịp hoặc che giấu raccord.
- **Góc cực đoan (High/Low/POV)**: Rất hạn chế, chỉ dùng có chủ đích (nhấn mạnh tâm lý, quyền lực, hoặc nhập vai).

### Phân rã đối thoại 2 người (Bộ góc tiêu chuẩn)
Để mô tả chính xác và đa dạng hơn trong dòng `goc` (cũng như prompt SF), ưu tiên sử dụng bộ thuật ngữ tiêu chuẩn sau:

**1. Khung Cơ Bản (Basic Frames)**
- **Master / Wide Two-Shot**: Toàn cảnh 2 người và không gian xung quanh. Dùng để mở/khép cảnh.
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
- **Wide Shot / Long Shot (Toàn cảnh)**: Thấy toàn bộ cơ thể và không gian xung quanh. Dùng để thiết lập bối cảnh, vị trí, khoảng cách giữa các nhân vật.
- **Full Shot / Medium Long Shot (Toàn thân)**: Thấy rõ toàn bộ cơ thể từ đầu đến chân. Dùng cho cảnh đối thoại di chuyển, hành động nhóm.
- **Medium Wide / 3-4 Shot (Nhìn gần)**: Cắt ngang từ đùi hoặc gối trở lên. Giữ được ngôn ngữ cơ thể và biểu cảm tương tác giữa các nhân vật.
- **Medium Shot / Waist Shot (Cắt ngang eo)**: Cắt ngang eo. Dùng nhiều trong hội thoại nhóm, tranh luận, tập trung vào tương tác và phản ứng.

**2. Nguyên tắc xử lý shot nhóm:**
- **Shot định vị**: BẮT BUỘC có ít nhất 1 góc rộng (Wide/Full/Medium Wide) ở đầu phân đoạn để khán giả nhận diện không gian và vị trí tương đối của nhóm.
- **Chia để trị (Sub-grouping)**: TUYỆT ĐỐI KHÔNG nhồi 3-4 người vào một khung hình Cận (CU/MCU). Khi hội thoại đi vào chi tiết, bắt buộc "chẻ" cụm đó ra thành các cặp Two-shot, OTS (A nói với B), hoặc Single (C đang nhìn).
- **Lọc Tham Chiếu (Cut-out)**: Với góc máy đã chẻ nhỏ, AI sinh ảnh BẮT BUỘC phải gạt bỏ những nhân vật không thuộc nón quan sát của góc máy đó.
- **Đám đông**: Không khai báo quần chúng/người đi đường vào dòng cấu trúc góc máy của main cast. Khung cảnh đông người chỉ được xử lý ở góc rộng toàn cảnh ban đầu.

## Tư duy chuyển góc máy (Sequence Logic)
- **Nguyên lý cốt lõi:** Không chuyển góc máy khi cảnh thay đổi vật lý. CHỈ chuyển góc khi nhận thức, quyền lực, thông tin hoặc cảm xúc thay đổi. Đừng nghĩ "Góc nào đẹp?", hãy nghĩ "Khán giả cần nhìn ai lúc này?".
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
- **Rà 5 trục liên tục**: Xa/gần, Trên/dưới (đứng/ngồi), Trước/sau, Trái/phải (trục 180°), **TAY CẦM GÌ** (đặc biệt các món có vai trò kịch bản).
- **Shot TRƯỚC di chuyển**: Trong prompt phải có đoạn KẾT CLIP, và SF của shot đó phải THẤY RÕ MẶT người sắp di chuyển (không để họ quay lưng tiền cảnh).
- **Mối nối nhảy `zone` / `who`**: Bắt buộc phải vá bằng MỘT TRONG BA CÁCH SAU (tùy ngữ cảnh): (1) Dùng một Shot CHUYỂN (Nhịp lặng), hoặc (2) Cho nhân vật vừa đi vừa nói (nếu nhịp phim cho phép), hoặc (3) Tả bước di chuyển ngắn ở CUỐI prompt shot trước.
- **Tối đa 3 mối chuyển/scene**. Đổi góc máy thì rẻ, nhưng bắt nhân vật đi lại đổi `zone` là đắt và dễ khựng.

## Nhịp Không Thoại (Nhịp Lặng & Chuyển Cảnh)
Nhịp không thoại CŨNG LÀ MỘT SHOT (SF). BẮT BUỘC phải sinh ra một dòng SF độc lập trong Bảng Shot cho mỗi nhịp lặng.
- **Tên Nhãn (Label)**: Phải gắn tag `[NHỊP]` hoặc `🎬 NHỊP LẶNG` vào tên nhãn.
- **Mã Shot (ID)**: BẮT BUỘC phải kết thúc bằng hậu tố `-B<số>` cho CẢ mã Shot Video và mã SF (Ví dụ: `V-S1-B1` và `SF-S1-B1`). Tuyệt đối không dùng số thứ tự thường (như `05`, `06`) cho nhịp lặng.
Rà mối nối giữa 2 scene VÀ các điểm rơi cảm xúc ở giữa cảnh.
1. **GIỮA CẢNH (Nhịp thở & Cao trào cảm xúc)**: Bắt buộc chèn vào giữa các chuỗi thoại dài để kéo dãn nhịp độ HOẶC làm nổi bật các điểm cảm xúc cao trào.
2. **MỞ CẢNH / TOÀN CẢNH**: Đầu scene sau (giới thiệu chỗ mới) hoặc Cuối scene trước. KHÁC địa điểm -> bắt buộc có nhịp lặng.
3. **CẦU NỐI**: Cuối cảnh trước/Đầu cảnh sau (nhảy thời gian/địa điểm).
- **Định mức**: Nhịp lặng chiếm khoảng **12%** tổng số shot của toàn phim. **Cho phép** xếp 2 cảnh không thoại liên tiếp nhau, thậm chí 3 cảnh liên tiếp ở 1-2 phân đoạn đặc biệt trong kịch bản để đẩy cảm xúc lên cao trào ( user sẽ ghép nhạc cho đoạn đó). Không bắt buộc phải luôn xen kẽ thoại.

## Xử Lý Kịch Bản
- **Tôn trọng kịch bản gốc**: TUYỆT ĐỐI KHÔNG tự ý sửa đổi, thêm bớt, hay cắt gọt thoại của nhân vật. Mọi câu chữ phải được giữ nguyên vẹn 100% như kịch bản cung cấp.
- **Kịch bản viết sẵn hard-cut trong 1 clip**: (Ví dụ: `0-5s: cảnh A, 5-10s: cắt cảnh B`). BẮT BUỘC phải tách thành 2 shot, 2 SF riêng biệt. Tuyệt đối không dựng hard-cut bên trong 1 clip video duy nhất. Báo lại user về việc tách.

## Kiểm tra cuối bước
- [ ] Chạy lệnh máy đếm: `kiem-luat.py` và `kiem-noi-shot.py` (pose continuity).
- [ ] Diff text với kịch bản gốc: Mọi câu chữ phải được giữ nguyên vẹn, không được tự ý lược bỏ.
- [ ] Người đang nói phải xuất hiện trong khung (rõ mặt hoặc vai/gáy OTS).
- [ ] Bộ góc máy đảm bảo luật 30° / 2 bậc giữa các shot liền nhau.
