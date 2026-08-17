---
name: hook-auto-an-theo-ui
description: "sfboard.py bên hook là bản copy, grokpipe là nguồn chuẩn; hai bên dùng chung tài khoản Chrome"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8b3d954d-ba80-4bb3-afbf-750d735a5b94
  modified: 2026-08-16T09:37:21.278Z
---

`sfboard.py` nằm bên hook là **bản copy**; nguồn chuẩn là bản trong repo `grokpipe`.
Hai bên **dùng chung pool tài khoản Chrome**, nên auto của bên này ăn theo trạng thái UI
của bên kia.

**Why:** sửa nhầm vào bản copy thì thay đổi biến mất ở lần đồng bộ sau; và vì chung tài
khoản Chrome nên bật auto cả hai bên là tranh nhau cùng một cửa sổ.

**How to apply:** mọi sửa đổi đi vào bản trong `grokpipe`. Trước khi bật auto, kiểm xem
bên kia có đang chạy không. Liên quan [[toi-da-4-chrome]].

⚠ File này được **dựng lại 2026-08-15** từ dòng tóm tắt còn sót trong `MEMORY.md` sau khi
file gốc bị mất — nội dung có thể thiếu so với bản đầu.
