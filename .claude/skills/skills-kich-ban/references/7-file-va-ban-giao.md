# 7 — Ghi file và bàn giao

> **File này trả lời:** kịch bản nằm ở đâu, tên folder đặt thế nào, giao cho skill nào tiếp.
> **Mở khi:** bước 2 (chốt tên folder cùng lúc chốt title), bước 3 (tạo file, ghi hook) và bước 6 (chốt sổ).
> **Không chứa:** cách viết title (→ `2-title.md`) · bất kỳ luật dựng hình nào —
>   đó là việc của `skills-film` / `skills-hook`, skill này không đụng vào `sf-board.json`

## 1. Tên folder dự án

```
<LOẠI>-<TÊN NHÂN VẬT CHÍNH>--<TITLE RÚT GỌN TIẾNG VIỆT KHÔNG DẤU>.project
```

- `<LOẠI>`: `FILM` nếu sản phẩm là phim dài; `HOOK` nếu sản phẩm là video hook độc lập.
- Toàn bộ **VIẾT HOA**, không dấu tiếng Việt, khoảng trắng đổi thành `-`.
- Hai dấu gạch `--` ngăn tên nhân vật với title. Trong mỗi vế chỉ dùng một gạch.
- Title rút gọn: lấy phần lõi của title đã chốt, dịch sang tiếng Việt không dấu, tối đa 6 từ.

Ví dụ đúng: `FILM-NORA--PHONG-314.project` · `HOOK-GLORENE--CHIN-MUOI-GIAY.project`

**Chốt tên folder ngay ở bước 2**, cùng lúc title qua cửa QC. Đổi tên folder sau khi đã dựng board là việc phải sửa dây chuyền nhiều chỗ.

## 2. Ghi dần, không dồn về cuối

File được tạo ngay khi **hook qua cửa QC** (bước 3), rồi ghi nối tiếp sau mỗi lượt 4a · 4b · 4c. Bước 6 chỉ chốt sổ và bàn giao.

Giữ cả 7.500 từ trong hội thoại rồi mới ghi một lần là cách chắc chắn để mất chữ — và user không xem lại được phần đã duyệt trong lúc bạn viết phần sau.

## 3. File kịch bản

Mỗi dự án có **đúng một** `KICH-BAN.md` nằm ngay trong `<TÊN-DỰ-ÁN>.project/`.

Khung file, theo đúng thứ tự:

```markdown
# <TÊN-DỰ-ÁN VIẾT HOA> — <TITLE TIẾNG ANH ĐÃ CHỐT>

> Bản kịch bản gốc (người đọc). TUYỆT ĐỐI KHÔNG tự sửa. Mọi thay đổi phải ghi
> lịch sử ngay dưới đây (ngày · phần · sửa gì · vì sao).
>
> **DẠNG BÀI**: <một trong tám>
> **SỰ THẬT LÕI**: <một câu>
> **LỆCH CÓ CHỦ Ý**: <chỗ đã làm khác kho, và vì sao>

## Lịch sử sửa
- <YYYY-MM-DD> · Khởi tạo.

---

## HOOK

<toàn bộ hook, tiếng Anh>

---

## THÂN TRUYỆN

<toàn bộ phần sau hook, tiếng Anh>
```

Trong `## THÂN TRUYỆN` **không đánh số, không đặt tên nhiệm vụ vào bài** — tên nhiệm vụ lọt ra là template leakage (`8-chong-rap-khuon.md` §2.5). Các phần ngăn nhau bằng dòng trống.

## 4. Luật sau khi file đã tồn tại

- **Không tự sửa `KICH-BAN.md`.** Chỉ sửa khi user yêu cầu đích danh.
- Mỗi lần sửa, thêm một dòng vào `## Lịch sử sửa`: ngày · phần nào · sửa gì · vì sao. Không gộp nhiều lần sửa vào một dòng.
- **Không đọc `KICH-BAN.md` của dự án khác** khi viết kịch bản mới (`SKILL.md` §Luật cứng).
- Trước khi thử một hướng viết khác trên dự án đã có, chạy `./luu-ban.sh "ghi chú"` ở thư mục gốc.

## 5. Bàn giao

Skill này dừng lại khi `KICH-BAN.md` đã ghi xong. Không tạo `sf-board.json`, không tạo `BANG-SHOT.md`, không viết prompt.

Báo cho user đúng ba dòng:

```
Kịch bản xong: <đường dẫn KICH-BAN.md>
Dạng bài: <tên> · Hook <số> từ · Toàn bài <số> từ
Bước tiếp: dựng board bằng skills-film (phim dài) hoặc skills-hook (video hook 120 giây)
```

Rồi dừng. Chuyển sang dựng board là **một yêu cầu mới của user**, không phải phần đuôi của bước 3.

## 6. Kiểm tra

- [ ] Tên folder đúng khuôn `<LOẠI>-<TÊN>--<TITLE>.project`, viết HOA, không dấu.
- [ ] Tên folder đã được chốt từ bước 1, không đổi giữa chừng.
- [ ] `KICH-BAN.md` nằm ngay trong `.project/`, đúng một file, đúng khung ở §3.
- [ ] File đã được tạo từ bước 2 và ghi nối tiếp, không dồn ghi một lần ở cuối.
- [ ] Trong bài không có số thứ tự hay tên nhiệm vụ nào lọt ra.
- [ ] Có khối `## Lịch sử sửa` với dòng khởi tạo ghi ngày thật.
- [ ] Header có `DẠNG BÀI`, `SỰ THẬT LÕI` và `LỆCH CÓ CHỦ Ý`.
- [ ] Không tạo `sf-board.json` hay bất cứ file dựng hình nào trong lượt này.
- [ ] Đã báo user đúng ba dòng bàn giao ở §4.
