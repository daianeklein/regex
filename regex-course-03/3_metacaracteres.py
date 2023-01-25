## metacaracteres
#  . ^ $ * + ? { } [ ] \ | ( )

# | OU
# . qualquer caracter, exceto quebra de linha

# [] Conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''
# | ou
print(re.findall(r'João|Maria', texto))

# . qualquer coisa
# cada caracter significa uma palavra
print(re.findall(r'João|Maria|ad.ltos', texto))
print(re.findall(r'João|ad...', texto))

# [] Conjunto de caracteres
# J e M maiúsculo ou minúsculo
print(re.findall('[Jj]oão|[Mm]aria', texto))

#range
print(re.findall('[a-zA-Z0-9]aria', texto))

# flags IGNORECASE
print(re.findall('JOAO|Maria', texto, flags=re.I))


