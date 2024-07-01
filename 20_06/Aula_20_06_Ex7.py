#variavies
n1 = 0
n2 = 0
resultado = 0

#função
def somar_numeros(num1,num2):
    resultado = num1+num2
    return resultado

#algoritimo principal
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
print(f"A soma dos números é: {somar_numeros(n1,n2)}")

