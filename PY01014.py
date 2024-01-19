# Chia hết cho K
# Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
# a + b ≤ N
# a + b chia hết cho K
# Input
# Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).
# Output
# Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.
# Nếu không tìm được số nào in ra -1

a,k,n = map(int,input().split())  
b = []  # Khởi tạo danh sách b để lưu các số thỏa mãn điều kiện
st = k -(a%k)  # Tính giá trị khởi đầu của b dựa trên a và k
end = n - a  # Tính giá trị kết thúc của b dựa trên a và n
while st<=end:  # Lặp cho đến khi giá trị khởi đầu vượt quá giá trị kết thúc
    b.append(str(st))  # Thêm giá trị khởi đầu vào danh sách b
    st+=k  # Tăng giá trị khởi đầu lên k
if(len(b)==0):  # Nếu danh sách b rỗng
        print(-1)  
else: 
    print(' '.join(b))  # In ra danh sách b, các số cách nhau bởi dấu cách



