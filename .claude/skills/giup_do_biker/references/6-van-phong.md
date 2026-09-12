# Định dạng và văn phong

> Viết lại ngày 2026-09-12 theo `GOLDEN-1.txt` mới. Văn phong của dòng này **không mô tả trọn được bằng luật** — phải nghe. Đọc L2–16 và một mảng dài ở giữa Golden một lần để lấy nhịp, rồi đóng lại. Các luật dưới đây là để soát, không phải để viết theo.

## 1. Định dạng file

```
title: <tiêu đề tiếng Anh>

<đoạn văn>

<đoạn văn>
```

> **Luật của user, thắng Golden.** `GOLDEN-1.txt` viết liền không dòng trống. **Không làm theo chỗ đó.**

- **Mỗi đoạn một dòng, giữa hai đoạn đúng một dòng trống** — kể cả giữa dòng `title:` và đoạn đầu tiên. Không bao giờ hai dòng trống liền nhau.
- **Mỗi lượt thoại là một đoạn riêng.** Câu dẫn hoặc hành động đi kèm lượt thoại đó nằm cùng đoạn; thoại của người khác thì xuống đoạn mới.
- **Đoạn ngắn.** Phần lớn đoạn một tới bốn câu. Khoảnh khắc cần dừng thì cho đứng riêng thành đoạn một câu.
- Không tiêu đề mục, không số cảnh, không nhãn, không gạch đầu dòng.

**Vì sao**: file được người mở ra đọc và dựng, không chỉ đưa vào máy đọc. Dòng trống cho mắt thấy nhịp.

---

## 2. Ngôi kể và thì

Ngôi thứ ba, thì quá khứ. Ngoại lệ: hai dòng lời hứa sau mở màn và các câu treo phóng tới tương lai, dùng **tương lai trong quá khứ** (*would*).

Người kể bám sát người cho, nhưng **được phép rời đi một lát** khi cần cho người xem biết một thứ đang chuyển động ở nơi khác mà nhân vật chính không biết. Những đoạn rời đi đó phải ngắn và phải đóng lại bằng một câu kéo về.

**Người kể được**: nói ra điều nhân vật không biết; nói thẳng rằng nhân vật đoán sai; cài hờ một chi tiết sẽ quay lại; đứng về phía cái nhìn cũ một lần để nó có chỗ bị lật.

**Người kể không**: giảng rằng định kiến là sai; gán tính từ đạo đức cho ai; xúc động thay người xem; tổng kết ý nghĩa của một cảnh vừa xảy ra.

---

## 3. Nhịp câu

Đây là chỗ dòng này khác mọi dòng khác. **Câu mảnh là công cụ chính, không phải gia vị.**

- **Mảnh câu đứng riêng.** Danh từ không có động từ. Tính từ không có chủ ngữ. Dùng để đưa hình ảnh vào theo đúng thứ tự mắt nhìn thấy, và để dựng nhịp gõ ở những chỗ căng.
- **Lặp cấu trúc thành thang.** Cùng một khuôn câu ba, bốn lần liền, đổi một biến mỗi lần. Dùng cho: thang từ chối, liệt kê những gì đôi tay đã làm, liệt kê những gì người ta vẫn đồn.
- **Câu dài chỉ dùng khi tóm lược.** Đoạn dựng lại và vĩ thanh được phép có câu dài — chúng đang lướt qua thời gian. Cảnh thì không.
- **Nhịp ba.** Ba thứ, cái thứ ba nặng nhất hoặc lệch hẳn ra. Dùng tiết chế; hai lần trong một trang là quá.
- **Đừng để hai đoạn liền nhau cùng một hình dạng nhịp.** Một đoạn toàn mảnh câu phải đi liền một đoạn có câu thở dài hơn.
- **Không mệnh đề so sánh trong cảnh.** *Như thể…*, *như một…*, *giống như…* — Golden gần như không dùng. Chúng nghe như văn viết. Trong cảnh, một vật chỉ là chính nó.

### 3b. ⛔ Bốn con số phải tự đo sau khi viết xong

Đây là chỗ chạy thử skill này trượt nặng nhất, nên nó được nâng thành mục riêng. Văn phong của dòng này **không cảm được bằng cảm giác** — người viết luôn thấy văn mình đã đủ ngắn, trong khi thực tế nó dài hơn Golden 50–60%.

| | Golden | Ngưỡng phải đạt | Bài chạy thử (trượt) |
|---|---|---|---|
| Độ dài câu trung bình, toàn bài | 7,1 | **≤ 8,5** | 11,4 |
| Tỉ lệ câu ≤ 5 từ | 51% | **≥ 45%** | 37% |
| Tỉ lệ câu ≥ 20 từ | 6% | **≤ 9%** | 16% |
| Tỉ lệ câu ≥ 25 từ | 2% | **≤ 4%** | 11% |

**Cách đo** (phải bỏ dấu nháy đóng sau dấu chấm, nếu không mọi lượt thoại bị dính vào câu sau và số liệu sai hẳn):

```python
# nhip.py — chay: python3 nhip.py <file>
import re, sys
t = open(sys.argv[1]).read()
t = re.sub(r'^title:[^\n]*\n', '', t)          # bo dong title
t = re.sub(r'([.!?])["\u201d]', r'\1', t)       # bo nhay dong sau dau cham
s = [x for x in re.split(r'(?<=[.!?])\s+', t) if x.strip()]
w = [len(x.split()) for x in s]
print('avg',round(sum(w)/len(w),1),
      '| <=5w',round(100*sum(1 for x in w if x<=5)/len(w)),
      '| >=20w',round(100*sum(1 for x in w if x>=20)/len(w)),
      '| >=25w',round(100*sum(1 for x in w if x>=25)/len(w)))
```

### 3c. Nhịp theo từng chặng — chỗ này mới là chỗ chẩn đoán

Con số toàn bài che mất vấn đề. Đo **từng chặng riêng**. Golden có một hình dạng rất rõ, và nó ngược với bản năng của người viết:

| Chặng | Golden avg | Golden ≤5 từ | Trần cho bài mới |
|---|---|---|---|
| Mở màn | **4,6** | 74% | ≤ 5,5 |
| Đời thường | 7,7 | 47% | ≤ 9 |
| **Cơn cớ** | **10,9** | 33% | ≤ 12 |
| Thang từ chối | 7,8 | 53% | ≤ 9 |
| **Cánh cửa mở** | **6,2** | 57% | **≤ 7,5** |
| Hạt giống | 6,3 | 54% | ≤ 7,5 |
| **Sự đền đáp** | **6,4** | 52% | **≤ 7,5** |
| Dựng lại + món quà | 7,0 | 55% | ≤ 8,5 |
| **Vĩ thanh** | **12,1** | 29% | ≤ 13 |
| Vòng khép | 6,8 | 46% | ≤ 8 |

**Luật rút ra — và đây là luật quan trọng nhất của cả file này:**

> **Đúng hai chặng được phép viết câu dài: cơn cớ và vĩ thanh.** Cả hai đều là giải trình, không phải cảnh — một bên giải thích cơ chế, một bên lướt qua nhiều tháng. Mọi chặng còn lại là **cảnh**, và cảnh chạy ở 6–8 từ một câu.

> **Chặng càng nặng cảm xúc thì câu càng phải ngắn.** Hai chặng nặng nhất bài — cánh cửa mở và sự đền đáp — là hai chặng có câu **ngắn nhất** sau mở màn. Bản năng của người viết thì ngược lại: xúc động thì câu dài ra. Ở thể loại này, câu dài ra đúng lúc đó là hỏng, vì người xem đang cần nhịp gõ chứ không cần văn.

**Lần chạy thử trượt đúng ở đây**: cánh cửa mở đo được 13,9 — hơn gấp đôi Golden, ở chính chặng dài nhất và quan trọng nhất bài — trong khi toàn bài chỉ 11,4. Nếu chỉ nhìn số toàn bài thì không thấy.

**Trượt thì sửa thế nào**: vào đúng chặng trượt, lấy mọi câu trên 20 từ và cắt làm hai hoặc ba. Gần như câu nào cũng cắt được ở một dấu phẩy mà không mất gì. Trong cảnh, cắt luôn mọi mệnh đề bắt đầu bằng *và*, *trong khi*, *bởi vì* — cho chúng đứng riêng thành câu.

**Vì sao đây là ngưỡng chứ không phải tham khảo**: thể loại này được đọc thành tiếng bởi một giọng duy nhất, không có hình. Nhịp gõ là thứ duy nhất thay cho dựng phim. Văn dài hơn không sai ngữ pháp — nó chỉ làm video nghe như một người đang đọc bài, thay vì một người đang kể.

---

## 4. Sổ con số

Dòng này đo mọi thứ. **Ưu tiên con số hơn tính từ ở mọi chỗ có thể đếm được.**

Đếm: tuổi, số năm làm một việc, số tiền còn lại, số khách còn lại, số cửa đã đóng, giờ phút của một tin nhắn, số người quay lại, số tuần sửa chữa, giá phải trả, khoảng cách.

- **Con số phải nhỏ đến mức nhói hoặc lớn đến mức vô lý.** Con số tầm tầm không có việc gì làm trong bài này.
- **Con số được nhắc lại.** Một con số đã đặt ở chặng 2 phải trở lại ở chặng 8 để người xem tự làm phép trừ.
- **Giờ giấc chính xác thay cho "một lúc sau".** "Mười một giờ bốn mươi sáu tối" có mùi thật; "khuya hôm đó" thì không.
- **Số tiền lẻ, không tròn.** Tiền tròn nghe như ví dụ.

---

## 5. Chỉ tiếng Anh Mỹ trong file

Không câu tiếng gốc, không phiên âm, không kính ngữ nước ngoài, không chữ nào không phải tiếng Anh.

Nếu một nhân vật nói bằng thứ tiếng khác, viết câu đó **bằng tiếng Anh**, và gọi tên thứ tiếng **trong câu dẫn của chính câu đó** (*she said in Spanish*), mỗi câu một lần — không phải chỉ một lần rồi để các câu sau tự hiểu.

**Vì sao**: file được đọc thành một giọng duy nhất cho khán giả Mỹ. Chữ nước ngoài làm họ mất đúng câu cần hiểu nhất. Và đội làm video cần biết câu nào phải lồng tiếng.

Giọng vùng miền thì được, và nên có: rút gọn, cách gọi nhau, cách xưng hô của thế hệ. Nhưng viết bằng chính tả tiếng Anh đọc được, đừng bóp méo chữ tới mức khó đọc.

---

## 5b. Dựng không gian của cảnh

- **Ai ở đâu phải rõ trước khi ai nói.** Mỗi cảnh chia được thành hai hoặc ba vùng (trong / ngoài / ngưỡng cửa; bếp / quầy / phòng sau), và mỗi người phải ở rõ một vùng.
- **Số người phải hợp với không gian.** Ai không cần có mặt thì cho họ có mặt từ xa — điện thoại, tin nhắn, tiếng vọng từ phòng khác — hoặc bỏ.
- **Người di chuyển giữa hai vùng là cách bài đánh dấu một quyết định.** Dùng nó thay cho câu tường thuật nội tâm.
- Không ai có mặt mà không có việc.

---

## 6. Chi tiết thay cho tính từ

**Cấm tuyệt đối các tính từ đạo đức và cảm xúc gán thẳng cho nhân vật**: tốt bụng, hào phóng, đáng sợ, cứng rắn, tử tế, dũng cảm, tuyệt vọng.

Thay bằng:
- **Việc đôi tay làm.** Cảm xúc của dòng này sống trong bàn tay: gấp một cái áo theo một cách nhất định, đặt tay lên một chỗ, đẩy một thứ trở lại qua mặt bàn, đặt một thứ xuống giữa chừng vì tay run.
- **Một thứ được làm dù không ai yêu cầu.**
- **Một thứ không được hỏi.** Cái người ta không hỏi nói nhiều hơn cái người ta nói.
- **Kích thước đặt cạnh hành vi.** Một người rất to làm một việc rất nhỏ, hoặc ngồi xuống như một đứa trẻ. Đây là hình ảnh trung tâm của dòng này — dùng, nhưng đừng dùng quá hai lần.

---

## 7. Thoại

- **Ngắn.** Người kiệt sức, người già, người làm việc bằng tay đều nói ngắn. Lượt thoại dài quá bốn dòng phải có lý do.
- **Người ta không nói ra điều mình đang nghĩ.** Họ nói về thời tiết, về đồ ăn, về việc phải làm. Cảnh nặng nhất trong bài thường là cảnh có ít chữ nhất.
- **Cắt ngang.** Dùng gạch ngang dài để một người bị chặn giữa câu. Đây là dấu hiệu của dòng này ở mọi chỗ có quyết định.
- **Xưng hô mang cả quan hệ.** Cách hai người gọi nhau — và **cái lúc cách gọi đó đổi** — là một công cụ cốt truyện.
- **Câu chủ đề phải tầm thường.** Câu mang ý nghĩa lớn nhất của bài phải là câu nghe bình thường nhất. Nếu nó nghe hay, viết lại cho dở đi.
- **Không ai diễn giải cảnh vừa xảy ra.**

---

## 8. Những thứ làm hỏng giọng

| Thứ | Vì sao |
|---|---|
| Người kể xúc động ("thật cảm động", "không ai cầm được nước mắt") | Cướp việc của người xem |
| Tính từ đạo đức gán cho nhân vật | Bảo người xem nghĩ gì |
| Một nhân vật tổng kết bài học | Giảng bài |
| Ẩn dụ văn chương, câu bay bổng | Sai giọng; dòng này viết bằng đồ vật |
| Câu dài nhiều mệnh đề trong cảnh | Giết nhịp |
| Con số tròn, giờ giấc mơ hồ | Mất mùi thật |
| Ai cũng khóc | Nước mắt chỉ đắt khi hiếm — tối đa ba lần trong cả bài, mỗi lần một người khác |
| Nhóm bị xa lánh được viết hoàn hảo | Thành tuyên truyền; họ phải thô, ồn, vụng |
| Người cho được viết không tì vết | Mất động cơ 3 |
| Lặp lại một câu hay của chính mình để nhấn | Lộ ý đồ |
