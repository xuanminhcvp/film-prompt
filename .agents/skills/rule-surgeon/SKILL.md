---
name: rule-surgeon
description: Truy nguyên và sửa tối thiểu rule, skill hoặc checker gây ra một lỗi cụ thể trong hệ prompt phim. Dùng khi người dùng muốn vá, tinh chỉnh hoặc tìm nguyên nhân của hành vi sai; không dùng cho tác vụ tạo nội dung mới thuần túy.
---

# Rule Surgeon

Mục tiêu là làm hệ prompt tốt dần sau mỗi lỗi mà không làm mất những hành vi đúng đã tích lũy. Bạn được phép sửa file thuộc phạm vi đã xác định; IDE sẽ hiển thị granular diff để người dùng duyệt. Chỉ được sửa trên skills-film thôi nhé ( không đụng đến skills-hook)

## Khi nào dùng

Dùng khi người dùng nêu lỗi của prompt, ảnh, video, board, rule hay cách agent làm việc và muốn truy nguyên, sửa hoặc tinh chỉnh. Không dùng để tạo hàng loạt prompt/SF/video mới khi không có mục tiêu sửa hệ luật.

## Nguyên tắc bất biến

- Điều tra kỹ và nghiên cứu toàn diện trước khi sửa. Không vá nông ở file đầu tiên tìm thấy.
- Tìm đủ và rà soát sạch mọi nguồn có khả năng ảnh hưởng trực tiếp lẫn gián tiếp: rule, skill, `references/`, prompt mẫu, checker, schema, caller và dữ liệu liên quan.
- **Sửa triệt để tất cả các nơi liên quan**: Nếu một quy định hoặc hành vi sai xuất hiện ở nhiều file (skill nền, reference, checker, schema), BẮT BUỘC phải research và cập nhật đồng bộ toàn bộ các file đó để đảm bảo tính nhất quán tuyệt đối của hệ thống, không tự giới hạn số lượng file sửa một cách máy móc.
- Ưu tiên sửa hoặc làm rõ rule hiện có. Chỉ thêm rule mới khi đã xác minh không có vị trí hiện hữu hợp lý.
- Luôn cho phép kết luận **không cần sửa rule** nếu lỗi đến từ execution, input, model variance hoặc rule hiện tại đã đủ rõ.
- Sửa chính xác đúng chỗ cần thiết. Không rewrite, reformat, rename, reorder hoặc “cleanup” phần không liên quan.
- Giữ nguyên mọi hành vi đúng cũ trừ khi người dùng yêu cầu thay đổi.

## Phạm vi sửa đổi (Diff scope)

Rà soát rộng nhưng sửa đúng trọng tâm. Khi đã xác định nguyên nhân hoặc quy tắc cần thay đổi, phải cập nhật đầy đủ toàn bộ các file bị ảnh hưởng trong chuỗi (từ tài liệu định hướng, reference chi tiết đến công cụ kiểm tra `kiem-luat.py`). Giải thích rõ các file đã sửa trong phần bàn giao.

## Quy trình bắt buộc

### 1. Chuyển lỗi thành tiêu chí kiểm tra

Tách phản hồi của người dùng thành các yêu cầu cụ thể: hành vi sai, hành vi mong muốn, phạm vi, ngoại lệ và điều không được thay đổi. Giữ checklist này xuyên suốt; không được bỏ sót yêu cầu nào mà không nêu lý do.

Nếu mô tả lỗi hoặc mong muốn của người dùng chưa rõ ràng hay còn mơ hồ, agent được phép chủ động đặt một vài câu hỏi cho người dùng để làm rõ hơn vấn đề và kỳ vọng trước khi điều tra hay chỉnh sửa. Đồng thời, vẫn ưu tiên kết hợp các bằng chứng sẵn có trong workspace (output, diff, board, checker, rule) để thu hẹp phạm vi.

### 2. Lập bản đồ phạm vi trước khi chỉnh

Tìm theo khái niệm và biến thể diễn đạt, không chỉ sao chép câu lỗi. Mở các file trúng trực tiếp và các file định nghĩa quy trình, nguồn dữ liệu hoặc phép kiểm liên quan.

Lập bản đồ phạm vi trong quá trình làm việc. Chỉ tóm tắt file đã xem, nhận định bao phủ và phạm vi dự kiến trước khi sửa nếu điều đó làm rõ một quyết định hoặc người dùng yêu cầu; nếu IDE đã thể hiện scope rõ, không tạo báo cáo trung gian dài.

## Project-specific bindings

Nếu workspace có skill nền cho hệ phim, đọc skill đó trước khi sửa các rule thuộc prompt phim, rồi đọc đúng tài liệu của bước đang xét. Với workspace hiện tại, skill nền là `.claude/skills/skills-film/SKILL.md` và các tài liệu nằm trong `references/`.

Với luật đếm được hoặc có thể kiểm xác định trong workspace hiện tại, kiểm tra `sfboard/kiem-luat.py` và `sfboard/kiem-noi-shot.py`: ưu tiên cải thiện phép kiểm hiện có thay vì chỉ thêm câu cảnh báo vào Markdown.

### 3. Chọn can thiệp nhỏ nhất

Trước khi sửa, chọn đúng một hướng chính:

0. Không sửa gì: rule hiện tại đã đủ, lỗi nằm ở execution, input hoặc model variance.
1. Làm rõ wording của rule hiện có.
2. Bổ sung điều kiện, ràng buộc hoặc ngoại lệ vào rule hiện có.
3. Sửa checker/logic hiện có nếu lỗi có thể kiểm xác định.
4. Tạo rule mới khi không có chỗ hiện hữu hợp lý.

Ưu tiên phương án có phạm vi nhỏ hơn nếu hai phương án cùng giải quyết được lỗi. Không chỉnh nhiều file chỉ để tạo cảm giác “đầy đủ”; mỗi file sửa phải có quan hệ nhân quả trực tiếp với lỗi.

### 4. Sửa trực tiếp, có kỷ luật

Áp dụng bản vá nhỏ nhất vào các file đã nêu. Không trì hoãn thành bản đề xuất thuần văn bản: người dùng đã cho phép sửa để xem granular diff.

Mỗi hunk phải phục vụ một tiêu chí trong checklist. Nếu cần thay đổi vượt phạm vi đã điều tra, dừng, nghiên cứu phần mới rồi mới sửa tiếp.

### 5. Tự kiểm tra tác động

Đọc lại phần đã sửa cùng các rule liên quan để kiểm tra:

- Tất cả tiêu chí người dùng nêu đã được xử lý hoặc được đánh dấu chưa xử lý kèm lý do.
- Không tạo trùng lặp, mâu thuẫn, lỗ hổng hoặc ngoại lệ vô tình.
- Wording mới vẫn áp đúng vào phạm vi intended, không làm yếu luật cũ.
- Nếu có checker/phép kiểm phù hợp, chạy nó và báo kết quả thực tế. Nếu phạm vi chạy hẹp không phủ liên-scene hay toàn dự án, nói rõ phần chưa được phủ.

Không tuyên bố “xong” khi còn requirement chưa kiểm chứng.

## Cách bàn giao

Sau khi sửa, trả lời ngắn gọn theo mẫu:

1. **Đã điều tra:** các file/khái niệm liên quan đã xem.
2. **Kết luận:** nguyên nhân gốc và vì sao chọn chỗ sửa này thay vì các chỗ khác.
3. **Đã sửa:** file và thay đổi tối thiểu tương ứng từng requirement.
4. **Đã kiểm:** phép kiểm/đọc lại đã thực hiện và kết quả.
5. **Chưa chắc hoặc chưa phủ:** mọi rủi ro, giả định, hoặc phạm vi chưa xác minh.
