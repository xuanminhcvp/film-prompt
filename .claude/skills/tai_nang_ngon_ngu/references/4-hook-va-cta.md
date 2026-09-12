# Title, mở màn, câu hook, lời rủ tương tác

> Viết lại ngày 2026-09-11 theo `GOLDEN-1.txt`. Phần mở màn của Golden nằm ở **L2–16** — đọc trọn một lần trước khi viết để nghe nhịp, rồi đóng lại. File này mô tả **chức năng** của từng phần; Golden chỉ là một cách lấp các chức năng đó.

---

## 1. Title

**Giữ nguyên văn title user đưa.** Chỉ đụng vào khi có lỗi gõ rõ ràng hoặc title bằng tiếng Việt; cả hai phải báo ở bước 8.

### 1.1. Đọc title ra dữ kiện

Title dòng này thường cho: **ai có quyền** · **ai bị coi thường** (thân phận, đôi khi kèm một lớp phủ như chủng tộc, tuổi, giới) · **cái hắn không biết** (thường là một con số thứ tiếng) · **căn phòng kín** (thứ tiếng hắn dùng) · **hành vi** · **kết cục được hứa**.

Ô nào title không cho thì tự quyết và ghi vào báo cáo.

### 1.2. Title nói ra tài năng — mở màn thì không

Người xem biết từ title rằng nhân vật chính hiểu. Phản diện không biết. **Toàn bộ sức căng của mở màn là người xem giữ bí mật cùng nhân vật chính** trong lúc phản diện nói.

Vì vậy, trong mở màn nhân vật chính **không để lộ tài năng** — không đáp bằng thứ tiếng kia, không cười hiểu ý, không liếc. Bất kỳ dấu hiệu nào cũng xả áp suất mà cả bài cần giữ tới cao trào.

Bài không dựa vào việc giấu danh tính. Bí mật của bài là **khi nào và bằng cách nào** nhân vật chính lên tiếng.

### 1.3. Khi phải tự viết title

Giữ ba thứ: thân phận ở đáy, một con số hoặc một chi tiết đo được về tài năng, và tên thứ tiếng (hoặc hành vi) của phản diện. Hai vế ngăn bằng gạch ngang dài. Nếu kho có skill `skills-title`, theo ràng buộc của skill đó: **90–100 ký tự, đúng một dấu `—`, hai mệnh đề**, đo bằng `skills-title/scripts/kiem-title.py` chứ không đếm bằng mắt.

**Ý tưởng lấy từ kho, không tự nghĩ.** Mở `skills-kich-ban/kho-tham-chieu/TITLES.md` (hoặc `skills-title/kho/PHAN-LOAI-131.md`) và chọn một dòng làm gốc. Giữ **lõi tình huống** của dòng đó — cặp quyền lực, loại đòn, trục lật; **đổi ít là đủ** (chức danh, nghề, bối cảnh, tuổi, con số, cách diễn đạt), không bắt viết mới hoàn toàn. Cấm hai đầu: giao nguyên văn dòng kho · nghĩ ra lõi không truy được về dòng kho nào. **Chức vụ và bối cảnh chỉ lấy từ kho** — tra `skills-title/kho/TU-DIEN-KHO.md` (98 chức vụ · 52 bối cảnh); nghề lạ hay nơi lạ là lỗi, kể cả khi nghe hay hơn. Con số, mốc thời gian và tuổi thì tự do. Ghi kèm dòng gốc ở báo cáo bước 8. Luật đầy đủ: `skills-title/references/3-quy-trinh.md` §0.

---

## 2. Mở màn

### 2.1. Mở màn là gì

**Một cảnh có thật ở giữa truyện, bị lôi lên đầu và nén lại.** Nó xảy ra ở khoảng giữa bài (Golden: ~40%), và thân bài sẽ đi tới nó rồi diễn lại nó đầy đủ hơn. Một địa điểm, một khoảnh khắc, khoảng 100–150 từ. Không phải trailer ghép nhiều thời điểm.

### 2.2. Sáu chức năng mở màn phải làm

Thứ tự và số dòng là tự do. Sáu chức năng thì không.

**1. Mở giữa cơn khinh miệt, bằng miệng phản diện.** Câu đầu là thoại, ngắn, đã đang căng. Nó bám vào **một đồ vật trong công việc của nhân vật chính** và, nếu title có lớp phủ, chạm vào lớp phủ đó. *Vì sao*: người nghe cần một kẻ không thể bênh trong vài giây đầu, và đồ vật cho họ biết ngay đây là nơi nào, ai đang phục vụ ai.

**2. Có một hành vi làm nhục nhìn thấy được**, để lại dấu trên thân thể hoặc đồng phục nhân vật chính, và có người khác trong phòng thấy. *Vì sao*: lời nói trôi đi, dấu vết thì ở lại — và nó sẽ còn trên người cô suốt phần sau.

**3. Phản diện chuyển sang căn phòng kín, và người nghe biết chính xác lúc đó.** Tên thứ tiếng được gọi ra. Lời hắn trong ngoặc kép được viết bằng tiếng Anh để người nghe hiểu, và **mỗi câu tự mang nhãn thứ tiếng trong câu dẫn của nó** (`6-van-phong.md` mục 5.1). *Vì sao*: nếu người nghe không biết câu nào là câu bí mật, trớ trêu không tồn tại.

**4. Lời bí mật mang hai thứ: khinh miệt nhân vật chính, và mầm hại một người khác.** Mầm đó là thứ sẽ hạ hắn — nên nó nằm **trong miệng phản diện**, không phải trong miệng nhân vật chính. Người bị hại có mặt, và người nghe biết họ không hiểu. *Vì sao*: khinh miệt làm người xem giận; mầm hại người khác cho họ một cốt truyện và một con tin.

**5. Nhân vật chính giữ phẩm giá mà không lộ gì.** Cô tiếp tục làm việc của nghề mình; nếu nói, cô nói một câu bình thường đến mức đau. Sự vững vàng được cho thấy qua **thân thể** (người kể ghi nhận), không qua lời đốp chát. *Vì sao*: lễ phép suông làm người xem thương hại; lễ phép cộng một thân thể không run làm họ biết người này đang chờ.

**6. Đóng lại bằng một nhịp mở sang lời hứa.** Mở màn dừng ở chỗ phản diện đã quay đi và nhân vật chính vẫn đứng — rồi câu hook nhận lấy.

### 2.3. Người kể trong mở màn

Golden để người kể chiếm khoảng hai phần ba số dòng, xen giữa bốn lượt thoại. Tỉ lệ đó **không bắt buộc**, nhưng tính chất thì có:

- Câu ngắn, mảnh câu, động từ và danh từ đi trước. Không câu nào dài lê thê.
- Chỉ ghi lại — không bình luận, không tính từ đánh giá, không thương hại.
- Bối cảnh lộ ra **qua đồ vật và người**, không qua một câu giới thiệu địa điểm.
- **Ai ở đâu phải rõ ngay**, và số người phải hợp với không gian (`6-van-phong.md` mục 5b). Mở màn thường diễn ra trong không gian chật — ai không cần có mặt thì cho họ có mặt từ xa (điện thoại, màn hình) hoặc bỏ.
- Không ai có mặt mà không làm gì. Không nhét trẻ em hay người đứng xem để gợi thương.

### 2.4. Bốn phép thử

- **Bịt tai**: đọc to, không nhìn chữ. Người nghe phải biết ai khinh ai, bằng thứ tiếng gì, ai đang bị hại, và nhân vật chính có run không.
- **Sơ đồ**: vẽ ra ai ngồi/đứng ở đâu. Vẽ không ra hoặc thấy chật là viết lại.
- **Dán**: câu khinh miệt của phản diện dán sang một truyện khác mà vẫn đứng → nó chưa bám nghề nhân vật chính. Viết lại quanh một đồ vật.
- **Khớp**: đặt mở màn cạnh dàn ý cảnh ở giữa bài. Cùng người, cùng đồ vật, cùng việc đang làm. Những câu bí mật trong mở màn sẽ quay lại ở cao trào — viết sao cho đáng nghe lần nữa.

### 2.5. Cường độ

Mở màn là chỗ sỉ nhục thẳng nhất của bài và được chạm vào lớp phủ trong title. **Không bao giờ dùng từ lăng mạ chủng tộc**, ở bất kỳ thứ tiếng nào. Xem `9-chu-de-nhay-cam.md`.

---

## 3. Sau mở màn: ba phần, ba việc

Ngay sau mở màn là một khối ngắn — Golden dùng ba dòng (L14–16). Đây là chỗ duy nhất ở đầu bài người kể nói thẳng với người xem.

### 3.1. Câu hook — lời hứa cái giá

**Việc của nó**: bẻ từ khoảnh khắc nhân vật chính im lặng sang lời hứa rằng im lặng đó sẽ khiến phản diện trả giá.

Tính chất Golden dùng, và vì sao chúng chạy:
- **Người kể bước ra khỏi cảnh** — Golden đổi sang thì hiện tại. Sự đổi thì báo cho người nghe rằng cảnh đã dừng và ai đó đang nói với họ.
- **Không gọi tên tài năng.** Title đã gọi; câu hook chỉ xác nhận khoảng cách giữa cái phản diện biết và cái người xem biết.
- **Có một mốc thời gian gần**, khớp với khung thời gian của truyện.
- **Có cái giá** mà phản diện sẽ trả.

Một câu, ngắn. Viết mới cho từng bài; không dùng lại khung chữ của Golden.

### 3.2. Câu hỏi và lời rủ tương tác

**Việc của nó**: gọi người xem vào đúng khoảnh khắc họ sẽ được thấy — rồi xin tương tác, rồi đưa họ quay lại từ đầu.

- **Câu hỏi hướng vào người xem như người chứng kiến cú lật** (Golden: *Have you ever watched…*). Nó tả **một phản ứng thân thể của phản diện** và **cái nhân vật chính sẽ làm**, bằng lời đời thường, theo hướng đảo ngược thế thượng phong. *Vì sao*: người xem đã biết trước cú lật từ title; thứ kéo họ ở lại là **khuôn mặt phản diện lúc căn phòng kín bị mở**. Câu hỏi hứa đúng khoảnh khắc đó, và người xem sẽ nhận ra nó khi tới nơi.
- **Lời rủ tương tác và câu đưa về đầu truyện** là lời của kênh — giữ **ý** (bình luận, bấm thích, "để tôi đưa bạn quay lại từ đầu"), đổi chữ mỗi bài. Golden gộp cả ba vào một câu dài; tách hai câu cũng được.

Câu hỏi hỏng khi nó tả một tình trạng chung (*bị coi thường ở chỗ làm*) thay vì một khoảnh khắc; khi không có thân thể phản diện; khi gọi tài năng bằng con số hay thuật ngữ; khi lặp lại câu hook.

### 3.3. Mốc lùi

**Việc của nó**: cắt về quá khứ gần, báo cho người nghe biết phần sau bắt đầu từ đâu. Golden dùng một mảnh câu thời gian đứng riêng một dòng. Chọn mốc theo khung thời gian thật của truyện bạn — vài giờ, sáng hôm đó, ba ngày trước.

---

## 4. Sau mốc lùi

- Đoạn đầu thân bài đặt nhân vật chính vào **công việc bình thường của họ**, có giờ giấc và giác quan. Người xem cần thấy cô trước khi thấy cô bị khinh.
- **Không có lời rủ tương tác nào nữa** cho tới khối đóng bài.
- Cường độ của mở màn **hạ xuống** ở phần dựng, rồi leo lại theo `3-cau-truc.md`.

---

## 5. Lỗi đã gặp — đừng lặp lại

| Lỗi | Vì sao hỏng |
|---|---|
| Không biết cảnh ở đâu | Chỉ có một giọng đọc; đồ vật và người phải đủ để dựng phòng |
| Nhét một đứa trẻ đứng nhìn | Không làm gì trong cảnh → gợi thương rẻ; user đã chê |
| Mở màn mâu thuẫn với cảnh ở thân bài | Phá lời hứa "đây là cảnh có thật" |
| Chép vỏ câu Golden, chỉ đổi danh từ | Rò khuôn; người xem kênh nghe ra ngay. Xem `12-pattern-golden.md` mục 3 |
| Thoại phản diện chung chung | Trượt phép thử dán |
| Nhân vật chính đáp bằng thứ tiếng bí mật ngay trong mở màn | Xả hết áp suất của cả bài |
| Viết chữ nước ngoài ở bất kỳ đâu (câu tiếng gốc, phiên âm, kính ngữ) | Khán giả Mỹ nghe một giọng đọc, không hiểu → mất đúng khoảnh khắc cần hiểu nhất |
| Chỉ báo thứ tiếng một lần rồi để các câu sau tự hiểu | Đội làm video không biết câu nào phải lồng tiếng nước ngoài |
| Nhồi ba người vào băng ghế sau xe, không nói ai ngồi đâu | Người nghe không dựng được cảnh. Người không cần ngồi đó thì cho họ có mặt qua điện thoại |
| Lời bí mật chỉ có khinh miệt, không có mầm hại người khác | Mất con tin, mất cốt truyện |
| Câu hook gọi tên tài năng | Lặp title, không hứa gì mới |
