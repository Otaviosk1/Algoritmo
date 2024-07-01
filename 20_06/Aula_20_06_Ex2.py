#variaveis
vet = [0]*10
i = 0

#algoritimo

for i in range(0,10,1):
    vet[i] = int(input("Digite um número: "))

for i in range(9,-1,-1):
    print(f"[{vet[i]}]", end='  ')


