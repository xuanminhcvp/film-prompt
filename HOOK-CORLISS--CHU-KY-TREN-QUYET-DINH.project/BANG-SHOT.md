# BẢNG SHOT — HOOK-CORLISS--CHU-KY-TREN-QUYET-DINH

Cổng số từ: **174 từ → ceil(174 ÷ 26) = 7 clip × 10s = 70 giây**. 0 nhịp lặng.

## Cụm không gian & Master SF

| Cụm | Máy đứng đâu, chĩa về đâu | Master SF | Nuôi shot | Con của cụm |
|---|---|---|---|---|
| 1 — trục trước | lối đi giữa khán phòng → bục | `SF-S1-M1-MASTER` | V-S1-01 | SF-S1-03 · SF-S1-04 · SF-S1-05 |
| 2 — trục ngang | hông phòng cạnh cửa sổ → cắt ngang bục + khán phòng | `SF-S1-M2-MASTER` | V-S1-06 | SF-S1-02 |

Corliss đứng lên là một Blocking Shift, nhưng nó xảy ra **bên trong** V-S1-06 (kết clip dạng 1 —
đổi tư thế) và không shot nào sau đó cần khung có bà đứng, nên không dựng Master thứ ba.

## Bảng shot

| Shot | SF | Cỡ cảnh | dur | Từ | Giây thoại | Lấp | Thoại / dẫn |
|---|---|---|---|---|---|---|---|
| V-S1-01 | `SF-S1-M1-MASTER` | Wide (rộng) | 10 | 24 | 8,0s | 80% | KIRSCH "Trash raises trash. Sit down." + dẫn |
| V-S1-02 | `SF-S1-02` | Medium Wide 3-4 (góc đôi) | 10 | 24 | 8,0s | 80% | dẫn + KIRSCH gọi thư ký lấy tên |
| V-S1-03 | `SF-S1-03` | OTS (góc đôi) | 10 | 24 | 8,0s | 80% | loạt cắt lời: KIRSCH ↔ STROUD ×5 lượt |
| V-S1-04 | `SF-S1-04` | MCU eye-level (cận) | 10 | 25 | 8,3s | 83% | KIRSCH hạch hỏi + dẫn (không ai đáp) |
| V-S1-05 | `SF-S1-05` | MCU low angle (cận) | 10 | 25 | 8,3s | 83% | KIRSCH câu phân loại người |
| V-S1-06 | `SF-S1-M2-MASTER` | Lateral Wide (rộng) | 10 | 27 | 9,0s | 90% | Corliss đứng lên & nói → KIRSCH đáp |
| V-S1-07 | `SF-S1-04` ♻ | MCU eye-level (cận) | 10 | 25 | 8,3s | 83% | KIRSCH "Next case." + hai câu khép hook |

♻ = dùng lại SF cũ, không sinh ảnh mới. Tổng SF cần sinh: **6** (2 Master + 4 SF thường).

## Tự kiểm định mức

| Định mức | Ngưỡng | Thực tế | |
|---|---|---|---|
| Mốc `dur` | 10s cho mọi shot | 7×10 | ✅ |
| Số shot | ceil(174÷26) = 7 | 7 | ✅ |
| Tổng thời lượng | số shot × 10s | 70s | ✅ |
| Trần thoại | ≤28 từ | max 27 | ✅ |
| Sàn lấp đầy | ≥80% dur (≥24 từ) | min 80%, max 90% | ✅ |
| Nhịp lặng | 0% | 0 | ✅ |
| Cận/trung | 40–50% | 3/7 = 43% | ✅ |
| Góc đôi | 20–30% | 2/7 = 29% | ✅ |
| Góc rộng | 20–25% | 2/7 = 29% | ⚠️ làm tròn |
| Góc đặc tả | ~2% | 0 | ✅ |
| Tái sử dụng SF | 20–25% | 1/7 = 14% | ⚠️ làm tròn |
| Trần ký tự prompt video | 2.000–2.800 | 2.409–2.796 | ✅ |
| Trần ký tự Master / SF thường | 1.400 / <1.000 | 1.228–1.284 / 667–832 | ✅ |
| Diff text với kịch bản gốc | khớp 100% | khớp 100% | ✅ |

### ⚠️ Hai chỗ lệch do làm tròn ở n = 7
Phim chỉ có 7 shot nên không số nguyên nào rơi đúng vào băng 20–25%: 1/7 = 14%, 2/7 = 29%.
- **Góc rộng**: chọn 2 (29%) vì 1 khung rộng không đủ thiết lập cả hai trục (trục trước và trục ngang).
- **Tái sử dụng SF**: chỉ đạt 1 lần (14%). Lý do là nội dung, không phải cẩu thả — 7 shot rơi vào
  7 thế trận khác nhau; cặp duy nhất trùng hoàn toàn nhân vật · góc · tư thế · nón quan sát là
  V-S1-04 và V-S1-07 (Kirsch cận ngang tầm mắt ở bục). Ép thêm một lần dùng lại sẽ phá tỉ lệ cỡ cảnh.

### Ghi chú một chỗ cắt giữa câu dẫn chuyện
Không tồn tại cách chia nào cho 174 từ thành 7 nhóm 24–28 từ mà mọi mối cắt đều rơi đúng ranh giới
câu (đã dò vét cạn toàn bộ tổ hợp). Phương án tối ưu chỉ có **đúng một** mối cắt giữa câu dẫn:
V-S1-01 kết ở *"…He meant the"* và V-S1-02 mở bằng *"woman in row two."* — lời dẫn là một track
voice-over chạy liên tục nên người xem chỉ thấy hình cắt, không thấy câu đứt.
