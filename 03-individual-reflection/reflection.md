# 03 — Individual Reflection

## 1. Vai trò và đóng góp của tôi

Tôi là Nguyễn Đức Dũng, thành viên của nhóm. Trong phần làm việc cá nhân, tôi scan các vấn đề liên quan đến tuyển dụng và xử lý hồ sơ, sau đó chọn bài toán sàng lọc CV/hồ sơ thủ công làm candidate chính. Tôi mô tả workflow hiện tại, xác định bottleneck ở bước đọc, đối chiếu tiêu chí và chấm điểm, đồng thời đề xuất metric về thời gian xử lý và độ nhất quán.

Khi thảo luận nhóm, tôi đóng góp góc nhìn rằng pain chính không phải chỉ là nhập dữ liệu, mà là chuyển nhiều tài liệu rời rạc thành một quyết định có căn cứ. Candidate của tôi giúp nhóm nhận ra điểm chung giữa xét học bổng, tuyển dụng và các bài toán đánh giá hồ sơ. Từ đó, nhóm thu hẹp bài toán thành AI hỗ trợ trích xuất, tóm tắt và đề xuất xếp hạng sơ bộ.

## 2. AI đã hỗ trợ tôi như thế nào

AI hỗ trợ tôi sắp xếp các ý tưởng ban đầu thành Problem Card có cấu trúc: actor, bối cảnh, workflow, bottleneck, impact, metric và phương án không dùng AI. AI cũng giúp gợi ý các cách diễn đạt rõ hơn cho workflow trước/sau và chỉ ra rằng checklist hoặc rule đơn thuần chưa xử lý tốt việc đọc các CV có định dạng, nội dung và ngữ cảnh khác nhau.

Tuy nhiên, AI không thể tự xác nhận rằng các metric hoặc giả định của tôi đúng với mọi quy trình tuyển dụng. Các con số về thời gian xử lý và rủi ro bỏ sót chỉ là giả định để định hướng bài toán; trước khi xây dựng giải pháp, cần kiểm chứng bằng dữ liệu thực tế hoặc trao đổi với HR/recruiter.

## 3. Phần tôi đã tự kiểm và chỉnh sửa

Ban đầu, tôi có xu hướng nghĩ về một công cụ AI có thể đọc toàn bộ CV và tự chọn ứng viên. Sau khi xem lại rủi ro sai lệch, thiếu ngữ cảnh và trách nhiệm trong quyết định tuyển dụng, tôi chỉnh lại phạm vi: AI chỉ trích xuất thông tin, đối chiếu rubric, tóm tắt và đưa ra lý do đề xuất; HR hoặc hội đồng vẫn phải review và quyết định cuối cùng.

Tôi cũng nhận ra rằng không nên chọn Agent chỉ vì bài toán có nhiều bước. Với phạm vi hiện tại, một workflow có rule rõ ràng, đầu ra có cấu trúc và điểm kiểm tra của con người phù hợp hơn một agent tự vận hành. Cách này dễ kiểm soát chất lượng, dễ đo hiệu quả và giảm rủi ro tự động hóa quá mức.

## 4. Điều tôi học được

Điều quan trọng nhất tôi học được là bắt đầu từ pain và workflow thực tế thay vì bắt đầu từ một giải pháp AI. Một bài toán chỉ phù hợp với AI khi actor, bottleneck, tác động, metric và boundary đều rõ. Việc có AI tóm tắt hoặc chấm điểm không tự động tạo ra giá trị nếu tiêu chí đánh giá chưa thống nhất hoặc dữ liệu đầu vào không đáng tin cậy.

Tôi cũng hiểu rõ hơn mạch lập luận của bài lab:

1. Quan sát một vấn đề có người chịu ảnh hưởng và dấu hiệu thật.
2. Vẽ workflow để tìm đúng bước nghẽn.
3. Đặt metric và boundary để tránh giải pháp quá rộng.
4. So sánh No AI, Rule, Workflow và Agent.
5. Chọn mức hỗ trợ AI nhỏ nhất nhưng giải quyết được bottleneck, đồng thời giữ người chịu trách nhiệm trong vòng review.

## 5. Nếu làm lại

Nếu làm lại, tôi sẽ phỏng vấn nhanh ít nhất một HR/recruiter hoặc thu thập mẫu dữ liệu ẩn danh để kiểm chứng ba điểm: thời gian sàng lọc thực tế, tiêu chí nào thường gây bất đồng và tỷ lệ hồ sơ phù hợp có thể bị bỏ sót. Tôi cũng sẽ thử một rubric chấm điểm trên một nhóm CV nhỏ, so sánh kết quả giữa AI và người review, rồi mới đặt mục tiêu metric cuối cùng.

Với bước tiếp theo, tôi vẫn giữ quyết định của nhóm: **Go with Workflow + Rule, not full agent**. Giải pháp cần ưu tiên tính minh bạch, lý do đánh giá và quyền quyết định của HR thay vì cố tự động hóa toàn bộ quy trình.
