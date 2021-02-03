import re

'''
Meta caracteres: ^ $
    
    ^ -> Começa com => Passado algo, ela requer que seja exatamente como o requerido, caso contrário retorna uma lista vazia
    $ ->

'''

cpf = '147.852.963-12'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
