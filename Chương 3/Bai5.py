i = int(input("Nhập số nguyên i: "))
j = int(input("Nhập số nguyên j: "))
k = int(input("Nhập số nguyên k: "))
if i < j :
    if j < k :
        i = j
    else:
        j = k
else:
    if j > k :
        j = i
    else:
        i = k
print(f"i = {i}, j = {j}, k = {k}")

# Kết quả in ra (theo định dạng chương trình: "i = ..., j = ..., k = ..."):

# (a) i = 3, j = 5, k = 7 → i = 5, j = 5, k = 7
# (b) i = 3, j = 7, k = 5 → i = 3, j = 5, k = 5
# (c) i = 5, j = 3, k = 7 → i = 7, j = 3, k = 7
# (d) i = 5, j = 7, k = 3 → i = 5, j = 3, k = 3
# (e) i = 7, j = 3, k = 5 → i = 5, j = 3, k = 5
# (f) i = 7, j = 5, k = 3 → i = 7, j = 7, k = 3