


print("\n BÁSICO \n")

#variáveis, operadores
a = 10
b = 5
print("A soma de a + b = ",a+b)
print("A soma de a - b = ",a-b)
print("A soma de a * b = ",a*b)
print("A soma de a / b = ",a/b)
print("resto da divisão  de a e b : ",a%b)


print("\n ESTRUTURA CONDICIONAL \n")

# estruturas condicionais
# simples
x = 10
if x > 5:
    print("x é maior do que 5")
#if e else
y = 2
if y > 5:
    print("y é maior do que 5")
else:
    print("y é menor ou igual a 5")
#if e elif
z = 7
if z > 10:
    print("z é maior do que 10")
elif z > 5:
    print("z é maior do que 5, mas menor ou igual a 10")
else:
    print("z é menor ou igual a 5")


print("\n ESTRUTURA DE REPETIÇÃO \n")
#FOR
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

print("\n WHILE \n")
#WHILE
i = 0
while i < 5:
    print(i)
    i += 1

print("\n WHILE E IF \n")
#WHILE ESTRUTURADO
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
    if i == 8:
        break

