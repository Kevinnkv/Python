# Tháp Hà Nội
# Chat GPT

def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Di chuyển n-1 đĩa từ cột nguồn (source) sang cột trung gian (auxiliary)
        hanoi(n - 1, source, auxiliary, target)
        
        # In ra bước di chuyển
        print(f"{source} -> {target}")
        
        # Di chuyển n-1 đĩa từ cột trung gian (auxiliary) sang cột đích (target)
        hanoi(n - 1, auxiliary, target, source)

# Nhập số đĩa
n = int(input())

# Gọi hàm để giải bài toán Tháp Hà Nội
hanoi(n, 'A', 'C', 'B')
