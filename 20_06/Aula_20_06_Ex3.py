#variaveis
i=0
vet = [0.0]*6

for i in range(0,6,1):
    vet[i] = float(input("Digite um número: "))

for i in range(0,6,2):
        print(f"[{vet[i]}]", end='  ')

'''for i in range(1,7,1):
    if(i % 2 != 0):
        print(f"[{vet[i]}]", end='  ')'''