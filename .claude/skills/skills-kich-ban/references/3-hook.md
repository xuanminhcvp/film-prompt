# 3 — Bước 3: HOOK (phần mở đầu video)

> **File này trả lời:** hook làm nhiệm vụ gì, gồm những nước đi nào, chốt ra sao.
> **Mở khi:** bước 3, sau khi title đã qua cửa QC.
> **Không chứa:** hook dài bao nhiêu từ · chuỗi nước đi cụ thể · CTA đặt ở đâu — đó là các
>   tham số `HOOK.*`, tra ở `../dang/<DẠNG>.md` §1 và §2 ·
>   cách viết câu và quy tắc số (→ `6-giong-van.md`) · cách bịa chi tiết (→ `5-nhan-vat-va-chi-tiet.md`)

## 1. Hook làm đúng ba việc

Không hơn. Mỗi việc thiếu là một lý do khán giả bỏ đi:

1. **Đặt một câu hỏi cụ thể** mà người xem không chịu được nếu không biết đáp án.
2. **Gieo lời hứa** — nói rõ (hoặc gần rõ) thứ mà phần sau sẽ trả.
3. **Không trả lời.** Hook mà giải thích xong thì phần sau còn ai xem.

Hook **không** làm: giới thiệu bối cảnh, dựng nhân vật đầy đủ, nêu chủ đề, nói trước ý nghĩa.

## 2. Độ dài

Tham số `HOOK.do-dai` quy định số từ và số giây đọc tương ứng.

Đếm từ thật, không ước lượng bằng mắt. Quy đổi giây: kịch bản đọc bằng giọng kể ở nhịp **170–200 từ/phút** — đây là nhịp chung mọi dạng, dạng nào cần nhịp khác thì ghi vào chính ô `HOOK.do-dai` của mình.

Thừa từ thì cắt theo thứ tự: tính từ → mệnh đề phụ giải thích → câu chuyển tiếp. **Không cắt dữ kiện cứng** — cắt số liệu là cắt đúng thứ giữ người xem.

## 3. Chuỗi nước đi

Hook không viết bằng cảm hứng. Nó là một chuỗi nước đi có thứ tự, mỗi nước có nhiệm vụ riêng — tham số `HOOK.chuoi-nuoc-di` chỉ định chuỗi nào, chi tiết từng nước ở §2 của hồ sơ dạng.

Phân biệt cho đúng, nếu không hook nào cũng ra một hình:

- **Làm xong đủ việc là [NHIỆM VỤ].** Thiếu một việc thì hook hụt chức năng — khán giả không biết mình đang đợi gì.
- **Thứ tự là [QUAN SÁT].** Thứ tự trong hồ sơ dạng là trình tự kho hay dùng vì nó điều tiết được thông tin. Đổi được — nhưng đổi phải có lý do kể chuyện, không đổi cho khác.
- **Có đúng một đỉnh** là [NHIỆM VỤ]. Hai đỉnh thì không cái nào là đỉnh. Đỉnh nằm ở đâu thì tuỳ truyện.
- **Gộp hai việc vào một câu thường làm việc sau mất trọng lượng** — [QUAN SÁT], không phải cấm.

## 4. CTA giữa hook

Tham số `HOOK.cta` quy định có hay không, và đặt ở đâu.

Khi dạng có CTA, luật chung:

- **Đúng một lần trong toàn bài.** CTA thứ hai làm mất niềm tin nhiều hơn số lượt tương tác nó mang lại.
- **Dính liền sau một câu hỏi trực tiếp gửi khán giả.** CTA đứng một mình là quảng cáo; CTA đứng sau câu hỏi là lời mời ở lại.
- **Dính liền trước mệnh đề mở lời hứa** (`because…`). Người xem phải đọc CTA và lý do ở lại trong cùng một hơi.
- **Không tự khen câu chuyện.** Không "câu chuyện đáng kinh ngạc này". Lời hứa phải là dữ kiện, không phải quảng cáo.

## 5. Câu chốt hook

Tham số `HOOK.cau-chot` quy định câu cuối phải làm gì.

Luật chung: **câu chốt hạ nhiệt, không leo thang.** Sau đỉnh, khán giả cần một chỗ đặt chân. Câu chốt leo cao hơn đỉnh làm hook thành tiếng hét, và tiếng hét thì không ai nghe được câu tiếp theo.

Câu chốt cũng là mối nối: nó phải giới thiệu thứ mà khối đầu tiên của thân truyện sẽ cầm lên nói tiếp.

## 5b. Trước khi chốt hook

Hook là chỗ rập khuôn lộ ra sớm nhất, vì nó ngắn và vì mọi bài trong kho đều mở giống nhau. Hỏi đúng một câu: *câu mở này có riêng cho câu chuyện này không, hay lắp vào bài nào cũng được?* Lắp đâu cũng được nghĩa là chưa có gì. Xem `8-chong-rap-khuon.md` §2.1 và §2.6.

## 6. Kiểm tra

- [ ] Hook nằm trong khoảng của `HOOK.do-dai`. Đếm từ thật.
- [ ] Làm xong đủ các nhiệm vụ mà `HOOK.chuoi-nuoc-di` chỉ định. Kiểm theo **việc đã xong**, không kiểm theo thứ tự.
- [ ] Chỉ có một đỉnh; mọi nước sau đỉnh nhẹ hơn đỉnh.
- [ ] CTA đúng như `HOOK.cta` quy định — đúng số lần, đúng vị trí.
- [ ] Câu chốt làm đúng việc mà `HOOK.cau-chot` quy định, và hạ nhiệt so với đỉnh.
- [ ] Hook **không** trả lời câu hỏi nó vừa đặt.
- [ ] Lời hứa ở hook viết ra được thành một câu — ghi câu đó lại, bước 3 sẽ phải đối chiếu.
- [ ] Không có tính từ tự khen câu chuyện.
- [ ] Hook đã qua **sạch** mọi dòng trên trước khi viết một chữ nào của thân truyện. Không qua thì viết lại, không mang lỗi xuống thân.
- [ ] Câu mở riêng cho câu chuyện này, không lắp vào bài nào cũng được.
