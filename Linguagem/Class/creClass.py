class Livros:
    pag = 0
    capa_dura = False
    cordinha = False
    cor = ""

Data_Science_do_Zero = Livros()
Fundacao = Livros()

print("\n\bData Science do Zero\b\n")
Data_Science_do_Zero.pag = 328
capa_D = "Sim" if Data_Science_do_Zero.capa_dura else "Não"
Data_Science_do_Zero.capa_dura = capa_D
corda = "Sim" if Data_Science_do_Zero.cordinha else "Não"
Data_Science_do_Zero.cordinha = corda
Data_Science_do_Zero.cor = "Branco"

print("Páginas: " + str(Data_Science_do_Zero.pag))
print("Capa dura: " + str(Data_Science_do_Zero.capa_dura))
print("Cordinha para marcação: " + str(Data_Science_do_Zero.cordinha))
print("Cor: " + Data_Science_do_Zero.cor)

print("\n\bFundação: A Trilogia\b\n")
Fundacao.pag = 850
capa_D = "Sim" if Data_Science_do_Zero.capa_dura else "Não"
Fundacao.capa_dura = capa_D
corda = "Sim" if Data_Science_do_Zero.cordinha else "Não"
Fundacao.cordinha = corda
Fundacao.cor = "Branco"

print("Páginas: " + str(Fundacao.pag))
print("Capa dura: " + str(Fundacao.capa_dura))
print("Cordinha para marcação: " + str(Fundacao.cordinha))
print("Cor: " + Fundacao.cor)