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

## 2. Quét kịch bản để dựng scene
- **Đối chiếu mọi Heading `##`**: bắt buộc quét mọi heading `##` trong `KICH-BAN.md`, kể cả các mục không mang tiền tố `SCENE` (như `## HOOK` hay `## SCENE 0`). Mục nào chỉ định phân đoạn thì bắt buộc phải dựng đúng scene tương ứng (như `HOOK` hoặc `S0`) trong `sf-board.json`, tuyệt đối không bỏ lọt.

## 3. Thẻ Siêu dữ liệu Kịch bản (Metadata Tags)
Kịch bản có thể chứa các thẻ ngữ cảnh trong ngoặc vuông: `[SCENE CONTEXT]`, `[SCENE PURPOSE]`, `[INTENTION]`, `[BEAT]`, `[KNOWLEDGE]`, `[END STATE]`.

- Bắt buộc coi đây là lời diễn giải tâm lý/đạo diễn để sinh biểu cảm và nhịp phim chính xác.
- **Tuyệt đối không** coi các thẻ này là lời thoại, không cho nhân vật đọc lên, và không render chúng ra như chữ viết trên màn hình.
- Dùng chúng làm kim chỉ nam để:
  - Chọn góc máy (Ví dụ: `[INTENTION: warning]` → cần góc quay uy quyền/thấp).
  - Viết phần "biểu cảm" trong SF (Ví dụ: `[KNOWLEDGE: the child sees through her]` → biểu cảm của bé tinh ý, mẹ chột dạ).
  - Chia tách `[BEAT]` thành các shot con hoặc nhịp lặng để tạo độ giãn cho mạch cảm xúc.

## 4. Kịch bản viết sẵn hard-cut trong 1 clip
Ví dụ: `0-5s: cảnh A, 5-10s: cắt cảnh B`.
- Bắt buộc phải tách thành 2 shot, 2 SF riêng biệt. Tuyệt đối không dựng hard-cut bên trong 1 clip video duy nhất.
- **Báo lại user** về việc tách.

## 5. Kiểm tra
- [ ] Mọi heading `##` của kịch bản đều có scene tương ứng trong `sf-board.json`.
- [ ] Diff text với kịch bản gốc: mọi câu chữ giữ nguyên vẹn, không tự ý lược bỏ.
- [ ] Không có thẻ metadata nào lọt vào trường `prompt` hay bị đọc thành thoại.
