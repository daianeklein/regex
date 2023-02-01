import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# encontrando todas as palavras
print(re.findall(r'[a-z]', texto)) #letra por letra com excecao de palavras acentuadas

# encontrando palavras
print(re.findall(r'[a-z]+', texto, flags = re.I)) #ignore cases
print(re.findall(r'[a-zA-Z]+', texto)) #ignore cases

# pegando textos e números
print(re.findall(r'[a-z0-9]+', texto, flags = re.I)) #ignore cases

# palavras acentuadas
print(re.findall(r'[a-z0-9À-ú]+', texto, flags = re.I)) #ignore cases

# short hands para palavras acentuadas
print(re.findall(r'\w+', texto))

# short hands para palavras não acenturadas
print(re.findall(r'/w+', texto, flags = re.A))

# w é para encontrar
# W (maiuscula) é para negar

