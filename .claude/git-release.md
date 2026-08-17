# Quy trình đẩy Git — ĐỌC TRƯỚC MỖI LẦN PUSH

> *Luật cứng nằm ở `CLAUDE.md`. File này chỉ chứa thao tác.*
>
> **Viết lại 2026-08-18.** Trước đó thư mục này có HAI kho chung một chỗ, và
> quy trình cũ xoay quanh việc chặn `.claude/` với `*.project/` khỏi kho public.
> Nay chỉ còn MỘT kho và nó private, nên luật lật ngược: skill và phần chữ của
> phim PHẢI lên git; thứ duy nhất phải chặn là MEDIA.

## 1. Kiểm TRƯỚC khi push

Chỉ một câu hỏi: có media lọt vào không. **Bắt buộc không trả về kết quả.**

```bash
git add -A && git diff --cached --name-only | grep -Ei "assets/|videos/|versions/|\.snapshots/|\.(mp4|mov|png|jpg|jpeg|webp|zip|tar|tgz|7z)$"
```

Có kết quả → DỪNG, xem lại `.gitignore`, đừng push. Media ở đây là 190GB; một
lần lọt là kẹt cứng và phải viết lại lịch sử để gỡ.

Xem tổng dung lượng sắp đẩy — con số lành mạnh là vài MB:

```bash
git diff --cached --name-only -z | xargs -0 du -ch | tail -1
```

## 2. Push

```bash
git push origin main
```

## 3. Kiểm SAU khi push

Đừng chỉ tin diff. Hỏi thẳng GitHub — repo phải là `private`:

```bash
gh api repos/xuanminhcvp/film-prompt --jq '.visibility'
```

Trả về khác `private` → skill, prompt và kịch bản của 6 phim đang công khai.
Xử lý ngay.

---

## Cấu trúc: một kho duy nhất

- **`xuanminhcvp/film-prompt` (PRIVATE)** — skill làm phim, 4 công cụ kiểm,
  `build_*/`, và json+md của các project. Đây là kho duy nhất của thư mục này.

Hai kho cũ đã cắt khỏi đây ngày 2026-08-18:

- `xuanminhcvp/grokpipe` (public) — code chạy máy, vẫn còn trên GitHub, không
  còn `.git` dưới máy.
- `xuanminhcvp/grokpipe-private` — kho `.git` của nó nằm ở
  `~/Desktop/grokpipe-git-cu-2026-08-18/git-rieng/`, không còn nối vào đây.

## Ghi nhớ (Không báo lại như phát hiện mới)

1. **Lịch sử `grokpipe` public**: vẫn chứa dữ liệu private cũ bị lộ (từ commit
   `61fd739`). User đã chốt KHÔNG rewrite lịch sử. Cấm tự ý can thiệp. Việc đó
   không đổi khi tách kho — repo cũ vẫn nằm nguyên trên GitHub.
2. **Media KHÔNG có bản backup trên git**: `sf-board.json` thì có, nhưng toàn bộ
   `assets/` và `videos/` thì không, và cố ý như vậy. Bản lưu của media là
   `./luu-ban.sh` (snapshot APFS trong `<project>/.snapshots`) cộng với việc
   user tự backup ổ cứng.
3. **`.claude/skills/` nằm trong git là CỐ Ý**, không phải lỗi — kho private.
