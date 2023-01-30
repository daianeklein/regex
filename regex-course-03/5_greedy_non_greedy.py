import re

texto = '''
 <p>Frase 1</p> <p></p> <p> Qualquer frase </p> <div> Frase 4</div>
 '''

# conjunto = d | div
# de 1 a 3 letras
# . = anything
# .* qualquer coisa, com excecao quebra de linha
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))

# ? --> non greedy
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))

# + --> 1 ou + (não aparece o vazio)
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
