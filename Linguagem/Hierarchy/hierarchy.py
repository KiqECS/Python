
class Pessoa():
    def __init__(self,nome_C,data_Nasc,nome_P,nome_M):
        self.nome_C = nome_C
        self.data_Nasc = data_Nasc
        self.nome_P = nome_P
        self.nome_M = nome_M
    """
    def show(self):
        print("Nome: " + self.nome_C)
        print("Data de Nascimento: " + self.data_Nasc)
        print("Nome do Pai " + self.nome_P)
        print("Nome da Mãe " + self.nome_M)
    """

class PessoaF(Pessoa):
    def __init__(self,nome_C,data_Nasc,nome_P,nome_M,cpf):
        self.cpf = cpf
        super().__init__(nome_C,data_Nasc,nome_P,nome_M)
    def show(self):
        print("-------------------------------------------------")
        print("Nome: " + self.nome_C)
        print("Data de Nascimento: " + self.data_Nasc)
        print("Nome do Pai: " + self.nome_P)
        print("Nome da Mãe: " + self.nome_M)
        print("CPF: " + self.cpf)
        print("-------------------------------------------------")
    
class PessoaJ(Pessoa):
    def __init__(self, nome_C, data_Nasc, nome_P, nome_M,cnpj):
        self.cnpj = cnpj
        super().__init__(nome_C, data_Nasc, nome_P, nome_M)
    def show(self):
        print("-------------------------------------------------")
        print("Nome: " + self.nome_C)
        print("Data de Nascimento: " + self.data_Nasc)
        print("Nome do Pai: " + self.nome_P)
        print("Nome da Mãe: " + self.nome_M)
        print("CNPJ: " + self.cnpj)
        print("-------------------------------------------------")
    
def form(f_or_j):
    if f_or_j == "J":
        nome_C = input("Digite o seu Nome Completo: ")
        data_Nasc = str(input("Sua data de nascimento: "))
        nome_P = input("O nome do seu Pai: ")
        nome_M = input("O nome da sua Mãe: ")
        cnpj = str(input("Digite o seu CNPJ: "))
        PessoaJ(nome_C,data_Nasc,nome_P,nome_M,cnpj).show()
    elif f_or_j == "F":
        nome_C = input("Digite o seu Nome Completo: ")
        data_Nasc = str(input("Sua data de nascimento: "))
        nome_P = input("O nome do seu Pai: ")
        nome_M = input("O nome da sua Mãe: ")
        cpf = str(input("Digite o seu CPF: "))
        PessoaF(nome_C,data_Nasc,nome_P,nome_M,cpf).show()

f_or_j = input("Você é Pessoa Juridica ou Fisica? [J/F]:  ")
form(f_or_j)
