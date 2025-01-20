import urllib.request
import json

# URL donnée dans l'exercice
serviceurl = 'https://py4e-data.dr-chuck.net/comments_1995146.json'

while True:
    # Demander l'emplacement (vous pouvez appuyer sur Entrée directement)
    address = input('Enter location: ')
    if len(address) < 1:
        # Si aucune entrée, utiliser l'URL par défaut
        url = serviceurl
    else:
        url = address.strip()

    print('Retrieving', url)
    try:
        # Ouvrir l'URL et lire les données
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        # Charger les données JSON
        js = json.loads(data)

        # Calculer la somme des champs "count"
        total = sum(item['count'] for item in js['comments'])
        print('Sum:', total)
        break
    except Exception as e:
        print('Error:', e)
        continue