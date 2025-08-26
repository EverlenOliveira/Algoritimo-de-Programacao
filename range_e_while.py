i=0
while (i<=10):
 print(2)
i=i+1


controle=''

while (controle != 's'):
  print("p -Pagar")
  print("r - Receber")
  print("c - Consultar")
  print("s - Sair")
  controle=input("Digite a opção desejada:")

print('loop encerrado')


controle=''

while (controle != 'sim'):
  print("s - sim")
  print("n - não")
  controle=input("Quer namorar comigo?")

print('resposta certa, te amo')


for i in "Everlen e Radja":
  print(i)


num = 1
while num !=0:
  num = int(input("Digite um número:"))


print("Responda as perguntas com sim ou não")
print("s - sim")
print("n - não")
resposta1=input("Telefonou para a vítima?")
resposta2=input("Esteve no local do crime?")
resposta3=input("Mora perto da vítima?")
resposta4=input("Devia para a vítima?")
resposta5=input("Já trabalhou com a vítima?")

soma=0
if resposta1 == 's':
  soma=soma+1
if resposta2 == 's':
  soma=soma+1
if resposta3 == 's':
  soma=soma+1
if resposta4 == 's':
  soma=soma+1
if resposta5 == 's':
  soma=soma+1

if soma == 2:
 print("Você é o suspeito")
elif soma == 3 or soma == 4:
 print("Você é cúmplice")
elif soma == 5:
  print("Você é o assassino")
else:
  print("Você é inocente")


print("Responda s(sim) e n(não) para as próximas perguntas")
#declaramos uma váriavel set - coleção de perguntas
perguntas = ("Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?")
#inicializamos uma váriavel lista que irá acumular as respostas
respostas = []
for pergunta in perguntas:
   respostas.append(input(pergunta))
#inicializo uma váriavel int para contar as respostas sim
classificacao=0
for resposta in respostas:
  if resposta == 's':
    classificacao=classificacao+1
if (classificacao == 2):
  print("Você é suspeito")
elif (classificacao == 3 or clasificacao == 4):
  print("Você é cúmplice")
elif (classificacao == 5):
  print("Você é o assassino")
else:
  print("Você é inocente!")
