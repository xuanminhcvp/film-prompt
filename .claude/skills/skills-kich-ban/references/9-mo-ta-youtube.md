# 9 — Mô tả YouTube

## 1. Nhiệm vụ của mô tả
- Bán khoảng trống cho người lướt.
- Cho thuật toán từ khoá.
- Giữ chân người xem bằng bài học & câu hỏi.
- **Cấm**: Kể lể tuần tự, giải thích ý nghĩa, khen phim.
- **Khác với Hook**: Mô tả NÓI THẲNG cú lật, cấm giấu.

## 2. 11 Khối BẮT BUỘC (Đúng thứ tự)
1. `🎬 + title`: Chép đúng title tiếng Anh đã chốt.
2. **Đoạn cảnh**: 4–6 câu ngắn, kể cảnh mở ở thì hiện tại. Chứa đủ tên, tuổi, giờ, địa điểm, số người. Kết ở lúc kẻ ra đòn bắt đầu hiểu.
3. **Đoạn lật**: 2–3 câu. **Nói thẳng cú lật** (ai, nắm gì, làm gì với nó) — [MỤC TIÊU]. Các khuôn như *What he/she doesn't know —* chỉ là [THAM KHẢO] (ví dụ dùng cho dạng REVEAL).
4. **Đoạn từ khoá**: 1–2 câu, nhồi từ khoá. 1 vế phủ định (*Not a...*), 1 câu chốt tuỳ dạng bài (ví dụ "ai nguy hiểm nhất" chỉ là [THAM KHẢO] cho dạng FIGHT/REVEAL).
5. Vạch ngăn: `━━━`
6. `💡 WHAT THIS STORY TEACHES US`: Tiêu đề.
7. **Ba bài học**: Mỗi bài học là **một dòng**: `✔️` + 1 câu trích nguyên văn từ kịch bản + đúng 1 câu giải thích (≤20 từ).
8. Vạch ngăn: `━━━`
9. `🔔 Subscribe`: 1 câu kêu gọi đăng ký.
10. `💬 Câu hỏi`: 1 câu hỏi liên hệ đời sống khán giả.
11. **Hashtag**: 8-10 thẻ (thể loại trước, thẻ riêng sau).

## 3. Luật viết
- **Số viết bằng chữ**, ngoại trừ mã hiệu.
- **Cấm bịa dữ kiện**: Mọi con số/chi tiết phải trích đúng từ `KICH-BAN.md`.
- **Cấm tính từ tự khen**.
- **Ba bài học**: Rút từ 3 chỗ khác nhau (cái châm ngòi, cái giá, cái cứu vãn). Cấm 3 bài học trùng ý.
- **Phép thử bài học**: Bỏ tên nhân vật đi, nếu câu nói áp dụng được cho mọi chuyện thì đó là sáo ngữ. Bài học phải dính chặt vào đúng phim này.
- **Độ dài**: **1.400–1.500 ký tự** cho toàn bộ mô tả, tính cả title, emoji, vạch ngăn và hashtag. Ba khối đầu (title + đoạn cảnh + đoạn lật) chiếm 50–60%. Thiếu chỗ thì cắt chi tiết phụ ở khối 2–3, không bỏ khối nào.

## 4. Kiểm tra
- [ ] Đủ 11 khối đúng thứ tự, 3 dấu ✔️, 8-10 hashtag, tổng 1.400–1.500 ký tự (chạy `scripts/kiem.py`).
- [ ] Mỗi bài học nằm gọn một dòng: câu trích + 1 câu giải thích ≤20 từ.
- [ ] Title chép đúng 100%.
- [ ] Khối 2 viết thì hiện tại, có: tên, tuổi, giờ, nơi, số người.
- [ ] Khối 3 NÓI THẲNG cú lật.
- [ ] 3 bài học mở bằng câu trích nguyên văn, không trùng ý.
- [ ] Bài học qua được phép thử sáo ngữ.
- [ ] Câu hỏi ở khối 10 gắn với đời khán giả.
- [ ] Số đếm viết bằng chữ.
- [ ] Không có dữ kiện nào ngoài kịch bản.
- [ ] Không tính từ tự khen.
