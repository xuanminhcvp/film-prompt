# 2 — Dữ liệu `sf-board.json`: khuôn, mã định danh, chuỗi neo

> **File này trả lời:** ghi vào `sf-board.json` thế nào cho đúng khuôn, đặt mã gì, thẻ nào trỏ vào thẻ nào.
> **Mở khi:** khởi tạo dự án, đặt mã cho bất kỳ thẻ/shot nào, hoặc khi phân vân `refs` trỏ về đâu.
> **Không chứa:** nội dung prompt của từng loại thẻ (→ `3-ref-nhan-vat.md` · `4-ref-dao-cu.md` ·
>   `5-the-dia-diem.md` · `6-cum-va-master-sf.md` · `8-prompt-sf.md`) ·
>   quyết định scene có mấy shot (→ `7-bang-shot.md`)

> **Luật cốt lõi**: File này là khuôn mẫu (template) khi khởi tạo bất kỳ dự án mới nào, để phần mềm UI Board không bị lỗi. Không phụ thuộc vào việc tìm kiếm các dự án cũ làm mẫu.

## 1. Cấu trúc thư mục dự án
Khi bắt đầu một dự án mới, tạo một thư mục mang tên `<TEN_DU_AN>.project/` ở môi trường làm việc.
Thư mục này bắt buộc chứa 2 file chính:
- `KICH-BAN.md`: bản kịch bản gốc để con người đọc và AI tham chiếu (luật đối xử với nó ở `1-kich-ban.md`).
- `sf-board.json`: database trung tâm chứa toàn bộ thông tin nhân vật, đạo cụ, địa điểm và các shot hình (SF) của phim.

---

## 2. Cấu trúc chuẩn (Schema) của `sf-board.json`
Định dạng file phải là chuẩn JSON. Không được phép thiếu các key cốt lõi dưới đây.

### 2.1 Cấp Root
```json
{
  "film": "TÊN PHIM — MÔ TẢ NGẮN (VIẾT HOA)",
  "kind": "phim",
  "updated_at": "YYYY-MM-DD HH:MM:SS",
  "scenes": [
    // ... Chứa các mảng Object của Scene
  ]
}
```

### 2.2 Cấp Scene
Mảng `scenes` bắt buộc luôn bắt đầu bằng một Scene có `id` là `REF` (chứa nhân vật, đạo cụ, bối cảnh), tiếp theo mới đến các Scene của kịch bản (`HOOK`, `S0`, `S1`, `S2`...).

Cách quét kịch bản để biết cần dựng những scene nào: `1-kich-ban.md` §2.

```json
{
  "id": "REF", // Hoặc "HOOK", "S0", "S1", "S2"
  "name": "REF — nhân vật · đạo cụ · bối cảnh", // Hoặc "S1 — Tên cảnh"
  "sfs": [
    // ... Chứa các mảng Object của Start Frame (SF, ảnh tĩnh) — khuôn ở §2.3/2.4
  ],
  "shots": [
    // ... Chứa các mảng Object của Video Shot — khuôn ở §2.5. Scene REF để mảng này RỖNG.
  ]
}
```
⚠️ **`shots` là mảng bắt buộc trên MỌI scene, kể cả scene `REF`** (để rỗng `[]`). Phần mềm UI Board đọc cả hai mảng `sfs` và `shots` song song — thiếu `shots` trên một scene sẽ làm UI hiển thị sai.

### 2.3 Cấp SF — dành cho khung REF
Sử dụng cho các thẻ nhân vật, đạo cụ, bối cảnh (bên trong scene `REF`).

**A. Thẻ Chân dung (Portrait):**
```json
{
  "id": "REF_TEN_NHAN_VAT_PORTRAIT",
  "label": "★ TÊN NHÂN VẬT (đã chốt — ảnh user dán)",
  "desc": "Mô tả ngắn gọn về nhân vật, tính cách, tuổi tác...",
  "prompt": "Ảnh chân dung tham chiếu nhân vật...",
  "status": "draft", // Hoặc "approved", "proposed"
  "notes": "",
  "usedBy": [],
  "refs": {
    "chars": [],
    "bg": null
  },
  "picked": "" // Có thể điền tên file ảnh nếu đã chốt
}
```

**B. Thẻ Toàn thân (Full Body):**
Bắt buộc đính kèm Portrait vào `chars` và có dòng `Dùng:` ở cuối `desc`.
```json
{
  "id": "REF_TEN_NHAN_VAT_WORK_FULL",
  "label": "TÊN NHÂN VẬT — ĐỒNG PHỤC ĐI LÀM",
  "desc": "Mô tả ý nghĩa bộ đồ.\nDùng: S1 · S2 · S5",
  "prompt": "Ảnh tham chiếu TRANG PHỤC, photorealistic...",
  "status": "proposed",
  "refs": {
    "chars": [
      "REF_TEN_NHAN_VAT_PORTRAIT"
    ],
    "bg": null
  }
}
```

**C. Thẻ Đạo cụ (Prop):**
```json
{
  "id": "REF_PROP_TEN_DAO_CU",
  "label": "Tên đạo cụ — mô tả ngắn",
  "desc": "Ý nghĩa đạo cụ trong phim.\nDùng: S2 · S5",
  "prompt": "Ảnh tĩnh photorealistic...",
  "status": "proposed",
  "refs": {
    "chars": [],
    "bg": null
  }
}
```

### 2.4 Cấp SF — dành cho khung Cảnh quay (Shot)
Sử dụng cho các shot phim thực tế (S1, S2...). Mọi tham chiếu nhân vật, trang phục và đạo cụ đều được đặt chung vào mảng `chars`.
```json
{
  "id": "SF-S1-01",
  "label": "[NHỊP] S1-01 · Tóm tắt ngắn gọn bối cảnh/hành động",
  "goc": "Wide, nhân vật A ở giữa, rõ mặt...",
  "pose": {
    "zone": "Vị trí trong phòng",
    "who": {
      "TEN_NHAN_VAT_A": "Đang đứng tựa lưng..."
    },
    "dist": "Máy quay cách bao xa",
    "hands": {
      "TEN_NHAN_VAT_A": "Tay trái cầm cốc nước..."
    }
  },
  "prompt": "ẢNH THAM CHIẾU: [Ref], và SF-MASTER...\n\nTạo MỘT ẢNH TĨNH photorealistic 16:9, cinematic medium shot...\n\nCHỦ THỂ: [Mô tả nhân vật, trang phục, tay, mắt, cảm xúc]...\n\nHẬU CẢNH: [Mô tả không gian, quần chúng]...\n\nKHUNG NGANG 16:9",
  "refs": {
    "chars": [
      "REF_TEN_NHAN_VAT_PORTRAIT"
    ],
    "bg": "REF_BG_BOI_CANH"
  },
  "status": "draft",
  "picked": "" // App tự điền tên file ảnh khi user chốt; luôn khai key này dù rỗng
}
```

### 2.5 Cấp Shot — mảng `shots` của mỗi scene (video)
Mỗi scene (trừ `REF`, luôn để `[]`) còn có mảng `shots` riêng — chứa **object video hoàn chỉnh**, khác hẳn mảng `sfs` (ảnh tĩnh). Đây là dữ liệu cấp cho Grok/AI video, không phải cấp cho AI ảnh.

⚠️ **Mảng này KHÔNG được bỏ trống với scene có nội dung** — thiếu `text` là lỗi thường gặp nhất, làm ô "Lời thoại / hành động trong kịch bản" trên UI Board hiện trống trơn dù ảnh và prompt video đã đủ.

```json
{
  "id": "V-S1-01",
  "sf": "SF-S1-01",
  "dur": 10,
  "text": "AUDREY: \"Câu thoại nguyên văn...\"\nNARRATION: Câu văn kể nguyên văn (nếu có), giữ ĐÚNG thứ tự xuất hiện trong kịch bản gốc — không đảo Thoại/Narration cho \"nghe xuôi hơn\".",
  "prompt": "Prompt video đầy đủ theo form chuẩn (→ 11-prompt-video.md)",
  "status": "draft",
  "vpicked": "" // App tự điền tên file video khi user chốt; luôn khai key này dù rỗng
}
```

- **`text`**: nguyên văn dòng thoại/hành động của kịch bản mà đúng clip này bao phủ. Bắt buộc nội dung thật (không được để trống hay bịa), định dạng `SPEAKER: "..."` hoặc `NARRATION: ...`, mỗi dòng một lượt. Luật giữ đúng thứ tự và cách chia dòng dài: `1-kich-ban.md` §2.2.
- **`sf`**: trỏ về đúng 1 `id` trong mảng `sfs` của CHÍNH scene đó — đây là ảnh neo duy nhất cho toàn bộ video (10s hoặc 6s, cả 2 shot con). Không video nào được neo vào 2 ảnh.
- Field `picked`/`vpicked` do app tự quản lý (điền hậu kỳ khi user chốt ảnh/video) — Claude luôn khai key với giá trị `""`, không tự bịa tên file.

---

## 3. Mã định danh (ID format)

| Loại | Cú pháp | Ví dụ |
|---|---|---|
| Thẻ tham chiếu | `REF_<Tên>_<Loại>` | `REF_KEISHA_PORTRAIT` · `REF_BG_AISLE_SEVEN` |
| Thẻ địa điểm | `REF_<ĐỊA ĐIỂM>_<THỜI ĐIỂM>` | `REF_S1_DAY` |
| Master SF | `SF-S<scene>-M<n>-MASTER` | `SF-S1-M1-MASTER` |
| SF shot thoại | `SF-S<scene>-<stt>` — tức `SF-<Cảnh>-<Số>` | `SF-S1-01` · `SF-S1-07` |
| Shot video thoại | `V-S<scene>-<stt>` — tức `V-<Cảnh>-<Số>` | `V-S1-01` · `V-S1-02` · `V-S1-03` · `V-S1-05` |
| SF nhịp không thoại | `SF-S<scene>-<stt>-B<thứ_tự_nhịp>` | `SF-S1-04-B1` · `SF-S2-05-B1` |
| Shot video nhịp | `V-S<scene>-<stt>-B<thứ_tự_nhịp>` | `V-S1-04-B1` · `V-S2-05-B1` · `V-S1-08-B2` |

**Chèn shot vào board ĐÃ có media chốt** (VD tách một clip thành 2 clip 6s — `7-bang-shot.md` §5.2b): shot mới lấy mã của shot liền trước + hậu tố chữ hoa `B`, `C`… dính liền số, KHÔNG gạch nối: `SF-HOOK-03B` · `V-HOOK-03B`. Không đánh lại số các shot phía sau, vì file ảnh/video đã chốt (`assets/`, `versions/`, `videos/`, trường `picked`/`vpicked`) mang tên theo mã cũ. Hậu tố này xếp đúng sau `03` và trước `04` khi sắp xếp theo tên file. Board còn đang dựng, chưa có media → đánh số liên tiếp bình thường.

⛔ **Nhịp không thoại bắt buộc có số thứ tự shot trước rồi mới đến `B`.** Tuyệt đối không đặt dạng `V-S1-B1` thiếu số thứ tự shot, vì sẽ làm file video bị dồn xuống đáy khi sắp xếp file theo tên.

## 4. Thứ tự sắp xếp trong mảng `sfs`
Toàn bộ các SF (SF Nhịp, Master SF, hay SF thường) bắt buộc được sắp xếp trong scene theo đúng thứ tự thời gian xuất hiện (thứ tự render video) từ trên xuống dưới.

**Tuyệt đối không gom các Master SF lên trên đầu bảng.**

## 5. Chuỗi neo `refs` — ai trỏ vào ai

```
Thẻ địa điểm (REF_BG_*)  ←── refs.bg ── Master SF  ←── refs.bg ── SF thường
Thẻ Portrait  ←── refs.chars ── Thẻ Full Body  ←── refs.chars ── SF
```

- **Thẻ địa điểm** nằm ở scene `REF`. `refs.chars` của nó bắt buộc để trống.
- **Master SF** dùng `refs.bg` trỏ về ID của Thẻ Địa Điểm. Có thể có nhiều Master SF trong 1 scene.
- **SF thường** thuộc cụm nào thì bắt buộc dùng `refs.bg` trỏ về đúng Master SF của cụm đó. Tuyệt đối không trỏ lung tung hay tự ý trỏ về Thẻ Địa Điểm rỗng.
- **Khung gối đầu hai cụm** có cách nối riêng: `6-cum-va-master-sf.md` §Khung gối đầu.

### 5.1 Ai được vào `refs.chars`
- **Mọi nhân vật chính trong khung đều cần có REF** (kể cả vai/gáy tiền cảnh). Cần đủ `REF_<TÊN>_PORTRAIT` và `FULL` đúng bộ đồ cảnh đó.
- **Lọc tham chiếu (Cut-out — chống lỗi chật khung):** Mỗi SF chỉ mang thẻ tham chiếu của những nhân vật thực sự có mặt trong nón quan sát. Chỉ gạt khỏi `refs.chars` những nhân vật không có mặt vật lý trong không gian đó, hoặc đứng sau lưng máy quay.
- Người đang ở trong phòng mà nằm trong nón quan sát thì phải có ref — kể cả khi họ chỉ là vai/gáy tiền cảnh hay một dáng mờ ở lớp sau. Gạt một người đang đứng ngay đó là bắt model dựng lại căn phòng thiếu họ.
- **Tối đa 4 nhân vật chính có ref / SF (tối đa 8 thẻ ref nhân vật).** Thẻ Master SF neo bối cảnh phụ được miễn trừ hoàn toàn khỏi trần này. Nếu >4 nhân vật chính: 1. Cắt người → 2. Tách 2 khung → 3. Ưu tiên 4 người có thoại/gần nhất, số còn lại là quần chúng mờ.

### 5.2 Không tái sử dụng SF — ghi vào dữ liệu thế nào
- **Mỗi shot trỏ về một `id` SF riêng.** Trong một scene, số mã `sf` khác nhau phải **bằng đúng** số phần tử của mảng `shots`. Tuyệt đối không có hai shot cùng giá trị `sf`.
- Mạch thoại lặp góc (chuỗi A-B-A-B) vẫn sinh SF mới cho từng lượt, đặt mã tiếp theo theo thứ tự thời gian.
- *Luật đầy đủ và cách làm SF mới khác SF cũ*: `7-bang-shot.md` §1.1.

## 6. Nguyên lý chung của mọi thẻ REF
1. **Tham chiếu bằng ảnh, không bằng chữ:** trực quan cần giống thì phải đính ảnh vào `refs.chars` / `refs.bg`.
2. **Nhất quán hai chiều:** khi đổi bất cứ thứ gì ở thẻ REF, phải rà ngược lại mọi SF, media, và thoại liên quan.
3. **Đồng bộ toàn dự án:** bất kỳ quy tắc mới nào được rút ra (trang sức, trang phục) phải quét và áp dụng cho toàn bộ dự án ngay lập tức.
4. **Cấu trúc lệnh cố định:** tỉ lệ khung → loại ảnh/ống kính → mô tả nhân vật → bối cảnh/ánh sáng → câu chặn lỗi.
5. **Sửa dây chuyền:** sửa gì trong `sf-board.json` thì nhớ sửa cả những thứ liên quan bị ảnh hưởng theo.

## 7. Quy ước trường `desc`
- **Dòng danh sách cảnh** — để riêng 1 dòng ở cuối `desc`, định dạng: `Dùng: S4 · S5 · S8` (để máy dễ quét đối chiếu `refs.chars`).
- **Dòng nhóm đồng phục** — cùng chỗ với dòng `Dùng:`:
  - `Đồng phục: LAOCONG (neo)` — ở thẻ neo
  - `Đồng phục: LAOCONG` — ở các thẻ còn lại

## 8. Khuôn của trường `prompt` — áp cho mọi thẻ ảnh

| Loại thẻ | Trần ký tự |
|---|---|
| Thẻ địa điểm / Master SF | `1.400 ký tự` |
| SF thường | `< 1.000 ký tự` |

**Dòng kết thúc bắt buộc: Prompt của mọi Thẻ Địa Điểm (`REF_BG_*`) và mọi Start Frame (`SF-*` trong `sfs[]`, bao gồm cả Master SF và SF thường)** bắt buộc kết thúc bằng dòng `KHUNG NGANG 16:9` ở dòng cuối cùng của prompt.

## 9. Quy tắc vận hành JSON
- **Cấm tự ý xóa key:** phần mềm đọc giao diện JSON Board sẽ bị sập (crash) hoặc hiện trống trên UI nếu thiếu các key như `status`, `refs`, `chars`, `bg`, `picked` (mọi `sfs`), `text`/`vpicked` (mọi `shots`). Dù giá trị rỗng hoặc null, phải giữ đúng khung mẫu bên trên. Riêng `text` không được để rỗng — đây là nội dung thật (nguyên văn thoại/narration), không phải field app tự điền.
- Khi user yêu cầu "Tạo một dự án mới", in ra khung JSON chuẩn với Scene `REF` trống để user xác nhận, hoặc lưu tự động vào file `sf-board.json`.

## 10. Kiểm tra

**Đếm được:**
- [ ] Mọi thẻ/shot có `id` đúng cú pháp ở §3 — đặc biệt nhịp phải là `-B<n>` **sau** số thứ tự shot, không phải `V-S1-B1`; shot chèn vào board đã có media dùng hậu tố dính liền (`V-HOOK-03B`), không đánh lại số.
- [ ] Mọi SF trong `sfs` xếp đúng thứ tự thời gian; không Master nào bị gom lên đầu.
- [ ] Mọi `shots` xếp đúng thứ tự thời gian, khớp với thứ tự các SF mà chúng trỏ tới.
- [ ] Số mã `sf` khác nhau **bằng đúng** số shot của scene (§5.2).
- [ ] Mỗi SF có **≤4 nhân vật chính** và **≤8 thẻ ref nhân vật** (thẻ neo bối cảnh phụ không tính).
- [ ] Prompt thẻ địa điểm / Master SF **≤1.400 ký tự**; SF thường **<1.000 ký tự**.
- [ ] Mọi `REF_BG_*` và mọi `SF-*` kết thúc bằng đúng dòng `KHUNG NGANG 16:9`.
- [ ] Mọi thẻ `_FULL` có dòng `Dùng: S… · S…` ở cuối `desc`.
- [ ] Không thẻ nào thiếu key `status` / `refs` / `chars` / `bg` / `picked`; không shot nào thiếu key `text` / `vpicked`.
- [ ] Mọi `shot.text` có nội dung thật, đúng nguyên văn và đúng thứ tự Thoại/Narration như kịch bản gốc (không đảo thứ tự — luật đầy đủ: `1-kich-ban.md` §2.2).

**Phải đọc mới thấy:**
- [ ] Mọi SF thường trỏ `refs.bg` về đúng Master SF của cụm mình, không trỏ thẳng thẻ địa điểm.
- [ ] Không SF nào mồ côi (không shot nào trỏ tới), và không hai shot nào dùng chung một giá trị `sf` (§5.2).
- [ ] Mọi người lọt nón quan sát đều có ref; không ai trong prompt mà vắng ở `pose`/`goc`.
