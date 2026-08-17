# Thao tác chạy ảnh ChatGPT 

> **Chỉ dẫn cách chạy tool render ảnh**. Chạy 1 hoặc Tích chọn các SF trên giao diện

## Mục lục
- [Quy trình tạo ảnh Giao diện (Stateless)](#quy-trình-tạo-ảnh-giao-diện-stateless)
- [Cấu trúc LUẬT CHUNG (6 khối)](#cấu-trúc-luật-chung-6-khối)
- [Cấu trúc Prompt Ảnh (6 phần)](#cấu-trúc-prompt-ảnh-6-phần)
- [Giới hạn ký tự (Trần)](#giới-hạn-ký-tự-trần)
- [Hai lệnh tự động từ Board](#hai-lệnh-tự-động-từ-board)

---

## Quy trình tạo ảnh Giao diện (Stateless)
- **Tích chọn trên UI**: Người dùng tự do tích chọn các SF muốn tạo ảnh trên giao diện (khuyến nghị tích các SF chung một thẻ địa điểm để bối cảnh nhất quán) hoặc tích tạo ảnh riêng trong từng SF.
- **Chạy tự động**: Khi bấm tạo, hệ thống sẽ gom toàn bộ các SF vừa tích thành một cụm chạy (request) duy nhất.
- **Phiên chat trắng (Stateless)**: Hệ thống tự động đẩy gói dữ liệu gồm ảnh Bối cảnh, ảnh Chân dung (`PORTRAIT` và `FULL`), và Luật chung vào một phiên chat trắng hoàn toàn mới.
- **Gọi tên thật**: Không dùng mã số (`MAYA`, `HAI TÚI VẢI` - Tuyệt đối không dùng `NGƯỜI 1`, `ĐỒ 2`).

## Cấu trúc LUẬT CHUNG (6 khối)
Nằm ở trường `luatchung` của thẻ địa điểm. Được gửi 1 lần duy nhất.
1. **Khung & Chất ảnh**: Tỉ lệ, chất ảnh, luật chữ thật.
2. **Ảnh đính kèm**: Ảnh nào là mặt của ai, đồ của ai.
3. **Nhân vật**: Mỗi người 1 đoạn, gọi bằng TÊN THẬT, tả 1 lần.
4. **Đạo cụ & Nơi chốn**: Gọi bằng tên thật.
5. **Trục**: Máy quay phía nào, ai luôn bên trái, ai phải (Không bao giờ đảo chiều).
6. **Liên tục**: Trạng thái đạo cụ theo dòng thời gian (vd: *S3 đóng -> S10 mở*).

## Cấu trúc Prompt Ảnh (7 phần)
MỌI prompt ảnh (cả thẻ địa điểm và SF thường) chỉ còn đúng 7 phần:
1. **Máy quay** (bằng thông số đo cụ thể)
2. **Trạng thái không gian của cụm** (nhưng chỉ tả những gì lọt vào nón quan sát của góc máy)
3. **Ai đang làm gì**
4. **Bàn tay** (Tuỳ chọn: chỉ tả nếu có hành động cầm nắm cụ thể hoặc tay có vai trò diễn xuất quan trọng trong shot; đừng lúc nào cũng dùng không sẽ lố/ diễn.)
5. **Hướng nhìn**
6. **Biểu cảm khoảnh khắc**
7. **Câu đóng băng** cuối khung (trạng thái TRƯỚC khi hành động).

## Giới hạn ký tự (Trần)
- **Thẻ địa điểm**: `1.400 - 1.800 ký tự` (Dài hơn vì phải khai BẢN ĐỒ VỊ TRÍ % và biểu cảm của nhiều người).
- **SF thường**: `< 1.000 ký tự` (Đã có bố cục từ thẻ địa điểm, chỉ khai phần thay đổi).
- **LUẬT CHUNG**: `3.000 - 4.500 ký tự` (Khai 1 lần cho mỗi địa điểm).
- **Ngoại lệ 2 vùng tương phản**: (ví dụ: phố nghèo giáp nhà giàu, trong nhà nhìn ra sân). Prompt `~2.000` / LUẬT CHUNG `6.000 - 7.000` do phải tả 2 lần nội thất, ánh sáng, màu sắc cho mỗi bên ranh giới.

## Hai lệnh tự động từ Board
*(Board tự động thêm vào prompt gửi đi, người dùng KHÔNG viết tay)*
1. **Mở khóa hướng máy**: Model thường bám hướng của thẻ địa điểm. Muốn đổi hướng -> Bắt buộc phải viết số máy quay cụ thể vào prompt.
