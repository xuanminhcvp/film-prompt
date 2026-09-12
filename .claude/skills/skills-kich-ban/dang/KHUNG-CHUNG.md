# Định mức Khung chung

**DÙNG KHI:** một người bị xã hội coi là thấp kém bị khinh, bị thách, bị phớt lờ hoặc bị thử — và họ nắm một thứ mà người đối diện không hề biết. Video dài, một giọng kể, không chia scene.

**NGUỒN:** đo trên 242 title và 117 kịch bản đầy đủ của kho tham chiếu *kho tham chiếu* (2026-09-04).

> Số đo dưới đây là số thật, nhưng **số thật không tự động là luật**. Mỗi ô mang một nhãn:
> **[BẮT BUỘC]** = yêu cầu có thật của kênh, cứng · **[MỤC TIÊU]** = việc phải làm được, tự do về cách · **[THAM KHẢO]** = kho hay làm thế, không phải luật.
> Đối xử với một ô [THAM KHẢO] như thể nó là [BẮT BUỘC] chính là cách biến kịch bản mới thành bản sao của kho cũ.

**ĐÂY LÀ KHUNG CHUNG.** Tám dạng bài ở `bai/` dùng chung mọi định mức và mọi nhiệm vụ trong file này. Cái khác nhau giữa chúng — *cái gì khởi động* và *cú lật là gì* — nằm ở `bai/<DẠNG-BÀI>.md`. Bước 1 chốt **một** dạng bài; file này luôn được nạp kèm. Cơ chế ghi đè ở §8.

## 1. Định mức (12 ô tham số)

| Mã | Nhãn | Giá trị |
|---|---|---|
| `TITLE.cong-thuc` | [THAM KHẢO] | Tám kiểu vế trước × bốn kiểu vế sau, bảng ở §2. Dạng bài ghi đè bằng cách chỉ định kiểu nào hợp với nó |
| `TITLE.tran` | [BẮT BUỘC] + [THAM KHẢO] | **90–100 ký tự** · **đúng 1 dấu `—`**. Trần trên 100 là [BẮT BUỘC] — chỗ nền tảng cắt chữ, nên đừng viết sát 100 vì phần bị cắt luôn là vế lật. Sàn 90 là [THAM KHẢO]: kho có trung vị 95, và dưới 90 thì không đủ chỗ cho cả hai đầu sắc lẫn vế sau có quy mô |
| `HOOK.do-dai` | [BẮT BUỘC] | **115–175 từ**. Đây là ngân sách chú ý: hook dài hơn thì người xem bỏ trước khi được hứa điều gì |
| `HOOK.chuoi-nuoc-di` | [THAM KHẢO] | Tám nhiệm vụ ở §3. Nhiệm vụ bắt buộc đạt; **thứ tự là mặc định để bắt đầu, không phải đường ray** |
| `HOOK.cta` | [THAM KHẢO] | Tuỳ chọn, tối đa 1 lần. Nhiều bài trong kho không có |
| `HOOK.cau-chot` | [MỤC TIÊU] | Đưa khán giả về mốc thời gian trước sự kiện, và trao cho nhiệm vụ mở đầu thân một thứ để cầm lên nói tiếp |
| `THAN.khung-muc` | [MỤC TIÊU] + [THAM KHẢO] | Bảy nhiệm vụ ở §4 là [MỤC TIÊU]; **thứ tự và tỉ lệ % là [THAM KHẢO]** |
| `THAN.do-dai` | [BẮT BUỘC] | **7.300–8.050 từ** (trung vị 7.560), tính cả hook — độ dài video kênh cần |
| `THAN.cta-cuoi` | [BẮT BUỘC] | Bắt buộc, ở 2% cuối: (1) like/share · (2) một câu hỏi mời khán giả kể chuyện của họ · (3) subscribe |
| `VAN.ngoi-ke` | [MỤC TIÊU] | Ngôi thứ ba, biết nhiều hơn khán giả. Thoại trong ngoặc kép, người nói lộ ra qua câu tả liền kề chứ không qua nhãn tên |
| `VAN.nhip-cau` | [BẮT BUỘC] + [THAM KHẢO] | Trần câu **40 từ** là [BẮT BUỘC] — bài này để đọc lên, câu dài làm người đọc hụt hơi. Câu trung vị **6 từ** và **~40–50% câu ≤ 6 từ** là [THAM KHẢO] |
| `CHI-TIET.mat-do` | [MỤC TIÊU] | Người và tổ chức phải cụ thể tới mức khán giả tin được. Kho làm điều đó bằng tên đầy đủ + tuổi + nghề ngay lần nhắc đầu — đó là **một** cách, không phải cách duy nhất |

## 2. Kiểu title — hai trục độc lập

Vế trước là **tội**. Vế sau là **giá phải trả**. Việc vế sau phải lật chứ không nối tiếp là [MỤC TIÊU]; chọn kiểu nào ở mỗi vế là [THAM KHẢO].

**Title bán KHOẢNG CÁCH, không bán sự kiện** — [MỤC TIÊU]. Vế trước phải có hai người và **cả hai đầu đều sắc**: một đầu là quyền lực nêu đích danh, đầu kia là địa vị thấp nêu cụ thể. Đo trên kho: **54%** nêu địa vị thấp cụ thể (maid's son · janitor's daughter · homeless · little · poor) · **34%** dùng danh xưng quyền lực cực đoan (billionaire · judge · CEO · senator · mafia boss) · **38%** có tiền hoặc con số quy mô — cả ba là [THAM KHẢO].

**Phép thử:** che vế sau đi. Hai danh từ chỉ người còn lại có nằm ở hai đầu xa nhau của thang xã hội không? Một đầu mờ → cú lật không có độ cao để rơi. `Bailiff` đối `a Black Woman` là hai đầu cùng mờ: không biết cô nghèo hay giàu, làm gì, bao tuổi — nên không có gì để thương, và cú ngã không thành cảnh tượng.

**Cụm sở hữu là cách nén rẻ nhất**: `Black janitor's daughter` gói cả một giai tầng vào ba chữ mà **không** đóng cú lật, vì nghề của cha không nói gì về con.

### 2.1 Tám kiểu vế trước · [THAM KHẢO]

Tỉ trọng đo trên 242 title của kho, phân loại bằng dấu hiệu bề mặt nên sai số vài phần trăm.

| Kiểu | Vế trước làm gì | ~% | Hay đi với dạng bài |
|---|---|---|---|
| `T1` **Đòn** | Người có quyền ra tay với người bị coi thường: gọi tên xấu, ném, xé, đuổi, còng, tát | 56 | `REVEAL` · `FIGHT` · `INVESTIGATION` |
| `T2` **Việc tốt của người yếu** | Người không dư dả cho đi hoặc cứu ai đó | 11 | `KINDNESS` |
| `T3` **Bế tắc** | Không ai giải được: chuyên gia bó tay, tiền đã đổ, thời hạn sắp hết | 8 | `CHALLENGE` · `WARNING` |
| `T4` **Thoại mở** | Mở thẳng bằng một câu trong ngoặc kép — của kẻ ra đòn hoặc của chính nhân vật chính | 9 | mọi dạng |
| `T5` **Đám đông cười** | Chủ ngữ là số đông: cả phòng, hội đồng, học viên, các nhà khoa học | 5 | `CHALLENGE` · `FIGHT` |
| `T6` **Giả dạng / phép thử** | Người có quyền cải trang, giả vờ, hoặc dàn dựng một phép thử | 5 | `TEST` |
| `T7` **Nguy cấp** | Có người đang sắp chết hoặc đang bị hại ngay lúc này | 4 | `WARNING` · `KINDNESS` |
| `T8` **Cô độc của người có quyền** | Người giàu đang một mình, bị bỏ rơi, hoặc thiếu thứ tiền không mua được | 2 | `KINDNESS` · `REUNION` |

`T3` là kiểu **dễ hỏng nhất**: bế tắc kỹ thuật không có nạn nhân. Dùng nó thì phải kéo một người vào vế trước hoặc vế sau, nếu không title thành bản tin.

### 2.2 Bốn kiểu vế sau · [THAM KHẢO]

| Kiểu | Khuôn | Cú lật hợp với kiểu này |
|---|---|---|
| `V1` **Không hề biết** | `Unaware…` · `Didn't Know…` · `Not Knowing…` · `Turns Out…` | Danh tính |
| `V2` **Cho đến khi** | `Until <ai> <làm gì>` | Năng lực |
| `V3` **Rồi thì** | `Then…` · `Minutes Later…` · `Next Morning…` | Hậu quả tức thì |
| `V4` **Chuyện gì xảy ra** | `What She/He Did Next…` · `Her Answer…` | Giấu hoàn toàn |

**Phản ứng cơ thể của kẻ thua là đòn mạnh sẵn có** — 21% kho dùng ở vế sau (*Went Pale · Froze · Knees Buckled · Nearly Fainted · Speechless*). Nó cho khán giả thấy cú lật đã hạ cánh xuống một con người, không dừng ở ý tưởng.

### 2.3 Ghép hai vế

Hai trục **độc lập**: tám kiểu vế trước nhân bốn kiểu vế sau. Cột "hay đi với" ở §2.1 là thói quen của kho, không phải ràng buộc — một `T3` ghép `V1` hay `T2` ghép `V4` đều dùng được nếu truyện đỡ được.

Khi dựng năm phương án ở bước 2, **đổi kiểu vế trước chứ đừng chỉ đổi cách nói**. Năm phương án cùng `T1` là năm cách viết một câu; `T1`, `T3`, `T4`, `T5`, `T7` mới là năm hướng vào truyện khác nhau.

Trong kho, ~26% title đặt một câu thoại ở vế trước. Riêng về yếu tố sắc tộc: **theo mặc định sản xuất của dự án, nhân vật chính luôn là người da đen, do đó từ "Black" BẮT BUỘC phải xuất hiện ở vế trước của mọi Title**.

## 3. Hook — tám nhiệm vụ

Hook phải làm xong tám việc trong ngân sách 115–175 từ. **Việc là bắt buộc; thứ tự dưới đây là trình tự kho hay dùng, đổi được khi truyện đòi.**

| # | Nhiệm vụ | Phải đạt được gì |
|---|---|---|
| 1 | **Ném vào giữa sự việc** | Câu đầu là thoại hoặc hành động đang diễn ra — **và trong đó phải có hai người: một ra đòn, một nhận**. Không dẫn dắt, không giới thiệu, không mở bằng một sự vật đang trục trặc. Kho: 64% mở bằng thoại, 64% có người ngay câu đầu. Dạng bài quyết định *loại* đòn |
| 2 | **Dựng kẻ đối diện** | Người gây áp lực hiện ra qua hành vi quan sát được, không qua nhãn dán đạo đức |
| 3 | **Leo thang** | Áp lực tăng thêm một nấc, đủ để khán giả chọn phe |
| 4 | **Cho thấy sự cô độc** | **Nói rõ có bao nhiêu người chứng kiến** rồi cho thấy không ai can thiệp: cười, quay phim, nhìn đi chỗ khác, đi ngang. Kho: 82% hook có đám đông, thường kèm con số. Cô độc giữa bốn người trong phòng họp thì chưa phải cô độc — nhục cần khán giả |
| 5 | **Nhân vật chính đáp lại, ngắn và giữ phẩm giá** | Hai đại lượng khác nhau, đừng nhập làm một: **lượng thoại của cả hook** do `VAN.ngoi-ke` quyết định, còn **phần của nhân vật chính** thì luôn nhỏ — họ nói đúng một câu, bình tĩnh, nêu một sự thật đơn giản (*tôi đã trả tiền chỗ này* · *tên tôi có trong danh sách* · *tôi không đi đâu cả*). Đây **không** phải trả đũa: họ chưa dùng đến thứ mình nắm. Im hoàn toàn thì nhân vật thành đồ vật, khán giả không có gì để yêu |
| 6 | **Mở khoảng trống** | Người kể cho biết kẻ đối diện đang không biết một điều — **mà không nói điều đó là gì** |
| 7 | **Gieo lời hứa** | Nói rõ đủ để khán giả biết mình đang đợi cái gì, và trong bao lâu |
| 8 | **Bắc cầu về quá khứ** | Chuyển khán giả về trước sự kiện, trao cho thân truyện một thứ để cầm lên |

Nhiệm vụ 6–7 là chỗ tò mò lên đỉnh. Hook **không được để lộ nhân vật chính nắm gì** — vi phạm là mất luôn lý do xem tiếp, nên đây là [MỤC TIÊU] chứ không phải sở thích.

## 4. Thân truyện — bảy giai đoạn

Bảng này định nghĩa **chức năng** của bảy giai đoạn. **Nội dung cụ thể của từng giai đoạn nằm ở `bai/<DẠNG-BÀI>.md` §3** — mỗi dạng bài kể những cảnh khác nhau trong cùng một giai đoạn.

Tỉ lệ % là [THAM KHẢO] — biên độ kho, dùng làm điểm xuất phát chứ không phải hạn mức.

**Biên độ từng giai đoạn KHÔNG cộng ra tổng — cộng cận dưới của cả bảy ô là hụt
~1.000 từ so với sàn `THAN.do-dai`.** Nên trước khi viết chữ đầu tiên của giai đoạn 1,
phải **chốt sẵn bảy con số cụ thể cộng đúng vào 7.300–8.050 (đã trừ hook) và ghi
chúng ra**. Biên độ chỉ dùng để chọn con số, không dùng để viết tới đâu hay tới đó. Với bài 7.500 từ, mỗi 10% là khoảng 750 từ.

| # | Giai đoạn | Chức năng | ~% |
|---|---|---|---|
| 1 | **Nhân vật chính là ai** | Đời thường hoá họ, và gài dấu vết của thứ họ đang nắm mà không nhấn. Dạng bài quyết định gài gì | 10–18 |
| 2 | **Cái giá đã trả** | Cho khán giả lý do đứng về phía họ, bằng dữ kiện chứ không bằng thương cảm | 10–15 |
| 3 | **Vì sao hôm nay** | Đưa hai bên vào cùng một chỗ bằng một lý do đời thường, không bằng trùng hợp | 8–12 |
| 4 | **Sự việc, bản đầy đủ** | Kể lại cảnh ở hook chậm và trọn vẹn, giờ đã có đủ ngữ cảnh để nó nặng hơn lần đầu | 12–18 |
| 5 | **Mất mát đến trước** | Nhân vật chính chịu thiệt thật. Không có nhiệm vụ này thì cú lật nhẹ bẫng — [MỤC TIÊU] | 10–15 |
| 6 | **Cú lật** | Dạng bài quyết định nội dung. Luật chung: **kể từng bước bằng hành động cụ thể, không tóm tắt bằng tính từ** | 18–25 |
| 7 | **Hệ quả và kết** | Hậu quả lan ra ngoài hai người, một cảnh đời thường khép lại, rồi CTA | 12–18 |

**Bảy giai đoạn này chung cho cả tám dạng bài; nội dung của chúng thì không.** Mỗi hồ sơ dạng bài §3 có bản đồ riêng: giai đoạn ấy kể cảnh gì, kết ở đâu để bắc sang giai đoạn sau.

## 5. Dấu nhận dạng · [THAM KHẢO]

Đây là **mô tả kho tham chiếu**, dùng để nhận ra một bài thuộc dạng này — **không phải danh sách phải làm đủ**:

- Câu đầu thường là thoại, không phải lời dẫn.
- Câu rất ngắn; gần một nửa số câu không quá sáu từ.
- Đám đông có mặt và im lặng — nhân vật thứ ba của hầu hết các bài.
- Con số quy mô xuất hiện sớm và viết bằng chữ.
- Kết quay về một cảnh nhỏ đời thường trước khi tới CTA.

Một bài không có đủ các dấu này vẫn có thể đúng dạng. Một bài có đủ mà nhạt thì vẫn nhạt.

## 6. Cấm — kèm lý do hỏng gì

Cấm không nêu được **hỏng gì** thì là sở thích, không phải luật.

| Cấm |
|---|
| Lộ nhân vật chính nắm gì trong hook |
| Câu mở tả một sự vật trục trặc thay vì một người bị làm gì đó |
| Nhân vật chính im hoàn toàn suốt hook |
| Bỏ nhiệm vụ 5 (mất mát đến trước) |
| Tóm tắt cú lật bằng tính từ |
| Kết ở phần thưởng cá nhân |
| Bỏ CTA cuối |
| Chia `## SCENE`, dùng thẻ `[BEAT]` |

## 7. Kiểm tra

- [ ] Title trong 90–100 ký tự, đúng 1 dấu `—`, và vế sau **lật** chứ không nối tiếp.
- [ ] Vế trước có **người bị tác động**, không chỉ có sự việc hay đồ vật.
- [ ] Hook 115–175 từ (chạy `scripts/kiem.py`).
- [ ] Lượng thoại của hook đúng mức đã chốt ở `VAN.ngoi-ke` — đếm số từ nằm trong ngoặc kép chia tổng số từ. Lệch mức thì viết lại, không phải ghi chú rồi cho qua.
- [ ] Hook làm xong đủ tám nhiệm vụ ở §3 — kiểm theo **nhiệm vụ**, không kiểm theo thứ tự.
- [ ] Hook không để lộ nhân vật chính nắm gì.
- [ ] Câu đầu có **hai người** — một ra đòn, một nhận — chứ không phải một sự vật đang trục trặc.
- [ ] Nhân vật chính xuất hiện trong ba câu đầu, không phải ở đoạn thứ tư.
- [ ] Có **đám đông chứng kiến**, nói rõ quy mô, và không ai can thiệp.
- [ ] Nhân vật chính **đáp lại đúng một câu ngắn, giữ phẩm giá** — không im hoàn toàn, cũng không trả đũa.
- [ ] Đã chốt bảy con số ngân sách TRƯỚC khi viết, và chúng cộng đúng vào `THAN.do-dai`.
- [ ] Toàn bài 7.300–8.050 từ (chạy `scripts/kiem.py`).
- [ ] Bảy nhiệm vụ ở §4 đều xong; nhiệm vụ 5 nằm trước nhiệm vụ 6.
- [ ] Cú lật kể từng bước bằng hành động, không tóm tắt.
- [ ] Không câu nào quá 40 từ (trừ tối đa 2 câu toàn bài).
- [ ] CTA cuối đủ ba phần.
- [ ] Kết có hệ quả lan ra ngoài hai người **và** một cảnh đời thường trước CTA.

## 8. Tám dạng bài — cơ chế ghi đè

Một hồ sơ dạng bài **chỉ được ghi đè những thứ dưới đây** — mọi nhiệm vụ không được nhắc tên thì làm đúng như file này, và dạng bài **cấm chép lại** chúng:

| Ghi đè | Ở mục nào của dạng bài |
|---|---|
| `TITLE.cong-thuc` — vế trước dấu `—` | §1 |
| Nhiệm vụ 1 của hook — cái gì khởi động | §2 |
| **Bản đồ đầy đủ bảy giai đoạn** — kể cảnh gì, kết ở đâu, bao nhiêu từ | §3 |
| Trục biến thiên — để hai bài cùng dạng không thành bản sao | §4 |
| Cấm riêng (kèm lý do) + checklist riêng | §5–§6 |

Mọi thứ khác dạng bài không đụng vào và không chép lại. Một kiểu chuyện đòi đổi định mức (độ dài, nhịp câu, CTA) thì nó không thuộc khung này — dựng một khung chung mới theo `../references/1-chon-dang.md` §4.

### Bảng tám dạng bài

Tỉ trọng là ước lượng trên 117 kịch bản đã đọc. **Tỉ trọng mô tả kho, không phải chỉ tiêu phải theo** — một dạng bài hiếm không phải là lựa chọn tệ.

| Dạng bài | Khởi động | Cú lật | Tỉ trọng kho |
|---|---|---|---|
| [`REVEAL`](bai/REVEAL.md) | Sỉ nhục công khai | Nhân vật chính **là ai** | ~35% |
| [`CHALLENGE`](bai/CHALLENGE.md) | Lời thách có treo giải, hoặc bài toán không ai giải được | Họ **làm được** | ~25% |
| [`KINDNESS`](bai/KINDNESS.md) | Tiếng cầu cứu, hoặc người lạ đang gặp nạn | Người được giúp hoá ra là ai, và phần thưởng đến sau | ~15% |
| [`FIGHT`](bai/FIGHT.md) | Lời thách đấu | Thắng nhanh bằng kỹ thuật | ~8% |
| [`WARNING`](bai/WARNING.md) | Một câu cảnh báo bị phớt lờ | Tai hoạ xảy ra đúng như cảnh báo | ~6% |
| [`TEST`](bai/TEST.md) | Người giàu dàn dựng một phép thử | Qua bài thử mà không biết mình bị thử | ~5% |
| [`REUNION`](bai/REUNION.md) | Một vật gợi quá khứ | Huyết thống hoặc người thất lạc | ~4% |
| [`INVESTIGATION`](bai/INVESTIGATION.md) | Một con số sai trong hồ sơ | Chứng cứ phơi bày cả hệ thống | ~2% |

Không dạng bài nào khớp → dừng, hỏi user. Đừng ép câu chuyện vào dạng gần nhất.
