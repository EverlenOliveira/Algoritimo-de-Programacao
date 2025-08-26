#Jogo da Forca
def forca():#Função para montar o jogo da forca
  from random import randint
  p = [['amarela', 'amor','ave','bolo','branco','balao','cama', 'caneca','escola','geleia'],
   ['abelha','anta','atum','cachorro','gato','coelho'],
   ['arroz','salada','bife','acai','tacaca','manicoba']]#palavras que serão usadas por modo
  print('-='*20)
  print('Jogo da forca')
  print('-='*20)
  while True:#escolhendo o modo de jogar
    print('[1] Fácil \n [2] Médio \n [3] Difícil')
    modo=int(input('Escolha o modo do Jogo da Forca:'))
    if modo == 1 or modo == 2 or modo == 3:
      break
  pal = p[modo-1][randint(0,len(p[modo-1]))]
  usadas=''
  guess='_'*len(pal)
  if modo == 1:
    vidas = 7
  elif modo ==2:
    vidas = 5
  else:
    vidas = 2
  while True:
    print('Vidas: {}'.format(vidas))
    print('Letras usadas: {}'.format(usadas))
    print(guess)
    t=input()
    x=0
    for i in range(len(pal)):
      if t==pal[i]:
        t1=guess[0:i]
        t2=guess[i+1:len(guess)]
        guess=t1+t+t2
      else:
        x+=1
    usadas+=''+t
    if x==len(pal):
      vidas-=1
    if vidas == 0 or guess == pal:
      print('-='*20)
      print(f'A palavra era {pal}!')
      break
  if vidas == 0:
    print('Você perdeu! Tente novamente')
  else:
    print('Você ganhou!Tente um nível mais difícil')

#Execução do Jogo
while True:
  forca()
  n=''
  while n not in 'nNsS':
    n=input('\n Deseja jogar novamente? [S/N]')
  if n in 'nN':
    break



from random import randint
itens=('pedra','papel','tesoura')
pc=randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador=int(input('Qual a sua jogada?'))
print('-='*12)
if pc == 0: #computador jogou pedra
 if jogador == 0:
  print('EMPATE')
 elif jogador == 1:
  print('JOGADOR VENCE')
 elif jogador == 2:
  print('COMPUTADOR VENCE')
 else:
  print('JOGADA INVÁLIDA')
elif pc == 1: #computador jogou papel
  if jogador == 0:
    print('COMPUTADOR VENCE')
  elif jogador == 1:
    print('EMPATE')
  elif jogador == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVÁLIDA')
elif pc == 2: #computador jogou tesoura
  if jogador == 0:
    print('JOGADOR VENCE')
  elif jogador == 1:
    print('COMPUTADOR VENCE')
  elif jogador == 2:
    print('EMPATE')
else:
  print('JOGADA INVÁLIDA')
print('-='*12)



vitorias = 0
derrotas = 0
empates = 0

while True:
  pc=randint(0,2)
  jogador=int(input("Qual a sua jogada?:"))

  if pc==jogador:
    empates+=1
  elif (jogador == 0 and pc == 2) or (jogador == 1 and pc == 0) or (jogador == 2 and pc == 1):
    vitorias+=1
  else:
    derrotas+=1

  n = input("Deseja jogar novamente?: [S/N]")
  if n in 'nN':
    break
print(f"Vitórias: {vitorias}")
print(f"Derrotas: {derrotas}")
print(f"Empates:  {empates}")




from random import randint
itens=('pedra','papel','tesoura')
pc=randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador=int(input('Qual a sua jogada?'))
print('-='*12)
if pc == 0: #computador jogou pedra
 if jogador == 0:
  print('EMPATE')
 elif jogador == 1:
  print('JOGADOR VENCE')
 elif jogador == 2:
  print('COMPUTADOR VENCE')
 else:
  print('JOGADA INVÁLIDA')
elif pc == 1: #computador jogou papel
  if jogador == 0:
    print('COMPUTADOR VENCE')
  elif jogador == 1:
    print('EMPATE')
  elif jogador == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVÁLIDA')
elif pc == 2: #computador jogou tesoura
  if jogador == 0:
    print('JOGADOR VENCE')
  elif jogador == 1:
    print('COMPUTADOR VENCE')
  elif jogador == 2:
    print('EMPATE')
else:
  print('JOGADA INVÁLIDA')
print('-='*12)








