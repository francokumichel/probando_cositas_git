def dividir(a, b):
     try:
         try:
             if a == 5 and b == 2:
                 raise Exception()
                 resultado = a / b
                 print(f"El resultado de {a} dividido {b} es: {resultado}")
     	except ZeroDivisionError:
             print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Tipos de datos no válidos para la operación.")
    else:
        print("No se produjo ninguna excepción")
 caracteres = [i for i in range(1, 100)]
 caracteres.extend([i for i in string.ascii_letters])
 print(caracteres)
 try:
     dividir(random.choice(caracteres), random.choice(caracteres))
except Exception:
     print("Error desconocido")
finally:
     print("Fin de la ejecución")
