
url = ""

# Sanitização de dados
# Método replace() ou strip()
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Fatiamento
url_base = url[0:13]
url_params = url[14:24]

# Separando base e parametros
# Método find()
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_params = url[indice_interrogacao+1:]
print(url_params)

# Busca o valor de um parametro
# Método len()
parametro_busca = 'comida'
indice_params = url_params.find(parametro_busca)
indice_valor = indice_params + len(parametro_busca) + 1
indice_e_comercial = url_params.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_params[indice_valor:]
else:
    valor = url_params[indice_valor:indice_e_comercial]

print(valor)