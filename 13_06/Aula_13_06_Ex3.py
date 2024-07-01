#variaveis
idade = 0
soma_idade = 0
media_idade = 0.0
sexo = ""
maioridade = 0
femi = 0
contador = 0

#algoritimo

for contador in range(1,4,1):
    idade = int(input("Insira a idade do aluno: "))
    sexo = input("Insira o sexo do aluno - Masculino ou Feminino: ")

    soma_idade += idade

    if(sexo.upper() == "FEMININO"):
        femi += 1
    if(idade >= 18):
        maioridade += 1

print("Número total de vagas atingido!!!")

media = soma_idade/3
print(f"Idade média dos participantes: {media}")
print(f"Quantidade de mulheres inscritas: {femi}")
print(f"Quantidade de candidatos maiores de idade: {maioridade}")