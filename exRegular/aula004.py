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
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

print(re.findall(r'<[a-z]{1,3}>', txt))  # Capturando tags de abertura HTML
print(re.findall(r'<[a-z]{1,3}>.*<\/[a-z]{1,3}>', txt))  # Capturando o conteúdo dentro das tags =>Comportamento gulos
print(re.findall(r'<[a-z]{1,3}>.*?<\/[a-z]{1,3}>', txt))  # Capturando o conteúdo dentro das tags => Comportamento não
# guloso -> Quebra entre as tags