#variaveis
i = 0
j = 0
vet = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

#algoritimo
for i in range(0,5,1):
    for j in range(0,5,1):
        vet[i][j] = int(input(f"Informe o número para a posição {i+1},{j+1}: "))

print("\nMatriz total!!!")

for i in range(0,5,1):
    for j in range(0,5,1):
            print(f"[{vet[i][j]}]", end= "      ")
            if(j==4):
                print()
print("\nDiagonal principal!!!")

for i in range(0,5,1):
    for j in range(0,5,1):
        if(i == j):
            print(f"[{vet[i][j]}]", end= "      ")
            if(j==4):
                print()
        else:
            print("      ", end= "      ")
            if(j==4):
                print()