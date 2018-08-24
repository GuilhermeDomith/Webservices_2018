#coding: utf-8
import urllib2, json

def main():

    while True:
        login = raw_input('\nLogin da consulta: ')

        userJson = loadJson(getUrl(login))
        if userJson == None:
            continue

        print('Usuário da consulta: {}'.format(userJson['name'].encode('utf-8')))

        followersJson = loadJson(getUrl(login+'/followers'))
        if not followersJson:
            return

        print('%d seguidores:\n'%len(followersJson))

        for seguidor in followersJson:
            login = seguidor['login']
            user = loadJson(getUrl(login))
            if not user:
                continue

            print(user['name'])

            repositorios = loadJson(getUrl(login+'/repos'))
            if not repositorios:
                continue

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
            cache = open("cache/"+cacheFileName, 'r')
            conteudo = cache.read()
        except:
            urlopen = urllib2.urlopen(url)
            conteudo = urlopen.read()

            cache = open("cache/"+cacheFileName, 'w')
            cache.write(conteudo)

        cache.close()
    except Exception as e:
        print(e)
        return None

    return json.loads(conteudo)

if __name__ == "__main__":
    main()
