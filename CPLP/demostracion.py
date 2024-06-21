inmutable = ({'key2': 'value2'}, {'key3': 'value3'})
print('Declaración de inmutable: ', inmutable)

def modificacion (unatupla):
    print('Dentro de la función, así es como recibe el parámetro: ', unatupla)
    unatupla[0]['key2'] = 'Soy re crack'
    print('Luego de la modificación dentro  de la función: ', unatupla)

modificacion(inmutable)
print('Esto es fuera de la función y luego de ejecutarla: ', inmutable)