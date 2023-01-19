import re

url = 'https://www.nivana.com.br/surftrips'
padrao_url = re.compile('(http(s)?://)?(www.)?nivana.com(.br)?/surftrips')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")
