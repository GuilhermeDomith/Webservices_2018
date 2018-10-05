import json
import os
from lxml import etree
from flask import Flask, request

app = Flask(__name__)

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
def arquivos(nome_arquivo):

    retorno = dict(arquivo=nome_arquivo)
    try: 
        retorno['conteudo'] = open(nome_arquivo).read()
    except FileNotFoundError: 
        retorno['status'] = 'Arquivo nao encontrado.'

    return json.dumps(retorno)


@app.route('/arquivos', methods=['DELETE'])
def arquivos_delete():
    files = os.listdir()
    files.remove(__file__)

    for file in files:
        os.remove(file)

    return json.dumps({'arquivos_removidos': files})


@app.route('/arquivos/<nome_arquivo>', methods=['DELETE'])
def arquivo_delete(nome_arquivo):

    if nome_arquivo == __file__:
        status = "O arquivo não pode ser removido."
    else:
        try: 
            os.remove(nome_arquivo)
            status = 'Removido com sucesso.'
        except FileNotFoundError: 
            status = 'Arquivo nao encontrado.'

    return json.dumps({'arquivo': nome_arquivo, 'status': status})


@app.route('/arquivos/<nome_arquivo>', methods=['PUT'])
def arquivo_update(nome_arquivo):
    
    conteudo = request.form['dados']
    with open(nome_arquivo, 'w') as file:
        file.write(conteudo)

    return arquivos(nome_arquivo)




if __name__ == '__main__':
    app.run(debug=True, port=3000)