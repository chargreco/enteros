def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def compuesto(num):
    return not primo(num)

def par(num):
    return num % 2 == 0

def impar(num):
    return not par(num)

def perfecto(num):
    suma = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            suma += i
            if i!= num // i:
                suma += num // i
    return suma == num

def deficiente(num):
    return num > suma_divisores(num)

def suma_divisores(num):
    suma = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            suma += i
            if i!= num // i:
                suma += num // i
    return suma