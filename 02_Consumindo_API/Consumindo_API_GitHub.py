#coding: utf-8
import urllib2, json

def main():

    while True:
        login = raw_input('Login da consulta: ')

        userJson = loadJson(getUrl(login))
        if userJson == None:
            continue

        continue
        print('Usuário da consulta: {}'.format(userJson['name']))
        followersJson = loadJson(getUrl(login+'/followers'))
        print('%d seguidores:'%len(followersJson))

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
        urlopen = urllib2.urlopen(url)
    except Exception as e:
        print(e)
        return None

    print(urlopen)
    print(json.load(urlopen))
    return json.load(urlopen)

if __name__ == "__main__":
    main()
