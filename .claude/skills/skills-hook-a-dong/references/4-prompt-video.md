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

Một shot liền <N> giây, không chuyển cảnh. Camera <PUSH-IN chậm / DOLLY IN chậm / TĨNH / PULL-OUT chậm>. (Lưu ý Hook: 92% shot là chuyển động Push-in/Dolly-in chậm để tăng kịch tính; Tĩnh chỉ chiếm 8% cho điểm lặng).

<Mô tả NHIỆM VỤ / MỤC ĐÍCH của nhân vật (Tránh tả hành động cơ học cụ thể. Hãy tả mục đích để AI tự tận dụng vật thể có sẵn trong ảnh)>:

<TÊN NÓI> — <nhãn cảm xúc tiếng Anh, vd: quiet, firm>: "<thoại tiếng Anh nguyên văn>"

<TÊN NGƯỜI NGHE> — silent, <nhãn cảm xúc tiếng Anh, vd: listening intently, frowning>

<QUẦN CHÚNG NỀN> (nếu có) — <mô tả hành động nền nhẹ nhàng, vd: murmuring softly, shifting weight, subtle natural movements> (Bắt buộc phải tả nhẹ để quần chúng không bị đơ cứng như tượng gỗ).

Âm thanh: 
- Cảnh thoại trực tiếp: CHỈ thoại nhân vật, tiếng Anh giọng Mỹ, rõ lời. Không nhạc, không narrator.
- Cảnh có Câu Dẫn Chuyện (Narration): Lời dẫn (Voiceover) sẽ được ghép sau. Nhân vật diễn kịch câm, CHỈ ĐƯỢC PHÉP có âm nền (ambient) nhẹ HOẶC phản ứng âm thanh ngắn không lời (thở mạnh, hừ, cười khẽ qua mũi, hít vào bất ngờ) để tránh nhân vật bị đơ cứng như tượng gỗ. Tuyệt đối không để nhân vật mấp máy môi đọc lời dẫn (phản ứng âm thanh ngắn KHÁC với việc đọc lời thoại).
  - **Trường hợp đặc biệt (Nhân vật đang thực hiện HÀNH ĐỘNG NÓI)**: Nếu Narrator kể về HÀNH ĐỘNG NÓI của chính nhân vật trong khung (gọi điện, phát biểu, gọi to...): KHÔNG mặc định câm hoàn toàn. Hãy thêm một câu thoại NGẮN do bạn tự chế, KHÔNG tiết lộ nội dung cốt truyện (giữ bí mật cho twist) hoặc để âm thanh lời nói bị nghe không rõ (do khoảng cách/tiếng ồn môi trường) — miễn nhân vật thực sự phát ra âm thanh khớp hành động đang làm trên hình.
  - **Đặc trưng Hook đối với Phản diện**: Ở nhịp dẫn chuyện mà phản diện là chủ thể RÕ MẶT, ưu tiên cho họ một cử chỉ/phản ứng âm thanh thể hiện thái độ (đắc thắng, khinh miệt, tự mãn) thay vì đứng yên trung tính. Thậm chí **ĐƯỢC PHÉP chế thêm một câu thoại ngắn** cho phản diện nói để khán giả ghét hơn — đây là cơ hội vàng để xây dựng sự căm ghét. (Lưu ý: Tuyệt đối bỏ qua điều này nếu phản diện chỉ là khối mờ tiền cảnh/quay lưng ở góc OTS, tránh tranh giành trọng tâm của khung hình).
MỘT SHOT LIỀN DUY NHẤT suốt cả video — tuyệt đối KHÔNG chuyển cảnh, KHÔNG cắt. Không thêm, xóa, thay thế hoặc nhân bản nhân vật.

KẾT CLIP: <CHỈ viết khi shot sau đổi trạng thái>
```
- **Khối `Nhận diện`**: BẮT BUỘC trình bày dạng gạch đầu dòng, mô tả ngắn gọn nhân dạng (tuổi, giới tính, sắc tộc, màu áo).
- **Nhiệm vụ / Mục đích**: Thay vì mô tả hành động tay chân cụ thể (vd: "lấy cốc nước trên bàn rồi uống"), hãy mô tả mục đích/trạng thái (vd: "đang làm việc nhà một cách uể oải", "tìm cách giải tỏa căng thẳng"). Điều này giúp AI tự tận dụng các vật thể ĐÃ CÓ SẴN trong khung hình, tránh tình trạng AI "ảo giác" tự vẽ ra đồ vật lạ lặp đi lặp lại khi prompt ép một hành động cụ thể.
- **Camera (Đặc trưng Hook & Start-frame rule)**: TUYỆT ĐỐI không bắt AI vẽ không gian mới. Chủ yếu dùng PUSH-IN chậm, DOLLY IN chậm (chiếm 92%). Góc TĨNH chỉ dùng cực hiếm (8%) ở các nhịp lặng cần thiết.
- **Cảm xúc**: Hành động và tính từ phải nhẹ nhàng/hợp lý (vd: không viết "quát", trẻ em gặp người lớn thì ghi bỡ ngỡ chứ không ghi giật mình sợ hãi). 
- **Đồng bộ chuẩn 100% thứ tự và nguyên văn thoại/lời dẫn (Kịch bản -> SF -> Video)**: Mảng `shots` trong `sf-board.json` bắt buộc phải xếp đúng thứ tự thời gian tuyến tính 1-1 với mảng `sfs`. Thoại nhân vật và lời dẫn narrator trong video prompt của từng shot phải khớp chính xác 100% nguyên văn với kịch bản gốc và Bảng shot ở Bước 1. TUYỆT ĐỐI KHÔNG bỏ bớt câu text nào, KHÔNG nhảy text linh tinh, và KHÔNG tráo thứ tự giữa các shot.

## Khối KẾT CLIP < 7% số shot của phim
**CẢNH BÁO LẠM DỤNG**: CHỈ `< 7%` số shot của phim thật sự cần khối kết clip.

**1. Định luật Bảo toàn Image-to-Video (TỐI QUAN TRỌNG)**
Video sinh ra từ MỘT BỨC ẢNH tĩnh duy nhất (được trỏ bởi ô `"sf"` trong mảng `shots`).
- **Cách viết Video Prompt chuẩn theo SF gốc**: Video shot này đọc đúng bức ảnh SF được trỏ tới làm Start Frame gốc. Chỉ viết prompt diễn biến/thoại/hành động dựa trên vốn liếng bối cảnh, vị trí và nhân vật đã có sẵn ở SF đó, không bịa ra thứ mà SF đó không có.
- **TUYỆT ĐỐI CẤM**: Lấy trạng thái của shot kế tiếp kéo về bắt shot hiện tại phải vẽ thêm trong khi SF được trỏ tới không có (Ví dụ: Bắt "A bước vào" trong khi SF hiện tại không hề có hình bóng A ở trong khung).

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
- [ ] Khối KẾT CLIP đặt đúng chỗ, dư thời gian diễn.
- [ ] Người thoại luôn có mặt (ngoại trừ qua điện thoại/loa).
- [ ] Mọi nhịp không thoại có vai trò rõ ràng, kèm đủ 2 prompt Suno (tại file `5b`).
