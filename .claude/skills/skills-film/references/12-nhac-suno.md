# 12 — Prompt nhạc nền Suno

> **File này trả lời:** viết prompt nhạc cho một nhịp không thoại thế nào.
> **Mở khi:** ngay sau khi viết xong prompt video của một nhịp.
> **Không chứa:** khi nào cần một nhịp không thoại và định mức của chúng (→ `10-nhip-lang.md`) ·
>   âm thanh trong clip video (→ `11-prompt-video.md`)

> Lưu vào trường `music` của shot, không lưu vào trường `prompt` video.

## 1. Luật cứng
- Mỗi nhịp có đúng 2 phương án: (A) có lời + (B) không lời. Hai nhịp cạnh nhau không được cùng vai trò hoặc cùng nhạc cụ dẫn. *(Luật gốc: `10-nhip-lang.md` §7.)*
- **Phân bổ tỷ lệ toàn phim**:
  - Nhạc có lời (~75% phim): chủ đề phải hợp vai trò. Không viết lyrics đầy đủ, chỉ nêu chủ đề/ngôi kể.
  - Nhạc không lời (~25% phim): dùng cho cảnh quá riêng tư, đỉnh điểm im lặng, hoặc vai nghỉ.

## 2. Bốn vai trò nhạc
Viết rõ vai trò + lý do trước khi viết 2 prompt Suno.

1. **Đẩy**: bùng nổ, nhạc chiếm sân khấu. Chỉ dùng 2–3 nhịp trong cả phim (Mở/Kết/Đỉnh cảm xúc).
2. **Nâng**: tạo đà đi cùng nhân vật nhưng không lấn lướt (thường dùng cho mốc nhảy thời gian/chuyển chương).
3. **Kìm**: nhạc nhỏ/kìm nén hơn cảm xúc thật. Dùng khi nhân vật đang cố gồng mình giữ phẩm giá.
4. **Nghỉ**: nhạc cụ đơn giản (không trống), gần như ambient, tạo nhịp thở. Đây là nhóm chiếm số lượng đông nhất.

## 3. Quy trình 3 bước
1. Chốt vai trò (Đẩy/Nâng/Kìm/Nghỉ) + viết lý do.
2. Viết 2 prompt (A có lời, B không lời) cùng cảm xúc nhưng khác cách xử lý âm thanh.
3. Lưu vào đúng trường `music: {role, emo, a, a_kind, b, b_kind}` của shot.

## 4. Cách viết prompt Suno
Prompt nhạc cần có:
- **BPM** cụ thể & mô tả nhịp (vd: walking pace).
- **Cấu trúc theo thời gian**: mở bằng gì → cú rút (quan trọng nhất) → kết mở/đóng.
- **Giọng hát**: mô tả chi tiết (quãng, chất giọng, cách hát — "close to the mic", "spoken"). Đừng chỉ ghi "female vocal".
- **Chủ đề lời**: giọng kể gì, cấm gì (vd: "không đắc thắng").
- **Mix**: warm analog, tape saturation, dry intimate...
- **Tag chốt cuối**: từ khóa thể loại, nhạc cụ cách nhau bằng dấu phẩy.

## 5. Kiểm tra cuối bước
- [ ] Số bộ prompt nhạc khớp số nhịp không thoại.
- [ ] Mỗi nhịp có (A) có lời + (B) không lời.
- [ ] Đã ghi vai trò + lý do.
- [ ] Cả phim chỉ có 2–3 nhịp vai đẩy.
- [ ] Lưu đúng vào trường `music`.

---

## 6. Mẫu đã duyệt (8 Dollars, 2026-07)
*Lưu ý: mẫu cũ có thể A/B cùng dạng, nhưng luật mới yêu cầu 1 có lời + 1 không lời. Dùng mẫu để học cách miêu tả nhạc cụ và cảm xúc.*

### Vai trò kìm
- **Lý do**: nhân vật giữ phẩm giá, không cho ai thấy mình gãy; nhạc cũng phải kìm.
- **Mẫu (có lời)**:
`Soul ballad at 66 BPM with a raw female alto lead sung very close to the mic, smoky and slightly worn, almost spoken in places; sparse Rhodes and upright bass underneath, brushed drums entering only halfway, one restrained string swell at the peak then dropping straight back to voice and Rhodes; lyrics about walking out with your head up when everything has been taken from you, never triumphant; warm analog mix, female vocal, soul, intimate, restrained`

### Vai trò nghỉ
- **Lý do**: cả phim đang dồn, cho khán giả khoảng thở cùng nhân vật kiệt sức ngủ thiếp đi.
- **Mẫu (không lời)**:
`Ambient lullaby at 52 BPM; a single warm pad breathing very slowly, one felt-piano phrase repeating with heavy sustain and getting quieter each time, a faint refrigerator-like hum underneath, no percussion, no arc, simply fading out; extremely soft late-night mix, almost subliminal, ambient, piano, warm, sleepy, minimal`

### Vai trò nâng (cầu nối nhảy thời gian)
- **Lý do**: báo hiệu chương mới nhưng nhân vật vẫn còn sợ. 82–88 BPM, dựng dần rồi rút về mộc.

### Vai trò đẩy (đỉnh cảm xúc lớn nhất)
- **Lý do**: chỗ duy nhất nhạc chiếm sân khấu hoàn toàn. 78–84 BPM, dàn dây/hợp xướng tới đỉnh và kết mở.
