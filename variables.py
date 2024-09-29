a = 5
b = 8
c = a + b
print(c)
nombre = "María"
nombre = "Mercedes"
nombre =  "Mechys"
#Podemos concluir que las variables son modificables
print(nombre)
numero = 10 #primero ejecuta esta linea de código y veras que se imprime el 10
#numero = 10+1 #luego ejecuta esta línea de código y veras que se imprime el 11
numero += 5 #de esta manera le sumamos 5 a la variable número
print(numero)
numero -= 5   #de esta manera le restamos 5 a la variable número
print(numero)

nombre = "Maria Mercedes Benavides"
bienvenida = "Hola " + nombre + " Feliz Noche"
print(bienvenida)
bienvenida = f"Hola {nombre} Feliz Noche"
print(bienvenida)
#del bienvenida #borramos la variable, es decir la variable  que ya no esta declarada
#print(bienvenida)  

nombre = True
bienvenida = f"Hola {nombre} feliz noche"
print ("ola" in bienvenida)       

print("Betty" not in bienvenida)
print("Hola" not in bienvenida)

nombreCompletoDeTuProfe ="Jheyson Galvis" #CamelCase sirve para definir variables
nombre_completp_de_tu_profe "Jheyson Galvis" #Snake Case este es el recomendado en Python segun la documentacion