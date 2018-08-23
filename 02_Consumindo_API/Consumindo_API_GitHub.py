#coding: utf-8
import urllib2, json

def main():

    while True:
        login = raw_input('\nLogin da consulta: ')

        userJson = loadJson(getUrl(login))
        if userJson == None:
            continue

        print('Usuário da consulta: {}'.format(userJson['name']))
        followersJson = loadJson(getUrl(login+'/followers'))
        print('%d seguidores:\n'%len(followersJson))

        for seguidor in followersJson:
            login = seguidor['login']
            user = loadJson(getUrl(login))

            print(user['name'])
            repositorios = loadJson(getUrl(login+'/repos'))
            for repos in repositorios:
                print('\t'+repos['name'])


def getUrl(user):
    return 'https://api.github.com/users/'+user

def loadJson(url):
    try:
        conteudo = ''
        cacheFileName = url.replace('/',',') + '.cache'

        ''' Abre o arquivo de cache, caso não exista cria um novo
        e escreve o conteúdo da requisição.
        '''
        try:
            cache = open(cacheFileName, 'r')
            conteudo = cache.read()
        except:
            urlopen = urllib2.urlopen(url)
            conteudo = urlopen.read()

            cache = open(cacheFileName, 'w')
            cache.write(conteudo)
        
        cache.close()
    except Exception as e:
        print(e)
        return None

    return json.loads(conteudo)

if __name__ == "__main__":
    main()
