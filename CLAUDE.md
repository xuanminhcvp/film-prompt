# grokpipe — kho viết prompt

Kho này CHỈ còn phần viết prompt cho `sf-board.json`: skill làm phim, luật kiểm
duyệt, công cụ kiểm luật và dữ liệu phim. Toàn bộ phần chạy máy (board HTTP, job
lifecycle, executor Grok/ChatGPT, test gate) đã gỡ khỏi thư mục này ngày
2026-08-18; lịch sử của nó nằm trong repo public `grokpipe` và trong `.git-rieng`.
Không dựng lại phần đó ở đây.

## Bố cục

```text
.claude/skills/skills-film/   luật viết prompt — SKILL.md + references/
.claude/memory-backup/        bản sao auto memory của user
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
- Không tự ý sửa, xoá, thay thế hoặc chọn version khác của ảnh/video đang dùng.
- Không sửa `SKILL.md` hay file trong `.claude/skills/` nếu user không yêu cầu
  rõ. Không tự sửa skill khi user chê output.
- Không tự ý sửa `KICH-BAN.md` gốc. Chỉ sửa khi user yêu cầu đích danh, và phải
  ghi lịch sử ở đầu file (ngày, scene, sửa gì, vì sao).
- Luật đếm được thì ghi vào `kiem-luat.py`, không ghi thành văn bản. Tìm luật cũ
  và sửa cho sắc hơn trước khi thêm mục mới.
- Trước khi thử hướng mới trên một phim, chạy `./luu-ban.sh "ghi chú"`. Snapshot
  là nơi DUY NHẤT có `sf-board.json` cũ — `*.project/` không nằm trong git.

## Git

- MỘT repo duy nhất: `xuanminhcvp/grokpipe-prompt`, **private**. Hai repo cũ
  (`grokpipe` public và `grokpipe-private`) đã cắt khỏi thư mục này ngày
  2026-08-18; kho `.git` của chúng nằm ở `~/Desktop/grokpipe-git-cu-2026-08-18/`.
- Repo private nên skill, công cụ kiểm và phần chữ của phim đều được track —
  đó chính là thứ cần lưu. `.gitignore` chỉ chặn MEDIA và rác.
- ⛔ Media trong thư mục này là 190GB. `.gitignore` chặn sạch bên trong
  `*.project/` rồi mở lại đúng `*.json` + `*.md` ở tầng gốc. Đừng thêm ngoại lệ
  cho `assets/`, `videos/`, `versions/`, `.snapshots/`.
- Không có lệnh git nào chạy tự động. `luu-ban.sh` chỉ snapshot APFS vào
  `<project>/.snapshots` — đó là bản lưu của media, git không thay thế được.
- Không pull/push/sync remote nếu user chưa cho phép chính xác.
- Không dùng commit message chung chung như `update`; mô tả đúng thứ đã đổi.
