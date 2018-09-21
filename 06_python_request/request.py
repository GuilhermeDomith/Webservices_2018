import json
import requests


#python -m pip install -U pylint

numero = 12345
while True:
    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d'%numero)
    print(r.text.rpartition(' '))
    if 'Divide by two' in r.text:
        numero = numero/2
    elif 'peak.html' in r.text:
        break
    else:
        numero = int(r.text.rpartition(' ')[2])