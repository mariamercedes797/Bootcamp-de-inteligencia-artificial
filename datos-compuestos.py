#El primer tipo de dato compuesto sera la lista

lista = ["María Mercedes Benavides", "Soy Ingeniera de Sistemas", True, 1.67] 
#En el mundo de la programacion no contamos del 1 al 10, contamos del 0 al 9
print(lista[0])
lista[0] = "Mechys"
print(lista[0])
         
#La tupla es una lista que no se puede modificar
tupla = ("arroz", "huevos", "chocolate", True, 8.30) 
print(tupla[1])
#tupla[1] = "arepa"
#print(tupla[1])

#Creando un conjunto set
#El conjunto no admite elementos duplicados
conjunto = {"María Mercedes","Ingeniera de Sistemas", True, 1.67, "María Mercedes"}
print(conjunto)
#Creando un diccionario
diccionario = {
    "nombre": "María",
    "apellido": "Benavides",
    "estatura": 1.67,
    "está feliz": True,
    "nombre": "María"   
}
print(diccionario) 
print(diccionario["nombre"])
print(diccionario["apellido"])
print(["está feliz"])
print(diccionario["estatura"] + 2)  #deberia imprimirme 3.67   