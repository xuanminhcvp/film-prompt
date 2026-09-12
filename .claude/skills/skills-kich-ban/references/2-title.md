# 2 — Bước 2: TITLE

## 0. Ý tưởng lấy từ kho, không tự nghĩ

**Mở kho trước khi viết chữ nào** — `../../skills-title/kho/KHO-BO-SUNG-2026-09-12.md` (437 title) hoặc `../kho-tham-chieu/TITLES.md` (206). Title phải mọc từ một dòng có thật ở đó — cấm nghĩ ra một lõi tình huống không có trong kho, dù nó hay tới đâu. Đây là ngoại lệ duy nhất của luật "đang viết thì cấm mở kho"; nó chỉ mở cho `TITLES.md`, **không** mở cho `kich-ban/` và `short/`.

- **Giữ lõi tình huống của dòng gốc**: cặp quyền lực (kẻ ra đòn ↔ người chịu đòn), loại đòn, và trục lật.
- **Đổi ít là đủ**: chức danh, nghề, bối cảnh, tuổi, con số, thứ bị giấu, cách diễn đạt. Không bắt viết mới hoàn toàn.
- **Chức vụ và bối cảnh chỉ lấy từ kho**: tra `../../skills-title/kho/TU-DIEN-KHO.md` (98 chức vụ · 52 bối cảnh). Nghề lạ / nơi lạ là lỗi. Đổi chức vụ phải giữ đúng phía (kẻ ra đòn ↔ kẻ ra đòn). Con số, mốc thời gian, tuổi thì tự do.
- **Cấm hai đầu**: giao nguyên văn một dòng kho không đổi gì · nghĩ ra lõi không truy được về dòng kho nào.
- **Ghi kèm dòng gốc** khi báo title cho user, ví dụ `(gốc: TITLES #47)`.
- Năm phương án ở §3 phải **năm dòng gốc khác nhau**.

Kho vắng mặt (không track git, chưa tải) → dừng, báo user, đừng tự nghĩ title thay thế.

---

## 1. Công thức
- Tra `TITLE.cong-thuc` ở `../dang/bai/<DẠNG-BÀI>.md`.
- Vế sau phải lật, không được nối tiếp.
- Vế trước là tội, vế sau là giá.
- Không giao đáp án ở title. Vế sau phải cho biết cú lật to cỡ nào và chạm vào cái gì, nhưng không nói nó là gì.

## 2. Thước đo
- **Trần ký tự, số từ, số dấu gạch**: tra `TITLE.tran`. Vượt trần → cắt tính từ trước, cắt danh từ riêng sau.
- **Chữ số**: tra `6-giong-van.md` §3.
- **Từ bắt buộc**: tra `KHUNG-CHUNG.md` §2.3.
- **Cấm**:
  - Dùng tính từ đánh giá (*incredible, shocking...*).
  - Hứa thứ kịch bản không có.
  - Nêu thẳng cú lật cuối.
  - Ba mệnh đề trở lên.

## 3. Dựng 5, tự chọn 1
- **Chọn 5 dòng kho gốc khác nhau trước** (§0), rồi mới dựng.
- Dựng 5 phương án khác nhau về góc vào (kiểu vế trước).
- Tự chấm qua checklist. Chọn 1 phương án qua sạch checklist, không chọn tạm.
- Chọn phương án mà kịch bản trả được đầy đủ nhất.
- Báo user title đã chọn kèm 1 câu lý do.

## 4. Kiểm tra
- [ ] **Có dòng kho gốc, ghi kèm được, và không trùng nguyên văn dòng đó** (§0).
- [ ] **Chức vụ và bối cảnh đều có trong `skills-title/kho/TU-DIEN-KHO.md`.**
- [ ] **Năm phương án là năm dòng gốc khác nhau.**
- [ ] Dựng theo đúng `TITLE.cong-thuc`.
- [ ] Vế sau dấu gạch lật, không nối tiếp vế trước.
- [ ] Đúng mọi ràng buộc `TITLE.tran`, tối đa 2 mệnh đề, từ bắt buộc (chạy `scripts/kiem.py`).
- [ ] Không có tính từ đánh giá.
- [ ] Không lộ cú lật cuối.
- [ ] Kịch bản thực sự trả lời được lời hứa này.
- [ ] Che vế sau: hai đầu ở vế trước phải sắc.
- [ ] Vế sau hứa cụ thể (quy mô/chỗ đau) mà chưa lộ cú lật.
- [ ] Phương án chọn qua sạch mọi dòng trên.
