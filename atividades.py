#Questão 1
menor = float('inf')
maior = float('-inf')
soma = 0

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num

    if num < menor:
        menor = num
    if num > maior:
        maior = num

media = soma / 10

print("\n=== RESULTADOS ===")
print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")








#Questão 2
n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))
n3 = float(input("Digite a nota da terceira prova: "))

if (n1 >= 0.0 and n1 <= 10.0) and (n2 >= 0.0 and n2 <= 10.0) and (n3 >= 0.0 and n3 <= 10.0):
  media = (n1*2 + n2*3 + n3*5) / (2+3+5)
  if media >= 7:
    print("Você foi Aprovado,parabéns!!!! ")
  else:
    print("Você foi Reprovado")
else:
  print("Notas digitadas não são válidas, por favor, digite notas entre 0 a 10.")












# Inicializa as variáveis
menor = float('inf')  # Começa com infinito positivo para garantir que qualquer número será menor
maior = float('-inf') # Começa com infinito negativo para garantir que qualquer número será maior
soma = 0  # Acumulador para a soma

# Loop para ler os 10 números
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))  # Permite números decimais também
    soma += num  # Soma os valores

    # Atualiza o menor e maior número
    if num < menor:
        menor = num
    if num > maior:
        maior = num

# Calculando a média
media = soma / 10

# Exibe os resultados
print("\n=== RESULTADOS ===")
print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")










