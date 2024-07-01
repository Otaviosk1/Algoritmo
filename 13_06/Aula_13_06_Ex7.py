#variaveis
escolha_canal = 1
canal9 = 0
canal12 = 0
canal23 = 0
canal40 = 0
canal_outro = 0
soma_canal = 0
porcentagem_canal9 = 0.0
porcentagem_canal12 = 0.0
porcentagem_canal23 = 0.0
porcentagem_canal40 = 0.0
porcentagem_canal_outro = 0.0

#algoritimo

while escolha_canal != 0:
    escolha_canal = int(input("Digite o número do canal escolhido(9 | 12 | 23 | 40)): "))

    if(escolha_canal == 9):
        canal9 += 1
    elif(escolha_canal == 12):
        canal12 += 1
    elif(escolha_canal == 23):
        canal23 += 1
    elif(escolha_canal == 40):
        canal40 += 1
    elif(escolha_canal != 0):
        canal_outro += 1

soma_canal = (canal12+canal9+canal23+canal40+canal_outro)

    
porcentagem_canal9 = (canal9/soma_canal)*100
porcentagem_canal12 = (canal12/soma_canal)*100
porcentagem_canal23 = (canal23/soma_canal)*100
porcentagem_canal40 = (canal40/soma_canal)*100
porcentagem_canal_outro = (canal_outro/soma_canal)*100

print(f"Audiência Canal 9: {porcentagem_canal9:,.2f}")
print(f"Audiência Canal 12: {porcentagem_canal12:,.2f}")
print(f"Audiência Canal 23: {porcentagem_canal23:,.2f}")
print(f"Audiência Canal 40: {porcentagem_canal40:,.2f}")
print(f"Audiência de outros canais: {porcentagem_canal_outro:,.2f}")