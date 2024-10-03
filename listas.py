lista = ["Numpy",
    "pandas",
    "Scikit-learn",
    "TensorFlow",
    "Keras"]
print (lista)
numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print(type(numbers))
mix = ["uno", 2, 3.14, True,[1, 2, 3]]
print(mix)
print(len(mix))
print("primer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Último elemento:", mix[-1])
string = "Numpy"
print("primer elemento:", string[0])
print("segundo elemento:", string[1])
print("ultimo elemento:", string[-1])
print(mix[0:2])
print(mix[:2])
print((mix[2:-2]))
mix.append(["Romulo","Nancy"])
print(mix)
mix.insert(0, "María Benavides")
print(mix.index("María Benavides")) #con index podemos ver la posicion