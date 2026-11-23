
"""
Bài tập 02: Chuyển đổi kiểu dữ liệu
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Chuyển chuỗi sang số nguyên
so_text = "42"
so_nguyen = int(so_text)
ket_qua = so_nguyen + 8

print("TODO 1:", ket_qua)


# TODO 2: Chuyển số thực sang số nguyên
pi = 3.14159
pi_nguyen = int(pi)

print("TODO 2:", pi_nguyen)


# TODO 3: Kiểm tra kiểu bool()
print("TODO 3:")
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("hello"):', bool("hello"))
print("bool([]):", bool([]))
print("bool([1, 2]):", bool([1, 2]))


# TODO 4: Nhập chiều cao và cân nặng, tính BMI
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print("BMI:", format(bmi, ".1f"))


# TODO 5: Chuyển số giây thành giờ, phút, giây
tong_giay = int(input("Nhập số giây: "))

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{gio} giờ {phut} phút {giay} giây")
