# THUMBNAIL — AVA — CÔ GÁI Ở TRỤ BƠM SỐ BỐN

> Golden reference cho bước 9 (`references/12-thumbnail.md`).
> Phim này **chưa dựng `sf-board.json`** — golden project số 4 chỉ chuẩn hoá ba thứ: **title · kịch bản · prompt thumbnail lấy từ kho mẫu**.
> Đây là ví dụ chuẩn cho tình huống *"user chỉ xin prompt thumb, chưa qua bảng shot"*.

---

## 1. Title

```
Cops Threatened a Black Woman at a Gas Station — Then Found Out She Was Undercover FBI
```
94 ký tự · đúng một dấu `—` · hai mệnh đề · dạng REVEAL.

**Luật rút ra từ ca này:** thumbnail phải bám **vế 1** của title (`Cops Threatened a Black Woman at a Gas Station`) và **giấu sạch vế 2** (`Undercover FBI`). Vế 2 là cú lật — lộ ở ảnh bìa thì video hết lý do để xem.
→ Khung ảnh phải đọc ra đủ bốn thứ của vế 1: **nhiều cảnh sát (số nhiều)** · **đang đe doạ/áp chế** · **một phụ nữ da đen** · **trạm xăng ban đêm**.
→ Khung ảnh phải **không có** một dấu hiệu nào của vế 2: không van giám sát, không áo gió FBI, không phù hiệu liên bang, không đặc vụ.

---

## 2. Prompt thumbnail chuẩn (bản user đã duyệt)

Nguồn: **`sfboard/thumbnail-templates.json` — nhóm `Cảnh sát`, hàng 4** (keywords: `cảnh sát`, `bắt giữ`, `còng tay`).
Lượt tra: **lượt 1 — theo bối cảnh + tình huống** (`12-thumbnail.md` §6.1).

```bash
python3 sfboard/tim-thumbnail.py "cảnh sát" "còng tay"
```

```text
[Ảnh chân thực, cực kỳ chi tiết, phong cách nhiếp ảnh chuyên nghiệp, tỷ lệ 16:9, siêu sắc nét, khuôn mặt thật, ánh sáng sáng rõ, không chữ, không watermark]

Dùng ảnh tham khảo thật kỹ. Ảnh A là Ava Greer: giữ đúng gương mặt, da nâu sẫm, gò má cao, tóc xoăn tự nhiên cắt rất ngắn ôm đầu, một khuyên tai nhỏ, dáng người thon chắc, áo khoác field jacket vải bông màu xanh olive mặc mở, bên trong áo thun cotton xám nhạt, quần tối màu, và thần thái bình tĩnh. Ảnh B là Deputy Lyle Brandt: giữ đúng gương mặt, đàn ông da trắng lớn tuổi, thân hình to nặng, bụng đầy, tóc dày màu xám nâu chải ngược, ria mép rậm màu xám, áo sơ mi đồng phục màu kaki nâu nhạt, khoác ngoài áo jacket đồng phục màu xanh navy gần đen có phù hiệu SHERIFF trên tay áo, ngôi sao cảnh sát mạ vàng trên ngực trái, thắt lưng công vụ đen đầy đủ dụng cụ. Ảnh C dùng để tham chiếu biểu cảm cảnh sát đang chế giễu, giữ đúng cảm giác cười lớn, khinh miệt. Không lấy chữ trong ảnh tham khảo.

Góc máy low-angle medium shot, máy quay đặt thấp hơn tầm mắt, lùi vừa đủ để thấy toàn bộ tình huống. Bố cục chia rõ hai phía: hai phó cảnh sát phản diện đứng ở khoảng 4/10 bên trái khung hình, Ava Greer đứng ở khoảng 6/10 bên phải khung hình. Một phó cảnh sát thứ ba đứng ngay phía sau Ava, áp sát người cô, giữ chặt cánh tay cô để tạo áp lực. Không có ô tô dân sự nào khác trong khung ngoài chiếc sedan sẫm màu của Ava đỗ tại trụ bơm số bốn. Ngay phía sau các nhân vật là 2 xe tuần tra quận màu trắng-đen đỗ chéo trên sân trạm, đèn xanh đỏ nhấp nháy rõ ràng. Khung hình thấy rõ 2 xe tuần tra, vài nhân chứng và toàn bộ trạm xăng 24 giờ ven xa lộ, nhưng khuôn mặt nhân vật chính vẫn đủ lớn và rõ cảm xúc.

Cảnh diễn ra dưới mái che của một trạm xăng 24 giờ ven đường liên bang vào lúc gần nửa đêm. Ánh sáng là dàn đèn LED trắng gắt gắn trên trần mái che, chiếu thẳng xuống từ trên cao, toàn cảnh phải sáng rõ, trong, sạch, sắc nét, không tối, không xỉn màu. Ánh trắng lạnh từ mái che kết hợp ánh sáng vàng ấm hắt ra từ ô kính lớn của cửa hàng tiện lợi phía sau, in rõ mặt các nhân vật. Đèn xanh đỏ từ 2 xe tuần tra phía sau nhấp nháy và phản chiếu trên các trụ bơm xăng, nắp capo xe sedan còn ẩm sương, tủ đá lạnh màu xanh dựng cạnh cửa hàng, huy hiệu cảnh sát và mặt bê tông sạch. Bên ngoài mái che là bóng đêm đặc và đường xa lộ tối. Hình ảnh phải bright, crisp, high visibility, thấy rõ da mặt, nếp áo, huy hiệu, xe cảnh sát, vòi bơm và bề mặt sân bê tông.

Ava Greer đúng 36 tuổi, phụ nữ da đen, da nâu sẫm, gương mặt sắc nét, điềm tĩnh, từng trải, ánh mắt bình thản và tự trọng. Cô có vóc dáng thon chắc, tóc xoăn tự nhiên cắt rất ngắn ôm sát đầu, một khuyên tai nhỏ. Cô mặc áo khoác field jacket xanh olive mở, áo thun xám nhạt bên trong, quần tối màu, giày thể thao tối màu. Trên cổ tay trái là một chiếc đồng hồ đàn ông cũ, mặt to, dây da nâu nứt và khâu lại. Hai tay bị còng phía trước bằng còng số 8 bạc, cổ tay có vết hằn nhẹ. Cô đứng thẳng, vai mở, không dựa vào xe, biểu cảm điềm tĩnh không sợ hãi, nhìn thẳng vào viên cảnh sát phản diện chính.

Deputy Lyle Brandt đúng 48 tuổi, đàn ông da trắng, thân hình to nặng, mặt vuông đầy đặn, tóc dày xám nâu, ria mép rậm màu xám, vẻ mặt ngạo mạn. Ông đứng bên trái khung hình, một tay cầm đèn pin kim loại đen chỉ về phía Ava, cười lớn đầy khinh miệt.

Phó cảnh sát quận thứ hai, Deputy Cody Ferris, đúng 32 tuổi, đàn ông da trắng, dáng gọn, tóc nâu ngắn, vẻ mặt hả hê. Anh ta đứng cạnh Brandt, cười chế giễu và giơ điện thoại quay Ava.

Phó cảnh sát thứ ba đúng 34 tuổi, đàn ông da trắng, thân hình chắc. Anh ta đứng phía sau Ava, một tay giữ chặt cánh tay cô, tạo cảm giác kiểm soát và đe dọa. Anh ta cũng đang cười lớn.

Cả 3 phó cảnh sát mặc đồng phục giống hệt nhau như ảnh tham khảo: áo sơ mi đồng phục màu kaki nâu nhạt, khoác ngoài jacket đồng phục xanh navy gần đen, ngôi sao cảnh sát mạ vàng trên ngực trái, bảng tên nhỏ, bộ đàm gắn trước ngực, phù hiệu SHERIFF trên tay áo, thắt lưng đen đầy đủ dụng cụ, quần đồng phục tối màu, giày boots đen bóng. Không dùng kiểu đồng phục khác.

Phía xa có 5 nhân chứng đứng gần cửa hàng tiện lợi và rìa sân trạm, gồm một nhân viên trực đêm khoảng 20 tuổi mặc áo polo đồng phục đứng cạnh cửa kính giơ điện thoại quay video với vẻ mặt căng thẳng, một tài xế xe tải trung niên đứng cạnh trụ bơm đối diện đã dừng tay bơm xăng và quay hẳn người nhìn về phía tiền cảnh, hai hành khách đứng cạnh một chiếc pickup ở rìa sân và một người đàn ông lớn tuổi cầm cốc cà phê; tất cả đã ngừng việc đang làm và đang dõi theo Ava, không ai nhìn vào camera.

Trọng tâm cảm xúc: sự sỉ nhục công khai giữa đêm khuya, cảnh sát quận ngạo mạn cậy sắc phục, người chứng kiến đứng nhìn, Ava vẫn bình tĩnh và đầy khí chất quyền lực ẩn giấu của một đặc vụ liên bang mười hai năm nghề.

Tránh lỗi: thiếu một trong 3 phó cảnh sát, chỉ có 1 xe tuần tra, xe tuần tra không bật đèn xanh đỏ, ảnh tối, màu xỉn, sai gương mặt, sai tuổi, sai đồng phục, đồng phục không đồng bộ, sai giới tính nhân vật chính, méo mặt, méo tay, thừa ngón, mờ, ít chi tiết, máu, bạo lực quá mức, phong cách hoạt hình.

KHÔNG chữ, KHÔNG watermark, KHÔNG logo, KHÔNG vòng tròn đỏ, KHÔNG mũi tên.
KHUNG NGANG 16:9
```

---

## 3. Lấy từ kho ra như thế nào

**Bước 1 — đọc khoảnh khắc, rút hai từ khoá.**
Khoảnh khắc chọn từ Hook: cảnh sát quận áp chế Ava tại trụ bơm giữa đêm. Hai từ khoá rút ra là **bối cảnh/vai** (`cảnh sát`) và **hành động** (`còng tay`).

**Bước 2 — chạy lượt 1 (theo bối cảnh + tình huống).**
```bash
python3 sfboard/tim-thumbnail.py "cảnh sát" "còng tay"
```
Script chấm điểm: trùng tag **+3** · trong tên nhóm **+2** · trong thân prompt **+1**, trả về 2 mẫu cao điểm nhất.
Kết quả: `Cảnh sát | Hàng 4` và `Cảnh sát | Hàng 2`.

**Bước 3 — kiểm "cùng thế trận", không chỉ cùng bối cảnh.**
Hàng 4 khớp cả hai:
- cùng loại bối cảnh: ngoài trời, công khai, có xe tuần tra bật đèn, có người nền chứng kiến;
- cùng thế trận: **nhiều cảnh sát áp đảo một người da đen đứng thẳng**, có người thứ ba giữ tay từ phía sau, đám đông nhìn.
→ Hợp lệ ở lượt 1, **không cần chạy lượt 2**.

**Bước 4 — cụm nhiều chữ phải để trong ngoặc kép.** Gõ rời `còng tay` thì script tách thành `còng` và `tay`, mà `tay` có mặt ở gần như mọi mẫu → kết quả vô nghĩa.

**Bước 5 — nếu cả hai lượt không ra mẫu khớp thế trận/tư thế thì báo user, tuyệt đối không bịa "template" thay thế.**

---

## 4. Thay đổi những gì — bảng đối chiếu với mẫu gốc

Luật: `12-thumbnail.md` §6.3 — **chỉ được thay hai phần: nhân vật và bối cảnh. Mọi thứ còn lại giữ nguyên văn.**

| Thành phần của mẫu `Cảnh sát · Hàng 4` | Xử lý | Kết quả trong prompt này |
|---|---|---|
| Dòng mở đầu `[Ảnh chân thực, …]` | **giữ nguyên văn** | y hệt |
| Khối "Dùng ảnh tham khảo thật kỹ… Ảnh A / Ảnh B / Ảnh C" | **thay người, giữ cấu trúc** | Ảnh A = Ava Greer, Ảnh B = Deputy Brandt, Ảnh C vẫn là ảnh tham chiếu biểu cảm chế giễu |
| Góc máy, bố cục, tỉ lệ 4/10 – 6/10, cảnh sát thứ ba giữ tay từ sau, số xe tuần tra | **giữ nguyên văn** | y hệt, chỉ đổi tên nhân vật và đổi "lối xe vào biệt thự" thành "sân trạm" |
| Kiểu ánh sáng (hướng từ trên cao, hard light, high visibility, đèn xanh đỏ phản chiếu) | **giữ nguyên kiểu** | giữ nguyên hướng + độ gắt; **đổi nguồn sáng theo bối cảnh mới**: hoàng hôn vàng ấm + đèn hiên nhà → đèn LED trắng gắt của mái che + ánh vàng hắt từ vách kính cửa hàng |
| Bối cảnh (biệt thự colonial, Briarcliff Estates, cuối chiều) | **thay** | trạm xăng 24 giờ ven xa lộ, gần nửa đêm |
| Vật nền bám bối cảnh cũ (cửa garage trắng, hàng rào cây xanh) | **thay bằng vật tương đương** | trụ bơm xăng, tủ đá lạnh xanh, vách kính cửa hàng tiện lợi, sedan ở trụ bơm số bốn |
| Nhân vật chính (Miles Armstrong, nam 52, cựu Chuẩn Đô đốc) | **thay người, giữ nguyên tư thế + biểu cảm + hướng nhìn** | Ava Greer, nữ 36, da đen — vẫn "đứng thẳng, vai mở, không dựa vào xe, điềm tĩnh không sợ hãi, nhìn thẳng vào phản diện", vẫn **còng tay phía trước** |
| Phản diện + cảnh sát 2 + cảnh sát 3 | **thay người, giữ nguyên số lượng + hành động** | Brandt (đèn pin, cười khinh miệt) · Ferris (giơ điện thoại quay) · cảnh sát thứ ba (giữ tay từ phía sau) |
| Mô tả đồng phục | **thay theo ảnh ref của phim** | kaki nâu nhạt + jacket navy + phù hiệu SHERIFF + sao vàng, thay cho đồng phục Fairfax County của mẫu |
| Quần chúng nền (6 người, cười nhạo) | **thay người, giữ chức năng** | 5 người: nhân viên trực đêm quay phim, tài xế xe tải đã dừng bơm và quay hẳn người, 2 hành khách, 1 người đàn ông cầm cà phê — **đều đã ngừng việc và đang dõi theo, không ai nhìn camera** |
| Câu "Trọng tâm cảm xúc" | **thay nội dung, giữ vị trí + cú pháp** | sỉ nhục công khai giữa đêm khuya |
| Câu "Tránh lỗi" | **giữ nguyên văn**, chỉ đổi vật thể riêng của mẫu | bỏ "Ford Explorer", còn lại y hệt |
| Câu chặn rác đồ hoạ + `KHUNG NGANG 16:9` | **bổ sung ở cuối** (mẫu chưa có đủ) | hai dòng cuối |

**Không được làm:** rút gọn câu, viết lại cho "hay hơn", thêm ý mới, đổi tỉ lệ chia khung, đổi số nhân vật, sửa file `thumbnail-templates.json`.

---

## 5. Hai chi tiết riêng của ca này — đọc trước khi copy sang phim khác

**(a) Thẻ FULL là nguồn nhân dạng duy nhất.** Hook không có thẻ portrait (`3-ref-nhan-vat.md` §2). Mọi mô tả tuổi/sắc tộc/tóc/màu áo trong prompt lấy từ ảnh ref user gửi và phải khớp 100% — không đổi màu áo hay kiểu tóc cho "ăn ảnh hơn". Áo olive của Ava, áo kaki + jacket navy của Brandt là **khoá nhân dạng**, không phải gợi ý.

**(b) Còng tay hay chưa còng — quyết bởi động từ trong title.**
Title này dùng **`Threatened`**. Nếu bám sát nghĩa đó thì khung phải là *đang đe doạ*: tay Ava buông mở lòng bàn tay, tay Brandt đặt lên báng súng với nắp bao súng đã bật — **không còng**. Bản user duyệt ở §2 vẫn giữ còng tay của mẫu gốc, vì còng tay đọc ra "bị áp chế" mạnh hơn ở kích thước thumbnail nhỏ và cảnh còng tay có thật trong phim.
→ **Luật rút ra:** khi động từ của title và tư thế của mẫu lệch nhau, đây là **điểm duy nhất được phép lệch khỏi §6.3** — và phải hỏi user, không tự quyết.
