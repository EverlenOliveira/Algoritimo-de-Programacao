#Estruturas de Dados:Listas
Lista = [] #Lista vazia
Lista = [1,2,3,4,5]
Lista = ["Banana", "Maça", "Pera"]#lista homogênea (mesmo tipo de dado)
Lista = ["Olá", 234, False, 345, 2.5]#lista heterogênea
Lista = [[2,5],[0,8]]#lista de lista


#funções para manipular listas
L=[3,9,12]
print(L)
A = L.copy() #copiando o conteúdo da lista L para A
A[1]=4 #alterando o valor de apenas uma posição da lista
print(A)


#função adicionar novo elemento a lista
L=[]
L.append(10)
L.append(20)
L.append(35)
L.append(40)
L.append(50)
print(L)
L.append("Olá")
L.append(True)
print(L)


L=['a','b']
print(L)
L = L + ['c','d'] #função adicionar lista
print(L)


#função unir listas
L=[1,2,3]
L.extend([4,5,6])
print(L)
del L[0] #função deletar elemento da lista
print(L)
del L[2:] #deleta partes inteiras de uma lista
print(L)


L=['a','b','c']
print(L.remove('c')) #remove a partir de um valor
print(L)


#Estruturas de Dados: Sets
valores = {1,2,3,4,5,6}
print(valores)

#inserir novos dados
valores.add(6)
valores.add(7)
valores.add(8)
print(valores)

#remover dados
valores.remove(6) #apaga de acordo com o valor
print(valores)

if 4 in valores:
  print("4 existe no conjunto")
else:
  print("4 não existe no conjunto")


  #operações entre conjuntos/sets
A = {1,2,3,4}
B = {4,5,6,7}
print(A)
print(B)

print(A | B)#união
print(A & B)#intersecção
print(A - B)#diferença
print(A ^ B)#diferença simétrica



#usando funções para manipular sets
print(A.union(B))#união de conjuntos
print(A.intersection(B))#intersecção de conjuntos
print(A.difference(B))#diferença de conjuntos


#função sem parâmetro
def msg_boasvindas():
  print("olá, seja bem-vindo ao curso de Python!")

msg_boasvindas()


#função com parâmetro obrigatório
def msg(texto):
  print(texto)

msg("Olá, turma de algoritimo e programação FTG2024!")
msg("Olá, mundo da programação!")


#função com parâmetro opcional
def media(lista, imprime=False):
  soma=sum(lista)
  if imprime:
    print(f"A soma é {soma:.2f}")

  media=soma/len(lista)
  if imprime:
    print(f"A média é {media:.2f}")

  return media

Lista=[2,4,6,3,1,8,9,6,7,44,23,6,5,234,7,6,234]
print(media(Lista))
print("**************")
print(media(Lista,imprime=True))


#função passando parâmetros nomeados
def mensagem(nome,idade):
  print(f"Bem-vindo(a){nome.upper()}")
  print(f"Sua idade atual é de {idade} anos")

mensagem(idade=120,nome="Alan Turing")
mensagem(nome="Ada Lovelace",idade=240)


#jogo da advinhação

#usando bibliotecas nativas python
from random import randint
random=randint(1,100)

#inicia o código do jogo
print("\n Boas-vindas! Vamos jogar um game de advinhação?")
print("Advinhe qual o número escolhido pelo computador entre 1 e 100 tentativas. \n")

tentativa=1
while tentativa <=11:
  print(f"Tentativa {tentativa} de 10")
  numero = int(input("Digite seu palpite:"))
  if numero > random:
    print("Você errou! Dica: seu palpite foi maior")
  elif numero < random:
    print("Você errou! Dica: seu palpite foi menor")
  else:
    print(f"Parabéns! Você acertou em {tentativa} tentativas!")
    break
  tentativa=tentativa+1
else:
  print(f"Você ultrapassou o número de tentativas! O número era {random}")
#fim do jogo