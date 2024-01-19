# def shrink_array(n, arr):
#     while True:
#         found = False
#         i = 0
#         while i < n - 1:
#             if (arr[i] + arr[i + 1]) % 2 == 0:
#                 arr.pop(i)
#                 arr.pop(i)
#                 n -= 2
#                 found = True
#             else:
#                 i += 1

#         if not found:
#             break

#     return n

# # Đọc input
# n = int(input())
# arr = list(map(int, input().split()))

# # Gọi hàm và in kết quả
# result = shrink_array(n, arr)
# print(result)
n=int(input())
a=(list(map(int,input().split())))
i=1;
while i<len(a):
    if(a[i-1]+a[i]) %2==0:
        a.pop(i)
        a.pop(i-1)
        if i>1:
            i-=1
    else: i+=1
print(len(a))