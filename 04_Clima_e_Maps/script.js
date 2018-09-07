var temp_min = document.querySelector("#temp_min");
var temp_max = document.querySelector("#temp_max");
var temp = document.querySelector("#temp");
var coordenada = document.querySelector("#coord");
var pressao = document.querySelector("#pressao");
var cidade = document.querySelector("#cidade");
var nasc_sol = document.querySelector("#nasc_sol");
var por_sol = document.querySelector("#por_sol");

function fazerRequisicaoClima(id){
    var req = new XMLHttpRequest();
    const api_key = '17b07ad3bdf211befe17b2d06a798397';

    req.onloadend = exibirDadosClima

    req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID='+api_key);
    req.send(null);

    return req;
}

function exibirDadosClima(){
    //console.log(this.responseText);
    //dados_clima = JSON.parse(this.responseText);


    dados_clima = {"coord":{"lon":37.62,"lat":55.75},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":285.89,"pressure":1021,"humidity":76,"temp_min":285.15,"temp_max":287.15},"visibility":10000,"wind":{"speed":2,"deg":80},"clouds":{"all":0},"dt":1536273000,"sys":{"type":1,"id":7325,"message":0.0209,"country":"RU","sunrise":1536201922,"sunset":1536250115},"id":524901,"name":"Moscow","cod":200};



    temp.innerHTML = dados_clima.main.temp + ' °C';
    temp_min.innerHTML = dados_clima.main.temp_min + ' °C';
    temp_max.innerHTML = dados_clima.main.temp_max + ' °C';
    coordenada.innerHTML = dados_clima.coord.lon + ' + ' +dados_clima.coord.lat; // lat:  21º13'33", long: 43º46'25"
    pressao.innerHTML = dados_clima.main.pressure + ' mb';
    cidade.innerHTML = dados_clima.name;
    nasc_sol.innerHTML = dados_clima.sys.sunset + ' hr';
    por_sol.innerHTML = dados_clima.sys.sunrise + ' hr';
}

document.addEventListener('DOMContentLoaded', function() {
    exibirDadosClima();
    //fazerRequisicaoClima(524901);
 }, false);

/*class DadosClima{
    constructor(reqJson){
        var dados = JSON.parse(reqJson);
        this.semanas = dados['list']
        this.cidade = dados['city']
    }
}*/