# 7 — Ghi file và bàn giao

## 1. Tên folder dự án
- Cấu trúc: `<LOẠI>-<TÊN NHÂN VẬT CHÍNH>--<TITLE RÚT GỌN TIẾNG VIỆT KHÔNG DẤU>.project`
- `<LOẠI>`: `FILM` hoặc `HOOK`.
- Yêu cầu: VIẾT HOA, không dấu tiếng Việt, khoảng trắng = `-`. Ngăn 2 vế bằng `--`. (Ví dụ: `FILM-NORA--PHONG-314.project`).
- **Chốt ở bước 2**, cấm đổi tên giữa chừng.

## 2. File Kịch bản
- Ghi nối tiếp vào file ngay khi qua từng bước (Hook, 4a, 4b, 4c). Không gộp chung ghi 1 lần.
- Chỉ tạo **đúng 1 file** `KICH-BAN.md` trong folder `.project`.

### Khung file `KICH-BAN.md`:
```markdown
# <TÊN DỰ ÁN VIẾT HOA> — <TITLE TIẾNG ANH ĐÃ CHỐT>

> Bản kịch bản gốc (người đọc). TUYỆT ĐỐI KHÔNG tự sửa.
>
> **DẠNG BÀI**: <tên dạng>
> **SỰ THẬT LÕI**: <một câu>
> **HẬU QUẢ**: <nhân vật chính giấu NĂNG LỰC gì> → <kẻ ra đòn mất THỨ GÌ đếm được>

## Lịch sử sửa
- <YYYY-MM-DD> · Khởi tạo.

---

## HOOK

<toàn bộ hook, tiếng Anh>

---

## THÂN TRUYỆN

<toàn bộ phần sau hook, tiếng Anh>
```
- Trong `## THÂN TRUYỆN` cấm đánh số hay in tên khối nhiệm vụ. Các phần ngăn nhau bằng dòng trống.

## 3. Luật cập nhật kịch bản
- **Cấm tự sửa** `KICH-BAN.md` khi user chưa yêu cầu.
- Sửa phải ghi vào `## Lịch sử sửa` (ngày · phần · sửa gì · vì sao).
- Cấm đọc `KICH-BAN.md` dự án khác khi viết dự án mới.

## 4. Bàn giao
- Skill dừng lại khi đã có 2 file: `KICH-BAN.md` và `MO-TA-YOUTUBE.md`.
- **Cấm tạo** `sf-board.json`, `BANG-SHOT.md` hay viết prompt trong phiên này.
- Báo user đúng 4 dòng sau rồi DỪNG:
```
Kịch bản xong: <đường dẫn KICH-BAN.md>
Mô tả xong: <đường dẫn MO-TA-YOUTUBE.md>
Dạng bài: <tên> · Hook <số> từ · Toàn bài <số> từ
Bước tiếp: dựng board bằng skills-film (phim dài) hoặc skills-hook (video hook 120 giây)
```

## 5. Kiểm tra
- [ ] Tên folder đúng cấu trúc, viết HOA, không dấu.
- [ ] Chỉ có đúng 1 file `KICH-BAN.md` theo khung chuẩn.
- [ ] File đã ghi dần nối tiếp, không in tên nhiệm vụ ra.
- [ ] Header đủ `DẠNG BÀI`, `SỰ THẬT LÕI`, `HẬU QUẢ`.
- [ ] Không tạo file hình ảnh/prompt nào.
- [ ] Có đủ `KICH-BAN.md` và `MO-TA-YOUTUBE.md`.
- [ ] Đã báo user 4 dòng bàn giao.
