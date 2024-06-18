function f_posicion(unNombre = 'John', unApellido = 'Doe'){
    console.log('My name is ', unNombre, unApellido);
}

function f_rest(...nombreCompleto){
    console.log(nombreCompleto); 
}

function f_spread(param1, param2){
    console.log(param1, param2);
}
let nombre = "Giovanni"; let apellido = "Giorgio"; 
f_posicion(nombre, apellido); //My name is Giovanni Giorgio
f_posicion(nombre); //My name is Giovanni Doe
f_rest(nombre, apellido) //['Giovanni', 'Giorgio']
let discovery = ['Harder', 'Better', 'Faster', 'Stronger'];
f_spread(...discovery); // Harder Better

console.log(nombre, apellido);


function probanding(...params){
    console.log(params);
}

let algo = function () {
    return 10;
}
probanding("6", 5, {nombre: "Juan"}, algo, algo());