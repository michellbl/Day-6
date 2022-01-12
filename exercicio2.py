#Crie um programa que mostre na tela
#todos os números PARES que estão no intervalo
#entre 1 e 50.

pares = 0
for n in range(1, 51):
#pares recebe n mod 2, se o resultado é zero, então ele é par
    pares = n % 2
    if pares == 0:
        print(n)