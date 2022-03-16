# tipe data integer
from ctypes import c_double
dataInteger = 1
print("data :", dataInteger, ", bertipe :", type(dataInteger))

# tipe data float
dataFloat = 1.5
print("data :", dataFloat, ", bertipe :", type(dataFloat))

# tipe data string
dataString = "Uzumaki"
print("data :", dataString, ", bertipe :", type(dataString))

# tipe data boolean
dataBoolean = True
print("data :", dataBoolean, ", bertipe :", type(dataBoolean))
dataBoolean = False
print("data :", dataBoolean, ", bertipe :", type(dataBoolean))

# TIPE DATA KHUSUS
# Bilangan Complex
dataComplex = complex(5, 6)
print("data :", dataComplex, ", bertipe :", type(dataComplex))

# Tipe data dari Bahasa C
dataDouble = c_double(10.5)
print("data :", dataDouble, ", bertipe :", type(dataDouble))
