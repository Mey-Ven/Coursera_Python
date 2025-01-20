import urllib.request
from bs4 import BeautifulSoup

# Demander à l'utilisateur d'entrer l'URL de départ, la position du lien et le nombre d'itérations
url = input("Enter URL: ")  # Exemple : http://py4e-data.dr-chuck.net/known_by_Fikret.html
count = int(input("Enter count: "))  # Nombre d'itérations (par exemple, 4 ou 7)
position = int(input("Enter position: "))  # Position du lien (par exemple, 3 ou 18)

print("Retrieving:", url)

# Boucle pour suivre les liens
for i in range(count):
    # Lire la page HTML et l'analyser
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # Trouver tous les liens <a> sur la page
    tags = soup.find_all('a')

    # Obtenir l'URL du lien à la position spécifiée (position - 1 car l'index commence à 0)
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)

# Afficher le dernier nom trouvé dans la séquence
name = url.split('_')[-1].split('.')[0]
print("Last name in sequence:", name)