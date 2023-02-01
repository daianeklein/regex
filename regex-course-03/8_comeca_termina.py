# ^ --> começa com
# $ termina com
# [^a-z] --> negacao / Qualquer comeca que não comeca com A entre Z

import re

cpf = 'a 147.852.963-12 a'

## ^ expressão regular - match exato
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))

cpf1 = 'a 147.852.963-12'
## ^ expressão regular - match exato - vai funcionar
# $ termina com
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf1))

cpf3 = 'a 147.852.963-12'
print(re.findall(r'[^0-9]', cpf))





