# 6 — Cụm không gian & Master SF

> **File này trả lời:** scene này chia làm mấy cụm không gian, và mỗi cụm neo bằng bức ảnh nào.
> **Mở khi:** trước khi chia shot chi tiết, khi sinh Master SF, và mỗi lần một SF con cần biết `refs.bg` trỏ về đâu.
> **Không chứa:** danh sách shot và thời lượng (→ `7-bang-shot.md`) ·
>   nội dung prompt của SF thường (→ `8-prompt-sf.md`) ·
>   cú pháp mã ID và chuỗi `refs` tổng quát (→ `2-du-lieu-sf-board.md`) ·
>   định mức tỉ lệ khung của scene (→ `7-bang-shot.md` §Định mức)

## 1. Phân rã thế trận (Blocking Shifts) — làm trước khi chia shot

Thay vì lao ngay vào chia shot cơ học, bắt buộc đọc kịch bản để tìm các "Điểm Khựng" (Blocking Shifts) làm thay đổi cấu trúc không gian:
- Nhân vật mới bước vào/bỏ đi làm vỡ cấu trúc nhóm.
- Các nhân vật dắt nhau di chuyển sang một khu vực khác (VD: từ Bàn thờ xuống Lối đi).
- Sự thay đổi từ trạng thái tĩnh sang động (VD: đang ngồi thì đứng phắt dậy cãi nhau).

**Mỗi một Cụm Không Gian (Blocking Shift) bắt buộc phải có một Master SF riêng để chốt vị trí.**

> **Ví dụ điển hình (Cảnh Đám Cưới ALTAR)**:
> - *Cụm 1 (Chờ đợi)*: Clara và Linh mục tại bàn thờ. → Cần Master 1.
> - *Cụm 2 (Đối đầu)*: Ryan dắt Vanessa lên bàn thờ cãi nhau. Vị trí xáo trộn 180 độ. → Cần Master 2.
> - *Cụm 3 (Đụng độ)*: Ryan và Vanessa quay lưng bỏ đi, đụng độ Adrian ngồi xe lăn ở lối đi giữa. Thế trận dịch chuyển 10 mét. → Cần Master 3.

### 1.1 Thế trận khung dọc — so le theo chiều sâu, cấm dàn hàng ngang

Khung 9:16 không có bề ngang để chứa một hàng người (`7-bang-shot.md` §3.0). Vì thế **thế trận phải được dàn ngay từ đây**, không phải sửa chữa ở bước cắt cận.

- **Mỗi cụm phải có một trục sâu rõ ràng**: chọn một điểm đặt máy sao cho các nhân vật của cụm nằm **so le theo chiều sâu** — mỗi người cách người kế tiếp ít nhất nửa bước chân về phía xa máy. Không cụm nào được để 3–4 nhân vật đứng cùng một khoảng cách tới máy.
- **Cách dàn khi đời thật họ đứng ngang hàng** (xếp hàng ở quầy, ngồi cùng dãy ghế, đứng thành vòng): không đổi vị trí nhân vật, mà **đổi chỗ đặt máy** — kéo máy về một đầu hàng để hàng ngang đó biến thành hàng sâu chạy vào trong khung. Đây là cách hợp lệ duy nhất; viết prompt đẩy người ngang hàng ra "lớp sau" là lỗi (`8-prompt-sf.md` §2.2).
- **Chốt thứ tự sâu bằng chữ, ngay khi phân rã cụm**: ghi ra "gần máy nhất → xa nhất" cho từng cụm trước khi sinh Master SF. Thứ tự này là nguồn sự thật cho mọi SF con của cụm; SF con nào xếp lớp khác thứ tự đó là vỡ raccord vị trí.
- **Cụm quá đông thì tách cụm, đừng lùi máy**: nếu một cụm có hơn 4 nhân vật chính, khung dọc không gánh nổi. Tách thành hai cụm với hai Master SF — nhưng cân nhắc trần góc rộng ở `7-bang-shot.md` §1.2 trước khi tách.

⚠️ **Cụm không gian không trùng với scene**: một cụm có thể vắt qua nhiều scene, và một scene có thể mở đầu bằng khung thuộc cụm của scene trước. Xác định cụm bằng câu hỏi *"máy đứng ở đâu, chĩa về đâu"* — tuyệt đối không xác định bằng *"shot này nằm ở scene nào"*.

## 2. Master SF

### 2.1 Vai trò
- Master SF là shot góc rộng đầu tiên của cụm (khi nhân vật đã vào vị trí). Nhiệm vụ: gắn kết Nhân Vật vào Bối Cảnh đã tạo ở Thẻ Địa Điểm.
- Nó thiết lập toàn bộ không gian, ánh sáng, vị trí nhân vật chính và chốt mật độ quần chúng nền ban đầu của cụm đó.
- Nó làm mốc tham chiếu (`refs.bg`) cho toàn bộ các SF con trong cụm. Các shot cận (CU, OTS) của cụm nào bắt buộc trỏ `refs.bg` về đúng Master SF của cụm đó.
- `refs.bg` của Master SF trỏ về ID của Thẻ Địa Điểm (VD: `REF_S1_DAY`).
- Quần chúng nền của Master SF phải tuân Nguyên lý Mật độ Sinh tồn (`9-quan-chung-nen.md`) — không gian công cộng không được viết trống người chỉ vì lý do cảm xúc/đạo diễn.

### 2.2 Cỡ cảnh cứng (Shot Size)
Ảnh SF dùng làm Master bắt buộc phải là góc **Vertical Wide / Cinematic Vertical Wide** (Góc Rộng / Toàn cảnh, khung dọc 9:16) để bao quát 70–100% không gian bối cảnh gốc.

**Khung dọc bao quát theo chiều SÂU, không theo bề ngang.** Một Master SF dọc không thể ôm trọn bề ngang căn phòng như phim ngang; nhiệm vụ của nó là cho thấy **trục sâu** của cụm — từ lớp tiền cảnh sát máy chạy vào tới bức tường/mốc cuối ở dải trên khung — kèm đủ trần/mái ở đỉnh và sàn ở đáy để SF con có chỗ neo. Trần 4 nhân vật rõ mặt (`7-bang-shot.md` §3.0 Hệ quả 2).

**Tuyệt đối cấm** dùng các góc hẹp như Medium Shot, Medium Two-Shot, OTS, hay Close-up làm Master SF — không đủ rộng để thiết lập không gian, khiến các SF con phía sau tham chiếu vào bị mất bối cảnh gốc.

### 2.3 tuyệt đối không dùng SF Nhịp (SF-B) làm Master
Master SF phải là ảnh đầu tiên chuẩn vị trí và tư thế của nhân vật trong cụm đó. Ví dụ: nếu có 2 nhân vật đang đối thoại, Master SF phải là khung hình rộng đầu tiên lúc 2 người đã ổn định vị trí ngồi/đứng nói chuyện, chứ không phải nhịp bước vào hay nhịp chờ.

### 2.4 Thứ tự
Master SF phải nằm đúng vị trí thời gian xuất hiện của nó trong mảng `sfs`. Tuyệt đối không gom toàn bộ Master SF lên đầu scene. (Luật thứ tự đầy đủ: `2-du-lieu-sf-board.md` §4.)

---

## 3. Khung gối đầu hai cụm

Khung hình đặt máy tại cụm A nhưng nhìn thấy cả cụm B ở lớp sau (VD: từ lều y tế nhìn thấy sân khấu ở xa), trong không gian thông nhau.

### 3.1 Phát hiện sớm — ngay ở bước phân rã thế trận
**Cảnh báo dây chuyền**: khung gối đầu nhìn sang cụm khác có thể kéo thêm Main Cast của cụm đó lọt vào nón quan sát, làm tăng số lượng nhân vật trong khung của scene. Bắt buộc chốt danh sách các khung gối đầu ngay ở giai đoạn phân rã thế trận để:
1. Rà soát tỷ lệ khung hình của scene (định mức: `7-bang-shot.md` §Định mức).
2. Kịp thời bổ sung ID của Scene hiện tại vào dòng `Dùng: S1 · S2...` trong trường `desc` của thẻ `REF_<TÊN>_FULL` của nhân vật lọt ở hậu cảnh (tránh thiếu đính thẻ).
3. Chừa sẵn slot REF bối cảnh phụ khi phân bổ thẻ tham chiếu nhân vật — vì mỗi khung này cần 2 tham chiếu bối cảnh.

### 3.2 Nối dữ liệu
- `refs.bg` → Master SF của cụm chứa chủ thể (cụm A).
- `refs.chars` → đính thêm Master SF hoặc Thẻ Địa Điểm của cụm B làm ảnh neo bối cảnh phụ.
- `pose.zone` khai bằng dấu mũi tên chỉ hướng nhìn để máy đọc được: `"zone": "góc lều y tế → sân khấu chính"`.

### 3.3 Chọn ảnh nào cho neo thứ hai
Hỏi: *"Cụm ở lớp sau, tại đúng thời điểm này, có Main Cast đang diễn không?"*
- **Trống người (không có main cast)** → neo bằng Thẻ địa điểm (`REF_BG_*`).
- **Có Main Cast đang diễn** (nhân vật vẫn đang phát biểu trên bục / ngồi ở bàn tại khoảnh khắc đó) → bắt buộc neo bằng Master SF của cụm đó (bức ảnh đã có sẵn nhân vật ở đúng vị trí, đúng tư thế). Dùng Thẻ địa điểm rỗng ở ca này chính là ra lệnh cho AI xóa sạch người khỏi hậu cảnh.

### 3.4 Câu lệnh trỏ ảnh trong prompt SF
**Tuyệt đối cấm tả kiến trúc cụm xa bằng văn xuôi cảm tính.** Trong prompt SF chỉ viết một câu trỏ ảnh:

> *"Lớp sau ở xa là [tên cụm] — trên đó [Tên nhân vật] vẫn đang [hành động], lấy đúng 100% không gian, bục VÀ dáng người phát biểu theo ảnh tham chiếu Master [Mã SF Master], KHÔNG tự ý dựng mới hay xóa người."*

Kèm câu chặn: *"Nhân vật ở lớp sau rất xa, nhỏ, ngoài nét/out nét"* — để AI không kéo họ lên làm chủ thể tiền cảnh.

**Main cast ở lớp sau thì neo bằng ảnh, không tả bằng chữ:** tuyệt đối không tả họ bằng chữ văn xuôi thuần túy. Bắt buộc đính Master SF của cụm đó + `REF_<TÊN>_PORTRAIT` + `FULL` vào `refs.chars`, đồng thời khai tên họ vào dòng `goc` và `pose.who` như mọi nhân vật lọt vào khung. Tả bằng chữ thì AI sẽ dựng ra một người lạ mặc đồ na ná, đứng sai chỗ.

*(Chữ trong prompt chỉ dành cho quần chúng vô danh — `9-quan-chung-nen.md` §4.)*

### 3.5 Linh hoạt về trần thẻ ref
- Thẻ Master SF cụm xa đính ở `refs.chars` đóng vai trò ảnh neo bối cảnh phụ, không bị tính là thẻ nhân vật (miễn trừ khỏi trần 4 nhân vật / 8 thẻ).
- Với Main Cast ở cụm xa (đứng rất xa, nhỏ, out nét như người phát biểu trên bục sân khấu): bản thân ảnh Master SF cụm xa đã chứa sẵn khuôn mặt, vóc dáng và trang phục chuẩn của họ. Nếu mảng `refs` đã có đủ 4 nhân vật chính ở tiền cảnh/trung cảnh, không bắt buộc đính thêm thẻ Portrait + Full riêng của nhân vật cụm xa — ảnh Master SF neo thứ hai đã đủ làm nguồn sự thật.
- Vẫn khai tên họ vào `goc`, `pose.who` và dòng `Dùng:` của thẻ `_FULL`.

## 4. Kiểm tra cuối bước
- [ ] Mỗi cụm không gian có đúng một Master SF, cỡ Vertical Wide / Cinematic Vertical Wide.
- [ ] Mỗi cụm đã ghi ra thứ tự sâu "gần máy nhất → xa nhất"; không cụm nào để 3–4 nhân vật cùng một khoảng cách tới máy (§1.1).
- [ ] Không cụm nào có hơn 4 nhân vật chính.
- [ ] Không Master nào là SF Nhịp (`-B<n>`).
- [ ] Mọi Master SF trỏ `refs.bg` về Thẻ Địa Điểm; mọi SF con trỏ về Master của cụm mình.
- [ ] Master SF nằm đúng vị trí thời gian trong mảng `sfs`, không bị gom lên đầu.
- [ ] Đã chốt danh sách khung gối đầu và bổ sung dòng `Dùng:` cho nhân vật lọt hậu cảnh.
