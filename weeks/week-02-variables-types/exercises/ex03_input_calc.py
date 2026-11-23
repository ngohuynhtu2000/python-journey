
"""
Bài tập 03: Máy tính nhận input
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số và tính toán
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)

if b != 0:
    print("Thương:", a / b)
else:
    print("Không thể chia cho 0")


# TODO 2: Tính diện tích và chu vi hình tròn
pi = 3.14159
r = float(input("\nNhập bán kính hình tròn: "))

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)


# TODO 3: Tính giá sau khi giảm giá
gia_goc = float(input("\nNhập giá gốc: "))
giam_gia = float(input("Nhập phần trăm giảm giá: "))

tien_giam = gia_goc * giam_gia / 100
gia_sau_giam = gia_goc - tien_giam

print("Số tiền được giảm:", tien_giam)
print("Giá sau khi giảm:", gia_sau_giam)


# TODO 4: Máy đổi tiền VNĐ sang USD
tien_vnd = float(input("\nNhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

tien_usd = tien_vnd / ty_gia

print("Số tiền USD:", round(tien_usd, 2))
