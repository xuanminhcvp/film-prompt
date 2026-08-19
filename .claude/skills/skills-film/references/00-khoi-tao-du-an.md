# Khởi Tạo Dự Án (Project Initialization)

> **Luật cốt lõi**: File này định nghĩa cấu trúc gốc của một dự án làm phim và Schema chuẩn mực của file `sf-board.json`. Bắt buộc dùng file này làm khuôn mẫu (template) khi khởi tạo bất kỳ dự án mới nào để phần mềm UI Board không bị lỗi, KHÔNG phụ thuộc vào việc tìm kiếm các dự án cũ làm mẫu.

## 1. Cấu trúc thư mục dự án
Khi bắt đầu một dự án mới, tạo một thư mục mang tên `<TEN_DU_AN>.project/` ở môi trường làm việc.
Thư mục này BẮT BUỘC chứa 2 file chính:
- `KICH-BAN.md`: Bản kịch bản gốc để con người đọc và AI tham chiếu (TUYỆT ĐỐI KHÔNG tự sửa file này trừ khi có lệnh).
- `sf-board.json`: Database trung tâm chứa toàn bộ thông tin nhân vật, đạo cụ, địa điểm và các shot hình (SF) của phim.

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
Mảng `scenes` bắt buộc luôn bắt đầu bằng một Scene có `id` là `REF` (chứa nhân vật, đạo cụ, bối cảnh), tiếp theo mới đến các Scene của kịch bản (`S1`, `S2`...).
```json
{
  "id": "REF", // Hoặc "S1", "S2"
  "name": "REF — nhân vật · đạo cụ · bối cảnh", // Hoặc "S1 — Tên cảnh"
  "sfs": [
    // ... Chứa các mảng Object của Start Frame (SF)
  ]
}
```

### 2.3 Cấp SF (Start Frame) - Dành cho khung REF
Sử dụng cho các thẻ nhân vật, đạo cụ, bối cảnh (Bên trong scene `REF`).

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

### 2.4 Cấp SF (Start Frame) - Dành cho khung Cảnh quay (Shot)
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
  "prompt": "MÁY QUAY:...\n\nAI VÀ ĐANG LÀM GÌ:...\n\nTAY:...\n\nHƯỚNG NHÌN:...\n\nBIỂU CẢM:...\n\nĐÓNG BĂNG:...",
  "refs": {
    "chars": [
      "REF_TEN_NHAN_VAT_PORTRAIT"
    ],
    "bg": "REF_BG_BOI_CANH"
  },
  "status": "draft"
}
```

## 3. Quy tắc vận hành JSON
- **Cấm tự ý xóa key:** Các phần mềm đọc giao diện JSON Board sẽ bị sập (crash) nếu thiếu các key như `status`, `refs`, `chars`, `bg`. Dù giá trị rỗng hoặc null, phải giữ đúng khung mẫu bên trên.
- **Tuân thủ đúng ID format:** 
  - `REF_<Tên>_<Loại>` cho tham chiếu (VD: `REF_KEISHA_PORTRAIT`, `REF_BG_AISLE_SEVEN`).
  - `SF-<Cảnh>-<Số>` cho shot thực tế (VD: `SF-S1-01`).
- Khi User yêu cầu "Tạo một dự án mới", hãy in ra khung JSON chuẩn với Scene `REF` trống để User xác nhận hoặc lưu tự động vào file `sf-board.json`.
