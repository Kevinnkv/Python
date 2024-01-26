#DÃY SỐ HAMMING

# Khởi tạo từ điển m với giá trị đầu tiên là 1
m = {1: 1}

# Lặp đến khi không còn số nào mới được thêm vào từ điển
while True:
    # Biến kiểm tra xem có số mới được thêm vào từ điển không
    ok = 0

    # Danh sách a để chứa các số mới cần thêm vào từ điển
    a = []

    # Lặp qua từng số trong từ điển để tạo danh sách các bội số của 2, 3, 5
    for i in m:
        if i < 10**18:
            # Kiểm tra và thêm các bội số vào danh sách a nếu chưa tồn tại
            if not((i * 2) in m):
                a.append(i * 2)
            if not((i * 3) in m):
                a.append(i * 3)
            if not((i * 5) in m):
                a.append(i * 5)

    # Nếu danh sách a không rỗng, thì đặt ok bằng 1 và thêm các số từ danh sách a vào từ điển m
    for i in a:
        ok = 1
        m[i] = 1

    # Nếu không có số mới được thêm vào từ điển, thoát khỏi vòng lặp
    if ok == 0:
        break

# Sắp xếp danh sách a và gán vị trí của các số trong danh sách đã sắp xếp vào từ điển m
p = 1
a = sorted(list(m))
for i in a:
    m[i] = p
    p += 1

# Đọc số lượng bộ test t
t = int(input())

# Đọc và in vị trí của số n trong dãy số Ugly Numbers cho mỗi test case
for i in range(t):
    n = int(input())
    if n in m:
        print(m[n])
    else:
        print("Not in sequence")
