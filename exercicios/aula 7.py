class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade} km/h")

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0

    def status(self):
        return f"marca: {self.marca} -modelo: {self.modelo} ({self.ano}) - Velocidade: {self.velocidade} km/h"


class Carro(veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia


class bicicleta(veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f"marca: {self.marca} -modelo: {self.modelo} ({self.ano}) - Tipo: {self.tipo} - Velocidade: {self.velocidade} km/h"


carro1 = Carro("Ford", "Mustang", 2022, 300)
bicicleta1 = bicicleta("Caloi", "Elite", 2021, "Mountain Bike")
carro1.acelerar(50)
bicicleta1.acelerar(20)
print("Status do carro:")
print(carro1.status())
print("\nStatus da bicicleta:")
print(bicicleta1.status())
