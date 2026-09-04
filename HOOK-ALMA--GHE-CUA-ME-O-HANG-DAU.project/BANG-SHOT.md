# BẢNG SHOT — HOOK · ALMA · GHẾ CỦA MẸ Ở HÀNG ĐẦU

**Đơn vị bàn giao**: 9 video full 15 giây (2:15) · 9 Start Frame nuôi video · 4 Master SF chốt thế trận
(không nuôi video) · 3 Thumbnail. Mỗi video = 3 shot con nối bằng 2 cú Hard Cut, mỗi shot con ≥ 3 giây.

**Phạm vi text**: 100% nguyên văn kịch bản gốc, theo đúng thứ tự tuyến tính, từ câu đầu tiên đến hết
*"...those ones somehow always got the bigger scoop."*

---

## Giai đoạn 1 — Phân rã thế trận (Blocking Shifts)

| Cụm | Không gian | Điểm khựng làm vỡ thế trận | Master SF |
|---|---|---|---|
| A | Vườn cưới — hàng ghế cuối | Alma ngồi, hai an ninh kèm hai bên, hàng ghế bên cạnh trống | `SF-S1-M1-MASTER` |
| B | Vườn cưới — bục altar | Đôi tân hôn trên bục, Frederick + Vivian ở hàng ghế đầu | `SF-S1-M2-MASTER` |
| C | Vườn cưới — lối đi đoạn cuối | Julian đi hết lối đi, đứng đối diện Alma → thế trận mới | `SF-S1-M3-MASTER` |
| D | Vườn cưới — trục lối đi (khung gối đầu bục ↔ cuối lối đi) | Máy quay đứng vuông góc trục, thấy cùng lúc hai đầu vườn | `SF-S1-M4-MASTER` |
| E | Bếp dinh thự Hartwell — tuyến quá khứ 30 năm trước | Nhảy dòng thời gian | `SF-S1-07-MASTER` (kiêm SF) |
| F | Nhà ăn trường Jefferson — hiện tại | Nhảy về hiện tại, địa điểm mới | `SF-S1-08-MASTER` (kiêm SF) |

Ranh giới đổi không gian **trùng khít ranh giới video** — không có cú Hard Cut nội bộ nào nhảy sang bối cảnh mới.

---

## Giai đoạn 2 — Bảng shot chi tiết

| Video | SF | Cụm | Thoại / Lời dẫn | Từ | Phân rã 3 shot con (giây) | Nhịp |
|---|---|---|---|---|---|---|
| `V-S1-01` | `SF-S1-01` | A | GUARD: *"Ma'am, I need you to come with me. Quietly."* + lời dẫn (hai bảo vệ · nhặt ví) | 33 | 5 + 5 + 5 — Medium Two-Shot → Cinematic Wide hàng ghế trống → MCU nhấc ví | thoại |
| `V-S1-02` | `SF-S1-02` | A | ALMA: *"I don't want any trouble," … "I'll go."* + lời dẫn (bốn trăm con mắt · bốn bước) | 38 | 5 + 5 + 5 — 3/4 Two-Shot đứng dậy → Cinematic Wide đi dọc lối đi → MCU khựng lại quay đầu | thoại · `chuyen` |
| `V-S1-03` | `SF-S1-03` | B | JULIAN: *"Stop."* + lời dẫn (bước xuống bục · đi ngược lối đi) | 44 | 4 + 5 + 6 — Medium Wide lên bục → Medium theo Julian xuống bậc → 3/4 Two-Shot hàng ghế đầu | thoại · `chuyen` |
| `V-S1-04` | `SF-S1-04` | C | JULIAN: *"Mom," … "Your seat is in the front."* + lời dẫn (lấy ví khỏi tay bà) | 25 | 5 + 5 + 5 — 3/4 Two-Shot lấy ví → **OTS qua vai Alma** → Clean Single cận trung Alma | thoại |
| `V-S1-05` | `SF-S1-05` | D | Lời dẫn: cô dâu là người duy nhất mỉm cười + nửa đầu câu CTA | 26 | 5 + 5 + 5 — Medium Sophie → MCU nụ cười → Cinematic Wide chéo trục lối đi | `[NHỊP]` KÌM |
| `V-S1-06` | `SF-S1-06` | D | Nửa sau câu CTA (like · comment) | 23 | 5 + 5 + 5 — Cinematic Wide toàn cảnh → Medium Two-Shot → Cinematic Wide cao hơn tầm mắt | `[NHỊP]` ĐẨY |
| `V-S1-07` | `SF-S1-07-MASTER` | E | Lời dẫn: quay về ba mươi năm trước · căn bếp có mùi quế | 40 | 5 + 5 + 5 — Cinematic Wide bếp → Medium nhấc khay → Medium Wide nhìn ra hành lang trống | `[NHỊP]` NÂNG · `hoituong` |
| `V-S1-08` | `SF-S1-08-MASTER` | F | Lời dẫn: Alma 58 tuổi · 18 năm dây chuyền bữa sáng · 4h40 sáng | 39 | 5 + 5 + 5 — Cinematic Wide nhà ăn → Medium múc thức ăn → Medium Wide dọc đường ray | `[NHỊP]` NGHỈ · `chuyen` |
| `V-S1-09` | `SF-S1-09` | F | Lời dẫn: bọn trẻ gọi bà là Miss Alma · muôi bao giờ cũng đầy hơn | 23 | 5 + 6 + 4 — Medium Alma → MCU muôi thứ hai → Medium Wide em học sinh đi tiếp | `[NHỊP]` KÌM |

Trần cứng 46 từ/video — video nhiều chữ nhất là `V-S1-03` (44 từ).

---

## Kiểm bằng máy

```bash
python3 sfboard/kiem-luat.py HOOK-ALMA--GHE-CUA-ME-O-HANG-DAU.project
python3 sfboard/kiem-noi-shot.py HOOK-ALMA--GHE-CUA-ME-O-HANG-DAU.project S1 --day-du
```

- `kiem-luat.py`: **✓ SẠCH** (0 lỗi).
- `kiem-noi-shot.py`: còn 5 nhắc ở hai mối `V-S1-04 → V-S1-05` và `V-S1-05 → V-S1-06`. Cả hai là **đổi cụm
  không gian trong cùng khu vườn, không phải người di chuyển** — và cả hai đã được vá đúng cách skill quy
  định: video sau là **nhịp không thoại**. Script chưa đọc tag `[NHỊP]` nên vẫn nhắc.

## Việc còn lại

1. Sinh ảnh 12 thẻ REF (nhân vật · đạo cụ · 3 bối cảnh) → duyệt → mới sinh ảnh SF.
2. Sinh 4 Master SF, rồi 9 Start Frame.
3. Sinh 3 Thumbnail (`SF-THUMB-01/02/03`), tinh chỉnh bằng Menu 1-5 ghi ở trường `notes`.
4. Chọn phương án nhạc A (có lời) hoặc B (không lời) cho 5 nhịp không thoại.
