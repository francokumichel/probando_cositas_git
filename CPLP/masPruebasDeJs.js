function funcion1(a, b){
    a.push("elemento2");
    b = 20;
    a = [10, 3];
}

let v = ["elemento1"]; 
let o = {
    campo1: "valor1"
} 
funcion1(v, o);
console.log(v, o);