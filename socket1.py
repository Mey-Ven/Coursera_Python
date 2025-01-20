import socket

# Connexion au serveur
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Demande HTTP GET à la bonne URL
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Lire la réponse
response = ""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    response += data.decode()

mysock.close()

# Séparer les en-têtes du corps
headers, body = response.split("\r\n\r\n", 1)

# Afficher les en-têtes pour analyse
print("En-têtes HTTP :")
print(headers)

# Extraire les valeurs spécifiques
for header_line in headers.split("\r\n"):
    if "Last-Modified" in header_line:
        print(f"Last-Modified: {header_line.split(': ', 1)[1]}")
    if "ETag" in header_line:
        print(f"ETag: {header_line.split(': ', 1)[1]}")
    if "Content-Length" in header_line:
        print(f"Content-Length: {header_line.split(': ', 1)[1]}")
    if "Cache-Control" in header_line:
        print(f"Cache-Control: {header_line.split(': ', 1)[1]}")
    if "Content-Type" in header_line:
        print(f"Content-Type: {header_line.split(': ', 1)[1]}")