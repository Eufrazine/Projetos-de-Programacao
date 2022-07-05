function tEstilo1() {
    let $divEstilo = document.getElementById("iPrincipal");
    $divEstilo.classList.add('estilo1');
    $divEstilo.classList.remove('estilo2')
}

function tEstilo2() {
    let $divEstilo = document.getElementById("iPrincipal");
    $divEstilo.classList.add('estilo2');
}

function padrão() {
    let $divEstilo = document.getElementById("iPrincipal");
    $divEstilo.classList.remove('estilo1');
    $divEstilo.classList.remove('estilo2');
}