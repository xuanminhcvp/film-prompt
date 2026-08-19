# Bước 3 — Prompt SF

> **Nguồn sự thật duy nhất** cho khung hình, bám kịch bản và cấu trúc dữ liệu của SF.

## Mục lục
- [Nguyên lý bố cục cốt lõi](#nguyên-lý-bố-cục-cốt-lõi)
- [Quy tắc Prompt SF Thường](#quy-tắc-prompt-sf-thường)
- [Thiết kế một khung hình](#thiết-kế-một-khung-hình)
- [Checklist bắt buộc](#checklist-bắt-buộc)
- [Quy tắc SF trong dữ liệu](#quy-tắc-sf-trong-dữ-liệu)

---

## Nguyên lý bố cục cốt lõi
1. **Bản đồ vị trí tường minh**: Mô tả vị trí bằng mốc cụ thể (% khung, landmark), chỉ rõ ai thuộc nhóm nào, tách nhóm dễ nhầm bằng khoảng trống rõ ràng.
2. **Liệt kê ĐẦY ĐỦ chữ**: Mọi chữ muốn hiện trên ảnh (bảng tên, biển số, logo) phải được liệt kê rõ, kèm đánh vần chính xác.
3. **Ba loại vật thể**:
   - **(a) Thuộc bối cảnh**: Bắt buộc có, tả khái quát, lùi ra nền (giấy tờ, sách vở...).
   - **(b) Đạo cụ tham gia hành động**: Đang cầm/đưa/nhìn. Tả cụ thể, tách bạch khỏi nhóm nền. **Đính ảnh nếu có**.
   - **(c) Đạo cụ minh họa nội tâm**: **THỪA, LOẠI BỎ.** (Vd: khung ảnh gia đình, bằng khen). Dùng ngôn ngữ cơ thể thay thế.
4. **Xác định CAST & Lọc Tham chiếu (REF Filtering) theo góc máy**: Lấy từ bản đồ không gian toàn cảnh -> Đặt máy quay -> Xác định nón quan sát.
   - **Mô tả văn bản**: Những người có thoại hoặc nằm trong nón quan sát thì BẮT BUỘC phải xuất hiện bằng chữ (không được tàng hình).
   - **Lọc REF (Chống lỗi chật khung)**: Mỗi SF chỉ được phép mang thẻ tham chiếu (REF keys) của những nhân vật **THỰC SỰ CÓ MẶT** trong nón quan sát.
   - **Lệnh Cắt Tham Chiếu**: BẮT BUỘC phải chỉ đích danh việc gạt bỏ (không tham chiếu) những người thừa ra khỏi lô REF của góc máy đó. Ví dụ: Scene có A, B, C; nhưng nếu SF là góc cận (CU) chỉ có A, thì phải chốt rõ "CHỈ tham chiếu A, KHÔNG tham chiếu B và C".

## Quy tắc Prompt SF Thường
- **Cấu trúc Prompt Ảnh (7 phần)**: MỌI prompt ảnh (cả thẻ địa điểm và SF thường) chỉ còn đúng 7 phần:
  1. **Máy quay** (bằng thông số đo cụ thể)
  2. **Trạng thái không gian của cụm** (nhưng chỉ tả những gì lọt vào nón quan sát của góc máy)
  3. **Ai đang làm gì**
  4. **Bàn tay** (Tuỳ chọn: chỉ tả nếu có hành động cầm nắm cụ thể hoặc tay có vai trò diễn xuất quan trọng trong shot; đừng lúc nào cũng dùng không sẽ lố/ diễn.)
  5. **Hướng nhìn**
  6. **Biểu cảm khoảnh khắc**
  7. **Câu đóng băng** cuối khung (trạng thái TRƯỚC khi hành động).
- **Cấm Đạo Diễn Ngón Tay (Anti-Finger Trope)**: vì AI ngôn ngữ rất hay gán hành động "đếm bằng ngón tay", "xoa cằm" khi nhân vật đang thoại. **TUYỆT ĐỐI NGHIÊM CẤM** giơ số ngón tay để minh hoạ.
- **CẤM TẢ ÁNH SÁNG/THỜI ĐIỂM**: Tuyệt đối không miêu tả thời điểm, thời tiết, ánh sáng hay bảng màu trong prompt của SF lẻ (vd: không viết "CẢNH ĐÊM MƯA" hay "đêm đen"). Những thứ này thuộc về Thẻ địa điểm và đã được KHOÁ LOOK bằng ảnh đính kèm. Miêu tả lại sẽ làm ChatGPT nhiễu và đè mất Look gốc.
- **Nhất quán Không gian Nâng cao (Spatial Consistency & 180° Rule)**: Không chỉ gọi tên vật thể nền, mà còn BẮT BUỘC thiết lập 4 khóa trục không gian nhằm chống hallucination tuyệt đối khi đổi góc máy:
  - **1. Khóa hướng Camera**: Chọn một hướng la bàn cố định và không vượt qua nó (Vd: "Máy quay luôn ở hướng Nam, nhìn về Bắc").
  - **2. Khóa vị trí màn hình (Screen Mapping)**: Gắn cứng nhân vật/phe phái vào một nửa khung hình (Vd: A luôn ở SCREEN RIGHT, B luôn ở SCREEN LEFT). Tuyệt đối không đảo ngược.
  - **3. Khóa nền theo nhân vật (Background Coupling)**: Nếu A ở bên phải màn hình nhìn sang trái, hậu cảnh sau lưng A sẽ luôn là Cảnh A. Khi xoay máy quay sang B, hậu cảnh sau lưng B luôn là Cảnh B. Prompt BẮT BUỘC phải trích xuất đúng Cảnh A hoặc Cảnh B từ Floor Plan để làm nền.
  - **4. Khóa hướng sáng (Lighting Axis)**: Cố định nguồn sáng theo phương hướng màn hình (Vd: "Ánh sáng mặt trời chiếu từ bên phải màn hình") để đổ bóng luôn nhất quán.
- **TRẠNG THÁI KHÔNG GIAN CỦA CỤM**: Nêu tổng thể ai đang làm gì, nhưng **chỉ cắt theo nón quan sát của góc máy**. KHÔNG được nhồi tất cả nhân vật của scene vào khối này nếu họ không lọt vào khung.
- **Quy tắc TRẠNG THÁI CHỜ (Pending State)**: Nếu kịch bản/thoại có một mệnh lệnh thay đổi trạng thái tĩnh (ví dụ: mở cửa, ngồi xuống, đứng lên, đưa đồ), ảnh SF BẮT BUỘC phải vẽ trạng thái TRƯỚC KHI hành động đó xảy ra (cửa đóng, đang đứng, chưa cầm đồ). Tuyệt đối không vẽ trạng thái sau khi đã làm xong (vd: thoại nói "open up" thì SF phải vẽ cửa đang đóng). Thân người trung tính, nhưng **BIỂU CẢM PHẢI CỤ THỂ**. Cảm xúc nêu nguyên nhân (vd: *"vừa mất chỗ đứng..."*).
- **Quần chúng nền (Background Extras)**: Quần chúng nền ĐƯỢC QUYẾT ĐỊNH ĐỘC LẬP CHO TỪNG SF (tuỳ diễn biến và góc quay), TUYỆT ĐỐI KHÔNG khoá cố định hay quy chuẩn theo Thẻ Địa Điểm. Vì Thẻ Địa điểm (`refs.bg`) mặc định luôn là BỐI CẢNH TRỐNG, mọi nhân vật phụ/nền nếu có BẮT BUỘC phải được tạo ra bằng chữ trực tiếp trong khối `<AI VÀ ĐANG LÀM GÌ>` của riêng SF đó. 
  - **Nguyên lý 1: Mật độ Sinh tồn (Quy mô không gian)**
    Sự hiện diện và mật độ của đám đông không phải là một con số cố định, mà là tấm gương phản chiếu tính chất của bối cảnh tại khoảnh khắc đó. Không gian riêng tư triệt tiêu hoàn toàn sự tồn tại của nhân vật nền. Không gian công cộng điều tiết mật độ dựa trên thời gian thực tế của kịch bản (vắng vẻ ban đêm, luân chuyển giờ hành chính). Nếu nón quan sát không đổi, tuyệt đối không để đám đông bốc hơi một cách vô lý giữa các shot liền kề.
  - **Nguyên lý 2: Trạng thái Hành động & Tiết chế Cảm xúc**
    Trạng thái của quần chúng nền hãy xử lý linh hoạt và tự nhiên dựa trên sự liên quan của họ với tiền cảnh:
    - *Tính nhất quán Tư thế (Pose Continuity) & Luân chuyển Hành vi*: Tư thế vật lý cốt lõi (đứng, ngồi) của đám đông hầu như **KHÔNG ĐỔI** xuyên suốt một Scene. Tuy nhiên với các trạng thái tự nhiên của nhân vật, **TUYỆT ĐỐI CẤM** việc "khoá cứng" lặp đi lặp lại một hành động vi mô (như "cắm mặt ký giấy", "đưa ly uống nước") qua hàng tá SF liên tiếp gây cảm giác giả tạo như búp bê máy, trừ những trường hợp đặc biệt như người đàn ông ngủ gật ở ghế ( trạng thái đã tĩnh). Hãy luân chuyển/thư giãn các hành động nhỏ (ví dụ SF trước "ngồi ký giấy", SF sau chuyển thành "ngồi ngả lưng", "ngồi nói chuyện") để giữ tính tự nhiên của con người, miễn là vẫn duy trì tư thế NGỒI.
    - *Trường hợp có liên quan (Bị thu hút)*: Phần lớn nhân vật nền chỉ cần đứng/ngồi yên hướng mắt chú ý về phía sự kiện ở tiền cảnh là đủ. Không gán thêm các hành động thừa thãi.
    - *Trường hợp không liên quan (Sinh hoạt tự nhiên)*: Nếu sự kiện không ảnh hưởng đến họ, hãy để nhân vật nền hoạt động tự nhiên như vốn dĩ trong bối cảnh (ví dụ: người đi đường vẫn đang bước đi, khách vẫn đang ăn, bồi bàn đang bưng bê). Không cần gò ép họ phải đứng im, chỉ là mô tả hành động đó tại một khoảnh khắc chớp nhoáng (snapshot).
    - *Chuyển đổi Trạng thái theo Biến cố (State Transition)*: Trạng thái của đám đông KHÔNG PHẢI LÀ MỘT HẰNG SỐ CHẾT. Nếu diễn biến kịch tính leo thang (ví dụ: từ nói chuyện bình thường bỗng chuyển sang xô xát, cãi vã to tiếng, tai nạn), đám đông **BẮT BUỘC** phải chuyển đổi từ trạng thái "Sinh hoạt tự nhiên" sang trạng thái "Bị thu hút". (Ví dụ: Khách ở quán vỉa hè ban đầu đang ngồi uống cafe tự nhiên, nhưng khi hai nhân vật chính lao vào đánh nhau, tất cả mọi người phải dừng việc đang làm và quay sang nhìn, chú ý).
    - *Quy tắc Tiết chế*: **TUYỆT ĐỐI KHÔNG** vẽ vời cảm xúc phức tạp cho người nền. Giữ thái độ trung tính hoặc chỉ mô tả hành động thể chất, không bận tâm đến biểu cảm gương mặt của họ.

- **Hướng nhìn**: 2 người thì NHÌN THẲNG MẮT NHAU (trừ khi thoại bảo khác). 1 người thì nhìn vật/ngoài khung. Quần chúng **TUYỆT ĐỐI KHÔNG nhìn camera**.
- **Viết ngắn gọn**: Cắt mọi thứ ảnh ref đã có (màu áo, tóc), bỏ mã nội bộ.
- **Trần câu cấm**: Dưới 10 chữ `KHÔNG`.
- **Máy quay**: Bằng số đo cụ thể (cỡ cảnh, cao độ mét, khoảng cách, hướng sáng).
- **Câu đóng băng**: Mọi SF kết thúc bằng *"đúng khoảnh khắc ngay TRƯỚC khi..."*.

## Giới hạn ký tự (Trần)
- **Thẻ địa điểm**: `1.400 ký tự`.
- **SF thường**: `< 1.000 ký tự` 
- **LUẬT CHUNG**: `2500 ký tự` (Khai 1 lần cho mỗi địa điểm).

## Thiết kế một khung hình
- **Khung OTS**: Vai ở tiền cảnh phải là của NGƯỜI ĐANG ĐƯỢC NÓI VỚI.
- **Khung Cận (CU)**: Phải có 1 thân người ở tiền cảnh để ép máy quay lại gần, nếu không sẽ trôi ra khung rộng.
- **KHÔNG insert thuần đạo cụ hoặc thuần nhịp lặng không người**: Trừ cảnh thời tiết/bối cảnh thuần. Mọi cảnh khác phải CÓ NGƯỜI.
- **Giới hạn**: KHÔNG dựng khung ĐANG CHUYỂN ĐỘNG. TỐI ĐA 2 lớp chiều sâu.
- **Nghe lén**: Người nghe lén NÚP ở vùng tối, KHÔNG nhìn thấy người trong phòng (chỉ nghe).

## Checklist bắt buộc
0. **Địa điểm đã xuất hiện chưa?**: Rà tất cả scene. Đã xuất hiện (cùng phòng/cùng nhà/khu phố) thì phải khóa bằng `refs.bg`. Chú ý ngoại cảnh rất dễ sót.
1. **Cast**: Đúng người lọt nón quan sát.
2. **Nhân vật chính**: Vị trí, hướng nhìn, BIỂU CẢM KHOẢNH KHẮC.
3. **Quần chúng nền**: Có ai không? Từng vùng có gì? Mang đạo cụ hợp thời tiết/giờ. Khai theo từng vùng.
4. **Bản đồ không gian**: Giữ đúng continuity `pose`.
5. **Nội thất cơ bản**: Phải có (ghế, bàn, giường...).
6. **Đạo cụ**: Phân loại theo (a) Nền, (b) Hành động. **Đính ảnh REF_PROP** nếu là món chủ chốt, tối đa 2 ảnh.
7. **Đồ vật nối tiếp scene trước**: BẮT BUỘC rà SF cuối scene trước (đóng/mở, nằm đâu). Báo user nếu kịch bản mới mâu thuẫn, không tự lách.
8. **Giờ giấc/Đông đúc**: Khớp thoại.
9. **Chữ**: Liệt kê đủ, yêu cầu rõ ràng, không nhòe.
10. Đọc lại thoại xem mốc đổi trạng thái chuẩn chưa. Khớp 100% chữ kịch bản.

## Quy tắc SF trong dữ liệu
- **Thẻ địa điểm** (`REF_<ĐỊA ĐIỂM>_<THỜI ĐIỂM>`) nằm ở scene `REF`. Mang `luatchung`. Mọi SF dùng `refs.bg` trỏ về đây. 
- **MỌI NHÂN VẬT TRONG KHUNG ĐỀU PHẢI CÓ REF** trong `refs.chars` (kể cả vai/gáy tiền cảnh). Cần có đủ `REF_<TÊN>_PORTRAIT` và `FULL` đúng bộ đồ cảnh đó.
- **TỐI ĐA 4 NHÂN VẬT có ref / SF**. Nếu >4: 1. Cắt người -> 2. Tách 2 khung -> 3. Ưu tiên 4 người có thoại/gần nhất, số còn lại là quần chúng mờ.
