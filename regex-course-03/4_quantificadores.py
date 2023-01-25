
#  . ^ $ * + ? { } [ ] \ | ( )

# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}

# {10, } 10 ou mais
# {, 10} de zero a 10
# {10} especificamente 10
# {5, 10} de 5 a 10


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

# print(re.findall(r'João', texto, flags=re.I))

# João pode ser repetido n vezes - quantificador +
# pode ser aplicado em um conjunto = [a-zA-Z0-9]+
print(re.findall(r'Jo+ão+', texto, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))

# substituindo João por Felipe
# jã
print(re.sub(r'Jo+ão+', 'Julieta', texto, flags=re.I)) # não substitui o jã 
print(re.sub(r'Jo*ão*', 'Julieta', texto, flags=re.I)) # substitui o jã

# especificamente 3 "E" e pode ter de 1 a 2 "M"
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

# # conjunto
text2 = 'João ama ser amado e amada'
print(re.findall(r'ama[do]', text2, flags=re.I)) # não considera o "O"
print(re.findall(r'ama[do]{2}', text2, flags=re.I)) # considera o "O", mas não encontra o "ama"
print(re.findall(r'ama[do]{0,2}', text2, flags=re.I)) # encontra ama e amado

# pode ser em ordem invertida
print(re.findall(r'ama[od]{0,2}', text2, flags=re.I))

print(re.findall(r'ama[do|a]{0,2}', text2, flags=re.I))
print(re.findall(r'ama[doa]{0,3}', text2, flags=re.I))

