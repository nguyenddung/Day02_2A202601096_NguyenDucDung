# 01 — Individual Problem Scan

## Dự án đề xuất: TalentScreen AI

> Trợ lý tuyển dụng và nhân sự sàng lọc CV, đề xuất ứng viên phù hợp, để HR quyết định cuối cùng.

## 1. Scan rộng: 8 vấn đề có thể quan sát

| # | Lăng kính | Problem quan sát được | Ai chịu ảnh hưởng? | Dấu hiệu thật |
|---|---|---|---|---|
| 1 | Lặp lại | HR phải đọc và sàng lọc hàng trăm CV mỗi đợt tuyển dụng | HR/TA/Hiring Manager | Mỗi vòng tuyển dụng mất 2–5 giờ chỉ để lọc ban đầu |
| 2 | Tốn thời gian | So sánh thông tin trên CV với mô tả công việc để quyết định có phù hợp hay không | HR | Mỗi ứng viên mất khoảng 10–15 phút để đánh giá |
| 3 | AI có thể tốt hơn | CV thường được gửi ở nhiều định dạng, nên việc trích xuất dữ liệu và phân loại kỹ năng khó thống nhất | HR | Dễ bỏ sót kỹ năng quan trọng hoặc chấm không nhất quán |
| 4 | Pain từ người khác | Hiring Manager thường hỏi lại: “Ứng viên này có đủ phù hợp không?” vì bản tóm tắt từ HR chưa đủ rõ | Hiring Manager, HR | Phải trao đổi lại nhiều vòng trước khi phỏng vấn |
| 5 | Lặp lại | Viết email follow-up, phản hồi và note cho từng ứng viên là việc lặp lại mỗi ngày | HR | Cần nhiều thời gian cho việc chuẩn hóa phản hồi |
| 6 | Tốn thời gian | Ghi chú kết quả vào ATS hoặc spreadsheet và cập nhật trạng thái ứng viên | HR/TA | Mỗi ứng viên mất 5–10 phút để nhập dữ liệu |
| 7 | AI có thể tốt hơn | Tóm tắt thông tin từ CV, LinkedIn, portfolio và email để đề xuất câu hỏi phỏng vấn | Recruiter | Nguồn thông tin rời rạc, khó nhìn tổng thể trong vài phút |
| 8 | Pain từ người khác | Một số ứng viên cung cấp thông tin thiếu rõ ràng, dẫn đến HR phải hỏi lại nhiều lần | HR, ứng viên | Tạo thêm vòng trao đổi không cần thiết |

### Vì sao phần scan này có giá trị

- Nó bắt đầu từ pain thật và workflow hiện tại, không bắt đầu bằng “xây chatbot”.
- Có cả vấn đề lặp lại, tốn thời gian và phù hợp để dùng AI hỗ trợ.
- Các vấn đề đều có actor rõ và có thể đo được bằng thời gian hoặc số vòng làm lại.

## 2. Top 3 problem cards

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc |
|---|---|---|---|
| 1 | Sàng lọc CV thủ công và chấm mức độ phù hợp | Workflow rõ, impact lớn, dễ đo bằng thời gian và độ nhất quán | Cần giới hạn phạm vi để không trở thành “AI đọc hết CV toàn diện” |
| 2 | Tóm tắt thông tin ứng viên từ nhiều nguồn | Có nhiều nguồn dữ liệu, AI có thể hỗ trợ tốt | Cần kiểm tra độ chính xác của thông tin và nguồn dữ liệu |
| 3 | Gợi ý câu hỏi phỏng vấn và scorecard cho từng ứng viên | Có thể dùng workflow + agent nhẹ, impact rõ với HR | Cần cân bằng giữa hỗ trợ và kiểm soát chất lượng |

## 3. Problem Card #1 — Sàng lọc CV thủ công

**Problem 1 câu:**  
HR mất nhiều thời gian để đọc từng CV, so sánh với mô tả công việc và chấm mức độ phù hợp, dẫn tới vòng tuyển dụng chậm và đánh giá không nhất quán.

**Ai chịu ảnh hưởng?**  
HR/TA và Hiring Manager chịu tác động trực tiếp.

**Thời điểm / bối cảnh:**  
Mỗi khi mở một đợt tuyển dụng mới, đặc biệt khi số lượng CV tăng đột biến.

**Workflow hiện tại:**
1. Nhận CV từ các kênh tuyển dụng.
2. Đọc lướt CV, LinkedIn hoặc portfolio.
3. So sánh thông tin với JD.
4. Ghi chú và chấm điểm thủ công vào sheet/ATS.
5. Chọn ứng viên để phỏng vấn hoặc loại bỏ.
6. Gửi phản hồi cho Hiring Manager.

**Bottleneck:**  
Bước 2–4: đọc, phân loại và chấm điểm thủ công là phần tốn thời gian nhất và dễ bị chủ quan.

**Impact:**  
Mỗi vòng tuyển dụng có thể mất 2–5 giờ chỉ cho bước sàng lọc ban đầu. Nếu không chuẩn hóa, độ nhất quán của đánh giá giảm và Hiring Manager phải hỏi lại nhiều lần.

**Success metric:**  
- Giảm thời gian sàng lọc từ 3–5 giờ xuống còn dưới 1 giờ cho 100 CV.
- Tăng độ nhất quán giữa HR và Hiring Manager.
- Không làm tăng số ứng viên phù hợp bị loại nhầm.

**Non-AI alternative:**  
Checklist chấm điểm, template đánh giá chuẩn, quy tắc trong ATS. Những phương án này giúp giảm lỗi định dạng, nhưng chưa giải quyết tốt việc đọc và tóm tắt CV linh hoạt.

**AI hypothesis:**  
AI có thể trích xuất thông tin từ CV, đối chiếu với JD, gợi ý mức độ phù hợp và lý do ngắn gọn để HR review. Người thật vẫn giữ vai trò quyết định cuối cùng.

**Quick gut:**  
Workflow.

### Draft current workflow

```text
CURRENT STATE — 3–5 giờ cho 100 CV

[1 Nhận CV] → [2 Đọc và phân loại CV] → [3 So sánh JD] → [4 Chấm điểm thủ công] → [5 Chọn ứng viên] → [6 Gửi feedback]
```

### Draft future workflow

```text
FUTURE STATE — dưới 1 giờ cho 100 CV

[1 Auto-import CV] → [2 AI trích xuất thông tin và đối chiếu JD] → [3 AI đề xuất score + lý do] → [4 HR review và chỉnh sửa] → [5 Chọn ứng viên để phỏng vấn]
```

**Fallback:** Nếu AI đề xuất sai hoặc thiếu ngữ cảnh, HR có thể bỏ qua đề xuất và tự quyết định.

## 4. Problem Card #2 — Tóm tắt thông tin ứng viên từ nhiều nguồn

**Problem 1 câu:**  
HR phải tổng hợp thông tin từ CV, LinkedIn, portfolio và email để hiểu rõ hơn về ứng viên, nhưng quá trình này rất rời rạc và mất thời gian.

**Actor:**  
HR và recruiter.

**Current workflow:**
1. Đọc CV.
2. Đọc thêm LinkedIn hoặc portfolio.
3. Tóm tắt điểm mạnh, điểm yếu và kinh nghiệm.
4. Ghi vào note hoặc sheet.

**Bottleneck:**  
Việc chuyển từ nhiều nguồn dữ liệu rời rạc sang một bản tóm tắt có cấu trúc.

**Impact:**  
Tăng thời gian chuẩn bị trước buổi phỏng vấn và làm chậm quy trình review.

## 5. Problem Card #3 — Gợi ý câu hỏi phỏng vấn và scorecard

**Problem 1 câu:**  
Sau khi xem CV, HR thường phải tự nghĩ câu hỏi phỏng vấn và tiêu chí chấm điểm cho từng ứng viên, dẫn tới việc đánh giá thiếu nhất quán.

**Actor:**  
HR và Hiring Manager.

**Current workflow:**
1. Đọc CV.
2. Xác định kỹ năng cần kiểm tra.
3. Viết câu hỏi phỏng vấn thủ công.
4. Chấm điểm và trao đổi với Hiring Manager.

**Bottleneck:**  
Bước viết câu hỏi và tiêu chí chấm điểm theo từng ứng viên.

**Impact:**  
Tăng công sức chuẩn bị và dễ làm mất chuẩn mực trong phỏng vấn.

## 6. Lựa chọn cá nhân

Trong ba vấn đề trên, tôi chọn “sàng lọc CV thủ công và chấm mức độ phù hợp” làm vấn đề chính vì nó có:

- Actor rõ và workflow dễ vẽ.
- Bottleneck rõ ràng: đọc, đối chiếu và chấm điểm thủ công.
- Impact có thể đo bằng thời gian và mức độ nhất quán.
- Có thể dùng Rule / Workflow / Agent một cách vừa đủ, thay vì build quá lớn.

Bản thân tôi thấy đây là bài toán phù hợp để thử một giải pháp hỗ trợ AI, nhưng vẫn giữ HR ở vị trí quyết định cuối cùng.
    