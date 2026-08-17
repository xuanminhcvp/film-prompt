#!/bin/bash
# Lưu một bản của MỌI dự án phim.
#   ./luu-ban.sh                 -> bản tự động (chạy theo lịch mỗi tối)
#   ./luu-ban.sh "ghi chú"       -> bản gõ tay, nên dùng TRƯỚC khi thử hướng mới
#
# Media + sf-board.json -> APFS clone vào <project>/.snapshots, gần như không
# tốn đĩa.
#
# 2026-08-18: gỡ hẳn phần git. Skill và công cụ nay nằm thẳng trong repo private
# grokpipe-prompt (`git add -A` là đủ) — script này chỉ còn lo snapshot media,
# thứ mà git cố tình không đụng tới vì nặng 190GB.
#
# TRƯỚC 2026-08-17 script này ghim đúng MỘT project (PIPELINE-8DOLLARS), mà
# project đó đã xong và không còn `sf-board.json`. Nên nó chụp media của một phim
# cũ trong khi 5 phim đang làm KHÔNG có bản lưu nào — phát hiện khi ALTAR mất
# `luatchung` của cả 27 thẻ bối cảnh và không có gì để lấy lại.
#
# `*.project/` vẫn nằm trong .gitignore và PHẢI ở lại như vậy: nguyên văn prompt
# và kịch bản chỉ đi lên repo private, và cũng chỉ phần json/md ở gốc project.
# Bản lưu thật của phim là .snapshots cục bộ, không phải git.
set -euo pipefail

ROOT="/Users/may1/Desktop/grokpipe"
GIU_NGAY=30
NGAY=$(date +%Y-%m-%d)
GIO=$(date +%H%M)
GHICHU="${1:-bản tự động}"

cd "$ROOT"

# ── mỗi project một bản clone (copy-on-write, tức thì) ──────────────────────
SO_PROJ=0
for DUONG in "$ROOT"/*.project; do
  [ -d "$DUONG" ] || continue
  PROJ=$(basename "$DUONG")
  SNAP="$DUONG/.snapshots"

  DICH="$SNAP/$NGAY"
  [ -d "$DICH" ] && DICH="$SNAP/$NGAY-$GIO"
  mkdir -p "$DICH"

  for TH in videos assets versions; do
    [ -d "$DUONG/$TH" ] && cp -c -R "$DUONG/$TH" "$DICH/$TH" 2>/dev/null || true
  done
  # sf-board.json là thứ QUAN TRỌNG NHẤT ở đây: prompt, luatchung, quan hệ REF.
  # Mất ảnh còn vẽ lại được; mất nó là mất toàn bộ phần chữ đã viết.
  CO_BOARD="—"
  if [ -f "$DUONG/sf-board.json" ]; then
    cp -c "$DUONG/sf-board.json" "$DICH/sf-board.json" 2>/dev/null || true
    CO_BOARD="có sf-board.json"
  fi
  for MD in "$DUONG"/*.md; do
    [ -f "$MD" ] && cp -c "$MD" "$DICH/$(basename "$MD")" 2>/dev/null || true
  done
  echo "$GHICHU" > "$DICH/.ghi-chu"

  # dọn bản quá hạn CỦA CHÍNH project này
  XOA=0
  for CU in "$SNAP"/*/; do
    [ -d "$CU" ] || continue
    NGAYCU=$(basename "$CU" | cut -d'-' -f1-3)
    TUOI=$(( ( $(date +%s) - $(date -j -f "%Y-%m-%d" "$NGAYCU" +%s 2>/dev/null || date +%s) ) / 86400 ))
    if [ "$TUOI" -gt "$GIU_NGAY" ]; then
      rm -rf "$CU"; XOA=$((XOA+1))
    fi
  done

  GIU=$( (ls -1d "$SNAP"/*/ 2>/dev/null || true) | wc -l | tr -d ' ')
  printf "· %-30s %s · giữ %s bản%s\n" "$PROJ" "$CO_BOARD" "$GIU" \
    "$([ "$XOA" -gt 0 ] && echo " · xoá $XOA bản quá $GIU_NGAY ngày")"
  SO_PROJ=$((SO_PROJ+1))
done

echo "✓ xong — $SO_PROJ project · đĩa trống $(df -h "$ROOT" | tail -1 | awk '{print $4}')"
