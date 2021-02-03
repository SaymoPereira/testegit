import re

str = 'Esse é um teste de expressões regulares, teste!'

'''
print(re.search(r'teste', str))  # -> Procura determinada expressão e retorna um math de sua localização
print(re.findall(r'teste', str))  # -> Procura determinada expressão e retorna uma lista com todos encontrados
print(re.sub('teste', 'compilação', str))  # -> Substitui determinada expressão(palavra) por outra
'''

exreg = re.compile(r'teste')

print(exreg.search(str))
print(exreg.findall(str))
print(exreg.sub('macaco', str))
