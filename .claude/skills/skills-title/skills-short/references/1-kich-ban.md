# 1 — Kịch bản gốc (`KICH-BAN.md`)

> **File này trả lời:** đọc và đối xử với kịch bản gốc thế nào.
> **Mở khi:** bắt đầu dự án, và mỗi lần kịch bản được cập nhật.
> **Không chứa:** cách dựng mảng `scenes` trong JSON (→ `2-du-lieu-sf-board.md`) ·
>   cách chia beat thành shot (→ `7-bang-shot.md`) ·
>   cách chọn góc máy theo tâm lý (→ `0-tu-duy-dien-anh.md`)

## 1. Vị trí và quyền hạn
- Mỗi dự án có **1 file `KICH-BAN.md`** (bản người đọc) nằm trong `<TEN_DU_AN>.project/`.
- **Tuyệt đối không tự ý sửa kịch bản gốc.** Không sửa đổi, thêm bớt, hay cắt gọt thoại của nhân vật. Mọi câu chữ phải được giữ nguyên vẹn 100% như kịch bản cung cấp.
- Chỉ cập nhật kịch bản khi user yêu cầu đích danh, và phải ghi lịch sử ở đầu file: ngày · scene · sửa gì · vì sao.
- **Short có thể được nối dài nhiều lượt**: user có quyền dán thêm đoạn tiếp nối ("làm thêm cho đoạn short đến hết đây") sau khi Short ban đầu đã dựng xong. Cộng dồn số từ cũ + đoạn mới rồi áp lại toàn bộ §2 từ đầu (kể cả khi đã vượt trần — xử lý ở §2.3).

## 2. Quét kịch bản để dựng Short
- **Luật 2 phút Short**: Bảng shot sản xuất của Short chỉ kéo dài **ĐÚNG 2 PHÚT (120 giây)**.

- **Xử lý khi user gửi kịch bản dài**: Dù user có cung cấp cả một kịch bản phim dài đầy đủ, kịch bản đó **chỉ dùng để lấy ngữ cảnh câu chuyện, bối cảnh địa điểm và dựng REF nhân vật chuẩn**. Phần phân rã bảng shot trong `sf-board.json` chỉ tập trung đúng đoạn Short.
- **Đối chiếu mọi Heading `##`**: bắt buộc quét các heading `##` nằm trong phân đoạn Short được chọn (như `## HOOK` hay `## SCENE 1`), tuyệt đối không bỏ lọt.

### 2.1 Tính thời lượng từ số chữ
- **Đếm số từ đoạn Short TRƯỚC khi dựng bất cứ thứ gì**.
- Công thức: **Số shot = ceil(số từ ÷ 26)**. Tổng thời lượng = **số shot × 10s**.
- Bắt buộc **báo user con số này trước khi dựng board**. Tuyệt đối không chia loãng cho đủ thời lượng.
- **Bảng tra**: 174 từ ≈ 7 clip ≈ 70s · 240 từ ≈ 9 clip ≈ 90s · 320 từ ≈ 12 clip ≈ 120s.

### 2.2 Chia câu vào từng clip — giữ đúng thứ tự, tách câu dài
- **Cấm đảo thứ tự Thoại/Narration**: kịch bản viết dòng nào trước thì dòng đó phải rơi vào clip trước (hoặc nửa đầu cùng clip). Ví dụ kịch bản viết *câu thoại* rồi mới đến *câu tả hành động/narration* thì trường `shot.text` và nội dung 2 shot con của video **bắt buộc giữ đúng thứ tự này** — tuyệt đối không tự ý đảo thành narration-trước-thoại-sau dù nghe "xuôi tai" hơn. Kiểm bằng cách đọc lại nguyên văn kịch bản theo đúng dòng, không suy diễn.
- **Câu một mình đã vượt trần 28 từ/clip** (VD: một câu tường thuật dài, không có hard-cut viết sẵn): tách làm nhiều clip liên tiếp, cắt tại chỗ ngắt tự nhiên của câu (dấu phẩy, dấu gạch ngang em dash, liên từ), giữ nguyên 100% từng chữ — không diễn giải lại. Khác với §4 (hard-cut *viết sẵn* trong kịch bản), đây là hard-cut *phát sinh* do giới hạn độ dài của một dòng duy nhất.

### 2.3 Khi tổng số từ vượt trần 120 giây
Cộng dồn Short cũ + đoạn nối thêm có thể vượt 12 shot/120s. Đây là luật **tuyệt đối**, không tự ý bỏ qua:
- **Bắt buộc báo user** con số vượt (bao nhiêu từ → bao nhiêu shot → vượt bao nhiêu giây) **trước khi dựng thêm bất cứ gì**.
- **Hỏi user chọn hướng xử lý** (không tự quyết): (a) vẫn dựng đủ, chấp nhận vượt trần, hoặc (b) nén/gộp bớt để vừa đúng 120s, hoặc (c) tách đoạn mới thành scene riêng (không tính vào Short). Nếu user xác nhận muốn vượt trần, tôn trọng quyết định đó và dựng đủ.

## 3. Thẻ Siêu dữ liệu Kịch bản (Metadata Tags)
Kịch bản có thể chứa các thẻ ngữ cảnh trong ngoặc vuông: `[SCENE CONTEXT]`, `[SCENE PURPOSE]`, `[INTENTION]`, `[BEAT]`, `[KNOWLEDGE]`, `[END STATE]`.

- Bắt buộc coi đây là lời diễn giải tâm lý/đạo diễn để sinh biểu cảm và nhịp phim chính xác.
- **Tuyệt đối không** coi các thẻ này là lời thoại, không cho nhân vật đọc lên, và không render chúng ra như chữ viết trên màn hình.
- Dùng chúng làm kim chỉ nam để:
  - Chọn góc máy (Ví dụ: `[INTENTION: warning]` → cần góc quay uy quyền/thấp).
  - Viết phần "biểu cảm" trong SF (Ví dụ: `[KNOWLEDGE: the child sees through her]` → biểu cảm của bé tinh ý, mẹ chột dạ).
  - Chia tách `[BEAT]` thành các shot con để tạo độ dồn dập và nhịp phim cảm xúc.

## 4. Kịch bản viết sẵn hard-cut trong 1 clip
Ví dụ: `0-5s: cảnh A, 5-10s: cắt cảnh B`.
- Bắt buộc phải tách thành 2 shot, 2 SF riêng biệt. Tuyệt đối không dựng hard-cut bên trong 1 clip video duy nhất.
- **Báo lại user** về việc tách.

## 5. Kiểm tra
- [ ] Số shot khớp công thức ceil(số từ ÷ 26); đã báo user tổng thời lượng trước khi dựng. Kịch bản dài (nếu có) chỉ dùng để lấy ngữ cảnh & nhân vật chuẩn.
- [ ] Vượt trần 120s (nếu có) đã báo số liệu cụ thể và để user chọn hướng xử lý, không tự quyết.
- [ ] Mọi heading `##` thuộc phân đoạn Short đều có scene tương ứng trong `sf-board.json`.
- [ ] Diff text với kịch bản gốc: mọi câu chữ giữ nguyên vẹn, không tự ý lược bỏ.
- [ ] Đối chiếu từng `shot.text` với kịch bản gốc: đúng thứ tự Thoại/Narration như văn bản gốc, không đảo chiều.
- [ ] Không có thẻ metadata nào lọt vào trường `prompt` hay bị đọc thành thoại.
