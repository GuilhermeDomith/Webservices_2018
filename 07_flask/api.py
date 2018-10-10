import json
import os
from lxml import etree
from flask import Flask, request

app = Flask(__name__)
nao_apagar = ['testa_api.py', __file__]

@app.route('/arquivos/json', methods=['GET'])
def arquivos_json():
    return json.dumps({'arquivos': os.listdir()})


@app.route('/arquivos/xml', methods=['GET'])
def arquivos_xml():

    root = etree.Element('arquivos')
    doc = etree.ElementTree(root)
    for file in os.listdir():
        etree.SubElement(root, 'file', name=file )

    xmlstring = etree.tostring(root, xml_declaration=True, encoding="UTF-8")
    print(xmlstring)
    return xmlstring


@app.route('/arquivos/<nome_arquivo>', methods=['GET'])
def arquivo(nome_arquivo):

    retorno = {'arquivo':nome_arquivo}
    try: 
        retorno['conteudo'] = open(nome_arquivo).read()
    except FileNotFoundError: 
        retorno['erro'] = 'Arquivo nao encontrado.'

    return json.dumps(retorno)


@app.route('/arquivos', methods=['DELETE'])
def arquivos_delete():
    files = os.listdir()
    [files.remove(f) for f in nao_apagar]

    for file in files:
        os.remove(file)

    return json.dumps({'arquivos_removidos': files})


@app.route('/arquivos/<nome_arquivo>', methods=['DELETE'])
def arquivo_delete(nome_arquivo):
    retorno = {'arquivo':nome_arquivo}

    if nome_arquivo in nao_apagar:
        retorno['erro'] = "O arquivo não pode ser removido."
    else:
        try: 
            os.remove(nome_arquivo)
            retorno['status'] = 'Removido com sucesso.'
        except FileNotFoundError: 
            retorno['erro'] = 'Arquivo nao encontrado.'

    return json.dumps(retorno)


@app.route('/arquivos/<nome_arquivo>', methods=['PUT'])
def arquivo_update(nome_arquivo):   

    if nome_arquivo in nao_apagar:
        erro = "O arquivo não pode ser atualizado."
        return json.dumps({'arquivo': nome_arquivo, 'erro': erro})
    
    conteudo = request.form['dados']
    with open(nome_arquivo, 'w') as file:
        file.write(conteudo)

    return json.dumps({'arquivo':nome_arquivo, 'status': 'Arquivo gravado com sucesso.'})


if __name__ == '__main__':
    app.run(debug=True, port=3000)