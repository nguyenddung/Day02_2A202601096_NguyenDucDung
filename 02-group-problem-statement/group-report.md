# Group Report — Day 02

## Thành viên nhóm

| STT | Họ và tên | Mã học viên | Vai trò trong nhóm |
|-----|-----------|-------------|--------------------|
| 1   | Dũng      |             | Người đề xuất vấn đề về xét học bổng và tóm tắt hồ sơ |
| 2   | Đạt       |             | Người đề xuất vấn đề về tổng hợp tài liệu và soạn giáo án |
| 3   | Minh      |             | Người đề xuất vấn đề về đối soát giao dịch và ghi biên bản họp |
| 4   | Hưng      |             | Người đề xuất vấn đề về giảm thời gian chờ khám và quản lý chi tiêu |
| 5   | Tình      |             | Người đề xuất vấn đề về chấm viết bài và phản hồi học tập |
| 6   | Hoàng Anh |             | Người đề xuất vấn đề về sàng lọc CV tuyển dụng và nhập dữ liệu thủ công |

## 1. Group convergence từ các candidate trong Excel

Nhóm thống nhất rằng các vấn đề được đề xuất có một mẫu chung: người thực hiện phải đọc nhiều tài liệu/thông tin rời rạc, so sánh với tiêu chí và đưa ra quyết định hoặc ghi chú. Đây là mẫu phù hợp để dùng AI hỗ trợ vì AI có thể làm tốt phần trích xuất, tóm tắt và đề xuất sơ bộ, trong khi con người vẫn giữ vai trò xác nhận.

| Cluster | Candidate từ các thành viên | Điểm chung |
|---|---|---|
| Sàng lọc hồ sơ / ứng viên | Dũng: xét học bổng; Hoàng Anh: sàng lọc CV tuyển dụng | Đọc nhiều tài liệu, đối chiếu tiêu chí, cần xếp hạng và shortlist |
| Tóm tắt và chuẩn hóa thông tin | Dũng: tóm tắt hồ sơ; Tình: phân tích bài viết | Chuyển dữ liệu rời rạc thành bản tóm tắt có cấu trúc |
| Giảm thao tác thủ công | Minh: đối soát giao dịch; Hoàng Anh: nhập dữ liệu hóa đơn | Các bước lặp lại, nhiều thao tác nhập thủ công |
| Tăng tốc phản hồi | Tình: chấm bài viết; Đạt: tổng hợp tài liệu | Cần phản hồi nhanh nhưng vẫn phải đảm bảo chất lượng |

### Vấn đề được chọn

Nhóm chọn vấn đề: “AI hỗ trợ sàng lọc và xếp hạng hồ sơ theo tiêu chí, từ đó giảm thời gian đọc và tăng độ nhất quán trong đánh giá”.

Vì sao chọn bài này:
- Có actor rõ: chuyên viên/phòng CTSV/HR/hội đồng xét.
- Có workflow rõ và lặp lại nhiều lần.
- Có bottleneck cụ thể: đọc hồ sơ thủ công, so sánh với tiêu chí, ghi chú và chấm điểm.
- Dễ đo bằng thời gian và mức độ nhất quán.
- Phù hợp với cách dùng AI: hỗ trợ trích xuất và đề xuất, không thay thế quyết định cuối cùng của người dùng.

## 2. Shortlist và scoring nhanh

| Candidate | Actor rõ | Workflow rõ | Pain có evidence | Impact đo được | Phù hợp với lab | Có thể dùng Rule/Workflow/Agent | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sàng lọc hồ sơ theo tiêu chí | 5 | 5 | 5 | 5 | 5 | 5 | 30 |
| Tổng hợp báo cáo tuần | 4 | 4 | 4 | 4 | 4 | 4 | 24 |
| Chấm bài viết và phản hồi | 4 | 4 | 4 | 4 | 4 | 4 | 24 |

## 3. Quick validation

Nhóm rà soát lại các đề xuất trong Excel và nhận thấy một tín hiệu chung rất rõ:
- 2 đề xuất có cùng bottleneck: đọc hồ sơ/dữ liệu thủ công rồi chấm/so sánh với tiêu chí.
- Các bước này lặp lại ở nhiều bối cảnh khác nhau: xét học bổng, tuyển dụng, đánh giá hồ sơ.
- Nếu chỉ dùng template hoặc checklist, vấn đề về đọc và tóm tắt hồ sơ vẫn chưa được giải quyết triệt để.

Kết luận sau validation:
- Pain thật không nằm ở việc “nhập dữ liệu”, mà ở việc “đọc và biến nhiều tài liệu thành quyết định có căn cứ nhanh hơn”.
- Vì vậy nhóm thu hẹp scope từ “AI đọc toàn bộ hồ sơ” thành “AI hỗ trợ trích xuất thông tin, tóm tắt và đề xuất xếp hạng sơ bộ, người xét review cuối cùng”.

## 4. Research giải pháp

Nhóm tìm các hướng đã có sẵn để tránh nghĩ trong chân không và không bắt đầu bằng việc “xây chatbot toàn năng”.

| Nguồn / hướng có sẵn | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---|---|---|---|
| Hệ thống quản lý hồ sơ / ATS | Có cấu trúc dữ liệu và workflow rõ | Thường chỉ quản lý thông tin, chưa tự đọc và tóm tắt tài liệu | Cần thêm lớp AI để xử lý tài liệu không cấu trúc |
| Công cụ trích xuất thông tin từ PDF/CV | Giúp phân tích nội dung nhanh | Dễ sai khi định dạng khác nhau | AI nên dùng để đề xuất, không tự quyết định tuyệt đối |
| Công cụ chấm điểm theo rubric | Giúp chuẩn hóa tiêu chí | Không tự nhiên hiểu ngữ cảnh toàn diện | Cần kết hợp rubric + tóm tắt + lý do đề xuất |
| Hệ thống AI hỗ trợ review nội dung | Tốt cho tóm tắt và gợi ý | Có thể hallucinate hoặc bỏ sót chi tiết | Người thật vẫn phải xác nhận trước khi quyết định |

### Research takeaway

Giải pháp phù hợp nhất không phải là “một agent tự xử lý toàn bộ quy trình”, mà là một workflow gồm:
1. Trích xuất dữ liệu từ tài liệu.
2. So sánh với tiêu chí.
3. Đề xuất xếp hạng và lý do ngắn gọn.
4. Người xét review và quyết định cuối cùng.

## 5. Workflow trước/sau

### Trước

1. Mở từng hồ sơ/PDF/CV.
2. Đọc nội dung và so sánh với tiêu chí.
3. Ghi chú thủ công hoặc nhập vào bảng chấm điểm.
4. Họp hoặc tranh luận để thống nhất.
5. Chốt shortlist.

### Sau

1. Tải lên nhiều hồ sơ cùng lúc.
2. AI trích xuất thông tin và tóm tắt theo cấu trúc.
3. AI đối chiếu với tiêu chí và đề xuất mức độ phù hợp.
4. Người xét rà soát kết quả và chỉnh sửa nếu cần.
5. Xuất shortlist và lưu lại lý do đánh giá.

### Metric mục tiêu

| Metric | Trước | Sau mục tiêu |
|---|---:|---:| 
| Thời gian đọc và so sánh mỗi hồ sơ | 5–10 phút | ≤3 phút |
| Thời gian thống nhất chấm điểm giữa các người xét | Cao, có thể mất nhiều giờ | Giảm ít nhất 50% |
| Tỷ lệ bỏ sót hồ sơ phù hợp | Có thể xảy ra | Giảm rõ rệt nhờ kiểm tra AI hỗ trợ |
| Độ nhất quán trong xếp hạng | Thay đổi giữa người xét | Tăng nhờ rubric và đề xuất chuẩn hóa |

## 6. Problem Statement v0

| Field | Nội dung |
|---|---|
| Actor | Chuyên viên phòng CTSV, HR hoặc thành viên hội đồng xét hồ sơ. |
| Problem | Việc đọc, so sánh và chấm điểm hồ sơ thủ công mất nhiều thời gian và dễ thiếu nhất quán. |
| Context | Mỗi đợt xét hồ sơ có số lượng tài liệu lớn và cần phải xử lý nhanh. |
| Metric | Giảm thời gian xử lý hồ sơ, tăng tính nhất quán và giảm sai sót khi chấm điểm. |
| Boundary | Không phải giải quyết toàn bộ quy trình tuyển dụng hay học bổng, mà chỉ tập trung vào bước sàng lọc và xếp hạng sơ bộ. |

## 7. Problem Statement v1

Trong quy trình xét hồ sơ học bổng hoặc tuyển dụng, chuyên viên và hội đồng cần một hệ thống hỗ trợ đọc hồ sơ, trích xuất thông tin quan trọng, đối chiếu với tiêu chí và đề xuất xếp hạng sơ bộ. Mục tiêu là giảm thời gian xử lý hồ sơ, tăng độ nhất quán trong đánh giá và giúp người xét tập trung vào các hồ sơ có khả năng phù hợp cao. Người thật vẫn giữ quyền quyết định cuối cùng.

## 8. Rule / Workflow / Agent

### Rule
- Dùng bộ tiêu chí chuẩn để chấm điểm.
- Luôn yêu cầu AI giải thích lý do đề xuất.
- Không cho AI tự quyết định thay người xét.

### Workflow
- Upload hồ sơ → trích xuất thông tin → tóm tắt ngắn → đối chiếu tiêu chí → đề xuất xếp hạng → người xét kiểm tra.

### Agent
- Có thể dùng agent nhẹ để tự động hỏi thêm thông tin hoặc gợi ý hồ sơ cần xem lại.
- Tuy nhiên, agent không được tự động chốt kết quả mà không có kiểm tra con người.

## 9. Quyết định cuối

### Kết luận
Nhóm chọn phương án “Go with Workflow + Rule, not full agent”.

### Vì sao
- Vấn đề đã đủ rõ và có bottleneck cụ thể.
- AI có thể giúp ở những bước lặp lại nhưng không nên thay toàn bộ vai trò đánh giá của con người.
- Đây là bài toán vừa đủ lớn để có thể demo và phân tích, nhưng không quá rộng để vượt khỏi phạm vi lab.

### Định hướng tiếp theo
- Xây dựng một quy trình hỗ trợ AI nhẹ: tóm tắt hồ sơ, đối chiếu tiêu chí và đề xuất mức độ phù hợp.
- Tập trung vào chất lượng review của con người thay vì cố tạo “AI tự quyết định toàn bộ”.

