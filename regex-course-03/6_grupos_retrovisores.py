import re
from pprint import pprint

texto = '''
 <p>Frase 1</p> <p></p> <p> Qualquer frase </p> <div> Frase 4</div>
 '''

#1 referenciando o grupo
re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', texto)


#2 referenciando o grupo dentro do grupo
tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
print(tags)

for t in tags:
    print(t)
pprint(tags)
