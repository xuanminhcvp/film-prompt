---
name: toi-da-4-chrome
description: User giới hạn pipeline chỉ được chạy tối đa 4 Chrome cùng lúc (không tính Chrome cá nhân)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b72893f5-0866-444d-a477-9cefb953bbed
  modified: 2026-07-30T04:59:48.180Z
---

Pipeline grokpipe chỉ được mở **tối đa 4 cửa sổ Chrome cùng lúc** (các Chrome có
`--remote-debugging-port=92xx`; Chrome cá nhân của user không tính). Đặt ra 2026-07-30.

**Why:** máy cạn RAM khi 8-9 Chrome pipeline chạy song song (còn ~65MB trống, 95 tiến trình
Chrome) → tab chết hàng loạt với lỗi `Locator.set_input_files: Target crashed`, 80 job render
ảnh hỏng một lượt.

**How to apply:** số tài khoản `enabled` trong `~/.grokpipe-accounts.json` ≤ 4 tại mọi thời
điểm. Giai đoạn render ảnh: 4 tài khoản ChatGPT. Giai đoạn render video: tắt bớt 1 ChatGPT để
nhường chỗ cho Grok (3 img + 1 vid). Guard/script giữ hàng đợi job song song ≤ 4. Liên quan
[[hook-auto-an-theo-ui]].
