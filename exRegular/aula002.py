import re

'''
Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
    | -> ou
    . -> qualquer caractere (EXCEÇÃO: Quebra de linha)
    [] -> Conjunto de caracteres
'''


txt = '''
João trouxe flores para sua namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo. zaria
Não canso de ouvir a Maria:
"Joooooooooooãoooooooo, o café tá prontinho aqui, Vemmmm"!
'''

print(re.findall(r'João|Maria|ad....s', txt))
print(re.findall(r'[a-zA-Z0-9]aria', txt))  # -> maiusculo, minusculo, númerico
print(re.findall(r'jOãO|mAriA', txt, flags=re.IGNORECASE))

