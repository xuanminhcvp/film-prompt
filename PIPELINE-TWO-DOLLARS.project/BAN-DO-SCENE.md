# TWO DOLLARS — bản đồ scene → thẻ REF

Lập ở bước 1–2 (2026-08-18). Đây là dữ liệu vào của **bước 3**: mỗi SF sinh ra
phải đính đúng `refs.bg` ghi ở đây và đúng thẻ `_FULL` mà `desc` của nó đã nhận.

## Địa điểm

| Scene | Thẻ `refs.bg` | Ghi chú mối nối |
|---|---|---|
| S1 | `REF_SANNHA_DEM` | Preston chỉ hiện trong ô cửa sổ bếp |
| S2 | `REF_HIENNHA_DEM` | |
| S3 | `REF_BAIXEGARAGE_NGAY` | |
| S4 | `REF_DUONGLAO_NGAY` → `REF_HANHLANGDL_NGAY` → `REF_DUONGLAO_NGAY` | đổi ở `V-S4-B2` và `V-S4-B3` |
| S5 | `REF_BAIXETRAM_DEM` (chỉ `B1`) → `REF_TRAMXANG_DEM` | |
| S6 | `REF_NGANHANG_NGAY` | ô giao dịch THỨ HAI từ trái |
| S7 | `REF_SANHBDS_NGAY` | |
| S8 | `REF_BAIXETRAM_DEM` | **trạm diễn 2** — ở xe bán tải |
| S9 | `REF_NHADIANE_NGAY` | |
| S10 | `REF_XUONG_DEM` | |
| S11 | `REF_HANHLANGTOA_NGAY` | |
| S12 | `REF_BAIXETRAM_DEM` | **trạm diễn 1** — bệ bê tông |
| S13 | `REF_PHONGKHACH_DEM` | |
| S14 | `REF_DUONGLAO_NGAY` | |
| S15 | `REF_HANHLANGBV_DEM` (`B1`–`09`) → `REF_BENHVIEN_DEM` (`B2`–`B3`) | đổi ở `V-S15-B2` |
| S16 | `REF_CAMDO_NGAY` | |
| S17 | `REF_BAIXETRAM_NGAY` | **trạm diễn 1** — bệ bê tông |
| S18 | `REF_BAIXETRAM_DEM` (`B1`–`14`) → `REF_TRAMXANG_DEM` (`B3`–`B4`) | đổi ở `V-S18-B3`; trạm diễn 2 |
| S19 | `REF_SANHDAI_DEM` | |
| S20 | `REF_PHONGKHACH_DEM` | khung TV lấy bố cục của `REF_TRUONGQUAY_DEM` |
| S21 | `REF_TRUONGQUAY_DEM` | |
| S22 | `REF_CUADAI_DEM` | |
| S23 | `REF_VPLUAT_NGAY` | |
| S24 | `REF_TOAAN_NGAY` | |
| S25 | `REF_BENHVIEN_NGAY`; riêng `V-S25-B2` dùng `REF_GARAGEMOI_NGAY` | |

## Giờ theo scene (để rà luật ≤2 scene tối liền)

```
S1 tối · S2 tối · S3 sáng · S4 sáng · S5 tối · S6 sáng · S7 sáng · S8 tối
S9 sáng · S10 tối · S11 sáng · S12 tối · S13 tối · S14 sáng · S15 tối
S16 sáng · S17 sáng · S18 tối · S19 tối · S20 tối · S21 tối · S22 tối
S23 sáng · S24 sáng · S25 sáng
```

⚠ **S18 → S22 là năm scene tối liền nhau.** Đây không phải lỗi dựng: kịch bản gốc
buộc như vậy — quay số, sảnh đài, phát trực tiếp, phòng khách và cửa đài đều nằm
trong CÙNG MỘT ĐÊM, và cắt một cảnh giờ hành chính vào giữa là sửa kịch bản.
`kiem-luat.py` sẽ báo mục này ngay khi bước 3 sinh xong SF; đó là ngoại lệ đã biết,
đừng "chữa" bằng cách đổi thẻ địa điểm.

## Trang phục

Danh sách scene của từng bộ nằm ở dòng `Dùng:` cuối trường `desc` của mỗi thẻ
`REF_*_FULL`. Trước khi bước 3 gắn xong `refs.chars`, `kiem-luat.py` sẽ báo mọi
thẻ là "desc nhận Sx nhưng KHÔNG SF nào đính" — đó là **danh sách việc còn phải
làm**, không phải lỗi dữ liệu. Khi bước 3 xong mà dòng nào còn báo thì mới là lệch thật.

## Ngoại lệ đã biết ở bảng shot

- `V-S25-B2` (nhịp lặng cắt sang xưởng chín khoang) là khung **cố ý không có
  nhân vật chính**. Phép kiểm `goc-không-nêu-ai` sẽ báo shot này khi có SF. Giữ
  nguyên — đây là cú trả cho câu thoại "put your name across the front of it".
- `V-S4-13b` là **BẢN SAO O.S** cho câu bà Ruth gọi vọng từ trong phòng ở
  `V-S4-13`; hai clip cắt xen vào nhau, không phải hai lần thoại.
