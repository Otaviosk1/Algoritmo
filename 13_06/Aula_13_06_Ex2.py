#variaveis
num_pessoas = 0
contador = 0
idade = 0
idade_maior = 0
idade_menor = 0
idade_total = 0
media = 0.0

#algoritimo

num_pessoas = int(input("Insira o número de pessoa que deseja: "))

for contador in range(0,num_pessoas,1):
    idade = int(input("Insira a idade: "))
    idade_total += idade

    if(contador == 0):
        idade_maior = idade
        idade_menor = idade

    else:
        if(idade_maior < idade):
            idade_maior = idade

        if(idade_menor > idade ):
            idade_menor = idade


media = (idade_total/num_pessoas)

print(f"A média de idade de {num_pessoas} pessoas é {media:,.2f}")
print(f"A maior idade é {idade_maior}")
print(f"A menor idade é {idade_menor}")
