# 4 — Thẻ REF của một đồ vật (`REF_PROP_*`)

> **File này trả lời:** đồ vật nào xứng đáng có thẻ riêng, và ảnh gốc của nó phải trông thế nào.
> **Mở khi:** rà kịch bản tìm đạo cụ chủ chốt, hoặc tạo/sửa một `REF_PROP_*`.
> **Không chứa:** cú pháp mã ID và dòng `Dùng:` (→ `2-du-lieu-sf-board.md`) ·
>   cách đưa đạo cụ vào một khung hình cụ thể (→ `8-prompt-sf.md`) ·
>   đồ đạc thuộc kiến trúc của nơi chốn (→ `5-the-dia-diem.md`)

## 1. Khi nào tạo REF cho đạo cụ (`REF_PROP_<TÊN>`)
- ⚠️ **Một danh từ có thể là nhiều vật:** trước khi tạo REF, rà xem cái tên ấy trong kịch bản có trỏ tới nhiều vật khác nhau không (hai chiếc thùng, ba bức tranh, hai cây bút). Nếu có: mỗi vật một mã REF riêng, tên gọi phân biệt được, và phải ghi rõ vật nào mang chữ / dấu hiệu nhận dạng — vì mọi SF sau đó sẽ trỏ vào nhầm nếu chúng cùng tên.
- Xuất hiện ở ≥ 3 scene (không tính các vật dụng thông thường/nhỏ lẻ như cốc, chăn, quần áo).
- Được nhắc thẳng trong thoại.
- Gắn với lệnh cấm, bí mật, hoặc thói quen.
- **Là vật trao tay, gieo-trả.**

## 2. Quy tắc tạo ảnh gốc
- Tỷ lệ 1:1, góc 3/4. Không có người/tay, chỉ đạo cụ.
- Một vật nhiều trạng thái (ví mở/ví đóng, thùng nguyên đai/thùng đã bẻ dẹp) phải tạo các ảnh riêng.
- **Trạng thái của ảnh gốc là trạng thái vật đang Ở trong cảnh đầu tiên kịch bản dùng nó** — hàng chưa bán thì còn nguyên đai, thư chưa đọc thì còn phong bì, không được mở sẵn cho dễ nhìn thấy chữ. Muốn thấy chữ bên trong thì tạo ảnh trạng thái thứ hai, đừng bẻ trạng thái của ảnh gốc.

### Theo loại vật
- **Đạo cụ có ảnh người in trên mặt** (thẻ nhân viên, giấy tờ tuỳ thân, ảnh khung...): vẫn phải đính `REF_<TÊN>_PORTRAIT` vào `refs.chars` để khuôn mặt in trên đó khớp nhân vật thật — không để AI tự bịa một khuôn mặt lạ. Đồng thời phải mô tả rõ trang phục/thời điểm của ảnh đó trong prompt (thường là ảnh chụp cũ hơn, trang phục khác cảnh hiện tại), vì nó không tự động thừa hưởng bộ đồ ở `REF_FULL`.
- **Đạo cụ nhỏ cầm tay** (ví, điện thoại, nhẫn): bắt buộc đặt trên một bề mặt trung tính (VD: mặt bàn gỗ trơn) để AI tính toán tỷ lệ (Scale) và bóng đổ. Không vẽ lơ lửng.
- **Đạo cụ cỡ lớn** (thùng hàng, tủ, máy móc, đồ nội thất): đứng trên sàn của chính bối cảnh nó thuộc về, tuyệt đối không đặt trên mặt bàn — đặt lên bàn là mất sạch mốc tỉ lệ. Chụp góc 3/4 từ ngang tầm hông, không chụp từ trên xuống. Bắt buộc khoá tỉ lệ bằng hai thứ cùng lúc: (a) số đo cụ thể so với cơ thể người ("cao ngang hông người lớn, khoảng một mét") và (b) một vật quen thuộc đứng cạnh làm mốc (bục trưng bày, ghế, thùng nhỏ).
- **Phương tiện:** biển số và logo hãng làm mờ.

## 3. Đạo cụ đã có REF thì SF phải "khoe" nó
Một khi đạo cụ đã được cấp thẻ `REF_PROP`, nghĩa là nó chứa thông tin tối quan trọng của kịch bản (logo, tên người, cấu tạo đặc biệt).

→ Luật cấm che khuất / lật úp trong ảnh SF tĩnh: `8-prompt-sf.md` §Ba loại vật thể → bảo vệ REF_PROP.

## 4. Kiểm tra
- [ ] Đạo cụ chủ chốt đã có `REF_PROP` riêng, đủ các trạng thái (ví mở/ví đóng, thùng nguyên đai/thùng đã bẻ dẹp).
- [ ] Không có hai vật khác nhau dùng chung một mã REF.
- [ ] Ảnh gốc đang ở trạng thái của cảnh đầu tiên kịch bản dùng nó.
- [ ] Đạo cụ cỡ lớn đứng trên sàn, có mốc tỉ lệ; đạo cụ nhỏ đặt trên bề mặt trung tính.

## 5. Đạo cụ không thuộc thẻ địa điểm
Đạo cụ thay đổi trạng thái hoặc chỉ xuất hiện ở vài khung hình (lấy đồng hồ từ túi ra, đẩy tờ giấy qua bàn) bắt buộc nằm ở prompt của từng khung SF lẻ, tuyệt đối không đưa vào phần mô tả Bối cảnh — chi tiết: `5-the-dia-diem.md` §Cấm nhét Đạo cụ di động.
