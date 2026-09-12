# BẢNG SHOT — HOOK-AUTO-17

Cổng số từ: **174 từ → ceil(174 ÷ 26) = 7 clip**, nhưng đoạn cắt lời Kirsch ↔ Stroud được **tách làm 2 clip theo yêu cầu user** → **6 clip × 10s + 2 clip × 6s = 8 clip, 72 giây** (`7-bang-shot.md` §5.2b). 0 nhịp lặng. 0 SF dùng lại (8 SF cho 8 shot).
Prompt video theo biến thể "không lồng narrator" (`11-prompt-video.md` §3.3), giống cả ba Golden Project: văn kể được chừa khoảng lặng trong khối TIMING.

## Bố trí phòng xử (khoá trục cho mọi khung)

Nhìn từ khán phòng lên bục: **bàn bào chữa + dãy cửa sổ bên TRÁI**, bàn công tố + hộp bồi thẩm (trống) bên PHẢI.
Ở bàn bào chữa, Tavion đứng phía cửa sổ, Stroud đứng phía lối giữa. Corliss ngồi **đầu hàng ghế thứ hai sát lối đi hông cửa sổ**,
cách con khoảng 2,5 m (khớp chi tiết "eight feet" và lối đi hông mà viên chấp pháp đi xuống ở phần sau).
Mọi máy đặt cùng phía cửa sổ của trục Kirsch–Corliss → Kirsch luôn nhìn về phải khung, Corliss luôn nhìn về trái khung.

## Cụm không gian & Master SF

| Cụm | Máy đứng đâu, chĩa về đâu | Master SF | Con của cụm |
|---|---|---|---|
| 1 — nhìn lên bục | khán phòng / bàn bào chữa → bục | `SF-HOOK-M1-MASTER` | SF-HOOK-03 · SF-HOOK-05 |
| 2 — trục ngang & nhìn xuống khán phòng | lối hông cửa sổ / trên bục bên phải Kirsch → khán phòng | `SF-HOOK-M2-MASTER` | SF-HOOK-03B · SF-HOOK-04 · SF-HOOK-06 · SF-HOOK-07 |

Corliss đứng dậy là một Blocking Shift, nhưng nó xảy ra **bên trong** V-HOOK-06 (Shot 1). Khung duy nhất sau đó có bà
đứng là SF-HOOK-07, nơi bà chỉ là dáng nhỏ ngoài nét ở hậu cảnh — nên không dựng Master thứ ba (dựng thì góc rộng lên 3/7 = 43%).
Prompt SF-HOOK-07 ghi thẳng "Corliss ĐÃ ĐỨNG THẲNG" để AI không bê tư thế ngồi từ Master 2 sang.

## Bảng shot

| Shot | SF | Cỡ cảnh | dur | Từ | Giây thoại | Lấp | Thoại / dẫn |
|---|---|---|---|---|---|---|---|
| V-HOOK-01 | `SF-HOOK-M1-MASTER` | Wide (rộng) | 10 | 24 | 8,0s | 80% | KIRSCH "Trash raises trash. Sit down." + dẫn |
| V-HOOK-02 | `SF-HOOK-M2-MASTER` | Lateral Wide (rộng) | 10 | 24 | 8,0s | 80% | dẫn giới thiệu Corliss + KIRSCH gọi lấy tên |
| V-HOOK-03 | `SF-HOOK-03` | OTS qua vai Stroud (góc đôi) | 6 | 13 | 4,3s | 72% | KIRSCH "Spell it out loud." → STROUD bị cắt lời → KIRSCH "Sit down, counselor." |
| V-HOOK-03B | `SF-HOOK-03B` | Medium two-shot trục ngang (góc đôi) | 6 | 11 | 3,7s | 61% | STROUD "Your Honor—" → KIRSCH "I said sit down." + "He never looked at her." |
| V-HOOK-04 | `SF-HOOK-04` | Medium wide 3/4 hai lớp (góc đôi) | 10 | 25 | 8,3s | 83% | KIRSCH hạch hỏi + "Nobody answered for her." |
| V-HOOK-05 | `SF-HOOK-05` | MCU dirty single (cận) | 10 | 25 | 8,3s | 83% | KIRSCH câu phân loại người |
| V-HOOK-06 | `SF-HOOK-06` | Medium dirty single (trung) | 10 | 27 | 9,0s | 90% | Corliss đứng lên & nói → KIRSCH "Noted for the record." |
| V-HOOK-07 | `SF-HOOK-07` | Medium 3/4 (trung) | 10 | 25 | 8,3s | 83% | KIRSCH "Next case." + ba câu khép Hook |

## Tự kiểm định mức

| Định mức | Ngưỡng | Thực tế | |
|---|---|---|---|
| Mốc `dur` | 10s · cặp tách thoại dồn 6s | 6×10 + 2×6 = 72s | ✅ |
| Số shot | ceil(174÷26) = 7, +1 mỗi lần tách | 8 | ✅ |
| Trần thoại | ≤28 từ (10s) · ≤16 từ (6s) | max 27 · 13 | ✅ |
| Sàn lấp đầy | ≥24 từ cho clip 10s · clip 6s miễn | min 24 | ✅ |
| Nhịp lặng | 0% | 0 | ✅ |
| Tái sử dụng SF | 0% — số SF = số shot | 8 SF / 8 shot | ✅ |
| Cận/trung | 40–50% | 3/8 = 38% | ⚠️ |
| Góc đôi | 20–30% | 3/8 = 38% | ⚠️ |
| Góc rộng | 20–25% | 2/8 = 25% | ✅ |
| Đặc tả | ~2% | 0 | ✅ |
| Khối kết clip | <7% | 0 | ✅ |
| Prompt video | 2.000–2.800 (6s chỉ ≤2.800) | 2.487–2.780 | ✅ |
| Thẻ địa điểm | ≤1.400 ký tự · 200–300 từ | 1.374 · 296 | ✅ |
| Master / SF thường | ≤1.400 / <1.000 | 1.066–1.119 / 759–965 | ✅ |
| Diff `shot.text` với kịch bản | khớp 100% | 174/174 từ, đúng thứ tự | ✅ |

### ⚠️ Ba chỗ lệch có lý do
1. **Góc rộng 29%**: n = 7 nên không số nguyên nào rơi vào băng 20–25% (1/7 = 14%, 2/7 = 29%). Chọn 2 vì cần hai Master cho hai trục.
2. **Định mức đủ cast (≥60%) ở cụm 1**: chỉ Master 1 có đủ bốn người (1/3). Hai khung con của cụm 1 nhìn lên bục, còn Corliss ngồi
   sau lưng máy — muốn nhét bà vào phải đảo trục. Cụm 2 đạt 3/4 = 75%. Khung chỉ có 2 người: 1/7 = 14% (≤20% ✅).
3. **Một mối cắt giữa câu dẫn**: dò vét cạn mọi cách chia 174 từ thành 7 nhóm 24–28 từ — không có cách nào cắt trọn ranh giới câu, kể cả
   cho phép cắt ở dấu phẩy. Phương án tối ưu có đúng một mối cắt, rơi vào lời dẫn: V-HOOK-01 kết ở *"…He meant the"*, V-HOOK-02 mở bằng
   *"woman in row two."* Lời dẫn là track voice-over hậu kỳ chạy liền, người xem chỉ thấy hình cắt.

## Cử chỉ kìm nén — mỗi cái đúng một lần trong cả Hook

| Nhân vật | Clip | Cử chỉ | Vì sao hợp hoàn cảnh |
|---|---|---|---|
| Corliss | V-02 | mi mắt nhắm một nhịp chậm rồi mở, mắt vẫn trên Kirsch · hàm siết | nhận chữ "rác" mà không để lộ ra (2026-09-11: bỏ cử chỉ liếc đồng hồ — sai khoảnh khắc, user chê) |
| Corliss | V-04 | mắt ngước lên vách trên đầu thẩm phán, không nhìn con · nuốt khan (Shot 2) | kịch bản: nhìn con thì con sẽ lên tiếng |
| Corliss | SF-06 / V-06 | cánh mũi phập phồng (ảnh) · mím môi một nhịp (video) · ngón cái đè phẳng tấm vé | tấm vé là chi tiết kịch bản |
| Tavion | V-02 | hít vào bằng mũi rồi giữ hơi | — |
| Tavion | V-04 | đầu định quay về hàng ghế thứ hai, dừng, mắt trả về phía trước | nghe lời luật sư "Eyes front" |
| Stroud | V-03B | bước nửa bước lên chắn trước thân chủ, bị cắt lời thì miệng khép lại, rút chân về chỗ cũ | cố bảo vệ thân chủ rồi phải lùi (thay cử chỉ giơ bàn tay — user chê) |

Không dùng "nắm tay siết" ở đâu cả; mọi SF thấy tay đều có câu chặn "không nắm chặt".
Kirsch rõ nét ở V-01/02/03/05/07, clip nào cũng có một hành vi khoe cái ác cho cả phòng (liếc khán phòng xem họ có nghe không,
búng hai ngón về hàng ghế như chỉ món hàng, giơ một ngón cắt lời mà không ngẩng lên, ném nửa câu về khán phòng, chia chiến thắng với bàn thư ký).

## Lịch sử sửa
- 2026-09-11 · V-HOOK-02 · bỏ cử chỉ Corliss liếc đồng hồ (sai hoàn cảnh), thay bằng mi mắt nhắm một nhịp chậm.
- 2026-09-11 · SF-HOOK-04 + V-HOOK-04 · bỏ góc sau lưng Kirsch — ông là người nói chính mà chỉ thấy gáy. Dựng lại thành trung-rộng 3/4 hai lớp từ trên bục bên phải ông: Kirsch rõ mặt tiền cảnh trái, bàn bào chữa và Corliss ở hậu cảnh phải. Ảnh SF-HOOK-04_v1 và video V-HOOK-04_v2 cần sinh lại.
- 2026-09-11 · V-HOOK-03 · tách thành V-HOOK-03 + V-HOOK-03B theo yêu cầu user (quá nhiều thoại ngắn liên tiếp trong một clip). Hai clip này chấp nhận dưới sàn 24 từ; thời lượng Hook thành 80s. Mã `03B` dùng hậu tố thay vì đánh lại số 04–07, vì media đã chốt đặt tên theo mã. Thay hành động của Stroud: bỏ giơ bàn tay xin phát biểu, V-03 chỉ ngả người về phía bục (quay lưng), V-03B bước nửa bước chắn trước thân chủ rồi rút về. Video V-HOOK-03_v1 cần sinh lại; SF-HOOK-03_v1 vẫn dùng được.
- 2026-09-11 · V-HOOK-03 + V-HOOK-03B · đổi sang `dur: 6` theo user, viết lại prompt khung 0:00–0:06. Luật tách thoại dồn → 2 clip 6s đã ghi vào skills-hook (`7-bang-shot.md` §5.2b). Hook còn 72s.
- 2026-09-11 · V-HOOK-03B · AI video gán nhầm người nói. Sửa: mỗi shot con một người nói (Shot 1 0:00–0:02 Stroud, Shot 2 0:02–0:06 Kirsch + khoảng lặng dẫn), mọi dòng thoại và LIP SYNC gọi người nói bằng màu áo + vị trí (tan suit / black robe), Stroud được 2s thay vì 1s. Cần sinh lại video.
