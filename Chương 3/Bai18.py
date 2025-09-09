#!/usr/bin/env python3
# Bai18.py - Vẽ 3 hình theo chiều cao n

def hollow_square(n):
	"""In hình vuông rỗng kích thước n x n"""
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i == 1 or i == n or j == 1 or j == n:
				print("*", end=" ")
			else:
				print("  ", end="")
		print()


def right_triangle_diag(n):
	"""In tam giác vuông (cạnh dọc trái) với cạnh đáy và đường chéo"""
	for i in range(1, n+1):
		for j in range(1, i+1):
			# j==1 (cạnh trái), i==n (đáy) hoặc i==j (đường chéo)
			if j == 1 or i == n or i == j:
				print("*", end=" ")
			else:
				print("  ", end="")
		print()


def top_right_triangle_diag(n):
	"""In tam giác vuông có cạnh trên và cạnh phải, kèm đường chéo từ trên phải xuống"""
	for i in range(1, n+1):
		for j in range(1, n+1):
			# i==1 (hàng trên), j==n (cạnh phải) hoặc j == n - i + 1 (đường chéo)
			if i == 1 or j == n or j == n - i + 1:
				print("*", end=" ")
			else:
				print("  ", end="")
		print()


def main():
	try:
		n = int(input("Nhập n (chiều cao, số nguyên >=1): "))
	except ValueError:
		print("Vui lòng nhập một số nguyên hợp lệ.")
		return
	if n < 1:
		print("n phải lớn hơn hoặc bằng 1.")
		return

	print("\nHình 1: Hollow square\n")
	hollow_square(n)

	print("\nHình 2: Right triangle with diagonal\n")
	right_triangle_diag(n)

	print("\nHình 3: Top row + right column + diagonal\n")
	top_right_triangle_diag(n)


if __name__ == "__main__":
	main()
