# BẢNG SHOT — HOOK BRYCE · ĐỪNG CỬ ĐỘNG, ĐI THEO CHÁU

**Phạm vi:** 2 phút đầu kịch bản · 287 từ nguyên văn · 8 video full 15s · 24 shot con
· 9 ảnh cần sinh (8 SF + 1 Master neo) + 3 Thumbnail + 6 thẻ REF.

## Giai đoạn 1 — Phân rã thế trận (Blocking Shifts)

| Cụm | Không gian | Master SF | Video |
|---|---|---|---|
| A | Vỉa hè Meridian Avenue, chiều thứ Sáu ~4:16–4:22 PM | `SF-S1-00-MASTER` (neo, không nuôi video) | V-S1-01 → V-S1-06 |
| B | Gian bếp căn hộ Tanner, sáng sớm | `SF-S2-01-MASTER` (kiêm SF của video mở cụm) | V-S2-01 → V-S2-02 |

Cụm A chỉ mở MỘT Master vì thế trận không đổi: ba người đứng nguyên một chỗ, cú
di chuyển duy nhất (kéo đi ngang bốn bước) nằm gọn trong V-S1-03 và đã khai cờ
`"chuyen": true`. Cụm B tách riêng vì đổi hẳn địa điểm + giờ — ranh giới cụm trùng
đúng ranh giới video (V-S1-06 → V-S2-01), và cả hai đầu mối đều là nhịp không thoại.

## Giai đoạn 2 — Bảng shot chi tiết

| Video | SF | Text (thoại · lời dẫn) | Từ | Shot con (giây) | Góc | Nhạc |
|---|---|---|---|---|---|---|
| V-S1-01 | SF-S1-01 | BRYCE "Don't move. Follow me." · NAR "The millionaire looked down…" · GORDON "Excuse me?" · BRYCE "Don't move, sir. Follow me. Now." | 30 | 5 · 5 · 5 | Medium Two-Shot → Low-Angle MCU → Medium Two-Shot đảo trục | — (có thoại) |
| V-S1-02 | SF-S1-02 | NAR "The bodyguard stepped in." · VOSS "Beat it, kid…" · NAR "The boy didn't even look at him…" · BRYCE "Please, sir…" | 39 | 5 · 5 · 5 | Medium Wide 3-4 → **OTS qua vai Voss** → MCU Bryce | — (có thoại) |
| V-S1-03 | SF-S1-03 | NAR "Something in that voice…" · "The sidewalk behind him exploded." · "Half a ton of glass…" | 43 | 4 · 5 · 6 | Medium Two-Shot theo bước → Cinematic Wide (cú rơi) → Insert điện thoại | **ĐẨY** |
| V-S1-04 | SF-S1-04 | NAR "A whole street stood frozen…" · "Gordon Pierce opened his mouth…" · "He didn't know the boy's name yet…" | 38 | 5 · 5 · 5 | Cinematic Wide → MCU Gordon → Medium Two-Shot | **KÌM** |
| V-S1-05 | SF-S1-05 | NAR "Have you ever wondered… after his own funeral," | 29 | 5 · 5 · 5 | Medium Two-Shot → MCU Bryce → Cinematic Wide | **NÂNG** |
| V-S1-06 | SF-S1-06 | NAR "so drop a like… where it started." · "To understand what happened…" | 42 | 5 · 5 · 5 | Medium Wide 3-4 → MCU Bryce → Cinematic Wide | **ĐẨY** |
| V-S2-01 | SF-S2-01-MASTER | NAR "Bryce Tanner was eleven years old… at Mercy General." | 26 | 5 · 5 · 5 | Cinematic Wide bếp → Medium → MCU | **NGHỈ** |
| V-S2-02 | SF-S2-02 | NAR "She got home a few minutes after seven… bruise cut away." · "He'd learned that trick from his father." | 40 | 5 · 5 · 5 | Medium → Insert quả táo → MCU | **KÌM** |

Tổng 287 từ · trần cứng 46 từ/video, video nặng nhất là V-S1-03 với 43 từ lời dẫn.

## Kiểm bằng máy

```bash
python3 sfboard/kiem-luat.py HOOK-BRYCE--DUNG-CU-DONG-DI-THEO-TOI.project
python3 sfboard/kiem-noi-shot.py HOOK-BRYCE--DUNG-CU-DONG-DI-THEO-TOI.project --day-du
```

Trạng thái 2026-08-28: `kiem-luat.py` ✓ SẠCH · `kiem-noi-shot.py` 0 mối cần nhịp chuyển.

## Hai điểm cần user quyết

1. **Cú rơi kính và LUẬT-an-toàn (trẻ em trong khung cảnh tai nạn).** `LUAT-an-toan.md`
   cấm cho trẻ lên hình trong cảnh tai nạn. Đây là lõi của hook nên không bỏ được;
   cách xử đang dùng: kiện kính đập xuống khoảng vỉa hè TRỐNG, Bryce và Gordon đã
   cách bốn mét và hoàn toàn ngoài vùng rơi, ban ngày sáng rõ, không máu, không ai
   bị thương, không ai nằm trong bãi kính — các câu chặn này đã ghi cứng vào prompt
   V-S1-03 và cả ba Thumbnail. Nếu muốn hạ thêm một nấc, cắt Bryce hẳn ra khỏi
   SHOT 2 của V-S1-03 và chỉ giữ cú rơi ở góc rộng không người.

2. **Mốc cắt 2 phút.** Dừng đúng ở "He'd learned that trick from his father." vì câu
   kế tiếp (đoạn Andre nói về quả táo, 30 từ) sẽ đẩy V-S2-02 lên 70 từ — vượt trần
   cứng 46 từ/video và buộc phải mở video thứ 9 (135 giây). Muốn lấy trọn đoạn đó
   thì phải chấp nhận 9 video.
