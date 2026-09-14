def numero_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print("Bem-vindo ao verificador de números primos!")
n = int(input("Digite um número inteiro positivo: "))
if numero_primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
repeat = input("Deseja verificar outro número? (s/n): ")
while repeat.lower() == "s":
    n = int(input("Digite um número inteiro positivo: "))
    if numero_primo(n):
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")
    repeat = input("Deseja verificar outro número? (s/n): ")
