class Livros:
    pag = 0
    capa_Dura = False
    cordinha = False
    cor = ""

    def __init__(self,pag,capa_Dura,cordinha,cor):
        self.pag = pag
        self.capa_Dura = capa_Dura
        self.cordinha = cordinha 
        self.cor = cor
    
    def exibir(self):
        print("Páginas: " + str(self.pag))
        capa_Dura = "Sim" if self.capa_Dura else "Não"
        print("Capa dura: " + capa_Dura)
        cordinha = "Sim" if self.cordinha else "Não"
        print("Cordinha para marcação: " + cordinha)
        print("Cor: " + self.cor)

    def mudaP(self):
        print("Digite o número de páginas: ")
        self.pag = int(input())
        

print("\nData Science do Zero\n")
Data_Science_do_Zero = Livros(328,False,False,"Branco")
Data_Science_do_Zero.exibir()
c_mudaP = input("Deseja mudar o número de paginas ? [s/n]: ")
if c_mudaP == 'S' or c_mudaP == 's':
    Data_Science_do_Zero.mudaP()
    Data_Science_do_Zero.exibir()

print("\nFundação: A Trilogia\n")
Fundacao = Livros(850,True,True,"Branco")
Fundacao.exibir()
c_mudaP = input("Deseja mudar o número de paginas ? [s/n]: ")
if c_mudaP == 'S' or c_mudaP == 's':
    Fundacao.mudaP()
    Fundacao.exibir()