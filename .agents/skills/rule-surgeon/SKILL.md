---
name: rule-surgeon
description: Truy nguyên và sửa tối thiểu rule, skill hoặc checker gây ra một lỗi cụ thể trong hệ prompt phim, hook hoặc các skill liên quan theo yêu cầu. Dùng khi người dùng muốn vá, tinh chỉnh hoặc tìm nguyên nhân của hành vi sai; không dùng cho tác vụ tạo nội dung mới thuần túy.
---

# Rule Surgeon

Mục tiêu là làm hệ prompt tốt dần sau mỗi lỗi mà không làm mất những hành vi đúng đã tích lũy. Bạn được phép sửa file thuộc phạm vi đã xác định theo đúng yêu cầu của người dùng (có thể là `skills-film`, `skills-hook` hoặc hệ skill bất kỳ được chỉ định); IDE sẽ hiển thị granular diff để người dùng duyệt.

## Nguyên tắc bất biến

- **Rà hết mọi nơi liên quan, nhưng sửa ở ĐÚNG MỘT nơi làm chủ.** Quy trình này giả định skill đang sửa CÓ bảng chủ quyền — tra nó để biết file nào làm chủ khái niệm, luật sửa ở đó. Skill chưa có bảng ấy thì nằm ngoài giả định: dừng và nói rõ, đừng tự chọn file làm chủ rồi sửa. Ở file không làm chủ, ba dạng sau **không phải bản chép và không được gỡ**:
  - **Dòng trỏ sang file chủ** — *giữ nguyên* khi tên file và tên mục còn đúng (mặc định, ca đông nhất); *thay thế đích* khi file chủ đổi tên, tên mục đổi, hoặc khái niệm chuyển chủ — sửa đích, giữ dòng; *xoá* chỉ khi đích không còn tồn tại **và** khái niệm đã bãi bỏ, hoặc khi file chứa nó không còn dính tới khái niệm đó nữa. Riêng dòng chỉ mục trong `SKILL.md` trỏ xuống `references/` thì **cấm xoá** chừng nào file kia còn sống — file phụ sẽ thành mồ côi.
  - **Ngoại lệ có phạm vi riêng** — file A miễn trừ luật của file B cho trường hợp của riêng A. Đó là luật thật của A.
  - **Ngưỡng đếm được nằm trong checker** — chính nó mới là chỗ chủ; phần chữ chỉ nêu ngưỡng kèm tên phép kiểm.

  **Bản chép thật** — chép lại nguyên luật thay vì trỏ — trong skill đã có bảng chủ quyền thì gần như không còn. Gặp một cái nghĩa là kiến trúc vừa bị phá: báo cho user, chỉ tự gỡ khi chính bản chép đó là nguyên nhân của lỗi đang vá.
- **Diff nhỏ nhất, mỗi thay đổi phải có nhân quả trực tiếp với lỗi.** Không rewrite, reformat, rename, reorder hay "cleanup" phần không liên quan; không chỉnh thêm file chỉ để tạo cảm giác đầy đủ. Mọi hành vi đúng cũ giữ nguyên trừ khi người dùng yêu cầu đổi.
- **Luật đếm được thì sửa ở phép kiểm, không sửa ở văn bản.** Ở workspace này là `sfboard/kiem-luat.py` và `sfboard/kiem-noi-shot.py`: làm sắc phép kiểm hiện có thay vì thêm câu cảnh báo vào Markdown. Phần chữ chỉ nêu ngưỡng kèm tên phép kiểm — sửa một mà quên chỗ kia là để lại hai con số đá nhau.

## Quy trình bắt buộc

### 1. Chuyển lỗi thành tiêu chí kiểm tra

Tách phản hồi của người dùng thành các yêu cầu cụ thể: hành vi sai, hành vi mong muốn, phạm vi, ngoại lệ và điều không được thay đổi. Giữ checklist này xuyên suốt; không được bỏ sót yêu cầu nào mà không nêu lý do.

Nếu mô tả lỗi hoặc mong muốn của người dùng chưa rõ ràng hay còn mơ hồ, agent được phép chủ động đặt một vài câu hỏi cho người dùng để làm rõ hơn vấn đề và kỳ vọng trước khi điều tra hay chỉnh sửa. Đồng thời, vẫn ưu tiên kết hợp các bằng chứng sẵn có trong workspace (output, diff, board, checker, rule) để thu hẹp phạm vi.

### 2. Lập bản đồ phạm vi trước khi chỉnh

Tìm theo khái niệm và biến thể diễn đạt, không chỉ sao chép câu lỗi — không vá nông ở file đầu tiên tìm thấy. Rà mọi nguồn có thể ảnh hưởng trực tiếp lẫn gián tiếp: rule, skill, `references/`, prompt mẫu, checker, schema, caller và dữ liệu liên quan.

Lập bản đồ phạm vi trong quá trình làm việc. Chỉ tóm tắt file đã xem, nhận định bao phủ và phạm vi dự kiến trước khi sửa nếu điều đó làm rõ một quyết định hoặc người dùng yêu cầu; nếu IDE đã thể hiện scope rõ, không tạo báo cáo trung gian dài.

### 3. Chọn can thiệp nhỏ nhất

Trước khi sửa, chọn đúng một hướng chính:

0. Không sửa gì: rule hiện tại đã đủ, lỗi nằm ở execution, input hoặc model variance.
1. Làm rõ wording của rule hiện có.
2. Bổ sung điều kiện, ràng buộc hoặc ngoại lệ vào rule hiện có.
3. Sửa checker/logic hiện có nếu lỗi có thể kiểm xác định.
4. Tạo rule mới khi không có chỗ hiện hữu hợp lý.

Hai phương án cùng giải quyết được lỗi thì lấy phương án hẹp hơn.

### 4. Sửa trực tiếp, có kỷ luật

Áp dụng bản vá nhỏ nhất vào các file đã nêu. Không trì hoãn thành bản đề xuất thuần văn bản: người dùng đã cho phép sửa để xem granular diff.

Mỗi hunk phục vụ đúng một tiêu chí trong checklist. Nếu cần thay đổi vượt phạm vi đã điều tra, dừng, nghiên cứu phần mới rồi mới sửa tiếp.

### 5. Tự kiểm tra tác động

Đọc lại phần đã sửa cùng các rule liền kề:

- Không tạo trùng lặp, mâu thuẫn, lỗ hổng hoặc ngoại lệ vô tình.
- Wording mới vẫn áp đúng phạm vi intended, không làm yếu luật cũ.
- Có phép kiểm phù hợp thì chạy, lấy kết quả thật để báo ở bước bàn giao.

Không tuyên bố "xong" khi còn requirement chưa kiểm chứng.

## Cách bàn giao

1. **Đã điều tra:** các file/khái niệm liên quan đã xem.
2. **Kết luận:** nguyên nhân gốc và vì sao chọn chỗ sửa này thay vì các chỗ khác.
3. **Đã sửa:** file và thay đổi tối thiểu tương ứng từng requirement; requirement nào chưa xử lý thì nêu lý do.
4. **Đã kiểm:** phép kiểm/đọc lại đã chạy và kết quả thực tế.
5. **Chưa chắc hoặc chưa phủ:** rủi ro, giả định, phạm vi chưa xác minh — gồm cả phần phép kiểm chạy hẹp không phủ (liên-scene, toàn dự án).
