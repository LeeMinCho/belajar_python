# casting integer
print("====INTEGER====")
dataInteger = 0
print("data :", dataInteger, ", bertipe :", type(dataInteger))

dataFloat = float(dataInteger)
print("data :", dataFloat, ", bertipe :", type(dataFloat))

dataString = str(dataInteger)
print("data :", dataString, ", bertipe :", type(dataString))

dataBoolean = bool(dataInteger)  # Akan False jika nilai int = 0
print("data :", dataBoolean, ", bertipe :", type(dataBoolean))

# casting float
print("====FLOAT====")
dataFloat = 9.5
print("data :", dataFloat, ", bertipe :", type(dataFloat))

dataInteger = int(dataFloat)  # Akan dibulatkan ke bawah
print("data :", dataInteger, ", bertipe :", type(dataInteger))

dataString = str(dataFloat)
print("data :", dataString, ", bertipe :", type(dataString))

dataBoolean = bool(dataFloat)  # Akan False jika nilai int = 0
print("data :", dataBoolean, ", bertipe :", type(dataBoolean))

# casting boolean
print("====BOOLEAN====")
dataBoolean = True
print("data :", dataBoolean, ", bertipe :", type(dataBoolean))

dataInteger = int(dataBoolean)  # True menjadi 1 & False menjadi 0
print("data :", dataInteger, ", bertipe :", type(dataInteger))

dataString = str(dataBoolean)
print("data :", dataString, ", bertipe :", type(dataString))

dataFloat = float(dataBoolean)
print("data :", dataFloat, ", bertipe :", type(dataFloat))

# casting String
print("====String====")
dataString = "10"
print("data :", dataString, ", bertipe :", type(dataString))

# Jika dataString = "Uchiha" akan error, jika dataString = "10" tidak error
dataInteger = int(dataString)
print("data :", dataInteger, ", bertipe :", type(dataInteger))

dataFloat = float(dataString)
print("data :", dataFloat, ", bertipe :", type(dataFloat))

dataBoolean = bool(dataString)  # Akan bernilai false jika dataString = ""
print("data :", dataBoolean, ", bertipe :", type(dataBoolean))
