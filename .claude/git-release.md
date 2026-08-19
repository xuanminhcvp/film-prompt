# Quy trình đẩy Git — ĐỌC TRƯỚC MỖI LẦN PUSH

> *Luật cứng nằm ở `CLAUDE.md`. File này chỉ chứa thao tác.*

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

## 2. Commit — viết message thế nào

Một message = **một dòng tiêu đề** nói ĐÃ ĐỔI GÌ, rồi nếu cần thì vài dòng nói
VÌ SAO. Người đọc là chính mình ba tháng sau, lúc đang tìm xem luật nào đã đổi
và tại sao.

```
<loại>: <đổi cái gì, ≤ 60 ký tự, không dấu chấm cuối>

<Vì sao đổi. Đổi vì đã gặp lỗi gì, hoặc vì luật cũ sai ở đâu.
Bỏ trống phần này nếu tiêu đề đã đủ.>
```

Sáu loại dùng trong kho này:

| loại | dùng khi | ví dụ tiêu đề |
|---|---|---|
| `luat` | đổi ngưỡng/luật trong `kiem-luat.py`, `kiem-noi-shot.py` | `luat: bắt SF thiếu khối KẾT CLIP khi shot có thoại lệnh` |
| `skill` | sửa `SKILL.md` hoặc file `references/` | `skill: gộp luật ánh sáng trẻ em vào LUAT-an-toan` |
| `phim` | sửa `sf-board.json`, `KICH-BAN.md`, `build_*/` | `phim: viết lại prompt video S8 của ALTAR cho khớp nối shot` |
| `cong-cu` | sửa script `sfboard/*.py`, `luu-ban.sh`, `quay-lai.sh` | `cong-cu: liet-ke-dao-cu đếm cả đạo cụ trong lời dẫn` |
| `docs` | `CLAUDE.md`, `AGENTS.md`, file này | `docs: ghi rõ khi nào một luật tự tắt lúc chạy --scene` |
| `chore` | dọn dẹp, đổi `.gitignore`, bỏ file | `chore: bỏ skill grokpipe-ops sau khi gỡ phần chạy máy` |

Ba lỗi phải tránh:

- **Chung chung**: `update`, `sửa lỗi`, `linh tinh` — đọc lại không biết là gì.
- **Kể thao tác thay vì kết quả**: `sửa file kiem-luat.py` → đổi thành `luat: …`
  nói rõ luật nào đổi.
- **Gộp nhiều việc không liên quan vào một commit**: sửa luật + sửa prompt của 3
  phim + dọn `.gitignore` thì tách ba commit, để sau còn lần ngược được.

Có sẵn khuôn nhắc khi gõ tay — `git commit` (không kèm `-m`) sẽ mở file
[.gitmessage](../.gitmessage) làm mẫu.

## 3. Push

```bash
git push origin main
```

Xem lại commit vừa đẩy gồm những gì:

```bash
git show --stat --oneline HEAD
```

Xem gọn lịch sử gần đây, mỗi commit một dòng kèm số file đổi:

```bash
git log --oneline --stat -5
```

## 4. Kiểm SAU khi push

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
