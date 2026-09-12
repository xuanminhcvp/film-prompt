# Title, mở màn, câu trớ trêu, lời rủ tương tác

> Viết lại ngày 2026-09-12 theo Golden mới. Phần mở màn của Golden nằm ở **L3–14** — đọc trọn một lần trước khi viết để nghe nhịp, rồi đóng lại. File này mô tả **chức năng** của từng phần; Golden chỉ là một cách lấp các chức năng đó.
>
> ⚠️ **Bốn luật trong file này cố ý đòi cao hơn Golden** (đánh dấu 🔺). User đã xem mở màn của Golden và đánh giá là chưa đạt. Ở bốn chỗ đó, **file này thắng Golden** — đừng "sửa lại cho khớp Golden" ở vòng duyệt nào. Bốn chỗ: nhân vật chính phải có một câu có nội dung · kẻ gác cổng phải có một niềm tin hắn cho là chính đáng · bài toán phải có thước đo cứng · đám đông phải có một gương mặt riêng.

---

## 1. Title

**Giữ nguyên văn title user đưa.** Chỉ đụng vào khi có lỗi gõ rõ ràng hoặc title bằng tiếng Việt; cả hai phải báo ở bước 8.

### 1.1. Đọc title ra dữ kiện

Title dòng này thường cho: **kẻ gác cổng** (giáo sư, bếp trưởng, giám đốc, huấn luyện viên) · **cái nhãn của nhân vật chính** (thường kèm một lớp phủ: chủng tộc, tuổi, giới) · **việc hắn ép cô làm** · **lý do hắn nói ra miệng** ("cho vui", "cho học trò tôi cười") · **thước đo kết quả** — thường là **một khoảng thời gian ngắn** ("in 3 minutes") hoặc một mệnh đề kết quả ("silenced the room").

Ô nào title không cho thì tự quyết và ghi vào báo cáo. Title **không bao giờ cho** ba thứ quan trọng nhất: bài toán thật, lời giải thật, và cái sẽ hạ kẻ gác cổng ở cuối. Ba thứ đó luôn phải tự dựng.

### 1.2. Title nói ra kết quả — mở màn giữ lại cách làm

Người xem biết từ title rằng cô sẽ làm được. Thứ họ chưa biết là **bằng cách nào**, **cô đã bị lấy mất gì để rơi xuống đây**, và **cái giá phải trả cho việc được nhìn thấy**. Mở màn cho họ thấy **giây phút trước khi cô bắt đầu**, và dừng ở đó.

Vì vậy trong mở màn, cô **không bắt đầu giải**, và không để lộ tài năng hay quá khứ. Mở màn kết thúc ở nhịp cô nhìn vào bài toán.

🔺 **Nhưng cô phải nói đúng một câu có nội dung.** Golden chỉ cho cô một câu xin lỗi bị cắt cụt giữa từ — kết quả là suốt mở màn cô là đồ vật trong chính cảnh của mình, và người xem thương hại cô thay vì đứng về phía cô. Xem chức năng 3 dưới đây.

### 1.3. Khi phải tự viết title

Giữ bốn thứ: chức danh của kẻ gác cổng, cái nhãn của nhân vật chính, **lý do mua vui nói thẳng ra miệng**, và **một thước đo ngắn gây sốc** ở vế sau. Hai vế ngăn bằng gạch ngang dài. Nếu kho có skill `skills-title`, theo ràng buộc của skill đó: **90–100 ký tự, đúng một dấu `—`, hai mệnh đề**, đo bằng `skills-title/scripts/kiem-title.py` chứ không đếm bằng mắt.

**Ý tưởng lấy từ kho, không tự nghĩ.** Mở `skills-kich-ban/kho-tham-chieu/TITLES.md` (hoặc `skills-title/kho/PHAN-LOAI-131.md`) và chọn một dòng làm gốc. Giữ **lõi tình huống** của dòng đó — cặp quyền lực, loại đòn, trục lật; **đổi ít là đủ** (chức danh, nghề, bối cảnh, tuổi, con số, cách diễn đạt), không bắt viết mới hoàn toàn. Cấm hai đầu: giao nguyên văn dòng kho · nghĩ ra lõi không truy được về dòng kho nào. **Chức vụ và bối cảnh chỉ lấy từ kho** — tra `skills-title/kho/TU-DIEN-KHO.md` (98 chức vụ · 52 bối cảnh); nghề lạ hay nơi lạ là lỗi, kể cả khi nghe hay hơn. Con số, mốc thời gian và tuổi thì tự do. Ghi kèm dòng gốc ở báo cáo bước 8. Luật đầy đủ: `skills-title/references/3-quy-trinh.md` §0.

---

## 2. Mở màn

### 2.1. Mở màn là gì

**Cảnh sỉ nhục có thật ở khoảng một phần tám bài — lúc kẻ gác cổng ấn công cụ của nghề vào tay cô — bị lôi lên đầu và nén lại.** Thân bài sẽ đi tới nó rồi diễn lại nó đầy đủ, chậm hơn, đông người hơn. Một địa điểm, một khoảnh khắc, **120–160 từ** (Golden: 140). Không phải trailer ghép nhiều thời điểm. Đếm bằng `scripts/kiem-do-dai.py`, không đếm bằng mắt.

**Vì sao là cảnh sỉ nhục chứ không phải cảnh chiến thắng**: chiến thắng mà không có nợ thì không ai xem hết. Mở màn phải làm người xem **giận trong mười lăm giây đầu** — và rồi treo họ ở đúng nhịp trước khi món nợ bắt đầu được trả. Cảnh chiến thắng thuộc về thân bài, và nó chỉ đắt nếu đã có cảnh này.

**Vì sao ngắn**: mở màn chỉ cần đủ để người xem giận và tò mò. Chi tiết về nơi chốn, về đám đông, về bài toán thuộc về thân bài — nhét lên đây là tiêu trước phần thưởng và làm người xem chờ quá lâu mới tới lời rủ.

Mở màn phải **khớp** với cảnh ở thân bài — cùng người, cùng vật, cùng lời thoại chủ chốt, cùng động tác. Thân bài được phép **thêm**, không được phép **khác**.

### 2.2. Bảy chức năng mở màn phải làm

Thứ tự và số dòng là tự do. Bảy chức năng thì không.

**1. Câu đầu tiên là lời xúc phạm của kẻ gác cổng, không có câu dẫn.** Người xem chưa biết ai nói, nói ở đâu, nói về ai. *Vì sao*: một câu xúc phạm trần trụi, không ngữ cảnh, ép người nghe phải ở lại để biết nó nhắm vào ai. Câu đó phải **gọi một con người bằng một thứ không phải người**, hoặc phủ nhận quyền có mặt của cô.

**2. Quy mô đám đông, ngay câu thứ hai, bằng một động tác tập thể có con số.** *Vì sao*: nó biến một câu chửi thành một sự kiện công khai. Con số ở đây là thứ định giá cả bài — người xem lập tức biết cú lật sẽ xảy ra trước bao nhiêu người.

**3. 🔺 Cô nói đúng một câu, và câu đó đúng sự thật.** Ba đến bảy chữ. Nó khẳng định **tư cách có mặt** của cô hoặc nêu **một dữ kiện khô về việc cô đang làm** — không xin lỗi, không chối, không giải thích. Rồi hắn gạt nó đi: cắt lời, nhại lại, hoặc trả lời bằng một câu chạm vào **thân thể** cô, và **đoạt lấy công cụ lao động của cô rồi ném đi**.

*Vì sao đổi*: Golden cho cô một câu xin lỗi cụt giữa từ (*"Thưa thầy, em chỉ đang lau—"*). Nó nhanh, nhưng nó đặt cô vào thế xin phép được tồn tại, và người xem nhận về **lòng thương hại** — thứ cảm xúc yếu nhất trong ba thứ khả dĩ. Khi cô nói một điều **đúng** và bị cười vào mặt, người xem nhận về **sự phẫn nộ**, và họ đứng về phía cô chứ không đứng bên trên cô. Đây cũng là hạt giống của tính cách: người này không cãi, nhưng cũng không tự thu nhỏ.

*Cách viết*: câu của cô phải **đúng nhưng đã bị tước hết ngữ cảnh**, nên nghe như một lời chống chế tầm thường. "Tôi làm ca đêm ở đây." · "Phòng này tôi dọn sáu năm rồi." · "Bảy giờ tôi mới hết ca." Người xem chưa biết nó nặng cỡ nào; cả phòng thì không bao giờ biết.

*Biến thể được phép*: câu xin lỗi cụt giữa từ vẫn dùng được — nhưng làm **nấc thứ nhất**, và cô vẫn phải có câu có nội dung ở nấc sau.

**4. Cô im. Một dòng.** *Vì sao*: sau hai nấc, một dòng im lặng đứng riêng có sức nặng hơn bất kỳ câu tả cảm xúc nào. Đây cũng là lần đầu người xem thấy thứ sẽ là tính cách xuyên suốt của cô.

**5. Hắn xoay sỉ nhục thành trò chơi — và tự trao sân khấu.** Hắn đổi ý giữa chừng (*"Thật ra — ở lại đây"*), chỉ vào **bài toán mà người có chức danh đã thua**, kèm một mệnh đề đo được (bao lâu, bao nhiêu người đã thử). Rồi hắn **nói thẳng lý do**: để mua vui. *Vì sao*: đây là động cơ trung tâm của thể loại (`1-nguyen-ly-cot-loi.md` động cơ 3). Việc hắn nói thẳng "cho học trò tôi cười" là thứ khiến người xem không thể rời đi.

🔺 **Và hắn phải nói ra một niềm tin hắn cho là chính đáng** — một câu, trong mở màn, về vai trò hắn tin mình đang bảo vệ: chuẩn mực của ngành, công sức của những người đã trả giá để vào được phòng này, danh dự của chỗ ngồi. *Vì sao*: Golden chỉ cho hắn sự tàn nhẫn thuần tuý (*"cô làm hôi cả phòng"*). Một kẻ ác không có lý do thì người xem xem xong **yên tâm vì mình không giống hắn** — và bài mất hết sức nặng xã hội. Một người tin chắc mình đúng thì người xem nhận ra cơ chế đó ở quanh mình, và ở chính mình. Câu đó cũng là câu sẽ bị đọc lại trước mặt hắn ở cuối bài.

🔺 **Bài toán phải có thước đo cứng.** Không phải "một phương trình chưa ai giải được" — mà **tên của nó, thời gian nó đứng đó, và số người đã thua nó**, ít nhất hai trong ba. *Vì sao*: người xem cần một con số để cầm. "Chưa ai giải được" là lời hứa suông; "mười một ngày, bốn nghiên cứu sinh, hai lần gửi đi hỏi" là một bức tường có kích thước.

**6. Công cụ của nghề được ấn vào tay cô, kèm một câu nghi ngờ cô có trí.** *Vì sao*: đối xứng với việc công cụ lao động của cô bị ném đi ở chức năng 3. Hai động tác đó gói cả truyện vào một cảnh, và người xem cảm được sự đối xứng mà không cần ai chỉ ra.

**7. Đám đông nhập cuộc và máy quay giơ lên. Rồi cô nhìn vào bài toán.** Một dòng cho đám đông (tiếng vỗ bàn, ngón tay chỉ, đèn đỏ), một dòng ngắn cho cô.

🔺 **Trong đám đông phải có đúng một gương mặt riêng** — một người có nghề nghiệp hoặc một chi tiết nhận dạng, làm **một cử chỉ lệch khỏi đám đông**: không cười, quay đi, mở miệng rồi thôi, cúi xuống nhìn giấy. Một dòng, không giải thích. *Vì sao*: Golden để đám đông là một khối hai trăm người phản ứng đồng loạt — nên sự im lặng của họ không tốn gì và không ai phải trả giá cho nó ở cuối. Một người do dự biến đám đông từ phông nền thành **chỗ người xem thật sự đang đứng**. Người đó cũng là chỗ rẻ nhất để cài người sẽ lên tiếng ở chặng sau. *Vì sao*: máy quay là hạt giống của cả chặng sau và phải được cài ở đây. Còn dòng cuối về cô là cánh cửa mở — mở màn dừng đúng ở đó, trước khi cô chạm vào bài toán.

### 2.3. Người kể trong mở màn

- Câu ngắn, mảnh câu, danh từ và động từ đi trước. Phần lớn dòng là một hoặc hai câu.
- **Thoại chiếm quá nửa mở màn.** Đây là cảnh của giọng nói, không phải của mô tả.
- Chỉ ghi lại — không bình luận, không tính từ đánh giá, không thương hại. Người kể **không được nói cô cảm thấy gì**.
- Bối cảnh lộ ra **qua đồ vật, thân thể và phản ứng tập thể**, không qua một câu giới thiệu địa điểm. Người xem không cần biết tên nơi này ở mở màn.
- **Ai ở đâu phải rõ ngay** (`6-van-phong.md` mục 5b): hắn ở đâu, cô ở đâu, đám đông ở đâu, bài toán ở đâu.
- Không ai có mặt mà không làm gì. Không nhét trẻ em hay người đứng xem để gợi thương.

### 2.4. Bốn phép thử

- **Bịt tai**: đọc to, không nhìn chữ. Người nghe phải biết ai đang bị hạ nhục, trước bao nhiêu người, bị ép làm gì, và vì sao kẻ kia làm thế.
- **Sơ đồ**: vẽ ra ai đứng/ngồi ở đâu, cạnh vật gì.
- **Giận**: đọc cho một người chưa biết gì nghe. Nếu họ không thấy tức ở khoảng câu thứ ba hoặc thứ tư, cái thang chưa leo đủ hoặc chưa chạm đủ ba thứ khác nhau.
- **Khớp**: đặt mở màn cạnh dàn ý cảnh sỉ nhục ở thân bài. Cùng người, cùng vật, cùng lời thoại chủ chốt, cùng động tác.

### 2.5. Cường độ

Mở màn của thể loại này **là cảnh sỉ nhục** — mạnh nhất có thể mà không dùng từ lăng mạ trực tiếp về chủng tộc hay thân thể theo kiểu tục tĩu (`9-chu-de-nhay-cam.md`). Sức nặng đến từ **sự công khai** và từ **giọng thản nhiên của kẻ có quyền**, không từ độ thô của từ ngữ. Hắn không gào; hắn cười.

---

## 3. Sau mở màn: câu trớ trêu, lời rủ, câu đưa về đầu

Ngay sau mở màn là một khối rất ngắn — Golden dùng hai dòng (L13–14). Đây là chỗ duy nhất ở đầu bài người kể nói thẳng với người xem.

### 3.1. Câu trớ trêu — lời hứa

**Việc của nó**: đóng mở màn bằng khoảng cách giữa điều căn phòng tin và điều sắp xảy ra.

Tính chất, và vì sao chúng chạy:
- **Vẫn thì quá khứ, vẫn ngôi ba.** Người kể chưa quay ra nói với người xem.
- **Đo bằng chính đơn vị của title** — nếu title nói ba phút thì câu này nói ba phút. *Vì sao*: nó biến con số trong title thành một cái đồng hồ mà người xem bắt đầu đếm.
- **Chủ ngữ là đám đông, không phải cô.** Thứ được hứa không phải "cô sẽ làm được" (title đã nói rồi) mà là **phản ứng của những người đang cười**. Đó là thứ người xem thật sự tới để xem.
- **Không nói kết quả, không gọi tên tài năng.**

Một câu, ngắn. Viết mới cho từng bài; **không dùng lại cụm *"none of them were ready for"*** hay biến thể của nó — đó là chữ ký Golden.

### 3.2. Câu hỏi, lời rủ, câu đưa về đầu

**Việc của nó**: gọi người xem vào đúng loại khoảnh khắc họ sẽ được thấy — rồi xin tương tác, rồi đưa họ quay lại từ đầu.

- **Câu hỏi hướng vào người xem như người sắp chứng kiến**, và nó có **hai vế nối bằng "rồi"**: vế một là **cái đã xảy ra ở mở màn** (bị xé nát trước đám đông), vế hai là **cái sắp xảy ra** (làm cả căn phòng đó câm lặng) — và vế hai kết bằng **công cụ tầm thường của nghề**, gọi bằng tên đời thường nhất của nó. *Vì sao*: hai vế dựng lại đúng đường cong cảm xúc của cả bài trong một câu; và cái công cụ rẻ tiền ở cuối câu là hình ảnh người xem sẽ nhớ.
- **Lời rủ tương tác và câu đưa về đầu truyện** là lời của kênh — giữ **ý** (bình luận, bấm thích, "để tôi đưa bạn quay lại từ đầu"), đổi chữ mỗi bài. Golden gộp tất cả vào một câu dài, thì hiện tại; tách hai câu cũng được. **Trần 55 từ.**
- **Câu đưa về đầu** thay cho mốc lùi — sau nó, chặng 1 mở thẳng vào nơi chốn.

Câu hỏi hỏng khi nó chỉ có một vế; khi nó tả một tình trạng chung (*bị coi thường ở chỗ làm*) thay vì một khoảnh khắc; khi gọi tài năng bằng thuật ngữ nghề; khi lặp lại câu trớ trêu; khi chép khung chữ Golden.

---

## 4. Sau khối mở đầu

- Đoạn đầu thân bài dựng **nơi chốn và thứ bậc của nó**, không dựng bài toán. Bài toán tới sau, ở cuối chặng 1.
- **Không có lời rủ tương tác nào nữa** cho tới khối đóng bài.
- Cường độ hạ hẳn xuống ở phần dựng — đây là chỗ duy nhất trong bài được phép chậm — rồi leo lại theo `3-cau-truc.md`.

---

## 5. Lỗi đã gặp — đừng lặp lại

| Lỗi | Vì sao hỏng |
|---|---|
| Mở màn là cảnh chiến thắng hoặc cảnh công bố ở cuối | Xả trước phần thưởng, và người xem chưa có lý do để giận |
| Mở màn bắt đầu bằng câu dẫn hoặc tả cảnh | Mất cú đấm của câu thoại trần trụi; người xem trôi đi ở dòng đầu |
| Chỉ leo một nấc (chửi rồi ép giải luôn) | Chưa đủ giận; cả bài mất lực trả nợ |
| Không có công cụ lao động bị ném đi | Mất sự đối xứng với công cụ của nghề được ấn vào tay |
| Không có con số đám đông | Cú lật không có giá; người xem không biết mình sắp thấy gì đổ vỡ |
| Cô bắt đầu giải, hoặc để lộ tài năng / quá khứ | Tiêu trước phần thưởng của thân bài |
| 🔺 Cô chỉ có một câu xin lỗi bị cắt, không có câu nào đúng sự thật | Cô thành đồ vật trong cảnh của chính mình; người xem thương hại thay vì phẫn nộ |
| 🔺 Kẻ gác cổng chỉ tàn nhẫn, không có niềm tin nào hắn cho là chính đáng | Hình nộm; người xem xem xong yên tâm vì mình không giống hắn |
| 🔺 Bài toán tả bằng lời hứa suông ("chưa ai giải được") | Không có con số để cầm; bức tường không có kích thước |
| 🔺 Đám đông là một khối, không ai do dự | Sự im lặng không tốn gì, nên không đòi lại được ở cuối |
| Không ai giơ máy quay | Chặng lan truyền sau đó không có gốc |
| Câu trớ trêu lấy cô làm chủ ngữ | Lặp title; thứ đáng hứa là phản ứng của đám đông |
| Chép vỏ câu Golden, chỉ đổi danh từ | Rò khuôn; người xem kênh nghe ra ngay. Xem `12-pattern-golden.md` mục 3 |
| Kẻ gác cổng gào lên, dùng từ tục | Cường độ giả; giọng thản nhiên của kẻ có quyền đáng sợ hơn nhiều |
