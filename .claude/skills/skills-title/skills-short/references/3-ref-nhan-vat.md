# 3 — Thẻ REF của một con người

> **File này trả lời:** thẻ gốc của một nhân vật (mặt, trang phục, trang sức) phải trông thế nào.
> **Mở khi:** tạo hoặc sửa bất kỳ `REF_*_PORTRAIT` / `REF_*_FULL` nào.
> **Không chứa:** cú pháp mã ID và dòng `Dùng:` / `Đồng phục:` (→ `2-du-lieu-sf-board.md`) ·
>   đạo cụ (→ `4-ref-dao-cu.md`) · ánh sáng bối cảnh (→ `5-the-dia-diem.md`) ·
>   người không có thoại (→ `9-quan-chung-nen.md`)

## 1. Nguyên lý nhân dạng
1. **Duy trì nhân dạng gốc:** Portrait là gốc. Full-body và SF phải lặp lại từ khoá khuôn mặt/tóc của portrait.
2. **REF chéo — bắt buộc khi hai người mặc cùng một bộ đồng phục:** hai nhân vật cùng nơi làm việc + cùng vị trí công việc thì mặc cùng bộ đồng phục, và bộ thứ hai phải đính ảnh full-body của bộ thứ nhất vào `refs.chars`. Chỉ áp cho đồng phục, không áp cho thường phục dù hai người ăn mặc giống nhau.

*(Các nguyên lý chung áp cho mọi loại thẻ REF — tham chiếu bằng ảnh, nhất quán hai chiều, đồng bộ toàn dự án, cấu trúc lệnh cố định — nằm ở `2-du-lieu-sf-board.md` §6.)*

---

## 2. Ảnh chân dung (PORTRAIT)
- **Mục đích:** Khóa khuôn mặt chuẩn cho cả phim, (Tỷ lệ 9:16, Scene `REF`).

- **Phạm vi tạo Portrait:** Chỉ 4 nhân vật quan trọng nhất của kịch bản mới cần portrait riêng. Nhân vật phụ không tạo portrait, chỉ tạo fullbody đầu tiên có khóa trực tiếp khuôn mặt + trang phục.
- **Ngoại lệ cho Short — KHÔNG tạo portrait cho bất kỳ ai:** Short không tạo `REF_*_PORTRAIT`, kể cả cho nhân vật chính. Mọi nhân vật (không phân biệt vai trò) đều dùng cơ chế "fullbody đầu tiên làm thẻ neo nhân dạng" ở mục 3 bên dưới. Lý do: Short chỉ dài 8–12 clip, một ảnh neo 9:16 khóa đủ mặt + đồ là đủ giữ nhân dạng xuyên suốt, không cần tách riêng vòng sinh ảnh chân dung.
- **Góc chụp & Khung hình — HAI GÓC TRONG MỘT ẢNH:** portrait bắt buộc là một ảnh **khung dọc 9:16** chia hai nửa TRÊN–DƯỚI của CÙNG MỘT người — nửa TRÊN chính diện nhìn thẳng ống kính, nửa DƯỚI góc ngang (profile 90°) nhìn về mép phải khung. nền trơn liền một dải, không đường kẻ chia và không chữ. Cả hai nửa chỉ lấy từ ngang cổ trở lên, không lấy thân người, không lấy quần áo.
- **Ánh sáng & Nền:** Nền màu trơn. Ánh sáng studio dịu đều, không mảng tối gắt.
- **Định dạng Prompt mẫu (bắt buộc dùng phần mở đầu này, không cắt bớt câu nào):**
  > Ảnh chân dung tham chiếu nhân vật, photorealistic, chất điện ảnh, KHUNG DỌC 9:16, da có kết cấu thật với lỗ chân lông nhìn rõ, nét căng. MỘT ẢNH DUY NHẤT chia hai nửa TRÊN và DƯỚI, CÙNG MỘT NGƯỜI: nửa TRÊN là góc CHÍNH DIỆN nhìn thẳng vào ống kính; nửa DƯỚI là góc NGANG (profile 90 độ) nhìn về phía bên phải khung hình. Cùng một khuôn mặt. Nền màu trơn. Ánh sáng studio dịu, đều trên mặt, KHÔNG mảng tối gắt. Cả hai nửa chỉ lấy NGANG CỔ TRỞ LÊN, không lấy thân/ quần áo. Miệng khép tự nhiên, KHÔNG cười. Không chữ, không khung viền, không đường kẻ chia giữa hai nửa.
- **Mô tả nhân vật:** Khoá cứng chủng tộc, kiểu tóc, tuổi bằng chữ. Không đính `refs.bg` hay ref nào khác.
- **Biểu cảm & Chặn lỗi:** Ánh nhìn tỉnh, ấm, chắc. Cấm làm hốc hác, quầng thâm hay nét khắc khổ (trừ khi kịch bản bắt buộc).
- **Cấm bịa phụ kiện/khiếm khuyết ngoài kịch bản:** không tự thêm kính, sẹo, hình xăm, hay bất cứ đặc điểm khuôn mặt nào mà kịch bản không nhắc tới. Portrait mặc định là một gương mặt ưa nhìn, khoẻ mạnh (đối với các nhân vật dưới 50 tuổi) — kể cả nhân vật phản diện hay nhân vật nghèo. Từ khoá hao mòn/mức sống (rẻ tiền, trầy xước, mí sụp, da xỉn...) chỉ được dùng ở trang phục của ảnh FULL BODY, tuyệt đối không dùng cho khuôn mặt portrait.
- **Bắt buộc có hao mòn do tuổi sinh học:** đây không phải "làm xấu", mà là dấu hiệu tuổi già / sức khoẻ (áp dụng với người già trên 70 tuổi).

---

## 3. Ảnh toàn thân (FULL BODY)
- **Mục đích:** Xác định các "trạng thái trang phục" theo cốt truyện. Tỷ lệ 9:16.
- **Cách đính REF:** Với 4 nhân vật chính, đính `REF_<TÊN>_PORTRAIT` vào `refs.chars` để lấy mặt, thay trang phục. (SF đính cả 2: Portrait và Full-body tương ứng). Đặt tên theo trạng thái nghĩa.
- **Với nhân vật phụ không có portrait (mọi nhân vật trong Short — xem ngoại lệ ở §2):** Fullbody đầu tiên là thẻ neo nhân dạng, `refs.chars` để rỗng. Trong `skills-film` gọi thẻ này là "NHÂN VẬT PHỤ + TRANG PHỤC"; trong Short gọi là "★ THẺ NEO NHÂN DẠNG + TRANG PHỤC" (dấu ★ đánh dấu đây là thẻ gốc). Cả hai đều khóa trực tiếp tuổi, sắc tộc, khuôn mặt, tóc, vóc dáng, thần thái và bộ đồ trong cùng một ảnh 9:16 — thêm câu "khuôn mặt phải lấy đủ lớn và đủ nét để đọc rõ từng đường ngũ quan" để chống khung toàn thân làm mặt bé. Các fullbody sau của cùng nhân vật (nếu có) phải đính fullbody đầu tiên vào `refs.chars` và ghi: giữ nguyên mặt, tuổi, tóc, vóc dáng, chỉ đổi trang phục.
- **Tối ưu Token (áp cho fullbody SAU thẻ neo đầu tiên):** từ ảnh full-body thứ hai trở đi của cùng nhân vật, tuyệt đối không tả lại ngũ quan khuôn mặt. Chỉ ghi "Gương mặt giống ảnh portrait/thẻ neo tham chiếu" và dành chữ chỉ để tả quần áo. Tránh AI bị "nhiễu" lai tạo mặt. *(Ngược lại, chính thẻ neo đầu tiên — portrait hoặc ★ THẺ NEO NHÂN DẠNG — bắt buộc phải tả đủ ngũ quan, vì đó là nguồn sự thật duy nhất.)*
- **Quy tắc tạo:** Đổi toàn bộ đồ → tạo REF FULL mới. Chỉ chỉnh nhỏ (tháo cà vạt, xắn tay) → viết thẳng vào SF, không tạo REF mới. Đặt tên theo nghĩa (VD: `_HOME`, `_UNIFORM`).
- **Thẻ neo của nhóm đồng phục:** Mỗi nhóm đồng phục chọn một thẻ neo — thẻ của nhân vật xuất hiện nhiều cảnh nhất. Thẻ neo tả đầy đủ bộ đồ. Các thẻ còn lại trong nhóm đính ảnh thẻ neo vào `refs.chars`. (Cách khai dòng `Đồng phục:` — `2-du-lieu-sf-board.md` §7.)

---

## 4. Trang phục & Mức sống
- **Số lượng trang phục bắt buộc** (áp dụng cho 4 nhân vật quan trọng nhất), phân bổ theo số phân cảnh xuất hiện để đảm bảo đa dạng:
  - **> 15 phân cảnh:** ít nhất 10 bộ trang phục.
  - **8 – 15 phân cảnh:** ít nhất 6 bộ.
  - **4 – 7 phân cảnh:** ít nhất 4 bộ.
- **Đồ thường ngày (nếu nghèo):**
  - Bắt buộc có từ khóa chỉ độ cũ (bạc màu, sờn vải).
  - **Phanh hãm độ lố:** phải luôn đi kèm từ khóa "được giặt cẩn thận". Cấm vẽ rách nát tơi tả như ăn xin trừ khi kịch bản yêu cầu. Nghèo thể hiện qua sự hao mòn chất liệu, không phải sự dơ bẩn.
- Nghèo chỉ ảnh hưởng chất liệu (bạc màu, sờn), không ảnh hưởng tới việc cài cúc/độ phẳng phiu — trừ khi kịch bản đã xảy ra xung đột vật lý ngay trước khoảnh khắc đó (bị giằng co, bị đổ nước, vừa chạy...).
- **Bộ ra ngoài** (bộ tử tế khi đi văn phòng / việc quan trọng): phẳng phiu, vừa vặn.
- **Gương mặt:** tuyệt đối không làm xấu khuôn mặt/thần thái nhân vật chính (không quầng thâm, hốc hác) dù hoàn cảnh tệ.
- **Bắt buộc phân biệt màu áo trong cùng scene:** khi thiết kế trang phục cho các nhân vật xuất hiện cùng nhau trong 1 scene, bắt buộc mỗi nhân vật mang một màu áo khác nhau rõ rệt (vd: A áo xanh nhạt, B áo xám tro). Tuyệt đối cấm để 2 hoặc nhiều nhân vật cùng scene mặc trùng màu áo (trừ đồng phục ngành/nghi thức bắt buộc). Việc phân biệt màu từ đây giúp prompt video nhận diện nhân vật tối giản (chỉ ghi màu áo, không ghi loại áo) chính xác 100% mà AI video không nhầm lẫn.

## 5. Trang phục theo chức vụ (Y phục thiết chế)
Có những nhân vật mà trang phục do thiết chế / bối cảnh nghề nghiệp quy định, không do mức sống hay tính cách cá nhân quyết định. Với các vai này, quy tắc mức sống không được áp dụng — không có bộ vest hay trang phục đời thường nào thay thế được y phục nghi thức/chuyên môn.

- **Danh sách vai phải rà y phục thiết chế:**
  Thẩm phán · Chủ tọa / Hội thẩm phiên điều trần (áo choàng đen) · Công tố viên · Bác sĩ / Dược sĩ / Y tá (blouse/đồ mổ) · Cảnh sát / Lính cứu hỏa / Quân nhân / Phi công (đồng phục ngành) · Đầu bếp · Giáo sĩ / Linh mục (áo dòng) · Học sinh · Công nhân bảo hộ · Nhân viên có đồng phục thương hiệu.
- **Xác định bằng bối cảnh hành nghề, không phụ thuộc danh xưng tiếng Anh:** dù kịch bản gọi là "Mr. Chairman" hay "Judge", nếu họ ngồi trên bục xét xử / bục điều trần (có quốc huy, cờ, bàn chủ tọa) → bắt buộc dùng Y phục nghi thức (áo choàng đen/lễ phục), không được gán bộ vest văn phòng thường.
- Các vai này tuyệt đối không rơi vào luật "Bộ ra ngoài: phẳng phiu, vừa vặn" thông thường.

## 6. Trang sức
- **Bắt buộc:** Nữ chính và nữ trẻ tuyệt đối có ít nhất 1 trang sức (dây chuyền, vòng tay, hoặc đồng hồ).
- **Nhất quán:** Chọn 1 món làm dấu riêng qua mọi bộ đồ.
- **Hiển thị theo áo:** Áo cổ V/tròn/hở → thấy dây chuyền. Áo sơ mi kín/khoác kín → dây chuyền nằm trong (không tả), đổi sang thấy khuyên tai/vòng tay.
- **Chống mù vị trí (Trái/Phải):** khi tả vòng tay/nhẫn, bắt buộc chỉ định rõ 1 bên (VD: "đeo vòng ở cổ tay phải").
- **Số lượng tối đa:** Công sở (2) · Thường ngày (3) · Nghèo (1).

## 7. Trường `desc` của thẻ nhân vật
- **Bắt buộc ghi:** Vai gì · Tuổi · Việc trong phim (số cảnh) · Mặt phải đọc ra điều gì.
- Thẻ FULL phải có dòng `Dùng: S4 · S5 · S8` ở cuối (định dạng: `2-du-lieu-sf-board.md` §7).

---

## 8. Checklist trước khi sang bước tạo địa điểm / bảng shot
- [ ] Chỉ 4 nhân vật quan trọng nhất có portrait riêng; nhân vật phụ dùng fullbody đầu tiên làm neo nhân dạng.
- [ ] Mọi portrait là ảnh 9:16 hai góc: trên chính diện · dưới ngang 90°.
- [ ] Mọi thẻ nhân vật (portrait & full) là khung dọc 9:16 và kết thúc bằng dòng `KHUNG DỌC 9:16`.
- [ ] Mọi trạng thái trang phục đều có 1 ảnh FULL (có đính portrait lấy mặt).
- [ ] Thẻ FULL ghi rõ danh sách cảnh dùng ở cuối `desc`.
- [ ] Trang phục khớp ba trục: Mức sống · Độ tuổi · Chức vụ (vai có y phục thiết chế thì y phục thắng mức sống).
- [ ] Đối chiếu Thẻ Trang Phục với Thẻ Địa Điểm: mức nghi thức của bối cảnh (quốc huy, cờ, bục cao, bàn thờ, sân khấu, phòng mổ...) phải khớp hoàn toàn với mức nghi thức của bộ đồ.
- [ ] Đã thêm trang sức cho nhân vật nữ và hợp lý theo cổ áo.
- [ ] Mọi thẻ REF (Portrait & Full) có `desc` đầy đủ vai/tuổi/ý nghĩa khuôn mặt.
- [ ] Không có hai nhân vật cùng scene trùng màu áo.
