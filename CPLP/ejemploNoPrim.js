var discovery = {
    att1: "Harder",
    att2: "Better",
    att3: "Faster",
    att4: "Stronger"
}

let song = ['Harder', 'Better', 'Faster', 'Stronger'];

const funcionCambio = (param1, param2) =>{
    param1.att1 = "Aerodynamic";
    console.log("Impresión parámetro: ", param1, "Impresión variable global: ", discovery);
    param2.push('One more time');
    console.log("Impresión variable global: ", song);
    param1 = "Ya no soy un objeto";
    param2 = "Chau";
    console.log("Impresión de los parámetros: ", param1, param2);
}

funcionCambio(discovery, song); 
console.log(discovery);
console.log(song);
