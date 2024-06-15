let a = 10; 
let b = 40;
let c = 100;

function probandoREST(...params){
    console.log(params);
    //params[1] = 20;
    b = "Voyager";
    console.log(params);
}

console.log(a, b, c);
probandoREST(a, b, c);
console.log(a, b, c);
