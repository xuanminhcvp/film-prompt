# Bước 1 — Bảng shot và sinh SF 1:1

> **Nguồn sự thật duy nhất** cho việc nối shot, đếm thời lượng và logic không gian. Lập BẢNG SHOT trước khi sinh prompt.

## Mục lục
- [Luật Cốt Lõi: 1 Shot = 1 SF](#luật-cốt-lõi-1-shot--1-sf)
- [Quy tắc viết `goc`](#quy-tắc-viết-goc)
- [Góc Máy (Coverage)](#góc-máy-coverage)
- [Chia Thoại và Thời Lượng](#chia-thoại-và-thời-lượng)
- [Continuity (Không gian liên tục)](#continuity-không-gian-liên-tục)
- [Nhịp Không Thoại (Chuyển Cảnh)](#nhịp-không-thoại-chuyển-cảnh)
- [Tinh Chỉnh Thoại & Xử Lý Kịch Bản](#tinh-chỉnh-thoại--xử-lý-kịch-bản)
- [Kiểm tra cuối bước](#kiểm-tra-cuối-bước)

---

## Luật Cốt Lõi: 1 Shot = 1 SF
- **BẮT BUỘC**: Số SF = số shot. Tên SF = mã shot (VD: `SF-S1-07`).
- Shot cùng góc máy vẫn sinh hai SF khác nhau về biểu cảm/tay/câu đóng băng theo beat.
- Lập bảng shot trước (Mã shot | Thoại | Số từ | Giây | Góc | Có kết clip). Kiểm tra sạch bằng script RỒI mới sinh prompt ảnh.

## Quy tắc viết `goc`
Dòng `goc` trả lời câu hỏi "Khung này quay bằng góc gì, có ai, nét hay mờ?". Bắt buộc có cho mọi SF. Viết cùng lúc sinh SF ban đầu.
> **Lưu ý**: Dòng `goc` này sinh ra cùng SF, nhưng nó sẽ được dùng làm **tiêu chuẩn khung hình** cho Video Shot trên timeline.
1. **Nêu đích danh**, không đếm số lượng (VD: *"Everett trái + Warren phải, CẢ HAI RÕ MẶT"*).
2. **OTS phải nêu rõ VAI CỦA AI** làm tiền cảnh.
3. **Đúng tên nhân vật** như trong kịch bản.
4. **Khai cả người KHÔNG phải chủ thể** (đang ngồi im/ngủ trong `pose.who` cũng phải khai).
5. **KHÔNG tả cảnh/đạo cụ/thông số máy quay** (cỡ cảnh, tiêu cự ống kính 35mm...) trong dòng này.
6. **TUYỆT ĐỐI CẤM khai báo nhân vật nền** (nền, quần chúng, khách nền, người đi đường). Dòng này **CHỈ** dành cho MAIN CAST. 

## Góc Máy (Coverage)
- **Tỷ lệ**: ~75-80% shot là Cận (CU) và Trung (MCU).
- **Góc rộng**: Chỉ dùng mở/khép/chuyển cảnh (1-2 góc/scene). KHÔNG gán thoại vào khung rộng. Nếu có >3 người, thêm 1 góc rộng vừa (chưa tới mức mở cảnh).
- **OTS (Qua vai)**: Bắt buộc dùng làm shot thoại chính. Một trạng thái gánh ≥3 shot thì BẮT BUỘC có cụm OTS/reverse.
- **Không dùng góc cực đoan**: Chỉ dùng trong những trường hợp đặt biệt cần như là mở cảnh/ lấy góc/ lấy bối cảnh (nhưng cũng hạn chế thôi).

## Chia Thoại và Thời Lượng
- **Cắt theo phản ứng**: Shot cắt sang mặt người nghe khi phản ứng của họ là nội dung chính.
- **Lấp kín thời lượng**: ~90% shot dài 10s (chứa 2-4 lượt thoại qua lại). 10s cần 21-30 từ. 6s (12-18 từ) dùng cho câu ngắn/nhịp chuyển. Chừa dư tối đa 3s.
- **Quy tắc khung thoại (≥2 người)**: Mặc định khung nên có ≥2 người (kể cả khung OTS). Khung 1 người chỉ dùng cho thoại nội tâm/monologue/điện thoại.
- **Xử lý Thoại O.S (Điện thoại / Loa / Gọi vọng)**: AI sinh video tự cấp giọng O.S rất tệ. Ta phải mồi một "bản sao" có người thật đứng nói để lấy chuẩn Voice.
  - *Với Gọi Điện Thoại*: Ví dụ lặp câu thoại của B 2 lần. Video 1: A nói, B nói off-screen (Giữ O.S y như kịch bản gốc để tạo nhịp diễn/thời lượng). Video 2 ngay dưới (Bản sao): SF ( SF chuẩn của B cầm điện thoại áp tai) riêng tả B đang NÓI LẠI CHÍNH XÁC CÂU ĐÓ.
  - *Với Loa phát / Lộ đoạn ghi âm / Gọi vọng*: Video 1: Nhịp không thoại kịch câm (Đám đông/ nhân vật ngơ ngác nghe ngóng/ cảm xúc lúc đó, KHÔNG ai nói O.S). Video 2: SF ( SF của chuẩn nhân vật đó nói) đặc tả chính nhân vật đang thốt ra câu thoại đó (Có thể là cảnh họ cầm micro, đứng gọi từ xa, hoặc cảnh rò rỉ trong quá khứ lúc họ bị lén ghi âm, chuẩn theo cảm xúc nói đúng lúc đó).
- **Chuyển động**: Cộng thêm 2-3s (hoặc hơn) vào thời lượng shot nếu có di chuyển, đứng/ngồi, đi khỏi khung.

## Continuity (Không gian liên tục)
SF là KHUNG ĐẦU clip, nên phải lấy TRẠNG THÁI KẾT THÚC của clip liền trước.
- **Quy tắc TRẠNG THÁI CHỜ (Pending State)**: Nếu trong shot có hành động thay đổi trạng thái tĩnh (mở cửa, đứng lên, ngồi xuống, đưa đồ), KHUNG ĐẦU clip (SF) phải ở trạng thái CHƯA THỰC HIỆN.
- **Rà 5 trục liên tục**: Xa/gần, Trên/dưới (đứng/ngồi), Trước/sau, Trái/phải (trục 180°), **TAY CẦM GÌ** (đặc biệt các món có vai trò kịch bản).
- **Shot TRƯỚC di chuyển**: Trong prompt phải có đoạn KẾT CLIP, và SF của shot đó phải THẤY RÕ MẶT người sắp di chuyển (không để họ quay lưng tiền cảnh).
- **Mối nối nhảy `zone` / `who`**: Bắt buộc phải vá bằng MỘT TRONG BA CÁCH SAU (tùy ngữ cảnh): (1) Dùng một Shot CHUYỂN (Nhịp lặng), hoặc (2) Cho nhân vật vừa đi vừa nói (nếu nhịp phim cho phép), hoặc (3) Tả bước di chuyển ngắn ở CUỐI prompt shot trước.
- **Tối đa 3 mối chuyển/scene**. Đổi góc máy thì rẻ, nhưng bắt nhân vật đi lại đổi `zone` là đắt và dễ khựng.

## Nhịp Không Thoại (Nhịp Lặng & Chuyển Cảnh)
Nhịp không thoại CŨNG LÀ MỘT SHOT (SF). BẮT BUỘC phải sinh ra một dòng SF độc lập trong Bảng Shot cho mỗi nhịp lặng.
- **Tên Nhãn (Label)**: Phải gắn tag `[NHỊP]` hoặc `🎬 NHỊP LẶNG` vào tên nhãn.
- **Mã Shot (ID)**: BẮT BUỘC phải kết thúc bằng hậu tố `-B<số>` cho CẢ mã Shot Video và mã SF (Ví dụ: `V-S1-B1` và `SF-S1-B1`). Tuyệt đối không dùng số thứ tự thường (như `05`, `06`) cho nhịp lặng.
Rà mối nối giữa 2 scene VÀ các điểm rơi cảm xúc ở giữa cảnh.
1. **GIỮA CẢNH (Nhịp thở & Cao trào cảm xúc)**: Bắt buộc chèn vào giữa các chuỗi thoại dài để kéo dãn nhịp độ HOẶC làm nổi bật các điểm cảm xúc cao trào.
2. **MỞ CẢNH / TOÀN CẢNH**: Đầu scene sau (giới thiệu chỗ mới) hoặc Cuối scene trước. KHÁC địa điểm -> bắt buộc có nhịp lặng.
3. **CẦU NỐI**: Cuối cảnh trước/Đầu cảnh sau (nhảy thời gian/địa điểm).
- **Định mức**: Nhịp lặng chiếm khoảng **12%** tổng số shot của toàn phim. **Cho phép** xếp 2 cảnh không thoại liên tiếp nhau, thậm chí 3 cảnh liên tiếp ở 1-2 phân đoạn đặc biệt trong kịch bản để đẩy cảm xúc lên cao trào ( user sẽ ghép nhạc cho đoạn đó). Không bắt buộc phải luôn xen kẽ thoại.

## Xử Lý Kịch Bản
- **Tôn trọng kịch bản gốc**: TUYỆT ĐỐI KHÔNG tự ý sửa đổi, thêm bớt, hay cắt gọt thoại của nhân vật. Mọi câu chữ phải được giữ nguyên vẹn 100% như kịch bản cung cấp.
- **Kịch bản viết sẵn hard-cut trong 1 clip**: (Ví dụ: `0-5s: cảnh A, 5-10s: cắt cảnh B`). BẮT BUỘC phải tách thành 2 shot, 2 SF riêng biệt. Tuyệt đối không dựng hard-cut bên trong 1 clip video duy nhất. Báo lại user về việc tách.

## Kiểm tra cuối bước
- [ ] Chạy lệnh máy đếm: `kiem-luat.py` và `kiem-noi-shot.py` (pose continuity).
- [ ] Diff text với kịch bản gốc: Mọi câu chữ phải được giữ nguyên vẹn, không được tự ý lược bỏ.
- [ ] Người đang nói phải xuất hiện trong khung (rõ mặt hoặc vai/gáy OTS).
- [ ] Bộ góc máy đảm bảo luật 30° / 2 bậc giữa các shot liền nhau.
