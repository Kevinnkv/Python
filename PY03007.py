# XỬ LÝ VĂN BẢN

import re

def normalize_sentence(sentence):
    # Chuẩn hóa câu: chữ cái đầu viết hoa, các chữ cái khác viết thường
    return sentence.capitalize()

def main():
    # Nhập văn bản và chuyển về dạng chữ thường
    text = input().lower()

    # Tách văn bản thành các câu dựa trên dấu chấm, dấu chấm hỏi và dấu chấm cảm
    sentences = re.split(r'[.!?]', text)

    # Xóa các câu trống và chuẩn hóa các câu
    #sentences = [normalize_sentence(sentence.strip()) for sentence in sentences if sentence.strip()]

    # In ra từng câu trên mỗi dòng
    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()
