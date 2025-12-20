"""
Curso Python #09 - Manipulando Texto

Manipulando string com funções

"""

FRASE = 'Curso em Video Python'

print(len(FRASE))
# Função len() mostra quantos caracteres temos na FRASE
print(FRASE.count('o'))
# Função count() conta quantas vezes ele localiza o parametro
print(FRASE.count('o', 0, 13))
# Desta forma, ele vai procurar apenas do indice 0 até o 13
print(FRASE.find('deo'))
# A função find() localiza onde iniciou o parametro
print(FRASE.find('Android'))
# Como não há essa FRASE na String, retorna -1
print('Curso' in FRASE)
# Retorna True caso encontre e False se não localizar
print(FRASE.replace('Python', 'Android'))
# Procura Python e altera para Android
print(FRASE.upper())
# Deixa a String em maisculo(uppercase)
print(FRASE.lower())
# Deixa a String em minusculo(lowercase)
print(FRASE.capitalize())
# Deixa a String Capitalizada
print(FRASE.title())
# Deixa a String em formato de titulo

FRASE2 = '   Aprenda Python  '
print(FRASE2.strip())
# Remove os espaços no inicio e final da String
print(FRASE2.rstrip())
# Remove os espaços apenas ao final da String(r = right)
print(FRASE2.lstrip())
# Remove os espaços do inicio da String(l = left)

print(FRASE.split())
# Separa a String com cada palavra sendo uma lista
print('-'.join(FRASE))
