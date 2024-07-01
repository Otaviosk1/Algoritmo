#variaveis
vet = [0]*5
i = 0

#algoritimo

for i in range(0,5,1):
    vet[i] = int(input("Digite um número: "))

for i in range(0,5,1):
    print(f"[{vet[i]}]", end='  ')


