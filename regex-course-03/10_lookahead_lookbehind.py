import re

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

#Positive lookahead
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

#Negative lookahead
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookahead
print(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind
print(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative lookbehind
print(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Positive lookbehind
print(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

# Negative lookbehind
print(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
