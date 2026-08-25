# Phong cách riêng (Custom Rules)

> **LƯU Ý QUAN TRỌNG:** Các quy tắc trong file này là **GHI ĐÈ (OVERRIDE)** và có mức ưu tiên cao nhất, thay thế cho các định nghĩa cũ bị mâu thuẫn ở `1-chia-shot.md`, `4-prompt-video.md` và `6-tu-duy-dien-anh.md`. Một luật chỉ được định nghĩa ở đây để tránh mâu thuẫn.

## 1. Tỷ lệ Hạn mức Hard-cut
Sử dụng bộ tỷ lệ (%) làm chuẩn cho các clip:
- 10s · nhịp lặng · ≤2 người: 40%
- 10s · nhịp lặng · ≥3 người: 25%
- 10s · thoại · ≤2 người: 30%
- 10s · thoại · ≥3 người: 20%
- 6s · thoại · ≤2 người: 10%
- 6s · thoại · ≥3 người: 5%
- 6s · nhịp lặng: 0%

## 2. Quy tắc 1 Clip = 1 Shot (Cập nhật đồng bộ)
- **Thay thế cho `1-chia-shot.md`**: "Hard-cut trong 1 clip là ngoại lệ có hạn mức — xem bảng hạn mức. Ngoài hạn mức thì tách 2 shot 2 SF."
- **Thay thế cho `4-prompt-video.md`**: "Mặc định 1 clip = 1 shot. Clip có khai ô `cat` thì dùng form HAI ĐOẠN."
- **Thay thế cho `6-tu-duy-dien-anh.md` (Mức C)**: Cấm 6 cú đích danh, `pull-back` được phép có điều kiện; và câu "dùng Edit thay Camera Move" nay trỏ về hạn mức cut chứ không còn là lời khuyên trống.

## 3. Khối HAI ĐOẠN (clip có hard cut)
*(Bổ sung vào `4-prompt-video.md` ngay sau mục "Form Prompt Video Chuẩn")*

Chỉ viết khi ô shot có khai `cat` (giây xảy ra cut). Không khai `cat` mà viết hai đoạn = lỗi; khai `cat` mà viết một shot liền = lỗi.

**Câu khóa:**
> Hai đoạn liền nhau trong cùng một bối cảnh, tổng <N> giây. Đúng MỘT hard cut ở giây <cat>, không dissolve, không morph, không cut thêm ở chỗ nào khác.
> 
> 0-<cat>s — <cỡ cảnh>, <ai trong khung>, camera <TĨNH / một cú Mức ○>.
> <cat>-<N>s — vẫn <bối cảnh nhắc lại bằng 5-8 chữ>; đổi sang <cỡ cảnh mới> trên CÙNG một trục. Trong khung có/CHỈ còn <danh sách người>. <chỉ định chỗ cut theo lời thoại>.

*(Footer, khối Nhận diện, khối thoại giữ y như form một-shot).*

**Điểm cắt:**
- 10s → 5/5 (55%) · 6/4 (30%) · 7/3 (15%). 
- 6s → chỉ 4/2. 
- *Cấm 3/3 ở clip thoại.*

**Kiểu cut:**
- Cùng trục đổi cỡ: 45% 
- Cắt sang đặc tả có sẵn trong khung: 30% 
- Đảo góc OTS: 20% 
- Đổi cỡ kèm giảm người: 5%

**Điều kiện cắt (Quyết định tỷ lệ đạt):**
- **Cắt trong nhịp có thoại:** cut rơi vào khoảng lặng giữa hai câu và phải viết câu đó ra; cut trùng với đổi người nói; không cắt giữa một câu dài (nếu buộc thì chỉ cắt sang đặc tả, không cắt sang mặt); nửa sau chừa 0,3-0,5s hình trước khi có tiếng; câu của ai thì người đó nét ở đúng nửa chứa câu ấy.
- **Cắt trong khung ≥3 người:** chỉ giảm người, không bao giờ tăng; bắt buộc câu "Trong khung CHỈ còn X"; giữ nguyên trái/phải; nhắc lại đúng bullet Nhận diện của người còn lại, không thêm chi tiết mới.
- **Luật chống chồng rủi ro:** clip có cat thì camera chỉ tĩnh hoặc một cú Mức ○ ở một nửa; mỗi scene ≤3 cut (scene ≥9 clip 10s được 4); không ba clip có cut liền kề.

## 4. Camera (Thay thế mục Camera hiện tại)
*Bảng cú máy bên dưới copy dán thẳng vào chỗ `Camera ...` của câu khoá.*

**○ Dùng thoải mái**
- Camera TĨNH.
- Camera PUSH-IN rất chậm khoảng 12% cỡ cảnh về phía <ai>, dừng khi <mốc>.
- Camera TĨNH, ZOOM-IN rất chậm khoảng 10% suốt clip.
- Camera TĨNH, RACK FOCUS từ <lớp trước> sang <lớp sau> vào khoảng giây <n>.
- Camera cầm tay rất nhẹ, biên độ nhỏ, không trôi khỏi bố cục.
- Camera dịch ngang rất nhẹ khoảng 4%, chậm đều, giữ nguyên bố cục.
- Camera TĨNH, nét bám theo <ai> khi <người đó di chuyển trong khung>.
- Camera chỉnh khung rất nhẹ theo <ai>, giữ <người đó> ở một phần ba <trái/phải>.
- Camera 0-4s TĨNH, 4-10s PUSH-IN rất chậm khoảng 12% cỡ cảnh.

**◐ Có điều kiện — đích đến PHẢI đã nằm trong ảnh SF**
- Camera PAN sang <phải/trái> không quá 10°, bám theo <ai>, dừng khi <mốc>.
- Camera TILT <lên/xuống> rất nhẹ từ <A> tới <B>, không quá 10°.
- Camera hạ/nâng rất nhẹ khoảng 6%, về ngang tầm mắt <ai>.
- Camera lượn sang <phải/trái> không quá 15° quanh <ai>, giữ nguyên cỡ cảnh.
- Camera DOLLY ngang rất chậm bám <ai> đi dọc <đường đi>, giữ nguyên cỡ cảnh.
- Camera PUSH-IN chậm khoảng 8% trong khi <ai> bước một bước về phía máy.

**● Chỉ nhịp lặng, nền đơn giản, có khung dự trữ**
- Camera PULL-BACK rất ngắn khoảng 8-10%, chậm đều, rồi dừng.

**Luật đi kèm Camera:**
- Một clip một cú máy. Ngoại lệ duy nhất là dạng hai mốc giây cùng một hướng (0-4s tĩnh, 4-10s push-in).
- Luôn có số và điểm dừng. Không có trần thì model tự đẩy quá tay.
- Khung dự trữ cho pull-back: sinh SF rộng hơn một cỡ → cắt ảnh vào 15-20% → dùng bản cắt làm start frame → prompt kéo ra đúng chừng ấy. Model chỉ trả lại phần ảnh có thật, cú ● tụt xuống gần ○. Không có khung dự trữ thì không được viết pull-back.
- Dutch angle khai ở prompt SF như bố cục tĩnh, không viết thành động tác lăn máy.
- **CẤM TOÀN BỘ:** orbit trọn vòng, crane, tracking ra ngoài frame, whip pan, snap zoom, foreground wipe, dolly zoom, và mọi chữ revealing / pull back to show.

**Bảng phân bổ Camera:**
| Nhóm | Tĩnh | ○ | ◐ | ● |
|---|---|---|---|---|
| 6s | 60% | 33% | 7% | 0 |
| 10s | 35% | 40% | 20% | 5% |
| Cận | 55% | 40% (rack, breathing, micro-dolly) | 0 | 0 |
| Trung | 35% | 30% | 30% | 5% |
| Trung-rộng / rộng | 20% | 30% | 35% | 15% |
| Shot thoại | 55% | 35% | 9% | 1% |
| Nhịp lặng | 15% | 40% | 35% | 10% |

## 5. Khóa Dữ liệu Mới trong Board (`sf-board.json`)
Cần sử dụng 4 khóa sau trong file dữ liệu để thể hiện thiết kế shot (đã được thêm vào `VALID_SHOT_KEYS` của `sua-board.py` để tránh bị lọc mất):
- `cat` (số): giây xảy ra hard cut. Không có ô này = clip một shot liền.
- `goc2` (chuỗi): góc/cast của nửa sau, viết đúng văn phong ô `goc`. (Khóa này vá lỗi kiểm nối shot `kiem-noi-shot.py` để so sánh shot nối tiếp với nửa sau của clip).
- `kieu_cat` (chuỗi): `doi-co` · `dac-ta` · `dao-goc` · `giam-nguoi`.
- `cam` (chuỗi): mã cú máy (`tinh`, `pushin`, `rack`, `pan`, `pullback`…).
*(⚠️ Đừng dùng lại ô `chuyen` vì nó đang mang ý nghĩa khác cho kịch bản).*

## 6. Luật đếm được (Dành cho `kiem-luat.py`)
*(Hướng dẫn yêu cầu logic đếm cho hệ thống kiểm tra tự động)*

**Nhóm cut:**
1. `cat` chỉ hợp lệ khi `dur` ∈ {6, 10}; `dur`=10 → `cat` ∈ 3..7; `dur`=6 → `cat` = 4.
2. `dur`=6 + nhịp lặng + có `cat` → lỗi (tỷ lệ 0%).
3. Có `cat` mà prompt thiếu câu "Đúng MỘT hard cut ở giây <cat>" khớp số → lỗi. Ngược lại: prompt có hard cut/hai đoạn mà shot không khai `cat` → lỗi.
4. Có `cat` mà prompt thiếu câu "Trong khung CHỈ còn" → lỗi.
5. Tên người xuất hiện ở đoạn 2 phải là tập con của đoạn 1 → tăng người = lỗi.
6. `kieu_cat` với khung ≥3 người chỉ được `dac-ta` hoặc `giam-nguoi`.
7. Có `cat` mà `cam` thuộc nhóm ◐/● → lỗi.
8. Trần theo scene: >3 clip có `cat` trong một scene (>4 nếu scene có ≥9 clip 10s) → lỗi; ba clip có `cat` liền kề → lỗi.
9. Trần theo phim: in ra bảng 7 hạng với % thực tế vs % đích, cảnh báo khi lệch quá ±5 điểm.
10. Phân bố điểm cắt: cảnh báo nếu >70% clip 10s dùng cùng một kiểu chia (tránh 5/5 đều đặn).

**Nhóm camera:**
11. Chặn từ khoá còn cấm: orbit, crane, tracking, revealing, whip, snap zoom, dolly zoom, pull back to show.
12. `pullback` mà SF không khai khung dự trữ → lỗi (cần thêm cờ `khung_du_tru` ở SF, hoặc quy ước ghi trong MÁY QUAY:).
13. `pan`/`tilt`/`arc`/`pullback` trên SF cỡ cận (đọc dòng MÁY QUAY:) → lỗi.
14. Đếm số cú máy trong một prompt: >1 (trừ dạng hai mốc giây cùng hướng) → lỗi.
15. Câu camera có động từ chuyển động mà thiếu số %/độ hoặc thiếu mốc dừng → lỗi.
16. In bảng phân bổ camera thực tế theo `dur` và theo cỡ cảnh, so với bảng đích ở mục Camera.
