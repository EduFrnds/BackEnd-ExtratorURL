import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?nivana.com(.br)?/surftrips')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_params(self):
        indice_interrogacao = self.url.find('?')
        url_params = self.url[indice_interrogacao + 1:]
        return url_params

    def get_valor_params(self, parametro_busca):
        indice_params = self.get_url_params().find(parametro_busca)
        indice_valor = indice_params + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_params().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_params()[indice_valor:]
        else:
            valor = self.get_url_params()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_params() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "nivana.com/surftrips?viagemorigem=imbituba&viagemdestino=costa rica&local=tamarindo"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)
