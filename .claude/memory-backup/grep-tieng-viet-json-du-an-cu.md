---
name: grep-tieng-viet-json-du-an-cu
description: grep chuỗi tiếng Việt trong sf-board.json của dự án cũ luôn trả rỗng vì file lưu \uXXXX — phải giải mã JSON mới tìm được
metadata: 
  node_type: memory
  type: project
  originSessionId: 8b3d954d-ba80-4bb3-afbf-750d735a5b94
  modified: 2026-08-16T09:36:53.717Z
---

`sf-board.json` của các dự án cũ (ALTAR, 8DOLLARS và toàn bộ `.snapshots/`) được ghi
với `ensure_ascii=True`, nên tiếng Việt nằm trong file dưới dạng `\uXXXX`.
**`grep "LUẬT CHỮ"` hay `grep "vệt mực mờ"` sẽ trả về RỖNG dù chuỗi đó có thật.**

**Why:** 2026-08-15, khi user hỏi luật "không chữ đọc được" nằm ở đâu, tôi grep toàn repo
và được 0 kết quả — suýt kết luận là luật đó không tồn tại ở đâu cả. Thực tế ALTAR có 181
lần, mỗi snapshot 8DOLLARS có ~201 lần, `build_altar/lib.py` có sẵn cả khối. Search hỏng
mà im lặng thì tệ hơn không search: nó cho ra một kết luận SAI trông rất chắc chắn.

**How to apply:** tìm chuỗi tiếng Việt trong `*.project/**/sf-board.json` thì phải
`json.load()` rồi `json.dumps(..., ensure_ascii=False)` trước khi regex — đừng tin
`grep`/`rg` trả rỗng trên các file này. File tôi tự ghi (`ensure_ascii=False`) thì grep
được bình thường, nên kết quả lệch nhau giữa dự án mới và dự án cũ là dấu hiệu của đúng
cái bẫy này. Liên quan [[doc-het-references-skills-film]].
