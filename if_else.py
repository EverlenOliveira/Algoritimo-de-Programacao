idade=int(input("Digite sua idade:"))
matricula=input("Está matriculado? (1-SIM, 2-NÃO)")
if (idade>=18)and(matricula=="1"):
  print("Você esta matriculado!")
else:
    print("Você não matriculou.")

    print("=====================================================")

    numero1=int(input("Digite o primeio número:"))
numero2=int(input("Digite o segundo número:"))
if numero1<numero2:
 print("O menor número é", numero1)
else:
 print("O menor número é", numero2)

 print("=========================================================")

 idade=int(input("Digite sua idade:"))
matricula=input("Está matriculado? (1-SIM, 2-NÃO)")
if (idade>=18)and(matricula=="1"):
  print("Você esta matriculado!")
else:
    print("Você não matriculou.")

 print("=========================================================")

    numero =int(input("Digite um número: "))
if numero % 2 == 0: #bloco principal onde verificamos se o número é par
 print("O número é par.")
 if numero < 100: #bloco interno que compara o número digitado com 100
  print("O número é menor que 100.")
 else:
  print("O número é maior que 100.")
else: #bloco pricipal onde verificamos se o número é ímpar
 print("O número é ímpar.")
 if numero < 100: #bloco interno que compara o número digitado com 100
  print("O número é menor que 100.")
 else:
  print("O número é maior que 100.")

print("=========================================================")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

if (nota1 >= 0.0 and nota1 <= 10.0) and (nota2 >= 0.0 and nota2 <= 10.0) and (nota3 >= 0.0 and nota3 <= 10.0) and (nota4 >= 0.0 and nota4 <= 10.0):
  media = (nota1 + nota2 + nota3 + nota4) / 4
  if media >= 5:
    print("Aprovado")
  else:
    print("Reprovado")
else:
  print("Notas digitadas não são válidas")


  

