import random
import time

def validate_input(s, f):
    """Kiểm tra tính hợp lệ của dữ liệu đầu vào"""
    if len(s) != len(f):
        raise ValueError("Độ dài mảng Start và Finish không bằng nhau.")
    for i in range(len(s)):
        if s[i] < 0 or f[i] < 0:
            raise ValueError("Thời gian không được là số âm.")
        if s[i] > f[i]:
            raise ValueError("Thời gian bắt đầu không được lớn hơn thời gian kết thúc.")
    return True

def activity_selection(s, f):
    """Thuật toán Tham ăn chọn tập các hoạt động không chồng lấp lớn nhất"""
    validate_input(s, f)
    n = len(s)
    if n == 0:
        return []
    
    activities = [(s[i], f[i], i) for i in range(n)]
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0][2]]
    last_finish = activities[0][1]
    
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i][2])
            last_finish = activities[i][1]
            
    return sorted(selected)

def run_tests():
    print("=== BẮT ĐẦU CHẠY TỰ ĐỘNG 12 CA KIỂM THỬ (TC01 - TC12) ===")
    passed = 0
    total = 12

    # TC01
    try:
        s, f = [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]
        res = activity_selection(s, f)
        assert res == [0, 1, 3, 4]
        print("[PASS] TC01: Ca kiểm thử ví dụ cơ bản 1")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC01: {e}")

    # TC02
    try:
        s, f = [10, 12, 20], [20, 25, 30]
        res = activity_selection(s, f)
        assert res == [0, 2]
        print("[PASS] TC02: Ca kiểm thử ví dụ cơ bản 2")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC02: {e}")

    # TC03
    try:
        s, f = [1], [5]
        res = activity_selection(s, f)
        assert res == [0]
        print("[PASS] TC03: Ca kiểm thử 1 hoạt động đơn lẻ")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC03: {e}")

    # TC04
    try:
        s, f = [1, 1, 1], [5, 5, 5]
        res = activity_selection(s, f)
        assert len(res) == 1
        print("[PASS] TC04: Ca kiểm thử tất cả trùng thời gian")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC04: {e}")

    # TC05
    try:
        s, f = [1, 5, 10], [4, 9, 15]
        res = activity_selection(s, f)
        assert res == [0, 1, 2]
        print("[PASS] TC05: Ca kiểm thử chuỗi hoạt động rời nhau")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC05: {e}")

    # TC06
    try:
        s, f = [1, 2, 3, 4], [2, 3, 4, 5]
        res = activity_selection(s, f)
        assert res == [0, 1, 2, 3]
        print("[PASS] TC06: Ca kiểm thử dữ liệu đã sắp xếp sẵn")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC06: {e}")

    # TC07
    try:
        s, f = [3, 1, 0, 5], [4, 2, 6, 7]
        res = activity_selection(s, f)
        assert res == [0, 1, 3]
        print("[PASS] TC07: Ca kiểm thử dữ liệu chưa sắp xếp")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC07: {e}")

    # TC08
    try:
        s, f = [1, 2, 3], [1, 2, 3]
        res = activity_selection(s, f)
        assert res == [0, 1, 2]
        print("[PASS] TC08: Ca biên thời gian bắt đầu bằng kết thúc")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC08: {e}")

    # TC09
    try:
        s, f = [1, 3, 5], [3, 5, 7]
        res = activity_selection(s, f)
        assert res == [0, 1, 2]
        print("[PASS] TC09: Ca biên nối tiếp mốc thời gian")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC09: {e}")

    # TC10
    try:
        s, f = [1, 2], [3]
        try:
            activity_selection(s, f)
            print("[FAIL] TC10: Không bắt được lỗi độ dài")
        except ValueError:
            print("[PASS] TC10: Bắt lỗi lệch độ dài mảng đầu vào")
            passed += 1
    except Exception as e:
        print(f"[FAIL] TC10: {e}")

    # TC11
    try:
        s, f = [5], [2]
        try:
            activity_selection(s, f)
            print("[FAIL] TC11: Không bắt được lỗi start > finish")
        except ValueError:
            print("[PASS] TC11: Bắt lỗi thời gian bắt đầu > kết thúc")
            passed += 1
    except Exception as e:
        print(f"[FAIL] TC11: {e}")

    # TC12
    try:
        random.seed(42)
        s_large, f_large = [], []
        for _ in range(1000):
            st = random.randint(0, 10000)
            ft = st + random.randint(1, 50)
            s_large.append(st)
            f_large.append(ft)
        res = activity_selection(s_large, f_large)
        assert len(res) > 0
        print(f"[PASS] TC12: Ca quy mô lớn n = 1000 (Chọn được {len(res)} hoạt động)")
        passed += 1
    except Exception as e:
        print(f"[FAIL] TC12: {e}")

    print("\n==================================================")
    print(f"KẾT QUẢ KIỂM THỬ: {passed}/{total} TEST CASES PASSED")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
