// I++ est équivalant à i += 1 
// boucle de type fore == pour
for (let i = 0; i < 10; i++){
    console.log(i)
}


// bien comprendre 
let fruits = ['abricot','baie','cerise']
fruits[3]=`datte`;
//boucle for classique
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// boucle foreach opar clé
for (let key in fruits) {
    console.log(`${key} : ${fruits[key]}`);
}

// boucle foreach par valeur
for (let fruit of fruits){
    console.log(`${fruit}`);
}



// Méthode forEach qui attend une fonction de call back
let legumes = new Array('artichaut', 'betterave', 'céléri');
legumes.push('carotte');

legumes.forEach(function (value , index, list){
    console.log(`${index} : ${value}`);
    if(value =='artichaut'){
        list[index] = 'tomate';
    }
});

console.log(legumes);

// Similaire a ce qui est écris au dessus . 
legumes.forEach((value,index,list) => {
    console.log(`${index} : ${value}`)
});


let forEachLog = (value,index,list) => {
    console.log(`${index}: ${value}`)
};

// Maintenant on peut réutiliser la fonction anonymes forEachLog avec d'autres boucle forEach()
legumes.forEach(forEachLog); 
fruits.forEach(forEachLog);
pattiseries.forEach(forEachLog);