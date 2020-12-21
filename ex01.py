print('-='*20, '\nTabuada')
print('-='*20)

while True:

    print('[Menu]\n'
          '[1] Soma\n'
          '[2] Subtração\n'
          '[3] Multiplicação')
    n = int(input('Digite um número [Digite 0 para parar]:'))
    escolha = int(input('Digite qual operção deseja efetuar:'))

    if n == 0:
        break

    for c in range(0, 11):
        if escolha == 1:
            s = n + c
            print(f'{n} + {c} = {s}')
        elif escolha == 2:
            s = n - c
            print(f'{n} - {c} = {s}')
        elif escolha == 3:
            s = n * c
            print(f'{n} x {c} = {s}')
    print('-' * 40)
