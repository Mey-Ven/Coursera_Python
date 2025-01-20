import urllib.request
import xml.etree.ElementTree as ET

# Demander l'URL
url = input("Enter URL: ")  # Exemple : http://py4e-data.dr-chuck.net/comments_2001230.xml
print("Retrieving", url)

# Lire les données depuis l'URL
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

# Analyser les données XML
tree = ET.fromstring(data)

# Trouver toutes les balises <count> et extraire leurs valeurs
counts = tree.findall('.//count')  # XPath pour trouver toutes les balises <count>
sum_counts = sum(int(count.text) for count in counts)

# Afficher le résultat
print("Count:", len(counts))
print("Sum:", sum_counts)