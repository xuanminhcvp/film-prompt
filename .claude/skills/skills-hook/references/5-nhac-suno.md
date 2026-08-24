# Bước 5 — Prompt nhạc nền Suno (Nhịp không thoại)

> **Nguồn sự thật duy nhất** cho nhạc. Viết ngay sau khi viết prompt video của nhịp đó. Lưu vào trường `music` của shot, KHÔNG lưu vào `prompt` video.

## Mục lục
- [Luật Cứng](#luật-cứng)
- [Bốn Vai Trò Nhạc](#bốn-vai-trò-nhạc)
- [Quy trình 3 bước](#quy-trình-3-bước)
- [Cách Viết Prompt Suno](#cách-viết-prompt-suno)
- [Kiểm tra cuối bước](#kiểm-tra-cuối-bước)
- [Mẫu Đã Duyệt](#mẫu-đã-duyệt)

---

## Luật Cứng
- **MỌI nhịp không thoại ĐỀU PHẢI có nhạc**. Không được để trống.
- **Đặc trưng Hook**: Âm nhạc trong Hook cần thu hút sự chú ý mạnh ngay từ những giây đầu tiên. Nhạc thường dùng vai trò ĐẨY hoặc NÂNG, nhịp độ có thể kịch tính hơn phim thông thường để giữ chân người xem.
- **Mỗi nhịp có ĐÚNG 2 phương án (A và B): 1 bản CÓ LỜI + 1 bản KHÔNG LỜI**.
- Hai nhịp cạnh nhau KHÔNG được cùng vai trò hoặc cùng nhạc cụ dẫn.
- **Phân bổ tỷ lệ**:
  - Nhạc CÓ LỜI (~75% phim): Chủ đề phải hợp vai trò. Không viết lyrics đầy đủ, chỉ nêu chủ đề/ngôi kể.
  - Nhạc KHÔNG LỜI (~25% phim): Dùng cho cảnh quá riêng tư, đỉnh điểm im lặng, hoặc vai NGHỈ.

## Bốn Vai Trò Nhạc
Viết rõ vai trò + lý do TRƯỚC khi viết 2 prompt Suno.
1. **ĐẨY**: Bùng nổ, nhạc chiếm sân khấu. Chỉ dùng 2-3 nhịp trong CẢ PHIM (Mở/Kết/Đỉnh cảm xúc).
2. **NÂNG**: Tạo đà đi cùng nhân vật nhưng không lấn lướt (Thường dùng cho mốc nhảy thời gian/chuyển chương).
3. **KÌM**: Nhạc nhỏ/kìm nén hơn cảm xúc thật. Dùng khi nhân vật đang cố gồng mình giữ phẩm giá.
4. **NGHỈ**: Nhạc cụ đơn giản (không trống), gần như ambient, tạo nhịp thở. Đây là nhóm chiếm số lượng ĐÔNG NHẤT.

## Quy trình 3 bước
1. Chốt **VAI TRÒ** (Đẩy/Nâng/Kìm/Nghỉ) + Viết **lý do**.
2. Viết **2 prompt (A có lời, B không lời)** cùng cảm xúc nhưng KHÁC cách xử lý âm thanh.
3. Lưu vào đúng trường `music: {role, emo, a, a_kind, b, b_kind}` của shot.

## Cách Viết Prompt Suno
Prompt nhạc cần có:
- **BPM** cụ thể & mô tả nhịp (vd: walking pace).
- **Cấu trúc theo thời gian**: Mở bằng gì -> Cú rút (quan trọng nhất) -> Kết mở/đóng.
- **Giọng hát**: Mô tả chi tiết (quãng, chất giọng, cách hát "close to the mic", "spoken"). Đừng chỉ ghi "female vocal".
- **Chủ đề lời**: Giọng kể gì, cấm gì (vd: "không đắc thắng"). 
- **Mix**: Warm analog, tape saturation, dry intimate...
- **Tag chốt cuối**: Từ khóa thể loại, nhạc cụ cách nhau bằng dấu phẩy.

## Kiểm tra cuối bước
- [ ] Số bộ prompt nhạc phải khớp số nhịp không thoại.
- [ ] Mỗi nhịp có (A) Có lời + (B) Không lời.
- [ ] Đã ghi VAI TRÒ + Lý do.
- [ ] Cả phim chỉ có 2-3 nhịp vai ĐẨY.
- [ ] Lưu đúng vào trường `music`.

---

## Mẫu Đã Duyệt (8 Dollars, 2026-07)
*Lưu ý: Mẫu cũ có thể A/B cùng dạng, NHƯNG luật mới yêu cầu 1 có lời + 1 không lời. Dùng mẫu để học cách miêu tả nhạc cụ và cảm xúc.*

### Vai trò KÌM
- **Lý do**: Nhân vật giữ phẩm giá, không cho ai thấy mình gãy; nhạc cũng phải kìm.
- **Mẫu (Có lời)**:
`Soul ballad at 66 BPM with a raw female alto lead sung very close to the mic, smoky and slightly worn, almost spoken in places; sparse Rhodes and upright bass underneath, brushed drums entering only halfway, one restrained string swell at the peak then dropping straight back to voice and Rhodes; lyrics about walking out with your head up when everything has been taken from you, never triumphant; warm analog mix, female vocal, soul, intimate, restrained`

### Vai trò NGHỈ
- **Lý do**: Cả phim đang dồn, cho khán giả khoảng thở cùng nhân vật kiệt sức ngủ thiếp đi.
- **Mẫu (Không lời)**:
`Ambient lullaby at 52 BPM; a single warm pad breathing very slowly, one felt-piano phrase repeating with heavy sustain and getting quieter each time, a faint refrigerator-like hum underneath, no percussion, no arc, simply fading out; extremely soft late-night mix, almost subliminal, ambient, piano, warm, sleepy, minimal`

### Vai trò NÂNG (Cầu nối nhảy thời gian)
- **Lý do**: Báo hiệu chương mới nhưng nhân vật vẫn còn sợ. 82-88 BPM, dựng dần rồi rút về mộc.

### Vai trò ĐẨY (Đỉnh cảm xúc lớn nhất)
- **Lý do**: Chỗ duy nhất nhạc chiếm sân khấu hoàn toàn. 78-84 BPM, dàn dây/hợp xướng tới đỉnh và kết mở.
