# film-prompts — kho viết prompt

Kho này CHỈ còn phần viết prompt cho `sf-board.json`: skill làm phim, luật kiểm
duyệt, công cụ kiểm luật và dữ liệu phim.

## Bố cục

```text
.claude/skills/skills-film/   luật viết prompt — SKILL.md + references/
.claude/memory-backup/        bản sao auto memory của user (chép TAY, xem dưới)
sfboard/kiem-luat.py          21 luật cứng trên sf-board.json
sfboard/kiem-noi-shot.py      kiểm nối shot giữa hai clip liền nhau
sfboard/liet-ke-dao-cu.py     gợi ý đạo cụ cần REF_PROP_
sfboard/sua-board.py          ghi/sửa sf-board.json theo schema
build_*/                      mã sinh prompt riêng của từng phim
*.project/                    dữ liệu phim: sf-board.json, KICH-BAN.md, assets
luu-ban.sh · quay-lai.sh      snapshot và khôi phục dữ liệu phim
```

## Quy trình

Khi task chạm tới prompt SF, prompt video, REF nhân vật/địa điểm, chia shot hoặc
nhạc Suno: đọc `.claude/skills/skills-film/SKILL.md` TRƯỚC, rồi mở đúng file
`references/` của bước đang làm. Khung nào có trẻ em thì bắt buộc mở
`references/LUAT-an-toan.md` trước khi viết.

Kiểm bằng máy, đừng kiểm tay:

```bash
python3 sfboard/kiem-luat.py PIPELINE-ALTAR.project [--scene S6]
python3 sfboard/kiem-noi-shot.py PIPELINE-ALTAR.project [S6] --day-du
```

Luật liên-scene TỰ TẮT khi chạy `--scene`; đọc phần dữ liệu chưa phủ trước khi
tin là "SẠCH".

## Luật cứng

- Luôn trả lời người dùng bằng tiếng Việt.
- Không đọc bất cứ project nào đã làm trước đó ( không tham khảo project cũ khi làm kịch bản mới)
- Chuẩn hoá cách đặt tên folder project với tên film giống hệt nhau bằng chữ viết hoa là title của kịch bản đó luôn. HOOK-TITLE hoặc FILM-TITLE.
- Không sửa `SKILL.md` hay file trong `.claude/skills/` nếu user không yêu cầu
  rõ. Không tự sửa skill khi user chê output.
- Không tự ý sửa `KICH-BAN.md` gốc. Chỉ sửa khi user yêu cầu đích danh, và phải
  ghi lịch sử ở đầu file (ngày, scene, sửa gì, vì sao).
- Luật đếm được thì ghi vào `kiem-luat.py`, không ghi thành văn bản. Tìm luật cũ
  và sửa cho sắc hơn trước khi thêm mục mới.
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
