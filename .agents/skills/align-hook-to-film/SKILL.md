---
name: align-hook-to-film
description: Đối chiếu và tự áp dụng tối đa 15 thay đổi có căn cứ từ skills-film vào skills-hook. Dùng khi người dùng muốn đồng bộ hoặc kế thừa rule Film cho Hook; không dùng để tạo prompt Hook thông thường.
---

# Align Hook to Film

`skills-film` là nguồn chuẩn để tham khảo; `skills-hook` là đích cần tinh chỉnh. Hook không phải bản sao của Film: giới hạn khoảng 2 phút, narration/thoại và mọi quy tắc đặc thù của Hook phải được giữ trừ khi người dùng quyết định khác.

Không tự đồng bộ toàn bộ. Không sửa `skills-film` trong workflow này. Mỗi đợt chỉ áp dụng tối đa 15 thay đổi có quan hệ nhân quả rõ ràng; không tạo thay đổi yếu chỉ để đủ số lượng.

## Project bindings

- Nguồn chuẩn: `.claude/skills/skills-film/`
- Đích: `.claude/skills/skills-hook/`
- File đầu vào bắt buộc: `SKILL.md` của cả hai skill và toàn bộ file trong `references/` của cả hai skill.
- Đơn vị duyệt trong một file reference là **một rule nguyên tử**: một bullet, dòng đánh số, điều kiện, hàng bảng có tính ràng buộc, hoặc tiểu mục quy định. Không dùng cả file hay cả mục lớn làm một đơn vị duyệt.

Trước khi sửa prompt phim, luôn tuân thủ các hướng dẫn workspace và đọc skill nền cùng reference đúng bước. Với khung hình có trẻ em, đọc file an toàn trẻ em của ĐÚNG BÊN đang đọc — hai bên đặt tên khác nhau: Film là `references/KHI-CO-TRE-EM.md`, Hook là `references/LUAT-an-toan.md`.

## Nguyên tắc bất biến

- Đối chiếu theo ý nghĩa và chức năng, không chỉ theo text diff hoặc tên file. Hai bên đang chia file theo hai trục khác hẳn nhau — Film chia theo **khái niệm làm chủ** (mỗi khái niệm đúng một file, tra bảng chủ quyền trong `SKILL.md` của Film), Hook chia theo **bước quy trình** — nên không còn ánh xạ 1-1 giữa tên file hai bên, và số file hai bên cũng không cần bằng nhau.
- Mỗi luật Film đem sang phải hạ xuống đúng MỘT file Hook đang làm chủ khái niệm đó. Chưa file nào làm chủ thì nêu ra để người dùng chọn, không rải cùng một luật vào nhiều file Hook.
- Luật Film hay trỏ chéo sang tên file khác của Film. Bê sang Hook thì mọi dòng trỏ đó phải đổi sang tên file Hook tương ứng hoặc bỏ hẳn — để nguyên là tạo dòng trỏ tới file không tồn tại ở Hook.
- Không mặc định mọi khác biệt ở Hook là lỗi; có thể là quy tắc đặc thù cần giữ.
- Khi người dùng yêu cầu đồng bộ tự động, tự sửa trực tiếp từng rule đủ căn cứ ở `skills-hook`, bằng granular diff nhỏ nhất. Không tiện tay đồng bộ rule tương tự không nằm trong đợt đã chọn.
- Không tự sửa checker dùng chung, schema, `KICH-BAN.md`, media, assets, snapshot, hay skill Film. Nếu chúng có liên quan, nêu chúng là tác động hoặc một quyết định riêng cần người dùng xác nhận.
- Không thay wording chỉ để hay hơn, ngắn hơn hoặc đồng nhất style. Mỗi thay đổi phải phục vụ quyết định đồng bộ/điều chỉnh đã được xác nhận.

## Ưu tiên thay đổi gần đây

Phải hoàn tất inventory toàn bộ rule, nhưng **không** hỏi theo thứ tự file, dòng hay khác biệt cũ. Sắp thứ tự các rule chưa quyết định theo bằng chứng mới nhất có sẵn:

1. Hunk/diff đang mở trong IDE, hoặc file/đoạn người dùng vừa nêu hay vừa sửa trong cuộc trao đổi hiện tại.
2. Phần được đánh dấu là đang làm dở, cần review, hoặc chưa được người dùng duyệt.
3. Dấu hiệu thay đổi gần đây có thể quan sát trong workspace, như thay đổi chưa áp dụng hoặc thời điểm sửa file; đây chỉ là tín hiệu phụ, không tự chứng minh rule đó cần đổi.
4. Các khác biệt lịch sử còn lại.

Không đưa lại một rule mà người dùng đã nói đã tinh chỉnh xong, trừ khi nó bị ảnh hưởng trực tiếp bởi thay đổi gần đây hoặc người dùng yêu cầu xem lại. Nếu không có bằng chứng đáng tin về phần mới, không tự tạo thay đổi từ các khác biệt lịch sử đó.

## Quy trình

### 1. Lập bản đồ khác biệt vừa đủ

Đọc toàn bộ `SKILL.md` của Film và Hook. Sau đó lập inventory toàn bộ file trong hai thư mục `references/`, kể cả file chỉ có ở một bên. Đọc và đối chiếu mọi file reference; có thể xử lý lần lượt từng file để giữ context gọn, nhưng không được bỏ qua file nào.

Tách mỗi file thành rule nguyên tử. Một rule ở Film và rule tương ứng ở Hook là hai đơn vị đối chiếu; một rule không có đối ứng cũng là một đơn vị phải phân loại xem có đủ quan hệ trực tiếp để áp dụng hay cần hoãn. Không gộp nhiều rule chỉ vì chúng nằm cùng mục, có wording giống nhau hoặc cùng dẫn đến một thay đổi file.

Với mỗi đơn vị, phân loại ngắn gọn:

- **Có thể áp dụng:** cùng mục tiêu, đủ rõ để copy hoặc điều chỉnh tối thiểu.
- **Cần phán đoán:** cùng mục tiêu nhưng thiếu căn cứ để chọn một cách điều chỉnh an toàn.
- **Đặc thù Hook:** cần giữ ở Hook.
- **Chỉ có ở Film/Hook:** chỉ áp dụng nếu có quan hệ trực tiếp với mục tiêu Hook.

Không sửa gì ở pha này.

### 2. Chọn tối đa 15 thay đổi

Chọn tối đa 15 rule theo thứ tự ưu tiên thay đổi gần đây. Một rule chỉ được chọn khi:

- luật Film mới hơn hoặc có bằng chứng là nguồn chuẩn hiện hành;
- thay đổi không mâu thuẫn với giới hạn 2 phút, narration/thoại, schema hoặc các đặc thù Hook đã xác định;
- bản vá có thể mô tả chính xác trong một hunk hoặc một thay đổi liên kết không thể tách rời.

Không chọn những rule chỉ khác wording, những khác biệt lịch sử đã được tinh chỉnh ở Hook, hoặc rule đòi hỏi lựa chọn sáng tạo không suy ra được từ tài liệu. Nếu có dưới 15 rule đủ căn cứ, dừng ở số thực tế thay vì lấp quota.

### 3. Áp dụng và kiểm tra

Áp dụng trực tiếp mỗi thay đổi đã chọn vào `skills-hook`. Có thể sửa nhiều file khi các thay đổi là độc lập, nhưng không mở rộng ngoài 15 rule đã chọn.

Đọc lại rule đích, các rule liền kề trực tiếp và reference đang xét để bảo đảm không tạo mâu thuẫn. Nếu có checker/phép kiểm phù hợp với một thay đổi đã áp dụng, chạy nó và báo kết quả thực tế.

### 4. Bàn giao theo đợt

Sau khi xử lý một đợt, báo ngắn:

- Từng rule đã áp dụng và file Hook đã sửa.
- Các đặc thù Hook được giữ lại và lý do.
- Số thay đổi đã áp dụng trên mức tối đa 15.
- Các rule được hoãn vì thiếu căn cứ hoặc cần quyết định sáng tạo.

Không tuyên bố hai skill đã đồng bộ hoàn toàn; chỉ tuyên bố đợt tối đa 15 thay đổi đã hoàn tất.
