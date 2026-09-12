# Title, mở màn, hai dòng lời hứa, mốc lùi

> Viết lại ngày 2026-09-12 theo `GOLDEN-1.txt` mới. Phần mở màn của Golden nằm ở **L2–16** — đọc trọn một lần trước khi viết để nghe nhịp, rồi đóng lại. File này mô tả **chức năng** của từng phần; Golden chỉ là một cách lấp các chức năng đó.

---

## 1. Title

**Giữ nguyên văn title user đưa.** Chỉ đụng vào khi có lỗi gõ rõ ràng hoặc title bằng tiếng Việt; cả hai phải báo ở bước 8.

### 1.1. Đọc title ra dữ kiện

Title dòng này thường cho: **ai giúp** (kèm một lớp phủ: tuổi, nghề, sắc tộc, hoàn cảnh) · **ai được giúp** (cái nhãn bị xa lánh) · **cơn cớ** (thời tiết, hỏng hóc, tai nạn) · **một mốc thời gian** ("lúc rạng sáng", "hôm sau", "ba ngày sau") · **cái xuất hiện sau đó**, thường được úp mở.

Ô nào title không cho thì tự quyết và ghi vào báo cáo.

### 1.2. Title hứa cái quay lại — mở màn thì không nói nó là gì

Người xem biết từ title rằng sẽ có một cái gì đó quay lại. Họ **không** biết nó lớn cỡ nào, gồm những ai, và nó sẽ chạm vào đâu.

Vì vậy mở màn **không giải thích** nhóm người kia là ai, không nói họ tốt, không hé ra rằng họ có mạng lưới. Mở màn chỉ được cho thấy **đúng cái một người qua đường sẽ thấy**: cái nhãn đáng sợ, và một người sắp chết.

Bài không dựa vào một cú lật. Nó dựa vào **quy mô** — và quy mô chỉ có sức nếu người xem bước vào với con mắt của cả thị trấn.

### 1.3. Khi phải tự viết title

Giữ ba thứ: hành động giúp, cái nhãn bị xa lánh, và một mốc thời gian gắn với thứ xuất hiện sau đó. Hai vế ngăn bằng gạch ngang dài. Nếu kho có skill `skills-title`, theo ràng buộc của skill đó: **90–100 ký tự, đúng một dấu `—`, hai mệnh đề**, đo bằng `skills-title/scripts/kiem-title.py` chứ không đếm bằng mắt.

**Ý tưởng lấy từ kho, không tự nghĩ.** Mở `skills-kich-ban/kho-tham-chieu/TITLES.md` (hoặc `skills-title/kho/PHAN-LOAI-131.md`) và chọn một dòng làm gốc. Giữ **lõi tình huống** của dòng đó — cặp quyền lực, loại đòn, trục lật; **đổi ít là đủ** (chức danh, nghề, bối cảnh, tuổi, con số, cách diễn đạt), không bắt viết mới hoàn toàn. Cấm hai đầu: giao nguyên văn dòng kho · nghĩ ra lõi không truy được về dòng kho nào. **Chức vụ và bối cảnh chỉ lấy từ kho** — tra `skills-title/kho/TU-DIEN-KHO.md` (98 chức vụ · 52 bối cảnh); nghề lạ hay nơi lạ là lỗi, kể cả khi nghe hay hơn. Con số, mốc thời gian và tuổi thì tự do. Ghi kèm dòng gốc ở báo cáo bước 8. Luật đầy đủ: `skills-title/references/3-quy-trinh.md` §0.

---

## 2. Mở màn

### 2.1. Mở màn là gì

**Cảnh mở cửa — cảnh lớn nhất của bài — bị nén lại và lôi lên đầu.** Nó xảy ra ở khoảng một phần tư bài, và chặng 5 sẽ đi tới nó rồi diễn lại nó đầy đủ, chậm hơn nhiều. Một địa điểm, một khoảnh khắc. Không phải trailer ghép nhiều thời điểm.

> ### ⛔ Ba trần cứng của mở màn — đếm được, phải đếm
>
> | | Trần | Golden |
> |---|---|---|
> | Tổng số từ **từ câu đầu tới hết hai dòng lời hứa** | **130–165** | 142 |
> | Độ dài câu trung bình trong mở màn | **≤ 5,5 từ** | 4,6 |
> | Tỉ lệ câu từ 5 từ trở xuống | **≥ 65%** | 74% |
>
> **Vì sao ba con số này là trần chứ không phải tham khảo** (khác với bảng ở `12-pattern-golden.md` mục 4, vốn chỉ là tham khảo cho toàn bài): mở màn là ba mươi giây đầu của video. Nó không kể chuyện — nó **gõ**. Mỗi mệnh đề phụ thêm vào là một nhịp gõ bị nuốt. Viết xong thì **đếm thật**, đừng ước lượng: một mở màn 260 từ với câu trung bình 8 từ **nghe như một đoạn văn**, không nghe như một cánh cửa.
>
> Kèm theo đó, trong mở màn:
> - **Không mệnh đề so sánh** (*như thể…*, *như một…*). Golden có 0.
> - **Không mệnh đề phụ chỉ nơi chốn nối vào câu khác** — cho địa điểm đứng riêng thành mảnh câu.
> - **Không câu nào có hai mệnh đề nối bằng "và"** trừ hai dòng lời hứa.

> **Luật khớp.** Bản nén và bản đầy đủ phải **khớp tuyệt đối**: cùng người nói câu quyết định, cùng con số cánh cửa, cùng thứ tự. `GOLDEN-1.txt` sai cả hai chỗ này (người nói câu quyết định đổi giữa L10–12 và L85–90; con số cửa lúc sáu lúc năm). **Không lặp lại lỗi đó.** Viết bản nén sau khi đã phác xong bản đầy đủ, hoặc soát lại ở Cổng 2.

### 2.2. Sáu chức năng mở màn phải làm

Thứ tự và số dòng là tự do. Sáu chức năng thì không.

**1. Câu đầu là tiếng cầu xin, trong miệng người cần giúp.** Thoại, ngắn, đã ở giữa cơn tuyệt vọng. Nó **tự hàm ý rằng đã bị từ chối nhiều lần** — bằng một chữ chỉ phạm vi ("cả cái thị trấn này", "ở đâu cũng vậy"), không bằng lời kể. *Vì sao*: câu đầu tiên phải đặt người xem vào thế bị từ chối, không phải thế được kể chuyện.

**2. Cái nhãn được trưng ra trần trụi, không ai bênh.** Viết bằng **danh từ và mảnh câu**, không tính từ đánh giá — cái người ta thấy, theo đúng thứ tự mắt nhìn thấy. *Vì sao*: nếu người kể làm mềm cái nhãn ngay từ đầu, cả bài mất đối trọng. Người xem phải sợ đúng cái cả thị trấn sợ.

**3. Sổ hai vế, đặt cạnh nhau, không nối bằng liên từ.** Một vế là tình cảnh người cần giúp, tính ra được. Vế kia là **người cho, đưa vào cùng lúc ba dữ kiện: họ là ai, họ còn lại bao nhiêu, và cái đồng hồ**. *Vì sao*: đây là chỗ người xem biết ngay cả hai bên đều ở đáy, mà không cần một câu nào giải thích.

> ⚠️ **Đây là chức năng, không phải một khuôn câu.** Golden lấp nó bằng một chuỗi mảnh câu "Tên, tuổi. Số tiền ở đâu. Giấy tờ ghi ngày." — chuỗi đó nằm trong danh sách cấm ở `12-pattern-golden.md` mục 3. Chạy thử skill này đã tái tạo lại đúng chuỗi đó, vì file này từng mô tả nó như một yêu cầu. **Không dùng lại.**
>
> Ba dữ kiện đó phải vào bằng **một cú pháp khác**, và đổi mỗi bài. Vài hướng:
> - đặt cả ba vào **một việc nhân vật đang làm** lúc tiếng gõ cửa đến;
> - đặt chúng vào **miệng người khác** trong một lượt thoại;
> - đặt chúng lên **một vật** trong khung hình (cái đang cầm, cái dán trên tường, cái vừa gập lại);
> - cho hai dữ kiện vào mở màn và **giấu dữ kiện thứ ba tới chặng 2** — mở màn không bắt buộc phải nói hết.

Một kỹ thuật khác ở đây: **lùi ống kính từng nấc**, nấc cuối mang thông tin đắt nhất. Nếu dùng, **nấc cuối không được rơi vào chính con số cánh cửa** — Golden đã làm thế, và nó là chữ ký. Cho con số cửa vào bằng miệng người, không bằng ống kính.

**4. Cái cần là một người có thể chết đêm nay, và nó được hỏi ra.** Hai hoặc ba lượt thoại, mỗi lượt vài chữ. Một câu hỏi lại. Một câu trả lời đặt tên bộ phận cơ thể, và một chữ chỉ thời gian gấp. *Vì sao*: "họ cần giúp" là một trạng thái; "ông ấy phải ngồi xuống, ngay bây giờ" là một cái đồng hồ.

**5. Quyết định đến dưới dạng một mệnh lệnh trần, và không mảnh nào trong cụm đó giải thích gì.**

```
(a) cơn do dự       — IM LẶNG. Người kể ghi lại rằng cửa chưa mở. Không ai nói thành lời.
(b) người thứ hai đẩy — một câu, ngắn nhất cảnh. Không tranh luận: công nhận nỗi sợ rồi bác nó.
(c) mệnh lệnh        — 2–4 chữ, trần, không kèm lý do.
```

*Vì sao (a) phải im*: mở màn không có chỗ để **đo** một cơn do dự — đo nó là việc của chặng 5, nơi có không gian để liệt kê. Ở đây nó chỉ được là một câu người kể ghi rằng người cho vẫn chưa mở cửa. Một câu là đủ; nó làm cả mở màn dừng lại.

*Vì sao (b) không tranh luận*: người đẩy không cãi rằng nỗi sợ là sai. Họ **nhận lấy con số đáng sợ rồi ra lệnh ngược lại**. Đó là câu hay nhất của mở màn, và nó dài không quá bảy chữ.

*Vì sao (c) trần*: một tiếng "vào đi" có kèm lý do là một **phép tính**. Không kèm gì là một **phản xạ**. Người xem tha thứ cho phép tính; họ chỉ nhớ phản xạ.

**Cả cụm (a)+(b)+(c) cộng lại ≤ 20 từ.**

> ⚠️ **Luật khớp, áp riêng cho cụm này.** Ai nói (b) và ai nói (c) ở mở màn **phải đúng là người đó ở chặng 5**. Golden đảo hai vai này giữa bản nén và bản đầy đủ — đừng lặp lại. Nén được phép **bỏ bớt** (bỏ hẳn phần đo cơn do dự), không được phép **đổi người**.

> ⚠️ Lỗi đã gặp khi chạy thử: viết người cho tự nói ra rằng mình biết cả thị trấn sẽ gọi những người kia là gì. Đó là nhân vật **tự bình luận về mình** — nghe thông minh, và sai. Nhận thức đó thuộc chặng 5, nằm trong đầu họ, do người kể đếm ra.

**6. Con số cánh cửa được nói thành lời và được đáp lại bằng một câu đời thường.** Người cần giúp nói ra con số như một lời xin lỗi. Người cho đáp bằng một câu **không hay ho, không đắt giá**, nói đúng cái đang xảy ra. *Vì sao*: đây là câu người xem sẽ nhớ, và nó chỉ trụ được nếu nó nghe như một người thật nói, không như một câu thoại.

### 2.3. Người kể trong mở màn

- **Câu mảnh chiếm ưu thế.** Danh từ đứng riêng. Không câu nào có mệnh đề phụ thuộc dài.
- **Chỉ ghi lại** — không bình luận, không tính từ đánh giá, không thương hại, không báo trước rằng đây là khoảnh khắc quan trọng.
- Bối cảnh lộ ra **qua đồ vật, thời tiết và người**, không qua một câu giới thiệu địa điểm.
- **Ai ở đâu phải rõ ngay** (`6-van-phong.md` mục 5b). Mở màn ở ngưỡng cửa — trong / ngoài / sau lưng là ba vùng, và mỗi người phải ở rõ một vùng.
- Không ai có mặt mà không làm gì. **Không nhét trẻ em** hay người đứng xem để gợi thương.

### 2.4. Bốn phép thử

- **Bịt tai**: đọc to, không nhìn chữ. Người nghe phải biết ai đang xin, họ trông ra sao, bao nhiêu cửa đã đóng, ai đang sắp chết, và người mở cửa nghèo cỡ nào.
- **Sơ đồ**: vẽ ra ai đứng ở đâu quanh cái ngưỡng cửa. Vẽ không ra là viết lại.
- **Dán**: bỏ cái nhãn cụ thể đi, thay bằng một nhãn khác — nếu cảnh vẫn chạy y hệt thì cảnh chưa bám vào nhóm người này. Viết lại quanh một chi tiết chỉ nhóm này mới có.
- **Khớp**: đặt bản nén cạnh dàn ý chặng 5. Cùng người, cùng câu quyết định, cùng con số, cùng đồ vật.

### 2.5. Cường độ

Mở màn là chỗ cái nhãn được trưng ra thẳng nhất. **Không bao giờ dùng từ lăng mạ chủng tộc**, ở bất kỳ đâu, kể cả trong miệng người từ chối. Xem `9-chu-de-nhay-cam.md`.

---

## 3. Sau mở màn: hai dòng lời hứa

> **Dòng này KHÔNG có lời rủ tương tác.** Golden không có, và không được thêm: không câu hỏi hướng vào người xem, không "bấm thích", không "để tôi đưa bạn quay lại từ đầu". Nếu user yêu cầu riêng thì mới thêm.

Ngay sau mở màn là **hai dòng**, mỗi dòng một đoạn. Đây là chỗ duy nhất ở đầu bài người kể bước ra khỏi cảnh.

### 3.1. Dòng thứ nhất — quy mô, đặt trên cùng một mặt đất

Việc của nó: nói rằng **tại đúng chỗ này**, sau **một khoảng thời gian ngắn đo được**, một thứ **đếm được và lớn đến mức vô lý** sẽ xuất hiện.

Ba thành phần bắt buộc:
- **Một mốc thời gian gần** — ngày, không phải năm. Nó phải khớp với khung thời gian thật của truyện.
- **Một con số** gắn với thứ sẽ tới. Con số là toàn bộ sức của dòng này; đừng thay nó bằng một tính từ.
- **Cùng một địa điểm vật lý** vừa xuất hiện trong mở màn, gọi lại bằng đúng thứ vừa được nhìn thấy.

**Thì tương lai trong quá khứ** (*would*). *Vì sao*: nó báo cho người nghe rằng người kể biết trước, mà không kéo họ ra khỏi thì quá khứ của truyện. Người xem chuyển từ "chuyện gì đang xảy ra" sang "chuyện đó dẫn tới đâu".

**⛔ Trần: mỗi dòng không quá 14 từ.** Golden: 10 và 10. Đây là hai câu quan trọng nhất của cả bài — sức của chúng nằm ở chỗ **không có gì để bám vào ngoài con số**. Mọi mệnh đề phụ thêm vào ("và không ai trong số họ lấy một xu") đều là một thứ để người xem bám vào thay vì con số, và nó làm dòng đó xẹp. Nếu thấy tiếc một chi tiết, để nó lại cho chặng 7 — ở đó nó đắt hơn nhiều.

### 3.2. Dòng thứ hai — tầm với

Việc của nó: nói rằng chuyện **không dừng ở cái sân đó**. Không con số, không chi tiết — chỉ một phạm vi rộng hơn hẳn dòng trên (nhiều vùng, nhiều đời người, nhiều năm), gắn với **tên** hoặc **cái tên nghề** của người cho.

*Vì sao*: dòng một hứa một cảnh; dòng hai hứa một hệ quả. Người xem ở lại vì cả hai.

**⛔ Trần: không quá 14 từ.**

> **Chống rập khuôn ở chỗ này.** Golden vào hai dòng bằng "[N ngày] sau, …" rồi "Và cái tên … sẽ …". Cặp mở đầu đó là chữ ký. Đổi lối vào mỗi bài: bắt đầu từ địa điểm; bắt đầu từ một người sẽ có mặt; bắt đầu bằng một phủ định ("Không ai trong số họ sẽ …"); hoặc đảo thứ tự hai dòng. Chỉ **chức năng** của hai dòng là bất biến.

### 3.3. Lỗi của hai dòng lời hứa

| Lỗi | Vì sao hỏng |
|---|---|
| Nói ra nhóm kia là ai, vì sao họ quay lại | Giết toàn bộ chặng 6 |
| Dùng tính từ thay con số ("một điều không ngờ") | Doạ suông; không có hình |
| Mốc thời gian mơ hồ ("một ngày nào đó") | Mất đồng hồ |
| Ba dòng trở lên | Thành tóm tắt phim; hai là đủ |
| Thêm câu hỏi hướng vào người xem | Không thuộc dòng này |
| Đặt ở thì hiện tại, giọng bình luận | Kéo người xem ra khỏi truyện |

---

## 4. Mốc lùi

Một câu, đứng riêng một đoạn, mở chặng 2. Nó làm **hai việc cùng lúc**:
- cho khoảng lùi, tính bằng **giờ** hoặc **ngày**, và gọi lại sự kiện ở mở màn bằng đúng hành động vật lý của nó (cái gõ cửa, cái tiếng xe, cái lúc họ đi tới);
- và **đã bắt đầu nghi thức** ngay trong nửa sau của câu — người cho đang làm cái việc họ vẫn làm, kèm số năm họ đã làm nó.

*Vì sao*: câu này phải quay ngược thời gian mà không làm bài chững lại. Gộp nghi thức vào chính nó là cách rẻ nhất để làm điều đó.

---

## 5. Sau mốc lùi

- Chặng 2 đặt người cho vào **nghi thức** của họ, có giờ giấc, có mùi, có tiếng, có một người thứ hai.
- **Cường độ hạ hẳn xuống.** Mở màn dồn dập; đoạn sau nó phải chậm và ấm, nếu không người xem không có chỗ thở và con số ở chặng 2 không kịp ngấm.
- Không có lời rủ tương tác nào, ở bất kỳ đâu trong bài.

---

## 6. Lỗi đã gặp — đừng lặp lại

| Lỗi | Vì sao hỏng |
|---|---|
| Người cho đồng ý ngay, không do dự | Mất động cơ 3; nhân vật thành thánh |
| Người kể bênh nhóm bị xa lánh ngay trong mở màn | Mất đối trọng; người xem không còn gì để đổi ý |
| Không có con số cánh cửa | Mất đơn vị đo của cả bài |
| Bản nén mâu thuẫn với bản đầy đủ ở chặng 5 | Phá lời hứa "đây là cảnh có thật" — Golden mắc lỗi này |
| Chép vỏ câu Golden, chỉ đổi danh từ | Rò khuôn. Xem `12-pattern-golden.md` mục 3 |
| Người cần giúp nói dài, giải thích hoàn cảnh | Người đang kiệt sức nói ngắn |
| Thêm câu hỏi tương tác hoặc lời rủ bình luận | Không thuộc dòng này |
| Hai dòng lời hứa tiết lộ hình thức đền đáp | Không còn gì để xem |
| Nhét một đứa trẻ đứng nhìn trong cảnh khốn cùng | Không làm gì trong cảnh → gợi thương rẻ; user đã chê |
| Viết chữ nước ngoài ở bất kỳ đâu | Khán giả Mỹ nghe một giọng đọc, không hiểu |
