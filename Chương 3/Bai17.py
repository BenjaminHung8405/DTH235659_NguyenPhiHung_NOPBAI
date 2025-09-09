# Viết lại đoạn code bằng cách dùng từ khóa break thay thế cho biến done

n, m = 0, 100
while n != m:
    n = int(input())
    print("n =", n)
    if n < 0:
        break
