class Carros:
    nome=""
    marca=""
    vel_max=0
    pot=0
    ligado=False

    def __init__(self,nome,marca,vel_max,pot,ligado):
        self.nome=nome 
        self.marca=marca
        self.vel_max=vel_max
        self.pot=pot
        self.ligado=ligado

    def exibir(self):
        print("Nome_________________: ",self.nome)
        print("Modelo_______________: ",self.marca)
        print("Velocidade Máxima____: ",self.vel_max)
        print("Potência (Em cavalos): ",self.pot)
        self.ligado = "Sim" if self.ligado else "Não"
        print("Véiculo ligado?______:", self.ligado)

    def ligar(self):
            if self.ligado == False:
                self.ligado = True
            elif self.ligado == True:
                print("Carro já está ligado")
    
    def desligar(self):
        if self.ligado == True:
            self.ligado = False
        elif self.ligado == False:
            print("Carro já está desligado")
