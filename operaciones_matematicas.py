#operadores numéricos
a = 10
b = 3
print("Suma:", a + b) 
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Division:", a/b)

#En python, el operador de módulo(%) se utiliza para obtener residuo de una division entre dos números
print("Módulo:", a % b)
#El siguiente signo es el de doble division y el resultado sería la parte entera
print("División entera:", a // b)
print("potenciacion:", a ** b) #**potenciacion 10 elevado a la 3
#Queremos sumarle 2 a la variable a podrías poner a = a + 2 o mejor:
a += 2
print(a)
operacion_1 = 2 + 3 * 4
operacion_2 = 2 + (3 * 4)
print(operacion_1)
print(operacion_2)
operacion_3 = (2+3) * (4 ** 2) / 8 - 1
print(operacion_3)
print(a > b)
print(b < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)