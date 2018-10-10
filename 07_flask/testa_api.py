import requests, json, lxml, os

url = 'http://localhost:3000'

def main():
    funcoes = [ listar_arquivos, exibir_arquivo, remover_arquivo,
        remover_todos_arquivos, criar_arquivo, atualizar_arquivo]

    while True:
        opcao = ler_opcao()
        if opcao == None:
            continue
            
        funcoes[opcao]()
        os.system('pause')


def listar_arquivos():
    print('> ARQUIVOS:')
    res = requests.get(url + '/arquivos/json')
    res = json.loads(res.text)

    for arquivo in res['arquivos']:
        print('> %s' %arquivo)

def exibir_arquivo():
    nome_arquivo = input('> Nome do arquivo: ')
    res = requests.get('%s/arquivos/%s' %(url, nome_arquivo))
    res = json.loads(res.text)

    if 'erro' in res:    
        print('> Erro: '+res['erro'])
    else:
        print('> Conteúdo: \n'+res['conteudo'])

def remover_arquivo():
    nome_arquivo = input('> Nome do arquivo: ')
    res = requests.delete('%s/arquivos/%s' %(url, nome_arquivo))
    res = json.loads(res.text)

    if 'erro' in res:    
        print('> Erro: '+res['erro'])
    else:
        print('> status: '+res['status'])


def remover_todos_arquivos():
    res = requests.delete('%s/arquivos'%url)
    res = json.loads(res.text)

    files = res['arquivos_removidos']
    print('> Arquivos Removidos: %s\n'%(files if len(files) > 0 else 'nenhum'))


def criar_arquivo():
    nome_arquivo = input('> Nome do arquivo: ')
    conteudo = input('> Conteudo: ')
    res = requests.put(
            '%s/arquivos/%s'%(url, nome_arquivo), 
            data={'dados': conteudo}
          )
    res = json.loads(res.text)
    
    if 'erro' in res:    
        print('> Erro: '+res['erro'])
    else:
        print('> Status: '+res['status'])


def atualizar_arquivo():
    nome_arquivo = input('> Nome do arquivo: ')
    res = requests.get('%s/arquivos/%s' %(url, nome_arquivo))
    res = json.loads(res.text)

    if 'erro' in res:    
        print('> Erro: '+res['erro'])
        print('> Um novo arquivo será criado ')
        conteudo = input('> Conteúdo: ')
    else:
        print('> Conteúdo Gravado: \n'+res['conteudo'])
        conteudo = input('> Novo Conteúdo: ')

    res = requests.put(
            '%s/arquivos/%s'%(url, nome_arquivo), 
            data={'dados': conteudo}
          )
    res = json.loads(res.text)

    if 'erro' in res:    
        print('> Erro: '+res['erro'])
    else:
        print('> Status: '+res['status'])



def ler_opcao():
    os.system('cls || clear')

    opcao = input('''
            SELECIONE UMA OPÇÃO:

            1. Listar arquivos
            2. Exibir arquivo
            3. Remover arquivo
            4. Remover todos os arquivos
            5. Criar arquivo
            6. Atualizar arquivo

            Opção: ''')

    try:
        opcao = int(opcao) - 1
        if opcao < 0 or opcao > 5:
            opcao = None
    except:
        return None

    return opcao
        
if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: pass