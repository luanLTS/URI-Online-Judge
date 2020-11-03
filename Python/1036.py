import math
entradas = input().split(" ")

a = float(entradas[0])
b = float(entradas[1])
c = float(entradas[2])

delta = (b**2) - (4*a*c)
if delta == 0 and a > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    print("R1 = %.5f" %x1)
elif delta > 0 and a > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("R1 = %.5f" %x1)
    print("R2 = %.5f" %x2)
else:
    print("Impossivel calcular")