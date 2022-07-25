var lista = [
   {nome: "spiderman", ano: 2000, categoria: "aventura"},
   {nome: "hulk", ano: 2002, categoria: "ação"},
   {nome: "ironman", ano: 2010, categoria: "scify"},
];

document.getElementById("button").onclick = function(){
   document.getElementById("nomes").innerHTML = lista[1].nome;
}