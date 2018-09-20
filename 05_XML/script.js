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
};

cidade_busca.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        buscar_btn.click();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    fazerRequisicaoClima('BARBACENA');
}, false);

cidade_busca.onkeyup = () => {
    info_erro.classList.add('contrair');
};

info_erro.addEventListener('animationend', () => {
    info_erro.setAttribute('hidden', null);
});

document.body.onresize = function() {
    map.setCenter((document.body.clientWidth <= 768)? centerMapV : centerMapH);
};

function setarMapa(latitude, longitude){
    coordMapa = {lat: parseFloat(latitude), lng: parseFloat(longitude)};
    centerMapH = new google.maps.LatLng(coordMapa.lat, coordMapa.lng - 0.2);
    centerMapV = new google.maps.LatLng(coordMapa.lat + 0.3, coordMapa.lng);
    

    map = new google.maps.Map(document.getElementById('mapa'), {
        center: (document.body.clientWidth <= 768)? centerMapV : centerMapH,
        zoom: 11
    });


    var marker = new google.maps.Marker({
        map: map,
        position: coordMapa,
    });

}

function fazerRequisicaoClima(cidade){
    var req = new XMLHttpRequest();
    const api_key = '17b07ad3bdf211befe17b2d06a798397';

    req.onloadend = () => { exibirDadosClima(req); };

    req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&mode=xml&APPID='+api_key);
    req.send(null);

    return req;
}


function exibirDadosClima(req){
    //console.log(req.responseText);
    dados_clima = new DOMParser().parseFromString(req.responseText, "text/xml");

    erro =  dados_clima.getElementsByTagName('cod')[0];
    if(erro != null && erro.innerHTML == '404'){
        cidadeNaoEncontrada();
        return;
    }

    dados_cidade.removeAttribute('hidden');

    var tempxml = dados_clima.getElementsByTagName('temperature')[0];
    var pressure = dados_clima.getElementsByTagName('pressure')[0];
    var coordxml = dados_clima.getElementsByTagName('coord')[0];
    var cidadexml = dados_clima.getElementsByTagName('city')[0];
    var sunxml = dados_clima.getElementsByTagName('sun')[0];
    var weatherxml = dados_clima.getElementsByTagName('weather')[0];

    temp.innerHTML = celcius(tempxml.getAttribute('value')) + ' °C';
    temp_min.innerHTML = celcius(tempxml.getAttribute('min')) + ' °C';
    temp_max.innerHTML = celcius(tempxml.getAttribute('max')) + ' °C';
    coordenada.innerHTML = coordxml.getAttribute('lat') + ', ' + coordxml.getAttribute('lon');
    pressao.innerHTML = pressure.getAttribute('value') + ' hpa';
    cidade.innerHTML = cidadexml.getAttribute('name');
    nasc_sol.innerHTML = hora(sunxml.getAttribute('rise'));
    por_sol.innerHTML = hora(sunxml.getAttribute('set'));
    icone_clima.src = 'http://openweathermap.org/img/w/'+weatherxml.getAttribute('icon')+'.png';

    setarMapa(coordxml.getAttribute('lat'), coordxml.getAttribute('lon'));
}

function cidadeNaoEncontrada(){
    info_erro.classList.remove('contrair');
    info_erro.removeAttribute('hidden');

    info_erro.innerHTML = 'Cidade não encontrada.';
}

function hora(timestamp){
    var date = new Date(timestamp + '+0000');
    return date.getHours() +':'+date.getMinutes();
}

function celcius(temp){
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
