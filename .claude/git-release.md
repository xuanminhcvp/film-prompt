# Quy trình đẩy Git — ĐỌC TRƯỚC MỖI LẦN PUSH

> *Luật cứng nằm ở `CLAUDE.md`. File này chỉ chứa thao tác.*

## 1. Kiểm tra TRƯỚC khi push PUBLIC
Chạy 2 lệnh kiểm tra sau. **BẮT BUỘC KHÔNG TRẢ VỀ KẾT QUẢ** (trừ dòng tiền tố D - deleted). Có kết quả -> DỪNG NGAY.
```bash
git add -A
git diff --cached --name-only | grep -Ei "^\.claude/|\.project/|kiem-luat|kiem-noi-shot|\.(zip|tar|tar\.gz|tgz|7z)$"
```
*(Lệnh trên lọc cả tiền tố và đuôi file nén để chống lọt `.claude.zip`. Cấm rút gọn).*

```bash
git diff --cached -- . ':!CLAUDE.md' | grep "^+" | grep -v "^+++" | grep -ci "KHÓA TỪ ẢNH NEO\|TRẠNG THÁI KHÔNG GIAN\|cận+trung"
```

## 2. Kiểm tra SAU khi push PUBLIC
Đừng chỉ tin diff, chạy Github API để xác nhận:
```bash
gh api repos/xuanminhcvp/grokpipe/contents/.claude/skills/skills-film/SKILL.md >/dev/null 2>&1 && echo "✗ LỘ" || echo "✓ sạch"
```

## 3. Đẩy PRIVATE (Kho riêng)
Dùng script để lách `.gitignore` của kho public mà KHÔNG dính media khổng lồ.
```bash
./day-rieng.sh trangthai    # Xem list sắp đẩy
./day-rieng.sh day          # Tự động add -f + commit "update" + push
```

---

## Cấu trúc: Hai Kho, Một Thư Mục (Chung file vật lý trên đĩa)
- **PUBLIC (`.git`)**: `xuanminhcvp/grokpipe` — CHỈ chứa code công cụ.
- **PRIVATE (`.git-rieng`)**: `xuanminhcvp/grokpipe-private` — Chứa code + skills + 2 tool kiểm + json/md các phim.

## Ghi nhớ (Không báo lại như phát hiện mới)
1. **Lịch sử Git Public**: Vẫn đang chứa dữ liệu private cũ bị lộ (từ commit `61fd739`). User đã chốt KHÔNG rewrite lịch sử. Cấm tự ý can thiệp.
2. **Media 21GB KHÔNG backup**: `sf-board.json` có trên kho private, NHƯNG toàn bộ `assets/` & `videos/` KHÔNG đẩy git. Việc backup ổ cứng là do user tự lo.
3. **`CLAUDE.md`**: Việc file này nhắc tới `.claude/skills/` (dù thư mục không lên public) là **cố ý**, không phải lỗi.
