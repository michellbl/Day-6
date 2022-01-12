#Faça um programa que calcule a soma
#entre todos os numeros impares que são
#multiplos de três e que se encontram no
#intervalo de 1 até 500.

multi_tres = 0
soma = 0

for n in range (1,500):
#o resto de n mod 3 é zero
    multi_tres = n % 3
    if multi_tres == 0:
        print(n)
        soma +=n
print(f"A soma de todos os numeros é: {soma}")
    