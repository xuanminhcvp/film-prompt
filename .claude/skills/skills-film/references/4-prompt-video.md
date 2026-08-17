# Bước 4 — Prompt Video

> **Nguồn sự thật duy nhất** cho việc chuyển hóa ảnh tĩnh thành video bằng Grok, tập trung vào chuyển động và biểu cảm.
*(Prompt nhạc Suno nằm ở file riêng: [5-nhac-suno.md](5-nhac-suno.md)).*

## Mục lục
- [Luật Cốt Lõi: 1 Clip = 1 Shot Liền](#luật-cốt-lõi-1-clip--1-shot-liền)
- [Form Prompt Video Chuẩn](#form-prompt-video-chuẩn)
- [Khối KẾT CLIP](#khối-kết-clip)
- [Prompt Nhịp Không Thoại](#prompt-nhịp-không-thoại)
- [Kiểm tra cuối bước](#kiểm-tra-cuối-bước)

---

## Luật Cốt Lõi: 1 Clip = 1 Shot Liền
- Không thể cắt cảnh bên trong 1 clip. Hard-cut trong kịch bản bắt buộc tách thành 2 shot (2 SF).
- Câu khóa *"Một shot liền <N> giây, không chuyển cảnh."* chỉ nằm ở dòng đầu tiên, KHÔNG lặp lại ở footer.

## Form Prompt Video Chuẩn
**Dùng ĐÚNG form này, không thêm bớt khối nào.** 
```text

Nhận diện:
- <Tên A> = <mô tả tuổi, sắc tộc, quần áo> 
- <Tên B> = <mô tả tuổi, sắc tộc, quần áo>
Trong khung: <Mô tả chính xác ai RÕ MẶT, ai bị MỜ/QUAY LƯNG/CHỈ THẤY VAI GÁY tuỳ theo đúng ảnh SF thực tế>. <nếu chỉ thấy Vai và gáy thì không được quay mặt lại, vì quay mặt lại sẽ bị tạo ra nhân vật khác>. (TUYỆT ĐỐI CẤM chêm thêm các câu thừa thãi như "Ngoài những người đã nêu, không thêm ai khác vào khung" hay "Không ai khác lọt khung").

Một shot liền <N> giây, không chuyển cảnh. Camera <TĨNH / PUSH-IN chậm / DOLLY ngang nhẹ...>. TUYỆT ĐỐI KHÔNG để Camera lùi, kéo lùi hay PULL-OUT.

<Mô tả hành động của người nói trước/trong khi thoại>:

<TÊN NÓI> — <nhãn cảm xúc tiếng Anh, vd: quiet, firm>: "<thoại tiếng Anh nguyên văn>"

<TÊN NGƯỜI NGHE> — silent, <nhãn cảm xúc tiếng Anh, vd: listening intently, frowning>

Âm thanh: CHỈ thoại nhân vật, tiếng Anh giọng Mỹ, rõ lời. Không âm nền. Không nhạc, không narrator, không phụ đề. MỘT SHOT LIỀN DUY NHẤT suốt cả video — tuyệt đối KHÔNG chuyển cảnh, KHÔNG cắt. Không thêm, xóa, thay thế hoặc nhân bản nhân vật.

KẾT CLIP: <CHỈ viết khi shot sau đổi trạng thái>
```
- **Khối `Nhận diện`**: BẮT BUỘC trình bày dạng gạch đầu dòng, mô tả ngắn gọn nhân dạng (tuổi, giới tính, sắc tộc, màu áo).
- **Khối `Trong khung`**: 
  - Khung OTS -> BẮT BUỘC viết: *"<B> chỉ thấy VAI VÀ GÁY... TUYỆT ĐỐI KHÔNG quay mặt về camera"* (Không được viết "Cả hai rõ mặt").
  - Phải mô tả ĐÚNG với ảnh thực tế đã render.
- **Camera**: Chỉ được dùng TĨNH, PUSH-IN, PAN, DOLLY ngang. Tuyệt đối không dùng lệnh lùi (Pull-out, Kéo lùi).
- **Cảm xúc**: Hành động và tính từ phải nhẹ nhàng/hợp lý (vd: không viết "quát", trẻ em gặp người lớn thì ghi bỡ ngỡ chứ không ghi giật mình sợ hãi). 

## Khối KẾT CLIP < 7% số shot của phim
**CẢNH BÁO LẠM DỤNG**: CHỈ `< 7%` số shot của phim thật sự cần khối kết clip.

**1. Định luật Bảo toàn Image-to-Video (TỐI QUAN TRỌNG)**
Video sinh ra từ MỘT BỨC ẢNH tĩnh duy nhất. Nếu ảnh SF hiện tại KHÔNG CÓ nhân vật A hay đạo cụ X, hay vật thể Y, video không thể đẻ ra cái đó được. 
- **Cách viết ĐÚNG**: Chỉ viết từ những vốn liếng đang có sẵn trong SF hiện tại, không bịa ra một cái mà SF hiện tại không có.
- **TUYỆT ĐỐI CẤM**: Lấy trạng thái của shot kế tiếp kéo về bắt shot hiện tại phải vẽ thêm trong khi shot hiện tại không có (Ví dụ: Bắt "A bước vào" trong khi SF hiện tại không hề có hình bóng A ở trong khung).

**2. Bốn (04) Dạng Hành Động trong khối kết clip Hợp Lệ Nhất (White-list)**
Cấm tự phát minh hành động. Chỉ được phép dùng 4 dạng sau:
- **Dạng 1 (Đổi tư thế)**: Chủ thể trong ảnh tự thay đổi (từ ngồi thành đứng dậy, quỳ thành đứng).
- **Dạng 2 (Đạo cụ tại chỗ)**: Đưa tay lấy/ném/thả một vật *đã hiện diện sẵn* trong khung ảnh.
- **Dạng 3 (Bước đi/Rời khỏi khung - Exit Frame)**: Một chủ thể quay lưng đi hoặc bước đi/ bước ra khỏi màn hình.

**3. Khi nào TUYỆT ĐỐI KHÔNG viết KẾT CLIP (Sẽ làm rác prompt)**
- **Đổi góc máy**: Không có nhu cầu nối raccord.
- **Quy mô quá tham lam**: Hễ có từ 2 thao tác nối nhau trở lên (VD: Lấy ván -> bắc ván -> đẩy xe), BẮT BUỘC phải tạo thành khối NHỊP KHÔNG THOẠI riêng. KẾT CLIP chỉ dùng cho MỘT thao tác đơn giản.
- **Phản bội Lời thoại**: Hành động trong kết clip mâu thuẫn với ý câu thoại (VD: Thoại vừa nói "Tôi sẽ ngồi im đây" thì tuyệt đối không được viết KẾT CLIP bảo họ đứng dậy bỏ đi).

## Prompt Nhịp Không Thoại
- **Mật độ**: ≈ 12% tổng shot có thoại của TOÀN PHIM. Thường đặt ở chỗ giao scene (cuối và đầu scene) hoặc cao trào im lặng. **Cho phép** xếp 2 cảnh không thoại liên tiếp nhau, hoặc thậm chí 3 cảnh liên tiếp (khoảng 1-2 lần trong toàn kịch bản) nếu chuỗi hành động hoặc cảm xúc cao trào đòi hỏi kéo dài. 
- **3 loại nhịp giao scene**: 
  1. **MỞ CẢNH**: Đầu cảnh sau (Báo nơi chốn + giờ).
  2. **TOÀN CẢNH**: Cuối cảnh trước (Khép cảnh cảm xúc). Tỷ lệ không gian/người CHÍNH LÀ nội dung.
  3. **CẦU NỐI**: Nối cảnh, báo nhảy thời gian/địa điểm (Dolly theo nhân vật). Luôn dừng TRƯỚC hành động cảnh sau.
- **Form nhịp không thoại**:
  - Phải có: `KHÔNG CÓ LỜI THOẠI TRONG CLIP NÀY. Tuyệt đối không ai mở miệng...`
  - `Âm thanh`: Cấm nhạc/thoại, NHƯNG CHO PHÉP ambient/SFX môi trường ở mức nhẹ (tiếng dế, gió, bước chân).
  - **Khối Cảm Xúc**: Viết **TRẠNG THÁI**, đừng viết list thao tác cử chỉ. Nêu rõ: *Nhân vật vừa trải qua gì? Nội tâm ra sao?* Kèm *Gợi ý diễn biến* để model bám nhưng TỰ CHỌN cử chỉ cho hợp lý.
- **Luật chuyển động**: Mọi sự di chuyển phải có TÁC NHÂN trong khung ảnh (người, gió, xe). Soi theo ảnh SF thật, không soi theo prompt cũ. Không cài ẩn dụ phức tạp ở nhịp chuyển. KHÔNG mặc định thở dài.

## Kiểm tra cuối bước
- [ ] Không có khối nào thừa ngoài form chuẩn. Không tả lại tuổi/quần áo/nhân dạng.
- [ ] Khối `Trong khung` mô tả đúng thứ ảnh cho thấy.
- [ ] Khối KẾT CLIP đặt đúng chỗ, dư thời gian diễn.
- [ ] Người thoại luôn có mặt (ngoại trừ qua điện thoại/loa).
- [ ] Mọi nhịp không thoại có vai trò rõ ràng, kèm đủ 2 prompt Suno (tại file `5b`).
