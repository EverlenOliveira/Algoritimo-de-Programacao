nome_curso="Curso de Python"
maiuscula=nome_curso.upper()
print(maiuscula)
minuscula=nome_curso.lower()
print(minuscula)
texto="PRODUTO-CAFÉ-FUTURO-2024"
separado=texto.split("-")
print(separado)
texto2="Eu vou no shopping Metropóle"
substituido=texto2.replace("shopping Metropóle", "Veropa")
print(substituido)

print("=================================================================")

frase = "O rato roeu a roupa do rei de Roma"
print(frase.count(''))#Resposta1
print(frase.upper())#Resposta2
print(frase.replace('R','g'))#Primeira solução Resposta3
pos=frase.find('r')#segunda solução resposta3
print(pos)
print(frase[:pos]+'g'+frase[pos+1:])