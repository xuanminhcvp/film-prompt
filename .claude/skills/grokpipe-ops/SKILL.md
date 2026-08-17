---
name: grokpipe-ops
description: Chẩn đoán khi khâu render của grokpipe hỏng — Grok/ChatGPT đổi giao diện làm selector chết, không thấy nút Submit/Video/thời lượng, lỗi CDP, crash tab, lô SF chết mà log sạch.
argument-hint: [triệu chứng]
---

# Chẩn đoán khâu render — Grok / ChatGPT / CDP

> **Chỉ mở khi khâu render hỏng.** Đừng đoán mò, phải đọc DOM thật.

## 1. Đọc DOM thật bằng Playwright
Nếu gặp triệu chứng: `Không thấy nút Video`, `Không thấy Submit`, `Không thấy chip thời lượng` -> Chạy thẳng đoạn script sau để đọc DOM hiện tại:
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    ctx = pw.chromium.connect_over_cdp("http://localhost:9228").contexts[0]
    p = [x for x in ctx.pages if 'grok.com' in (x.url or '')][0]
    p.goto("https://grok.com/imagine", wait_until="domcontentloaded")
    print(p.evaluate("""() => [...document.querySelectorAll('button,[role=radio]')]
        .filter(e => e.getBoundingClientRect().width > 0)
        .map(e => ({aria: e.getAttribute('aria-label'), type: e.getAttribute('type'),
                    text: (e.textContent||'').trim().slice(0,20)}))"""))
```

## 2. 5 Nguyên Tắc Xử Lý Lỗi Selector (Đừng mắc lại)
1. **Bám THUỘC TÍNH, đừng bám CHỮ**: UI có thể bị đổi sang tiếng Việt ("Gửi"). Hãy bám vào `button[type=submit]`. Chữ chỉ để dự phòng. Phím Enter là chốt cuối.
2. **DOM Grok KHÔNG nhất quán**: Cùng 1 nút nhưng lúc là `role=radio`, lúc là `button`. Luôn quét cả hai và khớp `aria-label` HOẶC `textContent`.
3. **Phải CHỜ nút hết `disabled`**: Nút bị `disabled` khi ô trống. Khi điền xong phải chờ vài giây (SPA cần thời gian dựng lại nút), kiểm `disabled`/`aria-disabled` trước khi bấm.
4. **Coi chừng Element ẨN đứng trước Element THẬT**: Trang hay giữ bản cũ (ẩn) đè lên bản mới (VD: `#prompt-textarea`).
   - *Playwright*: Phải lọc `filter(visible=True)`. Cấm dùng `nth(i)` sau khi tự gọi `is_visible()` vì thứ tự có thể trôi lúc thao tác. Thêm `.first` cho mọi locator nút để tránh lỗi strict mode.
   - *JavaScript*: `querySelector` thường bốc trúng ô ẩn đầu tiên. Mọi `evaluate` chạm ô soạn phải qua `_JS_O_SOAN`.
   - *Fail-closed*: Code kiểm tra phải phân biệt được "ô trống" và "không tìm thấy ô", nếu không lô ảnh chết mà log vẫn sạch (báo gửi thành công).
5. **Thông báo lỗi PHẢI KÈM HIỆN TRẠNG**: Mọi lỗi selector phải đính kèm danh sách các nút đang hiện (`_nut_dang_co()`) + URL, để người sau dễ debug.

## 3. Lỗi hàng loạt (Nhiều job hỏng cùng lúc)
Nhiều job lỗi cùng lúc thường do **HẠ TẦNG** (hết RAM, crash Chrome), KHÔNG PHẢI lỗi prompt. Đừng vội sửa prompt.
**Quy trình kiểm tra "Máy tôi chạy được, máy kia không":**
1. `git status` / `git rev-parse HEAD origin/main` (kiểm tra code đã đồng bộ chưa).
2. Kiểm tra ngôn ngữ giao diện Grok (`document.documentElement.lang`).
3. Cuối cùng mới nghi ngờ Grok đổi giao diện.

## 4. Cơ chế tự chữa
- **Bắt từ khóa cực chuẩn**: Hàm chẩn đoán tab chết bị thiếu đúng chữ `target crashed` làm mọi tab crash bị chết kẹt thay vì tự động mở lại.
- **Bắt Exception rõ ràng**: Tuyệt đối không dùng `except: return False`. Lỗi lập trình sẽ bị biến thành trạng thái hợp lệ (VD: cổng chặn nổ `NameError` vẫn báo "ĐANG KHÓA" làm bó tay). **Phải log exception trước khi trả về mặc định an toàn.**
