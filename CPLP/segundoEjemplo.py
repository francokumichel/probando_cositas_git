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

temas = ['Harder', 'Better', 'Faster', 'Stronger']

dict_copado = {i: temas[i] for i in range(0,4)}

def probanding(*tupla):
    print(tupla)

probanding(obj1, 5, 6, "Hola")


def f_otroscasos(param1, param2 = 3, param3 = "Giovanni", *tuple, **diccionario):
    print(param1, param2, param3, tuple, diccionario)
    #print("Claves del diccionario:", diccionario.keys())
    
        
nombre1 = "Get"
nombre2 = "Lucky"
f_otroscasos(nombre1) #Get Giovanni
f_otroscasos(100, param3=52) #100 3 52
f_otroscasos({"key1":"value1"}, 1, 6, 7, 8, key2="value2", key3="value3")
print(dict_copado)
