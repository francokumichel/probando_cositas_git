#### A. Cite un ejemplo de código para cada lenguaje seleccionado donde se aprecien los distintos tipos de parámetros soportados y su uso. Cada fragmento puede tener una breve explicación textual. En la misma debe quedar claro el modo de ligadura que utiliza el lenguaje (posicional, por nombre, etc), si requieren o no ser tipados, o cualquier otra característica que considere relevante

### JavaScript

```javascript
//Ejemplo caso de ligadura por posicion y parámetros por defecto
function f_posicion(unNombre = 'John', unApellido = 'Doe'){
    console.log('My name is ', unNombre, unApellido);
}

let nombre = "Giovanni"; let apellido = "Giorgio"; 
f_posicion(nombre, apellido); //My name is Giovanni Giorgio
f_posicion(); //My name is John Doe

console.log(nombre, apellido);
```
La lista de argumentos y la lista de parámetros no tienen que tener necesariamente la misma longitud. Los argumentos en exceso se ignoran. Los argumentos faltantes se les asigna el valor undefined. (Libro douglas, how js works). 

```javaScript
function f_rest(...nombreCompleto){
    //Se encapsulan todos los argumentos recibidos en un array
    console.log(nombreCompleto); 
}

function f_spread(param1, param2){
    //Cada elemento del array es tratado como un parámetro diferente
    console.log(param1, param2);
}
f_rest(nombre, apellido) //['Giovanni', 'Giorgio']
let discovery = ['Harder', 'Better', 'Faster', 'Stronger'];
f_spread(...discovery); // Harder Better
```

Los parámetros primitivos se pasan a las funciones por valor; el valor se pasa a la función, pero si la función cambia el valor del parámetro, este cambio no se refleja globalmente ni en la función que llama.
```javascript
function probando1(valor) {
    valor += valor*2
    console.log('El valor dentro de la funcion es: ', valor);
}

let numero = 5;
probando1(numero);
console.log('El número dentro de la funcion es: ', numero);
``` 

Si pasas un objeto (es decir, un valor no primitivo, como Array o un objeto definido por el usuario) como parámetro y la función cambia las propiedades del objeto, ese cambio es visible fuera de la función. 

Los objetos pueden tener sus propiedades modificadas a través de referencias pasadas a funciones, pero reasignar las referencias dentro de las funciones no afecta las referencias originales fuera de las funciones.

```javascript
let discovery: ['Harder', 'Better', 'Faster'];

function cambio(param1){
    param1.push('Stronger');
    console.log(param1, discovery); //['Harder', 'Better', 'Faster', 'Stronger']
    param1 = 10; 
    console.log(param1, discovery); //10 ['Harder', 'Better', 'Faster', 'Stronger']
}


cambio(discovery);
console.log(discovery); //['Harder', 'Better', 'Faster', 'Stronger']
```


También permite subprogramas como parámetros. 

### Python
Admite el pasaje por nombre, no solo por posicion. 
```python
def f_nombreposicion(nombre, apellido): #En este caso no se pueden recibir ni más ni menos de dos argumentos
    print("Mi nombre es", nombre, apellido)

f_nombreposicion(apellido = "Giorgio", nombre = "Giovanni")
palabra1 = "Too"
palabra2= "long"
f_nombreposicion(palabra1, palabra2) #Mi nombre es Too long
```
En este mismo ejemplo vemos la flexibilidad de f_nombreposicion: dependiendo de los argumentos es cómo se hará la ligadura con los parámetros. 
Para los casos definidos previamente la lista de parámetros y la lista de argumentos deben coincidir en tamaño. 

```python
def f_otroscasos(param1, param2 = "Giovanni"):
    print(param1, param2)

nombre1 = "Get"
nombre2 = "Lucky"
f_otroscasos(nombre1) #Get Giovanni
```

Modo IN: Pasaje por valor para tipos inmutables (int, float, str,
etc.) y pasaje por referencia para tipos mutables (listas,
diccionarios, etc.).
Modo OUT: No tiene un modo OUT explícito.
Modo IN/OUT: Pasaje por referencia para objetos mutables

##### Bibliografia
https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions


### Info adicional 
##### Js
. They are deallocated
(or popped off) when the function returns. JavaScript does this differently. JavaScript allocates activation objects on a heap, like ordinary objects. Activation objects are not
automatically deactivated when functions return. Instead, the activation object can
survive as long as there is a reference to it. Activation objects are garbage collected
like ordinary objects.
The activation object contains:
• A reference to the function object.
• A reference to the activation object of the caller. This is used by return to give
control back.
• Resumption information that is used to continue execution after a call. This
is usually the address of an instruction that is immediately after a function
call.
• The parameters of the function, initialized with the arguments.
• The variables of the function, initialized with undefined.
• Temporary variables that the function uses to evaluate complex expressions.
• this, which might be a reference to the object of interest if the function object was called as a method.

##### Python
```python
#Los valores por omisión son evaluados en el momento de la definición de la función en el ámbito de la definición
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```