#!/usr/bin/env python3
"""Bai19.py - Tính S(x,n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!"""
import math


def S(x, n):
    total = 0.0
    for k in range(0, n+1):
        p = 2*k + 1
        total += x**p / math.factorial(p)
    return total


def main():
    try:
        x = float(input("Nhập x: "))
        n = int(input("Nhập n (số nguyên không âm): "))
    except ValueError:
        print("Giá trị nhập không hợp lệ.")
        return
    if n < 0:
        print("n phải là số nguyên không âm.")
        return

    result = S(x, n)
    print(f"S(x,n) = {result}")


if __name__ == "__main__":
    main()
