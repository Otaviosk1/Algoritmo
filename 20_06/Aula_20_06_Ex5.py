#variaveis
i = 0
j = 0
vet = [[0]*3, [0]*3, [0]*3]

#algoritimo
for i in range(0,3,1):
    for j in range(0,3,1):
        vet[i][j] = int(input(f"Informe o número para a posição {i+1},{j+1}: "))
print()
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"O número digitado na posição {i+1},{j+1}: {vet[i][j]} ")