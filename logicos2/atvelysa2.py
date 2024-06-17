nota = int(input('Insira uma nota de 0 a 10'))
frequencia = float(input('Insira a frequência em %: '))

if nota >= 7 and frequencia >= 75:
    print('Você foi aprovada!')
else:
    print('Você foi reprovada!')