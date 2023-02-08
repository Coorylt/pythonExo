//  2. Entiers conséctutifs
//  198, 199, 200, 201 et 202 sont des entiers consécutifs dont la somme est égale à 1000.
//  Trouvez d'autres entiers conséctufis dont la somme vaut 1000



// Ceci est la version JS du code python.

function sum(list) {
    my_sum=0
    for(let key in list){
        my_sum += list[key];
    }

    return my_sum;
}


let somme = 0
let nombres = []

for (let i = 1; i<= 500; i++) {

    nombres.push(i);
    somme=sum(nombres);

    while (somme>1000){
        nombres.shift(0);
        somme=sum(nombres);
    }

    if (somme === 1000) {
        console.log(nombres);
    }
}


// Autre façon d'obtenir la somme sans appeller une fonction.
my_sum = nombres.reduce((accumulateur, currentValue) => {
    return accumulateur + currentValue;
}) 
console.log(my_sum)