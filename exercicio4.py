#Refaça o desafio 009, mostrando a tabuada de um número
#que o usuário escolher, só que agora
#utilizando um laço for.

number = int(input("Digite um numero para saber a tabuada: \n"))

for c in range(0,11):
    result = number * c
    print(f"{number} x {c} = {result}")