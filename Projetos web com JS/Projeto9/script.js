const api = "https://digimon-api.vercel.app/api/digimon";

var filter = prompt();

window.onload = function () {
    fetch(api)
        .then(data => data.json())
        .then(data => {
            for (let index = 0; index < data.length; index++) {
                var digimon = `
                <div id="digimon">
                    <img src="${data[index].img}">
                    <p>${data[index].level}</p>
                    <p>${data[index].name}</p>
                </div>
                `
                if(data[index].level == filter){
                    document.getElementById("digimons").innerHTML += digimon;
                }
            }
        })
}