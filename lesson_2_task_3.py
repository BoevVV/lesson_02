import math
def sguare(side):
    return math.ceil(side * side)
num_side = float(input("Введите сторону квадрата - "))
print (f"Площадь квадрата равна: {sguare(num_side)}")
