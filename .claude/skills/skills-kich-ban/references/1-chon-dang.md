# 1 — Chọn dạng bài (bộ định tuyến)

## 1. Ba tầng luật
- **Lõi (`references/`)**: Luật đúng với mọi kịch bản.
- **Khung chung (`dang/KHUNG-CHUNG.md`)**: 12 định mức, 8 nhiệm vụ hook, 7 nhiệm vụ thân.
- **Dạng bài (`dang/bai/<TÊN>.md`)**: Khởi động và Cú lật.

Nạp mỗi lượt: lõi + `dang/KHUNG-CHUNG.md` + **đúng MỘT** dạng bài.

## 2. Hợp đồng tham số
Tra cứu 12 tham số từ `KHUNG-CHUNG.md` §1. 
- `TITLE.cong-thuc`, `TITLE.tran`, `HOOK.do-dai`, `HOOK.chuoi-nuoc-di`, `HOOK.cta`, `HOOK.cau-chot`, `THAN.khung-muc`, `THAN.do-dai`, `THAN.cta-cuoi`, `VAN.ngoi-ke`, `VAN.nhip-cau`, `CHI-TIET.mat-do`.

## 3. Quy trình bước 1
1. **Có ý tưởng**: Chọn dạng khớp Khởi động & Cú lật ở `../dang/KHUNG-CHUNG.md` §8.
   **Không có ý tưởng**: Bốc ngẫu nhiên (loại 2 bài gần nhất).
2. Ghi đủ 3 dòng:
```
DẠNG BÀI: <tên file>
SỰ THẬT LÕI: <1 câu ≤ 25 từ, thứ khán giả chưa biết>
HẬU QUẢ: <năng lực gì> → <kẻ ra đòn mất thứ gì đếm được>
```
3. Phép thử `HẬU QUẢ`:
   - Thứ nhân vật giấu phải do họ LÀM NÊN (không phải do hoàn cảnh rơi xuống).
   - Vế sau phải bằng danh từ đếm được, không phải cảm xúc hối hận.
4. Nạp file và báo cho user (không chờ duyệt).

## 4. Mở rộng (Khi user gửi mẫu mới)
- **Nhánh A (Trùng định mức KHUNG-CHUNG)**: Tạo dạng mới `dang/bai/<TÊN>.md`. Thêm vào bảng `KHUNG-CHUNG.md` §8.
- **Nhánh B (Định mức khác hẳn)**: Tạo khung chung mới `dang/<TÊN>.md`.

## 5. Kiểm tra
- [ ] Ghi đủ `DẠNG BÀI:`, `SỰ THẬT LÕI:`, `HẬU QUẢ:`.
- [ ] `SỰ THẬT LÕI` ≤ 25 từ.
- [ ] `HẬU QUẢ` thoả mãn 2 phép thử ở §3.
- [ ] Chỉ nạp MỘT dạng bài kèm `KHUNG-CHUNG.md`.
