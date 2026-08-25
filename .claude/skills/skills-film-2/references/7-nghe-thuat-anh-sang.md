# Tiêu chuẩn Chất ảnh, Màu sắc & Ánh sáng Điện ảnh

> Khác biệt lớn nhất giữa một khung hình AI nhòe nhoẹt, giả tạo và một shot phim điện ảnh thực thụ nằm ở **Sự hiện thực có chủ đích**. File này trang bị cho AI hệ thống quy tắc để viết prompt về Chất ảnh, Màu sắc và Ánh sáng khi khởi tạo Thẻ Địa Điểm (`refs.bg`).

## ⚠️ PHẠM VI ÁP DỤNG (SCOPE) - BẮT BUỘC ĐỌC
1. **CHỈ DÙNG CHO BỐI CẢNH (Thẻ Địa Điểm):** Mọi kỹ thuật ánh sáng, màu sắc trong file này CHỈ được phép áp dụng khi tạo Prompt cho **Thẻ Địa Điểm (`REF_BG`)**.
2. **CẤM DÙNG CHO NHÂN VẬT:** Tuyệt đối KHÔNG áp dụng đánh sáng điện ảnh (đổ bóng gắt, tối, tương phản cao) vào Thẻ Nhân Vật (Portrait / Full-body). Ảnh REF nhân vật bắt buộc phải dùng ánh sáng studio dịu nhẹ, đều, phẳng để lấy nét rõ khuôn mặt.
3. **CẤM VIẾT LẠI VÀO SHOT LẺ (SF):** Khi tạo các khung hình SF lẻ (S1, S2...), KHÔNG được nhét lại từ khóa ánh sáng/màu sắc vào prompt. SF lẻ sẽ tự động kế thừa (inherit) ánh sáng từ Thẻ Địa Điểm. Tả lại sẽ làm đè (override) Look gốc.

---

Thay vì sử dụng các từ khóa "Cinematic lighting", "Moody", "Low-key" một cách sáo rỗng và cường điệu hóa khiến AI vẽ bẹp ảnh hoặc làm lố, hãy sử dụng ngôn ngữ miêu tả mang tính **HIỆN THỰC ĐIỆN ẢNH**. Dưới đây là 3 trụ cột bắt buộc:

## 1. Chất ảnh (Image Quality)
- **Từ khoá cốt lõi:** Bắt đầu phần miêu tả bằng `photorealistic`, `điện ảnh nhưng hiện thực` (Cinematic but realistic). Luôn kết hợp định hình cỡ cảnh và tiêu cự ống kính rõ ràng (VD: `cinematic wide shot, ống kính 28mm, camera ngang tầm mắt`).
- **Nói KHÔNG với cường điệu hóa:** Tránh lạm dụng các từ khóa làm gắt hình ảnh nếu không đúng thể loại hoặc hoàn cảnh. 
  - Nếu bối cảnh là phòng bình thường, bệnh viện hoặc nơi sáng sủa, BẮT BUỘC dùng các lệnh phanh: `không u tối, không moody, không low-key, không cháy trắng`.
- **Kiểm soát Bóng & Độ Tương Phản:** Quy định rõ tính chất vật lý của bóng đổ và độ tương phản thay vì nói bóng gió. 
  - VD: `độ tương phản trung bình, bóng đổ mềm` (cho phòng sáng), hoặc `đổ bóng dài trên sân và bậc thềm` (cho nắng xiên chiều).

## 2. Màu sắc (Color Palette)
- **Màu sắc phải neo vào Vật liệu (Set Dressing):** Đừng chỉ miêu tả màu của "không khí" (grading). Hãy gắn màu sắc vào chất liệu nội thất/vật dụng cụ thể để AI không tô màu cả bức ảnh thành 1 mảng đơn sắc.
  - *Ví dụ Nghèo/Cũ:* `tường sơn kem cũ hơi ố, đồ gỗ nâu sờn, vải hoa bạc màu`.
  - *Ví dụ Sang/Sạch:* `tường trắng ngà sáng, ga giường xanh bạc hà rất nhạt, kim loại inox sạch, gỗ óc chó ấm vừa phải`.
- **Tông màu Tổng thể (Tone & Mood):** Khóa không gian bằng một câu chốt về cảm giác chung của cảnh, khớp với diễn biến câu chuyện. Tránh dùng từ kỹ thuật nhiếp ảnh như `high-key` vì AI dễ làm cháy sáng (blowout), hãy dùng từ miêu tả trực quan.
  - *Ví dụ:* `Tổng thể TRẦM, GIẢM BÃO HÒA, ngả nâu-xám`, `Tổng thể ẤM ÁP nhưng có sắc mệt mỏi`, `Tổng thể sáng sủa, sạch sẽ, rõ nét`.
- **Sự Tương Phản Liên Hoàn (BẮT BUỘC):** Màu sắc của bối cảnh này phải được đặt trong hệ quy chiếu với bối cảnh trước/sau nó để tạo nhịp điệu thị giác.
  - *Công thức:* `... phải KHÁC HẲN [đặc điểm của cảnh trước/cảnh song song]`.
  - *Ví dụ:* `... phải KHÁC HẲN ánh trắng lạnh của siêu thị và ánh vàng-xám ngột ngạt của văn phòng trong các cảnh trước.` Hoặc `Khác hẳn ánh đèn nhân tạo của các cảnh trong nhà.`

## 3. Ánh sáng (Lighting)
- **Định danh CỤ THỂ Nguồn sáng & Hướng sáng:** Cấm viết "cinematic lighting" chung chung mà thiếu nguồn gốc. Phải chỉ rõ loại đèn, màu của đèn và cách ánh sáng rơi xuống không gian.
  - *Nội cảnh tồi tàn/ngột ngạt:* `đèn huỳnh quang trần cũ ám VÀNG-XÁM, yếu và phẳng, tạo cảm giác ngột ngạt tù túng`.
  - *Nội cảnh đẹp/chuyên nghiệp:* `Đèn LED trắng trung tính dịu từ trần chiếu đều toàn phòng, không ám xanh nặng, không tối góc.`
  - *Ngoại cảnh/Cửa sổ:* `Nắng chiều muộn vàng ấm chiếu xiên từ một bên... trời xanh nhạt phía sau, không mây gắt.`
- **Phân vùng Ánh sáng (Đa lớp):** Một khung hình điện ảnh thực tế luôn có sự giao thoa của nhiều luồng sáng tạo chiều sâu.
  - *Ví dụ tạo không gian:* `Đèn đọc sách vàng nhạt ở đầu giường chỉ tạo một lớp ấm nhẹ quanh nhân vật... Có thêm ánh sáng trắng dịu từ khu vực cửa sổ và hành lang để mở nền, giúp căn phòng rộng và thoáng.`
  - *Ví dụ tạo độ sâu:* `ánh trắng lạnh sáng hơn hắt vào từ cửa sổ nội bộ phía sau`.
- **Bảo toàn Skin tone (Mặt nhân vật):** Trong mọi bối cảnh, ánh sáng chiếu lên người phải đảm bảo giữ được sắc tố da tự nhiên và đọc được chi tiết khuôn mặt, trừ khi có lệnh đặc biệt yêu cầu che giấu.
  - *Câu lệnh mẫu:* `Ánh sáng chính mềm và rõ, giữ skin tone tự nhiên, rõ mặt nhân vật`.

---
**Tóm tắt Công thức Viết Lệnh (Prompting Formula):**
`[Chất ảnh, Ống kính & Cỡ cảnh] + [Nội thất & Màu vật liệu cụ thể] + [Định danh nguồn sáng + Phân vùng sáng] + [Tổng thể Tone & Đối chiếu khác biệt với cảnh trước]`
