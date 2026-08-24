# Khởi Tạo Dự Án (Project Initialization)

> **Luật cốt lõi**: File này định nghĩa cấu trúc gốc của một dự án và Schema chuẩn mực của file `sf-board.json`. Bắt buộc dùng file này làm khuôn mẫu (template) khi khởi tạo bất kỳ dự án mới nào để phần mềm UI Board và script `kiem-luat.py` không bị lỗi, KHÔNG phụ thuộc vào việc tìm kiếm các dự án cũ làm mẫu.

## 1. Cấu trúc thư mục dự án
Khi bắt đầu một dự án mới, tạo một thư mục mang tên `<TEN_DU_AN>.project/` ở môi trường làm việc.
Thư mục này BẮT BUỘC chứa 2 file chính:
- `KICH-BAN.md`: Bản kịch bản gốc để con người đọc và AI tham chiếu (TUYỆT ĐỐI KHÔNG tự sửa file này trừ khi có lệnh).
- `sf-board.json`: Database trung tâm chứa toàn bộ thông tin nhân vật, đạo cụ, địa điểm, các ảnh tĩnh (SF) và các shot hình của phim.

---

## 2. Cấu trúc chuẩn (Schema) của `sf-board.json`
Định dạng file phải là chuẩn JSON. Không được phép thiếu các key cốt lõi dưới đây để script `kiem-luat.py` có thể kiểm tra.

### 2.1 Cấp Root
```json
{
  "film": "TÊN PHIM — MÔ TẢ NGẮN (VIẾT HOA)",
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
    // ... Chứa các thẻ Start Frame (SF) định nghĩa tĩnh
  ],
  "shots": [
    // ... (Chỉ xuất hiện ở các scene kịch bản S1, S2...) Chứa định nghĩa video/thoại
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
  "picked": ""
}
```

**B. Thẻ Toàn thân / Trang phục:**
Bắt buộc đính kèm Portrait vào `chars` và có dòng `Dùng:` ở cuối `desc`.
```json
{
  "id": "REF_TEN_NHAN_VAT_FULL_1",
  "label": "TÊN NHÂN VẬT — TRANG PHỤC 1",
  "desc": "Mô tả ý nghĩa bộ đồ.\nDùng: S1 · S2 · S5",
  "prompt": "Ảnh tham chiếu TRANG PHỤC, photorealistic...",
  "status": "proposed",
  "notes": "",
  "usedBy": [],
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
  "notes": "",
  "usedBy": [],
  "refs": {
    "chars": [],
    "bg": null
  }
}
```

**D. Thẻ Bối cảnh / Ánh sáng:**
Phải có hậu tố giờ (VD: `_DEM`, `_SANG`) và trường `prompt`.
```json
{
  "id": "REF_TEN_DIA_DIEM_DEM",
  "label": "TÊN ĐỊA ĐIỂM BAN ĐÊM",
  "desc": "Mô tả địa điểm.",
  "prompt": "ÁNH SÁNG: CHẬP TỐI. Không gian vắng vẻ... (Tối đa 2500 ký tự)",
  "status": "proposed",
  "notes": "",
  "usedBy": [],
  "refs": {
    "chars": [],
    "bg": null
  }
}
```

### 2.4 Cấp SF (Start Frame) - Dành cho khung Cảnh quay (Shot tĩnh)
Nằm trong mảng `sfs` của S1, S2... định nghĩa **Góc máy tĩnh**.
Mỗi ảnh tĩnh không được chứa quá 4 nhân vật. Prompt có 6 khối bắt buộc (MÁY QUAY, AI VÀ ĐANG LÀM GÌ, TAY, HƯỚNG NHÌN, BIỂU CẢM, ĐÓNG BĂNG) và tối đa 1.000 ký tự.
```json
{
  "id": "SF_1_1",
  "label": "Tóm tắt hình ảnh tĩnh",
  "desc": "",
  "prompt": "MÁY QUAY: 35mm, ngang tầm mắt, cách 2m, trung cảnh.\n\nAI VÀ ĐANG LÀM GÌ: Nhân vật đang đứng.\n\nTAY: Hai tay buông thõng.\n\nHƯỚNG NHÌN: Nhìn thẳng vào ống kính.\n\nBIỂU CẢM: Bình tĩnh.\n\nĐÓNG BĂNG: Khoảnh khắc đứng yên.",
  "status": "draft",
  "notes": "",
  "usedBy": [],
  "refs": {
    "chars": [
      "REF_TEN_NHAN_VAT_FULL_1"
    ],
    "bg": "REF_TEN_DIA_DIEM_DEM"
  },
  "pose": {
    "who": {
      "TEN_NHAN_VAT": "trung"
    }
  }
}
```

### 2.5 Cấp Shot - Đoạn video/thoại
Nằm trong mảng `shots` của S1, S2... Trỏ 1:1 tới `sf`.
Trường `dur` là số (float/int). Trường `goc` bắt buộc có để định nghĩa ai đang trong khung hình. Prompt video tối đa 1.400 ký tự.
```json
{
  "id": "S1_1",
  "sf": "SF_1_1",
  "dur": 4.5,
  "text": "[NHỊP] mô tả nhịp\nNARRATOR: <lời dẫn nguyên văn tiếng Anh>",
  "music": null,
  "goc": "TEN_NHAN_VAT trung",
  "prompt": "Mô tả chuyển động cho video... (Không chứa mã REF_ hay Start frame)"
}
```
> **Lưu ý quan trọng về Lời Dẫn (NARRATOR)**: Lời dẫn ghi vào `text` với nhãn `NARRATOR:` (script đã biết bỏ nhãn này khi soát người-nói). TUYỆT ĐỐI KHÔNG ghi lời dẫn vào `prompt` video — Grok sẽ cho nhân vật đọc nó lên.

## 3. Quy tắc vận hành JSON (tương thích kiem-luat.py)
- **Cấm tự ý xóa key**: Các phần mềm đọc giao diện JSON Board sẽ bị sập (crash) nếu thiếu các key như `status`, `refs`, `chars`, `bg`. Dù giá trị rỗng hoặc null, phải giữ đúng khung mẫu bên trên.
- **Tuân thủ đúng ID format**:
  - `REF_<Tên>_<Loại>` cho tham chiếu (VD: `REF_MAYA_PORTRAIT`, `REF_HOSPITAL_DEM`).
  - `SF_<Số>_<Số>` cho shot thực tế (VD: `SF_1_1`).
- **Luật 1:1**: 1 Shot (trong mảng `shots`) chỉ trỏ tới đúng 1 SF. Không dùng chung 1 SF cho 2 shot.
- **Tính toán `dur`**: Độ dài = (số từ / 3) + 2 (nếu là KẾT CLIP). Với shot mang lời dẫn (`NARRATOR:`), tính số từ của lời dẫn để đảm bảo đủ giây đọc (`dur >= số từ / 3 - 0.5`). Phải là kiểu số thực (`float`) hoặc nguyên (`int`).
- **Liên kết pose và goc**: Tên người nói phải có mặt trong `goc` của shot. Tên khai báo trong `pose.who` của SF cũng bắt buộc phải xuất hiện trong `goc`.
- Khi User yêu cầu "Tạo một dự án mới", hãy in ra hoặc ghi trực tiếp khung JSON chuẩn với Scene `REF` trống để User xác nhận hoặc lưu tự động vào file `sf-board.json`.
