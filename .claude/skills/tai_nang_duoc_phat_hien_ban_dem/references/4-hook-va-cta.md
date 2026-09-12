# Title, mở màn, câu trớ trêu, lời rủ tương tác

> Viết lại ngày 2026-09-11 theo Golden mới. Phần mở màn của Golden nằm ở **L3–13** — đọc trọn một lần trước khi viết để nghe nhịp, rồi đóng lại. File này mô tả **chức năng** của từng phần; Golden chỉ là một cách lấp các chức năng đó.

---

## 1. Title

**Giữ nguyên văn title user đưa.** Chỉ đụng vào khi có lỗi gõ rõ ràng hoặc title bằng tiếng Việt; cả hai phải báo ở bước 8.

### 1.1. Đọc title ra dữ kiện

Title dòng này thường cho: **người bắt gặp** (tỉ phú, chủ, giám đốc, bác sĩ trưởng) · **thời điểm/nơi bắt gặp** · **người bị coi thường** (cái nhãn, đôi khi kèm một lớp phủ như chủng tộc, tuổi, giới) · **việc cô đang làm** · **giá trị của thứ đang hỏng** · **con số chuyên gia đã thua** · **phán quyết của họ** ("called dead", "said it was impossible").

Ô nào title không cho thì tự quyết và ghi vào báo cáo. Title không cho kẻ gác cổng — hắn luôn phải tự dựng.

### 1.2. Title nói ra kết quả — mở màn giữ lại cách làm

Người xem biết từ title rằng cô sẽ làm được. Thứ họ chưa biết là **bằng cách nào**, và **cô đã phải đi qua gì để tới đó**. Mở màn cho họ thấy cô **đang làm**, chưa cho thấy **lời giải**.

Vì vậy, trong mở màn, cô **không giải thích** lời giải — chỉ một câu ngắn chỉ vào hướng của nó. Lời giải đầy đủ là phần thưởng của màn trình diễn.

### 1.3. Khi phải tự viết title

Giữ bốn thứ: người bắt gặp, cái nhãn của nhân vật chính, một con số giá trị hoặc con số chuyên gia, và phán quyết sai của chuyên gia. Hai vế ngăn bằng gạch ngang dài. Nếu kho có skill `skills-title`, theo ràng buộc của skill đó: **90–100 ký tự, đúng một dấu `—`, hai mệnh đề**, đo bằng `skills-title/scripts/kiem-title.py` chứ không đếm bằng mắt.

**Ý tưởng lấy từ kho, không tự nghĩ.** Mở `skills-kich-ban/kho-tham-chieu/TITLES.md` (hoặc `skills-title/kho/PHAN-LOAI-131.md`) và chọn một dòng làm gốc. Giữ **lõi tình huống** của dòng đó — cặp quyền lực, loại đòn, trục lật; **đổi ít là đủ** (chức danh, nghề, bối cảnh, tuổi, con số, cách diễn đạt), không bắt viết mới hoàn toàn. Cấm hai đầu: giao nguyên văn dòng kho · nghĩ ra lõi không truy được về dòng kho nào. **Chức vụ và bối cảnh chỉ lấy từ kho** — tra `skills-title/kho/TU-DIEN-KHO.md` (98 chức vụ · 52 bối cảnh); nghề lạ hay nơi lạ là lỗi, kể cả khi nghe hay hơn. Con số, mốc thời gian và tuổi thì tự do. Ghi kèm dòng gốc ở báo cáo bước 8. Luật đầy đủ: `skills-title/references/3-quy-trinh.md` §0.

---

## 2. Mở màn

### 2.1. Mở màn là gì

**Một cảnh có thật ở khoảng ba phần tư bài — lúc người có quyền cao hơn bắt gặp cô — bị lôi lên đầu và nén lại.** Thân bài sẽ đi tới nó rồi diễn lại nó đầy đủ. Một địa điểm, một khoảnh khắc, **120–160 từ** (Golden: 140). Không phải trailer ghép nhiều thời điểm. Đếm bằng `scripts/kiem-do-dai.py`, không đếm bằng mắt — mở màn đọc trôi rất dễ dài gấp đôi mà không thấy.

**Vì sao ngắn**: mở màn chỉ cần một câu chỉ vào khe hở. Manh mối của lời giải (tấm bìa lật từng trang, đèn bật từng hàng, chi tiết thân thể thứ hai) thuộc về cảnh bắt gặp ở thân bài — nhét lên đây là tiêu trước phần thưởng và làm người xem chờ quá lâu mới tới lời rủ.

Mở màn phải **khớp** với cảnh ở thân bài — cùng người, cùng đồ vật, cùng việc đang làm, cùng giờ. Golden lệch nhẹ ở đây (mở màn cho Avery còn đang sửa; thân bài cho máy đã chạy và Avery ngồi chờ). **Không làm theo chỗ lệch đó**: người xem nhớ mở màn, và khi tới nơi mà cảnh khác đi, lời hứa "đây là cảnh có thật" vỡ.

### 2.2. Sáu chức năng mở màn phải làm

Thứ tự và số dòng là tự do. Sáu chức năng thì không.

**1. Mở giữa việc, bằng thoại.** Câu đầu là thoại ngắn, và nó đặt người nghe **ngay trong tay nghề** của nhân vật chính — cô đang làm, đang cần một dụng cụ, đang đếm, đang nghe. Cô **không nhìn lên**. *Vì sao*: người nghe gặp cô qua tài năng trước khi gặp cô qua cái nhãn; và việc cô không nhìn lên cho biết cô đang chìm trong việc — và không biết ai vừa tới.

**2. Người có quyền bước vào, không xưng danh.** Người kể dựng họ bằng vài mảnh câu thân thể và quần áo. Họ hỏi cô là ai, làm gì ở đây. *Vì sao*: title đã nói họ là ai; cô thì không biết. Người xem giữ bí mật đó cùng người kể — đó là trớ trêu của mở màn.

**3. Cô tự gọi cái nhãn của mình.** Một câu lễ phép, khiêm tốn, gọi đúng thân phận thấp (*chỉ là…*). *Vì sao*: chính miệng cô hạ mình xuống thì khoảng cách với việc cô đang làm hiện ra rõ nhất.

**4. Thách thức bằng con số của title, và một câu đáp chỉ vào khe hở.** Người có quyền nói ra con số chuyên gia đã thua và phán quyết của họ, rồi hỏi vì sao cô nghĩ mình làm được. Cô đáp **một câu ngắn**, không khoe, không giải thích, chỉ vào **đúng chỗ họ đã nhìn sai**. *Vì sao*: câu đáp đó là lời hứa của cả bài — người xem sẽ chờ tới lúc được thấy nó đúng.

**5. Bằng chứng tài năng nằm trên thân thể và đồ vật, qua mắt người có quyền.** Họ nhìn: tay cô, vật mang tài năng, cách dụng cụ được bày. Nếu title có lớp phủ, người kể gọi tên nó **một lần, ở đây, như một dữ kiện**. *Vì sao*: người bắt gặp đánh giá bằng mắt, không bằng thẻ — đó là điều kẻ gác cổng đã không làm.

**6. Lời thách và câu trớ trêu.** Người có quyền bảo cô cho họ xem. Rồi người kể bước ra một nhịp: **cô không biết người này là ai**, hoặc không biết điều sắp tới. *Vì sao*: mở màn dừng ở một cánh cửa mở — và câu trớ trêu nhận lấy lời hứa.

### 2.3. Người kể trong mở màn

- Câu ngắn, mảnh câu, danh từ và động từ đi trước.
- Chỉ ghi lại — không bình luận, không tính từ đánh giá, không thương hại.
- Bối cảnh lộ ra **qua đồ vật, thân thể và giờ**, không qua một câu giới thiệu địa điểm.
- **Ai ở đâu phải rõ ngay** (`6-van-phong.md` mục 5b). Mở màn thường chỉ có hai người.
- Không ai có mặt mà không làm gì. Không nhét trẻ em hay người đứng xem để gợi thương.

### 2.4. Bốn phép thử

- **Bịt tai**: đọc to, không nhìn chữ. Người nghe phải biết cô đang làm gì bằng tay, ai vừa tới, con số chuyên gia đã thua, và cô có run không.
- **Sơ đồ**: vẽ ra ai đứng/ngồi ở đâu, cạnh vật gì.
- **Dán**: câu đáp của cô dán sang một truyện khác nghề mà vẫn đứng → nó chưa chỉ vào khe hở thật. Viết lại quanh lời giải thật.
- **Khớp**: đặt mở màn cạnh dàn ý cảnh bắt gặp ở thân bài. Cùng người, cùng đồ vật, cùng việc đang làm, cùng giờ.

### 2.5. Cường độ

Mở màn của thể loại này **không phải cảnh sỉ nhục** — sỉ nhục nằm ở chặng 2. Mở màn là **sự nghi ngờ của một người có quyền** và **sự bình tĩnh của cô**. Căng thẳng đến từ khoảng cách giữa cái nhãn và việc đang làm. Xem `9-chu-de-nhay-cam.md` về lớp phủ.

---

## 3. Sau mở màn: câu trớ trêu, lời rủ, câu đưa về đầu

Ngay sau mở màn là một khối rất ngắn — Golden dùng hai dòng (L12–13). Đây là chỗ duy nhất ở đầu bài người kể nói thẳng với người xem.

### 3.1. Câu trớ trêu — lời hứa

**Việc của nó**: đóng mở màn bằng khoảng cách giữa điều cô biết và điều người xem biết, rồi hứa rằng khoảng cách đó sẽ đổi đời cô.

Tính chất Golden dùng, và vì sao chúng chạy:
- **Vẫn thì quá khứ, vẫn ngôi ba** — người kể chưa quay ra nói với người xem, chỉ nói điều nhân vật không biết.
- **Hai nhịp**: cái cô không biết về người trước mặt → cái sắp xảy ra với cô.
- **Không gọi tên tài năng, không nói kết quả.** Title đã nói.

Một hai câu, ngắn. Viết mới cho từng bài; **không dùng lại cụm "life was about to change forever"** hay biến thể của nó — đó là câu sáo, và là chữ ký Golden.

### 3.2. Câu hỏi, lời rủ, câu đưa về đầu

**Việc của nó**: gọi người xem vào đúng loại khoảnh khắc họ sẽ được thấy — rồi xin tương tác, rồi đưa họ quay lại từ đầu.

- **Câu hỏi hướng vào người xem như người sắp chứng kiến** (Golden: *Have you ever watched…*). Nó gọi tên **loại khoảnh khắc** — một người chứng minh những kẻ nghi ngờ sai — và **công cụ của tài năng** (đôi tay, cái lưỡi, đôi tai, cây bút), bằng lời đời thường. Rồi nói rằng người xem sắp được thấy.
- **Lời rủ tương tác và câu đưa về đầu truyện** là lời của kênh — giữ **ý** (bình luận, bấm thích, "để tôi đưa bạn quay lại từ đầu"), đổi chữ mỗi bài. Golden gộp tất cả vào **một câu dài, thì hiện tại**; tách hai câu cũng được.
- **Câu đưa về đầu** thay cho mốc lùi — sau nó, chặng 1 mở thẳng vào nơi chốn và bài toán. Nếu cần, thêm một mốc thời gian ngắn ở đầu chặng 1.

Câu hỏi hỏng khi nó tả một tình trạng chung (*bị coi thường ở chỗ làm*) thay vì một khoảnh khắc; khi gọi tài năng bằng thuật ngữ nghề; khi lặp lại câu trớ trêu; khi chép khung chữ Golden.

---

## 4. Sau khối mở đầu

- Đoạn đầu thân bài dựng **nơi chốn và bài toán**, có giác quan và con số. Người xem cần hiểu thứ đang hỏng quan trọng cỡ nào trước khi gặp cô.
- **Không có lời rủ tương tác nào nữa** cho tới khối đóng bài.
- Cường độ hạ xuống ở phần dựng, rồi leo lại theo `3-cau-truc.md`.

---

## 5. Lỗi đã gặp — đừng lặp lại

| Lỗi | Vì sao hỏng |
|---|---|
| Mở màn là cảnh sỉ nhục thay vì cảnh bắt gặp | Đổi thể loại; xả trước cảnh bị dập ở chặng 2 |
| Mở màn lệch với cảnh ở thân bài | Phá lời hứa "đây là cảnh có thật" |
| Cô giải thích lời giải ngay trong mở màn | Tiêu mất phần thưởng của màn trình diễn |
| Câu đáp của cô chung chung (*I just know machines*) | Trượt phép thử dán; không hứa gì cụ thể |
| Người có quyền xưng danh trong mở màn | Mất trớ trêu — người xem không còn giữ bí mật nào |
| Không biết cảnh ở đâu, mấy giờ | Chỉ có một giọng đọc; đồ vật, thân thể và giờ phải đủ để dựng |
| Nhét một đứa trẻ đứng nhìn | Không làm gì trong cảnh → gợi thương rẻ; user đã chê |
| Chép vỏ câu Golden, chỉ đổi danh từ | Rò khuôn; người xem kênh nghe ra ngay. Xem `12-pattern-golden.md` mục 3 |
| Câu trớ trêu gọi tên tài năng hoặc kết quả | Lặp title, không hứa gì mới |
