# Crie um algoritmo que leia 3 valores (lados de um triângulo)
# Determine se formam um triângulo
# Se é um equilátero, isósceles ou escaleno

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 + valor2 > valor3 and valor2 + valor3 > valor1 and valor1 + valor3 > valor2:
    if valor1 == valor2 and valor2 == valor3:
        situacao = "Equilátero"
    elif valor1 == valor2 or valor2 == valor3 or valor1 == valor3:
        situacao = "Isósceles"
    else:
        situacao = "Escaleno"
    print (f"Seus valores formam um triângulo. E seu triângulo é {situacao}")
else:
    print (f"Seus valores não formam um triângulo.")