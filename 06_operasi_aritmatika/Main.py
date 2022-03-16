a = 10
b = 3

# operasi tambah
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi pembagian => otomatis menjadi float
hasil = a / b
print(a, ":", b, "=", hasil)

# operasi eksponen (pangkat)
hasil = a ** b
print(a, "**", b, "=", hasil)

# operasi modulus (sisa pembagian)
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi floor division (counterpart modulus / dibulatkan ke bawah)
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi
'''
    1. ()
    2. eksponen **
    3. perkalian, pembagian, modulus, floor division (* / % //)
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x**y*z+x/y-y % z//x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)
# 36+1.5-
