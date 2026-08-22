# Bước 2 — Tạo hình Nhân vật & Thẻ Địa điểm

> **Nguồn sự thật duy nhất** cho ảnh gốc của nhân vật và thẻ bối cảnh. Đọc trước khi viết bất kỳ prompt REF nào.

## Mục lục
1. [Nguyên lý REF chung](#nguyên-lý-ref-chung)
2. [Ảnh chân dung (PORTRAIT)](#ảnh-chân-dung-portrait)
3. [Ảnh toàn thân (FULL BODY)](#ảnh-toàn-thân-full-body)
4. [Luật: Trang phục & Mức sống](#luật-trang-phục--mức-sống)
5. [Luật: Trang sức](#luật-trang-sức)
6. [Luật: Thẻ nhân vật](#luật-thẻ-nhân-vật)
7. [Luật: Ảnh đạo cụ chủ chốt](#luật-ảnh-đạo-cụ-chủ-chốt)
8. [Quy trình Thẻ Địa Điểm](#quy-trình-thẻ-địa-điểm)
9. [Checklist trước khi sang Bước 3](#checklist-trước-khi-sang-bước-3)

---

## Nguyên lý REF chung
1. **Duy trì nhân dạng gốc:** Portrait là gốc. Full-body và SF phải lặp lại từ khoá khuôn mặt/tóc của portrait.
2. **Tham chiếu bằng ảnh, không bằng chữ:** Trực quan cần giống thì PHẢI đính ảnh vào `refs.chars` / `refs.bg`.
3. **REF CHÉO — BẮT BUỘC khi hai người mặc CÙNG MỘT BỘ ĐỒNG PHỤC:** Hai nhân vật cùng nơi làm việc + cùng vị trí công việc thì mặc cùng bộ đồng phục, và bộ thứ hai PHẢI đính ảnh full-body của bộ thứ nhất vào `refs.chars`. Chỉ áp cho ĐỒNG PHỤC, không áp cho thường phục dù hai người ăn mặc giống nhau.
4. **Nhất quán hai chiều:** Khi đổi bất cứ thứ gì ở thẻ REF, phải rà ngược lại mọi SF, media, và THOẠI liên quan.
5. **Đồng bộ toàn dự án:** Bất kỳ quy tắc mới nào được rút ra (trang sức, trang phục) phải quét và áp dụng cho TOÀN BỘ dự án ngay lập tức.
6. **Cấu trúc lệnh cố định:** tỉ lệ khung → loại ảnh/ống kính → mô tả nhân vật → bối cảnh/ánh sáng → câu chặn lỗi.
7. **Cấm bịa ngoài kịch bản — cả TRẠNG THÁI lẫn DANH MỤC MÓN:** Cấm bịa khiếm khuyết, độ xộc xệch, độ hở... ở BẤT KỲ REF nào — khuôn mặt, trang phục, đạo cụ. Đồng thời TUYỆT ĐỐI CẤM tự ý thêm hoặc bớt một món đồ khỏi bộ đồ chuẩn của dịp đó (như bỏ cà vạt, cởi áo khoác, thêm kính, thêm mũ). Đặc biệt CẤM dịch TÍNH CÁCH nhân vật thành trang phục ("ông ta phóng khoáng nên không thắt cà vạt") trong khi lên hình như vây sẽ không đẹp.

---

## Ảnh chân dung (PORTRAIT)
- **Mục đích:** Khóa khuôn mặt chuẩn cho cả phim. MỖI NHÂN VẬT CHỈ CÓ 1 PORTRAIT DUY NHẤT. (Tỷ lệ 2:3, Scene `REF`).
- **Góc chụp & Khung hình:** BẮT BUỘC chụp từ NGANG CỔ TRỞ LÊN, chính diện, nhìn thẳng vào ống kính. KHÔNG lấy thân người, KHÔNG lấy quần áo.
- **Ánh sáng & Nền:** Nền trắng xám trung tính trơn. Ánh sáng studio dịu đều, không mảng tối gắt.
- **Định dạng Prompt mẫu (Bắt buộc dùng phần mở đầu này):**
  > Ảnh chân dung tham chiếu nhân vật, photorealistic, chất điện ảnh, KHUNG DỌC 2:3 (cao hơn rộng), da có kết cấu thật với lỗ chân lông nhìn rõ, nét căng. Chụp NGANG CỔ TRỞ LÊN, chính diện, NHÌN THẲNG VÀO ỐNG KÍNH. Nền màu trơn, không đồ đạc. Ánh sáng studio dịu, đều trên mặt, KHÔNG mảng tối gắt. Chỉ từ cổ trở lên, không lấy thân/ quần áo. Miệng khép tự nhiên, KHÔNG cười.
- **Mô tả nhân vật:** Khoá cứng chủng tộc, kiểu tóc, tuổi bằng chữ. Không đính `refs.bg` hay ref nào khác.
- **Biểu cảm & Chặn lỗi:** Ánh nhìn tỉnh, ấm, chắc. Cấm làm hốc hác, quầng thâm hay nét khắc khổ (trừ khi kịch bản bắt buộc).
- **Cấm bịa phụ kiện/khiếm khuyết ngoài kịch bản:** KHÔNG tự thêm kính, sẹo, hình xăm, hay bất cứ đặc điểm khuôn mặt nào mà kịch bản không nhắc tới. Portrait mặc định là một gương mặt ƯA NHÌN, khoẻ mạnh — kể cả nhân vật phản diện hay nhân vật nghèo. Từ khoá hao mòn/mức sống (rẻ tiền, trầy xước, mí sụp, da xỉn...) CHỈ được dùng ở trang phục của ảnh FULL BODY, TUYỆT ĐỐI KHÔNG dùng cho khuôn mặt portrait.
- **Lưu ý:** Không tự ý crop ảnh đã duyệt.

---

## Ảnh toàn thân (FULL BODY)
- **Mục đích:** Xác định các "trạng thái trang phục" theo cốt truyện. Tỷ lệ 9:16.
- **Cách đính REF:** Đính `REF_<TÊN>_PORTRAIT` vào `refs.chars` để lấy mặt, thay trang phục. (SF đính cả 2: Portrait và Full-body tương ứng). Đặt tên theo trạng thái nghĩa.
- **Tối ưu Token:** TUYỆT ĐỐI KHÔNG tả lại ngũ quan khuôn mặt trong prompt FULL BODY. Chỉ ghi "Gương mặt giống ẢNH portrait tham chiếu" và dành chữ chỉ để để tả quần áo. Tránh AI bị "nhiễu" lai tạo mặt.
- **Quy tắc tạo:** Đổi TOÀN BỘ đồ → tạo REF FULL mới. Chỉ chỉnh nhỏ (tháo cà vạt, xắn tay) → viết thẳng vào SF, không tạo REF mới. Đặt tên theo NGHĨA (VD: `_HOME`, `_UNIFORM`).
- **Thẻ NEO của nhóm đồng phục:** Mỗi nhóm đồng phục chọn MỘT thẻ neo — thẻ của nhân vật xuất hiện nhiều cảnh nhất. Thẻ neo tả đầy đủ bộ đồ. Các thẻ còn lại trong nhóm đính ảnh thẻ neo vào `refs.chars`.
- **Khai nhóm đồng phục:** Khai bằng dòng máy đọc được ở cuối `desc`, cùng chỗ với dòng `Dùng:`:
  - `Đồng phục: LAOCONG (neo)` — ở thẻ neo
  - `Đồng phục: LAOCONG` — ở các thẻ còn lại

---

## Luật: Trang phục & Mức sống
- **Số lượng trang phục bắt buộc (áp dụng cho 4 nhân vật quan trọng nhất):** Phân bổ dựa theo số lượng phân cảnh (scene) xuất hiện để đảm bảo sự đa dạng:
  - **> 15 phân cảnh:** Bắt buộc có ít nhất 10 bộ trang phục.
  - **Từ 8 - 15 phân cảnh:** Bắt buộc có ít nhất 6 bộ trang phục.
  - **Từ 4 - 7 phân cảnh:** Bắt buộc có ít nhất 4 bộ trang phục.
- **Đồ thường ngày (Nếu nghèo):** 
  - BẮT BUỘC có từ khóa chỉ độ cũ (bạc màu, sờn vải). 
  - **Phanh hãm độ lố:** Phải luôn đi kèm từ khóa "được giặt cẩn thận". Cấm vẽ rách nát tơi tả như ăn xin trừ khi kịch bản yêu cầu. Nghèo thể hiện qua sự hao mòn chất liệu, không phải sự dơ bẩn.
- Nghèo chỉ ảnh hưởng CHẤT LIỆU (bạc màu, sờn), KHÔNG ảnh hưởng tới việc cài cúc/độ phẳng phiu — trừ khi kịch bản đã xảy ra xung đột vật lý ngay TRƯỚC khoảnh khắc đó (bị giằng co, bị đổ nước, vừa chạy...).
- **Bộ ra ngoài (Bộ tử tế khi đi văn phòng/ việc quan trọng):** Phẳng phiu, vừa vặn.
- **Gương mặt:** TUYỆT ĐỐI KHÔNG làm xấu khuôn mặt/thần thái nhân vật chính (không quầng thâm, hốc hác) dù hoàn cảnh tệ.

---

## Luật: Trang sức
- **Bắt buộc:** Nữ chính và nữ trẻ TUYỆT ĐỐI CÓ ít nhất 1 trang sức (dây chuyền, vòng tay, hoặc đồng hồ).
- **Nhất quán:** Chọn 1 món làm dấu riêng qua mọi bộ đồ.
- **Hiển thị theo áo:** Áo cổ V/tròn/hở → thấy dây chuyền. Áo sơ mi kín/khoác kín → dây chuyền nằm trong (không tả), đổi sang thấy khuyên tai/vòng tay.
- **Chống mù vị trí (Trái/Phải):** Khi tả vòng tay/nhẫn, BẮT BUỘC chỉ định rõ 1 bên (VD: "Đeo vòng ở cổ tay PHẢI)
- **Số lượng tối đa:** Công sở (2), Thường ngày (3). Nghèo (1).

---

## Luật: Thẻ nhân vật
- **Bắt buộc ghi trường `desc`:** Vai gì · Tuổi · Việc trong phim (số cảnh) · Mặt phải đọc ra điều gì.
- **Thẻ FULL ghi rõ danh sách cảnh:** Để riêng 1 dòng ở cuối định dạng `Dùng: S4 · S5 · S8`. (Để máy dễ quét đối chiếu `refs.chars`).

---

## Luật: Ảnh đạo cụ chủ chốt
- **Khi nào tạo REF cho đạo cụ (`REF_PROP_<TÊN>`):**
  - **MỘT DANH TỪ CÓ THỂ LÀ NHIỀU VẬT:** Trước khi tạo REF, rà xem cái tên ấy trong kịch bản có trỏ tới nhiều vật khác nhau không (hai chiếc thùng, ba bức tranh, hai cây bút). Nếu có: mỗi vật một mã REF riêng, tên gọi phân biệt được, và phải ghi rõ vật nào mang chữ / dấu hiệu nhận dạng — vì mọi SF sau đó sẽ trỏ vào nhầm nếu chúng cùng tên.
  - Xuất hiện ở ≥ 3 scene (không tính các vật dụng thông thường/nhỏ lẻ như cốc, chăn, quần áo).
  - Được nhắc thẳng trong thoại.
  - Gắn với LỆNH CẤM, BÍ MẬT, hoặc THÓI QUEN.
  - **Là vật trao tay, gieo-trả.**
- **Quy tắc tạo theo Quy mô:** Tỷ lệ 1:1, góc 3/4. KHÔNG CÓ người/tay, chỉ đạo cụ. Một vật nhiều trạng thái (ví mở/ví đóng, thùng nguyên đai/thùng đã bẻ dẹp) phải tạo các ảnh riêng. **Trạng thái của ảnh gốc là trạng thái vật ĐANG Ở trong cảnh ĐẦU TIÊN kịch bản dùng nó** — hàng chưa bán thì còn nguyên đai, thư chưa đọc thì còn phong bì, không được mở sẵn cho dễ nhìn thấy chữ. Muốn thấy chữ bên trong thì tạo ảnh trạng thái thứ hai, đừng bẻ trạng thái của ảnh gốc.
  - **Đạo cụ có ẢNH NGƯỜI in trên mặt (thẻ nhân viên, giấy tờ tuỳ thân, ảnh khung...):** vẫn phải đính `REF_<TÊN>_PORTRAIT` vào `refs.chars` để khuôn mặt in trên đó khớp nhân vật thật — KHÔNG để AI tự bịa một khuôn mặt lạ. Đồng thời phải MÔ TẢ RÕ trang phục/thời điểm của ảnh đó trong prompt (thường là ảnh chụp cũ hơn, trang phục khác cảnh hiện tại), vì nó không tự động thừa hưởng bộ đồ ở REF_FULL.
  - **Đạo cụ nhỏ cầm tay (Ví, điện thoại, nhẫn):** BẮT BUỘC đặt trên một bề mặt trung tính (VD: mặt bàn gỗ trơn) để AI tính toán tỷ lệ (Scale) và bóng đổ. Không vẽ lơ lửng.
  - **Đạo cụ CỠ LỚN (thùng hàng, tủ, máy móc, đồ nội thất):** ĐỨNG TRÊN SÀN của chính bối cảnh nó thuộc về, TUYỆT ĐỐI KHÔNG đặt trên mặt bàn — đặt lên bàn là mất sạch mốc tỉ lệ. Chụp góc 3/4 từ NGANG TẦM HÔNG, không chụp từ trên xuống. BẮT BUỘC khoá tỉ lệ bằng hai thứ cùng lúc: (a) số đo cụ thể so với cơ thể người ("cao ngang hông người lớn, khoảng một mét") và (b) một vật quen thuộc đứng cạnh làm mốc (bục trưng bày, ghế, thùng nhỏ).
  - **Phương tiện:** biển số và logo hãng làm mờ.


---

## Quy trình Thẻ Địa Điểm
- **Khởi tạo ĐỒNG LOẠT ở Bước 1**: Toàn bộ Thẻ địa điểm (và mọi biến thể thời gian của chúng) của CẢ KỊCH BẢN phải được tạo và đưa vào scene `REF` ngay từ đầu, cùng lúc với tạo hình Nhân vật. 
- **Biến thể sinh ra từ BẢN GỐC**: Dù mỗi biến thể giờ giấc (vd: Bếp ngày, Bếp đêm) bắt buộc phải là MỘT Thẻ địa điểm độc lập (có mã REF riêng), **TUYỆT ĐỐI KHÔNG** tạo lại prompt không gian từ đầu cho từng thẻ. Hãy chọn một thời điểm xuất hiện nhiều nhất/chi tiết nhất làm "Bối cảnh gốc" và tạo prompt. Với các biến thể thời gian khác, đính ảnh của Bối cảnh gốc vào làm tham chiếu (`refs.bg`). Prompt của thẻ biến thể lúc này cực ngắn, chỉ tập trung vào việc ra lệnh thay đổi thời điểm (VD: *"Giữ nguyên 100% không gian và đồ đạc của ảnh tham chiếu, chỉ đổi ánh sáng thành ban đêm với đèn đường vàng hắt vào"*).
- **Đồng bộ Kiến trúc cùng tòa nhà (Cross-Room Reference)**: Tương tự như biến thể thời gian, các căn phòng khác nhau trong cùng một tòa nhà (VD: Phòng khách, Bếp, Phòng ngủ) cũng phải đính kèm ảnh của một "Phòng Chủ đạo" (thường là Phòng khách) vào `refs.bg` để đảm bảo chúng chung một Art Direction.
  - ⚠️ **Phòng KÍN khác không gian THÔNG NHAU:** Lệnh chỉ định *"KHÔNG copy đồ đạc của ảnh gốc vào khung này"* CHỈ ĐÚNG khi hai phòng có tường ngăn hoàn toàn (phòng khách kín vs phòng ngủ kín). Nếu từ khu vực này vẫn **NHÌN THẤY** khu vực kia (cùng một sảnh hội trường thông nhau, lều y tế nhìn ra sân khấu chính, ban công nhìn xuống phòng khách, bếp mở thông phòng ăn), **TUYỆT ĐỐI CẤM** viết *"không copy"* cho phần kiến trúc nhìn thấy được — mà BẮT BUỘC phải viết ngược lại: *"Giữ nguyên 100% [sân khấu · bục phát biểu · ruy băng / landmark] ở lớp sau xa đúng theo ảnh tham chiếu, chỉ đổi vị trí máy quay."* Xóa landmark khỏi thẻ bối cảnh hoặc SF con thì mọi khung hình nhìn về hướng đó sẽ bị AI bịa lại từ đầu, mỗi khung một kiểu.
- **Thẻ địa điểm là BỐI CẢNH KHÔNG NGƯỜI (Empty Location)**: Thẻ địa điểm dùng để định hình Kiến trúc, Ánh sáng môi trường, và Trục không gian. Do đó, trường `refs.chars` BẮT BUỘC ĐỂ TRỐNG (không đính kèm nhân vật).
- **Nội dung Thẻ Địa Điểm**: Thẻ địa điểm CHỈ chứa quy hoạch không gian (Floor Plan) và quy tắc trục (Screen Mapping). TUYỆT ĐỐI KHÔNG chép lại ngoại hình, tính cách hay trang phục nhân vật vào phần miêu tả không gian.
- **CẤM NHÉT QUẦN CHÚNG VÀ CẤM NEGATIVE PROMPTS RÁC**: Để thể hiện bối cảnh trống, CHỈ CẦN ghi đúng 1 cụm: *"Không có người trong khung hình"*. Câu chỉ thị *"Không có người trong khung hình"* CHỈ cấm người, TUYỆT ĐỐI KHÔNG cấm sự sống/phương tiện của nơi chốn. Ngoại cảnh có lòng đường/ngã tư/bãi đỗ thì phần mô tả BỐI CẢNH ở Thẻ địa điểm BẮT BUỘC phải tả các yếu tố tĩnh trên mặt đường (xe ô tô/xe tải đỗ sát lề đường, dải phân cách, trạm chờ) — xe ĐỖ là kiến trúc của con phố, thuộc Thẻ địa điểm; xe ĐANG CHẠY/di chuyển là yếu tố động, để dành cho khối HẬU CẢNH của từng SF lẻ. **TUYỆT ĐỐI CẤM** AI tự ý nhồi nhét các câu "Negative Prompts" rác rưởi kiểu cũ như *"KHÔNG chữ, KHÔNG watermark, KHÔNG logo"*.
- **Thẻ địa điểm là BẢN NEO**: Chờ user duyệt sinh ảnh và chốt 100% thẻ địa điểm mới bắt đầu chia shot cho các scene. Khung hình con sẽ neo vào thẻ bằng `refs.bg`.

- **CẤM "Ngụ ý văn học"**: Dịch ẩn ý đạo diễn thành ngôn ngữ thị giác thuần tuý. Cấm viết "đây là sân nhà của cô ấy", "sự lệch pha là nội dung". Chỉ viết thị giác: "Sự tương phản mạnh giữa bộ vest đắt tiền và chiếc ghế bọc da nứt nẻ." AI vẽ pixel, không vẽ ẩn ý.
- **CẤM nhét Đạo cụ di động (Dynamic Props)**: Những đạo cụ thay đổi trạng thái hoặc chỉ xuất hiện ở vài khung hình (như lấy đồng hồ từ túi ra, đẩy tờ giấy qua bàn) BẮT BUỘC để ở prompt của từng khung SF lẻ. Tuyệt đối không đưa vào phần mô tả Bối cảnh để tránh việc AI hallucinate vẽ nó tràn lan ở mọi khung hình.
- **Rút gọn Lệnh hệ thống**: Viết các chỉ định (như phong cách, bộ lọc) thành các gạch đầu dòng sắc bén, tránh viết văn xuôi dài dòng.
- **Giới hạn Độ dài Prompt (Word Limit):** Phần prompt miêu tả Bối cảnh BẮT BUỘC phải nằm trong khoảng **200 đến 300 từ**.
- **Quy hoạch không gian 360° (Floor Plan)**: BẮT BUỘC miêu tả vị trí tương quan của các vật thể/tường lớn theo 4 hướng (Trái, Phải, Đối diện, Sau lưng). Ví dụ: "Bên trái là dãy cửa sổ, đối diện là quầy bar inox, sau lưng là cửa ra vào". Việc này cấp dữ liệu thô để AI tạo ảnh không bị "mù" không gian khi camera xoay góc.

- **Miêu tả thời gian/độ cũ (Production Design):** TUYỆT ĐỐI CẤM dùng mốc thời gian hoặc thập niên (ví dụ: *kiến trúc cuối 1990-đầu 2000, đã mở 30 năm*) vì AI sẽ lập tức biến thành bối cảnh kinh dị, bỏ hoang, tắt đèn. Nếu muốn không gian cũ, chỉ được dùng từ miêu tả vibe: *retro, well-maintained, lived-in* và PHẢI kèm theo chỉ định *"không gian sáng sủa, đang hoạt động bình thường"*. *(Ghi chú: Để thiết lập ánh sáng/màu sắc điện ảnh, phải tuân thủ nghiêm ngặt các quy tắc D.O.P tại file số 7).*

## Quy tắc viết prompt ảnh của thẻ địa điểm

> 1. **Bắt đầu bằng TÌNH HUỐNG, không bắt đầu bằng kiến trúc**: câu đầu tiên phải trả lời "không gian này đang được DÙNG CHO VIỆC GÌ tại đúng khoảnh khắc này" (VD: "một khu vực tạm dựng cho buổi họp toàn công ty"), rồi mới liệt kê đồ vật. Đồ vật phải là HỆ QUẢ của tình huống đó, không phải liệt kê kiến trúc trung tính.
> 2. **Khóa Quốc gia / Ngôn ngữ**: BẮT BUỘC thêm cụm "Bối cảnh ở Mỹ" vào đầu prompt bối cảnh.
> 3. **Địa điểm lấy set-dressing từ CẢ KỊCH BẢN, không giới hạn theo đoạn đang dựng** — khác với luật costume/đạo cụ (chỉ lấy từ đúng đoạn đang dựng). Vì địa điểm được tạo "Đồng loạt" để phục vụ cả phim.
> 4. **CẤM KHOÁ NIÊN ĐẠI BẰNG SỐ NĂM**: Tuyệt đối không viết "kiến trúc cuối 1990" hay "xây năm 2000", AI sẽ làm hình ảnh cũ nát, tối tăm như nhà hoang. Hãy tập trung vào việc tả chi tiết đồ vật hiện tại (VD: tivi CRT, điện thoại bàn...).

## Checklist trước khi sang Bước 3
- [ ] Mọi nhân vật có tên đều có 1 portrait duy nhất.
- [ ] Mọi trạng thái trang phục đều có 1 ảnh FULL (có đính portrait lấy mặt).
- [ ] Thẻ FULL ghi rõ danh sách cảnh dùng ở cuối trường `desc`.
- [ ] Trang phục khớp mức sống (có từ khoá cũ/mòn nếu nghèo) và đúng độ tuổi.
- [ ] Đã thêm trang sức cho nhân vật nữ và hợp lý theo cổ áo.
- [ ] Mọi thẻ REF (Portrait & Full) có `desc` đầy đủ vai/tuổi/ý nghĩa khuôn mặt.
- [ ] Đạo cụ chủ chốt đã có REF_PROP riêng (đủ các trạng thái).
