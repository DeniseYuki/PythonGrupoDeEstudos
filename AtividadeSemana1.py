
# Atividades 1 semana

# 1- Solicita que o usuário digite dois números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))



# 2- Calcula a soma, subtração, multiplicação e divisão
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2



# 3- Imprime na tela os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)



# 4- Verifica se o primeiro número é maior, menor ou igual ao segundo número
if num1 > num2:
    print("O primeiro número é maior que o segundo.")
elif num1 < num2:
    print("O primeiro número é menor que o segundo.")
else:
    print("Os números são iguais.")



# 5- Cria uma lista com 5 elementos de tipos diferentes

lista = [10, "Python", True, 3.14, [1, 2, 3]]

# Imprime na tela o tipo de dado de cada elemento
for elemento in lista:
    print(type(elemento))

# Imprime na tela apenas os elementos que são do tipo string
for elemento in lista:
    if isinstance(elemento, str):
        print(elemento)
