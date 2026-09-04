# 10 — Nhịp không thoại (Nhịp lặng / B-roll)

> **File này trả lời:** trọn đời một shot không thoại — khi nào cần, đặt ở đâu, đặt mã gì, prompt video viết sao, nhạc ra sao.
> **Mở khi:** rà mối nối giữa hai scene, hoặc khi thấy chuỗi thoại quá dài cần kéo giãn.
> **Không chứa:** shot có thoại (→ `7-bang-shot.md`) ·
>   cách viết prompt Suno (→ `12-nhac-suno.md`) ·
>   form prompt video của shot thoại (→ `11-prompt-video.md`)

> **Luật cốt lõi: nhịp không thoại cũng là một shot (SF)**. Bắt buộc sinh ra một dòng SF độc lập trong Bảng Shot cho mỗi nhịp lặng.

## 1. Đặt ở đâu
Rà mối nối giữa 2 scene và các điểm rơi cảm xúc ở giữa cảnh.

1. **Giữa cảnh (nhịp thở & cao trào cảm xúc)**: bắt buộc chèn vào giữa các chuỗi thoại dài để kéo dãn nhịp độ hoặc làm nổi bật các điểm cảm xúc cao trào.
2. **Mở cảnh**: đầu scene sau — giới thiệu chỗ mới, báo nơi chốn + giờ.
3. **Toàn cảnh**: cuối scene trước — khép cảnh cảm xúc. Tỷ lệ không gian/người chính là nội dung.
4. **Cầu nối**: nối cảnh, báo nhảy thời gian/địa điểm (dolly theo nhân vật). Luôn dừng trước hành động cảnh sau.

**Khác địa điểm → bắt buộc có nhịp lặng.**

## 2. Phân loại — dùng khi cần giảm tỷ lệ nhịp vượt trần
1. **Nhịp bắt buộc**: ở mối chuyển địa điểm/không gian (không bao giờ được bỏ).
2. **Nhịp mắt xích kịch bản**: góc đặc tả gài đầu mối (bút E.C., tay gấp túi ngũ cốc, hồ sơ bí mật) — tuyệt đối cấm bỏ.
3. **Nhịp trang trí**: mở/khép cảnh cùng địa điểm — bỏ trước khi cần giảm tỷ lệ.

## 3. Định mức
- Nhịp lặng chiếm khoảng 12–15% tổng số shot của toàn phim. Trần tối đa 18%, mốc đích ~12–15%.
- **Cho phép** xếp 2 cảnh không thoại liên tiếp nhau, thậm chí 3 cảnh liên tiếp ở 1–2 phân đoạn đặc biệt trong kịch bản để đẩy cảm xúc lên cao trào (user sẽ ghép nhạc cho đoạn đó). Không bắt buộc phải luôn xen kẽ thoại.
- ⚠️ *Trước khi tách file, bộ luật cũ tồn tại song song hai bản: "12–15% tổng số shot, trần 18%" và "≈12% tổng shot có thoại" — khác mẫu số. Đã thống nhất về **tổng số shot toàn phim**.*

## 4. Đặt tên & đặt mã
- **Tên nhãn (`label`)**: phải gắn tag `[NHỊP]` hoặc `🎬 NHỊP LẶNG`.
- **Mã**: `SF-S<scene>-<stt>-B<thứ_tự_nhịp>` và `V-S<scene>-<stt>-B<thứ_tự_nhịp>` — **số thứ tự shot trước, rồi mới đến `B`**. Quy tắc đầy đủ và lý do: `2-du-lieu-sf-board.md` §3.

## 5. Neo bối cảnh
**Nhịp chuyển trỏ REF theo cụm nó đứng, không theo scene chứa nó.** Nhịp bắc cầu A→B đứng ở đầu nào thì neo master đầu ấy:
- Quay cảnh ở cụm cũ → neo master cụm cũ (kể cả master ấy nằm ở scene trước).
- Quay cảnh ở cụm mới → neo master cụm mới (kể cả master ấy xuất hiện sau nó trong mạch shot).

**Tuyệt đối không dùng SF Nhịp (SF-B) làm Master SF** (`6-cum-va-master-sf.md` §2.3).

## 6. Prompt video của nhịp
- **Bắt buộc có câu**: `KHÔNG CÓ LỜI THOẠI TRONG CLIP NÀY. Tuyệt đối không ai mở miệng...`
  Và trong khối `LIP SYNC:`: `No character speaks. No character moves their lips as if talking.`
- **Âm thanh**: cấm nhạc/thoại trong clip, nhưng cho phép ambient/SFX môi trường ở mức nhẹ (tiếng dế, gió, bước chân).
- **Khối Cảm Xúc**: viết trạng thái, đừng viết list thao tác cử chỉ. Nêu rõ: *nhân vật vừa trải qua gì? nội tâm ra sao?* Kèm *gợi ý diễn biến* để model bám nhưng tự chọn cử chỉ cho hợp lý.
- **Luật chuyển động**: mọi sự di chuyển phải có tác nhân trong khung ảnh (người, gió, xe). Soi theo ảnh SF thật, không soi theo prompt cũ. Không cài ẩn dụ phức tạp ở nhịp chuyển. Không mặc định thở dài.
- Cấu trúc clip, thang an toàn camera và khối kết clip: `11-prompt-video.md`.

## 7. Nhạc — bắt buộc
- **Mọi nhịp không thoại đều phải có nhạc.** Không được để trống.
- **Mỗi nhịp có đúng 2 phương án (A và B): 1 bản có lời + 1 bản không lời.**
- Hai nhịp cạnh nhau không được cùng vai trò hoặc cùng nhạc cụ dẫn.
- Cách chọn vai trò và viết prompt Suno: `12-nhac-suno.md`.

## 8. Kiểm tra
- [ ] Mỗi nhịp lặng là một dòng SF độc lập, có tag `[NHỊP]` và mã `-B<n>` đúng thứ tự.
- [ ] **Toàn phim:** nhịp lặng chiếm **12–15%** tổng số shot, không vượt trần **18%**.
- [ ] Nhịp bắt buộc ở mọi mối chuyển địa điểm — không thiếu cái nào.
- [ ] Nhịp mắt xích kịch bản còn nguyên, không bị cắt khi giảm tỷ lệ.
- [ ] Mọi nhịp có vai trò rõ ràng, kèm đủ 2 prompt Suno (A có lời + B không lời).
