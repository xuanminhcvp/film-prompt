---
name: write-long-to-short-script
argument-hint: [kịch bản gốc] + [scene cần chuyển, vd "scene 2 với scene 3"]
description: Chuyển thể 1-2 cảnh từ kịch bản dài thành kịch bản short 2-3 phút (Reels/TikTok/YouTube Short) có metadata context. Dùng khi user dán kịch bản dài kèm yêu cầu kiểu "scene 2 với scene 3", "cắt cảnh này ra short", "chuyển thể cảnh X". Đầu ra là kịch bản có [SCENE CONTEXT], [SCENE PURPOSE], [END STATE], hook mở đầu và kết cliffhanger.
---

# Chuyển Thể Kịch Bản Từ Long Sang Short

> **MỤC TIÊU**: Chuyển thể 1 hoặc 2 phân cảnh cụ thể từ kịch bản gốc dài thành một video ngắn độc lập (thời lượng 2-3 phút), đảm bảo nội dung trọn vẹn và dễ hiểu.

## Nguyên tắc & Quy trình chuyển thể
1. **Tập trung vào 1-2 cảnh (Scene Focus)**: KHÔNG tóm tắt toàn bộ kịch bản gốc. Dựa trên yêu cầu của user, xác định 1-2 cảnh cốt lõi cần chuyển thể (hoặc tự chọn 1-2 cảnh kịch tính nhất).
2. **Cấu trúc lại cảnh (Restructuring)**: 
   - Đưa phân đoạn giật gân/thoại sốc nhất lên đầu làm Hook (3 giây đầu tiên).
   - Lược bỏ nhân vật phụ hoặc lời thoại không phục vụ xung đột chính.
   - **Giữ ranh giới cảnh gốc**: Mỗi cảnh một bộ metadata riêng — `[END STATE]` cảnh trước là đầu vào của `[SCENE CONTEXT]` cảnh sau. (Ví dụ: Giữ nguyên số gốc là SCENE 2, SCENE 3 nếu lấy từ bản gốc).
3. **Thoại lồng bối cảnh tự nhiên (Show, Don't Tell)**: 
   - Tuyệt đối **KHÔNG biến nhân vật thành người kể chuyện (exposition dump)**.
   - Chỉnh sửa lời thoại để nhân vật vô tình để lộ bối cảnh qua cảm xúc (tức giận, mỉa mai).
4. **Kết mở kích thích (Cliffhanger Ending)**: BẮT BUỘC đoạn kết của Short phải là một kết mở. Mượn từ bất kỳ cảnh sau nào trong bản gốc, miễn là không tiết lộ đáp án (VD: tiếng gõ cửa, một lời đề nghị, một nhân vật bí ẩn xuất hiện) để làm mồi nhử kéo view cho bản Long.
5. **Định dạng 4 khối**: Đầu ra BẮT BUỘC theo `references/dinh-dang-kich-ban.md`. KHÔNG dùng format của kịch bản gốc làm mẫu (vì gốc không có metadata, bản short thì bắt buộc có). Mỗi cảnh là một khối đủ 4 phần: Tiêu đề cảnh, `[SCENE CONTEXT]`, Lời thoại, `[END STATE]`. Thiếu một khối = chưa xong.
6. **Ngôn ngữ**: 
   - Giao tiếp với user bằng **Tiếng Việt**.
   - Kịch bản đầu ra giữ đúng ngôn ngữ gốc, ở mức **Global English B1-B2**: từ phổ thông, câu ngắn, không thành ngữ, không từ bóng bẩy. Phép thử: người không nói tiếng Anh bản ngữ đọc một lượt có hiểu ngay không?
   - Được phép viết lại thoại gốc cho đơn giản hơn — bản short không phải bản copy.
   - Không dùng dạng viết tắt (VD: dùng `do not` thay vì `don't`) — thoại phục vụ đọc/dịch/TTS.

## Checklist trước khi giao
- [ ] Đếm từ: chỉ đếm THOẠI + inline context, 300-500 từ. Metadata KHÔNG tính.
- [ ] Mỗi cảnh đủ 4 khối: tiêu đề · [SCENE CONTEXT] · thoại · [END STATE]
- [ ] Inline context: 3-7 lần/cảnh. Đếm thật. Quá 7 là đang viết truyện, không phải kịch bản.
- [ ] Không còn dấu ngoặc kép bọc thoại
- [ ] Câu thoại dài nhất dưới 25 từ
- [ ] Câu cuối cùng của cảnh cuối là câu HỎI hoặc câu bỏ lửng

## Tài liệu bắt buộc đọc
- `references/dinh-dang-kich-ban.md` — cấu trúc 4 khối metadata, luật chèn inline context, văn phong Simple English. **MỞ TRƯỚC KHI viết dòng thoại đầu tiên**, mọi lần.
- `references/ky-thuat-thoai-nhan-van.md` — ví dụ minh hoạ kỹ thuật viết thoại nhân văn. Mở khi cảnh cần chiều sâu cảm xúc. Chỉ học KỸ THUẬT, cấm mượn tình huống/nhân vật.
