def primo(num, divisor=2):
    if num < 2:
        return False
    if divisor > int(num**0.5):
        return True
    if num % divisor == 0:
        return False
    return primo(num, divisor+1)

def primoRecursivo(n):
    def gerarPrimos(current=2):
        if current > n:
            return []  
        elif primo(current):
            return [current] + gerarPrimos(current+1)
        else:
            return gerarPrimos(current+1)

    return gerarPrimos()
    
def primoLinear(n):
    primos = []
    for i in range(1, n+1):
        if (primo(i)):
            primos.append(i)
    return primos

while True:
    print("Numeros primos até N")
    print("1 -> Forma Recursiva")
    print("2 -> Forma Sequencial")
    print("0 -> Sair do Programa")

    a = int(input("> "))

    match a:
        case 1:
            n = int(input("Escolha um numero: "))
            print(primoRecursivo(n))
        case 2:
            n = int(input("Escolha um numero: "))
            print(primoLinear(n))
        case 0:
            break
        case _:
            print("Digite um numero valido")



