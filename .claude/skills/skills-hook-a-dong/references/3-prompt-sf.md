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
2. **Chữ trong khung (Khai báo hai chiều)**:
   - *(a) Chiều Muốn hiện:* Mọi chữ muốn hiện trên ảnh (bảng tên, biển số, logo) phải được liệt kê rõ, kèm đánh vần chính xác.
   - *(b) Chiều Không muốn hiện (Nhãn hiệu):* Mọi bề mặt có thể mang chữ mà ta KHÔNG khai — vỏ thiết bị, thùng hàng, bao bì, biển hiệu nền, biển số xe — BẮT BUỘC phải được khoá bằng câu khẳng định là nhãn hư cấu. Tự viết ra 1 thương hiệu hư cấu không có thật.
3. **Ba loại vật thể**:
   - **(a) Thuộc bối cảnh**: Bắt buộc có, tả khái quát, lùi ra nền (giấy tờ, sách vở...).
   - **(b) Đạo cụ tham gia hành động**: Đang cầm/đưa/nhìn. Tả cụ thể, tách bạch khỏi nhóm nền. **Đính ảnh nếu có**.
   - **(c) Đạo cụ minh họa nội tâm**: **THỪA, LOẠI BỎ.** (Vd: khung ảnh gia đình, bằng khen). Dùng ngôn ngữ cơ thể thay thế.
   - **BẢO VỆ REF_PROP (Khoe Đạo Cụ)**: Một khi đạo cụ đã được cấp thẻ `REF_PROP`, nghĩa là nó chứa thông tin tối quan trọng của kịch bản (logo, tên người, cấu tạo đặc biệt). Trong ảnh SF tĩnh, TUYỆT ĐỐI KHÔNG che khuất, lật úp mặt lưng, hay xoay góc chết của đạo cụ này về phía camera. SF bắt buộc phải "khoe" ra góc diện thấy rõ nhất các thông tin đó. Mọi hành động lật úp, giấu đi hay nhét vào túi phải là hành động XẢY RA TRONG VIDEO, tuyệt đối không được phép là trạng thái chết đứng trên ảnh SF.
4. **Xác định CAST & Lọc Tham chiếu (REF Filtering) theo góc máy**: 
   - **Tuyệt đối tuân thủ Điểm Đặt Camera**: Lấy từ bản đồ không gian toàn cảnh (Master SF). Bắt buộc chốt vị trí Đặt Máy Quay TRƯỚC, từ đó mới chiếu ra Nón Quan Sát. Số lượng người và hướng Background hoàn toàn phụ thuộc vào góc chĩa của máy quay.
   - **Lọc REF (Chống lỗi chật khung)**: Mỗi SF chỉ được phép mang thẻ tham chiếu (REF keys) của những nhân vật **THỰC SỰ CÓ MẶT** trong nón quan sát.
   - ⚠️ **CẤM TỰ ĐẨY NHÂN VẬT NGANG HÀNG THÀNH "LỚP SAU" (Bảo toàn raccord vị trí)**: Khi cắt góc cận/trung (Two-Shot, Single) từ Master SF có nhóm đứng ngang hàng (cùng mặt phẳng chiều sâu), TUYỆT ĐỐI KHÔNG tự ý mô tả nhân vật còn lại là *"LỚP SAU, ngoài nét"* hay *"đứng phía sau"*. Từ khóa *"LỚP SAU"* sẽ ép AI kéo nhân vật đó lùi sâu về hậu cảnh (ví dụ: làm Maya bị đứng tụt lại đằng sau Grant & Walter), gây vỡ raccord vị trí. 
     - *Xử lý đúng:* Nếu nhân vật nằm ngoài nón quan sát -> Không mô tả họ trong prompt SF hoặc REF. CHỈ ĐƯỢC dùng *"LỚP SAU"* khi nhân vật đó thực sự ĐANG ĐỨNG PHÍA SAU theo chiều sâu vật lý ở Master SF.

## Quy tắc Prompt MASTER SF (Shot Thiết lập Bối Cảnh)
- **Quy định Cỡ Cảnh (Shot Size)**: Ảnh SF dùng làm Master của Scene BẮT BUỘC phải là góc **Wide Shot** (Toàn cảnh) hoặc **Medium Shot** (Trung cảnh). Tuyệt đối không dùng các góc cận (như CU, OTS) làm Master vì chúng quá hẹp để thiết lập bối cảnh.
- **Tuyệt đối không dùng SF Nhịp (SF-B) làm Master SF**: Master SF PHẢI LÀ ảnh đầu tiên chuẩn vị trí và tư thế của nhân vật (chuẩn suốt trong scene). Ví dụ, nếu cảnh có 2 nhân vật, chuẩn nhất đầu tiên là lúc 2 nhân vật đã ổn định vị trí ngồi/đứng nói chuyện với nhau.
- **Vai trò của Master SF**: Đây là shot góc rộng/trung đầu tiên của scene (khi nhân vật đã vào vị trí). Nhiệm vụ của nó là gắn kết Nhân Vật vào Bối Cảnh (đã được tạo ở Thẻ Địa Điểm).
- **Trường `refs.bg`**: Của Master SF phải trỏ về ID của Thẻ Địa Điểm (VD: `REF_S1_DAY`).
- ⚠️ **THỨ TỰ SẮP XẾP**: Master SF phải nằm đúng vị trí thời gian xuất hiện của nó trong mảng sfs (theo thứ tự render video), TUYỆT ĐỐI KHÔNG gom toàn bộ Master SF lên đầu scene.

## Quy tắc Prompt SF Thường
- **Trường `refs.bg`**: Của SF thường BẮT BUỘC phải trỏ về ID của **Master SF** phụ trách Cụm Không Gian đó (VD: `SF-S1-M1-MASTER`). Tuyệt đối không trỏ lung tung hay tự ý trỏ về Thẻ Địa Điểm rỗng.
- ⚠️ **CẤM TẢ VỊ TRÍ TƯƠNG ĐỐI CỦA BÀN VÀ QUẦY Ở SF THƯỜNG (Chống lệch layout với Master SF)**:
  - SF thường đã kế thừa toàn bộ bối cảnh không gian từ Master SF qua `refs.bg`.
  - Riêng đối với các vật thể là **BÀN** và **QUẦY**: TUYỆT ĐỐI CẤM tả lại các vị trí tương đối như *"trước quầy"*, *"sau quầy"*, *"bàn giữa"*, *"bàn trước"*, *"bàn sau"*... ở SF thường (đặc biệt là trong khối HẬU CẢNH).
  - *Vì sao*: Việc nhắc lại các cụm từ vị trí tương đối của bàn/quầy sẽ khiến AI sinh ảnh hiểu nhầm thành chỉ thị thiết lập lại layout bối cảnh mới, dẫn tới hiện tượng biến dạng, nhân bản bàn/quầy hoặc dịch chuyển góc quầy lệch hoàn toàn so với ảnh Master SF.
- **Khối HẬU CẢNH (gồm HAI phần bắt buộc, viết đúng thứ tự)**: Quần chúng nền và hướng bối cảnh ĐƯỢC QUYẾT ĐỊNH ĐỘC LẬP CHO TỪNG SF (tuỳ diễn biến và góc quay), TUYỆT ĐỐI KHÔNG khoá cố định hay quy chuẩn theo Thẻ Địa Điểm. 

  **(a) TRỤC BỐI CẢNH (Bức tường / Môi trường sau lưng chủ thể)**:
  - *Khi nào BẮT BUỘC viết*: Khi máy quay chĩa theo hướng **NGƯỢC TRỤC** hoặc **KHÁC HƯỚNG** so với Master SF (ví dụ: các góc OTS nhìn ngược vào lòng phòng, Close-up quay lưng ra cửa hàng, khung quay ngược lại so với góc rộng Master). Câu đầu của khối HẬU CẢNH BẮT BUỘC gọi tên đích danh một trong bốn hướng đã khai ở khối **QUY HOẠCH 360°** của Thẻ Địa Điểm (VD: *"Hậu cảnh sau lưng Bryce là phía trong cửa hàng: dãy tivi treo tường và kệ hàng"*).
  - *Khi nào BỎ TRỐNG phần (a)*: Khi máy quay chĩa **CÙNG HƯỚNG/CÙNG TRỤC** với Master SF (kế thừa tự nhiên từ ảnh `refs.bg` Master SF).
  - *Vì sao*: Ảnh Master SF chỉ chứa MỘT hướng nhìn. Khung ngược trục mà không có chữ chỉ hướng bối cảnh hoặc ảnh trỏ neo thứ hai thì model AI sẽ tự động bê nguyên toàn bộ hậu cảnh Master SF cũ hoặc tự bịa ra một bối cảnh mới.

  **(b) NGƯỜI & PHƯƠNG TIỆN trong Nón Quan Sát (Phân loại theo Cỡ Cảnh)**:
  - *Quy tắc Nón Quan Sát Cận Cảnh (Close-up / ECU / Tight MCU)*: Ở các góc CẬN, nón quan sát cực hẹp và xóa mờ nền mạnh. **TUYỆT ĐỐI KHÔNG nhồi nhét cả vòng cung đám đông hoặc nhiều quần chúng rộng vào HẬU CẢNH góc cận**. Chỉ tả mảng bối cảnh tĩnh sau lưng (hoặc tối đa 1 dáng mờ ngay sát sau lưng nếu có). Nhồi đám đông vào góc cận sẽ làm AI xung đột góc máy (kéo trôi thành góc rộng) hoặc nhồi nhiều đầu người chèn ép sát mặt/tai chủ thể.
  - ⚠️ **Phân biệt Chữ vs Ảnh ở HẬU CẢNH**:
    - *Chữ trong prompt* CHỈ DÙNG cho quần chúng vô danh (người qua đường, khán giả nền).
    - *Nếu lớp sau chứa MAIN CAST đang diễn ở cụm khác:* TUYỆT ĐỐI KHÔNG tả họ bằng chữ văn xuôi thuần túy. BẮT BUỘC phải đính Master SF của cụm đó + `REF_<TÊN>_PORTRAIT` + `FULL` vào `refs.chars`, đồng thời khai tên họ vào dòng `goc` và `pose.who` như mọi nhân vật lọt vào khung. Tả bằng chữ thì AI sẽ dựng ra một người lạ mặc đồ na ná, đứng sai chỗ.
- **Cấm Đạo Diễn Ngón Tay (Anti-Finger Trope)**: vì AI ngôn ngữ rất hay gán hành động "đếm bằng ngón tay", "xoa cằm" khi nhân vật đang thoại. **TUYỆT ĐỐI NGHIÊM CẤM** giơ số ngón tay để minh hoạ.
- **CẤM TẢ ÁNH SÁNG/THỜI ĐIỂM**: Tuyệt đối không miêu tả thời điểm, thời tiết, ánh sáng hay bảng màu trong prompt của SF lẻ (vd: không viết "CẢNH ĐÊM MƯA" hay "đêm đen"). Những thứ này thuộc về Thẻ địa điểm và đã được KHOÁ LOOK bằng ảnh đính kèm. Miêu tả lại sẽ làm ChatGPT nhiễu và đè mất Look gốc.

- **TRẠNG THÁI KHÔNG GIAN CỦA CỤM**: Nêu tổng thể ai đang làm gì, nhưng **chỉ cắt theo nón quan sát của góc máy**. KHÔNG được nhồi tất cả nhân vật của scene vào khối này nếu họ không lọt vào khung.
- **TRẠNG THÁI CHỜ (Pending State - Sống còn cho Video):** Hỏi trước khi viết mỗi SF: *"Trong clip này có hành động thay đổi trạng thái nào không?"* Nếu có (đặt xuống, lật úp, mở nắp, tháo ra, ném đi), ảnh SF **BẮT BUỘC** phải vẽ trạng thái **TRƯỚC** khi thay đổi. Viết trạng thái đã xong vào SF (vd: thẻ đã úp, cửa đã mở) là giết chết nội dung của clip — video sẽ không còn hành động gì để diễn. Lệnh của kịch bản (face down, sit down, open it) là để chỉ định **clip kết thúc ở đâu**, chứ KHÔNG PHẢI chỉ định frame ảnh tĩnh bắt đầu như thế nào. Thân người trung tính, nhưng **BIỂU CẢM PHẢI CỤ THỂ**. Cảm xúc nêu nguyên nhân (vd: *"vừa mất chỗ đứng..."*).
- **Quần chúng nền (Background Extras)**: Quần chúng nền ĐƯỢC QUYẾT ĐỊNH ĐỘC LẬP CHO TỪNG SF (tuỳ diễn biến và góc quay), TUYỆT ĐỐI KHÔNG khoá cố định hay quy chuẩn theo Thẻ Địa Điểm. Vì Thẻ Địa điểm (`refs.bg` của Master SF) mặc định luôn là BỐI CẢNH TRỐNG, mọi nhân vật phụ/nền nếu có BẮT BUỘC phải được tạo ra bằng chữ trực tiếp trong khối `<AI VÀ ĐANG LÀM GÌ>` của riêng SF đó. 
  - **Nguyên lý 1: Mật độ Sinh tồn (Quy mô không gian & Phương tiện)**
    Sự hiện diện và mật độ của đám đông và phương tiện không phải là một con số cố định, mà là tấm gương phản chiếu tính chất của bối cảnh tại khoảnh khắc đó. Không gian riêng tư triệt tiêu hoàn toàn sự tồn tại của nhân vật nền. Không gian công cộng điều tiết mật độ dựa trên thời gian thực tế của kịch bản (vắng vẻ ban đêm, luân chuyển giờ hành chính). Nếu nón quan sát không đổi, tuyệt đối không để đám đông hay xe cộ bốc hơi một cách vô lý giữa các shot liền kề.
    Phương tiện giao thông chính là "quần chúng" của mặt đường. Khung hình ngoại cảnh nào có sự xuất hiện của lòng đường, ngã tư, làn xe hay bãi đỗ, khối HẬU CẢNH của TỪNG SF BẮT BUỘC phải khai báo rõ xe cộ đang di chuyển (mấy chiếc ô tô/xe buýt/xe máy, di chuyển theo hướng nào) và xe đỗ sát lề. Mặt đường trống trơn giữa ban ngày/giờ chiều sẽ bị AI đọc nhầm thành PHỐ ĐI BỘ hoang vắng.
    ⚠️ **Phanh hãm "Cô lập cảm xúc"**: Ở không gian công cộng, **TUYỆT ĐỐI KHÔNG** được viết trống người hoặc trống xe cộ (xoá sạch quần chúng/phương tiện) chỉ vì lý do cảm xúc hay ý đồ đạo diễn.
  - **Nguyên lý 2: Trạng thái Hành động & Tiết chế Cảm xúc**
    Trạng thái của quần chúng nền hãy xử lý linh hoạt và tự nhiên dựa trên sự liên quan của họ với tiền cảnh:
    - *Tính nhất quán Tư thế (Pose Continuity) & Luân chuyển Hành vi*: Tư thế vật lý cốt lõi (đứng, ngồi) của đám đông hầu như **KHÔNG ĐỔI** xuyên suốt một Scene. Tuy nhiên với các trạng thái tự nhiên của nhân vật, **TUYỆT ĐỐI CẤM** việc "khoá cứng" lặp đi lặp lại một hành động vi mô (như "cắm mặt ký giấy", "đưa ly uống nước") qua hàng tá SF liên tiếp gây cảm giác giả tạo như búp bê máy, trừ những trường hợp đặc biệt như người đàn ông ngủ gật ở ghế ( trạng thái đã tĩnh). Hãy luân chuyển/thư giãn các hành động nhỏ (ví dụ SF trước "ngồi ký giấy", SF sau chuyển thành "ngồi ngả lưng", "ngồi nói chuyện") để giữ tính tự nhiên của con người, miễn là vẫn duy trì tư thế NGỒI.
    - *Trường hợp có liên quan (Bị thu hút)*: Phần lớn nhân vật nền chỉ cần đứng/ngồi yên hướng mắt chú ý về phía sự kiện ở tiền cảnh là đủ. Không gán thêm các hành động thừa thãi.
    - *Trường hợp không liên quan (Sinh hoạt tự nhiên)*: Nếu sự kiện không ảnh hưởng đến họ, hãy để nhân vật nền hoạt động tự nhiên như vốn dĩ trong bối cảnh (ví dụ: người đi đường vẫn đang bước đi, khách vẫn đang ăn, bồi bàn đang bưng bê). Không cần gò ép họ phải đứng im, chỉ là mô tả hành động đó tại một khoảnh khắc chớp nhoáng (snapshot).
    - *Chuyển đổi Trạng thái theo Biến cố (State Transition)*: Trạng thái của đám đông KHÔNG PHẢI LÀ MỘT HẰNG SỐ CHẾT. Nếu diễn biến kịch tính leo thang (ví dụ: từ nói chuyện bình thường bỗng chuyển sang xô xát, cãi vã to tiếng, tai nạn), đám đông **BẮT BUỘC** phải chuyển đổi từ trạng thái "Sinh hoạt tự nhiên" sang trạng thái "Bị thu hút". (Ví dụ: Khách ở quán vỉa hè ban đầu đang ngồi uống cafe tự nhiên, nhưng khi hai nhân vật chính lao vào đánh nhau, tất cả mọi người phải dừng việc đang làm và quay sang nhìn, chú ý).
    - *Quy tắc Tiết chế*: **TUYỆT ĐỐI KHÔNG** vẽ vời cảm xúc phức tạp cho người nền. Giữ thái độ trung tính hoặc chỉ mô tả hành động thể chất, không bận tâm đến biểu cảm gương mặt của họ.

- **Giới hạn**: KHÔNG dựng khung ĐANG CHUYỂN ĐỘNG. Tối đa 2 lớp chiều sâu (Tối đa 3 lớp khi scene có từ 3 main cast trở lên).
- **Hướng nhìn**: 2 người thì NHÌN THẲNG MẮT NHAU (trừ khi thoại bảo khác). 1 người thì nhìn vật/ngoài khung. Quần chúng **TUYỆT ĐỐI KHÔNG nhìn camera**.
- **Viết ngắn gọn**: Cắt mọi thứ ảnh ref đã có (màu áo, tóc), bỏ mã nội bộ.
- **CẤM LẠM DỤNG TỪ "KHÔNG" (Negative Prompts rác)**: TUYỆT ĐỐI CẤM thói quen chèn các từ cấm vô nghĩa (như *"KHÔNG chữ, KHÔNG watermark, KHÔNG logo"*) vào cuối prompt SF. Chỉ dùng chữ KHÔNG khi thực sự cần thiết để chặn hành vi sai của nhân vật (VD: "nhìn nhau nhưng không chạm tay", "đứng yên không bước tới"). Đừng biến câu cấm thành rác.
- **KHẲNG ĐỊNH TRẠNG THÁI (Tránh cấm theo ngưỡng)**: Khi cần khoá một trạng thái mặc định (cài cúc, đóng cửa, đứng thẳng...), viết câu khẳng định trạng thái đó trước ("cài kín toàn bộ cúc"), KHÔNG viết dưới dạng ngưỡng cấm ("không cởi quá N nút") — câu ngưỡng bị AI sinh ảnh đọc thành cho phép một phần, không phải khoá cứng.
- **Máy quay**: Bằng số đo cụ thể (cỡ cảnh, cao độ mét, khoảng cách, hướng sáng).
- **Câu đóng băng**: Mọi SF kết thúc bằng *"đúng khoảnh khắc ngay TRƯỚC khi..."*.

## Giới hạn ký tự (Trần)
- **Thẻ địa điểm / Master SF**: `1.400 ký tự`.
- **SF thường**: `< 1.000 ký tự` 

## Thiết kế một khung hình
- **Khung OTS**: Vai ở tiền cảnh phải là của NGƯỜI ĐANG ĐƯỢC NÓI VỚI.
- **Khung Cận (CU)**: Phải có 1 thân người ở tiền cảnh để ép máy quay lại gần, nếu không sẽ trôi ra khung rộng.
- **Hook 3 giây đầu**: Shot SF mở đầu phải có thị giác hoặc cảm xúc giật gân, đập vào mắt người xem (VD: Cận cảnh bực tức tột độ, hành động gay cấn, góc máy độc đáo) để giữ chân họ ngay lập tức.
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
- **Thẻ địa điểm** (`REF_<ĐỊA ĐIỂM>_<THỜI ĐIỂM>`) nằm ở scene `REF`. Master SF dùng `refs.bg` trỏ về đây.
- **Master SF** (VD: `SF-S1-M1-MASTER`): Nằm ở đầu mỗi Cụm Không Gian (Blocking Shift). Có thể có NHIỀU Master SF trong 1 scene. Master SF dùng `refs.bg` trỏ về Thẻ Địa Điểm. Các SF Thường thuộc cụm nào BẮT BUỘC dùng `refs.bg` trỏ về đúng Master SF của cụm đó.
- **MỌI NHÂN VẬT TRONG KHUNG ĐỀU PHẢI CÓ REF** trong `refs.chars` (kể cả vai/gáy tiền cảnh). Cần có đủ `REF_<TÊN>_PORTRAIT` và `FULL` đúng bộ đồ cảnh đó.
- **TỐI ĐA 4 NHÂN VẬT có ref / SF**. Nếu >4: 1. Cắt người -> 2. Tách 2 khung -> 3. Ưu tiên 4 người có thoại/gần nhất, số còn lại là quần chúng mờ.
