def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Kiểm tra số nguyên tố")
    while True:
        s = input("Nhập một số nguyên (hoặc 'exit/thoát' để thoát): ").strip()
        if s.lower() in ("exit", "thoát", "thoat"):
            print("Đã thoát chương trình.")
            break
        try:
            n = int(s)
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")
            continue
        if is_prime(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
        cont = input("Tiếp tục? (y/n): ").strip().lower()
        if cont in ("n", "no", "không", "khong", "k", "0", "exit", "thoát", "thoat"):
            print("Kết thúc.")
            break

if __name__ == "__main__":
    main()
