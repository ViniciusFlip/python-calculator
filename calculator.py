#obctive to create a smart calculator using python

def show_menu(): 
    print('/n===Calculadora Smart Python ===')
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")


def sum(a,b):
    return a + b

def subtraction(a,b):
    return a - b
 
def multiplication(a,b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b



while True:

    show_menu()

    opcao=input("Escolha uma opção:")

    if opcao == 0:
        print('Encerrando calculadora')
        break

    if opcao not in ["1","2","3","4"]:
        print("opção inválida") 
        continue

    num1=float(input("Digite o primeiro número:"))
    num2=float(input("Digite o segundo número:"))


    if opcao == "1":
       resultado = sum(num1,num2)
    

    if opcao == "2":
       resultado = subtraction(num1, num2)

    if opcao == "3":
       resultado = multiplication(num1, num2)

    if opcao == "4":
       resultado = division(num1, num2)

    print("resultado", resultado)