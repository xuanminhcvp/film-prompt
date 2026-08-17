#!/bin/bash
# Quay một dự án về một bản đã lưu.
#   ./quay-lai.sh                              -> liệt kê project và số bản
#   ./quay-lai.sh PIPELINE-ALTAR.project       -> liệt kê các bản của project đó
#   ./quay-lai.sh PIPELINE-ALTAR.project 2026-08-17
#
# Bản HIỆN TẠI luôn được chụp lại trước khi ghi đè, nên quay lại không mất gì.
#
# HAI LỖI SỬA NGÀY 2026-08-17:
#
# 1. Script ghim đúng một project (PIPELINE-8DOLLARS) y như luu-ban.sh, nên 5 phim
#    đang làm không quay lại được.
# 2. Phần khôi phục `sf-board.json` KHÔNG BAO GIỜ CHẠY. Nó thử `git checkout
#    <tag> -- <project>/sf-board.json` trước, và vì tag luôn tồn tại nên nhánh
#    `elif` đọc snapshot không tới lượt — nhưng `*.project/` nằm trong .gitignore
#    nên file đó chưa từng có trong git, `git checkout` thất bại im lặng.
#    Kết quả: media được khôi phục, phần CHỮ (prompt, luatchung, quan hệ REF) giữ
#    nguyên trạng thái hiện tại. Người dùng tưởng đã quay lại xong.
#    Nay đọc thẳng từ snapshot — đó là nơi duy nhất thật sự có nó.
set -euo pipefail

ROOT="/Users/may1/Desktop/grokpipe"
cd "$ROOT"

# ── không tham số: liệt kê project ──────────────────────────────────────────
if [ $# -eq 0 ]; then
  echo "CÁC PROJECT VÀ SỐ BẢN ĐANG GIỮ:"
  for DUONG in "$ROOT"/*.project; do
    [ -d "$DUONG" ] || continue
    # `|| true` bọc CẢ pipeline: project chưa có .snapshots thì `ls` trả lỗi, và
    # với `set -o pipefail` cái lỗi đó giết luôn script giữa lúc liệt kê.
    SO=$( (ls -1d "$DUONG"/.snapshots/*/ 2>/dev/null || true) | wc -l | tr -d ' ')
    printf "  %-30s %s bản%s\n" "$(basename "$DUONG")" "$SO" \
      "$([ "$SO" = "0" ] && echo "   ⚠ CHƯA CÓ BẢN LƯU NÀO" || true)"
  done
  echo
  echo "Xem bản của một project:  ./quay-lai.sh <PROJECT>"
  exit 0
fi

PROJ="$1"
[ -d "$ROOT/$PROJ" ] || { echo "✗ không có project '$PROJ'. Chạy ./quay-lai.sh để xem danh sách."; exit 1; }
SNAP="$ROOT/$PROJ/.snapshots"

# ── chỉ có project: liệt kê các bản ─────────────────────────────────────────
if [ $# -eq 1 ]; then
  echo "CÁC BẢN CỦA $PROJ:"
  printf "  %-22s %-9s %-18s %s\n" "bản" "video" "phần chữ" "ghi chú"
  for T in "$SNAP"/*/; do
    [ -d "$T" ] || continue
    SO=$(ls -1 "$T/videos" 2>/dev/null | grep -c '\.mp4$' || echo 0)
    CHU=$([ -f "$T/sf-board.json" ] && echo "có sf-board" || echo "KHÔNG có")
    printf "  %-22s %-9s %-18s %s\n" "$(basename "$T")" "$SO clip" "$CHU" \
      "$(cat "$T/.ghi-chu" 2>/dev/null || echo '-')"
  done
  echo
  echo "Quay về:  ./quay-lai.sh $PROJ <tên bản>"
  exit 0
fi

BAN="$2"
NGUON="$SNAP/$BAN"
[ -d "$NGUON" ] || { echo "✗ $PROJ không có bản '$BAN'. Chạy ./quay-lai.sh $PROJ để xem danh sách."; exit 1; }

echo "Sắp quay $PROJ về bản: $BAN — $(cat "$NGUON/.ghi-chu" 2>/dev/null || echo '-')"
[ -f "$NGUON/sf-board.json" ] \
  && echo "  bản này CÓ sf-board.json — prompt và luatchung sẽ bị ghi đè theo." \
  || echo "  ⚠ bản này KHÔNG có sf-board.json — chỉ media được khôi phục."
read -p "Chắc chưa? (gõ 'co' để làm) " OK
[ "$OK" = "co" ] || { echo "đã hủy."; exit 0; }

# ── 1. chụp bản hiện tại trước khi ghi đè ───────────────────────────────────
echo "· chụp bản hiện tại để phòng khi cần quay ngược..."
"$ROOT/luu-ban.sh" "tự động lưu trước khi quay $PROJ về $BAN" >/dev/null
echo "  (đã lưu)"

# ── 2. khôi phục media ──────────────────────────────────────────────────────
for TH in videos assets versions; do
  if [ -d "$NGUON/$TH" ]; then
    rm -rf "$ROOT/$PROJ/$TH"
    cp -c -R "$NGUON/$TH" "$ROOT/$PROJ/$TH"
  fi
done
echo "· media: đã khôi phục"

# ── 3. khôi phục phần chữ ───────────────────────────────────────────────────
# Snapshot là nguồn DUY NHẤT — `*.project/` không nằm trong git và phải giữ như
# vậy vì repo này public. Nói rõ khi không có gì để khôi phục, đừng im lặng.
if [ -f "$NGUON/sf-board.json" ]; then
  cp -c "$NGUON/sf-board.json" "$ROOT/$PROJ/sf-board.json"
  echo "· sf-board.json: đã khôi phục từ snapshot"
else
  echo "· sf-board.json: ⚠ bản lưu KHÔNG có file này — phần chữ GIỮ NGUYÊN hiện tại"
fi
for MD in "$NGUON"/*.md; do
  [ -f "$MD" ] && cp -c "$MD" "$ROOT/$PROJ/$(basename "$MD")" 2>/dev/null || true
done

echo
echo "✓ đã quay $PROJ về bản $BAN"
echo "  Kiểm lại phần chữ vừa khôi phục:"
echo "  python3 sfboard/kiem-luat.py $PROJ"
