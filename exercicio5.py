#Desenvolva um programa que leia seis
#numeros inteiros e mostre a soma apenas
#daqueles que forem pares. Se o valor
#digitado for impar, desconsidere-o.

lista_numeros = []

for i in range(0,3):
    numero = int(input("Digite: "))
    if numero % 2 == 0:
        lista_numeros.append(numero)

soma_lista = sum(lista_numeros)

print(soma_lista)