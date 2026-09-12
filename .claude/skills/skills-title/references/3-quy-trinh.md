# 3 — Quy trình: dựng, lọc, cắt, giao

## 0. Ý tưởng lấy từ kho, không tự nghĩ

**Mọi title giao ra phải mọc từ một dòng có thật trong kho.** Cấm nghĩ ra một lõi tình huống không có trong kho, dù nó hay tới đâu.

**Ba kho — 643 title:**

| Kho | Có gì |
|---|---|
| `../kho/KHO-BO-SUNG-2026-09-12.md` | **437 title** user dán trực tiếp — kho lớn nhất, 385 dòng đã sẵn trong dải 90–100 |
| `../../skills-kich-ban/kho-tham-chieu/TITLES.md` | 206 title từ sheet (232 dài + 117 short, sau khử trùng) |
| `../kho/PHAN-LOAI-131.md` | 131 title đã gán mã `D#/T#/V#/L#` — dùng khi cần tra mã sẵn |

**Giữ gì ở dòng gốc** — *lõi tình huống*: cặp quyền lực (kẻ ra đòn ↔ người chịu đòn), loại đòn, và trục lật.

**Đổi gì** — chỉ cần đổi ít: chức danh, nghề, bối cảnh, tuổi, con số, thứ bị giấu, cách diễn đạt. **Không bắt viết mới hoàn toàn.** Đổi một hai chỗ cho title đứng được một mình là đủ.

**Đổi trong hàng rào của kho.** Chức vụ và bối cảnh **chỉ được lấy từ những cái đã có trong kho** — tra [`../kho/TU-DIEN-KHO.md`](../kho/TU-DIEN-KHO.md) (98 chức vụ · 52 bối cảnh). Chế ra một nghề hoặc một nơi không có trong kho là **lỗi**, kể cả khi nó hay hơn. Đổi chức vụ phải giữ đúng phía: kẻ ra đòn đổi sang kẻ ra đòn, người chịu đòn đổi sang người chịu đòn.

**Ba thứ được tự do đổi** (không bị hàng rào chặn): con số quy mô · mốc thời gian và tuổi · chữ nghĩa của vế sau, kể cả lý do đặt trong ngoặc kép.

**Cấm hai đầu:**
- Giao nguyên văn một dòng kho, không đổi gì.
- Nghĩ ra một lõi tình huống không truy được về dòng kho nào.

**Ghi kèm dòng gốc.** Mỗi title giao ra ghi số thứ tự dòng kho ở cuối, ví dụ `(gốc: TITLES #47)`. Không ghi được nghĩa là title đó tự nghĩ — bỏ.

**Một dòng kho chỉ làm gốc cho một title trong cùng mẻ.** Hai phương án cùng gốc là một phương án viết hai lần.

**Vòng mẫu đã duyệt:** [`../golden_project/GOLDEN-1.md`](../golden_project/GOLDEN-1.md) — một dòng kho đi hết năm bước, kèm bảng chỉ rõ đổi gì và giữ gì. Đọc nó khi không chắc "đổi ít" là đổi tới đâu.

---

## 1. Dựng bao nhiêu

| User xin | Dựng ra | Giao |
|---|---|---|
| Một title cho phim đang làm | 6 phương án khác mã `T` | 1, kèm một câu lý do |
| "Cho tôi 10 title" | 14 | 10 |
| "Cho tôi 30 title" | 38, chia thành ba đợt để tự lọc giữa chừng | 30 |

Dựng dư khoảng 40% là để **có cái để bỏ**. Dựng đúng số phải giao là tự ép mình giữ lại cả phương án yếu.

## 2. Dựng thế nào

0. **Chọn dòng kho gốc cho từng phương án** (§0). Mở kho trước khi trải mã — dòng gốc quyết định dạng, không phải ngược lại.
1. **Trải mã `D` trước, rồi mới tới `T`.** Chốt mẻ này gồm những dạng truyện nào (`4-dang-bai.md` §4), vì dạng quyết định cú lật, mà cú lật quyết định vế sau.
2. **Trải mã `T`.** Trước khi viết chữ, liệt kê xem mẻ này dùng những mã vế trước nào. Không mã nào chiếm quá một phần ba mẻ.
3. **Viết vế trước xong mới nghĩ vế sau.** Ngược lại thì vế trước sẽ bị bẻ cong cho khớp cú lật đã nghĩ sẵn, và nó luôn lộ ra là gượng.
4. **Đọc to.** Title là thứ người ta liếc trong một phần tư giây. Câu vấp khi đọc to thì mắt cũng vấp.
5. **Chạy script sau mỗi đợt**, đừng để dồn tới cuối.

## 3. Lọc

Bỏ một phương án khi:

- Vượt hạn ngạch **dạng `D#`**: `D1` quá 40% mẻ, hoặc mẻ chưa đủ bốn dạng (`4-dang-bai.md` §4).
- Trùng **trục lật `L#`** với một phương án mạnh hơn trong cùng mẻ — một mẻ không được có quá hai title cùng `L#`.
- Trùng **nghề của kẻ ra đòn** với phương án khác (hai title cùng mở bằng `Bank Manager` là một title).
- Rơi vào một trong ba **cặp mòn** (`1-cong-thuc.md` §4) mà không có chi tiết lạ nào để bù.
- Vế sau đúng luật nhưng **không làm ta muốn biết tiếp** — thử thật: đọc xong, nếu không thấy một câu hỏi hiện lên trong đầu thì title chưa làm việc.

## 4. Cắt khi quá 100 ký tự

Cắt theo đúng thứ tự này, dừng ngay khi lọt trần:

1. **Mạo từ và tính từ trang trí**: `A CEO` → `CEO`; `a Quiet Black Woman` → `a Black Woman`.
2. **Trạng ngữ nơi chốn** nếu bối cảnh đã tự hiểu: `at a Gas Station`, `in the Park`.
3. **Số đếm không mang sức nặng**: `6 Stranded Bikers` → `Stranded Bikers` (giữ lại nếu con số chính là cú sốc, ví dụ `27 Times`).
4. **Rút danh xưng**: `MIT Professor` → `MIT Prof`; `Police Chief's Son` → `Chief's Son`.
5. **Đổi khuôn vế sau sang khuôn ngắn hơn**: `Not Knowing She Was…` → `Turns Out She's…`.

**Không bao giờ cắt** hai đầu của khoảng cách xã hội, hay con số quy mô ở vế sau. Cắt tới bước 5 mà vẫn quá dài nghĩa là **góc vào sai**, không phải câu dài — quay lại §2 chọn mã `T` khác.

## 5. Ngắn hơn 90 ký tự thì thêm gì

Thêm theo thứ tự này — thêm **chất**, đừng thêm **chữ**:

1. Một chi tiết cụ thể hoá người chịu đòn: tuổi, nghề, cảnh ngộ (`71-Year-Old`, `Single Dad`, `Barefoot`).
2. Một con số quy mô ở vế sau (`$400M`, `300`, `40 Years`).
3. Một mốc thời gian ở vế sau (`By Noon`, `24 Hours Later`, `At Dawn`).
4. Lý do của đòn, đặt trong ngoặc kép (`for "Talking Back"`, `for "Smelling Bad"`).

## 6. Giao bài

- Đánh số, mỗi title một dòng, **kèm số ký tự trong ngoặc** ở cuối dòng.
- Ghi mã `D#` sau **mọi** title, kèm skill sẽ viết nó (`4-dang-bai.md` §3) — đó là thứ user cần để chạy tiếp.
- Ghi thêm `T# × V# × L#` khi user xin từ mười title trở lên — để user thấy mẻ này đa dạng thật hay chỉ đổi chữ.
- Báo phân bố cuối mẻ: mỗi dạng `D` bao nhiêu cái, bao nhiêu mã `T` đã dùng, mã `L` nào lặp.
- **Không giao kèm chú thích "cái này hơi dài, bạn tự cắt nhé".** Cắt là việc của skill.

## 7. Checklist giao bài

- [ ] **Mọi title có dòng kho gốc ghi kèm, không dòng nào bị dùng hai lần trong mẻ** (§0).
- [ ] **Không title nào trùng nguyên văn dòng gốc của nó.**
- [ ] **Mọi chức vụ và bối cảnh có trong `kho/TU-DIEN-KHO.md`** — không nghề lạ, không nơi lạ.
- [ ] Đủ số user xin, không thừa không thiếu.
- [ ] Mọi title qua sạch checklist `2-do-luong.md` §4.
- [ ] Mọi title qua sạch checklist `1-cong-thuc.md` §6 và `4-dang-bai.md` §5.
- [ ] Mẻ có ít nhất **bốn** dạng `D` khác nhau, `D1` không quá 40% (trừ khi user chỉ định dạng).
- [ ] Mẻ dùng ít nhất **bốn** mã `T` khác nhau (khi giao từ mười title trở lên).
- [ ] Không mã `L#` nào lặp quá hai lần trong mẻ.
- [ ] Không hai title nào mở bằng cùng một nghề của kẻ ra đòn.
- [ ] Số ký tự đã ghi kèm từng dòng, lấy từ script chứ không đếm tay.
