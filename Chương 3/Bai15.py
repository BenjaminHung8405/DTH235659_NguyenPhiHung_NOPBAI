print("Câu 15: Giải thích cách chạy các dòng lệnh range")

print("\n(a) range(5):", list(range(5)))
print("Giải thích: Tạo dãy số từ 0 đến 4 (5 phần tử), bước 1 mặc định.")

print("\n(b) range(5, 10):", list(range(5, 10)))
print("Giải thích: Tạo dãy số từ 5 đến 9 (5 phần tử), bước 1 mặc định.")

print("\n(c) range(5, 20, 3):", list(range(5, 20, 3)))
print("Giải thích: Tạo dãy số từ 5 đến 19, bước 3 (5, 8, 11, 14, 17).")

print("\n(d) range(20, 5, -1):", list(range(20, 5, -1)))
print("Giải thích: Tạo dãy số từ 20 đến 6, bước -1 (giảm dần).")

print("\n(e) range(20, 5, -3):", list(range(20, 5, -3)))
print("Giải thích: Tạo dãy số từ 20 đến 8, bước -3 (giảm dần: 20, 17, 14, 11, 8).")

print("\n(f) range(10, 5):", list(range(10, 5)))
print("Giải thích: Tạo dãy từ 10 đến 5, bước 1 mặc định. Vì 10 > 5 và bước dương, dãy rỗng.")

print("\n(g) range(0):", list(range(0)))
print("Giải thích: Tạo dãy từ 0 đến -1, dãy rỗng.")

print("\n(h) range(10, 101, 10):", list(range(10, 101, 10)))
print("Giải thích: Tạo dãy số từ 10 đến 100, bước 10 (10, 20, 30, ..., 100).")

print("\n(i) range(10, -1, -1):", list(range(10, -1, -1)))
print("Giải thích: Tạo dãy số từ 10 đến 0, bước -1 (giảm dần: 10, 9, ..., 0).")

print("\n(j) range(-3, 4):", list(range(-3, 4)))
print("Giải thích: Tạo dãy số từ -3 đến 3 (7 phần tử), bước 1 mặc định.")

print("\n(k) range(0, 10, 1):", list(range(0, 10, 1)))
print("Giải thích: Tạo dãy số từ 0 đến 9 (10 phần tử), bước 1.")
