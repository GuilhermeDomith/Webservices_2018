var clima_div = document.querySelector("#clima");

var req = new XMLHttpRequest();

req.onloadend = (e) => {
    clima_div.value = req.responseText;
    console.log(e);
    console.log(req.responseText);
};

clima_div.value = 'teste';

const api_key = '17b07ad3bdf211befe17b2d06a798397';
req.open('GET', 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID='+api_key);
req.send(null);