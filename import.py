import re

# Nom du fichier à utiliser (remplacez-le si nécessaire)
file_name = "regex_sum_1995141.txt"

try:
    # Ouvrir et lire le contenu du fichier
    with open(file_name, 'r') as file:
        data = file.read()

    # Utiliser une expression régulière pour trouver tous les nombres
    numbers = re.findall(r'[0-9]+', data)

    # Convertir les nombres trouvés en entiers et calculer leur somme
    total_sum = sum(int(num) for num in numbers)

    # Afficher le résultat
    print("La somme totale des nombres dans le fichier est :", total_sum)

except FileNotFoundError:
    print(f"Fichier '{file_name}' introuvable. Assurez-vous qu'il est placé dans le même répertoire que ce script.")