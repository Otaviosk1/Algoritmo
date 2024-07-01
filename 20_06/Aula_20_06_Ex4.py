#variaveis
i=0
vet = [0.0]*6


for i in range(1,6,1):
    vet[i] = int(input("Digite um número: "))

for i in range(1,6,1):
        if(i % 2 == 0):
            print(f"[{vet[i]*1.02}]")
        else:
            print(f"[{vet[i]*1.05}]")