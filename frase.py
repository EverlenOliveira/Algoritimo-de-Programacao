frase = "Disciplina de Algoritimo e Programação"
print(frase.count('o'))
print(frase.count('a'))
print(frase.upper())
print(len(frase))
print(frase.find('Algoritimo'))
print(frase.replace("Algoritimo e Programação","Geoprocessamento"))

print("=====================================================")

frase = "Disciplina de Algoritimo e Programação"
print(frase[3])
print(frase[:15])
print(frase[7:18])

print("=====================================================")

palavra1=input("Digite uma palavra:")
palavra2=input("Digite outra palavra:")

print(f"As palavras digitadas foram {palavra1} e {palavra2}")

comp1=len(palavra1)
comp2=len(palavra2)

print(f"O comprimento das palavras é {comp1} e {comp2}")

print("=====================================================")

frase = "O rato roeu a roupa do rei de Roma"
tamanho = len(frase)
print(tamanho)
print(frase.upper())
print(frase.replace('R','g'))