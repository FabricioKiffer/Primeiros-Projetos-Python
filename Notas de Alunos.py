print ('** Bem Vindo **')

Nome = input(str('Digite Seu Nome: '))
Idade = input(str('Digite Sua Idade: '))
Turma = input(str('Digite Sua Turma: '))

print (str(('** Falta Pouco ') + (Nome) + (' **')))

Nota1 = float (input('Digite a Primeira Nota: '))
Nota2 = float (input('Digite a Segunda Nota: '))
Nota3 = float (input('Digite a Terceira Nota: '))
Nota4 = float (input('Digite a Quarta Nota: '))

Media = (float (Nota1 + Nota2 + Nota3 + Nota4) / 4)

if Media >= 7.0:
 print (str('** Parabéns, ') + (Nome + ', ' 'Sua Média é: '+ str(round(Media)) + str(' e você foi APROVADO! **' )))
if Media < 7.0:
 print (str('** Sinto Muito, ') + (Nome + ', ' 'Sua Média é: '+ str(round(Media)) + str(' e você foi REPROVADO! **' )))

