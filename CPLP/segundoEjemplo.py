def funcionPorNombre(nombre, apellido): ##Parámetros obligatorios
    print("Mi nombre es", nombre, apellido)

funcionPorNombre(apellido = "Giorgio", nombre = "Giovanni") #Mi nombre es Giovanni Giorgio
palabra1 = "Too"
palabra2= "long"
funcionPorNombre(palabra1, palabra2) #Mi nombre es Too long

'''
i = 5
a = int(input('a: '))
b = int(input('b: '))

def f(arg=max(a, b)):
    print(arg)

i = 6
f()
'''
#probanding(obj1)


obj1 = {
    "valor1" : "algo",
    "valor2" : "otra"
}

def probanding(*tupla):
    print(tupla)

probanding(obj1, 5, 6, "Hola")