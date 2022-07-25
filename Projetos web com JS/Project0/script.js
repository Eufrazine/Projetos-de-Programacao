var nome_carro = "Novo-Uno";
var n_portas = 2;
var cor_carro = "branco";
var ano_carro = 2022;
var sistema_eletrico = false;
var velocidade = 0;
var ligado = false;
var parado = false;

/* A declaração const cria uma variável cujo o valor é fixo, ou seja, 
   uma constante somente leitura.*/

const marca = "Fiat";

function acelerar(){
    // Se a condicão seguinte, valocidade menor que 120, ele somará mais 1. Ex= A velocidade está em 99, com essa função atividade ficara em 100.
    if(velocidade < 120){
        velocidade += 1;
    }
}

function freiar(){
    // Aqui diminuirá a velocidade. Ex= A velocidade está em 99, com essa função atividade ficará em 98.
    if(velocidade > 0){
        velocidade -= 1;
    }
}

function parar(){
    // Se a velocidade for igual a zero(se o meu carro estiver parado) essa minha variável de controle  confirma que eu estou realmente parado.
    if(velocidade == 0){
        parado = true;
    }else{
        parado = false;
    }
}

function ligar(){
    if(ligado == false){
        ligado = true;
    }
}

function desligar(){
    // Se o carro estiver ligado, eu posso desliga-lo. Se ele já estiver desliga-lo, eu não preciso desligar!
    if(ligado == true){
        ligado = false;
    }
}