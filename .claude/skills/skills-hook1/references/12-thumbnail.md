# 12 — Thumbnail (ảnh bìa Hook)

> **File này trả lời:** 3 ảnh thumbnail của một Hook chọn khoảnh khắc nào, khoá nhân vật ra sao, được phá luật SF nào, viết prompt thế nào, tra template ở đâu, tinh chỉnh theo lệnh user ra sao.
> **Mở khi:** tạo hoặc sửa `SF-THUMB-01/02/03`.
> **Không chứa:** khuôn JSON, mã ID, vị trí trong mảng `sfs`, chuỗi neo `refs`, trần ký tự, dòng kết 16:9 (→ `2-du-lieu-sf-board.md` §2.6 · §3 · §5 · §8) ·
>   mặt & trang phục của nhân vật (→ `3-ref-nhan-vat.md`) · luật chung của SF thường (→ `8-prompt-sf.md`) ·
>   an toàn trẻ em (→ `KHI-CO-TRE-EM.md`)

> Thumbnail phục vụ việc **bán click**, không phải nuôi video. Nó không có clip nào neo vào, nên được miễn một nhóm luật khung đầu (§4) — nhưng mặt và áo phải khớp phim, vì người bấm vào mà thấy người khác thì mất lòng tin ngay giây đầu.

## 1. Khi nào làm

Làm **sau** khi bảng shot và SF đã chốt (Bước 9). Cần đủ ba thứ trước đó:
- thẻ `REF_*_FULL` của mọi nhân vật sẽ lọt vào thumbnail;
- thẻ địa điểm `REF_BG_*` của nơi xảy ra khoảnh khắc được chọn;
- bảng shot của Hook — để biết khoảnh khắc nào căng nhất (THUMB-03 lấy từ đây).

## 2. Chiến lược 3 thumbnail

Mỗi Hook xuất ra **đúng 3** thumbnail, ba góc tiếp thị khác nhau:

| Mã SF | Loại | Nguồn | Tiêu chí nội dung |
|---|---|---|---|
| `SF-THUMB-01` | Template A | Mẫu thứ nhất chọn được từ kho (§6) | **Dùng lại nguyên văn prompt mẫu**, chỉ đổi nhân vật + bối cảnh (§6.3). |
| `SF-THUMB-02` | Template B | Mẫu thứ hai chọn được từ kho (§6) | Như trên, với một mẫu khác. |
| `SF-THUMB-03` | Tự sáng tạo | Khoảnh khắc căng nhất **trong đoạn Hook** | Bắt buộc lấy **khoảnh khắc tĩnh ngay trước bùng nổ** hoặc **giây phút cán cân quyền lực vừa lật**. Không lấy khoảnh khắc sau khi mọi thứ đã ngã ngũ. Viết theo khung §5. |

## 3. Cast & khoá nhân dạng

1. **`refs.chars` = thẻ `REF_*_FULL` đúng bộ đồ** nhân vật đang mặc ở khoảnh khắc được chọn. Hook không có portrait (`3-ref-nhan-vat.md` §2), nên FULL là nguồn nhân dạng duy nhất. Nhân vật có nhiều FULL → chọn đúng bộ của cảnh đó, không lấy bộ đẹp nhất.
2. **Prompt lấy đúng tuổi, sắc tộc, tóc và màu áo** từ thẻ FULL. Tuyệt đối không đổi màu áo, kiểu tóc, tuổi cho "ăn ảnh hơn". Mẫu template tả nhân vật khác → xoá phần tả người của mẫu, thay bằng người của phim.
3. **`refs.bg` trỏ thẻ địa điểm `REF_BG_*`**, không trỏ Master SF — bố cục thumbnail theo template, không kế thừa bố cục của cụm.
4. Trần số nhân vật có ref vẫn áp như SF thường: `2-du-lieu-sf-board.md` §5.1.

## 4. Luật SF nào được miễn, luật nào vẫn giữ

**Được miễn** (các luật này sinh ra để nuôi video, thumbnail không có video):

| Luật SF thường | Ở thumbnail |
|---|---|
| Nhân vật nhìn nhau / nhìn vật (`8-prompt-sf.md` §5 Hướng nhìn) | Nhân vật chính **được nhìn thẳng ống kính**, ánh mắt sắc, thách thức. |
| Biểu cảm kìm nén (`8-prompt-sf.md` §5) | **Được đẩy biểu cảm lên cực hạn**: kinh ngạc, kiêu hãnh, khinh bỉ, sững sờ. |
| Trạng thái chờ (`8-prompt-sf.md` §5) | Không áp — thumbnail là một khoảnh khắc đứng riêng, không có clip nào diễn tiếp. |
| Ánh sáng khớp biến thể giờ của thẻ địa điểm (`5-the-dia-diem.md` §4.3) | **Được tương phản mạnh**: rim light, vệt nắng gắt, đèn hắt kịch tính — miễn giữ đúng ngày/đêm của cảnh. THUMB-01/02 giữ ánh sáng của mẫu (§6.3). |
| Kế thừa bố cục Master SF (`8-prompt-sf.md` §3) | Không áp — bố cục theo template (§3.3). |
| Cách viết SF thường (`8-prompt-sf.md` — viết ngắn, cắt thứ ảnh ref đã có) | THUMB-01/02 không áp: prompt là nguyên văn mẫu, không rút gọn, không viết lại câu. |

**Vẫn giữ nguyên:**
- Cấm tả "mắt đỏ" và câu chặn đi kèm — `8-prompt-sf.md` §6.
- Chữ trong khung: bề mặt có thể mang chữ phải khoá bằng nhãn hư cấu — `8-prompt-sf.md` §1.2(b).
- Quần chúng nền không nhìn camera, đang dõi theo chủ thể — `9-quan-chung-nen.md`.
- Toàn bộ `KHI-CO-TRE-EM.md` nếu khung có trẻ em (kể cả khi đẩy biểu cảm phản diện).

## 5. Khung prompt & câu chặn

Khung dưới đây dùng cho **THUMB-03**. THUMB-01/02 lấy chính prompt mẫu làm khung (§6.3), chỉ bổ sung hai dòng cuối nếu mẫu chưa có.

```text
[Photorealistic, Highly detailed, Professional Photography, 16:9] [Thiết lập ánh sáng & vibe màu]
Bối cảnh: [không gian từ REF_BG_*].
Bố cục: [góc máy + tỉ lệ khung chia cho từng người, VD 4/10 – 6/10].
[NHÂN VẬT CHÍNH]: [tuổi, sắc tộc, tóc, màu áo đúng REF_FULL + hành động + biểu cảm khoảnh khắc].
[PHẢN DIỆN]: [đúng REF_FULL + hành động áp đảo / khinh khỉnh].
Nhân vật nền: [2–3 người mờ, đang nhìn về chủ thể].
KHÔNG chữ, KHÔNG watermark, KHÔNG logo, KHÔNG vòng tròn đỏ, KHÔNG mũi tên.
KHUNG NGANG 16:9
```

- **Câu chặn rác đồ hoạ là bắt buộc**, đặt ngay trước dòng `KHUNG NGANG 16:9`. Đây là **ngoại lệ hợp lệ** của luật cấm negative prompt rác (`8-prompt-sf.md` §6): AI ảnh học từ thumbnail YouTube thật, nên khi nhận prompt kiểu "ảnh bìa" nó tự chèn chữ to, mũi tên, vòng tròn đỏ — lỗi có thật, không phải câu cấm vô nghĩa. Chữ, nếu cần, user tự thêm ở khâu thiết kế.
- Dòng cuối cùng luôn là `KHUNG NGANG 16:9` (`2-du-lieu-sf-board.md` §8).

## 6. Tìm mẫu trong kho & dùng lại

Kho: `sfboard/thumbnail-templates.json` — 79 prompt text, 23 nhóm bối cảnh. Mỗi mẫu có tag gồm bối cảnh (`diner`, `máy bay`), hành động (`xé séc`, `đổ nước`, `tát`, `giơ tiền`) và vai (`veteran`, `CEO`, `người thứ 3`). Chạy từ gốc repo `SF Board/`.

Script chấm điểm mỗi từ khoá: trùng tag **+3** · nằm trong tên nhóm **+2** · nằm trong thân prompt **+1**; trả về 2 mẫu điểm cao nhất.

### 6.1 Lượt 1 — tra theo bối cảnh + tình huống
```bash
python3 sfboard/tim-thumbnail.py diner tip
python3 sfboard/tim-thumbnail.py "máy bay" "xé vé"
```
**Phù hợp** khi mẫu khớp đủ hai thứ với khoảnh khắc của phim: **cùng loại bối cảnh** và **cùng thế trận** (bao nhiêu người chính, ai áp đảo ai, hành động chính là gì). Chỉ khớp bối cảnh mà thế trận khác (VD mẫu diner cho tiền tip, phim là diner đổ nước lên người) → chưa phù hợp, sang lượt 2.

### 6.2 Lượt 2 — tra theo tư thế / biểu cảm
Không có mẫu phù hợp ở lượt 1 → **bỏ qua bối cảnh**, tra bằng tư thế, hành động hoặc biểu cảm của nhân vật ở khoảnh khắc được chọn:
```bash
python3 sfboard/tim-thumbnail.py "đổ nước" "sững sờ"
python3 sfboard/tim-thumbnail.py "chỉ tay" "khinh bỉ"
```
- **Cụm nhiều chữ phải đặt trong ngoặc kép.** Gõ rời `chỉ tay` thì script tách thành `chỉ` và `tay`, mà chữ `tay` có ở gần như mọi mẫu → kết quả vô nghĩa.
- Mẫu tìm được ở lượt này có bối cảnh khác phim là **bình thường** — bối cảnh sẽ được thay ở §6.3.
- Đọc thân prompt của mẫu để chắc tư thế/biểu cảm thật sự khớp, không chỉ trùng chữ.

Cả hai lượt vẫn không ra mẫu nào khớp tư thế → báo user, không tự bịa "template" thay thế.

Gọi đích danh một mẫu: `python3 sfboard/tim-thumbnail.py "Máy bay" 3` (tên nhóm + số hàng).

### 6.3 Dùng lại mẫu đã chọn — chỉ đổi nhân vật và bối cảnh
Đã chọn mẫu nào thì **dùng lại toàn bộ prompt đó, nguyên văn**. Chỉ được thay đúng hai phần:
1. **Nhân vật chính và phản diện** — mọi câu tả người của hai vai này (tuổi, sắc tộc, tóc, dáng, trang phục) → thay bằng người của phim theo thẻ `REF_*_FULL` (§3). Giữ nguyên tư thế, hành động, biểu cảm, hướng nhìn, tỉ lệ chiếm khung của từng vai.
   - **Nhân viên bảo vệ của mẫu giữ nguyên văn** — ngoại hình, đồng phục, hành động khống chế và biểu cảm đều để nguyên, **không cần kịch bản có nhân viên bảo vệ**, không thay bằng nhân vật khác, không xoá vì "phim chưa tới đoạn đó". Bàn tay bảo vệ ghì nhân vật chính là thế trận bán click, không phải chi tiết tường thuật. Chỉ đổi đại từ cho khớp giới tính nhân vật chính.
   - **Các vai phụ còn lại (cơ trưởng, khách VIP, tiếp viên phụ, người thứ ba…) thì linh hoạt theo kịch bản**: phim có vai tương đương thì thay bằng người của phim, giữ nguyên vị trí đứng, tư thế, biểu cảm và tỉ lệ chiếm khung của mẫu; phim không có ai vào vai đó thì để nguyên văn vai của mẫu, không xoá khỏi khung.
2. **Bối cảnh** — câu tả không gian, đồ vật nền, quần chúng nền → thay bằng nơi chốn của phim theo thẻ `REF_BG_*`. Nguồn sáng gắn liền bối cảnh cũ (rèm cửa sổ diner, đèn quầy bar) đổi theo bối cảnh mới; **kiểu ánh sáng** (hướng, độ gắt, tông màu) giữ nguyên, trừ khi phải đổi ngày/đêm cho khớp cảnh.

**Giữ nguyên mọi thứ còn lại**: dòng mở đầu, khối ánh sáng, góc máy, bố cục, tỉ lệ chia khung, đạo cụ tham gia hành động (đổi sang đạo cụ tương đương của phim nếu khác), câu chặn sẵn có. Không rút gọn, không viết lại câu cho "hay hơn", không thêm ý mới.

Chỉ được **bổ sung** ở cuối, nếu mẫu chưa có: câu chặn rác đồ hoạ và dòng `KHUNG NGANG 16:9` (§5).

Không sửa `thumbnail-templates.json` để "cho khớp" — kho mẫu là của user.

## 7. Trường `notes` & tinh chỉnh theo lệnh user

`notes` của mỗi SF-THUMB ghi nguồn gốc + menu tinh chỉnh để user chọn nhanh:

```text
Nguồn: Template <Nhóm> hàng <n> — tra theo bối cảnh | tra theo tư thế "<từ khoá đã dùng>"
       (THUMB-03 ghi: Tự sáng tạo — <mã shot của khoảnh khắc>)
Menu tinh chỉnh:
1. Bối cảnh điện ảnh & đắt giá hơn (ánh sáng, chi tiết bối cảnh)
2. Đẩy căng tương tác tay & đạo cụ (tiền, còng tay, séc, vé…)
3. Biểu cảm khoảnh khắc ghen tị / bất ngờ / lạnh lùng tột độ
4. Tăng tương phản màu & ánh sáng (đèn strobe, nắng sớm hắt)
5. Đẩy cao áp lực đe doạ của phản diện
```

User gõ dạng `T1: 2 + 4` hoặc `T3: 5`:
- **Vá luỹ tiến trên prompt hiện tại** của SF-THUMB đó. Tuyệt đối không reset về template thô.
- Mục 1 chỉ dùng không gian có thật trong kịch bản / thẻ `REF_BG_*`, không bịa bối cảnh mới mâu thuẫn với phim.
- Mục 5: khung có trẻ em → chạy lại checklist `KHI-CO-TRE-EM.md` §3 sau khi vá.

## 8. Kiểm tra

**Đếm được:**
- [ ] Đúng **3** SF: `SF-THUMB-01`, `SF-THUMB-02`, `SF-THUMB-03`, nằm cuối `sfs[]` của scene `REF` (`2-du-lieu-sf-board.md` §2.6).
- [ ] THUMB-01 và THUMB-02 ghi nguồn template (nhóm + hàng + lượt tra) trong `notes`; THUMB-03 ghi mã shot của khoảnh khắc được chọn.
- [ ] THUMB-01/02: đặt cạnh mẫu gốc, mọi câu **không** tả nhân vật chính / phản diện / bối cảnh vẫn giữ nguyên văn (§6.3).
- [ ] THUMB-01/02: nhân viên bảo vệ của mẫu còn nguyên, đúng hành động khống chế và biểu cảm của mẫu — kể cả khi kịch bản không có bảo vệ (§6.3).
- [ ] THUMB-01/02: vai phụ khác đã đối chiếu kịch bản — có vai tương đương thì đã thay người, không có thì để nguyên mẫu; không vai nào bị xoá khỏi khung (§6.3).
- [ ] Mọi nhân vật lọt khung có đúng thẻ `REF_*_FULL` của bộ đồ cảnh đó trong `refs.chars`; `refs.bg` trỏ một `REF_BG_*`.
- [ ] Prompt kết thúc bằng câu chặn rác đồ hoạ, rồi dòng cuối `KHUNG NGANG 16:9`.
- [ ] Prompt nằm trong trần ký tự của SF-THUMB (`2-du-lieu-sf-board.md` §8).
- [ ] Không có "mắt đỏ" / "red eyes" trong prompt.

**Phải đọc mới thấy:**
- [ ] Mẫu chọn ở lượt 1 thật sự cùng thế trận với khoảnh khắc phim; mẫu ở lượt 2 thật sự cùng tư thế/biểu cảm (§6.1 · §6.2).
- [ ] Tuổi, sắc tộc, tóc, màu áo trong prompt khớp thẻ FULL — không còn sót chữ tả người hay bối cảnh cũ của template.
- [ ] THUMB-03 là khoảnh khắc **trước** bùng nổ hoặc lúc quyền lực vừa lật, có thật trong đoạn Hook.
- [ ] Ba thumbnail khác nhau rõ về bố cục hoặc khoảnh khắc — không phải ba biến thể của cùng một khung.
- [ ] Bối cảnh đúng ngày/đêm của cảnh; chữ trên bề mặt (biển hiệu, bao bì) là nhãn hư cấu.
- [ ] Khung có trẻ em → đã qua `KHI-CO-TRE-EM.md` §3.
