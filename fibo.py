def fiboRecursivo(n):
    return fiboRecursivo(n-1) + fiboRecursivo(n-2) if n > 1 else n

def fiboLinear(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        c = a + b
        a, b = b, c
    return b if n > 0 else 0


while True:
    print("1 -> Fibonacci Recursiva")
    print("2 -> Fibonacci Sequencial")
    print("0 -> Sair do Programa")

    a = int(input("> "))

    match a:
        case 1:
            n = int(input("Escolha um numero: "))
            print(fiboRecursivo(n))
        case 2:
            n = int(input("Escolha um numero: "))
            print(fiboLinear(n))
        case 0:
            break
        case _:
            print("Digite um numero valido")



