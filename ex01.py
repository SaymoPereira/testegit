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
            # Quebrando o número
            u = s // 1 % 10
            d = s // 10 % 10
            a = s // 100 % 10
            m = s // 100 % 10
            nf = u + d + a + m

            print(f'{n} + {c} = {s}', 'Par' if s % 2 == 0 else 'Impar', end=' ')
            if nf == 9:
                print('noves fora 0')
            else:
                print(f'Noves fora {nf}')
        elif escolha == 2:
            s = n - c
            print(f'{n} - {c} = {s}', 'Par' if s % 2 == 0 else 'Impar')
        elif escolha == 3:
            s = n * c
            print(f'{n} x {c} = {s}', 'Par' if s % 2 == 0 else 'Impar')
    print('-' * 40)
