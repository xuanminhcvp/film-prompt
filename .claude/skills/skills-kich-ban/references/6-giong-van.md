# 6 — Giọng văn

> **File này trả lời:** viết câu thế nào, viết số thế nào, phần nào tiếng Anh phần nào tiếng Việt.
> **Mở khi:** bước 3 và bước 4, trong suốt lúc viết.
> **Không chứa:** ngôi kể và mức thoại cho phép (tham số `VAN.ngoi-ke`) · độ dài câu và đoạn
>   (tham số `VAN.nhip-cau`) — cả hai tra ở `../dang/<DẠNG>.md` §1 · chi tiết và số liệu lấy ở đâu (→ `5-nhan-vat-va-chi-tiet.md`)

## 1. Kịch bản này để **đọc lên**, không để đọc bằng mắt

Đây là luật gốc, mọi luật dưới đây chỉ là hệ quả của nó. Trước khi chốt một đoạn, đọc thành tiếng trong đầu. Chỗ nào hụt hơi, chỗ đó sai.

## 2. Câu

- **Câu dài xen câu ngắn.** Một đoạn toàn câu dài là một đoạn không ai nghe hết. Một đoạn toàn câu ngắn nghe như bản tin.
- **Nhịp câu — độ dài trung vị, tỉ lệ câu ngắn, trần câu dài, độ dài đoạn: tham số `VAN.nhip-cau`.** Đây là thứ phân biệt hai dạng story rõ nhất, nên lõi không đặt một con số chung.
- **Câu ngắn là chỗ trọng lượng rơi xuống.** Sau một cụm câu dài, một câu ngắn làm cả cụm nặng thêm. Đặt câu ngắn ngay sau đòn mạnh nhất, đừng đặt cho đều.
- **Một câu một ý.** Câu có hai mệnh đề "và" nối hai ý khác nhau → tách đôi.
- **Được phép mở câu bằng `And`, `But`, `Then`.** Đây là văn nói.
- Ngôi kể và mức thoại: tham số `VAN.ngoi-ke`.

## 3. Số viết bằng chữ

**Trong thân bài và hook, mọi con số viết bằng chữ, không dùng chữ số Ả Rập.**

- `twenty two years old`, không phải `22 years old`
- `thirteen dollars and ten cents an hour`, không phải `$13.10/hr`
- `four fifty on a Friday`, không phải `4:50 PM Friday`
- `sixty two percent`, không phải `62%`

Lý do: kịch bản đi vào miệng người đọc hoặc vào máy đọc. Chữ số ép người đọc tự phiên âm, và máy đọc phiên âm sai.

**Hai ngoại lệ:**
- **Title** được dùng chữ số (`2-title.md` §3), vì title là chữ để đọc bằng mắt.
- **Mã hiệu** giữ nguyên chữ số, vì đọc lên người ta cũng đọc từng ký tự: số hiệu máy bay (`A320`), số hiệu chuyến (`Flight 2136`), số ghế (`4B`), số phòng, số điện thoại khẩn (`911`), giờ trên đồng hồ điện tử (`4:47`). Mã hiệu là **tên riêng của một vật**, không phải số đếm.

Ranh giới: đếm được, cân được, tiêu được → viết chữ. Chỉ dùng để gọi tên một vật → giữ chữ số.

## 4. Cấm

- **Cấm tính từ đánh giá thay cho dữ kiện**: *incredible, devastating, heartbreaking, amazing, shocking*. Nếu sự việc thật sự sốc, dữ kiện đã đủ; nếu không, tính từ cũng không cứu được.
- **Cấm người kể tự khen câu chuyện**: "câu chuyện đáng kinh ngạc này", "điều tiếp theo sẽ khiến bạn...". Khen trước là hứa thay cho dữ kiện; khán giả trừ điểm ngay vì họ biết chuyện hay thì không cần rao.
- **Cấm sáo ngữ**: *little did she know, at the end of the day, tears streamed down her face, in that moment everything changed*. Câu đã nghe nghìn lần thì tai lướt qua — chỗ đáng lẽ nặng nhất lại thành chỗ rỗng nhất.
- **Cấm giải thích cảm xúc nhân vật.** Tả cái họ làm, để khán giả tự gọi tên cảm xúc. "Cô ấy rất sợ" → "Cô ấy đặt bàn tay lên mặt quầy và giữ yên ở đó."
- **Cấm câu hỏi tu từ rải rác.** Mỗi câu hỏi gửi thẳng khán giả là một lần kéo họ ra khỏi truyện; dùng nhiều thì lần cần đến nó nhất cũng hết tác dụng. Chỗ được dùng: `HOOK.cta` và hồ sơ dạng.

## 5. Tiếng Anh ở đâu, tiếng Việt ở đâu

| Phần | Ngôn ngữ |
|---|---|
| Title | **Tiếng Anh** |
| Hook, thân truyện, thoại | **Tiếng Anh** |
| Tên folder dự án | Tiếng Việt không dấu, viết HOA (`7-file-va-ban-giao.md` §1) |
| Tiêu đề mục trong `KICH-BAN.md`, khối Lịch sử sửa, ghi chú | **Tiếng Việt** |
| Mọi câu trả lời cho user trong chat | **Tiếng Việt** |

Không trộn hai ngôn ngữ trong cùng một câu kịch bản. Không chú thích tiếng Việt trong ngoặc giữa dòng tiếng Anh.

## 6. Kiểm tra

- [ ] Đã đọc thành tiếng trong đầu ít nhất một lượt; không chỗ nào hụt hơi.
- [ ] Nhịp câu đạt `VAN.nhip-cau`: độ dài trung vị · tỉ lệ câu ngắn · trần câu dài · độ dài đoạn.
- [ ] Có câu ngắn đặt ngay sau các đòn mạnh, không rải đều cho có.
- [ ] (Toàn bài) Rà mọi chữ số Ả Rập: mỗi cái còn lại phải là mã hiệu theo §3, không được là số đếm/tuổi/tiền/phần trăm.
- [ ] Không tính từ đánh giá nào trong danh sách cấm ở §4.
- [ ] Không sáo ngữ nào trong danh sách cấm ở §4.
- [ ] Không câu nào giải thích thẳng cảm xúc nhân vật.
- [ ] Câu hỏi gửi khán giả chỉ xuất hiện đúng chỗ hồ sơ dạng cho phép.
- [ ] Ngôn ngữ đúng bảng §5; không trộn hai ngôn ngữ trong một câu.
