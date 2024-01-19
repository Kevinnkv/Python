

# Loại bỏ dấu cách thừa và tách thành danh sách các từ
words = input().split()

# Chuyển đổi chữ in hoa thành chữ thường (ngoại trừ chữ cái đầu tiên của mỗi từ)
normalized_words = [word.capitalize() for word in words]

# Kết hợp các từ thành xâu ký tự 
# chuẩn hóa
normalized_text = ' '.join(normalized_words)

print(normalized_text)
