"""
Desafio 114: Crie um código em Python que teste se o site Pudim (www.pudim.com.br) está acessível 
pelo computador usado.
"""

import urllib.request

def teste_site(url):
    try:
        # Tenta abrir uma conexão com a URL fornecida
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        # Se houver erro de rede ou o site estiver offline
        print('O site não está acessível no momento.')
    except Exception as erro:
        # Captura outros erros inesperados
        print(f'Ocorreu um erro inesperado: {erro}')
    else:
        # Se a conexão foi bem-sucedida
        print('Consegui acessar o site com sucesso!')
        # Opcional: print(site.read()) # Isso leria o código HTML do site

# Execução
teste_site('http://www.pudim.com.br')
