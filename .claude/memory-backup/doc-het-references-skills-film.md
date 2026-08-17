---
name: doc-het-references-skills-film
description: "Phải đọc HẾT thư mục references/ của skills-film trước khi dựng prompt, không chỉ các file được route theo bước"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8b3d954d-ba80-4bb3-afbf-750d735a5b94
  modified: 2026-08-16T09:37:10.151Z
---

Trước khi viết dòng prompt đầu tiên cho một phim: `ls .claude/skills/skills-film/references/`
rồi **đọc từng file**, kể cả file không được SKILL.md route tới theo bước 1→5.

**Why:** 2026-08-15 dựng PIPELINE-AISLE-SEVEN, tôi đọc `1-chia-shot` → `5-nhac-suno` và
`LUAT-an-toan` nhưng bỏ `thao-tac-chatgpt.md`. Đúng file đó mới quy định: `luatchung` gồm
**6 khối** (khối 5 = Trục, khối 6 = Liên tục trạng thái đạo cụ theo dòng thời gian), trần
prompt thẻ địa điểm **1.400–1.800** ký tự, trần `luatchung` **3.000–4.500**, và khối **TAY
là TUỲ CHỌN**. Hậu quả trên dữ liệu thật: 19/19 thẻ thiếu khối Trục và khối Liên tục,
14/19 prompt thẻ địa điểm vượt trần, TAY viết ở cả 339 SF. Không phép kiểm nào bắt được —
`kiem-luat.py` không kiểm mấy điều này, thậm chí còn *bắt buộc* TAY (`KHOI_SF`), ngược với
skill.

**How to apply:** đọc hết references trước, rồi khi viện dẫn luật thì **trích `file:dòng`**
và đối chiếu ba nguồn — skill, code (`sfboard/`, `grokpipe/executors/`), và dự án cũ — chứ
đừng khẳng định theo trí nhớ của phiên làm việc. User kiểm lại từng câu và sẽ bắt được.
Liên quan [[grep-tieng-viet-json-du-an-cu]].
