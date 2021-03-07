"""
cont = 0
while (cont < 2000):
    print("Vários números " + str(cont))
    cont+=1
print("Fim da porra toda")
"""
"""
comidas = ['Arroz', 'Feijão', 'Batata']
tamanho = len(comidas)
i = 0
while (i < tamanho):
    print(comidas[i])
    i+=1
"""
frutas = []
fruta = input("Digite uma fruta: ")
while (fruta != "Tomate"):
    frutas.append(fruta)
    fruta = input("Digite uma fruta: ")
print("Está porra não é uma fruta!!!")
print("Estás são as frutas que você adicionou!!")
for f in frutas:
    print(f)
