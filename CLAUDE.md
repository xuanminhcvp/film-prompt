# film-prompts — kho viết prompt

## Luật cứng

- Luôn trả lời người dùng bằng tiếng Việt.
- Không đọc bất cứ project nào đã làm trước đó ( không tham khảo project cũ khi làm kịch bản mới)
- Chuẩn hoá cách đặt tên folder project với tên film giống hệt nhau bằng chữ viết hoa là title của kịch bản đó luôn. HOOK-TITLE hoặc FILM-TITLE.
- Không sửa `SKILL.md` hay file trong `.claude/skills/` nếu user không yêu cầu
  rõ. Không tự sửa skill khi user chê output.
- Không tự ý sửa `KICH-BAN.md` gốc. Chỉ sửa khi user yêu cầu đích danh, và phải
  ghi lịch sử ở đầu file (ngày, scene, sửa gì, vì sao).
- Trước khi thử hướng mới trên một phim, chạy `./luu-ban.sh "ghi chú"`. Snapshot
  là nơi DUY NHẤT có `sf-board.json` cũ — `*.project/` không nằm trong git.

## Git

- MỘT repo duy nhất: `xuanminhcvp/film-prompt`, **private**.
- Repo private nên skill, công cụ kiểm và phần chữ của phim đều được track —
  đó chính là thứ cần lưu. `.gitignore` chỉ chặn MEDIA và rác.
- ⛔ Media trong thư mục này là 190GB. `.gitignore` chặn sạch bên trong
  `*.project/` rồi mở lại đúng `*.json` + `*.md` ở tầng gốc. Đừng thêm ngoại lệ
  cho `assets/`, `videos/`, `versions/`, `.snapshots/`.
- Không có lệnh git nào chạy tự động. `luu-ban.sh` chỉ snapshot APFS vào
  `<project>/.snapshots` — đó là bản lưu của media, git không thay thế được.
- `.claude/memory-backup/` trước đây được `day-rieng.sh` tự rsync mỗi lần đẩy.
  Script đó đã gỡ, nên giờ phải chép tay trước khi commit, nếu không nó lặng lẽ
  cũ đi mà không ai biết:

  ```bash
  rsync -a --delete --exclude '.DS_Store' \
    ~/.claude/projects/-Users-may1-Desktop-film-prompts/memory/ .claude/memory-backup/
  ```
- Không pull/push/sync remote nếu user chưa cho phép chính xác.
- Không dùng commit message chung chung như `update`; mô tả đúng thứ đã đổi.
