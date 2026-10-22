Python 3.13.15 (tags/v3.13.15:4061bc4, Aug  5 2026, 13:05:39) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
==== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python313/main.py ===
=== KẾT QUẢ CHẠY 5 CA KIỂM TRA ===

Ca 1: Danh sách rỗng:
  Input: []
  IDs được chọn (Tham ăn): [] (Số lượng: 0)
  Kiểm tra hợp lệ: ĐÚNG
  Tối ưu nhất (Duyệt tập con): [] (Số lượng: 0)

Ca 2: Một hoạt động:
  Input: [(2, 5)]
  IDs được chọn (Tham ăn): [1] (Số lượng: 1)
  Kiểm tra hợp lệ: ĐÚNG
  Tối ưu nhất (Duyệt tập con): [1] (Số lượng: 1)

Ca 3: Ba hoạt động chạm đầu mút:
  Input: [(1, 2), (2, 3), (3, 4)]
  IDs được chọn (Tham ăn): [1, 2, 3] (Số lượng: 3)
  Kiểm tra hợp lệ: ĐÚNG
  Tối ưu nhất (Duyệt tập con): [1, 2, 3] (Số lượng: 3)

Ca 4: Hoạt động dài bắt đầu sớm vs hoạt động ngắn:
  Input: [(0, 10), (1, 2), (2, 3)]
  IDs được chọn (Tham ăn): [2, 3] (Số lượng: 2)
  Kiểm tra hợp lệ: ĐÚNG
  Tối ưu nhất (Duyệt tập con): [2, 3] (Số lượng: 2)

Ca 5: Hai hoạt động cùng thời điểm kết thúc 4:
  Input: [(1, 4), (2, 4), (4, 5)]
  IDs được chọn (Tham ăn): [1, 3] (Số lượng: 2)
  Kiểm tra hợp lệ: ĐÚNG
  Tối ưu nhất (Duyệt tập con): [1, 3] (Số lượng: 2)
