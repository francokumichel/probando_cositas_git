#### A. Cite un ejemplo de código para cada lenguaje seleccionado donde se aprecien los distintos tipos de parámetros soportados y su uso. Cada fragmento puede tener una breve explicación textual. En la misma debe quedar claro el modo de ligadura que utiliza el lenguaje (posicional, por nombre, etc), si requieren o no ser tipados, o cualquier otra característica que considere relevante

### JavaScript
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
Modo IN: Pasaje por valor para tipos inmutables (int, float, str,
etc.) y pasaje por referencia para tipos mutables (listas,
diccionarios, etc.).
Modo OUT: No tiene un modo OUT explícito.
Modo IN/OUT: Pasaje por referencia para objetos mutables

##### Bibliografia
https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions

