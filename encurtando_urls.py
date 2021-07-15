import pyshorteners

# URL original
url = 'digite a url aqui'

# Carrega lib
s = pyshorteners.Shortener()
# Gera URL encurtada
shortUrl = s.tinyurl.short(url)

# Mostra resultado
print(f'URL Encurtada: {shortUrl}')
