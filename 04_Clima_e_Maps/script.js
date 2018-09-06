var temp_min = document.querySelector("#temp_min span");
var temp_max = document.querySelector("#temp_max span");
var temp = document.querySelector("#temp span");
var coordenada = document.querySelector("#coord span");
var pressao = document.querySelector("#pressao span");
var cidade = document.querySelector("#cidade span");
var nasc_sol = document.querySelector("#nasc_sol span");
var por_sol = document.querySelector("#por_sol span");

function fazerRequisicaoClima(id){
    var req = new XMLHttpRequest();
    const api_key = '17b07ad3bdf211befe17b2d06a798397';

    req.onloadend = exibirDadosClima

    req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID='+api_key);
    req.send(null);

    return req;
}

function exibirDadosClima(){
    console.log(this.responseText);
    dados_clima = JSON.parse(this.responseText);
    temp.innerHTML = dados_clima.main.temp;
    temp_min.innerHTML = dados_clima.main.temp_min;
    temp_max.innerHTML = dados_clima.main.temp_max;
    coordenada.innerHTML = dados_clima.coord.lon + ' + ' +dados_clima.coord.lat;
    pressao.innerHTML = dados_clima.main.pressure;
    cidade.innerHTML = dados_clima.name;
    nasc_sol.innerHTML = dados_clima.sys.sunset;
    por_sol.innerHTML = dados_clima.sys.sunrise;
}

document.addEventListener('DOMContentLoaded', function() {
    fazerRequisicaoClima(524901)
 }, false);

/*class DadosClima{
    constructor(reqJson){
        var dados = JSON.parse(reqJson);
        this.semanas = dados['list']
        this.cidade = dados['city']
    }
}*/