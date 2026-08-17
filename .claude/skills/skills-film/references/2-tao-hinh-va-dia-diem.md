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
9. [Quy tắc viết luatchung](#quy-tắc-viết-luatchung)
10. [Checklist trước khi sang Bước 3](#checklist-trước-khi-sang-bước-3)

---

## Nguyên lý REF chung
1. **Duy trì nhân dạng gốc:** Portrait là gốc. Full-body và SF phải lặp lại từ khoá khuôn mặt/tóc của portrait.
2. **Tham chiếu bằng ảnh, không bằng chữ:** Trực quan cần giống thì PHẢI đính ảnh vào `refs.chars` / `refs.bg`.
3. **REF CHÉO (Mượn trang phục/đạo cụ từ người khác):** Phải chống lỗi bằng 3 lớp: Mở đầu nói rõ "Đây là người HOÀN TOÀN KHÁC" → Mô tả tương phản cụ thể → Cấm copy mặt ở cuối.
4. **Nhất quán hai chiều:** Khi đổi bất cứ thứ gì ở thẻ REF, phải rà ngược lại mọi SF, media, và THOẠI liên quan.
5. **Đồng bộ toàn dự án:** Bất kỳ quy tắc mới nào được rút ra (trang sức, trang phục) phải quét và áp dụng cho TOÀN BỘ dự án ngay lập tức.
6. **Cấu trúc lệnh cố định:** tỉ lệ khung → loại ảnh/ống kính → mô tả nhân vật → bối cảnh/ánh sáng → câu chặn lỗi.

---

## Ảnh chân dung (PORTRAIT)
- **Mục đích:** Khóa khuôn mặt chuẩn cho cả phim. MỖI NHÂN VẬT CHỈ CÓ 1 PORTRAIT DUY NHẤT. (Tỷ lệ 2:3, Scene `REF`).
- **Góc chụp:** Nhìn thẳng camera. SÁNG RÕ (chụp studio).
- **Prompt:** Khoá cứng chủng tộc, kiểu tóc, tuổi bằng chữ. Không đính `refs.bg` hay ref nào khác.
- **Lưu ý:** Không tự ý crop ảnh đã duyệt.

---

## Ảnh toàn thân (FULL BODY)
- **Mục đích:** Xác định các "trạng thái trang phục" theo cốt truyện. Tỷ lệ 9:16.
- **Cách đính REF:** Đính `REF_<TÊN>_PORTRAIT` vào `refs.chars` để lấy mặt, thay trang phục. (SF đính cả 2: Portrait và Full-body tương ứng). Đặt tên theo trạng thái nghĩa.
- **Tối ưu Token:** TUYỆT ĐỐI KHÔNG tả lại ngũ quan khuôn mặt trong prompt FULL BODY. Chỉ ghi "Gương mặt giống ẢNH portrait tham chiếu" và dành chữ chỉ để để tả quần áo. Tránh AI bị "nhiễu" lai tạo mặt.
- **Quy tắc tạo:** Đổi TOÀN BỘ đồ → tạo REF FULL mới. Chỉ chỉnh nhỏ (tháo cà vạt, xắn tay) → viết thẳng vào SF, không tạo REF mới. Đặt tên theo NGHĨA (VD: `_HOME`, `_UNIFORM`).

---

## Luật: Trang phục & Mức sống
- **Đồ thường ngày (Nghèo):** 
  - BẮT BUỘC có từ khóa chỉ độ cũ (bạc màu, sờn cổ, giày mòn). 
  - **Phanh hãm độ lố:** Phải luôn đi kèm từ khóa "sạch sẽ, được giặt cẩn thận". Cấm vẽ rách nát tơi tả như ăn xin trừ khi kịch bản yêu cầu. Nghèo thể hiện qua sự hao mòn chất liệu, không phải sự dơ bẩn.
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
  - Xuất hiện ở ≥ 3 scene (không tính các vật dụng thông thường/nhỏ lẻ như cốc, chăn, quần áo).
  - Được nhắc thẳng trong thoại.
  - Gắn với LỆNH CẤM, BÍ MẬT, hoặc THÓI QUEN.
  - **Là vật trao tay, gieo-trả.**
- **Quy tắc tạo theo Quy mô:** Tỷ lệ 1:1, góc 3/4. Một vật nhiều trạng thái (ví mở/ví đóng) phải tạo các ảnh riêng. KHÔNG CÓ người/tay, chỉ đạo cụ.
  - **Đạo cụ nhỏ cầm tay (Ví, điện thoại, nhẫn):** BẮT BUỘC đặt trên một bề mặt trung tính (VD: mặt bàn gỗ trơn) để AI tính toán tỷ lệ (Scale) và bóng đổ. Không vẽ lơ lửng.
  - **Đạo cụ cỡ lớn / Phương tiện:** biển số làm mờ.


---

## Quy trình Thẻ Địa Điểm
- **Khởi tạo ĐỒNG LOẠT ở Bước 1**: Toàn bộ Thẻ địa điểm (và mọi biến thể thời gian của chúng) của CẢ KỊCH BẢN phải được tạo và đưa vào scene `REF` ngay từ đầu, cùng lúc với tạo hình Nhân vật. 
- **Biến thể sinh ra từ BẢN GỐC**: Dù mỗi biến thể giờ giấc (vd: Bếp ngày, Bếp đêm) bắt buộc phải là MỘT Thẻ địa điểm độc lập (có mã REF riêng), **TUYỆT ĐỐI KHÔNG** tạo lại prompt không gian từ đầu cho từng thẻ. Hãy chọn một thời điểm xuất hiện nhiều nhất/chi tiết nhất làm "Bối cảnh gốc" và tạo prompt. Với các biến thể thời gian khác, đính ảnh của Bối cảnh gốc vào làm tham chiếu (`refs.bg`) để **KHÓA KIẾN TRÚC**. Prompt của thẻ biến thể lúc này cực ngắn, chỉ tập trung vào việc ra lệnh thay đổi thời điểm (VD: *"Giữ nguyên 100% không gian và đồ đạc của ảnh tham chiếu, chỉ đổi ánh sáng thành ban đêm với đèn đường vàng hắt vào"*).
- **Đồng bộ Kiến trúc cùng tòa nhà (Cross-Room Reference)**: Tương tự như biến thể thời gian, các căn phòng khác nhau trong cùng một tòa nhà (VD: Phòng khách, Bếp, Phòng ngủ) cũng phải đính kèm ảnh của một "Phòng Chủ đạo" (thường là Phòng khách) vào `refs.bg`. Tuy nhiên, thay vì khóa không gian, `luatchung` của các phòng phụ phải mang lệnh đổi không gian: *"1. ĐỒNG BỘ PHONG CÁCH: Dùng ảnh tham chiếu CHỈ ĐỂ LẤY VẬT LIỆU (màu sơn tường, sàn/ nền, phong cách nội thất, độ cũ mới). ĐÂY LÀ MỘT CĂN PHÒNG KHÁC (Phòng Bếp). KHÔNG copy đồ đạc của ảnh gốc."* Điều này đảm bảo chúng chung một Art Direction.
- **Thẻ địa điểm là BỐI CẢNH TRỐNG (KHÔNG NGƯỜI)**: Thẻ địa điểm dùng để khóa Kiến trúc, Ánh sáng môi trường, và Trục không gian. Do đó, trường `refs.chars` BẮT BUỘC ĐỂ TRỐNG (không đính kèm nhân vật).
- **Nội dung luatchung (SIÊU NGẮN)**: Thẻ địa điểm CHỈ chứa quy hoạch không gian (Floor Plan), quy tắc trục (Screen Mapping), và luật khung ảnh chung. TUYỆT ĐỐI KHÔNG chép lại ngoại hình, tính cách hay trang phục nhân vật vào `luatchung`.
- **CẤM NHÉT QUẦN CHÚNG/NHÂN VẬT NỀN VÀO LUATCHUNG**: Mọi nhân vật phụ, khách qua đường, hay người làm nền BẮT BUỘC PHẢI để trống ở `luatchung` và chỉ được mô tả định lượng rõ ràng trong từng lệnh SF cụ thể. Thẻ địa điểm phải là nhà trống.
- **Thẻ địa điểm là BẢN NEO**: Chờ user duyệt sinh ảnh và chốt 100% thẻ địa điểm mới bắt đầu chia shot cho các scene. Khung hình con sẽ neo vào thẻ bằng `refs.bg`.
- **Thẻ địa điểm khoá KHÔNG GIAN, không khoá CAMERA**: SF thường TỰ DO đổi góc quay (xoay 360°, đổi cỡ cảnh). Đổi hướng thì PHẢI tả thứ thấy ở hướng đó.

## Quy tắc viết luatchung
- **KHÓA LOOK (CẤM TẢ ÁNH SÁNG/THỜI ĐIỂM)**: Tuyệt đối KHÔNG dùng các từ ngữ tả thời tiết, ánh sáng, giờ giấc (vd: "đêm đen", "đèn vàng ấm") trong khối `luatchung`. Vì `luatchung` sẽ bị tự động nhúng vào mọi prompt khung hình con, khiến DALL-E tự chế lại ánh sáng làm hỏng Look gốc của thẻ. Hãy chỉ đạo AI bằng lệnh: *"Ảnh bối cảnh đính kèm là để KHOÁ LOOK. Giữ nguyên 100% ánh sáng, bảng màu và tông màu của frame tham chiếu."*
- **CẤM "Ngụ ý văn học"**: Dịch ẩn ý đạo diễn thành ngôn ngữ thị giác thuần tuý. Cấm viết "đây là sân nhà của cô ấy", "sự lệch pha là nội dung". Chỉ viết thị giác: "Sự tương phản mạnh giữa bộ vest đắt tiền và chiếc ghế bọc da nứt nẻ." AI vẽ pixel, không vẽ ẩn ý.
- **CẤM nhét Đạo cụ di động (Dynamic Props)**: Những đạo cụ thay đổi trạng thái hoặc chỉ xuất hiện ở vài khung hình (như lấy đồng hồ từ túi ra, đẩy tờ giấy qua bàn) BẮT BUỘC để ở prompt của từng khung SF lẻ. Tuyệt đối không đưa vào `luatchung` để tránh việc AI hallucinate vẽ nó tràn lan ở mọi khung hình.
- **Rút gọn Lệnh hệ thống**: Viết các chỉ định (như phong cách, bộ lọc) thành các gạch đầu dòng sắc bén, tránh viết văn xuôi dài dòng.
- **Quy hoạch không gian 360° (Floor Plan)**: BẮT BUỘC miêu tả vị trí tương quan của các vật thể/tường lớn theo 4 hướng (Trái, Phải, Đối diện, Sau lưng). Ví dụ: "Bên trái là dãy cửa sổ, đối diện là quầy bar inox, sau lưng là cửa ra vào". Việc này cấp dữ liệu thô để AI tạo ảnh không bị "mù" không gian khi camera xoay góc.


## Checklist trước khi sang Bước 3
- [ ] Mọi nhân vật có tên đều có 1 portrait duy nhất.
- [ ] Mọi trạng thái trang phục đều có 1 ảnh FULL (có đính portrait lấy mặt).
- [ ] Thẻ FULL ghi rõ danh sách cảnh dùng ở cuối trường `desc`.
- [ ] Trang phục khớp mức sống (có từ khoá cũ/mòn nếu nghèo) và đúng độ tuổi.
- [ ] Đã thêm trang sức cho nhân vật nữ và hợp lý theo cổ áo.
- [ ] Mọi thẻ REF (Portrait & Full) có `desc` đầy đủ vai/tuổi/ý nghĩa khuôn mặt.
- [ ] Đạo cụ chủ chốt đã có REF_PROP riêng (đủ các trạng thái).
