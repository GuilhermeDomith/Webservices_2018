var pesquisar = document.getElementById('pesquisar_cep');

pesquisar.onclick = function (){
    consulta_CEP(document.getElementById('cep').value);
};

function consulta_CEP(cep){

    var req = new XMLHttpRequest();
    
    req.onloadend = (e) => { exibir_info_cep(req) }

    req.open('GET', 'https://viacep.com.br/ws/' + cep + '/json/');
    req.send(null);
}

function exibir_info_cep(req){
    let cep;

    if(req.responseText.length > 0){
        cep = JSON.parse(req.responseText);
        if(cep['erro'])
            cep['erro'] = 'O CEP fornecido não existe'
        
    }else
        cep = {'ERRO': 'O CEP fornecido é inválido'};

    let tabela_cep =   document.getElementById('cep_info');
    let tbody = document.querySelector('#cep_info tbody');


    while(tabela_cep.rows.length > 0 ){
        tabela_cep.deleteRow(0);
    }

    

    for(key in cep){
        if(cep[key].length == 0) continue;

        let tr = document.createElement('tr');

        let th = document.createElement('th');
        th.appendChild(document.createTextNode(key.toUpperCase()));
        tr.appendChild(th);

        let td = document.createElement('td');
        td.appendChild(document.createTextNode(cep[key]));
        tr.appendChild(td);

        tbody.appendChild(tr);
    }
    
    document.querySelector('#entrada').classList.remove('centro');
    document.querySelector('#entrada').classList.add('deslizar-class');
    tabela_cep.hidden = false;
}