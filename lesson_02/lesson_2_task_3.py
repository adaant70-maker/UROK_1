import math
def square (A):
    S = A * A
    if isinstance(A, int):
        return S
    else:
        return math.ceil(S)
A = float(input("Введите сторону квадрата: "))   
print(f"Площадь квадрата:{square(A)}") 

