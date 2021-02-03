import re

'''
Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
    | -> ou
    . -> qualquer caractere (EXCEÇÃO: Quebra de linha)
    [] -> Conjunto de caracteres
    * + ? { } -> Quantificadores...
    * -> 0 ou n(ilimitadas) vezes
    + -> 1 ou n
    ? -> 0 ou 1
    {} -> Qualquer qnt de vezes ou o min e max de vezes que queira repetições
    """
    ex:
        {10,} -> 10 ou mais
        {,10} -> Até 10
        {10} -> Especificamente 10
        {5,10} -> 5 a 10 vezes
    """
'''


txt = '''
João trouxe flores para sua namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo. zaria
Não canso de ouvir a Maria:
"Joooooooooooãoooooooo, o café tá prontinho aqui, Veeemm"!
'''


print(re.findall(r'j[a-z]+ão+', txt, flags=re.IGNORECASE))
print(re.findall(r'jo{1,}ão{1,}', txt, flags=re.IGNORECASE))
print(re.findall(r've{3}m{1,2}', txt, flags=re.IGNORECASE))

txt2 = 'João, ama amar alguem e ser amado!'

print(re.findall(r'ama[a-z]{0,2}', txt2, flags=re.IGNORECASE))

