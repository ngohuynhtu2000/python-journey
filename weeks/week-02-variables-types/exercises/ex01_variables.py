
"""
Bài tập 01: Biến trong Python
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
ten = "Huỳnh Tú"
tuoi = 18
diem_tb = 8.5
dang_hoc = True

print("===== TODO 1 =====")
print("Tên:", ten, "- Kiểu dữ liệu:", type(ten))
print("Tuổi:", tuoi, "- Kiểu dữ liệu:", type(tuoi))
print("Điểm trung bình:", diem_tb, "- Kiểu dữ liệu:", type(diem_tb))
print("Đang học:", dang_hoc, "- Kiểu dữ liệu:", type(dang_hoc))


# TODO 2: Hoán đổi giá trị 2 biến không dùng biến tạm
a = 10
b = 20

a, b = b, a

print("\n===== TODO 2 =====")
print("a =", a)
print("b =", b)


# TODO 3: Augmented assignment
x = 100

print("\n===== TODO 3 =====")

x += 20
print("Sau += 20:", x)

x -= 10
print("Sau -= 10:", x)

x *= 2
print("Sau *= 2:", x)

x //= 5
print("Sau //= 5:", x)


# TODO 4: Multiple assignment
ho, ten, tuoi = "Ngô", "Huỳnh Tú", 19

print("\n===== TODO 4 =====")
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
