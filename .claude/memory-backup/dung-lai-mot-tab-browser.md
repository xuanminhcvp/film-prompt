---
name: dung-lai-mot-tab-browser
description: "Khi xem SF Board bằng browser tool, luôn dùng lại tab \"seed\" thay vì mở tab mới"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 226e57d5-4f80-4764-8bde-56b48d56c80d
  modified: 2026-08-09T05:12:07.586Z
---

Kiểm giao diện SF Board thì **dùng lại đúng một tab** — truyền `tabId: "seed"` cho
`mcp__Claude_Browser__navigate`. Không gọi `preview_start` (nó mở thêm tab), không
để `navigate` tự chọn tab.

**Why:** Mỗi lần sửa `board.html` xong lại mở một tab mới ở `localhost:<port>`, tab cũ
vẫn nằm đó. Sau một phiên sửa giao diện là 6 tab trùng nhau, user phải dọn tay. User
phàn nàn 2026-08-09.

**How to apply:** Sửa code → restart board → `navigate` với `tabId: "seed"` → chụp màn
hình trên chính tab đó. Lỡ sinh tab thừa thì `tabs_close` dọn ngay trong lượt đó, đừng
để dồn. Xem [[toi-da-4-chrome.md]] — cùng tinh thần giữ máy nhẹ.
