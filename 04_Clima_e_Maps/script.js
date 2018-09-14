var temp_min = document.querySelector("#temp_min");
var temp_max = document.querySelector("#temp_max");
var temp = document.querySelector("#temp");
var coordenada = document.querySelector("#coord");
var pressao = document.querySelector("#pressao");
var cidade = document.querySelector("#cidade");
var nasc_sol = document.querySelector("#nasc_sol");
var por_sol = document.querySelector("#por_sol");
var icone_clima = document.querySelector('#icone_clima');

var cidade_busca = document.querySelector('#cidade_busca');
var buscar_btn = document.querySelector('#buscar_btn');
var info_erro = document.querySelector('#info_erro');

buscar_btn.onclick = () => {
    fazerRequisicaoClima(removeAcento(cidade_busca.value));
    cidade_busca.value = '';
}

document.addEventListener('DOMContentLoaded', function() {
    fazerRequisicaoClima('BARBACENA');
}, false);

cidade_busca.onkeyup = () => {
    info_erro.classList.add('contrair');
};

info_erro.addEventListener('animationend', () => {
    info_erro.setAttribute('hidden', null);
});

function fazerRequisicaoClima(cidade){
    var req = new XMLHttpRequest();
    const api_key = '17b07ad3bdf211befe17b2d06a798397';

    req.onloadend = () => { exibirDadosClima(req); };

    req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&APPID='+api_key);
    req.send(null);

    return req;
}


function exibirDadosClima(req){
    console.log(req.responseText);
    dados_clima = JSON.parse(req.responseText);

    if(dados_clima.cod == '404'){
        cidadeNaoEncontrada();
        return;
    }

    dados_cidade.removeAttribute('hidden');

    temp.innerHTML = celcius(dados_clima.main.temp) + ' °C';
    temp_min.innerHTML = celcius(dados_clima.main.temp_min) + ' °C';
    temp_max.innerHTML = celcius(dados_clima.main.temp_max) + ' °C';
    coordenada.innerHTML = dados_clima.coord.lat + ', ' +dados_clima.coord.lon;
    pressao.innerHTML = dados_clima.main.pressure + ' hpa';
    cidade.innerHTML = dados_clima.name;
    nasc_sol.innerHTML = hora(dados_clima.sys.sunrise);
    por_sol.innerHTML = hora(dados_clima.sys.sunset);
    icone_clima.src = 'http://openweathermap.org/img/w/'+dados_clima.weather[0].icon+'.png';

    setarMapa(dados_clima.coord.lat, dados_clima.coord.lon);
}

function setarMapa(latitude, longitude){
    var loc = {lat: latitude, lng: longitude};

    var map = new google.maps.Map(document.getElementById('mapa'), {
        center: {lat: loc.lat,lng: loc.lng - 0.2},
        zoom: 11
    });

    var marker = new google.maps.Marker({
        map: map,
        position: loc,
    });

}

function cidadeNaoEncontrada(){
    info_erro.classList.remove('contrair');
    info_erro.removeAttribute('hidden');

    info_erro.innerHTML = 'Cidade não encontrada.';
}

function hora(timestamp){
    var date = new Date(timestamp * 1000);
    return date.getHours() +':'+date.getMinutes();
}

function celcius(temp){
    console.log(temp);
    console.log(temp - 32);

    return Math.round(temp - 273.15);
};

function removeAcento (text){       
    text = text.toLowerCase();                                                         
    text = text.replace(new RegExp('[ÁÀÂÃ]','gi'), 'a');
    text = text.replace(new RegExp('[ÉÈÊ]','gi'), 'e');
    text = text.replace(new RegExp('[ÍÌÎ]','gi'), 'i');
    text = text.replace(new RegExp('[ÓÒÔÕ]','gi'), 'o');
    text = text.replace(new RegExp('[ÚÙÛ]','gi'), 'u');
    text = text.replace(new RegExp('[Ç]','gi'), 'c');
    return text;                 
}