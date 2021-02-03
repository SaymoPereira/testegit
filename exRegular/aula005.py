import re

'''
Meta caracteres: ^ $ 
    
    ( ) -> Grupos de caracteres => Encontra os caracteres especificos passados e    são salvos na memória 
    ( ) ( ) -> \1 \2 => Acessando os retrovisores, como grupos são salvos em memória é necessário acessa-ló dessa forma
    ( () ) () -> \1\2 \3 -> 1 e 2 acessam os grupos que se encontram um dentro do outor e o 3 se refere ao 3 retrovisor
        
    
'''

txt = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div>
'''


# tags = re.findall(r'(<([a-z]{1,3})>(.*?)<\/\2>)', txt)
# tags2 = re.findall(r'<([a-z]{1,3})>(?:.*?)<\/\1>', txt)  # -> ?: usado para não salvar em memória o grupo
# print(tags)
# print(tags2)

'''
for t in tags:
    um, dois, tres = t
    print(tres, end=' ')
'''

cpf = '147.852.963-12'

# print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))

# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))  # -> Cria dois grupos o de fora serve para pegar
# todas informações do cpf, já o de dentro serve apenas como quantificador, portanto, não precisa ser salvo na memória


print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', txt))  # -> Colocando aspas entre as frases
