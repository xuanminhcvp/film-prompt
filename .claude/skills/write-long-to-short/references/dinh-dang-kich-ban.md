# Định dạng & Văn phong Kịch bản

## Cấu trúc Cảnh (Scene Structure)
Kịch bản là sự kết hợp giữa **Thoại (90%)** và **Ngữ cảnh siêu dữ liệu (Metadata Context - 10%)** để AI có thể giữ được logic của câu chuyện qua nhiều cảnh. 
Mỗi cảnh phải tuân thủ cấu trúc sau:

**A. Tiêu đề Cảnh:** Viết in hoa.
`SCENE [SỐ THỨ TỰ]: [TÊN ĐỊA ĐIỂM]`

**B. Ngữ cảnh Đầu Cảnh (ĐỂ GIỮ LOGIC CHO AI):**
Ngay sau tiêu đề, BẮT BUỘC cung cấp 2 khối thông tin (chỉ dài khoảng 3-8 dòng):
- `[SCENE CONTEXT]`: Thời gian, trạng thái của nhân vật (ai biết gì, chưa biết gì, cảm xúc thế nào). Đặc biệt chú trọng vào **Knowledge State** (Trạng thái nhận thức - ai biết gì, hiểu gì).
- `[SCENE PURPOSE]`: Mục đích của cảnh này là gì (Ví dụ: Chuyển biến cảm xúc, hé lộ bí mật).

**C. Lời thoại (Dialogue):**
- Tên nhân vật viết IN HOA, theo sau là dấu hai chấm `:`. Lời thoại viết liền sau đó, không dùng dấu ngoặc kép.
- **Inline Context (Ngữ cảnh chèn giữa thoại)**: CHỈ CHÈN KHI CÓ SỰ THAY ĐỔI VỀ TRẠNG THÁI (State Change). Đặt trong ngoặc vuông `[...]`. 
  - KHÔNG chèn sau mỗi câu. Chỉ chèn khoảng 3-7 lần trong một cảnh dài (20-30 câu thoại).
  - Ưu tiên các loại thay đổi sau (theo thứ tự quan trọng giảm dần):
    1. **Knowledge/Misunderstanding**: Sự hiểu lầm, ai đó vừa nhận ra điều gì (Rất quan trọng cho AI).
    2. **Intention**: Ý định thật sự ẩn sau câu thoại (Subtext).
    3. **Beat/Turn**: Sự thay đổi cảm xúc, quyết định bước ngoặt.
    4. **Spatial State / Physical Movement**: Dịch chuyển vị trí, không gian (ví dụ: ngồi xuống, đứng lên, tiến lại gần, quay lưng bỏ đi). Những hành động này làm thay đổi động lực (dynamic) và vị thế của các nhân vật trong cảnh.
    5. **Action/Reaction**: Hành động vật lý hoặc phản ứng khác (chỉ ghi khi sự việc quan trọng và không thể tự suy ra từ thoại).
  - *Lưu ý*: Không ghi các biểu cảm/hành động hiển nhiên (ví dụ như `[cô ấy nói một cách tức giận]` sau một câu chửi).

**D. Trạng thái Cuối Cảnh:**
- `[END STATE]`: 1-3 dòng chốt lại tình thế cuối cảnh đã thay đổi thế nào so với đầu cảnh (ai đã biết thêm điều gì, quyết định gì mới được đưa ra). Điều này cực kỳ quan trọng để làm đầu vào (anchor) cho cảnh tiếp theo.


## Văn phong Nhân văn (Humanistic Tone)
- **Từ vựng cực kỳ phổ thông (Simple English)**: BẮT BUỘC sử dụng tiếng Anh toàn cầu (Global English) ở mức độ dễ hiểu (tương đương B1-B2). TUYỆT ĐỐI KHÔNG dùng từ vựng bóng bẩy, thành ngữ phức tạp hay thuật ngữ chuyên ngành. Lời thoại phải mang tính đại chúng, trực diện.
- **Giọng điệu chân thật, không sến**: Nhân vật nói như người thật nói — ngắn gọn, đôi khi vụng về, đôi khi không nói hết ý. Tránh câu thoại quá hoàn hảo hoặc quá triết lý. Khoảnh khắc cảm động nhất thường đến từ câu nói giản dị nhất.
- **Văn phong phục vụ nhân vật**: Mỗi nhân vật có cách nói riêng phản ánh hoàn cảnh và tính cách.
- **Kỹ thuật nhịp điệu**: Câu ngắn cắt nhau trong những lúc căng thẳng. Câu dài hơn, nhịp chậm trong khoảnh khắc sâu lắng. Kỹ thuật ngắt lời (dấu gạch ngang `-`) tạo cảm giác đời thực.
