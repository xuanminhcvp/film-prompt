# 5 — Thẻ REF của một nơi chốn (`REF_BG_*`)

> **File này trả lời:** thẻ gốc của một địa điểm phải chứa gì — kiến trúc, quy hoạch không gian, màu, ánh sáng.
> **Mở khi:** tạo hoặc sửa bất kỳ Thẻ Địa Điểm nào, kể cả biến thể giờ giấc.
> **Không chứa:** ánh sáng/màu cho thẻ nhân vật hay SF lẻ (xem §phạm VI dưới đây) ·
>   Master SF neo nhân vật vào bối cảnh (→ `6-cum-va-master-sf.md`) ·
>   hậu cảnh của từng khung lẻ (→ `8-prompt-sf.md`) ·
>   quần chúng và xe cộ đang di chuyển (→ `9-quan-chung-nen.md`)

## ⚠️ phạm VI áp dụng của màu & ánh sáng — bắt buộc đọc
1. **Chỉ dùng cho bối cảnh (Thẻ Địa Điểm):** mọi kỹ thuật ánh sáng, màu sắc trong file này chỉ được áp dụng khi tạo prompt cho **Thẻ Địa Điểm (`REF_BG`)**.
2. **Cấm dùng cho nhân vật:** tuyệt đối không áp dụng đánh sáng điện ảnh (đổ bóng gắt, tối, tương phản cao) vào Thẻ Nhân Vật (Portrait / Full-body). Ảnh REF nhân vật bắt buộc dùng ánh sáng studio dịu nhẹ, đều, phẳng để lấy nét rõ khuôn mặt.
3. **Cấm viết lại vào shot lẻ (SF):** khi tạo các khung hình SF lẻ, không được nhét lại từ khóa ánh sáng/màu sắc vào prompt. SF lẻ tự động kế thừa ánh sáng từ Thẻ Địa Điểm. Tả lại sẽ đè (override) Look gốc.

---

## 1. Quy trình tạo thẻ địa điểm
- **Khởi tạo đồng loạt ngay từ đầu**: toàn bộ Thẻ địa điểm (và mọi biến thể thời gian của chúng) của cả kịch bản phải được tạo và đưa vào scene `REF` ngay từ đầu, cùng lúc với tạo hình nhân vật.
- **Biến thể sinh ra từ bản gốc**: dù mỗi biến thể giờ giấc (vd: Bếp ngày, Bếp đêm) bắt buộc là một Thẻ địa điểm độc lập (có mã REF riêng), tuyệt đối không tạo lại prompt không gian từ đầu cho từng thẻ. Chọn một thời điểm xuất hiện nhiều nhất/chi tiết nhất làm "Bối cảnh gốc" và tạo prompt. Với các biến thể thời gian khác, đính ảnh của Bối cảnh gốc vào `refs.bg`. Prompt của thẻ biến thể lúc này cực ngắn, chỉ tập trung ra lệnh thay đổi thời điểm (VD: *"Giữ nguyên 100% không gian và đồ đạc của ảnh tham chiếu, chỉ đổi ánh sáng thành ban đêm với đèn đường vàng hắt vào"*).
- **Đồng bộ Kiến trúc cùng tòa nhà (Cross-Room Reference)**: các căn phòng khác nhau trong cùng một tòa nhà (Phòng khách, Bếp, Phòng ngủ) cũng phải đính ảnh của một "Phòng Chủ đạo" (thường là Phòng khách) vào `refs.bg` để đảm bảo chung một Art Direction.
  - **Phòng kín khác không gian thông nhau:** lệnh *"không copy đồ đạc của ảnh gốc vào khung này"* chỉ đúng khi hai phòng có tường ngăn hoàn toàn (phòng khách kín vs phòng ngủ kín). Nếu từ khu vực này vẫn nhìn thấy khu vực kia (cùng một sảnh hội trường thông nhau, lều y tế nhìn ra sân khấu chính, ban công nhìn xuống phòng khách, bếp mở thông phòng ăn), tuyệt đối cấm viết *"không copy"* cho phần kiến trúc nhìn thấy được — mà bắt buộc viết ngược lại: *"Giữ nguyên 100% [sân khấu · bục phát biểu · ruy băng / landmark] ở lớp sau xa đúng theo ảnh tham chiếu, chỉ đổi vị trí máy quay."* Xóa landmark khỏi thẻ bối cảnh hoặc SF con thì mọi khung hình nhìn về hướng đó sẽ bị AI bịa lại từ đầu, mỗi khung một kiểu.
- **Thẻ địa điểm là bản neo**: chờ user duyệt sinh ảnh và chốt 100% thẻ địa điểm mới bắt đầu chia shot cho các scene. Khung hình con sẽ neo vào thẻ bằng `refs.bg`.

## 2. Nội dung được phép và bị cấm
- **Thẻ địa điểm là bối cảnh không người (Empty Location)**: dùng để định hình Kiến trúc, Ánh sáng môi trường, và Trục không gian. Do đó trường `refs.chars` bắt buộc để trống (không đính kèm nhân vật).
- **Chỉ chứa quy hoạch không gian (Floor Plan) và quy tắc trục (Screen Mapping).** tuyệt đối không chép lại ngoại hình, tính cách hay trang phục nhân vật vào phần miêu tả không gian.
- **Quy hoạch không gian 360° (Floor Plan)**: bắt buộc miêu tả vị trí tương quan của các vật thể/tường lớn theo 4 hướng (Trái, Phải, Đối diện, Sau lưng). Ví dụ: *"Bên trái là dãy cửa sổ, đối diện là quầy bar inox, sau lưng là cửa ra vào"*. Việc này cấp dữ liệu thô để AI không bị "mù" không gian khi camera xoay góc.
- **Cấm "Ngụ ý văn học"**: dịch ẩn ý đạo diễn thành ngôn ngữ thị giác thuần tuý. Cấm viết "đây là sân nhà của cô ấy", "sự lệch pha là nội dung". Chỉ viết thị giác: *"Sự tương phản mạnh giữa bộ vest đắt tiền và chiếc ghế bọc da nứt nẻ."* AI vẽ pixel, không vẽ ẩn ý.
- **Cấm nhét Đạo cụ di động (Dynamic Props)**: những đạo cụ thay đổi trạng thái hoặc chỉ xuất hiện ở vài khung hình (lấy đồng hồ từ túi ra, đẩy tờ giấy qua bàn) bắt buộc để ở prompt của từng khung SF lẻ. Tuyệt đối không đưa vào mô tả Bối cảnh, tránh AI hallucinate vẽ nó tràn lan ở mọi khung hình.
- **Rút gọn Lệnh hệ thống**: viết các chỉ định (phong cách, bộ lọc) thành gạch đầu dòng sắc bén, tránh văn xuôi dài dòng.
- **Giới hạn độ dài**: phần prompt miêu tả Bối cảnh bắt buộc nằm trong khoảng 200 – 300 từ. (Trần ký tự của trường `prompt`: `2-du-lieu-sf-board.md` §8.)

### Bối cảnh trống người ≠ bối cảnh chết
Để thể hiện bối cảnh trống, chỉ cần ghi đúng 1 cụm: *"Không có người trong khung hình"*.

Câu này chỉ cấm người, tuyệt đối không cấm sự sống/phương tiện của nơi chốn. Ngoại cảnh có lòng đường/ngã tư/bãi đỗ thì phần mô tả bối cảnh bắt buộc tả các yếu tố tĩnh trên mặt đường (xe ô tô/xe tải đỗ sát lề, dải phân cách, trạm chờ) — xe đỗ là kiến trúc của con phố, thuộc Thẻ địa điểm; xe đang chạy là yếu tố động, để dành cho khối hậu cảnh của từng SF lẻ (→ `9-quan-chung-nen.md`).

Luật cấm "Negative Prompts rác" (`KHÔNG chữ, KHÔNG watermark, KHÔNG logo`): `8-prompt-sf.md` §Cấm lạm dụng từ "không" — áp cho cả thẻ địa điểm.

### Chỗ ngồi / vị trí có chức năng
Khi Thẻ Địa Điểm khai báo các vị trí có chức năng rõ ràng (bục 3 ghế hội đồng, bàn họp 6 chỗ, dàn đồng ca, hàng ghế bị cáo...), bắt buộc phân vai hoặc xác định trạng thái cho từng chỗ ngồi:
- *(Phương án A — Có người)*: thêm nhân vật nền (cùng mặc áo choàng/đồng phục, không có thoại, không cần tạo REF riêng).
- *(Phương án B — Trống)*: khai rõ trong bối cảnh lý do trống (vd: phiên họp bất thường thiếu thành viên).

Tuyệt đối không để các vị trí chức năng bị bỏ trống mặc định khiến bối cảnh mâu thuẫn với lời thoại.

### Miêu tả thời gian / độ cũ (Production Design)
- **Tuyệt đối cấm dùng mốc thời gian hoặc thập niên** (vd: *kiến trúc cuối 1990-đầu 2000, đã mở 30 năm*) — AI sẽ lập tức biến thành bối cảnh kinh dị, bỏ hoang, tắt đèn.
- Muốn không gian cũ, chỉ được dùng từ miêu tả vibe: *retro, well-maintained, lived-in*, và phải kèm chỉ định *"không gian sáng sủa, đang hoạt động bình thường"*.

---

## 3. Quy tắc viết prompt ảnh của thẻ địa điểm

1. **Bắt đầu bằng tình huống, không bắt đầu bằng kiến trúc**: câu đầu tiên phải trả lời *"không gian này đang được dùng cho việc gì tại đúng khoảnh khắc này"* (VD: "một khu vực tạm dựng cho buổi họp toàn công ty"), rồi mới liệt kê đồ vật. Đồ vật phải là hệ quả của tình huống đó, không phải liệt kê kiến trúc trung tính.
2. **Khóa Quốc gia / Ngôn ngữ**: bắt buộc thêm cụm "Bối cảnh ở Mỹ" vào đầu prompt bối cảnh.
3. **Địa điểm lấy set-dressing từ cả kịch bản**, không giới hạn theo đoạn đang dựng — khác với luật costume/đạo cụ (chỉ lấy từ đúng đoạn đang dựng). Vì địa điểm được tạo "đồng loạt" để phục vụ cả phim.
4. **Cấm khoá niên đại bằng số năm**: tuyệt đối không viết "kiến trúc cuối 1990" hay "xây năm 2000". Tập trung tả chi tiết đồ vật hiện tại (VD: tivi CRT, điện thoại bàn...).
5. **Dòng kết thúc bắt buộc**: prompt của mọi Thẻ Địa Điểm kết thúc bằng dòng `KHUNG NGANG 16:9` (luật chung: `2-du-lieu-sf-board.md` §8).

**Công thức viết lệnh:**
`[Chất ảnh, Ống kính & Cỡ cảnh] + [Nội thất & Màu vật liệu cụ thể] + [Định danh nguồn sáng + Phân vùng sáng] + [Tổng thể Tone & Đối chiếu khác biệt với cảnh trước]`

---

## 4. Chất ảnh · Màu · Ánh sáng (Tiêu chuẩn D.O.P)

Khác biệt lớn nhất giữa một khung hình AI nhòe nhoẹt, giả tạo và một shot phim điện ảnh thực thụ nằm ở Sự hiện thực có chủ đích. Thay vì dùng "Cinematic lighting", "Moody", "Low-key" một cách sáo rỗng khiến AI vẽ bẹp ảnh, hãy dùng ngôn ngữ hiện thực điện ảnh.

### 4.1 Chất ảnh (Image Quality)
- **Từ khoá cốt lõi:** bắt đầu phần miêu tả bằng `photorealistic`, `điện ảnh nhưng hiện thực` (Cinematic but realistic). Luôn kết hợp định hình cỡ cảnh và tiêu cự ống kính rõ ràng (VD: `cinematic wide shot, ống kính 28mm, camera ngang tầm mắt`).
- **Nói không với cường điệu hóa:** tránh lạm dụng các từ khóa làm gắt hình ảnh nếu không đúng thể loại. Nếu bối cảnh là phòng bình thường, bệnh viện hoặc nơi sáng sủa, bắt buộc dùng các lệnh phanh: `không u tối, không moody, không low-key, không cháy trắng`.
- **Kiểm soát Bóng & Độ Tương Phản:** quy định rõ tính chất vật lý của bóng đổ và độ tương phản thay vì nói bóng gió. VD: `độ tương phản trung bình, bóng đổ mềm` (cho phòng sáng), hoặc `đổ bóng dài trên sân và bậc thềm` (cho nắng xiên chiều).

### 4.2 Màu sắc (Color Palette)
- **Màu sắc phải neo vào Vật liệu (Set Dressing):** đừng chỉ miêu tả màu của "không khí" (grading). Gắn màu vào chất liệu nội thất/vật dụng cụ thể để AI không tô cả bức ảnh thành một mảng đơn sắc.
  - *Nghèo/Cũ:* `tường sơn kem cũ hơi ố, đồ gỗ nâu sờn, vải hoa bạc màu`.
  - *Sang/Sạch:* `tường trắng ngà sáng, ga giường xanh bạc hà rất nhạt, kim loại inox sạch, gỗ óc chó ấm vừa phải`.
- **Tông màu tổng thể (Tone & Mood):** khóa không gian bằng một câu chốt về cảm giác chung, khớp diễn biến câu chuyện. Tránh từ kỹ thuật nhiếp ảnh như `high-key` vì AI dễ làm cháy sáng.
  - *Ví dụ:* `Tổng thể TRẦM, GIẢM BÃO HÒA, ngả nâu-xám` · `Tổng thể ẤM ÁP nhưng có sắc mệt mỏi` · `Tổng thể sáng sủa, sạch sẽ, rõ nét`.
- **Sự Tương Phản Liên Hoàn (bắt buộc):** màu của bối cảnh này phải đặt trong hệ quy chiếu với bối cảnh trước/sau để tạo nhịp điệu thị giác.
  - *Công thức:* `... phải KHÁC HẲN [đặc điểm của cảnh trước/cảnh song song]`.
  - *Ví dụ:* `... phải KHÁC HẲN ánh trắng lạnh của siêu thị và ánh vàng-xám ngột ngạt của văn phòng trong các cảnh trước.`

### 4.3 Ánh sáng (Lighting)
- **Định danh cụ thể nguồn sáng & hướng sáng:** cấm viết "cinematic lighting" chung chung mà thiếu nguồn gốc. Phải chỉ rõ loại đèn, màu đèn và cách ánh sáng rơi xuống không gian.
  - *Nội cảnh tồi tàn/ngột ngạt:* `đèn huỳnh quang trần cũ ám VÀNG-XÁM, yếu và phẳng, tạo cảm giác ngột ngạt tù túng`.
  - *Nội cảnh đẹp/chuyên nghiệp:* `Đèn LED trắng trung tính dịu từ trần chiếu đều toàn phòng, không ám xanh nặng, không tối góc.`
  - *Ngoại cảnh/Cửa sổ:* `Nắng chiều muộn vàng ấm chiếu xiên từ một bên... trời xanh nhạt phía sau, không mây gắt.`
- **Phân vùng ánh sáng (đa lớp):** một khung hình điện ảnh thực tế luôn có giao thoa nhiều luồng sáng tạo chiều sâu.
  - *Tạo không gian:* `Đèn đọc sách vàng nhạt ở đầu giường chỉ tạo một lớp ấm nhẹ quanh nhân vật... Có thêm ánh sáng trắng dịu từ khu vực cửa sổ và hành lang để mở nền, giúp căn phòng rộng và thoáng.`
  - *Tạo độ sâu:* `ánh trắng lạnh sáng hơn hắt vào từ cửa sổ nội bộ phía sau`.
- **Bảo toàn Skin tone:** trong mọi bối cảnh, ánh sáng chiếu lên người phải giữ được sắc tố da tự nhiên và đọc được chi tiết khuôn mặt, trừ khi có lệnh đặc biệt yêu cầu che giấu.
  - *Câu lệnh mẫu:* `Ánh sáng chính mềm và rõ, giữ skin tone tự nhiên, rõ mặt nhân vật`.

## 5. Kiểm tra

**Đếm được:**
- [ ] Prompt bối cảnh nằm trong **200–300 từ**.
- [ ] Prompt kết thúc bằng dòng `KHUNG NGANG 16:9`.
- [ ] Có cụm "Bối cảnh ở Mỹ" ở đầu prompt.
- [ ] Quy hoạch 360° khai đủ **4 hướng** (trái · phải · đối diện · sau lưng).
- [ ] `refs.chars` **rỗng** ở mọi thẻ địa điểm.
- [ ] Không có số năm / thập niên nào trong prompt.

**Phải đọc mới thấy:**
- [ ] Mọi biến thể giờ đính ảnh Bối cảnh gốc vào `refs.bg`, prompt chỉ ra lệnh đổi thời điểm.
- [ ] Không gian thông nhau: giữ landmark lớp sau, KHÔNG viết "không copy".
- [ ] Không có đạo cụ di động, không có ngụ ý văn học, không có mô tả nhân vật.
- [ ] Mọi vị trí có chức năng (ghế hội đồng, hàng ghế bị cáo…) đã phân vai hoặc khai rõ lý do trống.
- [ ] Ánh sáng/màu neo vào vật liệu cụ thể, có đối chiếu khác biệt với cảnh trước.
