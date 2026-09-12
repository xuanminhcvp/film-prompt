# BẢNG SHOT — HOOK-AUTO-18

Cổng số từ: **261 từ → ceil(261 ÷ 26) = 11 clip × 10s = 110 giây** (`1-kich-ban.md` §2.1). Không có chuỗi thoại dồn (≥4 lượt ngắn đổi người nói) nên không tách clip 6s. 0 nhịp lặng. 0 SF dùng lại (11 SF cho 11 shot).
Prompt video theo biến thể "không lồng narrator" (`11-prompt-video.md` §3.3), giống AUTO-17 và ba Golden Project: văn kể được chừa khoảng lặng trong khối TIMING.

## Thoại tiếng Nhật trong video

Kịch bản giữ 100% tiếng Anh (luật kênh). Riêng prompt video, bốn câu Preston nói "in Japanese" được viết **bằng chữ Nhật để AI video phát âm tiếng Nhật**, kèm nghĩa tiếng Anh trong ngoặc. Câu của Isaiah vẫn là tiếng Anh. `shot.text` giữ nguyên văn tiếng Anh.

| Clip | Câu kịch bản | Câu Preston nói trong video |
|---|---|---|
| V-03 | "Go ahead. The driver doesn't understand a word," | 「どうぞ。運転手は一言もわからないから。」 |
| V-04 | "He comes with the upholstery." | 「あいつは座席の付属品みたいなもんだ。」 |
| V-05 | "She signs at four. Power of attorney. She thinks it's for the taxes." | 「四時に署名する。委任状だ。税金の書類だと思ってる。」 |
| V-06 | "The house is sold by spring, and she's in a care home by Christmas." | 「家は春までに売って、クリスマスまでには老人ホームだ。」 |

## Bố trí khoang xe (khoá trục cho mọi khung)

Xe tay lái thuận: **Isaiah ở ghế lái bên TRÁI xe**, ghế phụ trống. Vách ngăn sau hai ghế trước đã hạ kính hết.
Băng ghế sau ngay sau vách: **Preston ngồi lệch vào giữa, sau lưng ghế lái**, nên mặt ông lọt khe giữa hai tựa đầu và chồm tới được gương chiếu hậu.
**Margaret sát cửa bên PHẢI xe.** Điện thoại nằm trên tay vịn gập giữa hai người. Xì gà luôn ở tay trái Preston.
Khi chồm tới, cẳng tay trái Preston gác đỉnh lưng ghế lái → tàn tro rơi xuống **vai PHẢI** Isaiah (máy đặt ở ghế phụ hoặc kính chắn gió đều thấy vai này).

Trạng thái liên tục: gương bình thường (M1) → hất lên trần ở V-01 → giữ nguyên hất lên ở SF-02…SF-07 → Isaiah chỉnh lại ở V-07 → bình thường ở SF-09, SF-11.
Tro: rơi ở V-02 → nằm trên vai ở SF-03, SF-06, SF-07 → phủi ở V-07 → còn vệt nhạt ở SF-09, SF-10.

## Cụm không gian & Master SF

| Cụm | Máy đứng đâu, chĩa về đâu | Master SF | Con của cụm |
|---|---|---|---|
| 1 — trong khoang xe | trong xe, mọi hướng | `SF-HOOK-M1-MASTER` (kính chắn gió → toàn khoang) | SF-HOOK-02…07 · 09 · 10 · 11 |
| 2 — ngoài parkway | xe quay chạy trước → đầu xe limousine | `SF-HOOK-M2-MASTER` | — |

Không có Blocking Shift nào đổi chỗ ngồi trong khoang (chỉ có Preston chồm tới rồi ngả lại, nằm gọn trong V-01/V-02), nên cụm 1 chỉ cần một Master.

## Bảng shot

| Shot | SF | Cỡ cảnh | dur | Từ | Giây thoại | Lấp | Thoại / dẫn |
|---|---|---|---|---|---|---|---|
| V-HOOK-01 | `SF-HOOK-M1-MASTER` | Wide nội cảnh (rộng) | 10 | 25 | 8,3s | 83% | PRESTON "Eyes on the road…" + dẫn hất gương |
| V-HOOK-02 | `SF-HOOK-02` | Medium ba lớp (trung) | 10 | 28 | 9,3s | 93% | dẫn: tro rơi · 41 tuổi · mẹ siết túi |
| V-HOOK-03 | `SF-HOOK-03` | OTS qua vai Margaret (góc đôi) | 10 | 27 | 9,0s | 90% | dẫn: im lặng · điện thoại + PRESTON (Nhật) "Go ahead…" |
| V-HOOK-04 | `SF-HOOK-04` | Medium two-shot (góc đôi) | 10 | 24 | 8,0s | 80% | PRESTON (Nhật) "upholstery" + dẫn Margaret cười |
| V-HOOK-05 | `SF-HOOK-05` | MCU dirty single (cận) | 10 | 21 | 7,0s | 70% | dẫn + PRESTON (Nhật) "She signs at four…" |
| V-HOOK-06 | `SF-HOOK-06` | Medium dirty single (trung) | 10 | 22 | 7,3s | 73% | PRESTON (Nhật) "The house is sold…" + dẫn đường dây im |
| V-HOOK-07 | `SF-HOOK-07` | Medium (trung) | 10 | 23 | 7,7s | 77% | dẫn chỉnh gương/phủi vai/đổi làn + ISAIAH "Forty minutes…" |
| V-HOOK-08 | `SF-HOOK-M2-MASTER` | Wide ngoại cảnh (rộng) | 10 | 26 | 8,7s | 87% | dẫn: limo không lệch · Preston tin tài xế chỉ nghe đường |
| V-HOOK-09 | `SF-HOOK-09` | Insert gương chiếu hậu (đặc tả) | 10 | 26 | 8,7s | 87% | dẫn "By four o'clock…" + CTA đoạn 1 |
| V-HOOK-10 | `SF-HOOK-10` | Close-up (cận) | 10 | 18 | 6,0s | 60% | CTA đoạn 2 |
| V-HOOK-11 | `SF-HOOK-11` | OTS medium wide (góc đôi) | 10 | 21 | 7,0s | 70% | CTA đoạn 3 |

## Tự kiểm định mức

| Định mức | Ngưỡng | Thực tế | |
|---|---|---|---|
| Mốc `dur` | 10s | 11 × 10 = 110s | ✅ |
| Số shot | ceil(261÷26) = 11 | 11 | ✅ |
| Trần thoại | ≤28 từ | max 28 | ✅ |
| Sàn lấp đầy | ≥24 từ / clip 10s | 6 clip dưới 24 (min 18) | ⚠️ |
| Chuỗi thoại dồn | tách nếu ≥4 lượt ngắn | 0 | ✅ |
| Nhịp lặng | 0% | 0 | ✅ |
| Tái sử dụng SF | 0% — số SF = số shot | 11 SF / 11 shot | ✅ |
| Cận/trung | 40–50% | 5/11 = 45% | ✅ |
| Góc đôi | 20–30% | 3/11 = 27% | ✅ |
| Góc rộng | 20–25% | 2/11 = 18% | ⚠️ |
| Đặc tả | ~2% | 1/11 = 9% | ⚠️ |
| Cụm ≥3 main cast (cụm 1) | ≥60% đủ mặt · ≤20% chỉ 2 người | 9/10 = 90% · 1/10 = 10% | ✅ |
| Khối kết clip | <7% | 0 | ✅ |
| Prompt video | 2.000–2.800 | 2.195–2.796 | ✅ |
| Thẻ địa điểm | ≤1.400 ký tự · 200–300 từ | 1.372 / 292 · 1.231 / 256 | ✅ |
| Master / SF thường | ≤1.400 / <1.000 | 951–1.248 / 515–832 | ✅ |
| Diff `shot.text` với kịch bản | khớp 100% | 261/261 từ, đúng thứ tự | ✅ |

### ⚠️ Ba chỗ lệch có lý do
1. **Sàn 24 từ**: 11 × 24 = 264 > 261 từ, nên không thể cho mọi clip đạt sàn khi số clip theo đúng công thức. Thêm vào đó câu CTA 52 từ phải tách ba (câu đầu 31 từ vượt trần 28), và câu thoại tiếng Nhật 27 từ của Preston phải tách hai — mọi mối cắt đều ở ranh giới câu hoặc liên từ ("when"), không cắt giữa cụm. Clip thấp nhất (V-10, 18 từ) là đoạn giữa của CTA, khoảng lặng cuối clip là nhịp giữ cho khuôn mặt Isaiah.
2. **Góc rộng 18% / đặc tả 9%**: n = 11 nên không số nguyên nào rơi vào băng 20–25% (2/11 = 18%, 3/11 = 27%). Trong khoang xe không đặt được khung rộng thứ ba có nghĩa. Clip đặc tả là cái gương chiếu hậu — đúng hình ảnh câu CTA gọi tên ("a rich man's smile … in a rearview mirror"), có mặt người phản chiếu nên không phải insert thuần đạo cụ.
3. **Isaiah không nói gì trong 6/11 clip** — đúng kịch bản (anh chỉ có một câu). Mọi clip có anh RÕ NÉT đều có hành vi kìm nén riêng, không lặp.

## Cử chỉ kìm nén — mỗi cái đúng một lần trong cả Hook

| Nhân vật | Clip | Cử chỉ | Vì sao hợp hoàn cảnh |
|---|---|---|---|
| Isaiah | V-01 | mắt rời gương xuống đường · hít vào bằng mũi rồi giữ hơi | vừa bị gọi "boy" vì nhìn bà cụ |
| Isaiah | SF-02 / V-02 | cơ hàm gồ ở khớp rồi giữ | tro rơi lên vai, không được quay đầu |
| Isaiah | SF-07 / V-07 | cánh mũi nở vì nén hơi (ảnh) · một cái nuốt khan trước câu "Forty minutes…" (video) | vừa nghe trọn kế hoạch, phải nói giọng phục vụ |
| Isaiah | V-08 | các ngón siết vô lăng một nhịp rồi CHỦ ĐỘNG nới ra, xe không lệch | "The limo never drifted an inch" — cái nén đi vào tay và dừng ở đó |
| Isaiah | V-10 | mi mắt nhắm một nhịp rồi mở · môi mím một nhịp | CTA "the driver he never once looked at" |
| Isaiah | V-11 | mắt trong gương ngước lên Preston một nhịp rồi trả về đường | cú nhìn duy nhất cả Hook, gối đầu sang phần sau |
| Margaret | V-02 | ngón siết khoá túi · môi hé định nói rồi khép | kịch bản: "held her purse a little tighter. She said nothing." |
| Margaret | V-04 | nụ cười kiên nhẫn, mắt dò mặt con, gật khẽ | kịch bản: "patient and a little lost" |

Không có "nắm tay siết bên hông" ở đâu; cú siết duy nhất là tay trên vô lăng ở V-08. Mọi SF thấy tay đều có câu chặn "không nắm chặt" / "không siết".
Preston rõ nét ở V-01…06, V-09, V-11 — clip nào cũng có một hành vi khoe cái ác: quay đầu chia câu đùa với mẹ, để tro rơi mà không thèm nhìn, chĩa xì gà vào gáy tài xế như chỉ cái móc áo, vỗ lưng ghế lái như vỗ đồ nội thất, liếc mẹ như người mua liếc món hàng đã trả tiền, nhìn gáy tài xế thẩm định trong lúc luật sư im lặng, thổi khói về ghế lái và lướt mắt qua gương mà không dừng, duỗi tay chiếm lưng ghế.

## Lịch sử sửa
- (chưa có)
