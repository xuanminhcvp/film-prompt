# 8 — Prompt của một khung hình tĩnh thường (SF)

> **File này trả lời:** viết prompt cho một Start Frame thường thế nào — ai trong khung, đứng đâu, hậu cảnh là gì.
> **Mở khi:** sinh prompt cho bất kỳ `SF-*` nào không phải Master.
> **Không chứa:** Master SF và khung gối đầu (→ `6-cum-va-master-sf.md`) ·
>   quần chúng nền & xe cộ (→ `9-quan-chung-nen.md`) ·
>   trần ký tự và dòng kết 16:9 (→ `2-du-lieu-sf-board.md` §8) ·
>   nhịp không thoại (→ `10-nhip-lang.md`) · ánh sáng/màu (→ `5-the-dia-diem.md`)

> **Luật viết: 85% nội dung lặp lại (bối cảnh, trang phục...) đã nằm ở Thẻ Địa Điểm và thẻ REF. Prompt SF viết thành các đoạn văn điện ảnh (Cinematic) mạch lạc**, không điền form cứng nhắc.

## 1. Nguyên lý bố cục cốt lõi

### 1.1 Bản đồ vị trí tường minh
Mô tả vị trí bằng mốc cụ thể (% khung, landmark), chỉ rõ ai thuộc nhóm nào, tách nhóm dễ nhầm bằng khoảng trống rõ ràng.

### 1.2 Chữ trong khung — khai báo hai chiều
- *(a) Chiều muốn hiện:* mọi chữ muốn hiện trên ảnh (bảng tên, biển số, logo) phải được liệt kê rõ, kèm đánh vần chính xác.
- *(b) Chiều không muốn hiện (nhãn hiệu):* mọi bề mặt có thể mang chữ mà ta không khai — vỏ thiết bị, thùng hàng, bao bì, biển hiệu nền, biển số xe — bắt buộc được khoá bằng câu khẳng định là nhãn hư cấu. Tự viết ra một thương hiệu hư cấu không có thật.

### 1.3 Ba loại vật thể
- **(a) Thuộc bối cảnh**: bắt buộc có, tả khái quát, lùi ra nền (giấy tờ, sách vở...).
- **(b) Đạo cụ tham gia hành động**: đang cầm/đưa/nhìn. Tả cụ thể, tách bạch khỏi nhóm nền. Đính ảnh nếu có.
- **(c) Đạo cụ minh họa nội tâm**: thừa, loại bỏ. (VD: khung ảnh gia đình, bằng khen). Dùng ngôn ngữ cơ thể thay thế.

⛔ **Bảo vệ REF_PROP (khoe đạo cụ):** một khi đạo cụ đã được cấp thẻ `REF_PROP`, nghĩa là nó chứa thông tin tối quan trọng của kịch bản (logo, tên người, cấu tạo đặc biệt). Trong ảnh SF tĩnh, tuyệt đối không che khuất, lật úp mặt lưng, hay xoay góc chết của đạo cụ này về phía camera. SF bắt buộc phải "khoe" ra góc diện thấy rõ nhất các thông tin đó. Mọi hành động lật úp, giấu đi hay nhét vào túi phải là hành động xảy RA trong video, tuyệt đối không được là trạng thái chết đứng trên ảnh SF.

## 2. Xác định CAST theo góc máy

### 2.1 Tuyệt đối tuân thủ điểm đặt camera
Lấy từ bản đồ không gian toàn cảnh (Master SF). Bắt buộc chốt vị trí Đặt Máy Quay trước, từ đó mới chiếu ra Nón Quan Sát. Số lượng người và hướng Background hoàn toàn phụ thuộc vào góc chĩa của máy quay.

Tư duy theo đúng trình tự: Đặt máy quay ở đâu? → Hướng máy chĩa về đâu? → Từ đó suy ra nón quan sát quét trúng ai và Background phía sau họ là gì. Nếu không chốt được điểm đặt máy, AI sẽ làm nhân vật và bối cảnh nhảy vị trí lung tung. Mọi điểm đặt camera phải tuân theo vị trí không gian đã chốt ở Master SF.

*Ai được vào `refs.chars` và trần 4 nhân vật:* `2-du-lieu-sf-board.md` §5.1.

### 2.2 cấm tự đẩy nhân vật ngang hàng thành "lớp sau" (bảo toàn raccord vị trí)
Khi cắt góc cận/trung (Two-Shot, Single) từ Master SF có nhóm đứng ngang hàng (cùng mặt phẳng chiều sâu), tuyệt đối không tự ý mô tả nhân vật còn lại là *"lớp sau, ngoài nét"* hay *"đứng phía sau"*. Từ khóa *"lớp sau"* sẽ ép AI kéo nhân vật đó lùi sâu về hậu cảnh, gây vỡ raccord vị trí.

*Xử lý đúng:* nếu nhân vật nằm ngoài nón quan sát → không mô tả họ trong prompt SF hoặc REF. Chỉ được dùng *"lớp sau"* khi nhân vật đó thực sự đang đứng phía sau theo chiều sâu vật lý ở Master SF.

## 3. Neo bối cảnh của SF thường

- `refs.bg` của SF thường bắt buộc trỏ về ID của Master SF phụ trách Cụm Không Gian đó (VD: `SF-S1-M1-MASTER`). Tuyệt đối không trỏ lung tung hay tự ý trỏ về Thẻ Địa Điểm rỗng.
- **Cấm tả vị trí tương đối của bàn và quầy Ở SF thường** (chống lệch layout với Master SF):
  - SF thường đã kế thừa toàn bộ bối cảnh không gian từ Master SF qua `refs.bg`.
  - Riêng với bàn và quầy: tuyệt đối cấm tả lại các vị trí tương đối như *"trước quầy"*, *"sau quầy"*, *"bàn giữa"*, *"bàn trước"*, *"bàn sau"*... (đặc biệt trong khối hậu cảnh).
  - *Vì sao*: nhắc lại các cụm từ vị trí tương đối của bàn/quầy khiến AI sinh ảnh hiểu nhầm thành chỉ thị thiết lập lại layout mới, dẫn tới biến dạng, nhân bản bàn/quầy hoặc dịch chuyển góc quầy lệch hoàn toàn so với Master SF.

## 4. Khối hậu cảnh — gồm hai phần bắt buộc, viết đúng thứ tự

Quần chúng nền và hướng bối cảnh được quyết định độc lập cho từng SF (tuỳ diễn biến và góc quay), tuyệt đối không khoá cố định hay quy chuẩn theo Thẻ Địa Điểm.

### (a) trục bối cảnh — bức tường / môi trường sau lưng chủ thể

- *(a1) Hậu cảnh là mảng tường/môi trường chưa có ảnh riêng*: khi máy quay chĩa theo hướng ngược trục hoặc khác hướng so với Master SF (ví dụ: OTS nhìn ngược vào lòng phòng, Close-up quay lưng ra cửa hàng) — câu đầu của khối hậu cảnh bắt buộc gọi tên đích danh một trong bốn hướng đã khai ở khối quy hoạch 360° của Thẻ Địa Điểm (VD: *"Hậu cảnh sau lưng Bryce là phía trong cửa hàng: dãy tivi treo tường và kệ hàng"*).
- *(a2) Hậu cảnh chứa một cụm khác đã có ảnh* (không gian thông nhau) → đây là khung gối đầu hai cụm, xử lý theo `6-cum-va-master-sf.md` §3.
- *Khi nào bỏ trống phần (a)*: khi máy quay chĩa cùng hướng / cùng trục với Master SF (kế thừa tự nhiên từ ảnh `refs.bg`).
- *Vì sao cần phần (a)*: ảnh Master SF chỉ chứa một hướng nhìn. Khung ngược trục mà không có chữ chỉ hướng bối cảnh hoặc ảnh trỏ neo thứ hai thì AI sẽ bê nguyên hậu cảnh Master SF cũ, hoặc tự bịa ra một bối cảnh mới.

### (b) người & phương tiện trong nón quan sát
→ Toàn bộ luật ở `9-quan-chung-nen.md`.

## 5. Thiết kế một khung hình

- **Trạng thái chờ (Pending State — sống còn cho video):** hỏi trước khi viết mỗi SF: *"Trong clip này có hành động thay đổi trạng thái nào không?"* Nếu có (đặt xuống, lật úp, mở nắp, tháo ra, ném đi), ảnh SF bắt buộc vẽ trạng thái trước khi thay đổi. Viết trạng thái đã xong vào SF (thẻ đã úp, cửa đã mở) là giết chết nội dung của clip — video sẽ không còn hành động gì để diễn. Lệnh của kịch bản (*face down, sit down, open it*) là để chỉ định clip kết thúc ở đâu, không phải chỉ định frame ảnh tĩnh bắt đầu thế nào.
- **Khung OTS**: vai ở tiền cảnh phải là của người đang được nói với.
- **Khung Cận (CU)**: phải có 1 thân người ở tiền cảnh để ép máy quay lại gần, nếu không sẽ trôi ra khung rộng.
- **Không insert thuần đạo cụ hoặc thuần nhịp lặng không người**: trừ cảnh thời tiết/bối cảnh thuần. Mọi cảnh khác phải có người.
- **Giới hạn**: không dựng khung đang chuyển động. Tối đa 2 lớp chiều sâu.
- **Nghe lén**: người nghe lén núp ở vùng tối, không nhìn thấy người trong phòng (chỉ nghe).
- **Hướng nhìn**: 2 người thì nhìn thẳng mắt nhau (trừ khi thoại bảo khác). 1 người thì nhìn vật/ngoài khung. Quần chúng tuyệt đối không nhìn camera.
- **Viết ngắn gọn**: cắt mọi thứ ảnh ref đã có (màu áo, tóc), bỏ mã nội bộ.

## 6. Hai luật về cách dùng chữ "không"

Áp cho mọi prompt ảnh, kể cả Thẻ Địa Điểm và Master SF.

- **Cấm lạm dụng từ "không" (Negative Prompts rác):** tuyệt đối cấm thói quen chèn các từ cấm vô nghĩa (*"không chữ, không watermark, không logo"*) vào cuối prompt. Chỉ dùng chữ không khi thực sự cần chặn hành vi sai của nhân vật (VD: *"nhìn nhau nhưng không chạm tay"*, *"đứng yên không bước tới"*). Đừng biến câu cấm thành rác.
- **Khẳng định trạng thái (tránh cấm theo ngưỡng):** khi cần khoá một trạng thái mặc định (cài cúc, đóng cửa, đứng thẳng...), viết câu khẳng định trạng thái đó ("cài kín toàn bộ cúc"), không viết dưới dạng ngưỡng cấm ("không cởi quá N nút") — câu ngưỡng bị AI sinh ảnh đọc thành *cho phép một phần*, không phải khoá cứng.

## 7. Checklist bắt buộc
0. **Địa điểm đã xuất hiện chưa?** Rà tất cả scene. Đã xuất hiện (cùng phòng/cùng nhà/khu phố) thì phải khóa bằng `refs.bg`. Chú ý ngoại cảnh rất dễ sót.
1. **Cast**: đúng người lọt nón quan sát.
2. **Nhân vật chính**: vị trí, hướng nhìn, biểu cảm khoảnh khắc.
3. **Quần chúng nền**: có ai không? Từng vùng có gì? Mang đạo cụ hợp thời tiết/giờ. Khai theo từng vùng.
4. **Bản đồ không gian**: giữ đúng continuity `pose`.
5. **Nội thất cơ bản**: phải có (ghế, bàn, giường...).
6. **Đạo cụ**: phân loại theo (a) nền, (b) hành động. Đính ảnh REF_PROP nếu là món chủ chốt, tối đa 2 ảnh.
7. **Đồ vật nối tiếp scene trước**: bắt buộc rà SF cuối scene trước (đóng/mở, nằm đâu). Báo user nếu kịch bản mới mâu thuẫn, không tự lách.
8. **Giờ giấc / đông đúc**: khớp thoại.
9. **Chữ**: liệt kê đủ, yêu cầu rõ ràng, không nhòe.
10. Đọc lại thoại xem mốc đổi trạng thái chuẩn chưa. Khớp 100% chữ kịch bản.
11. Prompt kết thúc bằng dòng `KHUNG NGANG 16:9` (`2-du-lieu-sf-board.md` §8).
