function f_posicion(unNombre = 'John', unApellido = 'Doe'){
    console.log('My name is ', unNombre, unApellido);
}

function f_rest(...nombreCompleto){
    console.log(nombreCompleto); 
}

function f_spread(param1, param2){
    param1 = "xd"
    console.log(param1, param2);
}
let nombre = "Giovanni"; let apellido = "Giorgio"; 
f_posicion(nombre, apellido); //My name is Giovanni Giorgio
f_posicion(nombre); //My name is Giovanni Doe
f_rest(nombre, apellido) //['Giovanni', 'Giorgio']
let discovery = ['Harder', 'Better', 'Faster', 'Stronger'];
f_spread(...discovery); // Harder Better
console.log(discovery)
console.log(nombre, apellido);


function probanding(...params){
    console.log(params);
    return 5, 20, 40, 10;
}

let algo = function () {
    return 10;
}

let returnacion = probanding("6", 5, {nombre: "Juan"}, algo, algo());
console.log(returnacion);